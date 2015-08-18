import os, sys
from appli import grapher
from functools import partial
from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.grapher.gui.ui import grapherUI
from appli.grapher.gui import graphTree, graphView, graphNodes, toolsWgts, nodeEditor


class GrapherUi(QtGui.QMainWindow, grapherUI.Ui_mwGrapher):

    def __init__(self, logLvl='info'):
        self.log = pFile.Logger(title="GrapherUi", level=logLvl)
        self.log.info("########## Launching Grapher Ui ##########")
        self.user = grapher.user
        self.station = grapher.station
        self.binPath = grapher.binPath
        self.iconPath = grapher.iconPath
        self.enabledIcon = QtGui.QIcon(os.path.join(self.iconPath, 'png', 'enabled.png'))
        self.disabledIcon = QtGui.QIcon(os.path.join(self.iconPath, 'png', 'disabled.png'))
        self.expandIcon = QtGui.QIcon(os.path.join(self.iconPath, 'png', 'expand.png'))
        self.collapseIcon = QtGui.QIcon(os.path.join(self.iconPath, 'png', 'collapse.png'))
        self._graphNodes = graphNodes
        super(GrapherUi, self).__init__()
        self._setupUi()

    def _setupUi(self):
        self.log.info("#-- Setup Main Ui --#", newLinesBefor=1)
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self._initWidgets()
        self._initMenu()

    # noinspection PyUnresolvedReferences
    def _initWidgets(self):
        self.log.info("#-- Init Widgets --#", newLinesBefor=1)
        #-- Graph Zone --#
        self.graphTree = graphTree.GraphTree(self)
        self.treeView = graphTree.TreeView(self, self.graphTree)
        self.vlGraphZone.insertWidget(0, self.graphTree)
        self.graphScene = graphView.GraphScene(self)
        self.graphView = graphView.GraphView(self, self.graphScene)
        self.vlGraphZone.insertWidget(0, self.graphView)
        #-- GraphTools --#
        self.graphTools = toolsWgts.GraphTools(self)
        self.tbTools.addWidget(self.graphTools)
        self.tbTools.orientationChanged.connect(partial(self.on_miToolsOrientChanged, orient=False, force=False))
        #-- Node Editor --#
        self.nodeEditor = nodeEditor.NodeEditor(self)
        self.vlNodeEditor.insertWidget(0, self.nodeEditor)

    # noinspection PyUnresolvedReferences
    def _initMenu(self):
        self.log.info("#-- Init Menus --#", newLinesBefor=1)
        self._menuGraph()
        self._menuDisplay()
        self._menuHelp()
        self.log.info("// ===> Grapher Ui Ready !!!", newLinesBefor=1, newLinesAfter=1)
        self.on_miNodeEditor()

    # noinspection PyUnresolvedReferences
    def _menuGraph(self):
        self.log.debug("\t ---> Menu Graph ...")
        self.miRefresh.triggered.connect(self.on_miRefresh)
        self.miRefresh.setShortcut("F5")
        self.miUnselectAll.triggered.connect(self.on_miUnselectAll)
        self.miUnselectAll.setShortcut("Esc")
        #-- SubMenu 'Create Node' --#
        self.miModul.triggered.connect(partial(self.on_miNewNode, 'modul'))
        self.miModul.setShortcut("1")
        self.miSysData.triggered.connect(partial(self.on_miNewNode, 'sysData'))
        self.miSysData.setShortcut("2")
        self.miCmdData.triggered.connect(partial(self.on_miNewNode, 'cmdData'))
        self.miCmdData.setShortcut("3")
        self.miPyData.triggered.connect(partial(self.on_miNewNode, 'pyData'))
        self.miPyData.setShortcut("4")
        #-- SubMenu 'Fold / Unfold' --#
        self.miFoldUnfold.triggered.connect(partial(self.on_miFoldUnfold, _mode='branch', toggle=True))
        self.miFoldUnfold.setShortcut("G")
        self.miExpandSel.triggered.connect(partial(self.on_miFoldUnfold, expand=True, _mode='sel'))
        self.miExpandSel.setShortcut("Right")
        self.miExpandBranch.triggered.connect(partial(self.on_miFoldUnfold, expand=True, _mode='branch'))
        self.miExpandBranch.setShortcut("Ctrl+Right")
        self.miExpandAllEnable.triggered.connect(partial(self.on_miFoldUnfold, expand=True, _mode='active'))
        self.miExpandAllEnable.setShortcut("Shift+Right")
        self.miExpandAll.triggered.connect(partial(self.on_miFoldUnfold, expand=True, _mode='all'))
        self.miExpandAll.setShortcut("Alt+Right")
        self.miCollapseSel.triggered.connect(partial(self.on_miFoldUnfold, expand=False, _mode='sel'))
        self.miCollapseSel.setShortcut("Left")
        self.miCollapseBranch.triggered.connect(partial(self.on_miFoldUnfold, expand=False, _mode='branch'))
        self.miCollapseBranch.setShortcut("Ctrl+Left")
        self.miCollapseAllEnabled.triggered.connect(partial(self.on_miFoldUnfold, expand=False, _mode='active'))
        self.miCollapseAllEnabled.setShortcut("Shift+Left")
        self.miCollapseAll.triggered.connect(partial(self.on_miFoldUnfold, expand=False, _mode='all'))
        self.miCollapseAll.setShortcut("Alt+Left")
        #-- SubMenu 'Copy / Paste' --#
        self.miCopyNodes.triggered.connect(partial(self.on_miCopy, _mode='nodes', rm=False))
        self.miCopyNodes.setShortcut("Ctrl+C")
        self.miCopyBranch.triggered.connect(partial(self.on_miCopy, _mode='branch', rm=False))
        self.miCopyBranch.setShortcut("Shift+C")
        self.miCutBranch.triggered.connect(partial(self.on_miCopy, _mode='branch', rm=True))
        self.miCutBranch.setShortcut("Ctrl+X")
        self.miPaste.triggered.connect(self.on_miPasteNodes)
        self.miPaste.setShortcut("Ctrl+V")
        #-- SubMenu 'Move Up / Down' --#
        self.miMoveUp.triggered.connect(partial(self.on_moveNodes, side='up'))
        self.miMoveUp.setShortcut("Ctrl+Up")
        self.miMoveDn.triggered.connect(partial(self.on_moveNodes, side='down'))
        self.miMoveDn.setShortcut("Ctrl+Down")
        #-- Fit In Options --#
        self.miFitInScene.triggered.connect(self.on_miFitInScene)
        self.miFitInScene.setShortcut("H")
        self.miFitInSel.triggered.connect(self.on_miFitInSelected)
        self.miFitInSel.setShortcut("F")
        #-- Others --#
        self.miDelSel.triggered.connect(self.on_miDeleteSelected)
        self.miDelSel.setShortcut("Del")

    # noinspection PyUnresolvedReferences
    def _menuDisplay(self):
        self.log.debug("\t ---> Menu Display ...")
        #-- Widgets Visibility --#
        self.miNodeEditor.triggered.connect(self.on_miNodeEditor)
        self.miNodeEditor.setShortcut("E")
        self.miGraphView.triggered.connect(self.on_miGraphView)
        self.miGraphView.setShortcut("Tab")
        self.miToolsVisibility.triggered.connect(self.on_miToolsVisibility)
        self.miToolsVisibility.setShortcut("T")
        #-- SubMenu 'Tools Bar Orient' --#
        self.miBarHorizontal.triggered.connect(partial(self.on_miToolsOrientChanged, orient='horizontal', force=True))
        self.miBarVertical.triggered.connect(partial(self.on_miToolsOrientChanged, orient='vertical', force=True))
        #-- SubMenu 'Tools Tab Orient' --#
        self.miTabNorth.triggered.connect(partial(self.on_miTabOrientChanged, 'North'))
        self.miTabSouth.triggered.connect(partial(self.on_miTabOrientChanged, 'South'))
        self.miTabWest.triggered.connect(partial(self.on_miTabOrientChanged, 'West'))
        self.miTabEast.triggered.connect(partial(self.on_miTabOrientChanged, 'East'))
        #-- Tools Options --#
        self.miToolsIconOnly.triggered.connect(self.on_miToolsIconOnly)
        self.miToolsIconOnly.setShortcut("Ctrl+T")

    # noinspection PyUnresolvedReferences
    def _menuHelp(self):
        self.log.debug("\t ---> Menu Help ...")
        self.miTreeDict.triggered.connect(self.on_printTreeDict)

    @staticmethod
    def _checkNodeName(nodeName, items):
        """
        Check new nodeName and return a unique name
        :param nodeName: New nodeName
        :type nodeName: str
        :param items: Items to compare with
        :type: list
        :return: New valide node name
        :rtype: str
        """
        rejected = [' ', '-', ',', ';', ':', '.', '/', '!', '?', '*', '$', '=', '+', '\'', '\\', '"', '&']
        #-- Check Rejected --#
        for r in rejected:
            if r in nodeName:
                nodeName.replace(r, '')
        #-- Check CamelCase --#
        if '_' in nodeName:
            if not nodeName.split('_')[-1].isdigit():
                nodeName.replace('_', '')
        #-- Check Index --#
        if not '_' in nodeName:
            nodeName = '%s_1' % nodeName
        #-- Find Same Base Name --#
        founds = []
        for item in items:
            if nodeName == item.nodeName:
                if not item.nodeName in founds:
                    founds.append(item.nodeName)
            elif item.nodeName.startswith(nodeName.split('_')[0]):
                if not item.nodeName in founds:
                    founds.append(item.nodeName)
        #-- Result: Name Is Unique --#
        if not founds or not nodeName in founds:
            return nodeName
        #-- Result: Generate Unique Name --#
        iList = []
        for f in founds:
            iList.append(int(f.split('_')[-1]))
        return '%s_%s' % (nodeName.split('_')[0], (max(iList) + 1))

    @property
    def currentGraphMode(self):
        """
        Get GraphZone mode
        :return: GraphZone mode ('tree' or 'scene')
        :rtype: str
        """
        if self.miGraphView.isChecked():
            return 'scene'
        else:
            return 'tree'

    @property
    def currentView(self):
        """
        Get current GraphZone widget
        :return: GraphZone widget ('self.graphTree' or 'self.graphView')
        :rtype: GrapherUi.treeView | GrapherUi.graphView
        """
        if self.currentGraphMode == 'tree':
            return self.treeView
        elif self.currentGraphMode == 'scene':
            return self.graphView

    @property
    def currentGraph(self):
        """
        Get current GraphZone widget
        :return: GraphZone widget ('self.graphTree' or 'self.graphView')
        :rtype: GrapherUi.graphTree | GrapherUi.graphView
        """
        if self.currentGraphMode == 'tree':
            return self.graphTree
        elif self.currentGraphMode == 'scene':
            return self.graphScene

    @property
    def toolsIconOnly(self):
        """
        Get tools icon only state
        :return: Tools icon only state
        :rtype: bool
        """
        return self.miToolsIconOnly.isChecked()

    @staticmethod
    def getNodeDictFromNodeName(treeDict, nodeName):
        """
        Get node dict from given nodeName
        :param treeDict: TreeGraph repr
        :type treeDict: dict
        :param nodeName: Graph node name
        :type nodeName: str
        :return: Node dict
        :rtype: dict
        """
        for n in sorted(treeDict.keys()):
            if treeDict[n]['_nodeName'] == nodeName:
                return treeDict[n]

    def on_miRefresh(self):
        """
        Command launched when 'Refresh' QMenuItem is triggered.
        Refresh graph tree
        """
        self.log.detail(">>> Launch menuItem 'Refresh' ...")
        if self.currentGraphMode == 'tree':
            graphDict = self.graphTree.__repr__()
            self.graphTree.clearSelection()
            self.graphTree.clear()
            self.graphTree.buildGraph(graphDict)
        else:
            self.log.detail("\t\t >>> Not yet implemented !!!")

    def on_miNewNode(self, nodeType):
        """
        Command launched when 'New Node' QMenuItem is triggered.
        Create new node (modul)
        :param nodeType: Graph node type ('modul', 'sysData', 'cmdData', 'pyData', 'loop', 'condition')
        :type nodeType: str
        """
        self.log.detail(">>> Launch menuItem 'New Node' ...")
        self.currentGraph.createGraphNode(nodeType=nodeType)

    def on_miFoldUnfold(self, expand=True, _mode='sel', toggle=False):
        """
        Manage graphNodes folding and unfolding
        :param expand: Expand state
        :type expand: bool
        :param _mode: 'sel', 'branch', 'active', or 'all'
        :type _mode: str
        :param toggle: Enable automatic switch
        :type toggle: bool
        """
        self.log.detail(">>> Launch menuItem 'Fold / Unfold' ...")
        if self.currentGraphMode == 'tree':
            self.currentView.foldUnfold(expand=expand, _mode=_mode, toggle=toggle)
        else:
            self.log.detail("\t\t >>> Not yet implemented !!!")

    def on_miUnselectAll(self):
        """
        Command launched when 'Unselect All' QMenuItem is triggered.
        Unselect all graph nodes
        """
        self.log.detail(">>> Launch menuItem 'Unselect All' ...")
        if self.currentGraphMode == 'tree':
            self.graphTree.clearSelection()
        else:
            self.log.detail("\t\t >>> Not yet implemented !!!")

    def on_miCopy(self, _mode='nodes', rm=False):
        """
        Command launched when 'Copy Nodes / Branch' or 'Cut Nodes' QMenuItem is triggered.
        Copy / Cut selected nodes or branch
        :param _mode: 'nodes' or 'branch'
        :type _mode: str
        :param rm: Remove selected nodes (cut)
        :type rm: bool
        """
        if self.currentGraphMode == 'tree':
            if not rm:
                self.log.detail(">>> Launch menuItem 'Copy %s' ..." % _mode)
            else:
                self.log.detail(">>> Launch menuItem 'Cut Nodes' ...")
            self.treeView.copyNodes(_mode=_mode, rm=rm)
        else:
            self.log.detail("\t\t >>> Not yet implemented !!!")

    def on_miPasteNodes(self):
        """
        Command launched when 'Paste' QMenuItem is triggered.
        Paste stored nodes
        """
        self.log.detail(">>> Launch menuItem 'Paste Nodes' ...")
        if self.currentGraphMode == 'tree':
            self.treeView.pasteNodes()
        else:
            self.log.detail("\t\t >>> Not yet implemented !!!")

    def on_moveNodes(self, side='up'):
        """
        Command launched when 'Move Up / Down' QMenuItem is triggered.
        Move up or down selected nodes
        :param side: 'up' or 'down'
        :type side: str
        """
        self.log.detail(">>> Launch menuItem 'Move Nodes' ...")
        if self.currentGraphMode == 'tree':
            self.treeView.moveNodes(side=side)
        else:
            self.log.detail("\t\t >>> Not yet implemented !!!")

    def on_miDeleteSelected(self):
        """
        Command launched when 'Delete Selected' QMenuItem is triggered.
        Launch deletion confirm dialog
        """
        self.log.detail(">>> Launch menuItem 'Delete Selected' ...")
        if self.currentGraphMode == 'tree':
            self.fdDelNode = pQt.ConfirmDialog("Delete selected nodes and children ?", ['Delete'],
                                               [self.deleteSelected])
            self.fdDelNode.exec_()
        else:
            self.log.detail("\t\t >>> Not yet implemented !!!")

    def deleteSelected(self):
        """
        Delete selected nodes
        """
        self.log.detail("\t ---> Deletion confirmed.")
        self.fdDelNode.close()
        if self.currentGraphMode == 'tree':
            self.treeView.deleteSelectedNodes()
        else:
            self.log.detail("\t\t >>> Not yet implemented !!!")

    def on_miFitInScene(self):
        """
        Command launched when 'Fit In Scene' QMenuItem is triggered.
        Fit GraphView to scene
        """
        self.log.detail(">>> Launch menuItem 'Fit In Scene' ...")
        if self.currentGraphMode == 'tree':
            self.log.detail("\t\t >>> Not available for 'tree' mode !!!")
        else:
            self.graphView.fitInScene()

    def on_miFitInSelected(self):
        """
        Command launched when 'Fit In Selected' QMenuItem is triggered.
        Fit GraphView to scene selection
        """
        self.log.detail(">>> Launch menuItem 'Fit In Selected' ...")
        if self.currentGraphMode == 'tree':
            self.log.detail("\t\t >>> Not available for 'tree' mode !!!")
        else:
            self.graphView.fitInSelected()

    def on_miNodeEditor(self):
        """
        Command launched when 'Node Editor' QMenuItem is triggered
        Show / Hide node editor
        """
        self.log.detail(">>> Launch menuItem 'Node Editor' ...")
        self.vfNodeEditor.setVisible(self.miNodeEditor.isChecked())

    def on_miGraphView(self):
        """
        Command launched when 'Graph View' QMenuItem is triggered
        Show / Hide Graph View
        """
        self.log.detail(">>> Launch menuItem 'Switch Graph Mode' ...")
        self.graphTree.setVisible(not self.miGraphView.isChecked())
        self.graphView.setVisible(self.miGraphView.isChecked())

    def on_miToolsOrientChanged(self, orient=False, force=False):
        """
        Orient toolsTab and their contents
        :param orient: 'horizontal' or 'vertical'
        :type orient: str
        :param force: Force orientation
        :type force: bool
        """
        self.log.detail(">>> Launch menuItem 'Tools Orient' ...")
        if force:
            if orient == 'horizontal':
                self.tbTools.setOrientation(QtCore.Qt.Horizontal)
            elif orient == 'vertical':
                self.tbTools.setOrientation(QtCore.Qt.Vertical)
        if self.tbTools.orientation() == 1:
            self.graphTools.tabOrientation('North')
            self.miToolsIconOnly.setChecked(True)
        else:
            self.graphTools.tabOrientation('West')
            self.miToolsIconOnly.setChecked(False)
        self.graphTools.toolsAspect()

    def on_miTabOrientChanged(self, orient):
        """
        Command launched when 'Tab Orient' QMenuItem is triggered
        Orient tab contents
        :param orient: 'North', 'South', 'West' or 'East'
        :type orient: str
        """
        self.log.detail(">>> Launch menuItem 'Tab Orient' ...")
        self.graphTools.tabOrientation(orient)

    def on_miToolsVisibility(self):
        """
        Command launched when 'Tools Visibility' QMenuItem is triggered
        Turn on or off tools bar visibility
        """
        self.log.detail(">>> Launch menuItem 'Tools Visibility' ...")
        self.tbTools.setVisible(self.miToolsVisibility.isChecked())

    def on_miToolsIconOnly(self):
        """
        Command launched when 'Tools Icon Only' QMenuItem is triggered
        Switch toolsTab aspect
        """
        self.log.detail(">>> Launch menuItem 'Tools Icon Only' ...")
        self.graphTools.toolsAspect()

    def on_printTreeDict(self):
        """
        Command launched when 'Print Tree Dict' QMenuItem is triggered.
        Print graph tree repr
        """
        self.log.detail(">>> Launch menuItem 'Print Tree Dict' ...")
        print self.graphTree.__str__()


def launch(logLvl='info'):
    """
    Grapher launcher
    :param logLvl: Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """
    app = QtGui.QApplication(sys.argv)
    window = GrapherUi(logLvl=logLvl)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch(logLvl='detail')
