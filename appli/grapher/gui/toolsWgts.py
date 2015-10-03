import os
from functools import partial
from PyQt4 import QtGui, QtCore
from appli.grapher.gui.ui import toolsTabUI


class GraphTools(QtGui.QTabWidget):
    """
    Fondation tools tab widget, child of GrapherUi

    :param mainUi: Fondation main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        super(GraphTools, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphTools Widget.")
        self._pWidget = self.mainUi.tbTools
        self.tabs = []
        self.tools = []
        self._setupWidget()

    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphTools Widget.")
        self.addTabs()
        self.tabOrientation('West')
        self.toolsAspect()

    def tabOrientation(self, orient):
        """
        Edit tools tab orientation

        :param orient: 'North', 'South', 'West', 'East'
        :type orient: str
        """
        if orient == 'North':
            self.setTabPosition(QtGui.QTabWidget.North)
        elif orient == 'South':
            self.setTabPosition(QtGui.QTabWidget.South)
        elif orient == 'West':
            self.setTabPosition(QtGui.QTabWidget.West)
        elif orient == 'East':
            self.setTabPosition(QtGui.QTabWidget.East)
        for tab in self.tabs:
            if orient in ['North', 'South']:
                tab.setOrientation('horizontal')
            elif orient in ['West', 'East']:
                tab.setOrientation('vertical')

    def toolsAspect(self):
        """
        Edit tools button aspect
        """
        for tab in self.tabs:
            tab.rf_size()
        for tool in self.tools:
            if self.mainUi.toolsIconOnly:
                tool.setText("")
                tool.setToolTip(tool.name)
            else:
                tool.setText(tool.name)
                tool.setToolTip("")

    def addTabs(self):
        """
        Add tools tab
        """
        self.clear()
        #-- Tab Util --#
        self.tabUtil = TabUtil(self.mainUi, self)
        self.insertTab(-1, self.tabUtil, 'Util')
        self.tabs.append(self.tabUtil)


class ToolsTab(QtGui.QWidget, toolsTabUI.Ui_wgToolsTab):
    """
    Fondation tools tab widget, child of GrapherUi.GraphTools

    :param mainUi: Fondation main window
    :type mainUi: QtGui.QMainWindow
    :param tabWidget: Parent tabWidget
    :type tabWidget: QtGui.QTabWidget
    """

    def __init__(self, mainUi, tabWidget):
        super(ToolsTab, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphTools TabWidget.")
        self.iconPath = self.mainUi.iconPath
        self.tabWidget = tabWidget
        self.log = self.mainUi.log
        self._setupWidget()

    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphTools TabWidget.")
        self.setupUi(self)

    def setOrientation(self, orient):
        """
        Edit tools orientation

        :param orient: 'horizontal' or 'vertical'
        :type orient: str
        """
        if orient == 'horizontal':
            self.saHorizontal.setVisible(True)
            self.saVertical.setVisible(False)
        elif orient == 'vertical':
            self.saHorizontal.setVisible(False)
            self.saVertical.setVisible(True)

    def rf_size(self):
        """
        refresh toolBar size
        """
        if self.mainUi.toolsIconOnly:
            self.saVertical.setMinimumWidth(40)
            self.saVertical.setMaximumWidth(40)
        else:
            self.saVertical.setMinimumWidth(125)
            self.saVertical.setMaximumWidth(125)

    # noinspection PyUnresolvedReferences
    def newTool(self, name, cmd=None, iconFile=None):
        """
        Add tool to tab

        :param name: Tool button name
        :type name: str
        :param cmd: Tool button command
        :type cmd: object
        :param iconFile: Tool button iconfile
        :type iconFile: str | None
        """
        newTools = [QtGui.QPushButton(), QtGui.QPushButton()]
        for tool in newTools:
            tool.setText(name)
            tool.name = name
            if cmd is not None:
                tool.clicked.connect(cmd)
            if iconFile is not None:
                qIcon = QtGui.QIcon(iconFile)
                tool.setIcon(qIcon)
                tool.setIconSize(QtCore.QSize(24, 24))
        self.hlTools.insertWidget(0, newTools[0])
        self.vlTools.insertWidget(0, newTools[1])
        self.tabWidget.tools.extend(newTools)


class TabUtil(ToolsTab):
    """
    Util tool tab template, GrapherUi.GraphTools.ToolsTab

    :param mainUi: Fondation main window
    :type mainUi: QtGui.QMainWindow
    :param tabWidget: Parent tabWidget
    :type tabWidget: QtGui.QTabWidget
    """

    def __init__(self, mainUi, tabWidget):
        super(TabUtil, self).__init__(mainUi, tabWidget)
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphTools UtilTab.")
        self._setupTab()

    def _setupTab(self):
        self.log.debug("\t ---> Setup 'Util' Tab.")
        self.log.detail("\t\t ---> Add tool 'PurData'.")
        self.newTool('Loop', cmd=partial(self.mainUi.graphZone.on_miNewNode, 'loop'),
                             iconFile=os.path.join(self.iconPath, 'png', 'loop.png'))
        self.newTool('PurData', cmd=partial(self.mainUi.graphZone.on_miNewNode, 'purData'),
                               iconFile=os.path.join(self.iconPath, 'png', 'purData.png'))
        self.log.detail("\t\t ---> Add tool 'CmdData'.")
        self.newTool('CmdData', cmd=partial(self.mainUi.graphZone.on_miNewNode, 'cmdData'),
                                iconFile=os.path.join(self.iconPath, 'png', 'cmdData.png'))
        self.log.detail("\t\t ---> Add tool 'SysData'.")
        self.newTool('SysData', cmd=partial(self.mainUi.graphZone.on_miNewNode, 'sysData'),
                                iconFile=os.path.join(self.iconPath, 'png', 'sysData.png'))
        self.log.detail("\t\t ---> Add tool 'Modul'.")
        self.newTool('Modul', cmd=partial(self.mainUi.graphZone.on_miNewNode, 'modul'),
                              iconFile=os.path.join(self.iconPath, 'png', 'modul.png'))
