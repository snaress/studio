import sys
from functools import partial
from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.grapher.ui import grapherUI
from appli.grapher import graphWgts as gpWgts
from appli.grapher import toolsWgts as tlWgts


class GrapherUi(QtGui.QMainWindow, grapherUI.Ui_mwGrapher, pQt.Style):

    def __init__(self, logLvl='info'):
        self.log = pFile.Logger(title="Grapher-UI", level=logLvl)
        self.log.info("#-- Launching Grapher Ui --#")
        super(GrapherUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        self.log.debug("---> Setup Main Ui ...")
        self.setupUi(self)
        #-- GraphZone --#
        self.on_addGraphZone()
        #-- GraphTools --#
        self.graphTools = tlWgts.ToolsBar(mainUi=self)
        self.tbTools.addWidget(self.graphTools)
        self.tbTools.orientationChanged.connect(partial(self.toolBarOrientChanged, orient=False, force=False))
        #-- GraphMenu --#
        self._setupMenu()

    # noinspection PyUnresolvedReferences
    def _setupMenu(self):
        #-- Menu Edit --#
        self.miAddGraphZone.triggered.connect(self.on_addGraphZone)
        self.miAddGraphZone.setShortcut("Ctrl+N")
        self.miConnectNodes.triggered.connect(self.on_connectNodes)
        self.miConnectNodes.setShortcut("C")
        #-- Menu Pref --#
        self.miDefaultStyle.triggered.connect(partial(self.on_StyleOption, styleName='default'))
        self.miDarkOrange.triggered.connect(partial(self.on_StyleOption, styleName='darkOrange'))
        self.miDarkGrey.triggered.connect(partial(self.on_StyleOption, styleName='darkGrey'))
        self.miRedGrey.triggered.connect(partial(self.on_StyleOption, styleName='redGrey'))
        self.miHorizontal.triggered.connect(partial(self.toolBarOrientChanged, orient='horizontal', force=True))
        self.miVertical.triggered.connect(partial(self.toolBarOrientChanged, orient='vertical', force=True))
        self.miNorth.triggered.connect(partial(self.graphTools.tabOrientation, 'North'))
        self.miSouth.triggered.connect(partial(self.graphTools.tabOrientation, 'South'))
        self.miWest.triggered.connect(partial(self.graphTools.tabOrientation, 'West'))
        self.miEast.triggered.connect(partial(self.graphTools.tabOrientation, 'East'))

    @property
    def currentGraphZone(self):
        return self.tabGraph.widget(self.tabGraph.currentIndex())

    @property
    def currentGraphScene(self):
        return self.currentGraphZone.graphScene

    def on_addGraphZone(self):
        newGraphScene = gpWgts.GraphScene(self)
        newGraphZone = gpWgts.GraphZone(self, newGraphScene)
        self.tabGraph.insertTab(-1, newGraphZone, 'Untitled')

    def on_connectNodes(self):
        if len(self.currentGraphScene.selBuffer['_order']) == 2:
            startNode = self.currentGraphScene.selBuffer[self.currentGraphScene.selBuffer['_order'][0]]
            startItem = startNode.outConnectionNode
            endNode = self.currentGraphScene.selBuffer[self.currentGraphScene.selBuffer['_order'][1]]
            endItem = endNode.inConnectionNode
            connectionLine = gpWgts.LineConnection(startItem, endItem)
            self.currentGraphScene.addItem(connectionLine)

    def on_StyleOption(self, styleName='default'):
        if styleName == 'default':
            self.setStyleSheet("")
        else:
            self.setStyleSheet(self.applyStyle(styleName=styleName))

    def toolBarOrientChanged(self, orient=False, force=False):
        if force:
            if orient == 'horizontal':
                self.tbTools.setOrientation(QtCore.Qt.Horizontal)
            elif orient == 'vertical':
                self.tbTools.setOrientation(QtCore.Qt.Vertical)
        if self.tbTools.orientation() == 1:
            self.graphTools.tabOrientation('North')
        else:
            self.graphTools.tabOrientation('West')

    def closeEvent(self, *args, **kwargs):
        self.tabGraph.clear()


def launch(logLvl='info'):
    """ Grapher launcher
        :param logLvl: (str) : Log level ('critical', 'error', 'warning', 'info', 'debug') """
    app = QtGui.QApplication(sys.argv)
    window = GrapherUi(logLvl=logLvl)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch(logLvl='debug')