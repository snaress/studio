from PyQt4 import QtGui
from functools import partial
from lib.qt import textEditor
from lib.qt import procQt as pQt
from appli.grapher.gui import graphWgts
from appli.grapher.gui.ui import nodeEditorUI


class NodeEditor(QtGui.QWidget, nodeEditorUI.Ui_wgNodeEditor):
    """
    NodeEditor widget, child of GrapherUi. Widget used to edit nodes attributes

    :param mainUi: Grapher mainUi class
    :type mainUi: GrapherUi
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
        self.pbDelVersion.clicked.connect(self.on_delVersion)
        #-- Node Comment --#
        self.nodeComment = textEditor.TextEditor()
        self.nodeComment.bLoadFile.setEnabled(False)
        self.nodeComment.bSaveFile.setEnabled(False)
        self.glComment.addWidget(self.nodeComment, 0, 0)
        self.gbComment.clicked.connect(partial(self.mainUi.rf_nodeGroupVisibility, self.gbComment, self.nodeComment))
        #-- Node Variables --#
        self.nodeVar = graphWgts.Variables(self.mainUi, self)
        self.glVariables.addWidget(self.nodeVar, 0, 0)
        self.gbVariables.clicked.connect(partial(self.mainUi.rf_nodeGroupVisibility, self.gbVariables, self.nodeVar))
        #-- Node Script --#
        self.nodeScript = graphWgts.Script(self.mainUi, self)
        self.vlScript.addWidget(self.nodeScript)
        #-- Node Notes --#
        self.gbNotes.clicked.connect(partial(self.mainUi.rf_nodeGroupVisibility, self.gbNotes, self.teNotes))
        #-- Node Buttons --#
        self.pbSave.clicked.connect(self.on_save)
        self.pbCancel.clicked.connect(self.on_cancel)
        self.pbClose.clicked.connect(self.close)
        #-- Refresh --#
        self.refresh()

    def getDatas(self):
        """
        Get node editor datas

        :return: Node editor datas
        :rtype: dict
        """
        datas = dict(nodeComments=str(self.nodeComment.teText.toHtml()),
                     nodeVariables=self.nodeVar.getDatas(),
                     nodeScript=str(self.nodeScript.scriptEditor._widget.getCode()),
                     nodeNotes=str(self.teNotes.toPlainText()))
        return datas
    def clear(self):
        """
        Clear all editor values
        """
        self.log.detail(">>> Clear NodeEditor")
        for w in [self.leNodeName, self.lTypeValue, self.leVersionTitle, self.cbNodeVersion, self.nodeComment.teText,
                  self.nodeVar.twVar, self.teNotes]:
            w.clear()
        self.nodeScript.scriptEditor.resetScript()
        self.refresh()

    def refresh(self):
        """
        Refresh nodeEditor widgets
        """
        self.log.detail(">>> Refreshing NodeEditor")
        self.mainUi.rf_nodeGroupVisibility(self.gbComment, self.nodeComment)
        self.mainUi.rf_nodeGroupVisibility(self.gbVariables, self.nodeVar)
        self.mainUi.rf_nodeGroupVisibility(self.gbNotes, self.teNotes)
        self.vfScript.setVisible(False)
        self.vfSpacer.setVisible(True)

    def updateVisibility(self):
        spacer = True
        self.vfScript.setVisible(False)
        if hasattr(self.node, 'nodeScript'):
            self.vfScript.setVisible(True)
            spacer = False
        self.vfSpacer.setVisible(spacer)

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
        self.nodeVar.buildTree(self.node.nodeVariables[self.node.nodeVersion])
        if hasattr(self.node, 'nodeScript'):
            self.nodeScript.scriptEditor._widget.setCode(self.node.nodeScript[self.node.nodeVersion])
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
        self.updateVisibility()
        self.update()

    def delVersion(self):
        """
        Delete current node version
        """
        self.fdDelVersion.close()
        self.node.delVersion()
        self.clear()
        self.update()

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
        self.updateVisibility()
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

    def on_delVersion(self):
        """
        Command launched when 'Del Version' QPushButton is clicked.

        Launch confirm dialog
        """
        if self.node is not None:
            self.log.detail(">>> Delete current node version")
            mess = "Delete node version %s ?" % self.node.nodeVersion
            self.fdDelVersion = pQt.ConfirmDialog(mess, ['Delete'], [self.delVersion])
            self.fdDelVersion.exec_()

    def on_save(self):
        """
        Command launched when 'Save' QPushButton is clicked.

        Save nodeEditor datas to node
        """
        if self.node is not None:
            self.log.detail(">>> Save node datas")
            self.node.setVersionnedDatas(**self.getDatas())

    def on_cancel(self):
        """
        Command launched when 'Cancel' QPushButton is clicked.

        Cancel node edition
        """
        if self.node is not None:
            self.clear()
            self.update()
