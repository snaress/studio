from tools.maya.util.proc import procRigg as pRigg
try:
    import maya.cmds as mc
    import maya.mel as ml
except:
    pass


def getClothNodeFromSel(returnLog=False):
    """ Try to find cloth node connected to selected object.
        Only one object must be selected
        :param returnLog: (bool) : Log return enable
        :return: (str) : Cloth node name, or None if cloth node not found """
    selection = mc.ls(sl=True)
    #-- Check Selection --#
    if not len(selection) == 1:
        if returnLog:
            return None, "!!! WARNING: Select only one object !!!"
        return None
    #-- Search Cloth Node --#
    if returnLog:
        clothNode, log = getClothNode(selection[0], returnLog=True)
        return clothNode, log
    clothNode = getClothNode(selection[0], returnLog=False)
    return clothNode

def getClothNode(objectName, returnLog=False):
    """ Try to find cloth node connected to given object
        :param objectName: (str) : Transform or Mesh node name
        :param returnLog: (bool) : Log return enable
        :returns: (str) : Cloth node name, or None if cloth node not found
                  (str) : Result log (optionnal) """
    result = pRigg.findTypeInHistory(objectName, ['nCloth', 'nRigid'], future=True, past=True)
    if not result:
        if returnLog:
            return None, "No cloth node found !"
        return None
    if returnLog:
        return result, "Cloth node found: %s" % result

def getClothNodeOld(objectName, returnLog=False):
    """ Try to find cloth node connected to given object
        :param objectName: (str) : Transform or Mesh node name
        :param returnLog: (bool) : Log return enable
        :returns: (str) : Cloth node name, or None if cloth node not found
                  (str) : Result log (optionnal) """
    selObj = objectName
    #-- Object Type: Transform --#
    if mc.nodeType(selObj) == "transform":
        shapes = mc.listRelatives(selObj, s=True, ni=True)
        #-- Check Connected Shape --#
        if shapes is None:
            if returnLog:
                return None, "!!! WARNING: Shape not found !!!"
            return None
        #-- Check No-Intermediate Shape --#
        if not len(shapes) == 1:
            if returnLog:
                return None, "!!! WARNING: Selection should have only one non-intermediate shape !!!"
            return None
        selShape = shapes[0]
    #-- Object Type: Shape --#
    elif mc.nodeType(selObj) in ["mesh", "nCloth", "nRigid"]:
        selShape = selObj
    #-- Object Type: Unknown --#
    else:
        if returnLog:
            return None, "!!! WARNING: SelType should be 'transform' or 'mesh', get %s" % mc.nodeType(selObj)
        return None
    #-- ClothNode Given --#
    if mc.nodeType(selShape) in ["nCloth", "nRigid"]:
        if returnLog:
            return selShape, "---> getClothNode result: Cloth node found: %s" % selShape
        return selShape
    #-- ClothNode Search --#
    connections = mc.listConnections(selShape, s=True, d=True, p=True)
    for c in connections:
        nodeName = c.split('.')[0]
        if mc.nodeType(nodeName) in ["nCloth", "nRigid"]:
            if returnLog:
                return nodeName, "---> getClothNode result: Cloth node found: %s" % nodeName
            return nodeName
    #-- No ClothNode --#
    if returnLog:
        return None, "---> getClothNode result: No cloth node found"
    return None

def getVtxMaps(clothNode):
    """ Get vertex map list from given clothNode
        :param clothNode: (str) : Cloth shape node name
        :return: (list) : Vertex map list """
    maps = []
    if mc.objExists(clothNode) and mc.nodeType(clothNode) in ['nCloth', 'nRigid']:
        #-- Get vertex mapType list --#
        attrs = mc.listAttr(clothNode)
        for attr in attrs:
            if attr.endswith("MapType"):
                mapName = attr.replace('MapType', '')
                maps.append(mapName)
    else:
        print "!!! WARNING: No vertex map found !!!"
    return maps

def getVtxMapType(clothNode, mapType):
    """ Get given clothNode vtxMap type
        :param clothNode: (str) : Cloth shape node name
        :param mapType: (str) : Cloth node vtxMap name (must ends with 'MapType')
        :return: (int) : VtxMap type (0 = None, 1 = Vertex, 2 = Texture) """
    if mc.objExists(clothNode) and mc.nodeType(clothNode) in ['nCloth', 'nRigid']:
        return mc.getAttr("%s.%s" % (clothNode, mapType))
    print "!!! WARNING: ClothNode not found, or is not a cloth node: %s" % clothNode
    return None

def setVtxMapType(clothNode, mapType, value):
    """ Set given clothNode vtxMap value
        :param clothNode: (str) : Cloth shape node name
        :param mapType: (str) : Cloth node vtxMap name (must ends with 'MapType')
        :param value: (int) : VtxMap type (0 = None, 1 = Vertex, 2 = Texture)
        :return: (bool) : True if success, else False """
    if mc.objExists(clothNode) and mc.nodeType(clothNode) in ['nCloth', 'nRigid']:
        mc.setAttr("%s.%s" % (clothNode, mapType), value)
        return True
    else:
        print "!!! WARNING: ClothNode not found, or is not a cloth node: %s" % clothNode
        return False

def getVtxMapData(clothNode, vtxMap):
    """ Get vertex map influence per vertex
        :param clothNode: (str) : Cloth shape node name
        :param vtxMap: (str) : Vertex map name (must ends with 'PerVertex')
        :return: (list) : Influence list per vertex """
    if mc.objExists(clothNode) and mc.nodeType(clothNode) in ['nCloth', 'nRigid']:
        return mc.getAttr("%s.%s" % (clothNode, vtxMap))
    else:
        print "!!! WARNING: ClothNode not found, or is not a cloth node: %s" % clothNode
        return None

def setVtxMapData(clothNode, vtxMap, value, refresh=False):
    """ Set vertex map influence per vertex
        :param clothNode: (str) : Cloth shape node name
        :param vtxMap: (str) : Vertex map name (must ends with 'PerVertex')
        :param value: (list) : Influence list per vertex
        :param refresh: (bool) : Refresh maya ui """
    if isinstance(value, list):
        mc.setAttr('%s.%s' % (clothNode, vtxMap), value, type='doubleArray')
        if refresh:
            mc.refresh()
    else:
        print "!!! WARNING: Value arg should be a list !!!"

def getModelFromClothNode(clothNode):
    """ Get model from given clothNode
        :param clothNode: (str) : Cloth shape node name
        :return: (str) : Connected model """
    if mc.objExists(clothNode) and mc.nodeType(clothNode) in ['nCloth', 'nRigid']:
        model = mc.listConnections("%s.inputMesh" %clothNode, s=True)
        if model:
            return model[0]
        else:
            print "!!! WARNING: No 'inputMesh' connection found !!!"
            return None
    else:
        print "!!! WARNING: ClothNode not found, or is not a cloth node: %s" % clothNode
        return None

def getModelSelectedVtx(clothNode, indexOnly=False):
    """ Get selected vertex on model
        :param clothNode: (str) : Cloth shape node name
        :param indexOnly: (bool) : If True, return index only, else fullName
        :return: (list) : selection list """
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

def selectVtxOnModel(clothNode, vtxMap, selMode, value=None, minInf=None, maxInf=None):
    """ Select vertex on model given by value or range
        :param clothNode: (str) : Cloth shape node name
        :param vtxMap: (str) : Vertex map name (must ends with 'PerVertex')
        :param selMode: (str) : 'range' or 'value'
        :param value: (float) : Influence value
        :param minInf: (float) : Range minimum influence
        :param maxInf: (float) : Range maximum influence """
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
        :param clothNode: (str) : Cloth shape node name
        :param mapName: (str) : Vertex map name """
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



def createNCloth(worldSpace=True):
    """ Create nCloth node on selection
        :param worldSpace: (bool) : If true, use worldSpace, else use localSpace
        :return: (list) : New nCloth nodes """
    result = ml.eval("createNCloth %s;" % int(worldSpace))
    return result

def createNRigid():
    """ Create nRigid node on selection
        :return: (list) : New nRigid nodes """
    result = ml.eval("makeCollideNCloth;")
    return result

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


class CreateNCloth(object):

    def __init__(self, useNucleus=None, selectExisting=False, createNew=False, worldSpace=True):
        #-- Store kwargs --#
        self.useNucleus = useNucleus
        self.selectExisting = selectExisting
        self.createNew = createNew
        self.worldSpace = worldSpace
        #-- Init --#
        self.selected = self._initSelection()
        self.meshes = self._initMeshes()
        self.outMeshName = 'outputCloth1'
        print self.selected
        print self.meshes

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
        nucleus = nuc.getActiveNucleus( nucleusName=self.useNucleus,
                                        selectExisting=self.selected,
                                        createNew=self.createNew )
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



class GetActiveNucleusNode(object):
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
                nBase = pRigg.findTypeInHistory(mesh, 'nBase', future=True, past=True)
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

