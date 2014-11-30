import os
import pymel.core as pm
from PyQt4 import QtGui
from appli.factory import factoryUi
from lib.system import procFile as pFile
from tools.maya.util.proc import procUi as pUi
from tools.maya.util.factory.ui import dialShaderUI
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
        self.miSaveShader.triggered.connect(self.on_saveShader)

    def on_saveShader(self):
        """ Command launched when miSaveShader is clicked """
        self.dialShader = ShaderUi(self)
        self.dialShader.show()


class ShaderUi(QtGui.QMainWindow, dialShaderUI.Ui_Shader):

    def __init__(self, ui):
        self._ui = ui
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
        self.cbCategory.currentIndexChanged.connect(self.rf_subCategory)
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

    def on_importPresentoir(self):
        """ Import default model """
        modelPath = pFile.conformPath(os.path.join(self._ui.factory.path, "_lib", "maya", "presentoir.ma"))
        fCmds.importPresentoir(modelPath)

    def on_initShader(self):
        """ Command launched when bInit is clicked """
        matDict = fCmds.getMat('S_factory_ball')
        if matDict['ss'] is not None:
            self.leShader.setText(matDict['ss'])
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

    def on_paramRender(self):
        """ Command launched when bParamRender is clicked """
        if fCmds.checkRenderEngine():
            fCmds.paramCam()
            envPath = os.path.join(self._ui.factory.path, 'texture', 'hdr_env', 'inside', 'JapanSubway_env.hdr')
            fCmds.paramRender('shader_preview', envPath)

    def on_render(self):
        """ Command launched when bRender is clicked """




def launch():
    """ Launch ToolManager
        :return: (object) : Launched window """
    toolName = 'factory'
    if pm.window(toolName, q=True, ex=True):
        pm.deleteUI(toolName, wnd=True)
    window = FactoryUi(parent=pUi.getMayaMainWindow(), logLvl='debug')
    window.show()
    return window
