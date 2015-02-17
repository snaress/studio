from functools import partial
from PyQt4 import QtGui, QtCore
from appli.prodManager.ui import settingsUI, defaultSettingsWgtUI


class ProjectSettingsUi(QtGui.QMainWindow, settingsUI.Ui_mwSettings):

    def __init__(self, newProject=False):
        self.newProject = newProject
        super(ProjectSettingsUi, self).__init__()
        self._setupUi()

    def _setupUi(self):
        """ Setup main ui """
        self.setupUi(self)
        self.leProjectRootPath.setText("D:/prods")
        if self.newProject:
            self.qfSettings.setEnabled(False)
        else:
            self.qfNewProject.setEnabled(False)
        self.addWidgets()

    def addWidgets(self):
        """ Parent all settings widget to ui """
        self.addGeneralWidget()
        self.addTasksWidget()

    def addGeneralWidget(self):
        newItem = self.newSettingsItem("General")
        self.twSettings.addTopLevelItem(newItem)
        self.wgGeneral = General()
        self.vlSettings.insertWidget(0, self.wgGeneral)

    def addTasksWidget(self):
        """ Add 'Tasks' widget """
        newItem = self.newSettingsItem("Tasks")
        self.twSettings.addTopLevelItem(newItem)
        self.wgTasks = Tasks(self)
        self.vlSettings.insertWidget(0, self.wgTasks)

    @staticmethod
    def newSettingsItem(label):
        newItem = QtGui.QTreeWidgetItem()
        newItem.setText(0, label)
        return newItem


class General(QtGui.QWidget, defaultSettingsWgtUI.Ui_wgSettings):

    def __init__(self):
        super(General, self).__init__()
        self._setupUi()

    def _setupUi(self):
        """ Setup widget """
        self.setupUi(self)

    @property
    def defaultRootPath(self):
        return "D:/prods"


class Tasks(QtGui.QWidget, defaultSettingsWgtUI.Ui_wgSettings):

    def __init__(self, pWidget):
        self.pWidget = pWidget
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
        if self.pWidget.newProject:
            self._refresh(self.defaultTasks)

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
        self.twTree.clear()
        for n in sorted(tasksDict.keys()):
            newItem = self.newTaskItem(tasksDict[n])
            self.twTree.addTopLevelItem(newItem)

    def newTaskItem(self, taskDict):
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
        # if dialog:
        #     newColor.connect(newColor, QtCore.SIGNAL("clicked()"), partial(self.on_taskColor, taskItem))
        if taskColor is None:
            taskItem.taskColor = (200, 200, 200)
        else:
            taskItem.taskColor = taskColor
            newColor.setStyleSheet("background:rgb(%s, %s, %s)" % (taskColor[0], taskColor[1], taskColor[2]))
        return newColor