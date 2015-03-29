from PyQt4 import QtGui
from lib.system import procFile as pFile
from appli.prodManager.ui import tabInfoUI


class TabInfo(QtGui.QWidget, tabInfoUI.Ui_wgInfo):
    """ QWidget class used by 'ProdManager' QMainWindow.
        :param mainUi: ProdManager window
        :type mainUi: QtGui.QMainWindow
        :param logLvl: Print log level
        :type logLvl: str """

    def __init__(self, mainUi, logLvl='info'):
        self.log = pFile.Logger(title="TabInfoUi", level=logLvl)
        self.log.info("#-- Tab Info Ui --#")
        self.mainUi = mainUi
        self.pm = self.mainUi.pm
        super(TabInfo, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup main ui """
        self.setupUi(self)

