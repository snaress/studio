from tools.maya.cmds import pScene, pCloth
try:
    import maya.cmds as mc
except:
    pass


def getNamespace(nodeName, returnList=False):
    """ Get given node namespace
        :param nodeName: Node full name
        :type nodeName: str
        :param returnList: Return result as list instead of str
        :return: Node namespace, Node name
        :rtype: (str | list, str) """
    ns, name = pScene.getNamespace(nodeName, returnList=returnList)
    return ns, name

def attrIsLocked(nodeFullName):
    """ Check if given node attribute is locked
        :param nodeFullName: 'nodeName.nodeAttr'
        :type nodeFullName: str
        :return: Attribute lock state
        :rtype: bool """
    if mc.objExists(nodeFullName):
        return mc.getAttr(nodeFullName, l=True)
    print "!!! WARNING: Node not found: %s !!!" % nodeFullName

def setAttrLock(nodeFullName, state):
    """ Set given nodeAttr lock on or off
        :param nodeFullName: 'nodeName.nodeAttr'
        :type nodeFullName: str
        :param state: Attribute lock state
        :type state: bool
        :return: True if success, else False
        :rtype: bool """
    if mc.objExists(nodeFullName):
        try:
            mc.setAttr(nodeFullName, l=state)
            return True
        except:
            return False
    print "!!! WARNING: Node not found: %s !!!" % nodeFullName
    return False

def getAllNucleus():
    """ Get all nucleus in scene
        :return: Nucleus nodes
        :rtype: list """
    return mc.ls(type='nucleus')

def getNodeParent(nodeName):
    """ Get given node parent (transform)
        :param nodeName: Node name
        :type nodeName: str
        :return: Node parent name (transform)
        :rtype: str """
    if mc.objExists(nodeName):
        parent = mc.listRelatives(nodeName, p=True)
        if parent:
            return parent[0]
        print "!!! WARNING: Parent not found for %s" % nodeName
    else:
        print "!!! WARNING: ClothNode not found for %s" % nodeName

def getNodeShape(nodeName):
    """ Get given node shape (mesh)
        :param nodeName: Node name
        :type nodeName: str
        :return: Node parent name (transform)
        :rtype: str """
    if mc.objExists(nodeName):
        shape = mc.listRelatives(nodeName, s=True, ni=True)
        if shape:
            return shape[0]
        print "!!! WARNING: Shape not found for %s" % nodeName
    else:
        print "!!! WARNING: Node not found for %s" % nodeName

def getClothType(clothNode):
    """ Get clothNode type
        :param clothNode: Cloth node name
        :type clothNode: str
        :return: Cloth node type ['nCloth', 'nRigid']
        :rtype: str """
    clothType = mc.nodeType(clothNode)
    if clothType in ['nucleus', 'nCloth', 'nRigid']:
        return clothType

def getModelFromClothNode(clothNode):
    """ Get model from given clothNode
        :param clothNode: Cloth node name
        :type clothNode: str
        :return: Connected model
        :rtype: str """
    return pCloth.getModelFromClothNode(clothNode)

def selectModel(clothNode):
    """ Select model from given clothNode
        :param clothNode: Cloth node name
        :type clothNode: str """
    model = getModelFromClothNode(clothNode)
    if mc.objExists(model):
        mc.select(model, r=True)

def selectVtxOnModel(vtxToSelect):
    """ Select given vertex list
        :param vtxToSelect: Elements to select
        :type vtxToSelect: list """
    mc.select(vtxToSelect, r=True)

def getModelSelVtx(clothNode, indexOnly=False):
    """ Get selected vertex on model
        :param clothNode: Cloth node name
        :type clothNode: str
        :param indexOnly: If True, return index only, else fullName
        :type indexOnly: bool
        :return: selection list
        :rtype: list """
    return pCloth.getModelSelectedVtx(clothNode, indexOnly=indexOnly)

def clearVtxSelection():
    """ Clear vertex selection on model """
    mc.select(cl=True)

def getVtxMaps(clothNode):
    """ Get vertex map list from given clothNode
        :param clothNode: Cloth node name
        :type clothNode: str
        :return: Vertex map list
        :rtype: list """
    return pCloth.getVtxMaps(clothNode)

def getVtxMapType(clothNode, mapType):
    """ Get given clothNode vtxMap type
        :param clothNode: Cloth node name
        :type clothNode: str
        :param mapType: Cloth node vtxMap name
        :type mapType: str
        :return: VtxMap type (0 = None, 1 = Vertex, 2 = Texture)
        :rtype: int """
    return pCloth.getVtxMapType(clothNode, mapType)

def setVtxMapType(clothNode, mapType, value):
    """ Set given clothNode vtxMap value
        :param clothNode: Cloth node name
        :type clothNode: str
        :param mapType: Cloth node vtxMap name (must ends with 'MapType')
        :type mapType: str
        :param value: VtxMap type (0 = None, 1 = Vertex, 2 = Texture)
        :type value: int """
    pCloth.setVtxMapType(clothNode, mapType, value)

def getVtxMapData(clothNode, vtxMap):
    """ Get vertex map influence per vertex
        :param clothNode: Cloth node name
        :type clothNode: str
        :param vtxMap: Vertex map name (must ends with 'PerVertex')
        :type vtxMap: str
        :return: Influence list per vertex
        :rtype: list """
    return pCloth.getVtxMapData(clothNode, vtxMap)

def setVtxMapData(clothNode, vtxMap, value):
    """ Set vertex map influence per vertex
        :param clothNode: Cloth node name
        :type clothNode: str
        :param vtxMap: Vertex map name (must ends with 'PerVertex')
        :type vtxMap: str
        :param value: Influence list per vertex
        :type value: list """
    pCloth.setVtxMapData(clothNode, vtxMap, value, refresh=True)

def paintVtxMap(clothNode, mapName):
    """ Enable maya vertex paint tool
        :param clothNode: Cloth node name
        :type clothNode: str
        :param mapName: Vertex map name
        :type mapName: str """
    pCloth.paintVtxMap(clothNode, mapName)

def selectVtxInfluence(clothNode, vtxMap, selMode, value=None, minInf=None, maxInf=None):
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
    if selMode == 'range':
        pCloth.selectVtxInfOnModel(clothNode, vtxMap, selMode, minInf=minInf, maxInf=maxInf)
    elif selMode == 'value':
        pCloth.selectVtxInfOnModel(clothNode, vtxMap, selMode, value=value)
