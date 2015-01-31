from lib.system import procMath as pMath
try:
    import maya.cmds as mc
except:
    pass


def getBboxInfoFromMesh(mesh):
    """ Get boundingBox info from given mesh
        :param mesh: shape name
        :type mesh: str
        :return: Bbox info {'bbox', 'pMin', 'pMax', 'x', 'y', 'z', 'surfaceArea'}
        :rtype: dict """
    bbox = mc.exactWorldBoundingBox(mesh)
    return getInfoFromBbox(bbox)

def getInfoFromBbox(bbox):
    """ Get boundingBox info from bbox values
        :param bbox: BoundingBox values (Xmin, Ymin, Zmin, Xmax, Ymax, Zmax)
        :type bbox: list
        :return: Bbox info {'bbox', 'pMin', 'pMax', 'x', 'y', 'z', 'surfaceArea'}
        :rtype: dict """
    pMin = (bbox[0], bbox[1], bbox[2])
    pMax = (bbox[3], bbox[4], bbox[5])
    x = (bbox[3] - bbox[0])
    y = (bbox[4] - bbox[1])
    z = (bbox[5] - bbox[2])
    bboxSurfaceArea = (2 * ((x * y) + (x * z) + (y * z)))
    return {'bbox': bbox, 'pMin': pMin, 'pMax': pMax, 'x': x, 'y': y, 'z': z, 'surfaceArea': bboxSurfaceArea}

def creeBoxOnSelected(name=None, multi=False, returnShape=False):
    """ Create boundingBox around selected objects
        :param name: New box name
        :type name: str
        :param multi: If true, create a box around each mesh
        :type multi: bool
        :param returnShape: Enable new bbox shape name return
        :type returnShape: bool
        :return: New boxes info {'bbox', 'boxInfo'}
        :rtype: dict """
    selected = mc.ls(sl=True)
    if selected:
        return creeBoxOnNodes(selected, name=name, multi=multi, returnShape=returnShape)

def creeBoxOnNodes(meshes, name=None, multi=False, returnShape=False):
    """ Create boundingBox around given meshes
        :param meshes: Mesh nodes
        :type meshes: list
        :param name: New box name
        :type name: str
        :param multi: If true, create a box around each mesh
        :type multi: bool
        :param returnShape: Enable new bbox shape name return
        :type returnShape: bool
        :return: New boxes info {'bbox', 'boxInfo'}
        :rtype: dict """
    boxesDict = {}
    for mesh in meshes:
        #-- Store multi Bbox Dict --#
        bboxDict = getBboxInfoFromMesh(mesh)
        boxesDict[mesh] = {}
        boxesDict[mesh]['bboxDict'] = bboxDict
        if multi:
            #-- Create multi boxes and store info --#
            boxTForm, boxMesh = creeBox(bboxDict=bboxDict, name=name, returnShape=True)
            if returnShape:
                boxesDict[mesh]['boxInfo'] = {'tForm': boxTForm, 'mesh': boxMesh}
            else:
                boxesDict[mesh]['boxInfo'] = {'tForm': boxTForm}
    if not multi:
        #-- Get single bbox values --#
        tmpMin = [None, None, None]
        tmpMax = [None, None, None]
        for axe in range(3):
            for storedMesh in boxesDict.keys():
                valMin = boxesDict[storedMesh]['bboxDict']['pMin'][axe]
                valMax = boxesDict[storedMesh]['bboxDict']['pMax'][axe]
                if tmpMin[axe] is None or valMin < tmpMin[axe]:
                    tmpMin[axe] = valMin
                if tmpMax[axe] is None or valMax > tmpMax[axe]:
                    tmpMax[axe] = valMax
        #-- Store single Bbox Dict --#
        bboxDict = getInfoFromBbox([tmpMin[0], tmpMin[1], tmpMin[2], tmpMax[0], tmpMax[1], tmpMax[2]])
        boxesDict['all'] = {}
        boxesDict['all']['bboxDict'] = bboxDict
        #-- Create single box and store info --#
        boxTForm, boxMesh = creeBox(bboxDict=bboxDict, name=name, returnShape=True)
        if returnShape:
            boxesDict['all']['boxInfo'] = {'tForm': boxTForm, 'mesh': boxMesh}
        else:
            boxesDict['all']['boxInfo'] = {'tForm': boxTForm}
    return boxesDict

def creeBox(bboxDict=None, name=None, returnShape=False):
    """ Create a boundingBox from given bounding box dict
        :param bboxDict: Mesh bbox info
        :type bboxDict: dict
        :param name: Name of the new bbox
        :type name: str
        :param returnShape: Enable new bbox shape name return
        :type returnShape: bool
        :return: New bbox transform ans shape name
        :rtype: (str, str) """
    pos = pMath.coordOp(bboxDict['pMin'], bboxDict['pMax'], 'average')
    if name is None:
        name = 'newBox1'
    boxName = mc.polyCube(n=name, w=bboxDict['x'], h=bboxDict['y'], d=bboxDict['z'])
    mc.setAttr('%s.translate' % boxName[0], pos[0], pos[1], pos[2])
    if returnShape:
        return boxName[0], boxName[1]
    return boxName[0]
