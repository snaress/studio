import os
from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.foundation.gui.foundation._ui import dial_newProjectUI, dial_loadProjectUI


class NewProject(QtGui.QDialog, dial_newProjectUI.Ui_dial_newProject):
    """
    NewProject Dialog: Project creation, child of Foundation

    :param parent: Parent Ui
    :type parent: Foundation
    """

    def __init__(self, parent=None):
        super(NewProject, self).__init__(parent)
        self.log = parent.log
        self.foundation = parent.foundation
        self.iconSave = QtGui.QIcon(pFile.conformPath(os.path.join(parent.iconPath, 'apply.png')))
        self.iconCancel = QtGui.QIcon(pFile.conformPath(os.path.join(parent.iconPath, 'cancel.png')))
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
        self.foundation.project.createNewProject(projectName, projectCode)
        self.close()


class LoadProject(QtGui.QDialog, dial_loadProjectUI.Ui_Dialog):
    """
    LoadProject Dialog: Project load, child of Foundation

    :param parent: Parent Ui
    :type parent: Foundation
    """

    def __init__(self, parent=None):
        super(LoadProject, self).__init__(parent)
        self.log = parent.log
        self.foundation = parent.foundation
        self.iconStore = QtGui.QIcon(pFile.conformPath(os.path.join(parent.iconPath, 'pinGreen.png')))
        self.iconRemove = QtGui.QIcon(pFile.conformPath(os.path.join(parent.iconPath, 'del.png')))
        self.iconRefresh = QtGui.QIcon(pFile.conformPath(os.path.join(parent.iconPath, 'refresh.png')))
        self.iconLoad = QtGui.QIcon(pFile.conformPath(os.path.join(parent.iconPath, 'apply.png')))
        self.iconCancel = QtGui.QIcon(pFile.conformPath(os.path.join(parent.iconPath, 'cancel.png')))
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
            projects = self.foundation.project.projects
            treeWidget = self.tw_allProjects
        else:
            self.log.detail("Build 'My Projects' tree ...")
            projects = self.foundation.userGroups._user.userPinedProjects
            treeWidget = self.tw_myProjects
        #-- Populate Tree --#
        treeWidget.clear()
        for project in projects:
            newItem = self.new_projectItem(project, treeWidget)
            treeWidget.addTopLevelItem(newItem)
        #-- Refresh --#
        self.rf_treeColumns(treeWidget)
        treeWidget.sortItems(0, QtCore.Qt.AscendingOrder)

    @staticmethod
    def new_projectItem(project, twTree):
        """
        Create new project item

        :param project: Project (name--code)
        :type project: str
        :param twTree: Tree to refresh
        :type twTree: QtGui.QTreeWidget
        :return: Project tree item
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = QtGui.QTreeWidgetItem()
        newItem.projectName = project.split('--')[0]
        newItem.projectCode = project.split('--')[1]
        newItem.project = project
        newItem.setText(0, newItem.projectName)
        newItem.setText(1, newItem.projectCode)
        for n in range(twTree.columnCount()):
            newItem.setTextAlignment(n, 5)
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
            self.foundation.userGroups._user.addPinedProject(selItems[0].project)
            self.foundation.userGroups._user.writeFile()
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
            self.foundation.userGroups._user.delPinedProject(selItems[0].project)
            self.foundation.userGroups._user.writeFile()
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
            self.foundation.project.loadProject(selItems[0].project)
            self.close()
