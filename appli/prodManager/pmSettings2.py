import os
from functools import partial
from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.prodManager.ui import settingsUI, defaultSettingsWgtUI, defaultSettingsDialUI


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
        self.treeSwitch = []
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
        self.addWidget('General', self.general)
        self.tasks = Tasks(self)
        self.addWidget('Tasks', self.tasks)
        self.trees = Trees(self)
        self.addWidget('Trees', self.trees)
        self.steps = Steps(self)
        self.addWidget('Steps', self.steps)
        self.tree = Tree(self)
        self.addWidget('Tree Contents', self.tree)

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
        self.log.info("#-- Save Project Settings --#")
        self.pm.project.setParam('rootPath', self.general.getParams())
        self.pm.project.setParam('tasks', self.tasks.getParams())
        self.pm.project.setParam('trees', self.trees.getParams())
        # self.pm.project.setParam('steps', self.trees.getParams())
        self.pm.project.saveSettings()
        self.pbReset.setEnabled(False)

    def closeEvent(self, *args, **kwargs):
        """ Command launched when QPushButton 'Close' is clicked, or dialog is closed """
        self.log.debug("Closing project settings ui ...")


class General(QtGui.QWidget, defaultSettingsWgtUI.Ui_wgSettings):
    """ QWidget class used by 'ProjectSettings' QMainWindow.
        :param settingsUi: Parent window
        :type settingsUi: QtGui.QMainWindow """

    def __init__(self, settingsUi):
        self.settingsUi = settingsUi
        self.pm = self.settingsUi.pm
        self.log = self.settingsUi.log
        super(General, self).__init__()
        self._setupUi()
        self._refresh()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget """
        self.setupUi(self)
        self.setMinimumHeight(100)
        self.setMaximumHeight(100)
        self.cbCurrentTree.setVisible(False)
        self.pbAddItem.setText("Add Root Path")
        self.pbAddItem.clicked.connect(self.on_addRoot)
        self.pbDelItem.setText("Del Root Path")
        self.pbDelItem.clicked.connect(self.on_delRoot)
        self.pbItemUp.clicked.connect(partial(self.on_moveRoot, 'up'))
        self.pbItemDn.clicked.connect(partial(self.on_moveRoot, 'down'))
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

    def _refresh(self):
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

    def on_addRoot(self):
        """ Command launched when QPushButton 'Add Root Path' is clicked """
        rootUi = NewRootUi(self)
        rootUi.exec_()

    def on_delRoot(self):
        """ Command launch when 'Del Item' QPushButton is clicked """
        pQt.delSelItems(self.twTree)
        self.settingsUi.pbReset.setEnabled(True)

    def on_moveRoot(self, side):
        """ Command launch when 'up' or 'down' QPushButton is clicked
            :param side: 'up' or 'down'
            :type side: str """
        selItems = self.twTree.selectedItems()
        if selItems:
            movedItem = pQt.moveSelItem(self.twTree, selItems[0], side)
            if movedItem is not None:
                pQt.deselectAllItems(self.twTree)
                movedItem.setSelected(True)
                self.settingsUi.pbReset.setEnabled(True)

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
    """ QDialog class used by 'General' QWidget. Launch new path edit window
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
                self.pWidget.settingsUi.pbReset.setEnabled(True)
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


class Tasks(QtGui.QWidget, defaultSettingsWgtUI.Ui_wgSettings):
    """ QWidget class used by 'ProjectSettings' QMainWindow.
        :param settingsUi: Parent window
        :type settingsUi: QtGui.QMainWindow """

    def __init__(self, settingsUi):
        self.settingsUi = settingsUi
        self.pm = self.settingsUi.pm
        self.log = self.settingsUi.log
        super(Tasks, self).__init__()
        self._setupUi()
        self._refresh()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget """
        self.setupUi(self)
        self.setMinimumHeight(350)
        self.cbCurrentTree.setVisible(False)
        self.pbAddItem.setText("Add Task")
        self.pbAddItem.clicked.connect(self.on_addTask)
        self.pbDelItem.setText("Del Task")
        self.pbDelItem.clicked.connect(self.on_delTask)
        self.pbItemUp.clicked.connect(partial(self.on_moveTask, 'up'))
        self.pbItemDn.clicked.connect(partial(self.on_moveTask, 'down'))
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

    def _refresh(self):
        """ Refresh task widget """
        self.twTree.clear()
        tasks = self.pm.project.tasks
        if tasks is None:
            tasks = self.defaultTasks
        for n in sorted(tasks.keys()):
            self.addTask(tasks[n]['name'], tasks[n]['label'], color=tasks[n]['color'], stat=tasks[n]['stat'])

    def on_addTask(self):
        """ Command launched when 'Add Task' QPushButton is clicked """
        taskUi = NewTaskUi(self)
        taskUi.exec_()

    def on_delTask(self):
        """ Command launch when 'Del Item' QPushButton is clicked """
        pQt.delSelItems(self.twTree)
        self.settingsUi.pbReset.setEnabled(True)

    def on_moveTask(self, side):
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
                self.settingsUi.pbReset.setEnabled(True)

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
    """ QDialog class used by 'Tasks' QWidget. Launch new task window
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
            self.pWidget.settingsUi.pbReset.setEnabled(True)
            self.log.debug("Task %r successfully added." % label)


class Trees(QtGui.QWidget, defaultSettingsWgtUI.Ui_wgSettings):
    """ Class used by 'ProjectSettings' QMainWindow.
        :param settingsUi: Parent window
        :type settingsUi: QtGui.QMainWindow """

    def __init__(self, settingsUi):
        self.settingsUi = settingsUi
        self.pm = self.settingsUi.pm
        self.log = self.settingsUi.log
        super(Trees, self).__init__()
        self._setupUi()
        self._refresh()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget """
        self.setupUi(self)
        self.cbCurrentTree.setVisible(False)
        self.pbAddItem.setText("Add Tree")
        self.pbAddItem.clicked.connect(self.on_addTree)
        self.pbDelItem.setText("Del Tree")
        self.pbDelItem.clicked.connect(self.on_delTree)
        self.pbItemUp.clicked.connect(partial(self.on_moveTree, 'up'))
        self.pbItemDn.clicked.connect(partial(self.on_moveTree, 'down'))
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
            :rtype: list """
        allItems = pQt.getAllItems(self.twTree)
        trees = {}
        for n, item in enumerate(allItems):
            trees[n] = {}
            trees[n][item.name] = item.type
        return trees

    def _refresh(self):
        """ Refresh tree widget """
        self.twTree.clear()
        trees = self.pm.project.trees
        if trees is None:
            trees = self.defaultTrees
        for n in sorted(trees.keys()):
            treeDict = trees[n]
            treeName = treeDict.keys()[0]
            self.addTree(treeName, treeDict[treeName])

    def rf_allTreeSwitch(self):
        """ Refresh all treeSwitch """
        self.log.debug("refresh all treeSwitch")
        if hasattr(self.settingsUi, 'steps'):
            self.settingsUi.steps.rf_treeSwitch()

    def on_addTree(self):
        """ Command launched when 'Add Task' QPushButton is clicked """
        treeUi = NewTreeUi(self)
        treeUi.exec_()

    def on_delTree(self):
        """ Command launch when 'Del Item' QPushButton is clicked """
        pQt.delSelItems(self.twTree)
        self.settingsUi.pbReset.setEnabled(True)
        self.rf_allTreeSwitch()

    def on_moveTree(self, side):
        """ Command launch when 'up' or 'down' QPushButton is clicked
            :param side: 'up' or 'down'
            :type side: str """
        selItems = self.twTree.selectedItems()
        if selItems:
            movedItem = pQt.moveSelItem(self.twTree, selItems[0], side)
            if movedItem is not None:
                pQt.deselectAllItems(self.twTree)
                movedItem.setSelected(True)
                self.settingsUi.pbReset.setEnabled(True)

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
            self.rf_allTreeSwitch()
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
    """ QDialog class used by 'Tasks' QWidget. Launch new task window
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
            self.pWidget.settingsUi.pbReset.setEnabled(True)
            self.pWidget.rf_allTreeSwitch()
            self.log.debug("Tree %r successfully added." % treeName)


class Steps(QtGui.QWidget, defaultSettingsWgtUI.Ui_wgSettings):

    def __init__(self, settingsUi):
        self.settingsUi = settingsUi
        self.pm = self.settingsUi.pm
        self.log = self.settingsUi.log
        super(Steps, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget """
        self.setupUi(self)
        self.cbCurrentTree.setVisible(True)
        self.pbAddItem.setText("Add Step")
        self.pbDelItem.setText("Del Step")
        self.twTree.setColumnCount(1)
        self.twTree.setHeaderLabels(['Steps'])
        self.twTree.header().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.rf_treeSwitch()
        self._refresh()
        # self.cbCurrentTree.currentIndexChanged.connect(partial(self.on_treeSwitch, freeze=False))

    @property
    def widgetInfo(self):
        """ Widget info printed in settings ui
            :return: Widget info to print
            :rtype: str """
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

    @property
    def currentTree(self):
        """ Get current tree
            :return: Selected tree name
            :rtype: str """
        return str(self.cbCurrentTree.currentText())

    def _refresh(self):
        """ Refresh step widget """
        self.twTree.clear()
        steps = getattr(self.cbCurrentTree, self.currentTree)
        for step in steps:
            newItem = self.newStepItem(step)
            self.twTree.addTopLevelItem(newItem)

    def rf_treeSwitch(self):
        """ Refresh tree switch contents and data """
        trees = self.settingsUi.trees.getParams()
        self.cbCurrentTree.clear()
        for n in sorted(trees.keys()):
            treeName = trees[n].keys()[0]
            treeType = trees[n][treeName]
            self.cbCurrentTree.addItem(treeName)
            steps = self.pm.project.steps
            if steps is None:
                steps = {}
            if not treeName in steps.keys():
                steps[treeName] = self.defaultSteps(treeType)
            setattr(self.cbCurrentTree, treeName, steps[treeName])

    def on_treeSwitch(self, freeze=True):
        if freeze:
            pass
        else:
            self._refresh()

    @staticmethod
    def newStepItem(name):
        newItem = QtGui.QTreeWidgetItem()
        newItem.setText(0, name)
        newItem.name = name
        return newItem


class Tree(QtGui.QWidget, defaultSettingsWgtUI.Ui_wgSettings):

    def __init__(self, settingsUi):
        self.settingsUi = settingsUi
        self.pm = self.settingsUi.pm
        self.log = self.settingsUi.log
        super(Tree, self).__init__()
        self._setupUi()
        self.rf_treeSwitch()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget """
        self.setupUi(self)
        self.cbCurrentTree.setVisible(True)
        self.pbAddItem.setVisible(False)
        self.pbDelItem.setVisible(False)

    @property
    def widgetInfo(self):
        """ Widget info printed in settings ui
            :return: Widget info to print
            :rtype: str """
        return "Project tree: Tree contents."

    @property
    def currentTree(self):
        """ Get current tree
            :return: Selected tree name
            :rtype: str """
        return str(self.cbCurrentTree.currentText())

    def rf_treeSwitch(self):
        """ Refresh tree switch contents and data """
        trees = self.settingsUi.trees.getParams()
        self.cbCurrentTree.clear()
        for n in sorted(trees.keys()):
            self.cbCurrentTree.addItem(trees[n].keys()[0])
            setattr(self.cbCurrentTree, trees[n].keys()[0], [])
