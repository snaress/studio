import sys
from PyQt4 import QtGui
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.grapher import gpWidget
from appli.grapher.ui import grapherUI


class GrapherUi(QtGui.QMainWindow, grapherUI.Ui_mwGrapher, pQt.Style):

    def __init__(self, logLvl='info'):
        self.log = pFile.Logger(title="Grapher-UI", level=logLvl)
        self.log.info("#-- Launching Grapher --#")
        super(GrapherUi, self).__init__()
        self._setupUi()
        self._initUi()

    def _setupUi(self):
        """ Setup main ui """
        self.log.debug("#-- Setup Grapher Ui --#")
        self.setupUi(self)
        self.setStyleSheet(self.applyStyle(styleName='darkOrange'))
        self.wgComment = gpWidget.Comment(self)
        self.vlComment.addWidget(self.wgComment)
        self.wgVariables = gpWidget.Variables(self)
        self.vlVariables.addWidget(self.wgVariables)

    def _initUi(self):
        """ Initialized main ui """
        self.log.debug("#-- Init Grapher Ui --#")
        self.wgComment.rf_widgetVis()
        self.wgVariables.rf_widgetVis()



def launch(logLvl='info'):
    """ Grapher launcher
        :param logLvl: (str) : Log level ('critical', 'error', 'warning', 'info', 'debug') """
    app = QtGui.QApplication(sys.argv)
    window = GrapherUi(logLvl=logLvl)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch(logLvl='debug')