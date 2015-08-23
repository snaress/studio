from PyQt4 import QtGui
from appli.grapher.gui.ui import nodeEditorUI


class NodeEditor(QtGui.QWidget, nodeEditorUI.Ui_wgNodeEditor):

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init NodeEditor Widget.")
        self.node = None
        super(NodeEditor, self).__init__()
        self._setupWidget()

    def _setupWidget(self):
        self.log.debug("\t ---> Setup NodeEditor Widget.")
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(1)

    def connectNode(self, node):
        self.node = node