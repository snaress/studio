from lib.system import procFile as pFile
from tools.maya.util.proc import procScene as pScene
from tools.maya.util.proc import procMapping as pMap
try:
    import maya.cmds as mc
    import maya.mel as ml
except:
    pass


def importPresentoir(sceneFile):
    """ Import given model file
        :param sceneFile: (str) : Model file """
    #-- Clean Model --#
    model = 'factory_presentoir'
    if mc.objExists(model):
        print "Warning: %s already in scene, clean before importing new ..." % model
        mc.delete(model)
    #-- Clean Shader --#
    shader = 'mat_factory_sol'
    if mc.objExists(shader):
        print "Warning: %s already in scene, clean before importing new ..." % shader
        mc.delete(shader)
    #-- Import Model --#
    pScene.importScene(sceneFile)

def getMat(model):
    """ Get material assigned on model
        :param model: (str) : Transform name
        :return: (dict) : Connected material """
    sg = pMap.getShadingEngine(model)
    if sg is not None:
        return pMap.getMatFromSg(sg)

def checkRenderEngine():
    """ Check if Turtle is loaded
        :return: (bool) : True if render engine is loaded """
    if not mc.pluginInfo('Turtle', q=True, l=True):
        try:
            mc.loadPlugin('Turtle')
            print "Render engine successfully loaded"
            return True
        except:
            print "Error: Can not load Turtle"
            return False
    else:
        print "Turtle already loaded"
        return True

def paramRender(imaOut, envMap):
    """ Param render for preview image
        :param imaOut: (str) : Image out file absolute path
        :param envMap: (str) : Light env map file absolute path"""
    drg = "defaultRenderGlobals"
    dr = "defaultResolution"
    tro = "TurtleRenderOptions"
    #-- Default Render Params --#
    print "Param default render globals ..."
    mc.setAttr('%s.currentRenderer' % drg, 'turtle', type='string')
    mc.setAttr('%s.imageFilePrefix' % drg, imaOut, type='string')
    mc.setAttr('%s.imfPluginKey' % drg, 'png', type='string')
    mc.setAttr('%s.animation' % drg, False)
    mc.setAttr('%s.fieldExtControl' % drg, 0)
    mc.setAttr('%s.width' % dr, 600)
    mc.setAttr('%s.height' % dr, 600)
    mc.setAttr('%s.imageSizeUnits' % dr, 0)
    mc.setAttr('%s.dotsPerInch' % dr, 72)
    mc.setAttr('%s.pixelDensityUnits' % dr, 0)
    #-- Turtle Render params --#
    print "Param turtle render params ..."
    mc.setAttr('%s.renderer' % tro, 0)
    mc.setAttr('%s.fileNameFormat' % tro, 1)
    mc.setAttr('%s.imageFormat' % tro, 9)
    mc.setAttr('%s.fileNamePrefix' % tro, imaOut, type='string')
    mc.setAttr('%s.width' % tro, 600)
    mc.setAttr('%s.height' % tro, 600)
    mc.setAttr('%s.aspectRatio' % tro, float(600 / 600))
    mc.setAttr('%s.aaMinSampleRate' % tro, 0)
    mc.setAttr('%s.aaMaxSampleRate' % tro, 2)
    #-- Turtle Environment Param --#
    print "Param turtle environment params ..."
    mc.setAttr('%s.iblImageFile' %tro, pFile.conformPath(envMap), type='string')
    mc.setAttr('%s.iblTurnDome' %tro, 130)
    mc.setAttr('%s.iblEmitLight' %tro, 1)
    mc.setAttr('%s.iblEmitDiffuse' %tro, 1)
    mc.setAttr('%s.iblEmitSpecular' %tro, 1)
    mc.setAttr('%s.iblSamples' %tro, 200)
    mc.setAttr('%s.iblIntensity' %tro, 1.5)
    mc.setAttr('%s.iblSpecularBoost' %tro, 1)
    mc.setAttr('%s.iblShadows' %tro, 1)
    mc.setAttr('%s.iblEmitPhotons' %tro, 0)
    mc.setAttr('%s.rtEnvironment' %tro, 3)
    mc.setAttr('%s.rtEnvironmentEye' %tro, 0)
    mc.setAttr('%s.rtEnvironmentRefl' %tro, 1)
    mc.setAttr('%s.rtEnvironmentRefr' %tro, 1)

def paramCam():
    """ Edit renderable camera """
    print "Param Cam ..."
    mc.setAttr('cam_factoryShape.renderable', True)
    mc.setAttr('frontShape.renderable', False)
    mc.setAttr('perspShape.renderable', False)
    mc.setAttr('sideShape.renderable', False)
    mc.setAttr('topShape.renderable', False)

def renderPreview():
    ml.eval('ilrRenderCallback(600, 600, 1, 1, "cam_factory", " -layer defaultRenderLayer")')
