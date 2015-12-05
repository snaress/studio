import sys, os
from PyQt4 import QtGui
from lib.system import procFile as pFile
from appli.fondationOld.gui.fondation.ui import fondationUI


class FondationUi(QtGui.QMainWindow, fondationUI.Ui_mw_fondation):
    """
    FondationUi Class: Contains fondation mainUi

    :param logLvl : Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """

    log = pFile.Logger(title="FondationUi")
    iconPath = "%s/_icon/png" % '/'.join(pFile.conformPath(os.path.dirname(__file__)).split('/')[:-1])

    def __init__(self, logLvl='info'):
        self.log.level = logLvl
        self.log.info("########## Launching Fondation Ui ##########", newLinesBefor=1)
        super(FondationUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup QtGui Fondation Ui
        """
        self.log.detail("#===== Setup Fondation Ui =====#", newLinesBefor=1)
        self.setupUi(self)


def launch(logLvl='info'):
    """
    Fondation launcher

    :param logLvl: Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """
    app = QtGui.QApplication(sys.argv)
    window = FondationUi(logLvl=logLvl)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch(logLvl='detail')
