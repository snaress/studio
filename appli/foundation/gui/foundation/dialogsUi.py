import os
from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.foundation.gui.common import dialogsUi
from appli.foundation.gui.foundation import settingsUserGrps
from appli.foundation.gui.foundation._ui import newProjectUI, loadProjectUI


class NewProject(QtGui.QDialog, newProjectUI.Ui_dial_newProject):
    """
    NewProject Dialog: Project creation, child of FoundationUi

    :param mainUi: Parent Ui
    :type mainUi: Foundation
    """

    def __init__(self, mainUi):
        super(NewProject, self).__init__(mainUi)
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.foundation = self.fdn = self.mainUi.foundation
        self.project = self.fdn.project
        self.iconSave = QtGui.QIcon(pFile.conformPath(os.path.join(self.mainUi.iconPath, 'apply.png')))
        self.iconCancel = QtGui.QIcon(pFile.conformPath(os.path.join(self.mainUi.iconPath, 'cancel.png')))
        self._setupDial()

    def _setupDial(self):
        """
        Setup NewProject dialog
        """
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        #-- Icons --#
        self.pb_save.setIcon(self.iconSave)
        self.pb_cancel.setIcon(self.iconCancel)
        #-- Connect --#
        self.pb_save.clicked.connect(self.on_save)
        self.pb_cancel.clicked.connect(self.close)

    def on_save(self):
        """
        Command launched when 'Save' QPushButton is clicked

        Create New Project
        """
        self.log.detail(">>> Save New Project Dialog")
        projectName = str(self.le_projectName.text())
        projectCode = str(self.le_projectCode.text())
        #-- Check Values --#
        exclusions = ['', ' ', 'None', None]
        if projectName in exclusions or projectCode in exclusions:
            mess = "Project Name or Project Code invalide: %s--%s" % (projectName, projectCode)
            pQt.errorDialog(mess, self)
            raise AttributeError(mess)
        #-- Create Project --#
        self.project.createNewProject(projectName, projectCode)
        self.close()


class LoadProject(QtGui.QDialog, loadProjectUI.Ui_Dialog):
    """
    LoadProject Dialog: Project load, child of FoundationUi

    :param mainUi: Parent Ui
    :type mainUi: Foundation
    """

    def __init__(self, mainUi):
        super(LoadProject, self).__init__(mainUi)
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.foundation = self.fdn = self.mainUi.foundation
        self.users = self.fdn.users
        self.userGrps = self.fdn.userGrps
        self.project = self.fdn.project
        self.iconStore = QtGui.QIcon(pFile.conformPath(os.path.join(self.mainUi.iconPath, 'pinGreen.png')))
        self.iconRemove = QtGui.QIcon(pFile.conformPath(os.path.join(self.mainUi.iconPath, 'del.png')))
        self.iconRefresh = QtGui.QIcon(pFile.conformPath(os.path.join(self.mainUi.iconPath, 'refresh.png')))
        self.iconLoad = QtGui.QIcon(pFile.conformPath(os.path.join(self.mainUi.iconPath, 'apply.png')))
        self.iconCancel = QtGui.QIcon(pFile.conformPath(os.path.join(self.mainUi.iconPath, 'cancel.png')))
        self._setupDial()

    def _setupDial(self):
        """
        Setup LoadProject dialog
        """
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.tw_allProjects.setHeaderHidden(False)
        self.tw_myProjects.setHeaderHidden(False)
        #-- Icons --#
        self.pb_store.setIcon(self.iconStore)
        self.pb_remove.setIcon(self.iconRemove)
        self.pb_refresh.setIcon(self.iconRefresh)
        self.pb_load.setIcon(self.iconLoad)
        self.pb_cancel.setIcon(self.iconCancel)
        #-- Connect --#
        self.pb_store.clicked.connect(self.on_storeProject)
        self.pb_remove.clicked.connect(self.on_removeProject)
        self.pb_refresh.clicked.connect(self.on_refresh)
        self.pb_load.clicked.connect(self.on_load)
        self.pb_cancel.clicked.connect(self.close)
        #-- Refresh --#
        self.rf_projectTree('allProjects')
        self.rf_projectTree('myProjects')

    @property
    def getPinedProjects(self):
        """
        Get pined projects from 'My Prijects' tree

        :return: Pined projects
        :rtype: list
        """
        projects = []
        for item in pQt.getAllItems(self.tw_myProjects) or []:
            projects.append(item.project)
        return projects

    @staticmethod
    def rf_treeColumns(twTree):
        """
        Refresh tree column size

        :param twTree: Tree to refresh
        :type twTree: QtGui.QTreeWidget
        """
        for n in range(twTree.columnCount()):
            twTree.resizeColumnToContents(n)

    def rf_projectTree(self, treeName):
        """
        Refresh 'All Projects' tree

        :param treeName: Tree widget name ('allProjects' or 'myProjects')
        :type treeName: str
        """
        #-- Get Projects --#
        if treeName == 'allProjects':
            self.log.detail("Build 'All Projects' tree ...")
            projects = self.project.projects
            treeWidget = self.tw_allProjects
        else:
            self.log.detail("Build 'My Projects' tree ...")
            projects = self.users._user.userPinedProjects
            treeWidget = self.tw_myProjects
        #-- Populate Tree --#
        treeWidget.clear()
        for project in projects:
            projectFile = pFile.conformPath(os.path.join(self.fdn.__projectsPath__, project, '%s.py' % project))
            data = pFile.readDictFile(projectFile)
            newItem = self.new_projectItem(project, data, treeWidget)
            treeWidget.addTopLevelItem(newItem)
        #-- Refresh --#
        self.rf_treeColumns(treeWidget)
        treeWidget.sortItems(0, QtCore.Qt.AscendingOrder)

    def new_projectItem(self, project, data, twTree):
        """
        Create new project item

        :param project: Project (name--code)
        :type project: str
        :param data: Project Datas
        :type data: dict
        :param twTree: Tree to refresh
        :type twTree: QtGui.QTreeWidget
        :return: Project tree item
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = QtGui.QTreeWidgetItem()
        newItem.projectName = project.split('--')[0]
        newItem.projectCode = project.split('--')[1]
        newItem.projectDatas = data
        newItem.project = project
        newItem.setText(0, newItem.projectName)
        newItem.setText(1, newItem.projectCode)
        #-- Font --#
        newFont = QtGui.QFont()
        newFont.setItalic(True)
        for n in range(twTree.columnCount()):
            newItem.setTextAlignment(n, 5)
            if not self.users._user.userName in data['projectUsers']:
                newItem.setFont(n, newFont)
                newItem.setTextColor(n, QtGui.QColor(125, 125, 125))
        return newItem

    def on_storeProject(self):
        """
        Command launched when 'Store Project' QPushButton is clicked

        Store project in 'My Projects'
        """
        self.log.detail(">>> Launch 'Store Project' ...")
        selItems = self.tw_allProjects.selectedItems() or []
        if selItems:
            #-- Check Project --#
            if selItems[0].project in self.getPinedProjects:
                mess = "!!! Project %r already in pinedProjects, Skipp !!!" % selItems[0].project
                pQt.errorDialog(mess, self)
                raise ValueError(mess)
            #-- Add Poject --#
            self.users._user.addPinedProject(selItems[0].project)
            self.users._user.writeFile()
        #-- Refresh --#
        self.rf_projectTree('myProjects')

    def on_removeProject(self):
        """
        Command launched when 'Remove Project' QPushButton is clicked

        Remove project from 'My Projects'
        """
        self.log.detail(">>> Launch 'remove Project' ...")
        selItems = self.tw_myProjects.selectedItems() or []
        if selItems:
            #-- Check Project --#
            if selItems[0].project not in self.getPinedProjects:
                mess = "!!! Project %r not found, Skipp !!!" % selItems[0].project
                pQt.errorDialog(mess, self)
                raise ValueError(mess)
            #-- Remove Poject --#
            self.users._user.delPinedProject(selItems[0].project)
            self.users._user.writeFile()
        #-- Refresh --#
        self.rf_projectTree('myProjects')

    def on_refresh(self):
        """
        Command launched when 'Refresh' QPushButton is clicked

        Refresh project list
        """
        self.log.detail(">>> Launch 'Refresh' ...")
        self.rf_projectTree('myProjects')

    def on_load(self):
        """
        Command launched when 'Load' QPushButton is clicked

        Load selected project
        """
        self.log.detail(">>> Launch 'Load Project' ...")
        #-- Get Selected Project --#
        if self.tabWidget.currentIndex() == 0:
            selItems = self.tw_allProjects.selectedItems() or []
        else:
            selItems = self.tw_myProjects.selectedItems() or []
        #-- Load Project --#
        if selItems:
            userName = self.users._user.userName
            if not userName in selItems[0].projectDatas['projectUsers']:
                mess = "User %r is not set as projectUser in %s !" % (userName, selItems[0].project)
                pQt.errorDialog(mess, self)
                raise ValueError(mess)
            self.mainUi.loadProject(project=selItems[0].project)
            self.close()


class ToolSettings(dialogsUi.ToolSettings):
    """
    ToolSettings Dialog: Contains Foundation tool settings, child of FoundationUi

    :param parent: Parent Ui
    :type parent: FoundationUi
    """

    def __init__(self, parent=None):
        self.log = parent.log
        self.log.title = 'ToolSettingsUi'
        self.foundation = self.fdn = parent.foundation
        self.userGrps = self.fdn.userGrps
        self.users = self.fdn.users
        super(ToolSettings, self).__init__(parent)

    def _initSettings(self):
        """
        Init Foundation settings
        """
        super(ToolSettings, self)._initSettings()
        self.users.collecteUsers(userName=self.fdn.__user__)

    def _initWidgets(self):
        """
        Init tool widgets
        """
        super(ToolSettings, self)._initWidgets()
        #-- UserGroups --#
        self.wg_groups = settingsUserGrps.Groups(self)
        self.wg_users = settingsUserGrps.Users(self)
        #-- Refresh --#
        for widget in [self.wg_groups, self.wg_users]:
            widget.setVisible(False)
            self.vl_settingsWidget.addWidget(widget)

    @property
    def category(self):
        """
        Get settings category

        :return: Category datas
        :rtype: dict
        """
        return {0: self.userGrpsCategory}

    @property
    def userGrpsCategory(self):
        """
        Get UserGroups category

        :return: UserGroups category
        :rtype: dict
        """
        return {'userGroups': {'code': 'userGroups',
                               'label': 'User Groups',
                               'subCat': {0: {'groups': {'widget': self.wg_groups,
                                                         'code': 'groups',
                                                         'label': 'Groups'}},
                                          1: {'users': {'widget': self.wg_users,
                                                        'code': 'users',
                                                        'label': 'Users'}}}}}
