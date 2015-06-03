import os
from PyQt4 import QtGui
from functools import partial
from lib.qt import procQt as pQt
from tools.maya.cmds import pScene
from tools.maya.cloth import clothCache
from tools.maya.cloth.clothCache.ui import clothCacheUI
from tools.maya.cloth.clothCache import clothCacheWgts as ccWgts
try:
    import maya.cmds as mc
except:
    pass


class ClothCacheUi(QtGui.QMainWindow, clothCacheUI.Ui_mwClothCache):

    def __init__(self, parent=None):
        print "\n########## %s ##########" % clothCache.toolName
        self.iconPath = clothCache.iconPath
        self.nucleusIcon = QtGui.QIcon(os.path.join(self.iconPath, 'nucleus.png'))
        self.nClothIcon = QtGui.QIcon(os.path.join(self.iconPath, 'nCloth.png'))
        self.nRigidIcon = QtGui.QIcon(os.path.join(self.iconPath, 'nRigid.png'))
        self.enableIcon = QtGui.QIcon(os.path.join(self.iconPath, 'enable.png'))
        self.disableIcon = QtGui.QIcon(os.path.join(self.iconPath, 'disable.png'))
        super(ClothCacheUi, self).__init__(parent)
        self._setuipUi()

    def _setuipUi(self):
        """ Setup main ui """
        print "#-- Setup Main Ui --#"
        self.setupUi(self)
        self._initWidgets()
        self.miToolTips.triggered.connect(self.on_miToolTips)
        self.rf_menuFilters()

    def _initWidgets(self):
        """ Import main ui widgets """
        self.wgSceneNodes = ccWgts.SceneNodeUi(self)
        self.vlSceneNodes.insertWidget(0, self.wgSceneNodes)
        self.wgCacheEval = ccWgts.CacheEvalUi(self)
        self.vlNodeOptions.insertWidget(0, self.wgCacheEval)
        self.wgCacheList = ccWgts.CacheListUi(self)
        self.vlCaches.insertWidget(0, self.wgCacheList)
        self.wgCacheInfo = ccWgts.CacheInfoUi(self)
        self.vlCacheInfo.insertWidget(0, self.wgCacheInfo)

    @property
    def toolTipState(self):
        """ Get toolTips state
            :return: ToolTips state
            :rtype: bool """
        return self.miToolTips.isChecked()

    @staticmethod
    def getLabelColor(color):
        """ Get rgb color from given arg
            :param color: 'green', 'blue', 'yellow'
            :type color: str
            :return: Rgb color
            :rtype: tuple """
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
        """ Refresh menu 'Filters' """
        self.mFilters.clear()
        nsList = []
        for item in pQt.getAllItems(self.wgSceneNodes.twSceneNodes):
            if item.clothNs is not None:
                if not item.clothNs in nsList:
                    nsList.append(item.clothNs)
                    menuItem = QtGui.QAction(QtGui.QIcon(), item.clothNs, self)
                    menuItem.setCheckable(True)
                    menuItem.setChecked(True)
                    menuItem.ns = item.clothNs
                    menuItem.triggered.connect(partial(self.on_filter, menuItem))
                    self.mFilters.addAction(menuItem)

    def on_miToolTips(self):
        """ Command launched when 'ToolTips' menuItem is clicked """
        self.wgSceneNodes.rf_widgetToolTips()
        self.wgSceneNodes.rf_sceneItemToolTips()
        self.wgCacheEval.rf_widgetToolTips()

    def on_filter(self, filterItem):
        """ Command launched when 'Filters' menuItem is clicked
            :param filterItem: Filters menuItem
            :type filterItem: QtGui.QAction """
        for topItem in pQt.getTopItems(self.wgSceneNodes.twSceneNodes):
            if topItem.clothNs == filterItem.ns:
                self.wgSceneNodes.twSceneNodes.setItemHidden(topItem, not filterItem.isChecked())


def launch():
    """ Launch ClothCache
        :return: Launched window
        :rtype: object """
    toolName = 'mwClothCache'
    if mc.window(toolName, q=True, ex=True):
        mc.deleteUI(toolName, wnd=True)
    global window
    window = ClothCacheUi(parent=pScene.getMayaMainWindow())
    window.show()
    return window
