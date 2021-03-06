import os
import sys
from PyQt4 import QtGui
from functools import partial
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.foundation_old.core import foundation
from appli.foundation_old.gui.foundation._ui import foundationUI
from appli.foundation_old.gui.foundation import dialogsUi, projectTree


class FoundationUi(QtGui.QMainWindow, foundationUI.Ui_mw_foundation):
    """
    FoundationUi Class: Contains foundation mainUi

    :param logLvl : Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """

    log = pFile.Logger(title="FoundationUi")
    iconPath = "%s/_lib/icon/png" % pFile.conformPath('/'.join(os.path.dirname(__file__).split('/')[:-1]))

    def __init__(self, logLvl='info'):
        self.log.level = logLvl
        self.foundation = foundation.Foundation(logLvl=self.log.level)
        super(FoundationUi, self).__init__()
        self.log.info("########## Launching Foundation Ui ##########", newLinesBefore=1)
        self._setupUi()

    def _setupUi(self):
        """
        Setup main Ui
        """
        self.log.info("#===== Setup Foundation Ui =====#", newLinesBefore=1)
        self.setupUi(self)
        self._initMainUi()
        self._initWidgets()
        self._initMenu()

    def _initMainUi(self):
        """
        Init main ui window
        """
        self.setWindowTitle("Foundation | %s" % self.foundation.__user__)
        self.resize(1200, 800)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.setStyleSheet(self._styleSheet)
        self.qf_left.setVisible(False)
        self.qf_datasDn.setVisible(False)

    def _initWidgets(self):
        """
        Init main ui widgets
        """
        self.wg_projectTree = projectTree.ProjectTree(parent=self)
        self.vl_treeDn.addWidget(self.wg_projectTree)

    def _initMenu(self):
        """
        Init main ui menus
        """
        #-- Menu Project --#
        self.mi_newProject.setShortcut("Ctrl+Shift+N")
        self.mi_newProject.triggered.connect(self.on_miNewProject)
        self.mi_loadProject.setShortcut("Ctrl+Shift+L")
        self.mi_loadProject.triggered.connect(self.on_miLoadProject)
        self.mi_projectSettings.setShortcut("Ctrl+Shift+S")
        self.mi_projectSettings.triggered.connect(self.on_miProjectSettings)
        #-- Menu Help --#
        for level in self.log.levels:
            menuItem = self.m_logLevel.addAction(level)
            menuItem.setCheckable(True)
            menuItem.triggered.connect(partial(self.on_miLogLevel, level))
        self.on_miLogLevel(self.log.level)

    @property
    def _styleSheet(self):
        """
        Foundation Ui styleSheet

        :return: Style sheet
        :rtype: str
        """
        #-- Attributes --#
        col = "color"
        bgCol = "background-color"
        aBgCol = "alternate-background-color"
        #-- Values --#
        color_1 = "rgb(200, 200, 200)"
        bgColor_1 = "rgb(50, 50, 50)"
        bgColor_2 = "rgb(40, 40, 40)"
        bgColor_3 = "rgb(65, 65, 65)"
        #-- Style Sheet --#
        style = ["QWidget {%s: %s; %s: %s; %s: %s;}" % (bgCol, bgColor_1, aBgCol, bgColor_2, col, color_1),
                 "QPushButton:hover, QLineEdit:hover, QTabBar::tab:hover {%s: %s}" % (bgCol, bgColor_3),
                 "QMenuBar::item {%s: %s; %s: %s;}" % (bgCol, bgColor_1, col, color_1),
                 "QMenuBar::item:selected, QMenu::item:selected {%s: %s}" % (bgCol, bgColor_3),
                 "QHeaderView::section {%s: %s;}" % (bgCol, bgColor_1),
                 "QProgressBar {border: %s;}" % bgColor_1,
                 "QLineEdit {%s: %s}" % (bgCol, bgColor_2),
                 "QTabBar::tab {%s: %s;}" % (bgCol, bgColor_2),
                 "QTabBar::tab:selected {%s: %s;}" % (bgCol, bgColor_1)]
        #-- Result --#
        return ''.join(style)

    @property
    def showToolTips(self):
        """
        Get 'Tool Tips' menuItem status

        :return: 'Tool Tips' status
        :rtype: bool
        """
        return self.mi_toolTips.isChecked()

    def loadProject(self, project=None):
        """
        Load given project. If project is None, load current core project

        :param project: Project (name--code)
        :type project: str
        """
        if project is not None:
            self.foundation.project.loadProject(project)
        self.setWindowTitle("Foundation | %s | %s" % (self.foundation.project.project, self.foundation.__user__))
        self.qf_left.setVisible(True)
        self.wg_projectTree.buildTree()

    def on_miNewProject(self):
        """
        Command launched when 'New Project' QMenuItem is triggered

        Launch NewProject dialog
        """
        self.log.detail(">>> Launch 'New Project' ...")
        #-- Check User Grade --#
        if not self.foundation.userGroups._user.grade <= 2:
            mess = "Your grade does not allow you to create new project !"
            self.log.error(mess)
            pQt.errorDialog(mess, self)
            raise UserWarning(mess)
        #-- Launch Dialog --#
        self.dial_newProject = dialogsUi.NewProject(parent=self)
        self.dial_newProject.exec_()

    def on_miLoadProject(self):
        """
        Command launched when 'Load Project' QMenuItem is triggered

        Launch LoadProject dialog
        """
        self.log.detail(">>> Launch 'Load Project' ...")
        self.dial_loadProject = dialogsUi.LoadProject(parent=self)
        self.dial_loadProject.exec_()

    def on_miProjectSettings(self):
        """
        Command launched when 'Project Settings' QMenuItem is triggered

        Launch ProjectSettings dialog
        """
        self.log.detail(">>> Launch 'Project Settings' ...")
        #-- Check User Grade --#
        if not self.foundation.userGroups._user.grade <= 3:
            mess = "Your grade does not allow you to edit project settings !"
            self.log.error(mess)
            pQt.errorDialog(mess, self)
            raise UserWarning(mess)
        #-- Check Project --#
        if self.foundation.project.project is None:
            mess = "!!! No project loaded. Load project to edit its settings !!!"
            pQt.errorDialog(mess, self)
            raise IOError(mess)
        #-- Launch Dialog --#
        self.dial_projectSettings = dialogsUi.ProjectSettings(parent=self)
        self.dial_projectSettings.exec_()

    def on_miLogLevel(self, logLevel):
        """
        Command launched when 'Log Level' QMenuItem is triggered

        Set ui and core log level
        :param logLevel : Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
        :type logLevel: str
        """
        self.log.detail(">>> Launch 'Log Level': %s ..." % logLevel)
        #-- Uncheck All --#
        for menuItem in self.m_logLevel.children():
            menuItem.setChecked(False)
        #-- Check Given LogLvl --#
        for menuItem in self.m_logLevel.children():
            if str(menuItem.text()) == logLevel:
                menuItem.setChecked(True)
                break
        #-- Set Log Level --#
        self.log.level = logLevel
        self.foundation.log.level = logLevel


def launch(logLvl='info'):
    """
    Foundation launcher

    :param logLvl: Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """
    app = QtGui.QApplication(sys.argv)
    window = FoundationUi(logLvl=logLvl)
    window.show()
    window.loadProject('animTest--AT')
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch(logLvl='detail')
