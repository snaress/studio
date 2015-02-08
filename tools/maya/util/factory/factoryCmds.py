import os, shutil
import tools.maya.cmds as smc
from lib.system import procFile as pFile
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
    smc.importScene(sceneFile)

def getMat(model):
    """ Get material assigned on model
        :param model: (str) : Transform name
        :return: (dict) : Connected material """
    sg = smc.getShadingEngine(model)
    if sg:
        return smc.getMatFromSg(sg[0])

def getSceneMap():
    """ Get all texture files
        :return: (list) : Map files """
    files = mc.ls(type='file')
    maps = []
    for f in files:
        if f.startswith('map_'):
            maps.append(f)
    return maps

def checkRenderEngine(plugInName):
    """ Check if Turtle is loaded
        :param plugInName: (str) : PlugIn name
        :return: (bool) : True if render engine is loaded """
    if not mc.pluginInfo(plugInName, q=True, l=True):
        try:
            mc.loadPlugin(plugInName)
            print "Render engine %s successfully loaded" % plugInName
            return True
        except:
            print "Error: Can not load %s" % plugInName
            return False
    else:
        print "%s already loaded" % plugInName
        return True

def paramCam():
    """ Edit renderable camera """
    print "Param Cam ..."
    mc.setAttr('cam_factoryShape.renderable', True)
    mc.setAttr('frontShape.renderable', False)
    mc.setAttr('perspShape.renderable', False)
    mc.setAttr('sideShape.renderable', False)
    mc.setAttr('topShape.renderable', False)

def paramLight(renderer):
    """ Edit lights considering renderer
        :param renderer: (str) : 'turtle' or 'mentalRay' """
    print "Param Light ..."
    if renderer == 'turtle':
        mc.setAttr("lum_dir1.visibility", 0)
        mc.setAttr("lum_amb1.visibility", 0)
        mc.setAttr("env_mrIbl1.visibility", 0)
    elif renderer == 'mentalRay':
        mc.setAttr("lum_dir1.visibility", 1)
        mc.setAttr("lum_amb1.visibility", 1)
        mc.setAttr("env_mrIbl1.visibility", 1)

def paramRender(renderer, imaOut, envMap, quality='draft'):
    """ Param render for preview image
        :param renderer: (str) : 'turtle' or 'mentalRay'
        :param imaOut: (str) : Image out file absolute path
        :param envMap: (str) : Light env map file absolute path
        :param quality: (str) : 'draft' or 'preview' """
    drg = "defaultRenderGlobals"
    dr = "defaultResolution"
    #-- Default Render Params --#
    print "Param default render globals ..."
    mc.setAttr('%s.currentRenderer' % drg, renderer, type='string')
    mc.setAttr('%s.imageFilePrefix' % drg, imaOut, type='string')
    mc.setAttr('%s.imfPluginKey' % drg, 'png', type='string')
    mc.setAttr('%s.animation' % drg, False)
    mc.setAttr('%s.fieldExtControl' % drg, 0)
    mc.setAttr('%s.motionBlur' % drg, 0)
    mc.setAttr('%s.width' % dr, 600)
    mc.setAttr('%s.height' % dr, 600)
    mc.setAttr('%s.deviceAspectRatio' % dr, 1)
    mc.setAttr('%s.imageSizeUnits' % dr, 0)
    mc.setAttr('%s.dotsPerInch' % dr, 72)
    mc.setAttr('%s.pixelDensityUnits' % dr, 0)
    #-- Renderer params --#
    if renderer == 'turtle':
        paramTurtleRenderer(imaOut, envMap, quality)
    elif renderer == 'mentalRay':
        paramMentalRayRender(quality)

def paramTurtleRenderer(imaOut, envMap, quality):
    """ Param turtle params
        :param imaOut: (str) : Image out file absolute path
        :param envMap: (str) : Light env map file absolute path
        :param quality: (str) : 'draft' or 'preview' """
    tro = "TurtleRenderOptions"
    #-- Turtle Render params --#
    print "Param turtle render params ..."
    mc.setAttr('%s.renderer' % tro, 0)
    mc.setAttr('%s.fileNameFormat' % tro, 1)
    mc.setAttr('%s.imageFormat' % tro, 9)
    mc.setAttr('%s.fileNamePrefix' % tro, imaOut, type='string')
    mc.setAttr('%s.width' % tro, 600)
    mc.setAttr('%s.height' % tro, 600)
    mc.setAttr('%s.aspectRatio' % tro, 1)
    mc.setAttr('%s.aaMinSampleRate' % tro, -2)
    mc.setAttr('%s.aaMaxSampleRate' % tro, 0)
    #-- Turtle Environment Param --#
    print "Param turtle environment params ..."
    mc.setAttr('%s.iblImageFile' %tro, pFile.conformPath(envMap), type='string')
    mc.setAttr('%s.iblTurnDome' %tro, 130)
    mc.setAttr('%s.iblEmitLight' %tro, 1)
    mc.setAttr('%s.iblEmitDiffuse' %tro, 1)
    mc.setAttr('%s.iblEmitSpecular' %tro, 1)
    mc.setAttr('%s.iblSamples' %tro, 100)
    mc.setAttr('%s.iblIntensity' %tro, 1.5)
    mc.setAttr('%s.iblSpecularBoost' %tro, 1)
    mc.setAttr('%s.iblShadows' %tro, 1)
    mc.setAttr('%s.iblEmitPhotons' %tro, 0)
    mc.setAttr('%s.rtEnvironment' %tro, 3)
    mc.setAttr('%s.rtEnvironmentEye' %tro, 0)
    mc.setAttr('%s.rtEnvironmentRefl' %tro, 1)
    mc.setAttr('%s.rtEnvironmentRefr' %tro, 1)
    if quality == 'preview':
        mc.setAttr('%s.aaMinSampleRate' % tro, 0)
        mc.setAttr('%s.aaMaxSampleRate' % tro, 2)
        mc.setAttr('%s.iblSamples' %tro, 200)

def paramMentalRayRender(quality):
    """ Param mentalRay params
        :param quality: (str) : 'draft' or 'preview' """
    mdo = "miDefaultOptions"
    #-- Mental Ray Render Params --#
    mc.setAttr('%s.motionBlur' % mdo, 0)
    mc.setAttr('%s.miRenderUsing' % mdo, 2)
    mc.setAttr('%s.minSamples' % mdo, -2)
    mc.setAttr('%s.maxSamples' % mdo, 0)
    if quality == 'preview':
        mc.setAttr('%s.minSamples' % mdo, 0)
        mc.setAttr('%s.maxSamples' % mdo, 2)
    #-- Mental Ray Environment Params --#
    shape = mc.listRelatives("env_mrIbl1", s=True, ni=True)
    mc.connectAttr("%s.message" % shape[0], "mentalrayGlobals.imageBasedLighting", f=True)

def renderPreview(imaPath):
    """ Launch rendering and save image in user path
        :return: (list) : Render result """
    cam = "cam_factory"
    imaOut = mc.getAttr("defaultRenderGlobals.imageFilePrefix")
    outFile = pFile.conformPath(os.path.join(imaPath, '%s.png' % imaOut))
    ml.eval('renderWindowRenderCamera render renderView %s;' % cam)
    if os.path.exists(outFile):
        print "Remove outFile file: %s" % outFile
        os.remove(outFile)
    result = mc.renderWindowEditor('renderView', e=True, wi=outFile)
    return result

def saveShader(root, category, subCategory, matName, previewFile, matDict):
    """ Save shader to factory
        :param root: (str) : Factory root path
        :param category: (str) : Category name
        :param subCategory: (str) : SubCategory name
        :param matName: (str) : Shader name
        :param previewFile: (str) : Preview image absolute path
        :param matDict: (dict) : Shader dict """
    rootPath = pFile.conformPath(os.path.join(root, category, subCategory))
    #-- Check RootPath --#
    if not os.path.exists(rootPath):
        raise IOError, "!!! ERROR: RootPath not found: %s" % rootPath
    #-- Check MatPath --#
    matPath = pFile.conformPath(os.path.join(rootPath, 'sahder', matName))
    if os.path.exists(matPath):
        raise IOError, "!!! ERROR: Shader already exists: %s" % matPath
    #-- Save Shader --#
    cpPreviewFile(previewFile, rootPath, matName)
    mapFiles = cpTextureFiles(rootPath, matName)
    saveMat(matDict, rootPath, matName)
    saveData(rootPath, matName, matDict, mapFiles)

def cpPreviewFile(previewFile, matPath, matName):
    """ Copy preview image file to factory
        :param previewFile: (str) : Preview image absolute path
        :param matName: (str) : Shader name
        :param matPath: (str) : Material absolute path """
    ext = os.path.splitext(os.path.basename(previewFile))
    preview = "%s%s" % (matName, ext[1])
    dst = pFile.conformPath(os.path.join(matPath, preview))
    print "Copy preview file ..."
    try:
        shutil.copy(previewFile, dst)
        print "Preview file successfully copied."
    except:
        raise IOError, "!!! ERROR: Can not copy previewFile:\n\t src: %s\n\t dst: %s" % (previewFile, dst)

def cpTextureFiles(matPath, matName):
    """ Copy texture file to factory
        :param matPath: (str) : Material absolute path
        :param matName: (str) : Shader name
        :return: (list) : Map files if exists """
    maps = getSceneMap()
    if maps:
        print "Texure file detected, copy maps."
        #-- Create Texture Folder --#
        texturePath = pFile.conformPath(os.path.join(matPath, 'texture'))
        if not os.path.exists(texturePath):
            try:
                os.mkdir(texturePath)
                print "Folder 'texture' successfully created."
            except:
                raise IOError, "Can not create folder %s" % texturePath
        #-- Create Map Folder --#
        mapPath = pFile.conformPath(os.path.join(texturePath, matName))
        if not os.path.exists(mapPath):
            try:
                os.mkdir(mapPath)
                print "Folder %r successfully created." % matName
            except:
                raise IOError, "Can not create folder %r" % matName
        #-- Copy Texture Files --#
        mapFiles = []
        for mapNode in maps:
            texture = mc.getAttr("%s.fileTextureName" % mapNode)
            if not os.path.exists(texture):
                raise IOError, "!!! ERROR: Texture %r not found." % texture
            dst = pFile.conformPath(os.path.join(mapPath, os.path.basename(texture)))
            print "Copy texture file ..."
            try:
                shutil.copy(texture, dst)
                print "Texture file successfully copied: %s" % dst
            except:
                raise IOError, "!!! ERROR: Can not copy textureFile:\n\t src: %s\n\t dst: %s" % (texture, dst)
            #-- Edit MapNode File Path --#
            mc.setAttr("%s.fileTextureName" % mapNode, dst, type='string')
            mapFiles.append(dst)
        return mapFiles

def saveMat(matDict, matPath, matName):
    """ Save shader to factory
        :param matDict: (dict) : Shader dict
        :param matPath: (str) : Material absolute path
        :param matName: (str) : Shader name """
    mayaShaders = ['ss', 'ds', 'vs']
    #-- Get Materials --#
    mc.select(cl=True)
    for k in matDict.keys():
        if k in mayaShaders:
            if matDict[k] is not None:
                mc.select(matDict[k], add=True)
        else:
            mc.select(matDict[k], add=True)
    #-- Create Shader Folder --#
    shaderPath = pFile.conformPath(os.path.join(matPath, 'shader'))
    if not os.path.exists(shaderPath):
        print "Creating folder 'shader' ..."
        try:
            os.mkdir(shaderPath)
            print "Folder 'shader' successfully created."
        except:
            raise IOError, "Can not create folder 'shader'"
    #-- Save Materials --#
    shaderFile = os.path.join(shaderPath, '%s.ma' % matName)
    smc.exportSel(shaderFile)

def saveData(matPath, matName, matDict, mapFiles):
    """ Write shader's data to python file
        :param matPath: (str) : Material absolute path
        :param matName: (str) : Shader name
        :param matDict: (dict) : Shader dict
        :param mapFiles: (list) : Texture files """
    data = ['Name = "%s"' % matName]
    mayaShaders = ['ss', 'ds', 'vs']
    #-- Maya Shaders --#
    if matDict['ss'] is not None:
        data.append('SurfaceShader = "%s"' % matDict['ss'])
    if matDict['ds'] is not None:
        data.append('DisplaceShader = "%s"' % matDict['ds'])
    if matDict['vs'] is not None:
        data.append('VolumeShader = "%s"' % matDict['vs'])
    #-- Mental Ray Shaders --#
    for k, v in matDict.iteritems():
        if k not in mayaShaders:
            data.append('%s = "%s -- (mrShader)"' % (k, v))
    #-- Map Files --#
    if mapFiles is not None:
        data.append('mapFiles = %s' % mapFiles)
    #-- Create Data Path --#
    dataPath = pFile.conformPath(os.path.join(matPath, '_data'))
    if not os.path.exists(dataPath):
        print "Creating folder '_data' ..."
        try:
            os.mkdir(dataPath)
            print "Folder '_data' successfully created."
        except:
            raise IOError, "Can not create folder '_data"
    #-- Save Data --#
    dataFile = os.path.join(dataPath, '%s.py' % matName)
    pFile.writeFile(dataFile, str('\n'.join(data)))
