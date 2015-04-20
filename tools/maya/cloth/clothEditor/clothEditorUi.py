import os
from PyQt4 import QtGui
from tools.maya.cmds import pScene
from tools.maya.cloth import clothEditor
from tools.maya.cloth.clothEditor.ui import clothEditorUI
from tools.maya.cloth.clothEditor import clothEditorWgts as ceWgts
try:
    import maya.cmds as mc
except:
    pass


class ClothEditorUi(QtGui.QMainWindow, clothEditorUI.Ui_mwClothEditor):

    def __init__(self, parent=None):
        print "\n########## %s ##########" % clothEditor.toolName
        self.iconPath = clothEditor.iconPath
        self.filesRootPath = None
        self.lockIconOn = QtGui.QIcon(os.path.join(self.iconPath, 'lockOn.png'))
        self.lockIconOff = QtGui.QIcon(os.path.join(self.iconPath, 'lockOff.png'))
        self.nucleusIcon = QtGui.QIcon(os.path.join(self.iconPath, 'nucleus.png'))
        self.nClothIcon = QtGui.QIcon(os.path.join(self.iconPath, 'nCloth.png'))
        self.nRigidIcon = QtGui.QIcon(os.path.join(self.iconPath, 'nRigid.png'))
        self.enableIcon = QtGui.QIcon(os.path.join(self.iconPath, 'enable.png'))
        self.disableIcon = QtGui.QIcon(os.path.join(self.iconPath, 'disable.png'))
        super(ClothEditorUi, self).__init__(parent)
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup main ui """
        print "#-- Setup Main Ui --#"
        self.setupUi(self)
        self._initWidgets()
        self.miToolTips.triggered.connect(self.on_miToolTips)

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
        elif color == 'lightGrey':
            rgb = (175, 175, 175)
        else:
            rgb = (225, 225, 225)
        return rgb

    @property
    def currentTab(self):
        """ Get clothEditor active tab
            :return: Active tab label
            :rtype: str """
        return str(self.tabClothEditor.tabText(self.tabClothEditor.currentIndex()))

    def _initWidgets(self):
        """ Import main ui widgets """
        self.wgSceneNodes = ceWgts.SceneNodeUi(self)
        self.vlSceneNodes.insertWidget(0, self.wgSceneNodes)
        self.wgAttributes = ceWgts.AttrUi(self)
        self.vlAttr.insertWidget(0, self.wgAttributes)
        self.wgAttrFiles = ceWgts.FilesUi(self, 'attrs', self.wgAttributes)
        self.wgAttributes.vlAttrFiles.insertWidget(0, self.wgAttrFiles)
        self.wgVtxMaps = ceWgts.VtxMapUi(self)
        self.vlVtxMap.insertWidget(0, self.wgVtxMaps)
        self.wgVtxFiles = ceWgts.FilesUi(self, 'vtxMap', self.wgVtxMaps)
        self.wgVtxMaps.vlVtxFiles.insertWidget(0, self.wgVtxFiles)

    def on_miToolTips(self):
        """ Command launched when 'ToolTips' menuItem is clicked """
        self.wgSceneNodes.rf_widgetToolTips()
        self.wgSceneNodes.rf_sceneItemToolTips()
        self.wgAttributes.rf_widgetToolTips()
        self.wgVtxMaps.rf_widgetToolTips()

    def closeEvent(self, *args, **kwargs):
        """ Command launched when ui is closing """
        print "#-- Closing Cloth Editor --#"
        mc.deleteUI(str(self.objectName()), wnd=True)


def launch():
    """ Launch ClothEditor
        :return: Launched window
        :rtype: object """
    toolName = 'mwClothEditor'
    if mc.window(toolName, q=True, ex=True):
        mc.deleteUI(toolName, wnd=True)
    global window
    window = ClothEditorUi(parent=pScene.getMayaMainWindow())
    window.show()
    return window
