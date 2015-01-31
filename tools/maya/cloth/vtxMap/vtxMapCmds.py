from tools.maya.util.proc import procCloth as pCloth
try:
    import maya.cmds as mc
except:
    pass


def getAllClothNodes(nodeType):
    """ Get scene nodes from given nodeType
        :param nodeType: (str) : 'nCloth' or 'nRigid'
        :return: (list) : Cloth nodes """
    nodes = []
    if nodeType in ['nCloth', 'nRigid']:
        tmpNodes = mc.ls(type=nodeType)
        if tmpNodes:
            nodes = tmpNodes
    else:
        print "!!! WARNING: NodeType unknown (%s)" % nodeType
    return nodes

def getClothNode(returnLog=False):
    """ Get cloth node shape from selected object
        :return: (str) : Cloth shape node name """
    if returnLog:
        clothNode, log = pCloth.getClothNodeFromSel(returnLog=returnLog)
        return clothNode, log
    return pCloth.getClothNodeFromSel(returnLog=returnLog)

def getNodeType(clothNode):
    """ Get given cloth node type
        :param clothNode: (str) : Cloth shape node name
        :return: (str) : Node type if given node is a cloth node, else None """
    nodeType = mc.nodeType(clothNode)
    if nodeType in ['nCloth', 'nRigid']:
        return nodeType
    return None

def selectClothNode(clothNode):
    """ Select given clothNode
        :param clothNode: (str) : Cloth shape node name """
    if not mc.objExists(clothNode):
        print "!!! WARNING: Cloth node not found: %s !!!" % clothNode
    else:
        mc.select(clothNode)

def getClothNodeParent(clothNode):
    """ Get given clothNode parent
        :param clothNode: (str) : Cloth parent node name """
    if mc.objExists(clothNode) and mc.nodeType(clothNode) in ['nCloth', 'nRigid']:
        parent = mc.listRelatives(clothNode, p=True)
        if parent:
            return parent[0]
        else:
            print "!!! WARNING: Parent not found for %s" % clothNode
            return None
    else:
        print "!!! WARNING: ClothNode not found for %s" % clothNode
        return None

def getVtxMaps(clothNode):
    """ Get vertex map list from given clothNode
        :param clothNode: (str) : Cloth shape node name
        :return: (list) : Vertex map list """
    return pCloth.getVtxMaps(clothNode)

def getVtxMapType(clothNode, mapType):
    """ Get given clothNode vtxMap type
        :param clothNode: (str) : Cloth shape node name
        :param mapType: (str) : Cloth node vtxMap name
        :return: (int) : VtxMap type (0 = None, 1 = Vertex, 2 = Texture) """
    return pCloth.getVtxMapType(clothNode, mapType)

def setVtxMapType(clothNode, mapType, value):
    """ Set given clothNode vtxMap value
        :param clothNode: (str) : Cloth shape node name
        :param mapType: (str) : Cloth node vtxMap name (must ends with 'MapType')
        :param value: (int) : VtxMap type (0 = None, 1 = Vertex, 2 = Texture) """
    pCloth.setVtxMapType(clothNode, mapType, value)

def getVtxMapData(clothNode, vtxMap):
    """ Get vertex map influence per vertex
        :param clothNode: (str) : Cloth shape node name
        :param vtxMap: (str) : Vertex map name (must ends with 'PerVertex')
        :return: (list) : Influence list per vertex """
    return pCloth.getVtxMapData(clothNode, vtxMap)

def getModelFromClothNode(clothNode):
    """ Get model from given clothNode
        :param clothNode: (str) : Cloth shape node name
        :return: (str) : Connected model """
    return pCloth.getModelFromClothNode(clothNode)

def getModelSelVtx(clothNode, indexOnly=False):
    """ Get selected vertex on model
        :param clothNode: (str) : Cloth shape node name
        :param indexOnly: (bool) : If True, return index only, else fullName
        :return: (list) : selection list """
    return pCloth.getModelSelectedVtx(clothNode, indexOnly=indexOnly)

def selectVtx(clothNode, vtxMap, selMode, value=None, minInf=None, maxInf=None):
    """ Select vertex on model given by value or range
        :param clothNode: (str) : Cloth shape node name
        :param vtxMap: (str) : Vertex map name (must ends with 'PerVertex')
        :param selMode: (str) : 'range' or 'value'
        :param value: (float) : Influence value
        :param minInf: (float) : Range minimum influence
        :param maxInf: (float) : Range maximum influence """
    if selMode == 'range':
        pCloth.selectVtxOnModel(clothNode, vtxMap, selMode, minInf=minInf, maxInf=maxInf)
    elif selMode == 'value':
        pCloth.selectVtxOnModel(clothNode, vtxMap, selMode, value=value)

def paintVtxMap(clothNode, mapName):
    """ Enable maya vertex paint tool
        :param clothNode: (str) : Cloth shape node name
        :param mapName: (str) : Vertex map name """
    pCloth.paintVtxMap(clothNode, mapName)