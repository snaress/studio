from tools.maya.cmds import pRigg
from lib.system import procMath as pMath
try:
    import maya.cmds as mc
except:
    pass


def getBboxInfoFromMesh(mesh):
    """ Get boundingBox info from given mesh
        :param mesh: Mesh name
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
    #-- Multi Box --#
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
    #-- Single Box --#
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
    #-- Result --#
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

def polySelectTraverse(traversal=1):
    """ Grow polyComponent selection
        :param traversal: 0 = Off.
                          1 = More : will add current selection border to current selection.
                          2 = Less : will remove current selection border from current selection.
                          3 = Border : will keep only current selection border.
                          4 = Contiguous Edges : Add edges aligned with the current edges selected
        :type traversal: int """
    #-- Vertex --#
    result = mc.polyListComponentConversion(fv=True, tv=True)
    if result:
        mc.polySelectConstraint(pp=traversal, t=0x0001)
    else:
        #-- Edge --#
        result = mc.polyListComponentConversion(fe=True, te=True)
        if result:
            mc.polySelectConstraint(pp=traversal, t=0x8000)
        else:
            #-- Face --#
            result = mc.polyListComponentConversion(ff=True, tf=True)
            if result:
                mc.polySelectConstraint(pp=traversal, t=0x0008)
            else:
                #-- Uv --#
                result = mc.polyListComponentConversion(fuv=True, tuv=True)
                if result:
                    mc.polySelectConstraint(pp=traversal, t=0x0010)

def duplicateSelected(selObjects=None, name=None, worldParent=True):
    """ Duplicate and parent to world selected objects
        :param selObjects: Objects to duplicate.
                           If None, duplicate selected scene nodes.
        :type selObjects: str | list
        :param name: New object name
        :type name: str
        :param worldParent: Parent new object to world
        :type worldParent: bool
        :return: Duplicate objects
        :rtype: list """
    #-- Check Object List --#
    if selObjects is None:
        objectList = mc.ls(sl=True)
    else:
        if isinstance(selObjects, str):
            objectList = [selObjects]
        else:
            objectList = selObjects
    #-- Duplicate Objects --#
    cpList = []
    for obj in objectList:
        if name is None:
            cpName = "%s__cp#" % obj.split(':')[-1].split('__')[0]
        else:
            cpName = name
        cpObject = mc.duplicate(obj, n=cpName)
        newName = cpObject[0]
        #-- Parent To World --#
        if worldParent:
            if mc.listRelatives(cpObject[0], p=True) is not None:
                newName = mc.parent(cpObject[0], w=True)
        cpList.append(newName)
    return cpList

def connectOutMesh(srcMesh=None, outMesh=None, force=True):
    """ Connect srcMesh.outMesh to outMesh.inMesh
        :param srcMesh: Source mesh
        :type srcMesh: str
        :param outMesh: Out mesh
        :type outMesh: str
        :param force: Force connection
        :type force: True """
    #-- Check Object List --#
    if srcMesh is None and outMesh is None:
        selObjects = mc.ls(sl=True)
        if not selObjects:
            print "!!! Error: Select srcMesh, then outMesh !!!"
        else:
            srcMesh = selObjects[0]
            outMesh = selObjects[1]
    #-- Connect Attr --#
    ind = pRigg.getNextFreeMultiIndex("%s.worldMesh" % srcMesh)
    mc.connectAttr("%s.worldMesh[%s]" % (srcMesh, ind), "%s.inMesh" % outMesh, f=force)
    print "// Connect %s.worldMesh ---> %s.inMesh" % (srcMesh, outMesh)

def updateOutMesh(srcMesh=None, outMesh=None, force=True):
    """ Update given outMesh, then remove connection
        :param srcMesh: Source mesh
        :type srcMesh: str
        :param outMesh: Out mesh
        :type outMesh: str
        :param force: Force connection
        :type force: True """
    #-- Check Object List --#
    if srcMesh is None and outMesh is None:
        selObjects = mc.ls(sl=True)
        print selObjects
        if not selObjects:
            print "!!! Error: Select srcMesh, then outMesh !!!"
        else:
            srcMesh = selObjects[0]
            outMesh = selObjects[1]
    #-- Update Mesh --#
    connectOutMesh(srcMesh, outMesh, force=force)
    mc.refresh()
    mc.disconnectAttr("%s.outMesh" % srcMesh, "%s.inMesh" % outMesh)
    print "// Update %s.outMesh ---> %s.inMesh" % (srcMesh, outMesh)

def createOutMesh(selObjects=None, name=None, worldParent=True):
    """ Create outMesh from selected objects
        :param selObjects: Objects to duplicate and connect.
                           If None, duplicate selected scene nodes.
        :type selObjects: str | list
        :param name: New object name
        :type name: str
        :param worldParent: Parent new object to world
        :type worldParent: bool
        :return: OutMesh objects
        :rtype: list """
    #-- Check Object List --#
    if selObjects is None:
        selObjects = mc.ls(sl=True)
    else:
        if isinstance(selObjects, str):
            selObjects = [selObjects]
    #-- Create OutMesh --#
    outList = []
    for obj in selObjects:
        if name is None:
            outName = "%s__out#" % obj.split(':')[-1].split('__')[0]
        else:
            outName = name
        outMesh = duplicateSelected(selObjects=str(obj), name=str(outName), worldParent=worldParent)[0]
        if isinstance(outMesh, list):
            connectOutMesh(srcMesh=str(obj), outMesh=str(outMesh[0]))
            outList.append(outMesh[0])
        else:
            connectOutMesh(srcMesh=str(obj), outMesh=str(outMesh))
            outList.append(outMesh)
    return outList
