import random, time
from PyQt4 import QtGui, QtCore
from appli.grapher.gui.ui import wgToolsTabUI
from appli.grapher.template import graphNodes


class ToolsBar(QtGui.QTabWidget):
    """
    Grapher tools tab
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        super(ToolsBar, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.pWidget = self.mainUi.tbTools
        self.tabs = []
        self.tools = []
        self._setupUi()

    def _setupUi(self):
        """
        Setup tools tab
        """
        self.log.debug("---> Setup Tools Bar ...")
        self.addTabs()
        self.tabOrientation('West')

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
            if self.mainUi.miButtonIconOnly.isChecked():
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
        #-- Tab Mode --#
        self.tabMode = TabMode(self.mainUi, self)
        self.insertTab(-1, self.tabMode, 'Mode')
        self.tabs.append(self.tabMode)
        #-- Tab Util --#
        self.tabUtil = TabUtil(self.mainUi, self)
        self.insertTab(-1, self.tabUtil, 'Util')
        self.tabs.append(self.tabUtil)


class ToolsTab(QtGui.QWidget, wgToolsTabUI.Ui_wgToolsTab):
    """
    Grapher tools tab widget
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    :param tabWidget: Parent tabWidget
    :type tabWidget: QtGui.QTabWidget
    """

    def __init__(self, mainUi, tabWidget):
        super(ToolsTab, self).__init__()
        self.mainUi = mainUi
        self.tabWidget = tabWidget
        self.log = self.mainUi.log
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
        if self.mainUi.miButtonIconOnly.isChecked():
            self.saVertical.setMinimumWidth(40)
            self.saVertical.setMaximumWidth(40)
        else:
            self.saVertical.setMinimumWidth(150)
            self.saVertical.setMaximumWidth(150)

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


class TabMode(ToolsTab):
    """
    Modeling tool tab template
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    :param tabWidget: Parent tabWidget
    :type tabWidget: QtGui.QTabWidget
    """

    def __init__(self, mainUi, tabWidget):
        super(TabMode, self).__init__(mainUi, tabWidget)
        self._addTools()

    def _addTools(self):
        """
        Add tools to tab
        """
        self.newTool('ModeCharsGraph', cmd=self.modeCharsGraph, iconFile="gui/icon/png/toolModeCharsBranch.png")

    def modeCharsGraph(self):
        pass


class TabUtil(ToolsTab):
    """
    Util tool tab template
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    :param tabWidget: Parent tabWidget
    :type tabWidget: QtGui.QTabWidget
    """

    def __init__(self, mainUi, tabWidget):
        self.mainUi = mainUi
        super(TabUtil, self).__init__(mainUi, tabWidget)
        self._addTools()

    def _addTools(self):
        """
        Add tools to tab
        """
        self.newTool('DataNode', cmd=self.dataNode, iconFile="gui/icon/png/toolDataNode.png")
        self.newTool('MayaNode', cmd=self.mayaNode, iconFile="gui/icon/png/toolMayaNode.png")
        self.newTool('AssetNode', cmd=self.assetNode, iconFile="gui/icon/png/toolAssetNode.png")
        self.newTool('AssetCastingNode', cmd=self.assetCastingNode, iconFile="gui/icon/png/toolAssetCastingNode.png")

    def assetCastingNode(self):
        """
        Add tool: Create Asset Casting Node
        :return: Graph node
        :rtype: AssetCastingNode
        """
        nodeName = self.mainUi.currentGraphScene.getNextNameIndex("asset_casting_node")
        nodeId = time.time()
        self.log.info("#-- Creating Casting Asset Node: %s --#" % nodeName)
        newNode = graphNodes.AssetCastingNode(mainUi=self.mainUi, nodeName=nodeName, nodeId=nodeId)
        newNode.setPos(random.randrange(200, 400), random.randrange(200, 400))
        self.mainUi.currentGraphScene.addItem(newNode)
        return newNode

    def assetNode(self):
        """
        Add tool: Create Asset Node
        :return: Graph node
        :rtype: AssetNode
        """
        nodeName = self.mainUi.currentGraphScene.getNextNameIndex("asset_node")
        nodeId = time.time()
        self.mainUi.log.info("#-- Creating Asset Node: %s --#" % nodeName)
        newNode = graphNodes.AssetNode(mainUi=self.mainUi, nodeName=nodeName, nodeId=nodeId)
        newNode.setPos(random.randrange(200, 400), random.randrange(200, 400))
        self.mainUi.currentGraphScene.addItem(newNode)
        return newNode

    def mayaNode(self):
        """
        Add tool: Create Maya Node
        :return: Graph node
        :rtype: MayaNode
        """
        nodeName = self.mainUi.currentGraphScene.getNextNameIndex("maya_node")
        nodeId = time.time()
        self.log.info("#-- Creating Maya Node: %s --#" % nodeName)
        newNode = graphNodes.MayaNode(mainUi=self.mainUi, nodeName=nodeName, nodeId=nodeId)
        newNode.setPos(random.randrange(200, 400), random.randrange(200, 400))
        self.mainUi.currentGraphScene.addItem(newNode)
        return newNode

    def dataNode(self):
        """
        Add tool: Create Maya Node
        :return: Graph node
        :rtype: DataNode
        """
        nodeName = self.mainUi.currentGraphScene.getNextNameIndex("data_node")
        nodeId = time.time()
        self.log.info("#-- Creating Maya Node: %s --#" % nodeName)
        newNode = graphNodes.DataNode(mainUi=self.mainUi, nodeName=nodeName, nodeId=nodeId)
        newNode.setPos(random.randrange(200, 400), random.randrange(200, 400))
        self.mainUi.currentGraphScene.addItem(newNode)
        return newNode
