from tools.maya.cmds import pScene, pCloth
try:
    import maya.cmds as mc
except:
    pass


def getAttr(nodeName, nodeAttr):
    """ Get given nodeAttr value
        :param nodeName: Node full name
        :type nodeName: str
        :param nodeAttr: Node attribute
        :type nodeAttr: str
        :return: Node attribute value
        :rtype: float | list """
    if mc.objExists("%s.%s" % (nodeName, nodeAttr)):
        return mc.getAttr("%s.%s" % (nodeName, nodeAttr))

def setAttr(nodeName, nodeAttr, value):
    """ set given nodeAttr value
        :param nodeName: Node full name
        :type nodeName: str
        :param nodeAttr: Node attribute
        :type nodeAttr: str
        :param value: Node attriute value
        :type value: int | float | list | tuple """
    node = "%s.%s" % (nodeName, nodeAttr)
    if mc.objExists(node):
        if mc.getAttr(node, type=True) == 'float3':
            mc.setAttr("%s.%s" % (nodeName, nodeAttr), value[0], value[1], value[2])
        else:
            mc.setAttr("%s.%s" % (nodeName, nodeAttr), value)

def getNamespace(nodeName, returnList=False):
    """ Get given node namespace
        :param nodeName: Node full name
        :type nodeName: str
        :param returnList: Return result as list instead of str
        :return: Node namespace, Node name
        :rtype: (str | list, str) """
    ns, name = pScene.getNamespace(nodeName, returnList=returnList)
    return ns, name

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
    if mc.nodeType(clothNode) == 'nucleus':
        model = clothNode
    else:
        model = getModelFromClothNode(clothNode)
    if mc.objExists(model):
        mc.select(model, r=True)
