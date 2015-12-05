import sys, os
from PyQt4 import QtGui
from lib.system import procFile as pFile
from appli.fondationOld.core import fondation
from appli.fondationOld.gui.fondation import toolSettingsUi
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
        self.fondation = fondation.Fondation(logLvl=self.log.level)
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup QtGui Fondation Ui
        """
        self.log.detail("#===== Setup Fondation Ui =====#", newLinesBefor=1)
        self.setupUi(self)
        self.setWindowTitle("Fondation | %s" % self.fondation.__user__)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self._setupMenu()

    # noinspection PyUnresolvedReferences
    def _setupMenu(self):
        """
        Setup Fondation menu
        """
        self.log.detail("#-- Setup Menu --#")
        #-- Menu Pref --#
        self.log.detail("Menu Pref ...")
        self.mi_fondationSettings.triggered.connect(self.on_miFondationSettings)
        #-- Check UserGrp --#
        if not self.fondation.userGrps._user.userGroup in ['ADMIN', 'DEV']:
            self.mi_fondationSettings.setEnabled(False)

    @property
    def showToolTips(self):
        """
        Get 'Show ToolTips' state

        :return: ToolTips state
        :rtype: bool
        """
        return self.mi_showToolTips.isChecked()

    def on_miFondationSettings(self):
        """
        Command launched when 'Tool Settings' QMenuItem is triggered

        Launch Tool Settings Ui
        """
        self.toolSettingsUi = toolSettingsUi.ToolSettingsUi(self, logLvl=self.log.level)
        self.toolSettingsUi.show()


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

