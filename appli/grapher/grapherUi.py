import os, sys
from pprint import pprint
from appli import grapher
from lib.env import studio
from functools import partial
from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.grapher.gui.ui import grapherUI
from appli.grapher.gui import projectWgts, toolsWgts, dataWgts, graphWgts


class GrapherUi(QtGui.QMainWindow, grapherUI.Ui_mwGrapher, pQt.Style):
    """
    Grapher appli main class
    :param logLvl: Log level ('critical', 'error', 'warning', 'info', 'debug')
    :type logLvl: str
    """

    def __init__(self, project=None, logLvl='info'):
        self.log = pFile.Logger(title="Grapher-UI", level=logLvl)
        self.log.info("#-- Launching Grapher Ui --#")
        self.studio = studio
        self.grapherRootPath = grapher.grapherRootPath
        self.prodsRootPath = grapher.prodsRootPath
        super(GrapherUi, self).__init__()
        self.projectPath = None
        self.projectName = None
        self.projectAlias = None
        self.projectFullName = None
        self._setupUi()
        if project is not None:
            self.loadProject(project)

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup main ui
        """
        self.log.debug("---> Setup Main Ui ...")
        self.setupUi(self)
        #-- GraphTree --#
        self.graphTree = projectWgts.ProjectTree(self)
        self.vlProjectTree.addWidget(self.graphTree)
        #-- GraphZone --#
        self.on_addGraphZone()
        #-- DataZone --#
        self.dataZone = dataWgts.DataZone(self)
        #-- GraphTools --#
        self.graphTools = toolsWgts.ToolsBar(self)
        self.tbTools.addWidget(self.graphTools)
        self.tbTools.orientationChanged.connect(partial(self.on_toolBarOrientChanged, orient=False, force=False))
        #-- GraphMenu --#
        self._setupMenu()
        self.on_toolBarVisibility()
        self.on_toolBarOrientChanged()
        self.on_dataVisibility()

    # noinspection PyUnresolvedReferences
    def _setupMenu(self):
        """
        Setup main ui menu
        """
        #-- Menu Grapher --#
        self.miLoadProject.triggered.connect(self.on_loadProject)
        self.miEditProject.triggered.connect(self.on_editProject)
        self.miSaveGraphAs.triggered.connect(self.on_saveGraphAs)
        #-- Menu Edit --#
        self.miAddGraphZone.triggered.connect(self.on_addGraphZone)
        self.miAddGraphZone.setShortcut("Ctrl+N")
        self.miEditMode.triggered.connect(self.on_editMode)
        self.miEditMode.setShortcut("Ctrl+E")
        self.miConnectNodes.triggered.connect(self.on_connectNodes)
        self.miConnectNodes.setShortcut("L")
        #-- Menu Display --#
        self.miTreeVisibility.triggered.connect(self.on_treeVisibility)
        self.miTreeVisibility.setShortcut("Shift+T")
        self.miDataVisibility.triggered.connect(self.on_dataVisibility)
        self.miDataVisibility.setShortcut("Ctrl+D")
        self.miToolBarVisibility.triggered.connect(self.on_toolBarVisibility)
        self.miToolBarVisibility.setShortcut("Ctrl+T")
        self.miFitInScene.triggered.connect(self.on_fitInScene)
        self.miFitInScene.setShortcut("H")
        self.miFitInSelection.triggered.connect(self.on_fitInSelection)
        self.miFitInSelection.setShortcut("F")
        #-- Menu Pref --#
        self.miDefaultStyle.triggered.connect(partial(self.on_StyleOption, styleName='default'))
        self.miDarkOrange.triggered.connect(partial(self.on_StyleOption, styleName='darkOrange'))
        self.miDarkGrey.triggered.connect(partial(self.on_StyleOption, styleName='darkGrey'))
        self.miRedGrey.triggered.connect(partial(self.on_StyleOption, styleName='redGrey'))
        self.miBarHorizontal.triggered.connect(partial(self.on_toolBarOrientChanged, orient='horizontal', force=True))
        self.miBarVertical.triggered.connect(partial(self.on_toolBarOrientChanged, orient='vertical', force=True))
        self.miTabNorth.triggered.connect(partial(self.graphTools.tabOrientation, 'North'))
        self.miTabSouth.triggered.connect(partial(self.graphTools.tabOrientation, 'South'))
        self.miTabWest.triggered.connect(partial(self.graphTools.tabOrientation, 'West'))
        self.miTabEast.triggered.connect(partial(self.graphTools.tabOrientation, 'East'))
        self.miButtonIconOnly.triggered.connect(self.graphTools.toolsAspect)
        self.miButtonIconOnly.setShortcut("Ctrl+I")
        #-- Menu Help --#
        self.miPrintConnections.triggered.connect(self.on_printSelNodeConnections)

    @property
    def editMode(self):
        """
        Get edition mode state
        :return: Edition mode state
        :rtype: bool
        """
        return self.miEditMode.isChecked()

    @property
    def currentGraphZone(self):
        """
        Get grapher view from active graphTab
        :return: Active graphZone
        :rtype: QtGui.QGraphicsView
        """
        return self.tabGraph.widget(self.tabGraph.currentIndex())

    @property
    def currentGraphScene(self):
        """
        Get grapher scene from active graphTab
        :return: Active graphScene
        :rtype: QtGui.QGraphicsScene
        """
        return self.currentGraphZone.graphScene

    def on_loadProject(self):
        """
        Command launched when 'Load Project' QMenuItem is triggered
        Open new project dialog
        """
        self.fdNewProject = projectWgts.LoadProject(self)
        self.fdNewProject.exec_()

    def on_editProject(self):
        """
        Command launched when 'Edit Project' QMenuItem is triggered
        Open project settings dialog
        """
        if self.projectName is not None:
            self.fdEditProject = projectWgts.EditProject(self)
            self.fdEditProject.show()

    def on_saveGraphAs(self):
        """
        Command launched when 'Save Graph As' QMenuItem is triggered, Open fileDialog
        """
        self.fdSaveGraphAs = pQt.fileDialog(fdMode='save', fdFileMode='AnyFile', fdRoot=self.projectPath,
                                            fdCmd=self.saveGraphAs, fdFilters=['*.grp*'])
        self.fdSaveGraphAs.exec_()

    def on_addGraphZone(self):
        """
        Command launched when 'Add GraphZone' QMenuItem is triggered
        Add a new graphTab, initialize new graphWidget
        """
        newGraphScene = graphWgts.GraphScene(self)
        newGraphZone = graphWgts.GraphZone(self, newGraphScene)
        self.tabGraph.insertTab(-1, newGraphZone, 'Untitled')
        self.tabGraph.setAcceptDrops(True)

    def on_editMode(self):
        """
        Command launched when 'Edit Mode' QMenuItem is triggered.
        Turn on or off edition mode
        """
        groups = ['Node Id', 'Node Connections', 'Node Script']
        for grp in groups:
            widget = self.dataZone.getDataWidgetFromGroupName(grp)
            if widget is not None:
                widget.rf_editModeState()

    def on_connectNodes(self):
        """
        Command launched when 'Connect Nodes' QMenuItem is triggered
        Connect the two selected nodes
        """
        if len(self.currentGraphScene.selBuffer['_order']) == 2:
            startNode = self.currentGraphScene.selBuffer[self.currentGraphScene.selBuffer['_order'][0]]
            startItem = startNode.outputDataPlug
            endNode = self.currentGraphScene.selBuffer[self.currentGraphScene.selBuffer['_order'][1]]
            endItem = endNode.inputFilePlug
            self.currentGraphScene.createLine(startItem, endItem)

    def on_treeVisibility(self):
        """
        Command launched when 'Tree Visibility' QMenuItem is triggered
        Turn on or off tree visibility
        """
        self.qfProjectTree.setVisible(self.miTreeVisibility.isChecked())

    def on_dataVisibility(self):
        """
        Command launched when 'Data Visibility' QMenuItem is triggered
        Turn on or off data visibility
        """
        self.vfNodeData.setVisible(self.miDataVisibility.isChecked())

    def on_toolBarVisibility(self):
        """
        Command launched when 'ToolBar Visibility' QMenuItem is triggered
        Turn on or off tools bar visibility
        """
        self.tbTools.setVisible(self.miToolBarVisibility.isChecked())

    def on_fitInScene(self):
        """
        Command launched when 'Fit In Scene' QMenuItem is triggered
        Fit graphZone to graphScene
        """
        self.currentGraphZone.fitInView(self.currentGraphScene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)

    def on_fitInSelection(self):
        """
        Command launched when 'Fit In Selection' QMenuItem is triggered
        Fit graphZone to selected nodes
        """
        if len(self.currentGraphScene.selectedItems()) == 1:
            self.currentGraphZone.fitInView(self.currentGraphScene.selectedItems()[0], QtCore.Qt.KeepAspectRatio)
        if len(self.currentGraphScene.selectedItems()) > 1:
            self.currentGraphZone.fitInView(self.currentGraphScene.getSelectedNodesArea(), QtCore.Qt.KeepAspectRatio)

    def on_StyleOption(self, styleName='default'):
        """
        Command launched when 'Style' QMenuItem is triggered
        Change ui styleSheet
        """
        if styleName == 'default':
            self.setStyleSheet("")
        else:
            self.setStyleSheet(self.applyStyle(styleName=styleName))

    def on_toolBarOrientChanged(self, orient=False, force=False):
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
            self.miButtonIconOnly.setChecked(True)
        else:
            self.graphTools.tabOrientation('West')
            self.miButtonIconOnly.setChecked(False)
        self.graphTools.toolsAspect()

    def on_printSelNodeConnections(self):
        """
        Command launched when 'Print Connections' QMenuItem is triggered
        Print current graphScene connections info
        """
        selNodes = self.currentGraphScene.getSelectedNodes()
        print "\n", '#' * 60
        print "#========== CONNECTIONS INFO ==========#"
        for item in selNodes:
            print "#-- %s --#" % item.nodeName
            pprint(item.getConnectionsInfo())
        print '#' * 60, "\n"

    def loadProject(self, project):
        """
        Load given project
        :param project: Project full name
        :type: str
        """
        self.log.info("#===== Loading project %s =====#" % project)
        self.projectPath = os.path.join(self.grapherRootPath, 'projects', project)
        if not os.path.exists(self.projectPath):
            raise IOError, "!!! Project '%s' not found !!!" % project
        self.projectAlias = project.split('--')[0]
        self.projectName = project.split('--')[1]
        self.projectFullName = project
        self.setWindowTitle("Grapher | %s | %s" % (self.projectAlias, self.projectName))
        self.graphTree.rf_projectTree()

    def saveGraphAs(self):
        """
        Get fileDialog result, launch graph save
        """
        result = self.fdSaveGraphAs.selectedFiles()
        self.log.info("Save current graph as: %s" % result[0])
        self.currentGraphZone.saveGraphAs(result[0])

    def closeEvent(self, *args, **kwargs):
        """
        Clear graphZone to fix a bug when ui is closing
        """
        self.tabGraph.clear()


def launch(project=None, logLvl='info'):
    """
    Grapher launcher
    :param project: Grapher project
    :type project: str
    :param logLvl: Log level ('critical', 'error', 'warning', 'info', 'debug')
    :type logLvl: str
    """
    app = QtGui.QApplication(sys.argv)
    window = GrapherUi(project=project, logLvl=logLvl)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # launch(logLvl='debug')
    launch(project='a2--asterix2', logLvl='debug')
