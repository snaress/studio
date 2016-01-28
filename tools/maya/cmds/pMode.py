from tools.maya.cmds import pRigg
from lib.system import procMath as pMath
try:
    import maya.cmds as mc
    import maya.OpenMaya as om
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

def invertSelection():
    """
    Invert current selection

    Preference is given to objects if both objects and components are selected.
    there is no user case where the user wants to invert a mixed selection of objects and components
    """
    #// determine if anything is selected
    selection = mc.ls(sl=True)
    if selection:
        #// now determine if any objects are selected
        objects = mc.ls(sl=True, dag=True, v=True)
        if objects:
            mc.select(tgl=True, ado=True, vis=True)
            #//check if selection is in a hierarchy
            parents = mc.listRelatives()
            if parents:
                mc.select(parents, d=True)
                for parent in parents:
                    children = mc.listRelatives(parent, c=True, path=True)
                    mc.select(children, add=True)
                #// make sure the original objects are not selected
                mc.select(selection, d=True)
        else:
            #// must be a component selected
            newComponents = []
            for component in selection:
                newComponents.append('%s[*]' % component.split('[')[0])
            mc.select(newComponents, r=True)
            mc.select(selection, d=True)
    else:
        #// nothing is selected
        print "!!! Nothing is selected !!!"

def getVertexPosition(obj, toRound=5, ws=True) :
    """
    Get object vertex position, with approximation

    :param obj = obj to get vtx
    :type obj = str
    :param toRound = approximation
    :type toRound = int
    :param ws: World space state
    :type ws: bool
    :return: Vertex position
    :rtype: list
    """
    toR = []
    if not mc.ls(obj+".vtx[*]") :
        return toR
    tpos = mc.xform(obj+".vtx[*]", q=1, ws=ws, t=1)
    pos = zip(tpos[::3], tpos[1::3], tpos[2::3])
    for vtx in pos :
        x = round(vtx[0] , toRound)
        y = round(vtx[1] , toRound)
        z = round(vtx[2] , toRound)
        toR.append((x,y,z))
    return toR

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
        newName = cpObject
        #-- Parent To World --#
        if worldParent:
            if mc.listRelatives(cpObject[0], p=True) is not None:
                newName = mc.parent(cpObject[0], w=True)
        cpList.append(newName[0])
    return cpList

def duplicateGeom(selObjects=None, name=None):
    """
    Duplicate and parent to world selected objects via outMesh / inMesh

    :param selObjects: Objects to duplicate.
                       If None, duplicate selected scene nodes.
    :type selObjects: str | list
    :param name: New object name
    :type name: str
    :return: Duplicate objects
    :rtype: list
    """
    #-- Check Object List --#
    if selObjects is None:
        objectList = mc.ls(sl=True)
    else:
        if isinstance(selObjects, basestring):
            objectList = [selObjects]
        else:
            objectList = selObjects
    #-- Duplicate Objects --#
    cpList = []
    for obj in objectList:
        #-- Create Base Object --#
        if name is None:
            cpName = "%s__cp#" % obj.split(':')[-1].split('__')[0]
        else:
            cpName = name
        baseObj = mc.polySphere(n=cpName)[0]
        mc.delete(baseObj, ch=True)
        baseMesh = mc.listRelatives(baseObj, s=True, ni=True)[0]
        #-- Get Shape --#
        if not mc.nodeType(obj) == 'mesh':
            meshName = mc.listRelatives(obj, s=True, ni=True)[0]
        else:
            meshName = obj
        #-- Transfert Geom --#
        updateOutMesh(srcMesh=meshName, outMesh=baseMesh, force=True)
        cpList.append(baseObj)
    #-- Result --#
    return cpList

def decoupeMesh():
    """
    Extract selected faces via duplicate
    """
    #-- Check Selection --#
    selObject = mc.ls(sl=True, o=True)
    if not len(selObject) == 1:
        raise IOError("!!! Select only one object !!!")
    #-- Get Selected Components --#
    selection = mc.ls(sl=True, fl=True)
    selFaces = []
    for sel in selection:
        selFaces.append(int(sel.split('.')[-1].replace('f[', '').replace(']', '')))
    #-- Duplique Object --#
    tForm = mc.listRelatives(selObject[0], p=True)[0]
    dup = duplicateSelected(selObjects=tForm, name='%s__cut#' % tForm, worldParent=False)
    mc.select(cl=True)
    for f in selFaces:
        mc.select('%s.f[%s]' % (dup[0], f), add=True)
    #-- Remove Unselected --#
    invertSelection()
    mc.delete()

def symmetrizePose(baseObj, srcObj, dstObj, axe=(-1, 1, 1), delta=0.01):
    """
    Symmetrize Pose

    :param baseObj: Base object (bind pose)
    :type baseObj: str
    :param srcObj: Source object (morph pose)
    :type srcObj: str
    :param dstObj: Destination object (symmetry pose)
    :type dstObj: str
    :param axe: Symmetry axe (defaultAxe = 'X')
    :type axe: tuple
    :param delta: Precision coef
    :type delta: float
    """
    #-- Get Base Datas --#
    base = mc.xform(baseObj + ".vtx[*]", q=True, os=True, t=True)
    basePos = zip(base[::3], base[1::3], base[2::3])
    basePosPoints = [om.MPoint(*v) for v in basePos]

    #-- Get Source Datas --#
    base = mc.xform(srcObj + ".vtx[*]", q=True, os=True, t=True)
    srcPos = zip(base[::3], base[1::3], base[2::3])
    srcPosPoints = [om.MPoint(*v) for v in srcPos]

    #-- Get Matrix --#
    number = len(mc.getAttr(baseObj + ".pnts[*]"))
    mirrorMatrix = om.MTransformationMatrix()
    scaleUtil = om.MScriptUtil()
    scaleUtil.createFromDouble(*axe)
    scalePtr = scaleUtil.asDoublePtr()
    mirrorMatrix.setScale(scalePtr, om.MSpace.kObject)
    mirrorMatrix = mirrorMatrix.asScaleMatrix()

    #-- Mapping loop --#
    pointMap = {}
    for i in xrange(number):
        bpp = basePosPoints[i]
        for j in xrange(number):
            if i == j:
                continue
            cmpPos = basePosPoints[j]
            if bpp == cmpPos:
                mc.warning("Index %s and %s have the same position, check them..." % (i, j))
            mirrPos = bpp * mirrorMatrix
            if (mirrPos.x - delta <= cmpPos.x <= mirrPos.x + delta and
                mirrPos.y - delta <= cmpPos.y <= mirrPos.y + delta and
                mirrPos.z - delta <= cmpPos.z <= mirrPos.z + delta):
                pointMap[i] = j

    #-- Transfert Datas --#
    for i in xrange(number):
        if not i in pointMap:
            pointMap[i] = i
        dstPosPoints = srcPosPoints[i] * mirrorMatrix
        mc.xform("%s.vtx[%s]" % (dstObj, pointMap[i]), os=True, t=[dstPosPoints.x, dstPosPoints.y, dstPosPoints.z])

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
