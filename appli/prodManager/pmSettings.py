import os
from functools import partial
from lib.qt import procQt as pQt
from PyQt4 import QtGui, QtCore, Qt
from lib.system import procFile as pFile
from appli.prodManager.ui import settingsUI, defaultSettingsWgtUI, defaultSettingsDialUI, treeEditorWgtUI


class ProjectSettingsUi(QtGui.QMainWindow, settingsUI.Ui_mwSettings):
    """ QMainWindow class used by 'ProdManager' QMainWindow.
        :param mainUi: ProdManager window
        :type mainUi: QtGui.QMainWindow
        :param logLvl: Print log level
        :type logLvl: str """

    def __init__(self, mainUi, logLvl='info'):
        self.log = pFile.Logger(title="Settings", level=logLvl)
        self.log.info("########## PROJECT SETTINGS ##########", newLinesBefor=1)
        self.mainUi = mainUi
        self.pm = self.mainUi.pm
        super(ProjectSettingsUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup main ui """
        self.setupUi(self)
        self.rf_projectInfo()
        self.twSettings.itemClicked.connect(self.on_settings)
        self.addWidgets()
        self.pbReset.setEnabled(False)
        self.pbSave.clicked.connect(self.on_save)
        self.pbClose.clicked.connect(self.close)

    def rf_projectInfo(self):
        """ Refresh project info """
        self.log.debug("Refresh project info ...")
        self.lNameValue.setText(self.pm.project.name)
        self.lAliasValue.setText(self.pm.project.alias)
        self.lTypeValue.setText(self.pm.project.type)
        if self.pm.project.type is 'Movie':
            self.qfProject_2.setVisible(False)
        else:
            self.qfProject_2.setVisible(True)
            self.lSeasonValue.setText(self.pm.project.season)
            if self.pm.project.episode is None:
                self.lEpisode.setVisible(False)
                self.lEpisodeValue.setVisible(False)
            else:
                self.lEpisode.setVisible(True)
                self.lEpisodeValue.setVisible(True)
                self.lEpisodeValue.setText(self.pm.project.episode)

    def rf_settingsInfo(self, info):
        """ Refresh settings info
            :param info: Settings info to print
            :type info: str | list """
        self.teInfo.clear()
        if isinstance(info, str):
            self.teInfo.setPlainText(info)
        else:
            self.teInfo.setPlainText('\n'.join(info))

    def addWidgets(self):
        """ Parent all settings widget to ui """
        self.log.debug("Add widgets ...")
        self.general = General(self)
        self.addWidget('general', self.general)
        self.tasks = Tasks(self)
        self.addWidget('tasks', self.tasks)
        self.trees = Trees(self)
        self.addWidget('trees', self.trees)
        self.steps = Steps(self)
        self.addWidget('steps', self.steps)
        self.tree = Tree(self)
        self.addWidget('tree', self.tree)

    def addWidget(self, label, QWidget):
        """ Set andparent given widget
            :param label: Widget label
            :type label: str
            :param QWidget: QWidget to add
            :type QWidget: QtGui.QWidget """
        self.log.debug("\t %s" % label)
        newItem = QtGui.QTreeWidgetItem()
        newItem.setText(0, label)
        newItem.label = label
        newItem.widget = QWidget
        newItem.widget.setVisible(False)
        self.twSettings.addTopLevelItem(newItem)
        self.vlSettings.insertWidget(1, newItem.widget)
        self.log.debug("\t --> Done")

    def on_settings(self):
        """ Command launched when 'twProject' QTreeWidgetItem is clicked """
        selItems = self.twSettings.selectedItems()
        if selItems:
            allItems = pQt.getAllItems(self.twSettings)
            for item in allItems:
                item.widget.setVisible(False)
                if item.label == selItems[0].label:
                    item.widget.setVisible(True)
                    self.rf_settingsInfo(item.widget.widgetInfo)

    def on_save(self):
        """ Command launched when QPushButton 'Save' is clicked """
        self.log.info("#-- Save Project Settings --#")
        self.pm.project.setParam('rootPath', self.general.getParams())
        self.pm.project.setParam('tasks', self.tasks.getParams())
        self.pm.project.setParam('trees', self.trees.getParams())
        self.pm.project.setParam('steps', self.steps.getParams())
        self.pm.project.saveSettings()

    def closeEvent(self, *args, **kwargs):
        """ Command launched when QPushButton 'Close' is clicked, or dialog is closed """
        self.log.debug("Closing project settings ui ...")


class SettingsWidget(QtGui.QWidget, defaultSettingsWgtUI.Ui_wgSettings):
    """ QWidget class used by 'ProjectSettings' QMainWindow.
        :param settingsUi: Parent window
        :type settingsUi: QtGui.QMainWindow
        :param wgLabel: Widget label must be equal to instance name
        :type wgLabel: str
        :param btnLabel: Button suffixe for 'Add' and 'Del'
        :type btnLabel: str """

    def __init__(self, settingsUi, wgLabel, btnLabel, treeSwitch=False):
        self.settingsUi = settingsUi
        self.pm = self.settingsUi.pm
        self.log = self.settingsUi.log
        self.wgLabel = wgLabel
        self.btnLabel = btnLabel
        self.treeSwitch = treeSwitch
        super(SettingsWidget, self).__init__()
        self._setupUi()
        self._initTreeSwitch()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget """
        self.setupUi(self)
        self.cbCurrentTree.setVisible(self.treeSwitch)
        self.cbCurrentTree.addItem('None')
        self.pbAddItem.setText("Add %s" % self.btnLabel)
        self.pbDelItem.setText("Del %s" % self.btnLabel)
        self.pbDelItem.clicked.connect(self.on_delItem)
        self.pbItemUp.clicked.connect(partial(self.on_moveItem, 'up'))
        self.pbItemDn.clicked.connect(partial(self.on_moveItem, 'down'))

    def _initTreeSwitch(self):
        """ Init tree switch contents and data """
        if self.treeSwitch:
            trees = self.settingsUi.trees.getParams()
            for n in sorted(trees.keys()):
                treeName = trees[n].keys()[0]
                self.addTreeSwitch(treeName, None)

    @property
    def currentTree(self):
        """ Get current tree
            :return: Selected tree name
            :rtype: str """
        currentTree = str(self.cbCurrentTree.currentText())
        if not currentTree == 'None':
            return str(self.cbCurrentTree.currentText())

    def addTreeSwitch(self, treeName, value):
        """ Add tree switch item
            :param treeName: Tree name
            :type treeName: str
            :param value: Tree settings params
            :type value: list | dict | None """
        self.cbCurrentTree.addItem(treeName)
        setattr(self.cbCurrentTree, treeName, value)

    def delTreeSwitch(self, treeName):
        """ Delete tree switch item
            :param treeName: Tree name
            :type treeName: str """
        for n, tree in enumerate(pQt.getComboBoxItems(self.cbCurrentTree)):
            if tree == treeName:
                self.cbCurrentTree.setCurrentIndex(0)
                self.cbCurrentTree.removeItem(n)
                delattr(self.cbCurrentTree, treeName)

    def on_delItem(self):
        """ Command launch when 'Del Item' QPushButton is clicked """
        pQt.delSelItems(self.twTree)

    def on_moveItem(self, side):
        """ Command launch when 'up' or 'down' QPushButton is clicked
            :param side: 'up' or 'down'
            :type side: str """
        selItems = self.twTree.selectedItems()
        if selItems:
            movedItem = pQt.moveSelItem(self.twTree, selItems[0], side)
            if movedItem is not None:
                pQt.deselectAllItems(self.twTree)
                movedItem.setSelected(True)


class General(SettingsWidget):
    """ Class used by 'ProjectSettings' QMainWindow.
        :param settingsUi: Parent window
        :type settingsUi: QtGui.QMainWindow """

    def __init__(self, settingsUi):
        super(General, self).__init__(settingsUi, 'general', 'Path')
        self._setupWidget()
        self.refresh()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        """ Setup widget """
        self.setMinimumHeight(100)
        self.setMaximumHeight(100)
        self.pbAddItem.clicked.connect(self.on_addItem)
        self.twTree.setColumnCount(1)
        self.twTree.setHeaderLabels(['Root Path'])
        self.twTree.header().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)

    @property
    def widgetInfo(self):
        """ Widget info printed in settings ui
            :return: Widget info to print
            :rtype: list """
        return ["Project Root path: List of work directories root path.",
                "First path in tree will be the project main root path."]

    @property
    def defaultRootPath(self):
        """ Default work directories root path
            :return: Root path
            :rtype: str """
        return "D:/prods"

    def getParams(self):
        """ Get widget project params
            :return: General params
            :rtype: list """
        params = []
        allItems = pQt.getAllItems(self.twTree)
        for item in allItems:
            params.append(item.rootPath)
        return params

    def refresh(self):
        """ Refresh general widget """
        pathList = self.pm.project.rootPath
        if pathList is None:
            pathList = [self.defaultRootPath]
        self.twTree.clear()
        newItems = []
        for path in pathList:
            newItem = self.newPathItem(path)
            newItems.append(newItem)
        self.twTree.addTopLevelItems(newItems)

    def on_addItem(self):
        """ Command launched when QPushButton 'Add Root Path' is clicked """
        rootUi = NewRootUi(self)
        rootUi.exec_()

    @staticmethod
    def newPathItem(path):
        """ Create new path QTreeWidgetItem
            :param path: Project root path
            :type path: str
            :return: Root path QTreeWidgetItem
            :rtype: QtGui.QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem.setText(0, path)
        newItem.rootPath = path
        return newItem


class NewRootUi(QtGui.QDialog, defaultSettingsDialUI.Ui_settingsItem):
    """ QDialog class used by 'General' QWidget
        :param QWidget: Parent widget
        :type QWidget: QtGui.QWidget """

    def __init__(self, QWidget):
        self.pWidget = QWidget
        self.log = self.pWidget.log
        super(NewRootUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup dialog """
        self.setupUi(self)
        self.qfRootPath.setVisible(True)
        self.qfTask.setVisible(False)
        self.qfTreeName.setVisible(False)
        self.qfStep.setVisible(False)
        self.pbOpen.clicked.connect(self.on_open)
        self.pbAdd.clicked.connect(self.accept)
        self.pbCancel.clicked.connect(self.close)

    def on_open(self):
        """ Command launched when QPushButton 'Open' is clicked. Launch QFileDialog """
        self.fdOpen = pQt.fileDialog(fdMode='open', fdFileMode='DirectoryOnly',
                                     fdRoot=self.pWidget.defaultRootPath, fdCmd=self.editNewPath)
        self.fdOpen.exec_()

    def editNewPath(self):
        """ Command launched when QFileDialog 'Open' is accepted"""
        selectedPath = str(self.fdOpen.selectedFiles()[0])
        self.lePath.setText(selectedPath)
        self.fdOpen.close()

    def accept(self):
        """ Command launched when QPushButton 'Add' is clicked. Update parent widget """
        newPath = str(self.lePath.text())
        if newPath not in ['', ' ']:
            if os.path.exists(newPath):
                self._checkNewPath(newPath)
                newItem = self.pWidget.newPathItem(newPath)
                self.pWidget.twTree.addTopLevelItem(newItem)
                self.log.debug("Root path %r successfully added." % newPath)
                self.close()
            else:
                self.log.error("New path doesn't exist !!!")
        else:
            self.log.error("Path can not be empty !!!")

    def _checkNewPath(self, path):
        """ Check if new path is already in path list
            :param path: New root path
            :type path: str """
        allItems = pQt.getAllItems(self.pWidget.twTree)
        for item in allItems:
            if path == item.rootPath:
                log = "New path %s already exists !!!" % path
                self.log.error(log)
                raise ValueError, log


class Tasks(SettingsWidget):
    """ Class used by 'ProjectSettings' QMainWindow.
        :param settingsUi: Parent window
        :type settingsUi: QtGui.QMainWindow """

    def __init__(self, settingsUi):
        super(Tasks, self).__init__(settingsUi, 'tasks', 'Task')
        self._setupWidget()
        self.refresh()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        """ Setup widget """
        self.setMinimumHeight(350)
        self.pbAddItem.clicked.connect(self.on_addItem)
        self.twTree.setColumnCount(4)
        self.twTree.setHeaderLabels(['Name', 'Label', 'Color', 'Stat'])
        for n in range(4):
            self.twTree.header().setResizeMode(n, QtGui.QHeaderView.ResizeToContents)

    @property
    def widgetInfo(self):
        """ Widget info printed in settings ui
            :return: Widget info to print
            :rtype: str """
        return ["Project tasks: Asset or shot progression.",
                "If 'Stat' is True, all shotnode with this task progression",
                "will count in project statistics."]

    @property
    def defaultTasks(self):
        """ Default Tasks when creating a new project
            :return: Default tasks data
            :rtype: dict """
        return {0: {'name': "out", 'label': "Out", 'color': (0, 0, 0), 'stat': False},
                1: {'name': "sb", 'label': "Stand By", 'color': (125, 125, 125), 'stat': True},
                2: {'name': "warn", 'label': "Warning", 'color': (255, 0, 0), 'stat': True},
                3: {'name': "rdy", 'label': "Ready", 'color': (229, 229, 229), 'stat': True},
                4: {'name': "toDo", 'label': "To Do", 'color': (155, 232, 232), 'stat': True},
                5: {'name': "rtk", 'label': "Retake", 'color': (255, 170, 0), 'stat': True},
                6: {'name': "wip", 'label': "Work In Progress", 'color': (255, 255, 0), 'stat': True},
                7: {'name': "wfa", 'label': "Waiting For Approval", 'color': (0, 0, 255), 'stat': True},
                8: {'name': "rvw", 'label': "Review", 'color': (0, 170, 255), 'stat': True},
                9: {'name': "cbb", 'label': "Could Be Better", 'color': (171, 194, 255), 'stat': True},
                10: {'name': "app", 'label': "Approved", 'color': (85, 255, 127), 'stat': True},
                11: {'name': "vld", 'label': "Valide", 'color': (170, 255, 0), 'stat': True},
                12: {'name': "fin", 'label': "Final", 'color': (85, 255, 0), 'stat': True}}

    def getParams(self):
        """ Get widget task params
            :return: Task params
            :rtype: dict """
        taskDict = {}
        taskKeys = ['name', 'label', 'color', 'stat']
        allItems = pQt.getAllItems(self.twTree)
        for n, item in enumerate(allItems):
            taskDict[n] = {}
            for key in taskKeys:
                taskDict[n][key] = getattr(item, key)
        return taskDict

    def getTaskList(self, key='name'):
        """ List all project tasks
            :param key: 'name' or 'label'
            :type key: str
            :return: task list
            :rtype: list """
        tasks = []
        taskDict = self.getParams()
        for n in sorted(taskDict.keys()):
            tasks.append(taskDict[n][key])
        return tasks

    def refresh(self):
        """ Refresh task widget """
        self.twTree.clear()
        tasks = self.pm.project.tasks
        if tasks is None:
            tasks = self.defaultTasks
        for n in sorted(tasks.keys()):
            self.addTask(tasks[n]['name'], tasks[n]['label'], color=tasks[n]['color'], stat=tasks[n]['stat'])

    def on_addItem(self):
        """ Command launched when 'Add Task' QPushButton is clicked """
        taskUi = NewTaskUi(self)
        taskUi.exec_()

    def on_moveItem(self, side):
        """ Command launch when 'up' or 'down' QPushButton is clicked
            :param side: 'up' or 'down'
            :type side: str """
        selItems = self.twTree.selectedItems()
        if selItems:
            movedItem = pQt.moveSelItem(self.twTree, selItems[0], side)
            if movedItem is not None:
                pQt.deselectAllItems(self.twTree)
                movedItem._wgColor = self.newTaskColor(movedItem, movedItem.color)
                movedItem._wgStat = self.newTaskStat(movedItem, movedItem.stat)
                self.twTree.setItemWidget(movedItem, 2, movedItem._wgColor)
                self.twTree.setItemWidget(movedItem, 3, movedItem._wgStat)
                movedItem.setSelected(True)

    def addTask(self, name, label, color=None, stat=True):
        """ Add new task to QTreeWidget
            :param name: Task Name
            :type name: str
            :param label: Task Label
            :type label: str
            :param color: Rgb color
            :type color: tuple
            :param stat: Task count in stats
            :type stat: bool
            :return: New task item
            :rtype: QtGui.QTreeWidgetItem """
        if not name in self.getTaskList(key='name') and not label in self.getTaskList(key='label'):
            newItem = self.newTaskItem(name, label, color=color, stat=stat)
            self.twTree.addTopLevelItem(newItem)
            self.twTree.setItemWidget(newItem, 2, newItem._wgColor)
            self.twTree.setItemWidget(newItem, 3, newItem._wgStat)
            return newItem

    def newTaskItem(self, name, label, color=None, stat=True):
        """ Cretae new task TreeWidgetItem
            :param name: Task name
            :type name: str
            :param label: Task label
            :type label: str
            :param color: Task color
            :type color: tuple
            :param stat: Task count in statistic
            :type stat: bool
            :return: New QTreeWidgetItem
            :rtype: QtGui.QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem.setText(0, name)
        newItem.setText(1, label)
        newItem.name = name
        newItem.label = label
        newItem.color = color
        newItem.stat = stat
        newItem._wgColor = self.newTaskColor(newItem, color)
        newItem._wgStat = self.newTaskStat(newItem, stat)
        return newItem

    def newTaskColor(self, item, color):
        """ New task color QPushButton
            :param item: Parent QTreeWidgetItem
            :type item: QtGui.QTreeWidgetItem
            :param color: Rgb color
            :type color: tuple
            :return: New task color QPushButton
            :rtype: QtGui.QPushButton """
        newColor = QtGui.QPushButton()
        newColor.setText('')
        newColor.setMaximumWidth(40)
        newColor.connect(newColor, QtCore.SIGNAL("clicked()"), partial(self.on_taskColor, item))
        if color is None:
            item.color = (200, 200, 200)
        else:
            item.color = color
            newColor.setStyleSheet("background:rgb(%s, %s, %s)" % (color[0], color[1], color[2]))
        return newColor

    def on_taskColor(self, item):
        """ Command launch when 'colorChoice' QPushButton is clicked
            :param item: Task item
            :type item: QtGui.QTreeWidgetItem """
        # noinspection PyArgumentList
        color = QtGui.QColorDialog.getColor()
        if color.isValid():
            rgba = color.getRgb()
            item._wgColor.setStyleSheet("background:rgb(%s, %s, %s)" % (rgba[0], rgba[1], rgba[2]))
            item.color = (rgba[0], rgba[1], rgba[2])
            self.log.debug("\t %s color = %s" % (item.name, (rgba[0], rgba[1], rgba[2])))

    def newTaskStat(self, item, stat):
        """ New task stat QCheckBox
            :param item: Task item
            :type item: QtGui.QTreeWidgetItem
            :param stat: Task count in stats
            :type stat: bool
            :return: New task stat checkBox
            :rtype: QCheckBox """
        newStat = QtGui.QCheckBox()
        newStat.setText('')
        newStat.setChecked(stat)
        newStat.connect(newStat, QtCore.SIGNAL("clicked()"), partial(self.on_taskStat, item, newStat))
        return newStat

    @staticmethod
    def on_taskStat(item, QCheckBox):
        """ Command launch when 'Stat' QCheckBox is clicked
            :param item: Task item
            :type item: QtGui.QTreeWidgetItem
            :param QCheckBox: Task stat
            :type QCheckBox: QtGui.QCheckBox """
        item.stat = QCheckBox.isChecked()


class NewTaskUi(QtGui.QDialog, defaultSettingsDialUI.Ui_settingsItem):
    """ QDialog class used by 'Tasks' QWidget
        :param QWidget: Parent widget
        :type QWidget: QtGui.QWidget """

    def __init__(self, QWidget):
        self.pWidget = QWidget
        self.log = self.pWidget.log
        super(NewTaskUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup dialog """
        self.setupUi(self)
        self.qfRootPath.setVisible(False)
        self.qfTask.setVisible(True)
        self.qfTreeName.setVisible(False)
        self.qfStep.setVisible(False)
        self.pbAdd.clicked.connect(self.accept)
        self.pbCancel.clicked.connect(self.close)

    def accept(self):
        """ Command launched when QPushButton 'Add' is clicked. Update parent widget """
        name = str(self.leName.text())
        label = str(self.leLabel.text())
        errorFilters = ['', ' ']
        if name in errorFilters or label in errorFilters:
            log = "Task 'name' or 'label' can not be empty !!!"
            self.log.error(log)
            raise ValueError, log
        result = self.pWidget.addTask(name, label)
        if result is not None:
            self.close()
            self.log.debug("Task %r successfully added." % label)


class Trees(SettingsWidget):
    """ Class used by 'ProjectSettings' QMainWindow.
        :param settingsUi: Parent window
        :type settingsUi: QtGui.QMainWindow """

    def __init__(self, settingsUi):
        super(Trees, self).__init__(settingsUi, 'trees', 'Tree')
        self._setupWidget()
        self.refresh()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        """ Setup widget """
        self.pbAddItem.clicked.connect(self.on_addTree)
        self.twTree.setColumnCount(2)
        self.twTree.setHeaderLabels(['Tree Name', 'Tree Type'])
        self.twTree.header().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.twTree.header().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)

    @property
    def widgetInfo(self):
        """ Widget info printed in settings ui
            :return: Widget info to print
            :rtype: str """
        return "Project trees: Production work trees."

    @property
    def defaultTrees(self):
        """ Default Trees when creating a new project
            :return: Default trees params
            :rtype: dict """
        return {0: {'assets': 'asset'}, 1: {'shots': 'shot'}}

    def getParams(self):
        """ Get widget tree params
            :return: Trees params
            :rtype: Dict """
        allItems = pQt.getAllItems(self.twTree)
        trees = {}
        for n, item in enumerate(allItems):
            trees[n] = {}
            trees[n][item.name] = item.type
        return trees

    def getTreeType(self, treeName):
        """ Get given tree treeType
            :param treeName: Tree name
            :type treeName: str
            :return: Tree type
            :rtype: str """
        trees = self.getParams()
        for n in trees.keys():
            if treeName in trees[n].keys():
                return trees[n][treeName]

    def refresh(self):
        """ Refresh tree widget """
        self.twTree.clear()
        trees = self.pm.project.trees
        if trees is None:
            trees = self.defaultTrees
        for n in sorted(trees.keys()):
            treeDict = trees[n]
            treeName = treeDict.keys()[0]
            self.addTree(treeName, treeDict[treeName])

    def on_addTree(self):
        """ Command launched when 'Add Task' QPushButton is clicked """
        treeUi = NewTreeUi(self)
        treeUi.exec_()

    def on_delItem(self):
        """ Command launch when 'Del Tree' QPushButton is clicked """
        selItems = self.twTree.selectedItems()
        if selItems:
            treeName = selItems[0].name
            super(Trees, self).on_delItem()
            if hasattr(self.settingsUi, 'steps'):
                self.settingsUi.steps.delTreeSwitch(treeName)
                self.log.debug("Tree %r successfully deleted." % treeName)

    def addTree(self, treeName, treeType):
        """ Add new tree to QTreeWidget
            :param treeName: New tree name
            :type treeName: str
            :param treeType: 'asset', 'shot', 'shooting', 'other'
            :type treeType: str
            :return: Tree item
            :rtype: QtGui.QTreeWidgetItem """
        if not treeName in self.getParams():
            newItem = self.newTreeItem(treeName, treeType)
            self.twTree.addTopLevelItem(newItem)
            if hasattr(self.settingsUi, 'steps'):
                self.settingsUi.steps.addTreeSwitch(treeName, self.settingsUi.steps.defaultSteps(treeType))
            if hasattr(self.settingsUi, 'tree'):
                self.settingsUi.tree.addTreeSwitch(treeName, self.settingsUi.tree.defaultTree(treeType))
            return newItem

    @staticmethod
    def newTreeItem(treeName, treeType):
        """ Cretae new tree TreeWidgetItem
            :param treeName: Tree name
            :type treeName: str
            :param treeType: 'asset', 'shot', 'shooting', 'other'
            :type treeType: str
            :return: Tree item
            :rtype: QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem.setText(0, treeName)
        newItem.setText(1, treeType)
        newItem.name = treeName
        newItem.type = treeType
        return newItem


class NewTreeUi(QtGui.QDialog, defaultSettingsDialUI.Ui_settingsItem):
    """ QDialog class used by 'Trees' QWidget
        :param QWidget: Parent widget
        :type QWidget: QtGui.QWidget """

    def __init__(self, QWidget):
        self.pWidget = QWidget
        self.log = self.pWidget.log
        super(NewTreeUi, self).__init__()
        self._setupUi()
        self.rf_treeType()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup dialog """
        self.setupUi(self)
        self.qfRootPath.setVisible(False)
        self.qfTask.setVisible(False)
        self.qfTreeName.setVisible(True)
        self.qfStep.setVisible(False)
        self.pbAdd.clicked.connect(self.accept)
        self.pbCancel.clicked.connect(self.close)

    def rf_treeType(self):
        """ Refresh tree type """
        self.cbTreeType.addItems(['asset', 'shot', 'shooting', 'other'])

    def accept(self):
        """ Command launched when QPushButton 'Add' is clicked. Update parent widget """
        treeName = str(self.leTreeName.text())
        treeType = str(self.cbTreeType.currentText())
        if treeName in ['', ' ']:
            log = "Tree 'name' can not be empty !!!"
            self.log.error(log)
            raise ValueError, log
        result = self.pWidget.addTree(treeName, treeType)
        if result is not None:
            self.close()
            self.log.debug("Tree %r successfully added." % treeName)


class Steps(SettingsWidget):
    """ Class used by 'ProjectSettings' QMainWindow.
        :param settingsUi: Parent window
        :type settingsUi: QtGui.QMainWindow """

    def __init__(self, settingsUi):
        super(Steps, self).__init__(settingsUi, 'steps', 'Step', treeSwitch=True)
        self._setupWidget()
        self.initTreeSwitch()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        """ Setup widget """
        self.cbCurrentTree.setVisible(True)
        self.cbCurrentTree.currentIndexChanged.connect(self.refresh)
        self.pbAddItem.clicked.connect(self.on_addStep)
        self.twTree.setColumnCount(1)
        self.twTree.setHeaderLabels(['Step Name'])
        self.twTree.header().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)

    def initTreeSwitch(self):
        """ Init tree switch """
        trees = pQt.getComboBoxItems(self.cbCurrentTree)
        steps = self.pm.project.steps
        for tree in trees:
            if not tree == 'None':
                if steps is None:
                    steps = {}
                if not tree in steps.keys():
                    steps[tree] = self.defaultSteps(self.settingsUi.trees.getTreeType(tree))
                setattr(self.cbCurrentTree, tree, steps[tree])

    @property
    def widgetInfo(self):
        """ Widget info printed in settings ui
            :return: Widget info to print
            :rtype: list """
        return ["Project Steps: Steps for given tree.",
                "Use 'trees' comboBox to edit current tree."]

    @staticmethod
    def defaultSteps(treeType):
        """ Default Steps when creating a new project
            :return: Default steps
            :rtype: list """
        if treeType == 'asset':
            return ['modeling', 'mapping', 'rigg']
        elif treeType == 'shot':
            return ['anim', 'lighting', 'compo']
        elif treeType == 'shooting':
            return []
        elif treeType == 'other':
            return []

    def getParams(self):
        """ Get widget steps params
            :return: Steps params
            :rtype: dict """
        trees = pQt.getComboBoxItems(self.cbCurrentTree)
        treesDict = {}
        for tree in trees:
            if not tree == 'None':
                if hasattr(self.cbCurrentTree, tree):
                    treesDict[tree] = getattr(self.cbCurrentTree, tree)
        return treesDict

    def refresh(self):
        """ Refresh steps widget """
        self.twTree.clear()
        if self.currentTree is not None:
            steps = getattr(self.cbCurrentTree, self.currentTree)
            for step in steps:
                self.addStep(step)

    def on_addStep(self):
        """ Command launched when 'Add Task' QPushButton is clicked """
        if self.currentTree is not None:
            StepUi = NewStepUi(self)
            StepUi.exec_()

    def on_delItem(self):
        """ Command launch when 'Del Step' QPushButton is clicked """
        selItems = self.twTree.selectedItems()
        if selItems:
            stepName = selItems[0].name
            params = self.getParams()
            if params is not None:
                if self.currentTree is not None:
                    steps = params[self.currentTree]
                    if stepName in steps:
                        super(Steps, self).on_delItem()
                        steps.remove(stepName)
                        self.log.debug("remove step %s" % stepName)

    def on_moveItem(self, side):
        """ Command launch when 'up' or 'down' QPushButton is clicked
            :param side: 'up' or 'down'
            :type side: str """
        if self.currentTree is not None:
            steps = []
            super(Steps, self).on_moveItem(side)
            allItems = pQt.getAllItems(self.twTree)
            for item in allItems:
                steps.append(item.name)
            setattr(self.cbCurrentTree, self.currentTree, steps)

    def addStep(self, name):
        """ Add new Step to QTreeWidget
            :param name: Step name
            :type name: str
            :return: Step item
            :rtype: QtGui.QTreeWidgetItem """
        params = self.getParams()
        if self.currentTree is not None:
            steps = params[self.currentTree]
            newItem = self.newStepItem(name)
            self.twTree.addTopLevelItem(newItem)
            if name not in steps:
                steps.append(name)
                setattr(self.cbCurrentTree, self.currentTree, steps)
            return newItem

    @staticmethod
    def newStepItem(name):
        """ Cretae new tree TreeWidgetItem
            :param name: Step name
            :type name: str
            :return: Step item
            :rtype: QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem.setText(0, name)
        newItem.name = name
        return newItem


class NewStepUi(QtGui.QDialog, defaultSettingsDialUI.Ui_settingsItem):
    """ QDialog class used by 'Steps' QWidget
        :param QWidget: Parent widget
        :type QWidget: QtGui.QWidget """

    def __init__(self, QWidget):
        self.pWidget = QWidget
        self.log = self.pWidget.log
        super(NewStepUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup dialog """
        self.setupUi(self)
        self.qfRootPath.setVisible(False)
        self.qfTask.setVisible(False)
        self.qfTreeName.setVisible(False)
        self.qfStep.setVisible(True)
        self.pbAdd.clicked.connect(self.accept)
        self.pbCancel.clicked.connect(self.close)

    def accept(self):
        """ Command launched when QPushButton 'Add' is clicked. Update parent widget """
        stepName = str(self.leStep.text())
        if stepName in ['', ' ']:
            log = "Step name can not be empty !!!"
            self.log.error(log)
            raise ValueError, log
        result = self.pWidget.addStep(stepName)
        if result is not None:
            self.close()
            self.log.debug("Step %r successfully added." % stepName)


class Tree(SettingsWidget):
    """ Class used by 'ProjectSettings' QMainWindow.
        :param settingsUi: Parent window
        :type settingsUi: QtGui.QMainWindow """

    def __init__(self, settingsUi):
        super(Tree, self).__init__(settingsUi, 'tree', 'Tree', treeSwitch=True)
        self._setupWidget()
        self.initTreeSwitch()
        self.refresh()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        """ Setup widget """
        self.cbCurrentTree.setVisible(True)
        self.cbCurrentTree.currentIndexChanged.connect(self.on_treeSwitch)
        self.pbAddItem.setVisible(False)
        self.twTree.setColumnCount(1)
        self.twTree.setIndentation(20)
        self.twTree.setHeaderLabels(['Project Tree'])
        self.twTree.header().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.treeEditor = TreeEditor(self)
        self.vlSettings.addWidget(self.treeEditor)

    def initTreeSwitch(self):
        """ Init tree switch """
        trees = pQt.getComboBoxItems(self.cbCurrentTree)
        for tree in trees:
            if not tree == 'None':
                treesParams = self.pm.trees.getParams()
                setattr(self.cbCurrentTree, tree, treesParams[tree])

    @property
    def widgetInfo(self):
        """ Widget info printed in settings ui
            :return: Widget info to print
            :rtype: list """
        return ["Project Tree: Tree editor.",
                "Use 'trees' comboBox to edit current tree."]

    @staticmethod
    def defaultTree(treeType):
        """ Default tree folders when creating a new project
            :return: Default tree folders
            :rtype: list """
        if treeType == 'asset':
            return ['chars', 'props', 'sets']
        elif treeType == 'shot':
            return ['s001', 's002', 's003']
        elif treeType == 'shooting':
            return []
        elif treeType == 'other':
            return []

    def getParams(self):
        """ Get widget steps params
            :return: Steps params
            :rtype: dict """
        trees = pQt.getComboBoxItems(self.cbCurrentTree)
        treesDict = {}
        for tree in trees:
            if not tree == 'None':
                if hasattr(self.cbCurrentTree, tree):
                    treesDict[tree] = getattr(self.cbCurrentTree, tree)
        return treesDict

    def refresh(self):
        """ Refresh tree widget """
        self.twTree.clear()
        if self.currentTree is not None:
            treeDict = getattr(self.cbCurrentTree, self.currentTree)
            print "treeDict: ", treeDict

    def on_treeSwitch(self):
        """ Command launched when QComboBox 'TreeSwitch' current index changed """
        self.treeEditor.rf_btnCreateVis()
        self.refresh()

    def add_treeNode(self, itemLabel, itemName, itemType, parent=None):
        """ Create new tree node item
            :param itemLabel: New node label
            :type itemLabel: str
            :param itemName: New node name
            :type itemName: str
            :param itemType: New node Type ('container' or 'node')
            :type itemType: str
            :param parent: Parent item
            :type parent: QtGui.QTreeWidgetItem """
        newItem = self.newTreeItem(itemLabel, itemName, itemType)
        if parent is None:
            self.twTree.addTopLevelItem(newItem)
        else:
            parent.addChild(newItem)

    @staticmethod
    def newTreeItem(label, name, type):
        """ Create new TreeWidgetItem
            :param label: New node label
            :type label: str
            :param name: New node name
            :type name: str
            :param type: New node Type ('container' or 'node')
            :type type: str
            :return: New treeItem
            :rtype: QtGui.QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem.setText(0, label)
        newItem.label = label
        newItem.name = name
        newItem.type = type
        if type == 'node':
            newItem.setTextColor(0, Qt.QColor(0, 100, 255))
        return newItem


class TreeEditor(QtGui.QDialog, treeEditorWgtUI.Ui_wgTreeEditor):
    """ QDialog class used by 'Tree' QWidget
        :param QWidget: Parent widget
        :type QWidget: QtGui.QWidget """

    def __init__(self, QWidget):
        self.pWidget = QWidget
        self.log = self.pWidget.log
        self.settingsUi = self.pWidget.settingsUi
        super(TreeEditor, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup dialog """
        self.setupUi(self)
        self.rbUnique.clicked.connect(self.rf_methodeVis)
        self.rbMulti.clicked.connect(self.rf_methodeVis)
        self.pbCreate.clicked.connect(self.on_create)
        self.rf_methodeVis()
        self.rf_btnCreateVis()

    def rf_btnCreateVis(self):
        """ Refresh 'Create' button visibility """
        if self.pWidget.currentTree is None:
            self.pbCreate.setEnabled(False)
        else:
            self.pbCreate.setEnabled(True)

    def rf_methodeVis(self):
        """ Refresh methode visibility """
        self.fUnique.setVisible(self.rbUnique.isChecked())
        self.fMulti.setVisible(self.rbMulti.isChecked())

    def on_create(self):
        """ Command launched when QPushButton 'Create' is clicked """
        self.log.debug("Create Node")
        selItems = self.pWidget.twTree.selectedItems()
        itemType, newNodes = self.getEditorParams()
        if not selItems:
            for newNode in newNodes:
                self.pWidget.add_treeNode(newNode, newNode, itemType)
        else:
            for item in selItems:
                for newNode in newNodes:
                    self.pWidget.add_treeNode(newNode, item.name, itemType, parent=item)

    def getEditorParams(self):
        """ Get treeEditor creation params
            :return: Item type, NewNodes
            :rtype: str && list """
        if self.rbContainer.isChecked():
            itemType = 'container'
        else:
            itemType = 'node'
        newNodes = []
        if self.rbUnique.isChecked():
            newNodes.append(str(self.leNodeName.text()))
        else:
            for n in range(self.sbStart.value(), self.sbStop.value() + 1, self.sbStep.value()):
                newNodes.append("%s%s%s" % (str(self.lePrefixe.text()),
                                            str(n).zfill(self.sbPadding.value()),
                                            str(self.leSuffixe.text())))
        return itemType, newNodes
