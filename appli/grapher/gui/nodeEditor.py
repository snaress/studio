from PyQt4 import QtGui
from functools import partial
from lib.qt import textEditor
from appli.grapher.gui.ui import nodeEditorUI


class NodeEditor(QtGui.QWidget, nodeEditorUI.Ui_wgNodeEditor):
    """
    NodeEditor widget, child of GrapherUi. Widget used to edit nodes attributes

    :param mainUi: Grapher mainUi class
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init NodeEditor Widget.")
        self.item = None
        self.node = None
        super(NodeEditor, self).__init__()
        self._setupWidget()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        self.log.debug("\t ---> Setup NodeEditor Widget.")
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(1)
        #-- Node Id --#
        self.leVersionTitle.returnPressed.connect(self.on_versionTitle)
        self.pbSwitch.clicked.connect(self.on_switchVersion)
        self.pbNewVersion.clicked.connect(self.on_newVersion)
        #-- Node Comment --#
        self.nodeComment = textEditor.TextEditor()
        self.nodeComment.bLoadFile.setEnabled(False)
        self.nodeComment.bSaveFile.setEnabled(False)
        self.glComment.addWidget(self.nodeComment, 0, 0)
        self.gbComment.clicked.connect(partial(self.rf_nodeGroupVisibility, self.gbComment))
        #-- Node Variables --#
        self.gbVariables.clicked.connect(partial(self.rf_nodeGroupVisibility, self.gbVariables))
        #-- Node Notes --#
        self.gbNotes.clicked.connect(partial(self.rf_nodeGroupVisibility, self.gbNotes))
        #-- Node Buttons --#
        self.pbSave.clicked.connect(self.on_save)
        self.pbCancel.clicked.connect(self.on_cancel)
        self.pbClose.clicked.connect(self.close)
        #-- Refresh --#
        self.refresh()

    def getDatas(self):
        return dict(nodeComments=str(self.nodeComment.teText.toHtml()),
                    nodeNotes=str(self.teNotes.toPlainText()))

    def clear(self):
        """
        Clear all editor values
        """
        self.log.detail(">>> Clear NodeEditor")
        for w in [self.leNodeName, self.lTypeValue, self.leVersionTitle, self.cbNodeVersion, self.nodeComment.teText,
                  self.teNotes]:
            w.clear()

    def refresh(self):
        """
        Refresh nodeEditor widgets
        """
        self.log.detail(">>> Refreshing NodeEditor")
        self.rf_nodeGroupVisibility(self.gbComment)
        self.rf_nodeGroupVisibility(self.gbVariables)
        self.rf_nodeGroupVisibility(self.gbNotes)

    def update(self):
        """
        Update editor values from node
        """
        super(NodeEditor, self).update()
        self.log.detail(">>> Updating NodeEditor")
        self.setWindowTitle(self.node.nodeName)
        self.leNodeName.setText(self.node.nodeName)
        self.lTypeValue.setText(self.node.nodeType)
        self.leVersionTitle.setText(self.node.nodeVersions[self.node.nodeVersion])
        for n in sorted(self.node.nodeVersions.keys()):
            self.cbNodeVersion.addItem(str(n))
        self.cbNodeVersion.setCurrentIndex(self.cbNodeVersion.findText(str(self.node.nodeVersion)))
        self.nodeComment.teText.setHtml(self.node.nodeComments[self.node.nodeVersion])
        self.teNotes.setPlainText(self.node.nodeNotes[self.node.nodeVersion])

    def connectItem(self, item):
        """
        Connect editor to given item

        :param item: GraphTree item
        :type item: QtGui.QTreeWidgetItem | QtSvg.QGraphicsProxyWidget
        """
        self.log.detail(">>> Connecting NodeEditor to %s" % item._item._node.nodeName)
        self.item = item
        self.node = self.item._item._node
        self.update()

    def rf_nodeGroupVisibility(self, groupBox):
        """
        Refresh given QGroupBox visibility

        :param groupBox: Node editor groupBox
        :type groupBox: QtGui.QGroupBox
        """
        if str(groupBox.title()) == 'Comment':
            self.nodeComment.setVisible(groupBox.isChecked())
        elif str(groupBox.title()) == 'Notes':
            self.teNotes.setVisible(groupBox.isChecked())
        if groupBox.isChecked():
            groupBox.setMaximumHeight(16777215)
        else:
            groupBox.setMaximumHeight(20)

    def on_versionTitle(self):
        """
        Command launched when 'Version Title' QLineEdit is entered.

        Edit node version title
        """
        if self.node is not None:
            self.log.info("Edit node version title: %s" % str(self.leVersionTitle.text()))
            self.node.nodeVersions[self.node.nodeVersion] = str(self.leVersionTitle.text())

    def on_switchVersion(self):
        """
        Command launched when 'Switch Version' QPushButton is clicked.

        Switch node version
        """
        self.node.nodeVersion = int(self.cbNodeVersion.currentText())
        self.clear()
        self.update()

    def on_newVersion(self):
        """
        Command launched when 'New Version' QPushButton is clicked.

        Create new node version
        """
        if self.node is not None:
            self.log.detail(">>> Create new node version")
            self.node.addVersion()
            self.clear()
            self.update()

    def on_save(self):
        """
        Command launched when 'Save' QPushButton is clicked.

        Save nodeEditor datas to node
        """
        if self.node is not None:
            self.log.detail(">>> Save node datas")
            self.node.setDatas(**self.getDatas())

    def on_cancel(self):
        """
        Command launched when 'Cancel' QPushButton is clicked.

        Cancel node edition
        """
        if self.node is not None:
            self.clear()
            self.update()
