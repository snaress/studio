from  tools.maya.cmds import rigg
try:
    import maya.cmds as mc
    import maya.mel as ml
except:
    pass


def getClothNode(nodeName):
    """ Try to find cloth node connected to given object
        :param nodeName: Transform or Mesh node name
        :type nodeName: str
        :return: Cloth node name
        :rtype: str """
    clothNode = rigg.findTypeInHistory(nodeName, ['nCloth', 'nRigid'], future=True, past=True)
    if clothNode:
        return clothNode

def getClothNodeFromSelected():
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
    mc.setAttr('%s.%s' % (clothNode, vtxMap), value, type='doubleArray')
    if refresh:
        mc.refresh()

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
            mc.select(r=True)

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
