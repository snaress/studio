from PyQt4 import QtGui
from tools.maya.cmds import pScene
from tools.maya.cloth import clothBox
from tools.maya.cloth.clothBox.ui import clothBoxUI
from tools.maya.cloth.clothBox import clothBoxWgts as cbWgts
try:
    import maya.cmds as mc
except:
    pass


class ClothBoxUi(QtGui.QMainWindow, clothBoxUI.Ui_mwClothBox):

    def __init__(self, parent=None):
        print "\n########## %s ##########" % clothBox.toolName
        self.iconPath = clothBox.iconPath
        super(ClothBoxUi, self).__init__(parent)
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup main ui """
        print "#-- Setup Main Ui --#"
        self.setupUi(self)
        self._initWidgets()

    def _initWidgets(self):
        """ Import main ui widgets """
        self.wgModeBox = cbWgts.ModeBoxUi(self)
        self.vlMode.insertWidget(0, self.wgModeBox)
        self.wgRiggBox = cbWgts.RiggBoxUi(self)
        self.vlRigg.insertWidget(0, self.wgRiggBox)


def launch():
    """ Launch ClothEditor
        :return: Launched window
        :rtype: object """
    toolName = 'mwClothBox'
    if mc.window(toolName, q=True, ex=True):
        mc.deleteUI(toolName, wnd=True)
    global window
    window = ClothBoxUi(parent=pScene.getMayaMainWindow())
    window.show()
    return window
