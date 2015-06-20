import sys
from pprint import pprint
from functools import partial
from PyQt4 import QtGui, QtCore
from appli.grapher.gui import toolsWgts, dataWgts, graphWgts
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.grapher.gui.ui import grapherUI


class GrapherUi(QtGui.QMainWindow, grapherUI.Ui_mwGrapher, pQt.Style):
    """ Grapher appli main class
        :param logLvl: Log level ('critical', 'error', 'warning', 'info', 'debug')
        :type logLvl: str """

    def __init__(self, logLvl='info'):
        self.log = pFile.Logger(title="Grapher-UI", level=logLvl)
        self.log.info("#-- Launching Grapher Ui --#")
        super(GrapherUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup main ui """
        self.log.debug("---> Setup Main Ui ...")
        self.setupUi(self)
        #-- GraphZone --#
        self.on_addGraphZone()
        #-- DataZone --#
        self.dataZone = dataWgts.DataZone(self)
        #-- GraphTools --#
        self.graphTools = toolsWgts.ToolsBar(mainUi=self)
        self.tbTools.addWidget(self.graphTools)
        self.tbTools.orientationChanged.connect(partial(self.on_toolBarOrientChanged, orient=False, force=False))
        #-- GraphMenu --#
        self._setupMenu()
        self.on_toolBarVisibility()
        self.on_dataVisibility()

    # noinspection PyUnresolvedReferences
    def _setupMenu(self):
        """ Setup main ui menu """
        #-- Menu Edit --#
        self.miAddGraphZone.triggered.connect(self.on_addGraphZone)
        self.miAddGraphZone.setShortcut("Ctrl+N")
        self.miEditMode.triggered.connect(self.on_editMode)
        self.miEditMode.setShortcut("E")
        self.miConnectNodes.triggered.connect(self.on_connectNodes)
        self.miConnectNodes.setShortcut("C")
        #-- Menu Display --#
        self.miToolBarVisibility.triggered.connect(self.on_toolBarVisibility)
        self.miToolBarVisibility.setShortcut("T")
        self.miDataVisibility.triggered.connect(self.on_dataVisibility)
        self.miDataVisibility.setShortcut("D")
        self.miFitInView.triggered.connect(self.on_fitInView)
        self.miFitInView.setShortcut("F")
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
        #-- Menu Help --#
        self.miPrintConnections.triggered.connect(self.on_printSelNodeConnections)

    @property
    def currentGraphZone(self):
        """ Get grapher view from active graphTab
            :return: Active graphZone
            :rtype: QtGui.QGraphicsView """
        return self.tabGraph.widget(self.tabGraph.currentIndex())

    @property
    def currentGraphScene(self):
        """ Get grapher scene from active graphTab
            :return: Active graphScene
            :rtype: QtGui.QGraphicsScene """
        return self.currentGraphZone.graphScene

    def on_addGraphZone(self):
        """ Command launched when 'Add GraphZone' QMenuItem is triggered
            Add a new graphTab, initialize new graphWidget """
        newGraphScene = graphWgts.GraphScene(self)
        newGraphZone = graphWgts.GraphZone(self, newGraphScene)
        self.tabGraph.insertTab(-1, newGraphZone, 'Untitled')

    def on_editMode(self):
        """ Command launched when 'Edit Mode' QMenuItem is triggered.
            Turn on or off edition mode """
        self.currentGraphScene.rf_connections()

    def on_connectNodes(self):
        """ Command launched when 'Connect Nodes' QMenuItem is triggered
            Connect the two selected nodes """
        if len(self.currentGraphScene.selBuffer['_order']) == 2:
            startNode = self.currentGraphScene.selBuffer[self.currentGraphScene.selBuffer['_order'][0]]
            startItem = startNode.outputFileConnection
            endNode = self.currentGraphScene.selBuffer[self.currentGraphScene.selBuffer['_order'][1]]
            endItem = endNode.inputFileConnection
            self.currentGraphScene.createLine(startItem, endItem)

    def on_toolBarVisibility(self):
        """ Command launched when 'ToolBar Visibility' QMenuItem is triggered
            Turn on or off tools bar visibility """
        self.tbTools.setVisible(self.miToolBarVisibility.isChecked())

    def on_dataVisibility(self):
        """ Command launched when 'Data Visibility' QMenuItem is triggered
            Turn on or off data visibility """
        self.vfNodeData.setVisible(self.miDataVisibility.isChecked())

    def on_fitInView(self):
        """ Command launched when 'Fit In View' QMenuItem is triggered
            Fir graphZone to selected nods """
        graphZone = self.currentGraphZone
        graphScene = self.currentGraphScene
        x1, x2, y1, y2 = graphScene.getSelectedNodesArea()
        graphZone.fitInView(x1, y1, x2, y2, QtCore.Qt.KeepAspectRatio)

    def on_StyleOption(self, styleName='default'):
        """ Command launched when 'Style' QMenuItem is triggered
            Change ui styleSheet """
        if styleName == 'default':
            self.setStyleSheet("")
        else:
            self.setStyleSheet(self.applyStyle(styleName=styleName))

    def on_toolBarOrientChanged(self, orient=False, force=False):
        """ Orient toolsTab and their contents
            :param orient: 'horizontal' or 'vertical'
            :type orient: str
            :param force: Force orientation
            :type force: bool """
        if force:
            if orient == 'horizontal':
                self.tbTools.setOrientation(QtCore.Qt.Horizontal)
            elif orient == 'vertical':
                self.tbTools.setOrientation(QtCore.Qt.Vertical)
        if self.tbTools.orientation() == 1:
            self.graphTools.tabOrientation('North')
        else:
            self.graphTools.tabOrientation('West')

    def on_printSelNodeConnections(self):
        """ Command launched when 'Print Connections' QMenuItem is triggered
            Print current graphScene connections info """
        selNodes = self.currentGraphScene.getSelectedNodes()
        print "\n", '#' * 60
        print "#========== CONNECTIONS INFO ==========#"
        for item in selNodes:
            print "#-- %s --#" % item.nodeName
            pprint(item.getConnectionsInfo())
        print '#' * 60, "\n"

    def closeEvent(self, *args, **kwargs):
        """ Clear graphZone to fix a bug when ui is closing """
        self.tabGraph.clear()


def launch(logLvl='info'):
    """ Grapher launcher
        :param logLvl: Log level ('critical', 'error', 'warning', 'info', 'debug')
        :type logLvl: str """
    app = QtGui.QApplication(sys.argv)
    window = GrapherUi(logLvl=logLvl)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch(logLvl='debug')
