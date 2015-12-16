import sys
from PyQt4 import QtGui, QtCore
from lib.system import procFile as pFile
from appli.foundation.core import foundation
from appli.foundation.gui.foundation._ui import foundationUI


class FoundationUi(QtGui.QMainWindow, foundationUI.Ui_mw_foundation):

    log = pFile.Logger(title="FoundationUI")

    def __init__(self, logLvl='info'):
        self.log.level = logLvl
        self.foundation = self.fdtn = foundation.Foundation(logLvl=logLvl)
        self.log.info("########## Launching Foundation UI ##########", newLinesBefore=1)
        super(FoundationUi, self).__init__()
        self._setupUi()

    def _setupUi(self):
        """
        Setup Foundation UI
        """
        self.log.debug("#===== Setup Foundation Ui =====#", newLinesBefore=1)
        self.setupUi(self)
        self.showMaximized()
        self.scene = GraphScene(self)
        self.view = GraphView(self, self.scene)
        self.gridLayout.addWidget(self.view)


class GraphView(QtGui.QGraphicsView):

    def __init__(self, mainUi, scene):
        super(GraphView, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.setScene(scene)
        self._setupWidget()

    def _setupWidget(self):
        self.setSceneRect(0, 0, 10000, 10000)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(0, 0, 0, 255), QtCore.Qt.SolidPattern))


class GraphScene(QtGui.QGraphicsScene):

    def __init__(self, mainUi):
        super(GraphScene, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log


def launch(logLvl='info'):
    """
    Fondation launcher

    :param logLvl: Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """
    app = QtGui.QApplication(sys.argv)
    window = FoundationUi(logLvl=logLvl)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch()