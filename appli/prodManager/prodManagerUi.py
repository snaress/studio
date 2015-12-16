import sys
from lib.qt import procQt as pQt
from PyQt4 import QtGui, QtCore, Qt
from lib.system import procFile as pFile
from appli import prodManager as pmPack
from appli.prodManager import prodManager, pmSettings, pmTree, pmInfo
from appli.prodManager.ui import prodLoaderUI, prodManagerUI, newProjectUI


class ProdLoaderUi(QtGui.QMainWindow, prodLoaderUI.Ui_mwProdLoader):
    """ QMainWindow class launched when ProdManager QMainWindow is called
        :param logLvl: Print log level
        :type logLvl: str """

    def __init__(self, logLvl='info'):
        self.log = pFile.Logger(title="ProdLoader", level=logLvl)
        self.log.info("########## ProdManager Loader ##########", newLinesBefore=1)
        self.pm = prodManager.ProdManager(logLvl=logLvl)
        super(ProdLoaderUi, self).__init__()
        self._setupUi()
        self.rf_projects()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup main ui """
        self.setupUi(self)
        self.pbCreate.clicked.connect(self.on_newProject)
        for n in range(4):
            self.twProjects.header().setResizeMode(n, QtGui.QHeaderView.ResizeToContents)
        self.twProjects.sortItems(0, QtCore.Qt.AscendingOrder)
        self.twProjects.itemDoubleClicked.connect(self.on_loadProject)
        self.cbMovie.setStyleSheet(self.colorCode('Movie'))
        self.cbMovie.clicked.connect(self.rf_projects)
        self.cbMarketing.setStyleSheet(self.colorCode('Marketing'))
        self.cbMarketing.clicked.connect(self.rf_projects)
        self.cbSerie.setStyleSheet(self.colorCode('Serie'))
        self.cbSerie.clicked.connect(self.rf_projects)
        self.pbLoad.clicked.connect(self.on_loadProject)
        self.pbClose.clicked.connect(self.close)

    def rf_projects(self):
        """ Refresh 'All Projects' QTreeWidget """
        self.log.debug("#-- Refresh projects tree --#")
        self.twProjects.clear()
        projects = self.pm.project.getAllProjects()
        if projects is not None:
            items = []
            for project in projects.keys():
                if projects[project]['type'] == 'Movie' and self.cbMovie.isChecked():
                    newItem = self.newProjectItem(projects[project])
                    items.append(newItem)
                if projects[project]['type'] == 'Marketing' and self.cbMarketing.isChecked():
                    newItem = self.newProjectItem(projects[project])
                    items.append(newItem)
                if projects[project]['type'] == 'Serie' and self.cbSerie.isChecked():
                    newItem = self.newProjectItem(projects[project])
                    items.append(newItem)
            self.twProjects.addTopLevelItems(items)

    def on_newProject(self):
        """ Command launched when QPushButton 'Create New Project' is clicked """
        self.log.debug("#-- Create New Project --#")
        self.newProject = NewProjectUi(self, logLvl=self.log.level)
        self.newProject.exec_()

    def newProjectItem(self, projectDict):
        """ Create project QTreeWidgetItem
            :param projectDict: Project info
            :type projectDict: dict
            :return: Project item
            :rtype: QtGui.QTreeWidgetItem """
        #-- Edit Name --#
        newItem = QtGui.QTreeWidgetItem()
        newItem.setText(0, projectDict['alias'])
        newItem.setText(1, projectDict['name'])
        if projectDict['type'] == 'Marketing':
            newItem.setText(2, projectDict['season'])
        elif projectDict['type'] == 'Serie':
            newItem.setText(2, projectDict['season'])
            newItem.setText(3, projectDict['episode'])
        #-- Add Params --#
        for k in projectDict.keys():
            setattr(newItem, k, projectDict[k])
        #-- Edit Color --#
        for n in range(4):
            color = self.colorCode(projectDict['type'], colorMode='tuple')
            newItem.setTextColor(n, Qt.QColor(color[0], color[1], color[2]))
        return newItem

    def on_loadProject(self):
        """ Command launched when QPushButton 'Load' is clicked """
        selItems = self.twProjects.selectedItems()
        if selItems:
            self.pmUi = ProdManagerUi(prodId=selItems[0].alias, logLvl=self.log.level)
            self.pmUi.show()
            self.close()

    @staticmethod
    def colorCode(projectType, colorMode='styleSheet'):
        """ Get color code for given project type
            :param projectType: Project type ('Movie', 'Marketing', 'Serie')
            :type projectType: str
            :param colorMode: Color mode for return ('styleSheet' or 'tuple')
            :type colorMode: str
            :return: Style sheet string
            :rtype: str """
        if projectType == 'Movie':
            if colorMode == 'styleSheet':
                return "color: rgb(0, 125, 255)"
            elif colorMode == 'tuple':
                value = (0, 125, 255)
                return value
        elif projectType == 'Marketing':
            if colorMode == 'styleSheet':
                return "color: rgb(0, 180, 0)"
            elif colorMode == 'tuple':
                value = (0, 180, 0)
                return value
        elif projectType == 'Serie':
            if colorMode == 'styleSheet':
                return "color: rgb(150, 0, 150)"
            elif colorMode == 'tuple':
                value = (150, 0, 150)
                return value

    def closeEvent(self, *args, **kwargs):
        """ Command launched when QPushButton 'Close' is clicked, or dialog is closed """
        self.log.debug("Closing prodManager loader ui ...")


class NewProjectUi(QtGui.QDialog, newProjectUI.Ui_newProject):
    """ QDialog class used by 'ProdLoader' QMainWindow. Lanch new project dialog
        :param mainUi: ProdManager window
        :type mainUi: QtGui.QMainWindow
        :param logLvl: Print log level
        :type logLvl: str """

    def __init__(self, mainUi, logLvl='info'):
        self.log = pFile.Logger(title="PL-NewProject", level=logLvl)
        self.log.info("########## ProdManager New Project ##########", newLinesBefore=1)
        self.mainUi = mainUi
        self.pm = self.mainUi.pm
        super(NewProjectUi, self).__init__()
        self._setupUi()
        self._refresh()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup main ui """
        self.setupUi(self)
        self.cbProjectType.currentIndexChanged.connect(self._refresh)
        self.pbAccept.clicked.connect(self.accept)
        self.pbCancel.clicked.connect(self.close)

    def _refresh(self):
        """ Refresh ui project attr """
        pType = self.projectType
        self.log.debug("#-- Refresh Project Attributes --#")
        self.log.debug("Project Type: %s" % pType)
        if pType == 'Movie':
            self.lProjectSeason.setVisible(False)
            self.leProjectSeason.setVisible(False)
            self.lProjectEpisode.setVisible(False)
            self.leProjectEpisode.setVisible(False)
        elif pType == 'Marketing':
            self.lProjectSeason.setVisible(True)
            self.leProjectSeason.setVisible(True)
            self.lProjectEpisode.setVisible(False)
            self.leProjectEpisode.setVisible(False)
        elif pType == 'Serie':
            self.lProjectSeason.setVisible(True)
            self.leProjectSeason.setVisible(True)
            self.lProjectEpisode.setVisible(True)
            self.leProjectEpisode.setVisible(True)

    @property
    def projectType(self):
        """ Get current projectType
            :return: Project type
            :rtype: str """
        return str(self.cbProjectType.currentText())

    def getProjectParams(self):
        """ Get project params
            :return: Project params {'type', 'name', 'alias', 'season', 'episode'}
            :rtype: dict """
        #-- Check Project Name --#
        name = str(self.leProjectName.text())
        if name in ['', ' ']:
            name = None
        #-- Check Project Alias --#
        alias = str(self.leProjectAlias.text())
        if alias in ['', ' ']:
            alias =  None
        #-- Check Project Season --#
        season = str(self.leProjectSeason.text())
        if season in ['', ' ']:
            season = None
        #-- Check Project Episode --#
        episode = str(self.leProjectEpisode.text())
        if episode in ['', ' ']:
            episode = None
        #-- Result --#
        if alias is not None:
            return {'type': self.projectType, 'name': name, 'alias': alias,'season': season, 'episode': episode}

    def accept(self):
        """ Command launched when QPushButton 'Accept' is clicked """
        self.log.debug("#-- Create New Project --#")
        params = self.getProjectParams()
        if params is not None:
            if self.checkNewProject(params):
                self.pm.project.createNewProject(params)
                self.mainUi.rf_projects()
                self.close()

    def checkNewProject(self, params):
        """ Check if new project params are valide
            :param params: Project params
            :type params: dict
            :return: Check state, True if succes
            :rtype: bool """
        self.log.debug("Check New Project ...")
        allItems = pQt.getAllItems(self.mainUi.twProjects)
        #-- Check if new project already exists --#
        for item in allItems:
            if item.alias == params['alias']:
                self.log.error("Alias already exists !!! (%s) !!!" % params['alias'])
                return False
        return True

    def closeEvent(self, *args, **kwargs):
        """ Command launched when QPushButton 'Cancel' is clicked, or dialog is closed """
        self.log.debug("Closing new project ui ...")


class ProdManagerUi(QtGui.QMainWindow, prodManagerUI.Ui_mwProdManager):
    """ QMainWindow class launched when ProdManager mainUi is called
        :param prodId: Project alias
        :type prodId: str
        :param logLvl: Print log level
        :type logLvl: str """

    def __init__(self, prodId=None, logLvl='info'):
        self.log = pFile.Logger(title="ProdManagerUi", level=logLvl)
        self.pm = prodManager.ProdManager(prodId=prodId, logLvl=logLvl)
        self.log.info("########## ProdManager UI ##########", newLinesBefore=1)
        self.iconPath = pFile.conformPath(pmPack.iconPath)
        super(ProdManagerUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup main ui """
        self.setupUi(self)
        self._setWindowTitle()
        self.miProjectSettings.triggered.connect(self.on_projectSettings)
        self.wgMainTree = pmTree.MainTree(self, self.log.level)
        self.vlLeftUi.addWidget(self.wgMainTree)
        self.wgInfo = pmInfo.TabInfo(self, self.log.level)
        self.vlTabInfo.addWidget(self.wgInfo)

    def _setWindowTitle(self):
        """ Set window title """
        if self.pm.project.type == 'Movie':
            self.setWindowTitle("ProdManager: %s -- %s" % (self.pm.project.name, self.pm.project.alias))
        elif self.pm.project.type == 'Marketing':
            self.setWindowTitle("ProdManager: %s -- %s -- %s" % (self.pm.project.name, self.pm.project.season,
                                                                 self.pm.project.alias))
        if self.pm.project.type == 'Serie':
            self.setWindowTitle("ProdManager: %s -- %s -- %s -- %s" % (self.pm.project.name, self.pm.project.season,
                                                                       self.pm.project.episode, self.pm.project.alias))

    def on_projectSettings(self):
        """ Command launched when QMenuItem 'Project Settings' is clicked """
        self.ps = pmSettings.ProjectSettingsUi(self, logLvl=self.log.level)
        self.ps.show()


def launch(prodId=None, logLvl='info'):
    """ Grapher launcher
        :param prodId: Project alias
        :type prodId: str
        :param logLvl: Verbose log level ('critical', 'error', 'warning', 'info', 'debug')
        :type logLvl: str """
    app = QtGui.QApplication(sys.argv)
    if prodId is None:
        window = ProdLoaderUi(logLvl=logLvl)
    else:
        window = ProdManagerUi(prodId=prodId, logLvl=logLvl)
    window.show()
    # if prodId is not None:
    #     window.on_projectSettings()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # launch(logLvl='debug')
    launch(prodId='tdk', logLvl='debug')
