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
        rgb = (225, 225, 225)
        if color == 'green':
            rgb = (0, 255, 0)
        elif color == 'blue':
            rgb = (0, 150, 255)
        elif color == 'yellow':
            rgb = (200, 150, 0)
        elif color == 'lightGrey':
            rgb = (175, 175, 175)
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
        self.wgVtxMaps = ceWgts.VtxMapUi(self)
        self.vlVtxMap.insertWidget(0, self.wgVtxMaps)

    def on_miToolTips(self):
        """ Command launched when 'ToolTips' menuItem is clicked """
        self.wgSceneNodes.rf_sceneItemToolTips()


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
