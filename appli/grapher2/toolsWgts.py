import os
from PyQt4 import QtGui, QtCore
from lib.system import procFile as pFile
from appli.grapher2.ui import wgToolsTabUI
from appli.grapher2 import graphWgts as gpWgts


class ToolsBar(QtGui.QTabWidget):

    def __init__(self, **kwargs):
        self.mainUi = kwargs['mainUi']
        self.pWidget = self.mainUi.tbTools
        self.tabs = []
        super(ToolsBar, self).__init__()
        self._setupUi()

    def _setupUi(self):
        self.rf_tabs()
        self.tabOrientation('West')

    def rf_tabs(self):
        self.clear()
        newTab = TabUtil(mainUi=self.mainUi)
        self.insertTab(-1, newTab, 'util')
        self.tabs.append(newTab)

    def tabOrientation(self, orient):
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


class ToolsTab(QtGui.QWidget, wgToolsTabUI.Ui_wgToolsTab):

    def __init__(self, **kwargs):
        self.mainUi = kwargs['mainUi']
        self.graphScene = self.mainUi.graphScene
        super(ToolsTab, self).__init__()
        self.setupUi(self)

    def setOrientation(self, orient):
        if orient == 'horizontal':
            self.saHorizontal.setVisible(True)
            self.saVertical.setVisible(False)
        elif orient == 'vertical':
            self.saHorizontal.setVisible(False)
            self.saVertical.setVisible(True)

    # noinspection PyUnresolvedReferences
    def newTool(self, name, cmd=None, iconFile=None):
        newTools = [QtGui.QPushButton(), QtGui.QPushButton()]
        for tool in newTools:
            tool.setText(name)
            if cmd is not None:
                tool.clicked.connect(cmd)
            if iconFile is not None:
                qIcon = QtGui.QIcon(iconFile)
                tool.setIcon(qIcon)
                tool.setIconSize(QtCore.QSize(24, 24))
        self.hlTools.insertWidget(0, newTools[0])
        self.vlTools.insertWidget(0, newTools[1])


class TabUtil(ToolsTab):

    def __init__(self, **kwargs):
        super(TabUtil, self).__init__(**kwargs)
        self._addTools()

    def _addTools(self):
        self.newTool('CreateMayaNode', cmd=self.createMayaNode, iconFile="icon/toolCreateMayaNode.png")
        self.newTool('CreateAssetNode', cmd=self.createAssetNode, iconFile="icon/toolCreateAssetNode.png")

    def createAssetNode(self):
        print 'new asset'

    def createMayaNode(self):
        iconFile = os.path.join(self.mainUi.iconPath, "baseNode.svg")
        newNode = gpWgts.GraphNode(self.mainUi, iconFile)
        newNode.nodeName = self.graphScene.getNextNameIndex("maya_node")
        newNode.nodeLabel = "Maya Node"
        self.graphScene.addItem(newNode)


