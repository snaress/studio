import os, sys
from appli import fondation
from functools import partial
from PyQt4 import QtGui, QtCore
from lib.system import procFile as pFile
from appli.fondation.gui.ui import fondationUI
from appli.fondation.gui import graphWgts, graphNodes, toolsWgts


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
        """
        Setup main ui
        """
        self.log.debug("#-- Setup Main Ui --#")
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self._initWidgets()
        self._initMenu()

    # noinspection PyUnresolvedReferences
    def _initWidgets(self):
        """
        Init ui widgets
        """
        self.log.debug("#-- Init Widgets --#")
        #-- Graph Zone --#
        self.graphTree = graphWgts.GraphTree(self)
        self.vlGraphScene.insertWidget(0, self.graphTree)
        #-- GraphTools --#
        self.graphTools = toolsWgts.GraphTools(self)
        self.tbTools.addWidget(self.graphTools)
        self.tbTools.orientationChanged.connect(partial(self.on_toolsOrientChanged, orient=False, force=False))

    # noinspection PyUnresolvedReferences
    def _initMenu(self):
        """
        Init ui menu
        """
        self._menuGraph()
        self._menuDisplay()

    # noinspection PyUnresolvedReferences
    def _menuGraph(self):
        """
        Init menu 'Graph'
        """
        #-- SubMenu 'Create Node' --#
        self.miNewNode.triggered.connect(partial(self.on_miNewNode, 'modul'))
        self.miNewNode.setShortcut("N")
        self.miModul.triggered.connect(partial(self.on_miNewNode, 'modul'))
        self.miSysData.triggered.connect(partial(self.on_miNewNode, 'sysData'))
        self.miCmdData.triggered.connect(partial(self.on_miNewNode, 'cmdData'))
        self.miPyData.triggered.connect(partial(self.on_miNewNode, 'pyData'))
        #-- SubMenu 'Fold / Unfold' --#
        self.miExpandSel.triggered.connect(partial(self.on_foldUnfold, expand=True, _mode='sel'))
        self.miExpandSel.setShortcut("F")
        self.miExpandAll.triggered.connect(partial(self.on_foldUnfold, expand=True, _mode='all'))
        self.miExpandAll.setShortcut("Alt+F")
        self.miCollapseSel.triggered.connect(partial(self.on_foldUnfold, expand=False, _mode='sel'))
        self.miCollapseAll.triggered.connect(partial(self.on_foldUnfold, expand=False, _mode='all'))
        self.miCollapseAll.setShortcut("Ctrl+F")
        #-- SubMenu 'Hide / Unhide' --#
        self.miHideSel.triggered.connect(partial(self.on_hideUnhide, hidden=True, _mode='sel'))
        self.miHideSel.setShortcut("H")
        self.miHideAll.triggered.connect(partial(self.on_hideUnhide, hidden=True, _mode='all'))
        self.miHideAll.setShortcut("Alt+H")
        self.miUnhideSel.triggered.connect(partial(self.on_hideUnhide, hidden=False, _mode='sel'))
        self.miUnhideAll.triggered.connect(partial(self.on_hideUnhide, hidden=False, _mode='all'))
        self.miUnhideAll.setShortcut("Ctrl+H")
        #-- Others --#
        self.miUnselectAll.triggered.connect(self.on_unselectAll)
        self.miUnselectAll.setShortcut("Esc")

    # noinspection PyUnresolvedReferences
    def _menuDisplay(self):
        """
        Init menu 'Display'
        """
        #-- SubMenu 'Tools Bar Orient' --#
        self.miBarHorizontal.triggered.connect(partial(self.on_toolsOrientChanged, orient='horizontal', force=True))
        self.miBarVertical.triggered.connect(partial(self.on_toolsOrientChanged, orient='vertical', force=True))
        #-- SubMenu 'Tools Tab Orient' --#
        self.miTabNorth.triggered.connect(partial(self.graphTools.tabOrientation, 'North'))
        self.miTabSouth.triggered.connect(partial(self.graphTools.tabOrientation, 'South'))
        self.miTabWest.triggered.connect(partial(self.graphTools.tabOrientation, 'West'))
        self.miTabEast.triggered.connect(partial(self.graphTools.tabOrientation, 'East'))
        #-- Others --#
        self.miToolsVisibility.triggered.connect(self.on_toolsVisibility)
        self.miToolsVisibility.setShortcut("T")
        self.miToolsIconOnly.triggered.connect(self.graphTools.toolsAspect)
        self.miToolsIconOnly.setShortcut("Ctrl+T")

    @property
    def toolsIconOnly(self):
        return self.miToolsIconOnly.isChecked()

    def on_miNewNode(self, nodeType):
        """
        Command launched when 'New Node' QMenuItem is triggered.
        Create new node (modul)
        :param nodeType: Graph node type ('modul', 'sysData', 'cmdData', 'pyData', 'loop', 'condition')
        :type nodeType: str
        """
        self.graphTree.add_graphNode(nodeType=nodeType)

    def on_foldUnfold(self, expand=True, _mode='sel'):
        """
        Manage graphNodes folding and unfolding
        :param _expand: Expand state
        :type _expand: bool
        :param _mode: 'sel' or 'all'
        :type _mode: str
        """
        self.graphTree.foldUnfold(expand=expand, _mode=_mode)

    def on_hideUnhide(self, hidden=False, _mode='sel'):
        self.graphTree.hideUnhide(hidden=hidden, _mode=_mode)

    def on_unselectAll(self):
        """
        Command launched when 'Unselect All' QMenuItem is triggered.
        Unselect all graph nodes
        """
        self.graphTree.clearSelection()

    def on_toolsOrientChanged(self, orient=False, force=False):
        """
        Orient toolsTab and their contents
        :param orient: 'horizontal' or 'vertical'
        :type orient: str
        :param force: Force orientation
        :type force: bool
        """
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

    def on_toolsVisibility(self):
        """
        Command launched when 'Tools Visibility' QMenuItem is triggered
        Turn on or off tools bar visibility
        """
        self.tbTools.setVisible(self.miToolsVisibility.isChecked())


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
    launch(logLvl='debug')
