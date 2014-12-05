import os
import pymel.core as pm
from PyQt4 import QtGui
from functools import partial
from lib.qt import procQt as pQt
from appli.factory import factoryUi
from lib.system import procFile as pFile
from tools.maya.util.proc import procUi as pUi
from tools.maya.util.factory.ui import dialShaderUI
from tools.maya.util.proc import procMapping as pMap
from tools.maya.util.factory import factoryCmds as fCmds


class FactoryUi(factoryUi.FactoryUi):

    def __init__(self, parent=None, logLvl='info'):
        self.mayaWnd = parent
        super(FactoryUi, self).__init__(self.mayaWnd, logLvl=logLvl)
        self._setupMaUi()

    # noinspection PyUnresolvedReferences
    def _setupMaUi(self):
        """ Setup maya main ui """
        self.log.debug("#-- Setup Factory MayaUi --#")
        self.setStyleSheet("")
        wgShader = ShaderUi(self)
        self.glShader.addWidget(wgShader)


class ShaderUi(QtGui.QMainWindow, dialShaderUI.Ui_Shader):

    def __init__(self, ui):
        self._ui = ui
        self.log = self._ui.log
        self.shaderPath = pFile.conformPath(os.path.join(self._ui.factory.path, "shader"))
        super(ShaderUi, self).__init__(self._ui.mayaWnd)
        self._setupUi()
        self._initUi()

    @property
    def category(self):
        """ Get Shader category
            :return: (srt) : Shader category """
        return str(self.cbCategory.itemText(self.cbCategory.currentIndex()))

    @property
    def subCategory(self):
        """ Get Shader subCategory
            :return: (srt) : Shader subCategory """
        return str(self.cbSubCategory.itemText(self.cbSubCategory.currentIndex()))

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup dialog ui """
        self.setupUi(self)
        self.bImport.clicked.connect(self.on_importPresentoir)
        self.bInit.clicked.connect(self.on_initShader)
        self.bParamRender.clicked.connect(self.on_paramRender)
        self.bRender.clicked.connect(self.on_render)
        self.bOpen.clicked.connect(self.on_open)
        self.bCheck.clicked.connect(self.on_check)
        self.cbCategory.currentIndexChanged.connect(self.rf_subCategory)
        self.bSave.clicked.connect(self.on_save)
        self.bCancel.clicked.connect(self.close)

    def _initUi(self):
        """ Initialize dialog ui """
        self.rf_category()
        self.rf_subCategory()

    def rf_category(self):
        """ Refresh category """
        self.cbCategory.clear()
        cats = os.listdir(self.shaderPath) or []
        if cats:
            self.cbCategory.addItems(cats)

    def rf_subCategory(self):
        """ Refresh subCategory """
        self.cbSubCategory.clear()
        subCats = os.listdir(pFile.conformPath(os.path.join(self.shaderPath, self.category))) or []
        if subCats:
            self.cbSubCategory.addItems(subCats)

    def ud_preview(self, previewPath=None):
        """ Update preview path """
        if previewPath is None:
            selPath = self.fdPath.selectedFiles()
        else:
            selPath = [previewPath]
        if selPath:
            self.lePreview.setText(str(selPath[0]))

    def on_importPresentoir(self):
        """ Import default model """
        modelPath = pFile.conformPath(os.path.join(self._ui.factory.path, "_lib", "maya", "presentoir.ma"))
        fCmds.importPresentoir(modelPath)

    def on_initShader(self):
        """ Command launched when bInit is clicked """
        sg = pMap.getShadingEngine('S_factory_ball')
        matDict = fCmds.getMat('S_factory_ball')
        self.leShader.setText(sg[0])
        #-- Maya Shader --#
        if matDict['ss'] is not None or matDict['ds'] is not None or matDict['vs'] is not None:
            if matDict['ss'] is not None:
                self.lSSValue.setText(matDict['ss'])
            else:
                self.leShader.clear()
                self.lSSValue.setText("None")
            if matDict['ds'] is not None:
                self.lDSValue.setText(matDict['ds'])
            else:
                self.lDSValue.setText("None")
            if matDict['vs'] is not None:
                self.lVSValue.setText(matDict['vs'])
            else:
                self.lVSValue.setText("None")
        #-- Mental Ray Shader --#
        if matDict['ss'] is None and matDict['ds'] is None and matDict['vs'] is None:
            txt = []
            for k, v in matDict.iteritems():
                if k.startswith('mi'):
                    line = "%s -- (mrShader)" % v
                    if not line in txt:
                        txt.append(line)
            self.lSSValue.setText('\n'.join(txt))
            self.lDSValue.setText("None")
            self.lVSValue.setText("None")

    def on_paramRender(self):
        """ Command launched when bParamRender is clicked """
        #-- Get Renderer --#
        if self.cbTurtle.isChecked():
            renderer = 'turtle'
            plugInName = 'Turtle'
        else:
            renderer = 'mentalRay'
            plugInName = 'Mayatomr'
        if fCmds.checkRenderEngine(plugInName):
            #-- Param Scene --#
            fCmds.paramCam()
            fCmds.paramLight(renderer)
            envPath = os.path.join(self._ui.factory.path, 'texture', 'hdr_env', 'inside', 'JapanSubway_env.hdr')
            #-- Param Render --#
            if not self.rbPreview.isChecked():
                fCmds.paramRender(renderer, 'shader_preview', envPath, quality='draft')
            else:
                fCmds.paramRender(renderer, 'shader_preview', envPath, quality='preview')

    def on_render(self):
        """ Command launched when bRender is clicked """
        user = os.environ.get('username').lower()
        imaPath = pFile.conformPath(os.path.join(self._ui.factory.rndBinPath, 'users'))
        if not os.path.exists(imaPath):
            self.log.error("RndBin path not found: %s" % imaPath)
        else:
            imaPath = os.path.join(imaPath, user)
            if not os.path.exists(imaPath):
                self.log.info("Create user path: %s" % user)
                os.mkdir(imaPath)
            result = fCmds.renderPreview(imaPath)
            self.ud_preview(previewPath=result[1])
            self.log.info("Image path: %s" % result[1])

    def on_open(self):
        """ Command launched when bOpen is clicked """
        if str(self.lePreview.text()) in ['', ' ']:
            rootPath = self._ui.factory.rndBinPath
        else:
            rootPath = str(self.lePreview.text())
        self.fdPath = pQt.fileDialog(fdRoot=rootPath, fdCmd=partial(self.ud_preview, previewPath=None))
        self.fdPath.setFileMode(QtGui.QFileDialog.AnyFile)
        self.fdPath.exec_()

    def on_check(self):
        """ command launched when bCheck is clicked """
        if self._checkShaderName():
            self.lCheckValue.setText("Shader name is valide.")
        else:
            self.lCheckValue.setText("!!! WARNING: Shader %r already exists !!!" % str(self.leShaderName.text()))

    def on_save(self):
        """ Command launched when bSave is clicked """
        matName = str(self.leShaderName.text())
        previewFile = str(self.lePreview.text())
        if matName in ['', ' ']:
            self.log.error('Shader name not valide !!!')
        else:
            shaderPath = pFile.conformPath(os.path.join(self.shaderPath, self.category, self.subCategory,
                                                        'shader', "%s.ma" % matName))
            if os.path.exists(shaderPath):
                self.log.error("Shader already exists: %s" % matName)
            else:
                if previewFile in ['', ' ']:
                    self.log.error("Preview file not valide !!!")
                else:
                    if not os.path.exists(previewFile):
                        self.log.error("Preview file not found: %s" % previewFile)
                    else:
                        matDict = fCmds.getMat('S_factory_ball')
                        fCmds.saveShader(self.shaderPath, self.category, self.subCategory, matName, previewFile, matDict)

    def _checkShaderName(self):
        """ Check if shader name is valide
            :return: (bool) : True if shader name is valide """
        matName = str(self.leShaderName.text())
        matPath = pFile.conformPath(os.path.join(self.shaderPath, self.category, self.subCategory,
                                                 "shader", "%s.ma" % matName))
        if os.path.exists(matPath):
            self.log.warning("Shader already exists: %s" % matName)
            return False
        else:
            self.log.info("Shader name is valide")
            return True


def launch():
    """ Launch ToolManager
        :return: (object) : Launched window """
    toolName = 'factory'
    if pm.window(toolName, q=True, ex=True):
        pm.deleteUI(toolName, wnd=True)
    window = FactoryUi(parent=pUi.getMayaMainWindow(), logLvl='debug')
    window.show()
    return window
