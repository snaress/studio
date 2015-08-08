import os
from PyQt4 import QtGui
from functools import partial
from lib.qt import procQt as pQt
from tools.maya.cmds import pScene
from tools.maya.cloth import dynEval
from lib.system import procFile as pFile
from tools.maya.cloth.dynEval.ui import dynEvalUI
from tools.maya.cloth.dynEval import dynEvalWgts as deWgts
from tools.maya.cloth.dynEval import dynEvalCmds as deCmds
try:
    import maya.cmds as mc
except:
    pass


class DynEvalUi(QtGui.QMainWindow, dynEvalUI.Ui_mwDynEval):
    """
    Main window 'Dyn Eval'
    :param parent: Maya main window
    :type parent: QtCore.QObject
    """
    def __init__(self, parent=None):
        print "\n########## %s ##########" % dynEval.toolName
        self.iconPath = dynEval.iconPath
        self.nucleusIcon = QtGui.QIcon(os.path.join(self.iconPath, 'nucleus.png'))
        self.nClothIcon = QtGui.QIcon(os.path.join(self.iconPath, 'nCloth.png'))
        self.nRigidIcon = QtGui.QIcon(os.path.join(self.iconPath, 'nRigid.png'))
        self.enableIcon = QtGui.QIcon(os.path.join(self.iconPath, 'enable.png'))
        self.disableIcon = QtGui.QIcon(os.path.join(self.iconPath, 'disable.png'))
        super(DynEvalUi, self).__init__(parent)
        self._setuipUi()

    # noinspection PyUnresolvedReferences
    def _setuipUi(self):
        """
        Setup main ui
        """
        print "#-- Setup Main Ui --#"
        self.setupUi(self)
        self._initWidgets()
        self.miSetRootPath.triggered.connect(self.on_miSetRootPath)
        self.miSetRootPath.setShortcut("Ctrl+P")
        self.miXplorer.triggered.connect(self.on_miXplorer)
        self.miXplorer.setShortcut("Alt+E")
        self.miXterm.triggered.connect(self.on_miXterm)
        self.miXterm.setShortcut("Alt+X")
        self.miToolTips.triggered.connect(self.on_miToolTips)
        self.miToolTips.setShortcut("Ctrl+T")
        self.miNamespace.triggered.connect(self.on_miNamespace)
        self.miNamespace.setShortcut("Ctrl+N")
        self.miRfDisplay.setShortcut("Ctrl+R")
        self.miBackup.setShortcut("Ctrl+B")
        self.miRefreshUi.triggered.connect(self.on_miRefreshUi)
        self.miRefreshUi.setShortcut("F5")
        self.rf_menuFilters()

    def _initWidgets(self):
        """
        Import main ui widgets
        """
        self.sceneNodes = deWgts.SceneNodeUi(self)
        self.vlSceneNodes.insertWidget(0, self.sceneNodes)
        self.dynEval = deWgts.DynEvalCtrl(self)
        self.vlNodeOptions.insertWidget(0, self.dynEval)
        self.cacheList = deWgts.CacheListUi(self)
        self.vlCaches.insertWidget(0, self.cacheList)
        self.cacheInfo = deWgts.CacheInfoUi(self)
        self.vlCacheInfo.insertWidget(0, self.cacheInfo)
        #-- Set Widget Parent --#
        self.dynEval.cacheList = self.cacheList
        self.cacheList.cacheInfo = self.cacheInfo

    @property
    def toolTipState(self):
        """
        Get toolTips state
        :return: ToolTips state
        :rtype: bool
        """
        return self.miToolTips.isChecked()

    @property
    def namespaceState(self):
        """
        Get namespace state
        :return: Namespace state
        :rtype: bool
        """
        return self.miNamespace.isChecked()

    @property
    def displayState(self):
        """
        Get refresh display state
        :return: Display state
        :rtype: bool
        """
        return self.miRfDisplay.isChecked()

    @property
    def backupState(self):
        """
        Get backup state
        :return: Backup state
        :rtype: bool
        """
        return self.miBackup.isChecked()

    @staticmethod
    def getLabelColor(color):
        """
        Get rgb color from given arg
        :param color: 'green', 'blue', 'yellow'
        :type color: str
        :return: Rgb color
        :rtype: tuple
        """
        if color == 'green':
            rgb = (0, 255, 0)
        elif color == 'blue':
            rgb = (0, 150, 255)
        elif color == 'yellow':
            rgb = (200, 150, 0)
        elif color == 'red':
            rgb = (255, 75, 0)
        elif color == 'lightGrey':
            rgb = (175, 175, 175)
        else:
            rgb = (225, 225, 225)
        return rgb

    # noinspection PyUnresolvedReferences
    def rf_menuFilters(self):
        """
        Refresh menu 'Filters'
        """
        self.mFilters.clear()
        nsList = []
        for item in pQt.getAllItems(self.sceneNodes.twSceneNodes):
            if item.clothNs is not None:
                if not item.clothNs in nsList:
                    nsList.append(item.clothNs)
                    menuItem = QtGui.QAction(QtGui.QIcon(), item.clothNs, self)
                    menuItem.setCheckable(True)
                    menuItem.setChecked(True)
                    menuItem.ns = item.clothNs
                    menuItem.triggered.connect(partial(self.on_filter, menuItem))
                    self.mFilters.addAction(menuItem)

    def on_miSetRootPath(self):
        """
        Command launched when 'SetRootPath' menuItem is clicked
        """
        if self.cacheList.cachePath is None:
            self.cacheList.cachePath = self.cacheList.defaultCachePath
        self.fdRootPath = pQt.fileDialog(fdRoot=self.cacheList.cachePath, fdFileMode='DirectoryOnly',
                                         fdCmd=self.on_setRootPath)
        self.fdRootPath.exec_()

    def on_setRootPath(self):
        """
        Command launched when 'Choose' QPushButton is clicked
        """
        selPath = self.fdRootPath.selectedFiles()
        if selPath:
            self.cacheList.cachePath = pFile.conformPath(str(selPath[0]))
            self.fdRootPath.close()
            self.cacheList.rf_cachePath()

    def on_miXplorer(self):
        """ Command launched when 'Xplorer' menuItem is clicked """
        if self.cacheList.cachePath is None:
            deCmds.mayaWarning("!!! CacheRootPath is not set !!!")
            return
        os.system('explorer %s' % os.path.normpath(self.cacheList.cachePath))

    def on_miXterm(self):
        """ Command launched when 'Xterm' menuItem is clicked """
        if self.cacheList.cachePath is None:
            deCmds.mayaWarning("!!! CacheRootPath is not set !!!")
            return
        os.system('start "DynEval Root Path" /d "%s"' % os.path.normpath(self.cacheList.cachePath))

    def on_miToolTips(self):
        """
        Command launched when 'ToolTips' menuItem is clicked
        """
        self.sceneNodes.rf_widgetToolTips()
        self.sceneNodes.rf_sceneItemToolTips()
        self.dynEval.rf_widgetToolTips()
        self.cacheList.rf_widgetToolTips()
        self.cacheInfo.rf_widgetToolTips()

    def on_miNamespace(self):
        """
        Command launched when 'Namespace' menuItem is clicked
        """
        self.sceneNodes.rf_namespaces()

    def on_miRefreshUi(self):
        """
        Command launched when 'Refresh Ui' menuItem is clicked
        """
        self.sceneNodes.rf_sceneNodes()
        self.cacheList.rf_cacheList()
        self.cacheInfo.clearInfos()

    def on_filter(self, filterItem):
        """
        Command launched when 'Filters' menuItem is clicked
        :param filterItem: Filters menuItem
        :type filterItem: QtGui.QAction
        """
        for topItem in pQt.getTopItems(self.sceneNodes.twSceneNodes):
            if topItem.clothNs == filterItem.ns:
                self.sceneNodes.twSceneNodes.setItemHidden(topItem, not filterItem.isChecked())


def launch():
    """
    Launch ClothCache
    """
    toolName = 'mwDynEval'
    if mc.window(toolName, q=True, ex=True):
        mc.deleteUI(toolName, wnd=True)
    global window
    window = DynEvalUi(parent=pScene.getMayaMainWindow())
    window.show()
    return window
