import os
from lib.system import procFile as pFile
try:
    import maya.cmds as mc
except:
    pass


def loadRenderEngine(plugInName):
    """ Check if given render engine is loaded, load it if needed
        :param plugInName: (str) : PlugIn name ('Mayatomr', 'Turtle')
        :return: (bool) : True if render engine is loaded """
    if not mc.pluginInfo(plugInName, q=True, l=True):
        try:
            mc.loadPlugin(plugInName)
            log = "Render engine %s successfully loaded" % plugInName
            return True, log
        except:
            log = "Error: Can not load %s" % plugInName
            return False, log
    else:
        log = "%s already loaded" % plugInName
        return True, log

def initMrDefaultNodes(verbose=True):
    """ Create mentalRay default nodes
        :param verbose: (bool) : Enable verbose """
    print "Init Mentalray default nodes ..."
    mrNodes = {'mentalrayGlobals': 'mentalrayGlobals', 'mentalrayItemsList': 'mentalrayItemsList',
               'mentalrayOptions': 'miDefaultOptions', 'mentalrayFramebuffer': 'miDefaultFramebuffer'}
    #-- Create mrNodes --#
    create = False
    for mrNode in mrNodes.keys():
        if not mc.objExists(mrNodes[mrNode]):
            print "\tCreate mrNode %s named %s" % (mrNode, mrNodes[mrNode])
            mc.createNode(mrNode, n=mrNodes[mrNode])
            create = True
    #-- Link mrNodes --#
    if create:
        conns = {'mentalrayGlobals.options': 'miDefaultOptions.message',
                 'mentalrayItemsList.options[0]': 'miDefaultOptions.message',
                 'mentalrayGlobals.framebuffer': 'miDefaultFramebuffer.message',
                 'mentalrayItemsList.framebuffers[0]': 'miDefaultFramebuffer.message',
                 'mentalrayItemsList.globals': 'mentalrayGlobals.message'}
        for dst, src in conns.iteritems():
            try:
                mc.connectAttr(src, dst)
                if verbose:
                    print "\tConnect %s to %s" % (src, dst)
            except:
                if verbose:
                    print "\tSkip connection %s to %s" % (src, dst)

def getImageFormatIndex(format, turtleRE=False):
    """ Get format index
        :param format: (str) : Image file format
        :return: (int), (int) : Image format, Image data type """
    if not turtleRE:
        if format == 'tif':
            return 3, 2
        elif format == 'iff':
            return 7, 2
        elif format == 'jpg':
            return 8, 0
        elif format == 'tga':
            return 19, 2
        elif format == 'png':
            return 32, 2
        elif format == 'exr':
            return 51, 5
    else:
        if format == 'tif':
            return 3, 2
        elif format == 'iff':
            return 6, 2
        elif format == 'jpg':
            print "No jpg format with turtle !!!"
        elif format == 'tga':
            return 0, 2
        elif format == 'png':
            return 9, 2
        elif format == 'exr':
            return 2, 5

def getRenderableCameraShape():
    """ List renderable cameraShape in scene
        :return: (list) : Renderable cameraShape """
    cams = []
    for cam in mc.ls(type='camera'):
        if mc.getAttr('%s.renderable' % cam):
            cams.append(cam)
    return cams

def getRenderableCamera():
    """ List renderable camera in scene
        :return: (list) : Renderable camera """
    cams = []
    for cam in getRenderableCameraShape():
        parent = mc.listRelatives(cam, p=True)
        if parent:
            cams.append(parent[0])
    return cams

def setCameraRenderable(camera):
    """ Set given camera renderable, switch others to false
        :param camera: (str) or (list) : Camera name """
    cameras = camera
    if isinstance(camera, str):
        cameras = [camera]
    for cam in mc.ls(type='camera'):
        parent = mc.listRelatives(cam, p=True)
        if parent:
            if parent[0] in cameras:
                mc.setAttr("%s.renderable" % parent[0], True)
            else:
                mc.setAttr("%s.renderable" % parent[0], False)

def paramRenderOptions():
    """ Render options
        :return: (dict) : Render options
            :keyword project: (str) : Maya project path
            :keyword camera: (str) or (list) : Camera name to render (must be transform name)
            :keyword alphaChannel: (int) : Camera alpha channel on or off
            :keyword depthChannel: (int) : Camera depth channel on or off
            :keyword output: (str) : Image file output name (relativePath/imageName)
            :keyword format: (str) : 'jpg', 'png', 'exr' or 'tga'
            :keyword anim: (int) : Enable sequence mode
            :keyword padding: (int) : Frame padding
            :keyword range: (int) or (list) or (tuple): Single Frame, Frames list, range
            :keyword skipExistingFrames: (int) : Skip existing file on or off
            :keyword size: (tuple) : Frame width and height
            :keyword pixelAspect: (int) : Pixel aspect ratio
            :keyword samples: (tuple) : Sample min, Sample max
            :keyword shadows: (str) : 'off', 'simple', 'sort' or 'segments'
            :keyword shadowMaps: (str) : 'off', 'on', 'openGL' or 'detail'
            :keyword shadowMapRebuild: (str) : 'off', 'on' or 'merge
            :keyword motionBlur: (str) : 'off', 'linear' or 'exact'
            :keyword mbBy: (float) : Motion blur coeff
            :keyword mbShutter: (float) : Motion blur shutter
            :keyword mbDelay: (float) : Motion blur shutter delay
            :keyword mbSteps: (int) : Motion blur steps """
    return {'project': None, 'camera': None, 'alphaChannel': None, 'depthChannel': None,
            'output': None, 'format': None, 'anim': None, 'padding': None, 'range': None,
            'skipExistingFrames': None, 'size': None, 'pixelAspect': None, 'samples': None,
            'shadows': None, 'shadowMaps': None, 'shadowMapRebuild': None,
            'motionBlur': None, 'mbBy': None, 'mbShutter': None, 'mbDelay': None, 'mbSteps': None}


class ParamRender(object):

    def __init__(self, renderer, options, logLvl='info'):
        """ Set render params with given renderer
            :param renderer: (str) : 'mentalRay', 'turtle
            :param options: (dict) : Render options
            :param logLvl: (str) : 'critical', 'error', 'warning', 'info', 'debug' """
        self.log = pFile.Logger(title="ParamRender", level=logLvl)
        self.log.info("#========== PARAM RENDER: %s ==========#" % renderer)
        self.drg = "defaultRenderGlobals"
        self.dr = "defaultResolution"
        self.mido = "miDefaultOptions"
        self.tro = "TurtleRenderOptions"
        self.renderer = renderer
        self.options = options
        self.setParamRender()

    def setParamRender(self):
        """ Set param render with given options """
        #-- Default Render Globals --#
        self.initRenderEngine()
        self.setProject()
        self.setCamera()
        self.setOutput()
        self.setRange()
        self.setSize()
        self.setMotionBlur()
        #-- MentalRay Default Options --#
        if self.renderer == 'mentalRay':
            self.setMrSamples()
            self.setMrShadows()
            self.setMrMotionBlur()
        #-- Turtle Default Options --#
        elif self.renderer == 'turtle':
            self.setTurtleOutput()
            self.setTurtleRange()
            self.setTurtleSize()
            self.setTurtleSamples()

    def initRenderEngine(self):
        """ Init render engine plugin """
        self.log.info("#-- Init Render Engine --#")
        #-- Load Plugin --#
        result = False
        log = ""
        if self.renderer == 'mentalRay':
            result, log = loadRenderEngine('Mayatomr')
            if self.log.level == 'debug':
                initMrDefaultNodes(verbose=True)
            else:
                initMrDefaultNodes(verbose=False)
        if self.renderer == 'turtle':
            result, log = loadRenderEngine('Turtle')
        #-- Check Load --#
        if not result:
            self.log.error(log)
            raise IOError, log
        self.log.info(log)
        #-- Set Current Renderer --#
        mc.setAttr('%s.currentRenderer' % self.drg, self.renderer, type='string')

    def setProject(self):
        """ Set maya project """
        self.log.info("#-- Set Project --#")
        if self.options['project'] is None:
            self.log.debug("Use current project: %s" % mc.workspace(q=True, rd=True))
        else:
            self.log.debug("Option 'project' detected: %s" % self.options['project'])
            #-- Check Project Path --#
            if not os.path.exists(self.options['project']):
                log = "Project path not found : %s" % self.options['project']
                self.log.error(log)
                raise IOError, log
            #-- Set Project Path --#
            mc.workspace(self.options['project'], o=True)
            mc.workspace(dir='/'.join(self.options['project'].split('/')[:-1]))
            self.log.debug("Project Path: %s" % mc.workspace(q=True, fn=True))
            self.log.debug("Project Dir: %d" % mc.workspace(q=True, dir=True))

    def setCamera(self):
        """ Set renderable camera """
        self.log.info("#-- Set Camera --#")
        if self.options['camera'] is None:
            self.log.debug("Use current renderable camera: %s" % getRenderableCamera())
        else:
            self.log.debug("Option 'camera' detected: %s" % self.options['camera'])
            #-- Renderable Camera --#
            cameras = self.options['camera']
            if isinstance(self.options['camera'], str):
                cameras = [self.options['camera']]
            setCameraRenderable(cameras)
            for cam in cameras:
                #-- Alpha Channel --#
                if self.options['alphaChannel'] is None:
                    self.log.debug("Use current alphaChannel for %s" % cam)
                else:
                    self.log.debug("Option 'alphaChannel' detected for cam %s: %s" % (cam, self.options['alphaChannel']))
                    mc.setAttr("%s.mask" % cam, self.options['alphaChannel'])
                #-- Depth Channel --#
                if self.options['depthChannel'] is None:
                    self.log.debug("Use current depthChannel for %s" % cam)
                else:
                    self.log.debug("Option 'depthChannel' detected for cam %s: %s" % (cam, self.options['depthChannel']))
                    mc.setAttr("%s.depth" % cam, self.options['depthChannel'])

    def setOutput(self):
        """ Set output file params """
        self.log.info("#-- Set Output --#")
        #-- Image File Prefix --#
        if self.options['output'] is None:
            self.log.debug("Use current output: %s" % mc.getAttr("%s.ifp" % self.drg))
        else:
            self.log.debug("Option 'output' detected: %s" % self.options['output'])
            mc.setAttr("%s.imageFilePrefix" % self.drg, self.options['output'], type='string')
        #-- Image Format --#
        if self.options['format'] is None:
            self.log.debug("Use current format: %s" % mc.getAttr("%s.imfPluginKey" % self.drg))
        else:
            self.log.debug("Option 'format' detected: %s" % self.options['format'])
            extIndex, dataIndex = getImageFormatIndex(self.options['format'])
            mc.setAttr("%s.imageFormat" % self.drg, extIndex)
            mc.setAttr("%s.imfPluginKey" % self.drg, self.options['format'], type='string')
            if self.renderer == 'mentalRay':
                mc.setAttr("miDefaultFramebuffer.datatype", dataIndex)
        #-- Extension Rule --#
        if self.options['anim'] is None:
            self.log.debug("Use current extension rule: animatedExt = %s" % mc.getAttr("%s.animation" % self.drg))
        else:
            self.log.debug("Option 'anim' detected: %s" % self.options['anim'])
            mc.setAttr("%s.animation" % self.drg, self.options['anim'])
            if self.options['anim']:
                mc.setAttr("%s.outFormatControl" % self.drg, 0)
                mc.setAttr("%s.putFrameBeforeExt" % self.drg, 1)
                mc.setAttr("%s.periodInExt" % self.drg, 1)
            else:
                mc.setAttr("%s.outFormatControl" % self.drg, 0)
        #-- Padding --#
        if self.options['padding'] is None:
            self.log.debug("Use current padding: %s" % mc.getAttr("%s.extensionPadding" % self.drg))
        else:
            self.log.debug("Option 'padding' detected: %s" % self.options['padding'])
            mc.setAttr("%s.extensionPadding" % self.drg, self.options['padding'])

    def setRange(self):
        """ Set frame range """
        self.log.info("#-- Set Range --#")
        #-- Range --#
        if self.options['range'] is None:
            if mc.getAttr("%s.animation" % self.drg):
                self.log.debug("Use current range: (%s, %s, %s)" % (mc.getAttr('%s.startFrame' % self.drg),
                                                                    mc.getAttr('%s.endFrame' % self.drg),
                                                                    mc.getAttr('%s.byFrameStep' % self.drg)))
            else:
                self.log.debug("Use current frame: %s" % mc.currentTime(q=True))
        else:
            self.log.debug("Option 'range' detected: %s" % str(self.options['range']))
            if isinstance(self.options['range'], tuple):
                mc.setAttr("%s.startFrame" % self.drg, self.options['range'][0])
                mc.setAttr("%s.endFrame"% self.drg, self.options['range'][1])
                mc.setAttr("%s.byFrameStep" % self.drg, self.options['range'][2])
        #-- Frame Option --#
        if self.options['skipExistingFrames'] is None:
            self.log.debug("Use current skipExistingFrames: %s" % mc.getAttr("%s.skipExistingFrames" % self.drg))
        else:
            self.log.debug("Option 'skipExistingFrames' detected: %s" % str(self.options['skipExistingFrames']))
            mc.setAttr("%s.skipExistingFrames" % self.drg, self.options['skipExistingFrames'])

    def setSize(self):
        """ Set Frame size """
        self.log.info("#-- Set Size --#")
        #-- Frame Size --#
        if self.options['size'] is None:
            self.log.debug("Use current frame size: %s x %s" % (mc.getAttr("%s.width" % self.dr),
                                                                mc.getAttr("%s.height" % self.dr)))
        else:
            self.log.debug("Option 'size' detected: %s x %s" % (self.options['size'][0], self.options['size'][1]))
            mc.setAttr("%s.width" % self.dr, self.options['size'][0])
            mc.setAttr("%s.height" % self.dr, self.options['size'][1])
            #-- Aspect Ratio --#
            ar = ( float(self.options['size'][0]) / float(self.options['size'][1]) )
            mc.setAttr("%s.deviceAspectRatio" % self.dr, ar)
        #-- Pixel Aspect --#
        if self.options['pixelAspect'] is None:
            self.log.debug("Use current pixel aspect: %s" % mc.getAttr("%s.pixelAspect" % self.dr))
        else:
            self.log.debug("Option 'pixelAspect' detected: %s" % (self.options['pixelAspect']))
            mc.setAttr("%s.pixelAspect" % self.dr, self.options['pixelAspect'])

    def setMotionBlur(self):
        """ Set motion blur """
        self.log.info("#-- Set Motion Blur --#")
        #-- Motion Blur --#
        if self.options['motionBlur'] is None:
            self.log.debug("Use current 'motionBlur': %s" % mc.getAttr("%s.motionBlur" % self.drg))
        else:
            self.log.debug("Option 'motionBlur' detected: %s" % self.options['motionBlur'])
            if self.options['motionBlur'] == 'off':
                mc.setAttr("%s.motionBlur" % self.drg, 0)
            elif self.options['motionBlur'] == 'linear':
                mc.setAttr("%s.motionBlur" % self.drg, 1)
                mc.setAttr("%s.motionBlurType" % self.drg, 0)
            elif self.options['motionBlur'] == 'exact':
                mc.setAttr("%s.motionBlur" % self.drg, 1)
                mc.setAttr("%s.motionBlurType" % self.drg, 1)
        #-- Motion Blur Coef --#
        if self.options['mbBy'] is None:
            self.log.debug("Use current 'motionBlurBy': %s" % mc.getAttr("%s.motionBlurByFrame" % self.drg))
        else:
            self.log.debug("Option 'motionBlurBy' detected: %s" % self.options['mbBy'])
            mc.setAttr("%s.motionBlurByFrame" % self.drg, self.options['mbBy'])

    def setMrSamples(self):
        """ Set mentalRay samples """
        self.log.info("#-- Set MentalRay Samples --#")
        if self.options['samples'] is None:
            self.log.debug("Use current samples: %s x %s" % (mc.getAttr("%s.minSamples" % self.mido),
                                                             mc.getAttr("%s.maxSamples" % self.mido)))
        else:
            self.log.debug("Option 'samples' detected: %s x %s" % (self.options['samples'][0],
                                                                   self.options['samples'][1]))
            mc.setAttr("%s.miRenderUsing" % self.mido, 2)
            mc.setAttr("%s.minSamples" % self.mido, self.options['samples'][0])
            mc.setAttr("%s.maxSamples" % self.mido, self.options['samples'][1])

    def setMrShadows(self):
        """ Set mentalRay shadows """
        self.log.info("#-- Set MentalRay Shadows --#")
        #-- Shadows --#
        if self.options['shadows'] is None:
            self.log.debug("Use current shadow: %s" % mc.getAttr("%s.shadowMethod" % self.mido))
        else:
            self.log.debug("Option 'shadows' detected: %s" % self.options['shadows'])
            if self.options['shadows'] == 'off':
                mc.setAttr("%s.shadowMethod" % self.mido, 0)
            elif self.options['shadows'] == 'simple':
                mc.setAttr("%s.shadowMethod" % self.mido, 1)
            elif self.options['shadows'] == 'sort':
                mc.setAttr("%s.shadowMethod" % self.mido, 2)
            elif self.options['shadows'] == 'segments':
                mc.setAttr("%s.shadowMethod" % self.mido, 3)
        #-- Shadow Maps --#
        if self.options['shadowMaps'] is None:
            self.log.debug("Use current shadowMap: %s" % mc.setAttr("%s.shadowMaps" % self.mido))
        else:
            self.log.debug("Option 'shadowMaps' detected: %s" % self.options['shadowMaps'])
            if self.options['shadowMaps'] == 'off':
                mc.setAttr("%s.shadowMaps" % self.mido, 0)
            elif self.options['shadowMaps'] == 'on':
                mc.setAttr("%s.shadowMaps" % self.mido, 1)
            elif self.options['shadowMaps'] == 'openGL':
                mc.setAttr("%s.shadowMaps" % self.mido, 2)
            elif self.options['shadowMaps'] == 'detail':
                mc.setAttr("%s.shadowMaps" % self.mido, 3)
        #-- Shadow Maps Rebuild --#
        if self.options['shadowMapRebuild'] is None:
            self.log.debug("Use current shadowMapRebuild: %s" % mc.setAttr("%s.rebuildShadowMaps" % self.mido))
        else:
            self.log.debug("Option 'shadowMapRebuild' detected: %s" % self.options['shadowMapRebuild'])
            if self.options['shadowMapRebuild'] == 'off':
                mc.setAttr("%s.rebuildShadowMaps" % self.mido, 0)
            elif self.options['shadowMapRebuild'] == 'on':
                mc.setAttr("%s.rebuildShadowMaps" % self.mido, 1)
            elif self.options['shadowMapRebuild'] == 'merge':
                mc.setAttr("%s.rebuildShadowMaps" % self.mido, 2)

    def setMrMotionBlur(self):
        """ Set mentalRay motion blur """
        self.log.info("#-- Set MentalRay Motion Blur --#")
        #-- Motion Blur --#
        if self.options['motionBlur'] is None:
            self.log.debug("Use current 'motionBlur': %s" % mc.getAttr("%s.motionBlur" % self.mido))
        else:
            self.log.debug("Option 'motionBlur' detected: %s" % self.options['motionBlur'])
            if self.options['motionBlur'] == 'off':
                mc.setAttr("%s.motionBlur" % self.mido, 0)
            elif self.options['motionBlur'] == 'linear':
                mc.setAttr("%s.motionBlur" % self.mido, 1)
            elif self.options['motionBlur'] == 'exact':
                mc.setAttr("%s.motionBlur" % self.mido, 2)
        #-- Motion Blur Coef --#
        if self.options['mbBy'] is None:
            self.log.debug("Use current 'motionBlurBy': %s" % mc.getAttr("%s.motionBlurBy" % self.mido))
        else:
            self.log.debug("Option 'motionBlurBy' detected: %s" % self.options['mbBy'])
            mc.setAttr("%s.motionBlurBy" % self.mido, self.options['mbBy'])
        #-- Motion Blur Shutter --#
        if self.options['mbShutter'] is None:
            self.log.debug("Use current 'motionBlurShutter': %s" % mc.getAttr("%s.shutter" % self.mido))
        else:
            self.log.debug("Option 'motionBlurShutter' detected: %s" % self.options['mbShutter'])
            mc.setAttr("%s.shutter" % self.mido, self.options['mbShutter'])
        #-- Motion Blur Delay --#
        if self.options['mbDelay'] is None:
            self.log.debug("Use current 'motionBlurDelay': %s" % mc.getAttr("%s.shutterDelay" % self.mido))
        else:
            self.log.debug("Option 'motionBlurDelay' detected: %s" % self.options['mbDelay'])
            mc.setAttr("%s.shutterDelay" % self.mido, self.options['mbDelay'])
        #-- Motion Blur Steps --#
        if self.options['mbSteps'] is None:
            self.log.debug("Use current 'motionBlurSteps': %s" % mc.getAttr("%s.motionSteps" % self.mido))
        else:
            self.log.debug("Option 'motionBlurSteps' detected: %s" % self.options['mbSteps'])
            mc.setAttr("%s.motionSteps" % self.mido, self.options['mbSteps'])

    def setTurtleOutput(self):
        """ Set Turtle Output options """
        self.log.info("#-- Set Turtle Output --#")
        mc.setAttr('%s.renderer' % self.tro, 0)
        #-- File Name Format --#
        if self.options['output'] is None:
            self.log.debug("Use current output: %s" % mc.getAttr("%s.fileNamePrefix" % self.tro))
        else:
            self.log.debug("Option 'output' detected: %s" % self.options['output'])
            mc.setAttr("%s.fileNamePrefix" % self.tro, self.options['output'], type='string')
        #-- Image Format --#
        if self.options['format'] is None:
            self.log.debug("Use current 'fileFormat': %s" % mc.getAttr("%s.imageFormat" % self.tro))
        else:
            self.log.debug("Option 'imageFileFormat' detected: %s" % self.options['format'])
            if self.options['format'] == 'jpg':
                self.log.error("jpg format not allowed with turtle, use png instead !!!")
                extIndex, dataIndex = getImageFormatIndex('png', turtleRE=True)
            else:
                extIndex, dataIndex = getImageFormatIndex(self.options['format'], turtleRE=True)
            mc.setAttr("%s.imageFormat" % self.tro, extIndex)
        #-- Image File Format --#
        if self.options['anim'] is None:
            self.log.debug("Use current 'imageFileFormat': %s" % mc.getAttr("%s.fileNameFormat" % self.tro))
        else:
            self.log.debug("Option 'imageFileFormat' detected: %s" % self.options['anim'])
            if self.options['anim']:
                mc.setAttr("%s.fileNameFormat" % self.tro, 2)
            else:
                mc.setAttr("%s.fileNameFormat" % self.tro, 1)

    def setTurtleRange(self):
        """ Set turtle frame range """
        self.log.info("#-- Set Turtle Range --#")
        if self.options['range'] is None:
            self.log.debug("Use current range: (%s, %s, %s)" % (mc.getAttr("%s.startFrame" % self.tro),
                                                                mc.getAttr("%s.endFrame" % self.tro),
                                                                mc.getAttr("%s.frameStep" % self.tro)))
        else:
            self.log.debug("Option 'range' detected: %s" % str(self.options['range']))
            if isinstance(self.options['range'], tuple):
                mc.setAttr("%s.startFrame" % self.tro, self.options['range'][0])
                mc.setAttr("%s.endFrame" % self.tro, self.options['range'][1])
                mc.setAttr("%s.frameStep" % self.tro, self.options['range'][2])

    def setTurtleSize(self):
        """ Set turtle frame size """
        self.log.info("#-- Set Turtle Size --#")
        #-- Frame Size --#
        if self.options['size'] is None:
            self.log.debug("Use current frame size: %s x %s" % (mc.getAttr("%s.width" % self.tro),
                                                                mc.getAttr("%s.height" % self.tro)))
        else:
            self.log.debug("Option 'size' detected: %s x %s" % (self.options['size'][0], self.options['size'][1]))
            mc.setAttr("%s.width" % self.tro, self.options['size'][0])
            mc.setAttr("%s.height" % self.tro, self.options['size'][1])
            #-- Aspect Ratio --#
            ar = ( float(self.options['size'][0]) / float(self.options['size'][1]) )
            mc.setAttr("%s.aspectRatio" % self.tro, ar)

    def setTurtleSamples(self):
        """ Set turtle samples """
        self.log.info("#-- Set Turtle Samples --#")
        if self.options['samples'] is None:
            self.log.debug("Use current samples: %s x %s" % (mc.getAttr("%s.aaMinSampleRate" % self.tro),
                                                             mc.getAttr("%s.aaMaxSampleRate" % self.tro)))
        else:
            self.log.debug("Option 'samples' detected: %s x %s" % (self.options['samples'][0],
                                                                   self.options['samples'][1]))
            mc.setAttr('%s.aaMinSampleRate' % self.tro, self.options['samples'][0])
            mc.setAttr('%s.aaMaxSampleRate' % self.tro, self.options['samples'][1])

