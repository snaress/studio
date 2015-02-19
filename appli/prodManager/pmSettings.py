from functools import partial
from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from appli.prodManager.ui import settingsUI, defaultSettingsWgtUI


class ProjectSettingsUi(QtGui.QMainWindow, settingsUI.Ui_mwSettings):

    def __init__(self, mainUi):
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
        # self.teInfo.clear()

    def rf_projectInfo(self):
        """ Refresh project info """
        self.lNameValue.setText(self.pm.project.name)
        self.lAliasValue.setText(self.pm.project.alias)
        self.lTypeValue.setText(self.pm.project.type)
        if self.pm.project.type is 'Movie':
            self.qfProject_2.setVisible(False)
        else:
            self.qfProject_2.setVisible(True)
            self.lSeason.setText(self.pm.project.season)
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
        self.addWidget('General', General(self))
        self.addWidget('Tasks', Tasks(self))

    def addWidget(self, label, QWidget):
        """ Set andparent given widget
            :param label: Widget label
            :type label: str
            :param QWidget: QWidget to add
            :type QWidget: QtGui.QWidget """
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


class General(QtGui.QWidget, defaultSettingsWgtUI.Ui_wgSettings):

    def __init__(self, settingsUi):
        self.settingsUi = settingsUi
        super(General, self).__init__()
        self._setupUi()

    def _setupUi(self):
        """ Setup widget """
        self.setupUi(self)
        self.setMinimumHeight(100)
        self.setMaximumHeight(100)
        self.pbAddItem.setText("Add Root Path")
        self.pbDelItem.setText("Del RootPath")
        self.twTree.setColumnCount(1)
        self.twTree.setHeaderLabels(['Root Path'])
        self.twTree.header().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)

    @property
    def widgetInfo(self):
        """ Widget info printed in settings ui
            :return: Widget info to print
            :rtype: list """
        return ["ProdManager Root path:",
                "First path in tree will be the project main root path."]

    @property
    def defaultRootPath(self):
        return "D:/prods"


class Tasks(QtGui.QWidget, defaultSettingsWgtUI.Ui_wgSettings):

    def __init__(self, settingsUi):
        self.settingsUi = settingsUi
        super(Tasks, self).__init__()
        self._setupUi()

    def _setupUi(self):
        """ Setup widget """
        self.setupUi(self)
        self.setMinimumHeight(250)
        self.pbAddItem.setText("Add Task")
        self.pbDelItem.setText("Del Task")
        self.twTree.setColumnCount(3)
        self.twTree.setHeaderLabels(['Task', 'Color', 'Stat'])
        self.twTree.header().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.twTree.header().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        self.twTree.header().setResizeMode(2, QtGui.QHeaderView.ResizeToContents)

    @property
    def widgetInfo(self):
        """ Widget info printed in settings ui
            :return: Widget info to print
            :rtype: str """
        return "Project tasks: Tasks avalable for project."

    @property
    def defaultTasks(self):
        """ Default Tasks when creating a new project
            :return: Default tasks data
            :rtype: dict """
        return {0: {'name': "Out", 'color': (0, 0, 0), 'stat': False},
                1: {'name': "StandBy", 'color': (229, 229, 229), 'stat': True},
                2: {'name': "Ready", 'color': (229, 229, 229), 'stat': True},
                3: {'name': "ToDo", 'color': (155, 232, 232), 'stat': True},
                4: {'name': "Retake", 'color': (255, 170, 0), 'stat': True},
                5: {'name': "InProgress", 'color': (255, 255, 0), 'stat': True},
                6: {'name': "Warning", 'color': (255, 0, 0), 'stat': True},
                7: {'name': "WaitApproval", 'color': (255, 85, 255), 'stat': True},
                8: {'name': "Review", 'color': (85, 85, 255), 'stat': True},
                9: {'name': "Approved", 'color': (85, 255, 0), 'stat': True},
                10: {'name': "Final", 'color': (85, 255, 0), 'stat': True}}

    def _refresh(self, tasksDict):
        """ Refresh task widget """
        self.twTree.clear()
        for n in sorted(tasksDict.keys()):
            newItem = self.newTaskItem(tasksDict[n])
            self.twTree.addTopLevelItem(newItem)

    def newTaskItem(self, taskDict):
        """ Cretae new task TreeWidgetItem
            :param taskDict: Task info
            :type taskDict: dict
            :return: New QTreeWidgetItem
            :rtype: QtGui.QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem.setText(0, taskDict['name'])
        for k, v in taskDict.iteritems():
            setattr(newItem, k, v)
        newItem._wgColor = self.newTaskColor(newItem, taskDict['color'])
        return newItem

    def newTaskColor(self, taskItem, taskColor, dialog=True):
        newColor = QtGui.QPushButton()
        newColor.setText('')
        newColor.setMaximumWidth(40)
        if dialog:
            newColor.connect(newColor, QtCore.SIGNAL("clicked()"), partial(self.on_taskColor, taskItem))
        if taskColor is None:
            taskItem.taskColor = (200, 200, 200)
        else:
            taskItem.taskColor = taskColor
            newColor.setStyleSheet("background:rgb(%s, %s, %s)" % (taskColor[0], taskColor[1], taskColor[2]))
        return newColor
