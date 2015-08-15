import os, sys
from appli import fondation
from functools import partial
from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.fondation.gui.ui import fondationUI
from appli.fondation.gui import graphTree, graphView, graphNodes, toolsWgts, nodeEditor


class FondationUi(QtGui.QMainWindow, fondationUI.Ui_mwFondation):

    def __init__(self, logLvl='info'):
        self.log = pFile.Logger(title="FondationUI", level=logLvl)
        self.log.info("########## Launching Fondation Ui ##########")
        self.user = fondation.user
        self.station = fondation.station
        self.binPath = fondation.binPath
        self.iconPath = fondation.iconPath
        self.enabledIcon = QtGui.QIcon(os.path.join(self.iconPath, 'enabled.png'))
        self.disabledIcon = QtGui.QIcon(os.path.join(self.iconPath, 'disabled.png'))
        self.expandIcon = QtGui.QIcon(os.path.join(self.iconPath, 'expand.png'))
        self.collapseIcon = QtGui.QIcon(os.path.join(self.iconPath, 'collapse.png'))
        self._graphNodes = graphNodes
        super(FondationUi, self).__init__()
        self._setupUi()

    def _setupUi(self):
        self.log.info("#-- Setup Main Ui --#")
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self._initWidgets()
        self._initMenu()

    # noinspection PyUnresolvedReferences
    def _initWidgets(self):
        self.log.info("#-- Init Widgets --#")
        #-- Graph Zone --#
        self.graphTree = graphTree.GraphTree(self)
        self.graphScene = graphView.GraphScene(self)
        self.graphView = graphView.GraphView(self, self.graphScene)
        self.vlGraphScene.insertWidget(0, self.graphTree)
        self.vlGraphScene.insertWidget(0, self.graphView)
        #-- GraphTools --#
        self.graphTools = toolsWgts.GraphTools(self)
        self.tbTools.addWidget(self.graphTools)
        self.tbTools.orientationChanged.connect(partial(self.on_miToolsOrientChanged, orient=False, force=False))
        #-- Node Editor --#
        self.nodeEditor = nodeEditor.NodeEditor(self)
        self.vlNodeEditor.insertWidget(0, self.nodeEditor)

    # noinspection PyUnresolvedReferences
    def _initMenu(self):
        self.log.info("#-- Init Menus --#")
        self._menuGraph()
        self._menuDisplay()
        self._menuHelp()
        self.on_miNodeEditor()

    # noinspection PyUnresolvedReferences
    def _menuGraph(self):
        self.log.debug("\t ---> Menu Graph ...")
        #-- SubMenu 'Create Node' --#
        self.miNewNode.triggered.connect(partial(self.on_miNewNode, 'modul'))
        self.miNewNode.setShortcut("N")
        self.miModul.triggered.connect(partial(self.on_miNewNode, 'modul'))
        self.miSysData.triggered.connect(partial(self.on_miNewNode, 'sysData'))
        self.miCmdData.triggered.connect(partial(self.on_miNewNode, 'cmdData'))
        self.miPyData.triggered.connect(partial(self.on_miNewNode, 'pyData'))
        #-- SubMenu 'Fold / Unfold' --#
        self.miExpandSel.triggered.connect(partial(self.on_miFoldUnfold, expand=True, _mode='sel'))
        self.miExpandSel.setShortcut("F")
        self.miExpandAll.triggered.connect(partial(self.on_miFoldUnfold, expand=True, _mode='all'))
        self.miExpandAll.setShortcut("Alt+F")
        self.miCollapseSel.triggered.connect(partial(self.on_miFoldUnfold, expand=False, _mode='sel'))
        self.miCollapseAll.triggered.connect(partial(self.on_miFoldUnfold, expand=False, _mode='all'))
        self.miCollapseAll.setShortcut("Ctrl+F")
        #-- Copy Nodes / Branch --#
        self.miCopyNodes.triggered.connect(partial(self.on_miCopy, _mode='nodes', rm=False))
        self.miCopyNodes.setShortcut("Ctrl+C")
        self.miCopyBranch.triggered.connect(partial(self.on_miCopy, _mode='branch', rm=False))
        self.miCopyBranch.setShortcut("Shift+C")
        self.miCutBranch.triggered.connect(partial(self.on_miCopy, _mode='branch', rm=True))
        self.miCutBranch.setShortcut("Ctrl+X")
        self.miPaste.triggered.connect(self.on_miPasteNodes)
        self.miPaste.setShortcut("Ctrl+V")
        #-- Move Up / Down --#
        self.miMoveUp.setShortcut("Ctrl+Up")
        self.miMoveDn.setShortcut("Ctrl+Down")
        #-- Others --#
        self.miRefresh.triggered.connect(self.on_miRefresh)
        self.miRefresh.setShortcut("F5")
        self.miUnselectAll.triggered.connect(self.on_miUnselectAll)
        self.miUnselectAll.setShortcut("Esc")
        self.miDelSel.triggered.connect(self.on_miDeleteSelected)
        self.miDelSel.setShortcut("Del")

    # noinspection PyUnresolvedReferences
    def _menuDisplay(self):
        self.log.debug("\t ---> Menu Display ...")
        #-- SubMenu 'Tools Bar Orient' --#
        self.miBarHorizontal.triggered.connect(partial(self.on_miToolsOrientChanged, orient='horizontal', force=True))
        self.miBarVertical.triggered.connect(partial(self.on_miToolsOrientChanged, orient='vertical', force=True))
        #-- SubMenu 'Tools Tab Orient' --#
        self.miTabNorth.triggered.connect(partial(self.on_miTabOrientChanged, 'North'))
        self.miTabSouth.triggered.connect(partial(self.on_miTabOrientChanged, 'South'))
        self.miTabWest.triggered.connect(partial(self.on_miTabOrientChanged, 'West'))
        self.miTabEast.triggered.connect(partial(self.on_miTabOrientChanged, 'East'))
        #-- Others --#
        self.miNodeEditor.triggered.connect(self.on_miNodeEditor)
        self.miNodeEditor.setShortcut("E")
        self.miToolsVisibility.triggered.connect(self.on_miToolsVisibility)
        self.miToolsVisibility.setShortcut("T")
        self.miToolsIconOnly.triggered.connect(self.on_miToolsIconOnly)
        self.miToolsIconOnly.setShortcut("Ctrl+T")

    # noinspection PyUnresolvedReferences
    def _menuHelp(self):
        self.log.debug("\t ---> Menu Help ...")
        self.miTreeDict.triggered.connect(self.on_printTreeDict)

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
        graphDict = self.graphTree.__repr__()
        self.graphTree.clear()
        self.graphTree.buildGraph(graphDict)

    def on_miNewNode(self, nodeType):
        """
        Command launched when 'New Node' QMenuItem is triggered.
        Create new node (modul)
        :param nodeType: Graph node type ('modul', 'sysData', 'cmdData', 'pyData', 'loop', 'condition')
        :type nodeType: str
        """
        self.log.detail(">>> Launch menuItem 'New Node' ...")
        self.graphTree.add_graphNode(nodeType=nodeType)

    def on_miFoldUnfold(self, expand=True, _mode='sel'):
        """
        Manage graphNodes folding and unfolding
        :param expand: Expand state
        :type expand: bool
        :param _mode: 'sel' or 'all'
        :type _mode: str
        """
        self.log.detail(">>> Launch menuItem 'Fold / Unfold' ...")
        self.graphTree.foldUnfold(expand=expand, _mode=_mode)

    def on_miUnselectAll(self):
        """
        Command launched when 'Unselect All' QMenuItem is triggered.
        Unselect all graph nodes
        """
        self.log.detail(">>> Launch menuItem 'Unselect All' ...")
        self.graphTree.clearSelection()

    def on_miCopy(self, _mode='nodes', rm=False):
        """
        Command launched when 'Copy Nodes / Branch' or 'Cut Nodes' QMenuItem is triggered.
        Copy / Cut selected nodes or branch
        :param _mode: 'nodes' or 'branch'
        :type _mode: str
        :param rm: Remove selected nodes (cut)
        :type rm: bool
        """
        if not rm:
            self.log.detail(">>> Launch menuItem 'Copy %s' ..." % _mode)
        else:
            self.log.detail(">>> Launch menuItem 'Cut Nodes' ...")
        self.graphTree.copyNodes(_mode=_mode, rm=rm)

    def on_miPasteNodes(self):
        """
        Command launched when 'Paste' QMenuItem is triggered.
        Paste stored nodes
        """
        self.graphTree.pasteNodes()

    def on_miDeleteSelected(self):
        """
        Command launched when 'Delete Selected' QMenuItem is triggered.
        Launch deletion confirm dialog
        """
        self.log.detail(">>> Launch menuItem 'Delete Selected' ...")
        self.fdDelNode = pQt.ConfirmDialog("Delete selected nodes and children ?", ['Delete'],
                                           [self.deleteSelected])
        self.fdDelNode.exec_()

    def deleteSelected(self):
        """
        Delete selected nodes
        """
        self.log.detail("\t ---> Deletion confirmed.")
        self.fdDelNode.close()
        self.graphTree.deleteSelectedNodes()

    def on_miNodeEditor(self):
        """
        Command launched when 'Node Editor' QMenuItem is triggered
        Show / Hide node editor
        """
        self.log.detail(">>> Launch menuItem 'Node Editor' ...")
        self.vfNodeEditor.setVisible(self.miNodeEditor.isChecked())

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
    window = FondationUi(logLvl=logLvl)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch(logLvl='detail')
