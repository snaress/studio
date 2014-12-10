import math
from lib.system import procMath as pMath
from tools.maya.util.proc import procModeling as pMode
try:
    import maya.cmds as mc
except:
    pass


def getModels():
    """ Get selected models or list scene models if selection is empty
        :return: (list) : Model list """
    #-- Get models --#
    models = mc.ls(sl=True) or []
    if models:
        print "Selected models detected."
        return models
    else:
        print "No model selected, parse scene ..."
        models = []
        #-- Add Mesh --#
        sel = mc.ls(type='mesh') or []
        if sel:
            print "\t Mesh detected ..."
            for m in sel:
                parent = mc.listRelatives(m, p=True)
                if parent is not None:
                    models.append(parent[0])
        #-- Add Nurbs --#
        sel = mc.ls(type='nurbsSurface') or []
        if sel:
            print "\t Nurbs detected ..."
            for m in sel:
                parent = mc.listRelatives(m, p=True)
                if parent is not None:
                    models.append(parent[0])
        return models

def selectModels(models):
    """ Select models
        :param models: (list) : Model list
        :return: (bool) : True is success """
    if models:
        mc.select(cl=True)
        mc.select(models)
        if mc.ls(sl=True):
            print "Selection is valide."
            return True
        else:
            print "Selection is not valide !!!"
            return False
    else:
        print "Selection is not valide !!!"
        return False

def createBbox():
    """ Create Bbox from selected models
        :return: (str) : Bbox name """
    print "Creating boxCam ..."
    boxName = 'boxCam'
    if mc.objExists(boxName):
        print "Clean existing boxCam ..."
        mc.delete(boxName)
    pMode.creeBox(name=boxName)
    return boxName

def getBoxInfo(boxName):
    """ Get bbox info
        :param boxName: (str) : Bbox name
        :return: (float) : Max diagonal """
    refD = 0
    for diag in [[0, 3], [1, 5], [2, 5]]:
        p1 = mc.xform("%s.vtx[%s]" % (boxName, diag[0]), q=True, t=True)
        p2 = mc.xform("%s.vtx[%s]" % (boxName, diag[1]), q=True, t=True)
        d = pMath.getDistance(p1, p2)
        if d > refD:
            refD = d
    return refD

def cameraLocator(boxName):
    """ Create group and locator
        :param boxName: (str) : Bbox name """
    print "Creating camera locator ..."
    #-- Create Group --#
    grpName = 'GRP_camTurn'
    if mc.objExists(grpName):
        mc.delete(grpName)
    mc.group(n=grpName, em=True)
    for attr in ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']:
        mc.setAttr("%s.%s" % (grpName, attr), l=True, k=False, cb=False)
    #-- Create Locator --#
    locName = 'N_camTurn'
    if mc.objExists(locName):
        mc.delete(locName)
    mc.spaceLocator(n=locName, a=True, p=mc.getAttr("%s.translate" % boxName)[0])
    mc.parent(locName, grpName)

def cameraTurn(axe, boxName):
    """ Create camera turn
        :param axe: (str) : Front axe
        :param boxName: (str) : Bbox name """
    print "Creating camera Turn ..."
    camName = 'cam_turnPreviz1'
    refD = getBoxInfo(boxName)
    if mc.objExists(camName):
        mc.delete(camName)
    pBox = mc.getAttr("%s.translate" % boxName)[0]
    if axe == 'x':
        mc.camera(n=camName, ar=1, fl=50, p=(refD*2, pBox[1], pBox[2]), rot=(0, 90, 0))
    elif axe == '-x':
        mc.camera(n=camName, ar=1, fl=50, p=((refD*2)*-1, pBox[1], pBox[2]), rot=(0, -90, 0))
    elif axe == 'y':
        mc.camera(n=camName, ar=1, fl=50, p=(pBox[0], refD*2, pBox[2]), rot=(-90, 0, 0))
    elif axe == '-y':
        mc.camera(n=camName, ar=1, fl=50, p=(pBox[0], (refD*2)*-1, pBox[2]), rot=(90, 0, 0))
    elif axe == 'z':
        mc.camera(n=camName, ar=1, fl=50, p=(pBox[0], pBox[1], refD*2))
    elif axe == '-z':
        mc.camera(n=camName, ar=1, fl=50, p=(pBox[0], pBox[1], (refD*2)*-1), rot=(0, 180, 0))
    mc.parent(camName, 'N_camTurn')

def animTurn(duration, invert=False):
    """ Anim camera turn
        :param duration: (int) : Rotate duration in frame
        :param invert: (bool) : Invert camera rotation """
    print "Anim camera Turn ..."
    camName = 'N_camTurn'
    endR = float(360 - float(360/duration))
    mc.setKeyframe(camName, t=1, at='ry', v=0)
    mc.setKeyframe(camName, t=duration, at='ry', v=endR)
    if invert:
        mc.setKeyframe(camName, t=duration, at='ry', v=(endR*-1))
    mc.keyTangent(camName, itt="linear", ott="linear")

def createCamTurn(axe, duration):
    """ Genere camera rig fitting to selection if models are selected
        :param axe: (str) : Front axe
        :param duration: (int) : Duration """
    print "\n#-- Create Camera Turn --#"
    models = getModels()
    if selectModels(models):
        boxName = createBbox()
        cameraLocator(boxName)
        cameraTurn(axe, boxName)
        mc.delete(boxName)
        if duration < 0:
            animTurn(math.fabs(duration), invert=True)
        else:
            animTurn(duration, invert=False)
    else:
        raise IOError, "Selection or scene not valide !!!"
    print "#-- Create Camera Turn Done --#"
