try:
    import maya.cmds as mc
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
