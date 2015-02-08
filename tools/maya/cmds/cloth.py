import math
from tools.maya.cmds import rigg
from tools.maya.cmds import modeling as mode
try:
    import maya.cmds as mc
except:
    pass


def hideParticleAttrs(node):
    """ Hides the particle attributes for the given nCloth/nRigid node,
        so they won't show up in the channel box
        :param node: nCloth or nRigir node name
        :type node: str """
    attrs = ['dieOnEmissionVolumeExit', 'lifespanMode', 'lifespanRandom', 'expressionsAfterDynamics',
             'dynamicsWeight', 'forcesInWorld', 'conserve', 'emissionInWorld', 'maxCount', 'levelOfDetail',
             'inheritFactor', 'currentTime', 'startFrame', 'inputGeometrySpace', 'enforceCountFromHistory',
             'targetGeometrySpace', 'goalSmoothness', 'cacheData', 'traceDepth', 'particleRenderType']
    for attr in attrs:
        mc.setAttr('%s.%s' % (node, attr), k=False, cb=False)

def hideAllParticleAttrs():
    """ Hide the particle attrs for all the nBase nodes in the scene """
    shapes = mc.ls(type='nBase')
    if shapes:
        for shape in shapes:
            hideParticleAttrs(shape)

def getDefaultThickness(mesh, clothFlags=False, maxRatio=0.005, thicknessCoef=0.13, minWidth=0.0001):
    """ Try to find a reasonnable thickness for given mesh
        :param mesh: Shape name
        :type mesh: str
        :param clothFlags: Enable clothFlags return
        :type clothFlags: bool
        :param maxRatio: Ratio of width to bounding box size
        :type maxRatio: float
        :param thicknessCoef: Default thickness coef
        :type thicknessCoef: float
        :param minWidth: Min width for precision issues
        :type minWidth: float
        :return: Thicknass value, ClothFlags dict
        :rtype: float | dict """
    #-- Get mesh info --#
    bboxDict = mode.getBboxInfoFromMesh(mesh)
    numFaces = mc.polyEvaluate(mesh, face=True)
    objSize = math.sqrt(bboxDict['surfaceArea'])
    newWidth = (objSize * maxRatio)
    clothFlagsDict = {'selfCollisionFlag': None, 'selfCollideWidthScale': None, 'thickness':None, 'pushOutRadius': None}
    #-- Try to find default thickness --#
    if numFaces:
        estimatedEdgeLength = math.sqrt(bboxDict['surfaceArea'] / numFaces)
        thickness = (thicknessCoef * estimatedEdgeLength)
        if thickness > newWidth:
            clothFlagsDict['selfCollisionFlag'] = 3
        else:
            clothFlagsDict['selfCollideWidthScale'] = 3
            newWidth = thickness
    if newWidth < minWidth:
        newWidth = minWidth
    clothFlagsDict['thickness'] = newWidth
    clothFlagsDict['pushOutRadius'] = (newWidth * 4.0)
    #-- Result --#
    if clothFlags:
        return newWidth, clothFlagsDict
    return newWidth

def createNucleus():
    """ Create a new nucleus node connected to scene time
        :return: Nucleus node name
        :rtype: str """
    nucleus = mc.createNode('nucleus')
    mc.connectAttr('time1.outTime', '%s.currentTime' % nucleus)
    axe = mc.upAxis(q=True, ax=True)
    if axe == 'x':
        mc.setAttr('%s.gravityDirection' % nucleus, -1, 0, 0)
    elif axe == 'y':
        mc.setAttr('%s.gravityDirection' % nucleus, 0, -1, 0)
    elif axe == 'z':
        mc.setAttr('%s.gravityDirection' % nucleus, 0, 0, -1)
    return nucleus

def createNSystem():
    """ If there is a nucleus node selected, return it, else, create a new one and return it
        :return: Nucleus node name
        :rtype: str """
    selected = mc.ls(sl=True)
    nSys = mc.listRelatives(selected, type='nucleus')
    if not nSys:
        return createNucleus()
    else:
        return nSys[0]

def addActiveToNSystem(active, nucleus):
    """ Connect nCloth or nRigid to given nucleus
        :param active: nCloth or nRigid node
        :type active: str
        :param nucleus: Nucleus node
        :type nucleus: str
        :return: InputActive attribute index
        :rtype: int """
    ind = rigg.getNextFreeMultiIndex('%s.inputActive' % nucleus)
    mc.connectAttr('%s.currentState' % active, '%s.inputActive[%s]' % (nucleus, ind))
    mc.connectAttr('%s.startState' % active, '%s.inputActiveStart[%s]' % (nucleus, ind))
    mc.connectAttr('%s.outputObjects[%s]' % (nucleus, ind), '%s.nextState' % active)
    mc.setAttr('%s.active' % active, True)
    return ind


class GetActiveNucleusNode(object):
    """ Returns a nucleus node based on current selection, last referenced,
        last created, or dag order. """

    def __init__(self):
        self.activeNucleus = None

    def getActiveNucleus(self, selectExisting=False, createNew=False):
        """ Find the currently active nucleus node, if none found, execute kargs
            :param selectExisting: select the first existing one, if any
            :type selectExisting: bool
            :param createNew: force the creation of a new one
            :type createNew: bool
            :return: Active nucleus node
            :rtype: str """
        if self.findActiveNucleus() is None:
            if selectExisting:
                #-- Select an existing nucleus node, if there is one --#
                allNucleus = mc.ls(type='nucleus')
                if allNucleus:
                    self.activeNucleus = allNucleus[0]
                    return self.activeNucleus
            if createNew:
                #-- Force the creation of a new nucleus node --#
                self.activeNucleus = createNucleus()
        return self.activeNucleus

    def findActiveNucleus(self):
        """ We follow this order of checking for an active nucleus node
            1. explicitly selected nucleus
            2. explicitly selected nBase
            3. explicitly selected input or output mesh
            4. if active nucleus(global variable) use that
            5. use first nucleus in dag
            :return: Active nucleus node
            :rtype: str """
        #-- Check if any nucleus nodes already exist --#
        allNucleus = mc.ls(type='nucleus')
        if not allNucleus:
            self.activeNucleus = None
            return self.activeNucleus
        #-- Check if any nucleus nodes are selected --#
        nucleusNodes = mc.ls(sl=True, type='nucleus')
        if nucleusNodes:
            return self.pickBestNucleus(nucleusNodes)
        #-- Check if any cloth nodes are selected --#
        nBases = mc.ls(sl=True, type='nBase')
        if not nBases:
            #-- Look for cloth nodes indirectly selected through meshes --#
            meshes = mc.ls(sl=True, dag=True, type='mesh')
            for mesh in meshes:
                nBase = rigg.findTypeInHistory(mesh, ['nBase'], future=True, past=True)
                if nBase is not None:
                    nBases.append(nBase)
        if nBases:
            #-- Cloth nodes directly selected --#
            nBases = list(set(nBases))
            for nBase in nBases:
                startCon = mc.listConnections("%s.startState" % nBase, type='nucleus')
                nucleusNodes.append(startCon[0])
            if nucleusNodes:
                return self.pickBestNucleus(nucleusNodes)
        #-- Check nucleus nodes in dag --#
        if self.activeNucleus is not None:
            # Pick active if it still exists
            if not mc.objExists(self.activeNucleus):
                self.activeNucleus = None
        #-- Result --#
        return self.activeNucleus

    def pickBestNucleus(self, nucleusNodes):
        """ Choose best nucleus node
            :param nucleusNodes: Nucleus node list
            :type nucleusNodes: list
            :return: Best nucleus node
            :rtype: str """
        #-- Empty List --#
        if not nucleusNodes:
            self.activeNucleus = None
            return self.activeNucleus
        #-- One Nucleus --#
        nucleusNodes = list(set(nucleusNodes))
        if len(nucleusNodes) == 1:
            self.activeNucleus = nucleusNodes[0]
            return self.activeNucleus
        #-- Multiple Nucleus --#
        if self.activeNucleus is not None:
            for nucleus in nucleusNodes:
                if nucleus == self.activeNucleus:
                    print "!!! Warning: Multiple possible nucleus nodes: Will use %s" % self.activeNucleus
                    return self.activeNucleus
        #-- Result --#
        self.activeNucleus = nucleusNodes[0]
        print "!!! Warning: Multiple possible nucleus nodes: Will use %s" % self.activeNucleus
        return self.activeNucleus


class CreateNClothBeta(object):

    def __init__(self, useNucleus=None, selectExisting=False, createNewNucleus=False, worldSpace=False):
        #-- Store kwargs --#
        self.useNucleus = useNucleus
        self.selectExisting = selectExisting
        self.createNewNucleus = createNewNucleus
        self.worldSpace = worldSpace
        #-- Init --#
        self.selected = self._initSelection()
        self.meshes = self._initMeshes()
        self.outMeshName = 'outputCloth1'

    @staticmethod
    def _initSelection():
        """ Get Current selection
            :return: (list) : Selected objects """
        selected = mc.ls(sl=True)
        if not selected:
            raise IndexError, "!!! ERROR: No selection found !!!"
        return selected

    def _initMeshes(self):
        """ Get selected meshes
            :return: (list) : Selected meshes """
        meshes = mc.listRelatives(self.selected, f=True, ni=True, s=True, type='mesh')
        if not meshes:
            raise IndexError, "!!! ERROR: No shape found, check your selection !!!"
        return meshes

    def createNode(self):
        #-- Get Active Nucleus --#
        nuc = GetActiveNucleusNode()
        nucleus = nuc.getActiveNucleus(selectExisting=self.selected,
                                       createNew=self.createNewNucleus)
        #-- Create nCloth Nodes --#
        newClothNodes = []
        for mesh in self.meshes:
            conns = mc.listConnections(mesh, sh=True, type='nBase')
            if not conns:
                # This mesh has no nBase associated with it, connect it
                meshTforms = rigg.listTransforms(mesh)
                tForm = meshTforms[0]
                nCloth = mc.createNode('nCloth')
                hideParticleAttrs(nCloth)
                newClothNodes.append(nCloth)
                mc.connectAttr('time1.outTime', '%s.currentTime' % nCloth)
                # Check if this mesh is already being used as an input
                # to the driverPoints attribute of a wrap deformer
                wrapPlugs = mc.listConnections('%s.worldMesh' % mesh, d=True, p=True, sh=True, type='wrap')
                mc.connectAttr('%s.worldMesh' % mesh, '%s.inputMesh' % nCloth)
                # Create a mesh node, and hook it up as output
                if not self.worldSpace:
                    outMesh = mc.createNode('mesh', p=tForm, n=self.outMeshName)
                    mc.setAttr('%s.localSpaceOutput' % nCloth, True)
                else:
                    outMesh = mc.createNode('mesh', n=self.outMeshName)
                shadConns = mc.listConnections('%s.instObjGroups[0]' % mesh, d=True, sh=True, type='shadingEngine')
                if shadConns and not mc.about(batch=True):
                    mc.hyperShade(assign=shadConns[0]) # outMesh should be currently selected
                else:
                    mc.sets(outMesh, add=outMesh)
                mc.setAttr('%s.quadSplit' % outMesh, 0) # match nCloth quad tessellation
                mc.connectAttr('%s.outputMesh' % nCloth, '%s.inMesh' % outMesh)
                addActiveToNSystem(nCloth, nucleus)
                mc.connectAttr('%s.startFrame' % nucleus, '%s.startFrame' % nCloth)
                mc.setAttr('%s.intermediateObject' % mesh, 1)
                clothTforms = rigg.listTransforms(nCloth)
                mc.setAttr('%s.translate' % clothTforms[0], l=True)
                mc.setAttr('%s.rotate' % clothTforms[0], l=True)
                mc.setAttr('%s.scale' % clothTforms[0], l=True)
                # Try to pick a good default thickness
                thickness, clothFlagsDict = getDefaultThickness(mesh, clothFlags=True)
                for k, v in clothFlagsDict.iteritems():
                    if v is not None:
                        mc.setAttr('%s.%s' % (nCloth, k), v)
                # Now for each wrap deformer that was using the input surface as an input
                # to the driverPoints attribute, transfer the connection to the output surface.
                if wrapPlugs:
                    rigg.transfertWrapConns(wrapPlugs, outMesh)
        #-- Batch mode refresh --#
        if mc.about(batch=True):
            for cloth in newClothNodes:
                mc.getAttr('%s.forceDynamics' % cloth)
        #-- Result --#
        mc.select(newClothNodes)
        return newClothNodes

