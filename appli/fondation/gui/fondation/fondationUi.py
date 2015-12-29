import os, sys
from PyQt4 import QtGui
from lib.system import procFile as pFile
from appli.fondation.core import fondation
from appli.fondation.gui.fondation import toolSettingsUi
from appli.fondation.gui.fondation._ui import fondationUI


class FondationUi(QtGui.QMainWindow, fondationUI.Ui_mw_fondation):
    """
    FondationUi Class: Contains fondation mainUi

    :param logLvl : Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """

    log = pFile.Logger(title="FondationUi")
    iconPath = "%s/_lib/icon/png" % '/'.join(pFile.conformPath(os.path.dirname(__file__)).split('/')[:-1])

    def __init__(self, logLvl='info'):
        self.log.level = logLvl
        self.log.info("########## Launching Fondation Ui ##########", newLinesBefore=1)
        self.fondation = fondation.Fondation(logLvl=self.log.level)
        super(FondationUi, self).__init__()
        self.iconToolTip = QtGui.QIcon(os.path.join(self.iconPath, 'toolTip.png'))
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup QtGui Fondation Ui
        """
        self.log.detail("#===== Setup Fondation Ui =====#", newLinesBefore=1)
        self.setupUi(self)
        self.setWindowTitle("Fondation | %s" % self.fondation.__user__)
        self.setStyleSheet(self._styleSheet)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self._setupMenu()

    # noinspection PyUnresolvedReferences
    def _setupMenu(self):
        """
        Setup Fondation menu
        """
        self.log.detail("#-- Setup Menu --#")
        #-- Menu Settings --#
        self.log.detail("Menu Settings ...")
        self.mi_fondationSettings.triggered.connect(self.on_miFondationSettings)
        #-- Check UserGrp --#
        if not self.fondation.userGrps._user.grade <= 1:
            self.mi_fondationSettings.setEnabled(False)

    @property
    def _styleSheet(self):
        """
        Fondation Ui styleSheet

        :return: Style sheet
        :rtype: str
        """
        color_1 = "rgb(200, 200, 200)"
        bgColor_1 = "rgb(60, 60, 60)"
        bgColor_2 = "rgb(70, 70, 70)"
        style = ["QWidget {background-color: %s; alternate-background-color: %s; color: %s;}" % (bgColor_1, bgColor_2, color_1),
                 "QMenuBar::item {background-color: %s; color: %s;}" % (bgColor_1, color_1),
                 "QHeaderView::section {background-color: %s;}" % bgColor_1]
        return ''.join(style)

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
        self.toolSettingsUi = toolSettingsUi.ToolSettings(self, logLvl=self.log.level)
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
