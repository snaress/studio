import random
from PyQt4 import QtGui, QtCore
from appli.grapher.gui.ui import wgToolsTabUI
from appli.grapher.template import graphNodes


class ToolsBar(QtGui.QTabWidget):
    """ Grapher tools tab
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        super(ToolsBar, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.pWidget = self.mainUi.tbTools
        self.tabs = []
        self._setupUi()

    def _setupUi(self):
        """ Setup tools tab """
        self.log.debug("---> Setup Tools Bar ...")
        self.addTabs()
        self.tabOrientation('West')

    def tabOrientation(self, orient):
        """ Edit tools tab orientation
            :param orient: 'North', 'South', 'West', 'East'
            :type orient: str """
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

    def addTabs(self):
        """ Add tools tab """
        self.clear()
        #-- Tab Mode --#
        tabMode = TabMode(mainUi=self.mainUi)
        self.insertTab(-1, tabMode, 'Mode')
        self.tabs.append(tabMode)
        #-- Tab Util --#
        tabUtil = TabUtil(mainUi=self.mainUi)
        self.insertTab(-1, tabUtil, 'Util')
        self.tabs.append(tabUtil)


class ToolsTab(QtGui.QWidget, wgToolsTabUI.Ui_wgToolsTab):
    """ Grapher tools tab widget
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        super(ToolsTab, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.setupUi(self)

    def setOrientation(self, orient):
        """ Edit tools orientation
            :param orient: 'horizontal' or 'vertical'
            :type orient: str """
        if orient == 'horizontal':
            self.saHorizontal.setVisible(True)
            self.saVertical.setVisible(False)
        elif orient == 'vertical':
            self.saHorizontal.setVisible(False)
            self.saVertical.setVisible(True)

    # noinspection PyUnresolvedReferences
    def newTool(self, name, cmd=None, iconFile=None):
        """ Add tool to tab
            :param name: Tool button name
            :type name: str
            :param cmd: Tool button command
            :type cmd: object
            :param iconFile: Tool button iconfile
            :type iconFile: str | None """
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
    """ Modeling tool tab template
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        super(TabMode, self).__init__(mainUi)
        self._addTools()

    def _addTools(self):
        """ Add tools to tab """
        self.newTool('createModelingGraph', cmd=self.createModelingGraph, iconFile=None)

    def createModelingGraph(self):
        pass


class TabUtil(ToolsTab):
    """ Util tool tab template
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        super(TabUtil, self).__init__(mainUi)
        self._addTools()

    def _addTools(self):
        """ Add tools to tab """
        self.newTool('CreateSvgNode', cmd=self.createSvgNode, iconFile=None)
        self.newTool('CreateMayaNode', cmd=self.createMayaNode, iconFile="gui/icon/png/toolCreateMayaNode.png")
        self.newTool('CreateAssetNode', cmd=self.createAssetNode, iconFile="gui/icon/png/toolCreateAssetNode.png")

    def createAssetNode(self):
        """ Add tool: Create Asset Node """
        nodeName = self.mainUi.currentGraphScene.getNextNameIndex("asset_node")
        self.log.info("#-- Creating Asset Node: %s --#" % nodeName)
        newNode = graphNodes.AssetNode(mainUi=self.mainUi, nodeName=nodeName)
        newNode.setPos(random.randrange(200, 400), random.randrange(200, 400))
        self.mainUi.currentGraphScene.addItem(newNode)

    def createMayaNode(self):
        """ Add tool: Create Maya Node """
        nodeName = self.mainUi.currentGraphScene.getNextNameIndex("maya_node")
        self.log.info("#-- Creating Maya Node: %s --#" % nodeName)
        newNode = graphNodes.MayaNode(mainUi=self.mainUi, nodeName=nodeName)
        newNode.setPos(random.randrange(200, 400), random.randrange(200, 400))
        self.mainUi.currentGraphScene.addItem(newNode)

    def createSvgNode(self):
        """ Add tool: Create Svg Node """
        nodeName = self.mainUi.currentGraphScene.getNextNameIndex("svg_node")
        self.log.info("#-- Creating Svg Node: %s --#" % nodeName)
        newNode = graphNodes.SvgNode(mainUi=self.mainUi, nodeName=nodeName)
        newNode.setPos(random.randrange(200, 400), random.randrange(200, 400))
        self.mainUi.currentGraphScene.addItem(newNode)
