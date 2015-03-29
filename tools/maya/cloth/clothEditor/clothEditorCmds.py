from tools.maya.cmds import pCloth
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
    if ':' in nodeName:
        if returnList:
            return nodeName.split(':')[:-1], nodeName.split(':')[-1]
        else:
            return ':'.join(nodeName.split(':')[:-1]) , nodeName.split(':')[-1]
    return None, nodeName

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

def getVtxMaps(clothNode):
    """ Get vertex map list from given clothNode
        :param clothNode: Cloth node name
        :type clothNode: str
        :return: Vertex map list
        :rtype: list """
    return pCloth.getVtxMaps(clothNode)
