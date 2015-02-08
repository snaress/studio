import os
import tools.maya.cmds as smc
from PyQt4 import QtGui
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from tools.maya.camera.camPrez.ui import camPrezUI
from tools.maya.camera.camPrez import camPrezCmds as cpCmds
try:
    import maya.cmds as mc
except:
    pass


class CamPrez(QtGui.QMainWindow, camPrezUI.Ui_mwCamPrez):

    def __init__(self, parent=None):
        self.log = pFile.Logger(title="camPrez")
        self.log.info("#-- Launching CamPrez Ui --#")
        super(CamPrez, self).__init__(parent)
        self._setupUi()
        self.rf_imageExtension()
        self.rf_renderInfo()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup main ui """
        self.setupUi(self)
        self.sbTurnDuration.editingFinished.connect(self.rf_resultInfo)
        self.bCreateCamTurn.clicked.connect(self.on_createCamTurn)
        self.bRefreshInfo.clicked.connect(self.rf_renderInfo)
        self.bParamRender.clicked.connect(self.on_paramRender)
        self.leImagePath.editingFinished.connect(self.rf_resultInfo)
        self.bOpen.clicked.connect(self.on_openImagePath)
        self.leImageName.editingFinished.connect(self.rf_resultInfo)
        self.sbPadding.editingFinished.connect(self.rf_resultInfo)
        self.cbImageExt.currentIndexChanged.connect(self.rf_resultInfo)
        self.sbByFrame.editingFinished.connect(self.rf_resultInfo)
        self.bRender.clicked.connect(self.on_renderPreviz)

    def rf_renderInfo(self):
        """ Refresh ui render info """
        wsDict = smc.wsToDict()
        renderPath = pFile.conformPath(os.path.join(wsDict['projectPath'], wsDict['fileRules']['images']))
        self.leRenderPath.setText(renderPath)
        self.leImagePath.setText("turn")
        self.leImageName.setText(wsDict['projectName'])
        self.rf_resultInfo()

    def rf_resultInfo(self):
        """ Refresh render info """
        renderPath = str(self.leRenderPath.text())
        imaPath = str(self.leImagePath.text())
        imaName = str(self.leImageName.text())
        imaIn = str(1).zfill(self.getPadding)
        imaOut = str(self.getDuration).zfill(self.getPadding)
        self.lResultVal.setText("%s/%s/%s.[%s:%s:%s].%s" % (renderPath, imaPath, imaName, imaIn, imaOut,
                                                            self.getFrameStep, self.getExtension))

    def rf_imageExtension(self):
        """ Refresh image extension list """
        self.cbImageExt.addItems(['jpg', 'png', 'exr', 'tga'])
        self.cbImageExt.setCurrentIndex(self.cbImageExt.findText('jpg'))

    def on_createCamTurn(self):
        """ Command launched when QPushButton 'Create Camera Turn' is clicked """
        cpCmds.createCamTurn(self.getFrontAxe, self.getDuration)

    def on_paramRender(self):
        """ Command launched when QPushButton 'Param Render' is clicked """
        cpCmds.paramRender(renderer=self.getRenderer,
                           renderPath=str(self.leRenderPath.text()), imaPath=str(self.leImagePath.text()),
                           imaName=str(self.leImageName.text()), extension=self.getExtension,
                           start=1, stop=self.getDuration, step=self.getFrameStep, padding=self.getPadding,
                           width=self.sbWidth.value(), height=self.sbHeight.value())

    def on_openImagePath(self):
        """ Command launched when QPushButton 'open' is clicked """
        self.fdImaPath = pQt.fileDialog(fdFileMode='DirectoryOnly', fdRoot=str(self.leRenderPath.text()),
                                        fdCmd=self.ud_imagePath)
        self.fdImaPath.exec_()

    def on_renderPreviz(self):
        """ Command launched when QPushButton 'Render Previz' is clicked """
        self.log.info("Launch render ...")
        renderer = None
        if self.getRenderer == 'mentalRay':
            renderer = 'mr'
        elif self.getRenderer == 'turtle':
            renderer = 'turtle'
        if renderer is not None:
            cpCmds.launchRender(renderer)

    def ud_imagePath(self):
        """ Update image path """
        selPath = self.fdImaPath.selectedFiles()
        if selPath:
            imaPath = str(selPath[0]).replace('%s/' % str(self.leRenderPath.text()), '')
            self.leImagePath.setText(imaPath)
            self.rf_resultInfo()

    @property
    def getFrontAxe(self):
        """ Get front axe
            :return: (str) : Front axe """
        curTab = self.tabWidget.tabText(self.tabWidget.currentIndex())
        if curTab == 'Turn':
            if self.cbTurnX.isChecked():
                if self.cbTurnInvert.isChecked():
                    return '-x'
                return 'x'
            elif self.cbTurnY.isChecked():
                if self.cbTurnInvert.isChecked():
                    return '-y'
                return 'y'
            elif self.cbTurnZ.isChecked():
                if self.cbTurnInvert.isChecked():
                    return '-z'
                return 'z'

    @property
    def getDuration(self):
        """ Get duration
            :return: (int) : Duration """
        curTab = self.tabWidget.tabText(self.tabWidget.currentIndex())
        if curTab == 'Turn':
            if self.cbInvertRotate.isChecked():
                return int(self.sbTurnDuration.value())*-1
            return int(self.sbTurnDuration.value())

    @property
    def getRenderer(self):
        """ Get selected renderer
            :return: (str) : Render engine """
        if self.cbMentalRay.isChecked():
            return 'mentalRay'
        elif self.cbTurtle.isChecked():
            return 'turtle'

    @property
    def getPadding(self):
        """ Get image padding
            :return: (int) : Padding """
        return self.sbPadding.value()

    @property
    def getExtension(self):
        """ Get image extension
            :return: (str) : Extension """
        return str(self.cbImageExt.itemText(self.cbImageExt.currentIndex()))

    @property
    def getFrameStep(self):
        """ Get frame step
            :return: (int) : Range frame step """
        return self.sbByFrame.value()


def launch():
    """ Launch CamPrez
        :return: (object) : Launched window """
    toolName = 'mwCamPrez'
    if mc.window(toolName, q=True, ex=True):
        mc.deleteUI(toolName, wnd=True)
    global window
    window = CamPrez(parent=smc.getMayaMainWindow())
    window.show()
    return window
