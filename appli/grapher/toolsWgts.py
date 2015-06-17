import random
from PyQt4 import QtGui, QtCore
from appli.grapher.ui import wgToolsTabUI
from appli.grapher import graphNodes


class ToolsBar(QtGui.QTabWidget):

    def __init__(self, **kwargs):
        super(ToolsBar, self).__init__()
        self.mainUi = kwargs['mainUi']
        self.log = self.mainUi.log
        self.pWidget = self.mainUi.tbTools
        self.tabs = []
        self._setupUi()

    def _setupUi(self):
        self.log.debug("---> Setup Tools Bar ...")
        self.addTabs()
        self.tabOrientation('West')

    def addTabs(self):
        self.clear()
        #-- Tab Mode --#
        tabMode = TabMode(mainUi=self.mainUi)
        self.insertTab(-1, tabMode, 'Mode')
        self.tabs.append(tabMode)
        #-- Tab Util --#
        tabUtil = TabUtil(mainUi=self.mainUi)
        self.insertTab(-1, tabUtil, 'Util')
        self.tabs.append(tabUtil)

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
        super(ToolsTab, self).__init__()
        self.mainUi = kwargs['mainUi']
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


class TabMode(ToolsTab):

    def __init__(self, **kwargs):
        super(TabMode, self).__init__(**kwargs)
        self._addTools()

    def _addTools(self):
        self.newTool('createModelingGraph', cmd=self.createModelingGraph, iconFile=None)

    def createModelingGraph(self):
        pass


class TabUtil(ToolsTab):

    def __init__(self, **kwargs):
        super(TabUtil, self).__init__(**kwargs)
        self._addTools()

    def _addTools(self):
        self.newTool('CreateSvgNode', cmd=self.createSvgNode, iconFile=None)
        self.newTool('CreateMayaNode', cmd=self.createMayaNode, iconFile="icon/toolCreateMayaNode.png")
        self.newTool('CreateAssetNode', cmd=self.createAssetNode, iconFile="icon/toolCreateAssetNode.png")

    def createAssetNode(self):
        nodeName = self.mainUi.currentGraphScene.getNextNameIndex("asset_node")
        newNode = graphNodes.AssetNode(mainUi=self.mainUi, nodeName=nodeName)
        newNode.setPos(random.randrange(200, 400), random.randrange(200, 400))
        self.mainUi.currentGraphScene.addItem(newNode)

    def createMayaNode(self):
        nodeName = self.mainUi.currentGraphScene.getNextNameIndex("maya_node")
        newNode = graphNodes.MayaNode(mainUi=self.mainUi, nodeName=nodeName)
        newNode.setPos(random.randrange(200, 400), random.randrange(200, 400))
        self.mainUi.currentGraphScene.addItem(newNode)

    def createSvgNode(self):
        nodeName = self.mainUi.currentGraphScene.getNextNameIndex("svg_node")
        newNode = graphNodes.SvgNode(mainUi=self.mainUi, nodeName=nodeName)
        newNode.setPos(random.randrange(200, 400), random.randrange(200, 400))
        self.mainUi.currentGraphScene.addItem(newNode)
