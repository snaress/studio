import os, math
from lib.env import studio
from lib.system import procFile as pFile
from lib.system import procMath as pMath
from tools.maya.util.proc import procScene as pScene
from tools.maya.util.proc import procModeling as pMode
from tools.maya.util.proc import procRender as pRender
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
    pMode.creeBoxOnSelected(name=boxName, returnShape=True)
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
    #-- Lock Attributes --#
    for attr in ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']:
        mc.setAttr("%s.%s" % (grpName, attr), l=True, k=False, cb=False)
    #-- Create Locator --#
    locName = 'N_camTurn'
    if mc.objExists(locName):
        mc.delete(locName)
    # mc.spaceLocator(n=locName, a=True, p=mc.getAttr("%s.translate" % boxName)[0])
    mc.spaceLocator(n=locName)
    mc.setAttr("%s.tx" % locName, mc.getAttr("%s.translate" % boxName)[0][0])
    mc.setAttr("%s.ty" % locName, mc.getAttr("%s.translate" % boxName)[0][1])
    mc.setAttr("%s.tz" % locName, mc.getAttr("%s.translate" % boxName)[0][2])
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
    mc.camera(n=camName, ar=1, fl=50)
    #-- Set Attributes --#
    if axe == 'x':
        mc.setAttr("%s.tx" % camName, refD*2)
        mc.setAttr("%s.ry" % camName, 90)
    elif axe == '-x':
        mc.setAttr("%s.tx" % camName, (refD*2)*-1)
        mc.setAttr("%s.ry" % camName, -90)
    elif axe == 'y':
        mc.setAttr("%s.ty" % camName, refD*2)
        mc.setAttr("%s.rx" % camName, -90)
    elif axe == '-y':
        mc.setAttr("%s.ty" % camName, (refD*2)*-1)
        mc.setAttr("%s.rx" % camName, 90)
    elif axe == 'z':
        mc.setAttr("%s.tz" % camName, refD*2)
    elif axe == '-z':
        mc.setAttr("%s.tz" % camName, (refD*2)*-1)
        mc.setAttr("%s.ry" % camName, 180)
    #-- Lock Attributes --#
    for attr in ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']:
        mc.setAttr("%s.%s" % (camName, attr), l=True, k=False, cb=False)
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

def paramRender(**kwargs):
    """ Param Render
        :param kwargs: (dict) : Param render """
    if createPath(kwargs['renderPath'], kwargs['imaPath']):
        options = pRender.paramRenderOptions()
        options['camera'] = 'cam_turnPreviz1'
        options['output'] = "%s/%s" % (kwargs['imaPath'], kwargs['imaName'])
        options['format'] = kwargs['extension']
        options['anim'] = 1
        options['padding'] = kwargs['padding']
        options['range'] = (kwargs['start'], kwargs['stop'], kwargs['step'])
        options['skipExistingFrames'] = 0
        options['size'] = (kwargs['width'], kwargs['height'])
        options['pixelAspect'] = 1
        options['samples'] = (0, 2)
        options['shadows'] = 'simple'
        options['shadowMaps'] = 'on'
        options['motionBlur'] = 'off'
        pRender.ParamRender(kwargs['renderer'], options, logLvl='debug')

def createPath(rootPath, imagePath):
    """ Check rootPath and create folder if needed
        :param rootPath: (str) : Root path
        :param imagePath: (str) : Relative path
        :return: (bool) : True if success """
    if not os.path.exists(rootPath):
        raise IOError, "Root path not found !!!: %s" % rootPath
    checkPath = rootPath
    for path in imagePath.split('/'):
        checkPath = pFile.conformPath(os.path.join(checkPath, path))
        if not os.path.exists(checkPath):
            try:
                os.mkdir(checkPath)
                print "Create folder %s in %s" % (path, checkPath)
            except:
                raise IOError, "Can not create folder %s in %s" % (path, checkPath)
    return True

def launchRender(renderer):
    """ Launch render in external process """
    #-- save Tmp File --#
    wsInfo = pScene.wsToDict()
    tmpPath = pFile.conformPath(os.path.join(wsInfo['projectPath'], wsInfo['fileRules']['diskCache']))
    tmpFile = "previz_turn_%s__%s__%s.ma" % (wsInfo['projectName'], pFile.getDate(), pFile.getTime())
    tmpAbsPath = pFile.conformPath(os.path.join(tmpPath, tmpFile))
    print "Saving tmp file: ", tmpAbsPath
    pScene.saveSceneAs(tmpAbsPath, force=True, keepCurrentName=False)
    if renderer == 'mr':
        cmd = '%s -r %s -mr:v 5 %s' % (os.path.normpath(studio.mayaRender), renderer, os.path.normpath(tmpAbsPath))
    else:
        cmd = '%s -r %s %s' % (os.path.normpath(studio.mayaRender), renderer, os.path.normpath(tmpAbsPath))
    os.system('start %s' % cmd)

