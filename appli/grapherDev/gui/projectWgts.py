import os
from PyQt4 import QtGui
from functools import partial
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.grapherDev.core import grapher as gpCore
from appli.grapherDev.gui.ui import wgProjectLoadUI, wgProjectEditUI, wgTreeItemUI


class LoadProject(QtGui.QDialog, wgProjectLoadUI.Ui_wgLoadProject):
    """
    Load project dialog
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.info("Launching project load ui ...")
        self.grapherProjectsPath = pFile.conformPath(os.path.join(self.mainUi.grapherRootPath, 'projects'))
        super(LoadProject, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup dialog ui
        """
        self.setupUi(self)
        self.cbNewProject.clicked.connect(self.rf_newProjectVisibility)
        self.pbCreate.clicked.connect(self.on_createProject)
        self.pbCancel.clicked.connect(self.on_cancel)
        self.twProjects.itemDoubleClicked.connect(self.on_loadProject)
        self.rf_newProjectVisibility()
        self.rf_projectTree()

    @property
    def selectedProjectItem(self):
        """
        Get selected project tree item
        :return: Selected project item
        :rtype: QtGui.QTreeWidgetItem
        """
        selItems = self.twProjects.selectedItems()
        if selItems:
            return selItems[0]

    def rf_newProjectVisibility(self):
        """
        Refresh new project widget visibility
        """
        self.qfNewProject.setVisible(self.cbNewProject.isChecked())

    def rf_projectTree(self):
        """
        Refresh project tree
        """
        self.twProjects.clear()
        items = []
        for project in gpCore.getGrapherProjects(self.grapherProjectsPath):
            newItem = self.new_ProjectItem(project)
            items.append(newItem)
        self.twProjects.addTopLevelItems(items)

    def on_createProject(self):
        """
        Command launched when 'Create' QPushButton is clicked
        Will create new project
        """
        pName = str(self.leProjectName.text())
        pAlias = str(self.leProjectAlias.text())
        pFolder = "%s--%s" % (pAlias, pName)
        self.log.info("Creating new project: '%s' ..." % pFolder)
        gpCore.createProjectFolder(self.grapherProjectsPath, self.mainUi.prodsRootPath, pAlias, pName)
        self.log.info("---> Project folder %s successfully created." % pFolder)
        self.rf_projectTree()

    def on_cancel(self):
        """
        Reset new project values
        """
        self.leProjectName.clear()
        self.leProjectAlias.clear()

    def on_loadProject(self):
        """
        Load selected project
        """
        item = self.selectedProjectItem
        self.mainUi.loadProject(item.fullName)
        self.close()

    def new_ProjectItem(self, project):
        """
        Create project QTreeWidgetItem
        :param project: Priject name and alias
        :type project: dict
        :return: New projetct item
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = QtGui.QTreeWidgetItem()
        newItem.alias = project['alias']
        newItem.name = project['name']
        newItem.fullName = "%s--%s" % (project['alias'], project['name'])
        newItem.projectRootPath = os.path.join(self.grapherProjectsPath, newItem.fullName)
        newItem.setText(0, newItem.fullName)
        return newItem


class EditProject(QtGui.QMainWindow, wgProjectEditUI.Ui_mwEditProject):
    """
    Edit project dialog
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.info("Launching project settings ui ...")
        super(EditProject, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup dialog ui
        """
        self.setupUi(self)
        self.lNameValue.setText(self.projectName)
        self.lAliasValue.setText(self.projectAlias)
        self.twSettings.itemClicked.connect(self.on_category)
        self.cbEntity.currentIndexChanged.connect(partial(self.rf_cbSettings, self.cbEntityType, 'Entity Type'))
        self.cbEntityType.currentIndexChanged.connect(partial(self.rf_cbSettings, self.cbEntitySpec, 'Entity Spec'))
        self.pbCreate.clicked.connect(self.on_create)
        self.addAllCategory()
        self.rf_settingsVis()

    @property
    def projectPath(self):
        """
        Get project path
        :return: Project path
        :rtype: str
        """
        return self.mainUi.projectPath

    @property
    def projectName(self):
        """
        Get project name
        :return: Project name
        :rtype: str
        """
        return self.mainUi.projectName

    @property
    def projectAlias(self):
        """
        Get project alias
        :return: Project alias
        :rtype: str
        """
        return self.mainUi.projectAlias

    @property
    def projectFullName(self):
        """
        Get project fullName
        :return: Project fullName
        :rtype: str
        """
        return self.mainUi.projectFullName

    @property
    def currentTree(self):
        """
        Get tree QComboBox current text
        :return: Current Tree
        :rtype: str
        """
        return "graph"

    @property
    def currentEntity(self):
        """
        Get entity QComboBox current text
        :return: Current entity
        :rtype: str
        """
        return str(self.cbEntity.currentText())

    @property
    def currentEntityType(self):
        """
        Get entity type QComboBox current text
        :return: Current entity type
        :rtype: str
        """
        return str(self.cbEntityType.currentText())

    @property
    def currentEntitySpec(self):
        """
        Get entity spec QComboBox current text
        :return: Current entity spec
        :rtype: str
        """
        return str(self.cbEntitySpec.currentText())

    def rf_settingsVis(self):
        """
        Refresh settings widget visibility
        """
        items = self.twSettings.selectedItems()
        if items:
            self.qfTreeContents.setVisible(True)
            for k, v in items[0].settingsVis.iteritems():
                k.setVisible(v)
        else:
            self.qfTreeContents.setVisible(False)

    def rf_cbSettings(self, QComboBox, cat):
        """
        Refresh QComboBox
        :param QComboBox: Widget to update
        :type QComboBox: QtGui.QComboBox
        :param cat: Settings category
        :type cat: str
        """
        QComboBox.clear()
        if cat == 'Entity':
            QComboBox.addItems(os.listdir(os.path.join(self.projectPath, self.currentTree)))
            self.lNewFolder.setText("New Folder")
        elif cat == 'Entity Type':
            QComboBox.addItems(os.listdir(os.path.join(self.projectPath, self.currentTree, self.currentEntity)))
            self.lNewFolder.setText("New Folder")
        elif cat == 'Entity Spec':
            QComboBox.addItems(os.listdir(os.path.join(self.projectPath, self.currentTree, self.currentEntity,
                                                       self.currentEntityType)))
            self.lNewFolder.setText("Asset Name")

    def addAllCategory(self):
        """
        Add all settings tree category
        """
        self.twSettings.clear()
        self.addCategory('Entity', {self.qfEntity: False, self.qfEntityType: False, self.qfEntitySpec: False,
                                    self.qfAssetNs: False})
        self.addCategory('Entity Type', {self.qfEntity: True, self.qfEntityType: False, self.qfEntitySpec: False,
                                         self.qfAssetNs: False})
        self.addCategory('Entity Spec', {self.qfEntity: True, self.qfEntityType: True, self.qfEntitySpec: False,
                                         self.qfAssetNs: False})
        self.addCategory('New Asset', {self.qfEntity: True, self.qfEntityType: True, self.qfEntitySpec: True,
                                       self.qfAssetNs: True})

    def addCategory(self, catName, settingsVis):
        """
        Add settings tree category
        :param catName: Settings category name
        :type catName: str
        :param settingsVis: Category widget visibility state
        :type settingsVis: dict
        """
        newCat = self.new_categoryItem(catName, settingsVis)
        self.twSettings.addTopLevelItem(newCat)

    def on_category(self):
        """
        Command launched when 'Category' QTreeWidgetItem is clicked
        """
        self.rf_settingsVis()
        item = self.twSettings.selectedItems()[0]
        if item.name == 'Entity Type':
            self.rf_cbSettings(self.cbEntity, 'Entity')
        elif item.name == 'Entity Spec':
            self.rf_cbSettings(self.cbEntityType, 'Entity Type')
        elif item.name == 'New Asset':
            self.rf_cbSettings(self.cbEntitySpec, 'Entity Spec')

    def on_create(self):
        """
        Command launched when 'Create' QPushButton is clicked.
        Will create given folder in grapher project
        """
        items = self.twSettings.selectedItems()
        if items:
            cat = items[0].name
            folderName = str(self.leNewFolder.text())
            if cat == 'Tree':
                self.createFolder(folderName, cat)
            elif cat == 'Entity':
                self.createFolder(folderName, cat)
            elif cat == 'Entity Type':
                self.createFolder(folderName, cat)
            elif cat == 'Entity Spec':
                self.createFolder(folderName, cat)
            elif cat == 'New Asset':
                self.createAsset()
            self.mainUi.graphTree.rf_projectTree()
            self.leNewFolder.clear()

    def createFolder(self, folderName, category):
        """
        Create graph folder
        :param folderName: New folder name
        :type folderName: str
        :param category: Category name
        :type category: str
        """
        #-- Get params --#
        if category == 'Tree':
            path = pFile.conformPath(os.path.join(self.projectPath, folderName))
            log1 = "Creating grapher '%s' folder: '%s' ..." % (category, folderName)
            log2 = "---> Grapher '%s' folder '%s' successfully created." % (category, folderName)
        elif category == 'Entity':
            relPath = "%s/%s" % (self.currentTree, folderName)
            path = pFile.conformPath(os.path.join(self.projectPath, relPath))
            log1 = "Creating grapher '%s' folder: '%s' ..." % (category, relPath)
            log2 = "---> Grapher '%s' folder '%s' successfully created." % (category, relPath)
        elif category == 'Entity Type':
            relPath = "%s/%s/%s" % (self.currentTree, self.currentEntity, folderName)
            path = pFile.conformPath(os.path.join(self.projectPath, relPath))
            log1 = "Creating grapher '%s' folder: '%s' ..." % (category, relPath)
            log2 = "---> Grapher '%s' folder '%s' successfully created." % (category, relPath)
        elif category == 'Entity Spec':
            relPath = "%s/%s/%s/%s" % (self.currentTree, self.currentEntity, self.currentEntityType, folderName)
            path = pFile.conformPath(os.path.join(self.projectPath, relPath))
            log1 = "Creating grapher '%s' folder: '%s' ..." % (category, relPath)
            log2 = "---> Grapher '%s' folder '%s' successfully created." % (category, relPath)
        else:
            path = None
            log1 = None
            log2 = None
        #-- Create Graph Folder --#
        if path is not None:
            self.log.info(log1)
            gpCore.createGrapherFolder(path, category)
            self.log.info(log2)

    def createAsset(self):
        """
        Create graph asset
        """
        assetName = str(self.leNewFolder.text())
        assetNs = str(self.leAssetNs.text())
        relPath = "%s/%s/%s/%s/%s" % (self.currentTree, self.currentEntity, self.currentEntityType,
                                      self.currentEntitySpec, assetName)
        path = pFile.conformPath(os.path.join(self.projectPath, relPath))
        self.log.info("Creating grapher asset: '%s' ..." % relPath)
        data = {'assetEntity': self.currentEntity, 'assetType': self.currentEntityType,
                'assetSpec': self.currentEntitySpec, 'assetName': assetName, 'assetNs': assetNs}
        gpCore.createGrapherAsset(path, data)
        self.log.info("---> Grapher asset '%s' successfully created." % relPath)

    @staticmethod
    def new_categoryItem(catName, settingsVis):
        """
        Add settings tree item
        :param catName: Settings category name
        :type catName: str
        :param settingsVis: Category widget visibility state
        :type settingsVis: dict
        :return: New settings tree item
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = QtGui.QTreeWidgetItem()
        newItem.name = catName
        newItem.settingsVis = settingsVis
        newItem.setText(0, catName)
        return newItem


class ProjectTree(QtGui.QTreeWidget):

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        super(ProjectTree, self).__init__()
        self._setupUi()

    def _setupUi(self):
        """
        Setup tree widget
        """
        self.log.debug("---> Setup GraphTree ...")
        self.setItemsExpandable(True)
        self.setMinimumWidth(200)
        self.setHeaderHidden(False)
        self.setIndentation(15)
        self.setDragEnabled(True)
        self.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.rf_treeHeader()

    @property
    def projectPath(self):
        """
        Get project path
        :return: Project path
        :rtype: str
        """
        return self.mainUi.projectPath

    @property
    def projectName(self):
        """
        Get project name
        :return: Project name
        :rtype: str
        """
        return self.mainUi.projectName

    @property
    def projectAlias(self):
        """
        Get project alias
        :return: Project alias
        :rtype: str
        """
        return self.mainUi.projectAlias

    @property
    def projectFullName(self):
        """
        Get project fullName
        :return: Project fullName
        :rtype: str
        """
        return self.mainUi.projectFullName

    def getItemFromPath(self, path):
        """
        Get treeWidget from itemPath
        :param path: Item path
        :type path: str
        :return: Tree item
        :rtype: QtGui.QTreeWidgetItem
        """
        for item in pQt.getAllItems(self):
            if item.relPath == path:
                return item

    def rf_treeHeader(self):
        """
        Refresh project tree header
        """
        if self.projectFullName is not None:
            self.setHeaderLabel(self.projectFullName)
        else:
            self.setHeaderLabel("Untitled")

    def rf_projectTree(self):
        """
        Refresh project tree
        """
        self.rf_treeHeader()
        self.clear()
        tree = gpCore.getProjectTree(self.projectPath)
        for root in tree['_order']:
            folders = tree[root]['folders']
            files = tree[root]['files']
            for fld in folders:
                fullPath = os.path.join(root, fld)
                relPath = "%s" % fullPath.replace('%s%s' % (self.projectPath, os.sep), '')
                relPath = pFile.conformPath(relPath)
                newItem = self.new_treeItem(fld, 'folder', relPath)
                if root == self.projectPath:
                    self.addTopLevelItem(newItem)
                else:
                    pItem = self.getItemFromPath('/'.join(relPath.split('/')[:-1]))
                    if pItem is not None:
                        pItem.addChild(newItem)
                self.setItemWidget(newItem, 0, newItem._widget)
            for fl in files:
                fullPath = os.path.join(root, fl)
                relPath = "%s" % fullPath.replace('%s%s' % (self.projectPath, os.sep), '')
                relPath = pFile.conformPath(relPath)
                itemName = fl.replace('.py', '')
                newItem = self.new_treeItem(itemName, 'file', relPath)
                if root == self.projectPath:
                    self.addTopLevelItem(newItem)
                else:
                    pItem = self.getItemFromPath('/'.join(relPath.split('/')[:-1]))
                    if pItem is not None:
                        pItem.addChild(newItem)
                self.setItemWidget(newItem, 0, newItem._widget)

    def new_treeItem(self, itemName, itemType, relPath):
        """
        Create tree item
        :param itemName: Tree item name
        :type itemName: str
        :param itemType: Tree item type ('file' or 'folder')
        :type itemType: str
        :param relPath: Tree item relative path
        :type relPath: str
        :return: Tree item
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = QtGui.QTreeWidgetItem()
        newItem.relPath = relPath
        newItem.itemType = itemType
        newItem.itemName = itemName
        newItem._widget = ProjectTreeItem(self.mainUi, newItem)
        return newItem

    def startDrag(self, event):
        """
        Store dragged item for graphScene drops
        """
        item = self.selectedItems()[0]
        if item.itemType == 'file':
            self.mainUi.currentGraphScene.treeItemDragged = item
            super(ProjectTree, self).startDrag(event)


class ProjectTreeItem(QtGui.QWidget, wgTreeItemUI.Ui_wgTreeItem):

    def __init__(self, mainUi, pItem):
        self.mainUi = mainUi
        self.pItem = pItem
        self.collapseIcon = QtGui.QIcon("gui/icon/png/treeCollapse.png")
        self.expandIcon = QtGui.QIcon("gui/icon/png/treeExpand.png")
        self.folderFont = QtGui.QFont()
        self.folderFont.setBold(True)
        super(ProjectTreeItem, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup project tree item widget
        """
        self.setupUi(self)
        self.lItemName.setText(self.pItem.itemName)
        if self.pItem.itemType == 'folder':
            self.lItemName.setFont(self.folderFont)
            self.typeIcon = QtGui.QIcon("gui/icon/png/treefolder.png")
        else:
            if self.pItem.itemName.endswith('.cst'):
                self.typeIcon = QtGui.QIcon("gui/icon/png/toolAssetCastingNode.png")
            if self.pItem.itemName.endswith('.grp'):
                self.typeIcon = QtGui.QIcon("gui/icon/png/treeGraph.png")
        self.pbItemIcon.setIcon(self.typeIcon)
