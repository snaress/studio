import os
from PyQt4 import QtGui
from functools import partial
from lib.qt import procQt as pQt
from PyQt4.Qsci import QsciScintilla
from appli.grapher.gui import graphWgts
from lib.system import procFile as pFile
from lib.qt import textEditor, scriptEditor2
from appli.grapher.gui.ui import nodeEditorUI, wgLauncherUI, wgScriptUI


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
        self.nodeLauncher = Launcher(self.mainUi, self)
        self.vlScript.addWidget(self.nodeLauncher)
        self.nodeScript = Script(self.mainUi, self)
        self.vlScript.addWidget(self.nodeScript)
        #-- Node Trash --#
        self.teTrash.setStyleSheet("background-color: rgb(150, 150, 150)")
        self.gbTrash.clicked.connect(partial(self.mainUi.rf_nodeGroupVisibility, self.gbTrash, self.teTrash))
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
                     nodeScript=str(self.nodeScript.scriptEditor.getCode()),
                     nodeTrash=str(self.teTrash.toPlainText()))
        return datas

    def clear(self):
        """
        Clear all editor values
        """
        self.log.detail(">>> Clear NodeEditor")
        for w in [self.leNodeName, self.lTypeValue, self.leVersionTitle, self.cbNodeVersion, self.nodeComment.teText,
                  self.nodeVar.twVar, self.nodeScript.scriptEditor, self.teTrash]:
            w.clear()
        self.refresh()

    def refresh(self):
        """
        Refresh nodeEditor widgets
        """
        self.log.detail(">>> Refreshing NodeEditor")
        self.mainUi.rf_nodeGroupVisibility(self.gbComment, self.nodeComment)
        self.mainUi.rf_nodeGroupVisibility(self.gbVariables, self.nodeVar)
        self.mainUi.rf_nodeGroupVisibility(self.gbTrash, self.teTrash)
        self.nodeLauncher.setVisible(False)
        self.vfScript.setVisible(False)
        self.vfSpacer.setVisible(True)

    def updateVisibility(self):
        """
        Update widgets visibility
        """
        spacer = True
        self.vfScript.setVisible(False)
        if hasattr(self.node, 'nodeScript'):
            self.vfScript.setVisible(True)
            if hasattr(self.node, 'nodeLauncher'):
                self.nodeLauncher.setVisible(True)
            else:
                self.nodeLauncher.setVisible(False)
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
            self.nodeScript.scriptEditor.setCode(self.node.nodeScript[self.node.nodeVersion])
        self.teTrash.setPlainText(self.node.nodeTrash[self.node.nodeVersion])

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


class Launcher(QtGui.QWidget, wgLauncherUI.Ui_wgLauncher):
    """
    Node Launcher QWidget, child of NodeEditor

    :param mainUi: Grapher main window
    :type mainUi: GrapherUi
    :param pWidget: Parent widget
    :type: NodeEditor
    """

    def __init__(self, mainUi, pWidget):
        self.mainUi = mainUi
        self.pWidget = pWidget
        self.log = self.mainUi.log
        super(Launcher, self).__init__()
        self._setupWidget()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        self.setupUi(self)

    def updateLaunchers(self):
        self.cbLauncher.clear()



class Script(QtGui.QWidget, wgScriptUI.Ui_wgScript):
    """
    Node Script QWidget, child of NodeEditor

    :param mainUi: Grapher main window
    :type mainUi: GrapherUi
    :param pWidget: Parent widget
    :type: NodeEditor
    """

    def __init__(self, mainUi, pWidget):
        self.mainUi = mainUi
        self.pWidget = pWidget
        self.log = self.mainUi.log
        self.grapher = self.mainUi.grapher
        super(Script, self).__init__()
        self._setupWidget()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        self.setupUi(self)
        #-- Script Zone --#
        self.scriptEditor = scriptEditor2.ScriptEditor()
        self.vlScript.addWidget(self.scriptEditor)
        #-- Script Options --#
        self.cbLineNum.clicked.connect(self.on_lineNumber)
        self.cbFolding.clicked.connect(self.on_folding)
        self.cbCompletion.clicked.connect(self.on_completion)
        self.cbTabGuides.clicked.connect(self.on_tabGuides)
        self.cbWhiteSpace.clicked.connect(self.on_whiteSpace)
        self.cbEdge.clicked.connect(self.on_edge)
        #-- Externalize Script --#
        self.pbPush.setIcon(self.mainUi.graphZone.foldIcon)
        self.pbPush.clicked.connect(self.on_push)
        self.pbPull.setIcon(self.mainUi.graphZone.pullIcon)
        self.pbPull.clicked.connect(self.on_pull)

    @property
    def tmpScriptFile(self):
        """
        Get tmp script file

        :return: Tmp script relative path
        :rtype: str
        """
        if self.pWidget.node is not None:
            return os.path.join('tmp', self.mainUi.user, 'externScripts', '%s.py' % self.pWidget.node.nodeName)

    def on_lineNumber(self):
        """
        Command launched when 'Line Num' QCheckBox is clicked

        Enable / disable line numbers
        """
        if self.cbLineNum.isChecked():
            self.scriptEditor.setMarginWidth(0, self.scriptEditor.margeLine)
        else:
            self.scriptEditor.setMarginWidth(0, 0)

    def on_folding(self):
        """
        Command launched when 'Folding' QCheckBox is clicked

        Enable / disable code folding
        """
        if self.cbFolding.isChecked():
            self.scriptEditor.setFolding(QsciScintilla.BoxedTreeFoldStyle)
        else:
            self.scriptEditor.setFolding(QsciScintilla.NoFoldStyle)

    def on_completion(self):
        """
        Command launched when 'Completion' QCheckBox is clicked

        Enable / disable code completion
        """
        if self.cbCompletion.isChecked():
            self.scriptEditor.setAutoCompletionSource(QsciScintilla.AcsDocument)
        else:
            self.scriptEditor.setAutoCompletionSource(QsciScintilla.AcsNone)

    def on_tabGuides(self):
        """
        Command launched when 'Tab Guides' QCheckBox is clicked

        Enable / disable tab guides visiility
        """
        self.scriptEditor.setIndentationGuides(self.cbTabGuides.isChecked())

    def on_whiteSpace(self):
        """
        Command launched when 'White Space' QCheckBox is clicked

        Enable / disable white space visibility
        """
        if self.cbWhiteSpace.isChecked():
            self.scriptEditor.setWhitespaceSize(self.scriptEditor.spaceSize)
        else:
            self.scriptEditor.setWhitespaceSize(0)

    def on_edge(self):
        if self.cbEdge.isChecked():
            self.scriptEditor.setEdgeMode(QsciScintilla.EdgeLine)
        else:
            self.scriptEditor.setEdgeMode(QsciScintilla.EdgeNone)

    def on_push(self):
        """
        Command launched when 'Push' QPushButton is clicked

        Externalise script
        """
        if self.grapher._graphFile is not None:
            self.log.detail(">>> Push script ...")
            scriptPath = self.grapher.createFolders(os.path.dirname(self.tmpScriptFile))
            if scriptPath is not None:
                try:
                    pFile.writeFile(self.tmpScriptFile, str(self.scriptEditor.getCode()))
                    self.log.debug("Saved: %s" % pFile.conformPath(self.tmpScriptFile))
                except:
                    raise IOError("!!! Can not write tmpFile: %s !!!" % pFile.conformPath(self.tmpScriptFile))
            editor = self.grapher.studio.pyCharm
            os.system('%s %s' % (os.path.normpath(editor), os.path.normpath(self.tmpScriptFile)))

    def on_pull(self):
        """
        Command launched when 'Pull' QPushButton is clicked

        Update script
        """
        self.log.detail(">>> Pull script ...")
        if self.tmpScriptFile is not None:
            if os.path.exists(self.tmpScriptFile):
                self.scriptEditor.setCode(''.join(pFile.readFile(self.tmpScriptFile)))
                self.log.debug("Updated: %s" % pFile.conformPath(self.tmpScriptFile))
                os.remove(self.tmpScriptFile)
