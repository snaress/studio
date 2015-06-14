import sys
from functools import partial
from PyQt4 import QtGui, QtCore
from appli import grapher2
from lib.system import procFile as pFile
from appli.grapher2.ui import grapherUI
from appli.grapher2 import graphWgts as gpWgts
from appli.grapher2 import toolsWgts as tlWgts


class GrapherUi(QtGui.QMainWindow, grapherUI.Ui_mwGrapher):

    def __init__(self, logLvl='info'):
        self.log = pFile.Logger(title="Grapher-UI", level=logLvl)
        self.log.info("#-- Launching Grapher Ui --#")
        self.iconPath = grapher2.iconPath
        super(GrapherUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        self.setupUi(self)
        #-- GraphZone --#
        self.graphScene = gpWgts.GraphScene(self)
        self.gvGraphZone.setScene(self.graphScene)
        self.gvGraphZone.setSceneRect(0, 0, 1000, 1000)
        self.gvGraphZone.wheelEvent = self.graphZoneWheelEvent
        self.gvGraphZone.resizeEvent = self.graphZoneResizeEvent
        self.gvGraphZone.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(60, 60, 60, 255), QtCore.Qt.SolidPattern))
        #-- GraphTools --#
        self.graphTools = tlWgts.ToolsBar(mainUi=self)
        self.tbTools.addWidget(self.graphTools)
        self.tbTools.orientationChanged.connect(self.toolBarOrientChanged)
        #-- GraphMenu --#
        self._setupMenu()

    # noinspection PyUnresolvedReferences
    def _setupMenu(self):
        #-- Menu Edit --#
        self.miConnectNodes.triggered.connect(self.graphScene.connectNodes)
        self.miConnectNodes.setShortcut("C")
        #-- Menu Window --#
        self.miNorth.triggered.connect(partial(self.graphTools.tabOrientation, 'North'))
        self.miSouth.triggered.connect(partial(self.graphTools.tabOrientation, 'South'))
        self.miWest.triggered.connect(partial(self.graphTools.tabOrientation, 'West'))
        self.miEast.triggered.connect(partial(self.graphTools.tabOrientation, 'East'))

    def graphZoneWheelEvent(self, event):
        factor = 1.41 ** ((event.delta()*.5) / 240.0)
        self.gvGraphZone.scale(factor, factor)

    def graphZoneResizeEvent(self, event):
        self.graphScene.setSceneRect(0, 0, self.gvGraphZone.width(), self.gvGraphZone.height())

    def toolBarOrientChanged(self):
        if self.tbTools.orientation() == 1:
            self.graphTools.tabOrientation('North')
        else:
            self.graphTools.tabOrientation('West')

    def closeEvent(self, *args, **kwargs):
        self.graphScene.clear()


def launch(logLvl='info'):
    """ Grapher launcher
        :param logLvl: (str) : Log level ('critical', 'error', 'warning', 'info', 'debug') """
    app = QtGui.QApplication(sys.argv)
    window = GrapherUi(logLvl=logLvl)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch(logLvl='debug')