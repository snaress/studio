import math
from tools.maya.util.proc import procRigg as pRigg
from tools.maya.util.proc import procModeling as pMode
try:
    import maya.cmds as mc
    import maya.mel as ml
except:
    pass


def getClothNodeFromSel():
    """ Try to find cloth nodes connected to selected objects
        :return: Cloth node names
        :rtype: list """
    clothNodes = []
    selected = mc.ls(sl=True)
    #-- Search Cloth Node --#
    for node in selected:
        clothNode = getClothNode(node)
        if clothNode:
            if not clothNode in clothNodes:
                clothNodes.append(clothNode)
    return clothNodes

def getClothNode(nodeName):
    """ Try to find cloth node connected to given object
        :param nodeName: Transform or Mesh node name
        :type nodeName: str
        :return: Cloth node name
        :rtype: str """
    clothNode = pRigg.findTypeInHistory(nodeName, ['nCloth', 'nRigid'], future=True, past=True)
    if clothNode:
        return clothNode

def getVtxMaps(clothNode):
    """ Get vertex map list from given clothNode
        :param clothNode: Cloth node name
        :type clothNode: str
        :return: Vertex map list
        :rtype: list """
    maps = []
    if mc.objExists(clothNode) and mc.nodeType(clothNode) in ['nCloth', 'nRigid']:
        attrs = mc.listAttr(clothNode)
        for attr in attrs:
            if attr.endswith("MapType"):
                mapName = attr.replace('MapType', '')
                maps.append(mapName)
    return maps

def getVtxMapType(clothNode, mapType):
    """ Get given clothNode vtxMap type
        :param clothNode: Cloth node name
        :type clothNode: str
        :param mapType: Cloth node vtxMap name (must ends with 'MapType')
        :type mapType: str
        :return: VtxMap type (0 = None, 1 = Vertex, 2 = Texture)
        :rtype: int """
    if mc.objExists(clothNode) and mc.nodeType(clothNode) in ['nCloth', 'nRigid']:
        return mc.getAttr("%s.%s" % (clothNode, mapType))

def setVtxMapType(clothNode, mapType, value):
    """ Set given clothNode vtxMap value
        :param clothNode: Cloth shape node name
        :type clothNode: str
        :param mapType: Cloth node vtxMap name (must ends with 'MapType')
        :type mapType: str
        :param value: VtxMap type (0 = None, 1 = Vertex, 2 = Texture)
        :type value: int
        :return: True if success, else False
        :rtype: bool """
    if mc.objExists(clothNode) and mc.nodeType(clothNode) in ['nCloth', 'nRigid']:
        mc.setAttr("%s.%s" % (clothNode, mapType), value)
        return True
    else:
        return False

def getVtxMapData(clothNode, vtxMap):
    """ Get vertex map influence per vertex
        :param clothNode: Cloth node name
        :type clothNode: str
        :param vtxMap: Vertex map name (must ends with 'PerVertex')
        :type vtxMap: str
        :return: Influence list per vertex
        :rtype: list """
    if mc.objExists(clothNode) and mc.nodeType(clothNode) in ['nCloth', 'nRigid']:
        return mc.getAttr("%s.%s" % (clothNode, vtxMap))

def setVtxMapData(clothNode, vtxMap, value, refresh=False):
    """ Set vertex map influence per vertex
        :param clothNode: Cloth node name
        :type clothNode: str
        :param vtxMap: Vertex map name (must ends with 'PerVertex')
        :type vtxMap: str
        :param value: Influence list per vertex
        :type value: list
        :param refresh: Refresh maya ui
        :type refresh: bool """
    if isinstance(value, list):
        mc.setAttr('%s.%s' % (clothNode, vtxMap), value, type='doubleArray')
        if refresh:
            mc.refresh()
    else:
        print "!!! WARNING: setVtxMapData(): Value arg should be a list !!!"

def getModelFromClothNode(clothNode):
    """ Get model from given clothNode
        :param clothNode: Cloth node name
        :type clothNode: str
        :return: Connected model
        :rtype: str """
    if mc.objExists(clothNode) and mc.nodeType(clothNode) in ['nCloth', 'nRigid']:
        model = mc.listConnections("%s.inputMesh" %clothNode, s=True)
        if model:
            return model[0]

def getModelSelectedVtx(clothNode, indexOnly=False):
    """ Get selected vertex on model
        :param clothNode: Cloth node name
        :type clothNode: str
        :param indexOnly: If True, return index only, else fullName
        :type indexOnly: bool
        :return: selection list
        :rtype: list """
    sel = mc.ls(sl=True) or []
    model = getModelFromClothNode(clothNode)
    selVtx = []
    for node in sel:
        if node.startswith(model) and node.endswith(']'):
            selName = node.split('.')[0]
            ind = node.split('.')[-1].replace('vtx[', '').replace(']','')
            if not ':' in ind:
                if indexOnly:
                    selVtx.append(int(ind))
                else:
                    selVtx.append("%s.vtx[%s]" % (selName, ind))
            else:
                deb = int(ind.split(':')[0])
                fin = int(ind.split(':')[1])
                for n in range(deb, (fin + 1), 1):
                    if indexOnly:
                        selVtx.append(n)
                    else:
                        selVtx.append("%s.vtx[%s]" % (selName, n))
    return selVtx

def selectVtxInfOnModel(clothNode, vtxMap, selMode, value=None, minInf=None, maxInf=None):
    """ Select vertex on model given by value or range
        :param clothNode: Cloth node name
        :type clothNode: str
        :param vtxMap: Vertex map name (must ends with 'PerVertex')
        :type vtxMap: str
        :param selMode: 'range' or 'value'
        :type selMode: str
        :param value: Influence value
        :type value: float
        :param minInf: Range minimum influence
        :type minInf: float
        :param maxInf: Range maximum influence
        :type maxInf: float """
    #-- Get Data --#
    data = getVtxMapData(clothNode, vtxMap)
    if data is not None:
        vtxSel = []
        model = getModelFromClothNode(clothNode)
        if model is not None:
            for n, val in enumerate(data):
                if selMode == 'range':
                    if minInf <= val <= maxInf:
                        vtxSel.append("%s.vtx[%s]" % (model, n))
                elif selMode == 'value':
                    if value == val:
                        vtxSel.append("%s.vtx[%s]" % (model, n))
        #-- Select Matching Values --#
        if vtxSel:
            mc.select(vtxSel, r=True)
        else:
            print "!!! WARNING: No matching values found !!!"

def paintVtxMap(clothNode, mapName):
    """ Enable maya vertex paint tool
        :param clothNode: Cloth node name
        :type clothNode: str
        :param mapName: Vertex map name
        :type mapName: str """
    if not mc.objExists(clothNode) and mc.nodeType(clothNode) in ['nCloth', 'nRigid']:
        print "!!! WARNING: ClothNode not found, or is not a cloth node: %s" % clothNode
    else:
        if not getVtxMapType(clothNode, '%sMapType' % mapName) == 1:
            print "!!! WARNING: Vertex map disabled !!!"
        else:
            model = getModelFromClothNode(clothNode)
            shape = mc.listRelatives(model, s=True, ni=True)
            if not shape:
                print "!!! WARNING: No shape found !!!"
            else:
                mc.select(shape[0], r=True)
                mc.hilite(model)
                ml.eval('setNClothMapType("%s","",1);' % mapName)
                ml.eval('artAttrNClothToolScript 3 %s;' % mapName)



def createNSystem():
    """ Create a new nucleus node
        :return: (str) : Nucleus node """
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

def addActiveToNSystem(active, nucleus):
    """ Connect nCloth or nRigid to given nucleus
        :param active: (str) : nCloth or nRigid node
        :param nucleus: (str) : Nucleus node
        :return: (int) : InputActive attribute index """
    ind = pRigg.getNextFreeMultiIndex('%s.inputActive' % nucleus)
    mc.connectAttr('%s.currentState' % active, '%s.inputActive[%s]' % (nucleus, ind))
    mc.connectAttr('%s.startState' % active, '%s.inputActiveStart[%s]' % (nucleus, ind))
    mc.connectAttr('%s.outputObjects[%s]' % (nucleus, ind), '%s.nextState' % active)
    mc.setAttr('%s.active' % active, True)
    return ind

def hideParticleAttrs(node):
    """ Hides the particle attributes for the given nCloth/nRigid,
        so they won't show up in the channel box
        :param node: (str) : nCloth or nRigir node name """
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
        :rtype: (float, dict) """
    #-- Get mesh info --#
    bboxDict = pMode.getBboxInfoFromMesh(mesh)
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


class FromMel(object):
    """ List of NCloth commands calling melScript """

    def __init__(self):
        pass

    @staticmethod
    def createNSystem():
        """ If there is an nucleus node selected, return it, otherwise, create a new one and return it
            :return: Nucleus node name
            :rtype: str """
        return ml.eval("createNSystem:")

    @staticmethod
    def addActiveToNSystem(active, nucleus):
        """ Connect nCloth or nRigid to given nucleus
            :param active: nCloth or nRigid node
            :type active: str
            :param nucleus: Nucleus node
            :type nucleus: str
            :return: Nucleus inputActive attribute index
            :rtype: int """
        return ml.eval('addActiveToNSystem("%s", "%s");' % (active, nucleus))

    @staticmethod
    def getActiveNucleusNode(selectExisting=True, createNew=False):
        """ Find the currently active nucleus node, if none found, create one
            :param selectExisting: Select exisitng nucleus node
            :type selectExisting: bool
            :param createNew: Force new nucleus node creation
            :type createNew: bool
            :return: Active nucleus node
            :rtype: str """
        return ml.eval("getActiveNucleusNode(%s, %s);" % (int(selectExisting), int(createNew)))

    @staticmethod
    def createNCloth(worldSpace=False):
        """ Create nCloth node on selection
            :param worldSpace: If true, use worldSpace, else use localSpace
            :type worldSpace: bool
            :return: New nCloth nodes
            :rtype: list """
        return ml.eval("createNCloth %s;" % int(worldSpace))

    @staticmethod
    def createNRigid():
        """ Create nRigid node on selection
            :return: New nRigid nodes
            :rtype: list """
        return ml.eval("makeCollideNCloth;")

    @staticmethod
    def removeNCloth(delMode='selected'):
        """ Remove nCloth or nRigid nodes
            :param delMode: 'selected', 'allNCloths', 'allNRigids'
            :type delMode: str """
        ml.eval('removeNCloth "%s";' % delMode)


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
        nuc = GetActiveNucleusNodeBeta()
        nucleus = nuc.getActiveNucleus(nucleusName=self.useNucleus,
                                       selectExisting=self.selected,
                                       createNew=self.createNewNucleus)
        #-- Create nCloth Nodes --#
        newClothNodes = []
        for mesh in self.meshes:
            conns = mc.listConnections(mesh, sh=True, type='nBase')
            if not conns:
                # This mesh has no nBase associated with it, connect it
                meshTforms = pRigg.listTransforms(mesh)
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
                clothTforms = pRigg.listTransforms(nCloth)
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
                    pRigg.transfertWrapConns(wrapPlugs, outMesh)
        #-- Batch mode refresh --#
        if mc.about(batch=True):
            for cloth in newClothNodes:
                mc.getAttr('%s.forceDynamics' % cloth)
        #-- Result --#
        mc.select(newClothNodes)
        return newClothNodes


class GetActiveNucleusNodeBeta(object):
    """ Returns a nucleus node based on current selection, last referenced,
        last created, or dag order. """

    def __init__(self):
        self.activeNucleus = None

    def getActiveNucleus(self, nucleusName=None, selectExisting=False, createNew=False):
        """ Find the currently active nucleus node, if none found, execute kargs
            :param selectExisting: (bool) : select the first existing one, if any
            :param createNew: (bool) : force the creation of a new one
            :return: (str) : Active nucleus node """
        if nucleusName is not None:
            if mc.objExists(nucleusName) and mc.nodeType(nucleusName) == 'nucleus':
                self.activeNucleus = nucleusName
                return self.activeNucleus
        if self.findActiveNucleus() == "" or self.activeNucleus is None:
            if selectExisting:
                #-- Select an existing nucleus node, if there is one --#
                nodes = mc.ls(type='nucleus')
                if nodes:
                    self.activeNucleus = nodes[0]
                    return self.activeNucleus
                else:
                    self.activeNucleus = createNSystem()
                    return self.activeNucleus
        if createNew:
            #-- Force the creation of a new nucleus node --#
            self.activeNucleus = createNSystem()
        return self.activeNucleus

    def findActiveNucleus(self):
        """ We follow this order of checking for an active nucleus node
            1. explicitly selected nucleus
            2. explicitly selected nBase
            3. explicitly selected input or output mesh
            4. if active nucleus(global variable) use that
            5. use first nucleus in dag
            :return: (str) : Active nucleus node """
        #-- Check if any nucleus nodes already exist --#
        allNucleus = mc.ls(type='nucleus')
        if not allNucleus:
            self.activeNucleus = ""
            return self.activeNucleus
        if self.activeNucleus is None:
            self.activeNucleus = allNucleus[0]
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
                nBase = pRigg.findTypeInHistory(mesh, ['nBase'], future=True, past=True)
                if nBase is not None:
                    nBases.append(nBase)
        else:
            nBases = list(set(nBases))
            for nBase in nBases:
                startCon = mc.listConnections("%s.startState" % nBase, type='nucleus')
                nucleusNodes.append(startCon[0])
            if nucleusNodes:
                return self.pickBestNucleus(nucleusNodes)
        #-- Check nucleus nodes in dag --#
        if not self.activeNucleus == "":
            # Pick active if it still exists
            if not mc.objExists(self.activeNucleus):
                self.activeNucleus = ""
        #-- Result --#
        return self.activeNucleus

    def pickBestNucleus(self, nucleusNodes):
        """ Choose best nucleus node
            :param nucleusNodes: (list) : Nucleus node list
            :return: (str) : Best nucleus node """
        #-- Empty List --#
        if not nucleusNodes:
            self.activeNucleus = ""
            return self.activeNucleus
        #-- One Nucleus --#
        nucleusNodes = list(set(nucleusNodes))
        if len(nucleusNodes) == 1:
            self.activeNucleus = nucleusNodes[0]
            return self.activeNucleus
        #-- Multiple Nucleus --#
        if not self.activeNucleus == "":
            for nucleus in nucleusNodes:
                if nucleus == self.activeNucleus:
                    print "!!! Warning: Multiple possible nucleus nodes: Will use %s" % self.activeNucleus
                    return self.activeNucleus
        #-- Result --#
        self.activeNucleus = nucleusNodes[0]
        print "!!! Warning: Multiple possible nucleus nodes: Will use %s" % self.activeNucleus
        return self.activeNucleus
