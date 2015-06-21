import random
from PyQt4 import QtGui, QtCore
from appli.grapher.gui.ui import wgToolsTabUI
from appli.grapher.template import graphNodes


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
        self.log.info("#-- Creating Asset Node: %s --#" % nodeName, newLinesBefor=1)
        newNode = graphNodes.AssetNode(mainUi=self.mainUi, nodeName=nodeName)
        newNode.setPos(random.randrange(200, 400), random.randrange(200, 400))
        self.mainUi.currentGraphScene.addItem(newNode)

    def createMayaNode(self):
        """ Add tool: Create Maya Node """
        nodeName = self.mainUi.currentGraphScene.getNextNameIndex("maya_node")
        self.log.info("#-- Creating Maya Node: %s --#" % nodeName, newLinesBefor=1)
        newNode = graphNodes.MayaNode(mainUi=self.mainUi, nodeName=nodeName)
        newNode.setPos(random.randrange(200, 400), random.randrange(200, 400))
        self.mainUi.currentGraphScene.addItem(newNode)

    def createSvgNode(self):
        """ Add tool: Create Svg Node """
        nodeName = self.mainUi.currentGraphScene.getNextNameIndex("svg_node")
        self.log.info("#-- Creating Svg Node: %s --#" % nodeName, newLinesBefor=1)
        newNode = graphNodes.SvgNode(mainUi=self.mainUi, nodeName=nodeName)
        newNode.setPos(random.randrange(200, 400), random.randrange(200, 400))
        self.mainUi.currentGraphScene.addItem(newNode)
