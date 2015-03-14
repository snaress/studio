import tools.maya.cmds as smc
from tools.maya.cmds import pCloth
try:
    import maya.cmds as mc
except:
    pass


def getAllClothNodes():
    """ Get scene nodes from of type 'nCloth' and 'n
        :return: nCloth and nRigid nodes
        :rtype: list """
    return mc.ls(type=['nCloth', 'nRigid'])

def getClothNodeParent(clothNode):
    """ Get given clothNode parent (transform)
        :param clothNode: Cloth node name
        :type clothNode: str
        :return: Cloth node parent name (transform)
        :rtype: str """
    if mc.objExists(clothNode) and mc.nodeType(clothNode) in ['nCloth', 'nRigid']:
        parent = mc.listRelatives(clothNode, p=True)
        if parent:
            return parent[0]
        print "!!! WARNING: Parent not found for %s" % clothNode
    else:
        print "!!! WARNING: ClothNode not found for %s" % clothNode

def getClothType(clothNode):
    """ Get clothNode type
        :param clothNode: Cloth node name
        :type clothNode: str
        :return: Cloth node type ['nCloth', 'nRigid']
        :rtype: str """
    clothType = mc.nodeType(clothNode)
    if clothType in ['nCloth', 'nRigid']:
        return clothType

def getClothNodesFromSel():
    """ Get cloth nodes from current selected object
        :return: Cloth node names
        :rtype: list """
    return pCloth.getClothNodeFromSelected()

def selectClothNode(clothNode):
    """ Select given clothNode in scene
        :param clothNode: Cloth node name
        :type clothNode: str """
    if not mc.objExists(clothNode):
        print "!!! WARNING: Cloth node not found: %s !!!" % clothNode
    else:
        mc.select(clothNode, r=True)

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
        :param clothNode: (str) : Cloth node name
        :param mapType: (str) : Cloth node vtxMap name (must ends with 'MapType')
        :param value: (int) : VtxMap type (0 = None, 1 = Vertex, 2 = Texture) """
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

def getModelFromClothNode(clothNode):
    """ Get model from given clothNode
        :param clothNode: Cloth node name
        :type clothNode: str
        :return: Connected model
        :rtype: str """
    return pCloth.getModelFromClothNode(clothNode)

def getModelSelVtx(clothNode, indexOnly=False):
    """ Get selected vertex on model
        :param clothNode: Cloth node name
        :type clothNode: str
        :param indexOnly: If True, return index only, else fullName
        :type indexOnly: bool
        :return: selection list
        :rtype: list """
    return pCloth.getModelSelectedVtx(clothNode, indexOnly=indexOnly)

def paintVtxMap(clothNode, mapName):
    """ Enable maya vertex paint tool
        :param clothNode: Cloth node name
        :type clothNode: str
        :param mapName: Vertex map name
        :type mapName: str """
    pCloth.paintVtxMap(clothNode, mapName)

def clearVtxSelection():
    """ Clear vertex selection on model """
    mc.select(cl=True)

def selectVtxOnModel(vtxToSelect):
    """ Select given vertex list
        :param vtxToSelect: Elements to select
        :type vtxToSelect: list """
    mc.select(vtxToSelect, r=True)

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
