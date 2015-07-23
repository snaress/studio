import os
from functools import partial
from PyQt4 import QtGui, QtSvg, QtCore
from lib.system import procFile as pFile


class GraphZone(QtGui.QGraphicsView):
    """
    Graphic view widget, child of grapher.tagGraph. Contains graphScene
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    :param graphScene: Graph scene
    :type graphScene: QtGui.QGraphicsScene
    """

    def __init__(self, mainUi, graphScene):
        super(GraphZone, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.graphScene = graphScene
        self.graphPath = None
        self._setupUi()

    def _setupUi(self):
        """
        Setup graphZone
        """
        self.log.debug("---> Setup GraphZone ...")
        self.setScene(self.graphScene)
        self.setSceneRect(0, 0, 10000, 10000)
        self.scale(0.5, 0.5)
        self.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemShape)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(60, 60, 60, 255), QtCore.Qt.SolidPattern))

    def loadGraph(self, graphRelPath):
        """
        Load graph from given relative path
        :param graphRelPath: Graph relative path
        :type graphRelPath: str
        """
        self.log.info("Loading Graph %s ..." % graphRelPath)
        graphFullName = pFile.conformPath(os.path.join(self.mainUi.projectPath, graphRelPath))
        graphData = pFile.readPyFile(graphFullName)
        self.createGraphFromData(graphData)
        self.mainUi.tabGraph.setTabText(self.mainUi.tabGraph.currentIndex(),
                                        graphRelPath.replace('graph', '').replace('.py', ''))
        self.graphPath = pFile.conformPath(graphRelPath)

    def saveGraphAs(self, graphFullPath):
        """
        Save graph as given fileName
        :param graphFullPath: Graph file full name
        :type graphFullPath: str
        """
        filePath = "%s.grp.py" % (graphFullPath.split('.')[0])
        sceneDict = self.graphScene.getSceneDict()
        graphTxt = []
        for itemType in ['nodes', 'links']:
            graphTxt.append("%s = %s" % (itemType, sceneDict[itemType]))
        pFile.writeFile(filePath, '\n'.join(graphTxt))

    def createGraphFromData(self, graphData):
        """
        Create graph from given data
        :param graphData: Graph datas
        :type graphData: dict
        """
        self.log.debug("#-- Creating Graph --#")
        #-- Add Nodes --#
        for n in sorted(graphData['nodes'].keys()):
            newNode = self.graphScene.createNode(graphData['nodes'][n]['nodeType'])
            newNode.setPos(graphData['nodes'][n]['nodePosition'][0], graphData['nodes'][n]['nodePosition'][1])
            newNode.setNodeParams(**graphData['nodes'][n])
            newNode.rf_nodeLabel()
            newNode.rf_toolTip()
        #-- Add Links --#
        inPlugs = ['inputFile', 'inputData']
        outPlugs = ['outputFile']
        for n in sorted(graphData['links'].keys()):
            for outPlug in outPlugs:
                for np in sorted(graphData['links'][n][outPlug].keys()):
                    srcId = graphData['links'][n][outPlug][np]['srcId']
                    dstId = graphData['links'][n][outPlug][np]['dstId']
                    srcNode = self.graphScene.getNodeFromNodeId(srcId)
                    srcItem = getattr(srcNode, '%sPlug' % outPlug)
                    dstNode = self.graphScene.getNodeFromNodeId(dstId)
                    if srcNode is not None and dstNode is not None:
                        for inPlug in inPlugs:
                            for npp in sorted(graphData['links'].keys()):
                                if inPlug in graphData['links'][npp].keys():
                                    for nppp in sorted(graphData['links'][npp][inPlug].keys()):
                                        if graphData['links'][npp][inPlug][nppp]['srcId'] == srcId:
                                            dstItem = getattr(dstNode, '%sPlug' % inPlug)
                                            self.graphScene.createLine(srcItem, dstItem)

    # noinspection PyArgumentList,PyCallByClass,PyTypeChecker
    def mouseMoveEvent(self, event):
        """
        Add mouse move options: 'Left': If ctrlKey is True, enable scene drag movement
        """
        if event.y() < 0 or event.y() > self.height() or event.x() < 0 or event.x() > self.width():
            globalPos = self.mapToGlobal(event.pos())
            if event.y() < 0 or event.y() > self.height():
                if event.y() < 0:
                    globalPos.setY(globalPos.y() + self.height())
                else:
                    globalPos.setY(globalPos.y() - self.height())
            else:
                if event.x() < 0:
                    globalPos.setX(globalPos.x() + self.width())
                else:
                    globalPos.setX(globalPos.x() - self.width())
            r_event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonRelease, self.mapFromGlobal(QtGui.QCursor.pos()),
                                        QtCore.Qt.LeftButton, QtCore.Qt.NoButton, QtCore.Qt.NoModifier)
            self.mouseReleaseEvent(r_event)
            QtGui.QCursor.setPos(globalPos)
            p_event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonPress, self.mapFromGlobal(QtGui.QCursor.pos()),
                                        QtCore.Qt.LeftButton, QtCore.Qt.LeftButton, QtCore.Qt.NoModifier)
            QtCore.QTimer.singleShot(0, lambda: self.mousePressEvent(p_event))
        else:
            super(GraphZone, self).mouseMoveEvent(event)

    def wheelEvent(self, event):
        """
        Scale graph view (zoom fit)
        """
        factor = 1.41 ** ((event.delta()*.5) / 240.0)
        self.scale(factor, factor)

    def resizeEvent(self, event):
        """
        Resize graph view (widget size)
        """
        self.graphScene.setSceneRect(0, 0, self.width(), self.height())


class GraphScene(QtGui.QGraphicsScene):
    """
    Graphic scene widget, child of grapher.graphZone. Contains graphNodes
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        super(GraphScene, self).__init__()
        self.mainUi = mainUi
        self.dataTree = self.mainUi.twNodeData
        self.log = self.mainUi.log
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup graphScene
        """
        self.log.debug("---> Setup GraphScene ...")
        self.line = None
        self.selBuffer = {'_order': []}
        self.ctrlKey = False
        self.treeItemDragged = None
        self.selectionChanged.connect(self._selectionChanged)

    def _selectionChanged(self):
        """
        Store node selection order
        """
        selNodes = self.getSelectedNodes()
        if not selNodes:
            self.selBuffer = {'_order': []}
        else:
            for n, item in enumerate(selNodes):
                if not item.nodeName in self.selBuffer['_order']:
                    self.selBuffer['_order'].append(item.nodeName)
                    self.selBuffer[item.nodeName] = item

    def getAllNodes(self):
        """
        Get all graphScene nodes (_type=='nodeBase')
        :return: GraphScene nodes
        :rtype: list
        """
        items = []
        for item in self.items():
            if hasattr(item, '_type'):
                if item._type == "nodeBase":
                    items.append(item)
        return items

    def getAllLines(self):
        """
        Get all graphScene nodeLink
        :return: GraphScene nodeLink
        :rtype: list
        """
        lines = []
        for item in self.items():
            if hasattr(item, '_type'):
                if item._type == 'nodeLink':
                    lines.append(item)
        return lines

    def getSelectedNodes(self):
        """
        Get selected graphScene nodes (_type=='nodeBase')
        :return: Selected graphScene nodes
        :rtype: list
        """
        items = []
        for item in self.selectedItems():
            if hasattr(item, '_type'):
                if item._type == "nodeBase":
                    items.append(item)
        return items

    def getSelectedNodesArea(self):
        """
        Get selected nodes bbox
        :return: Bounding box region (posX, posY, width, height)
        :rtype: (float, float, float, float)
        """
        nodes = self.getSelectedNodes()
        posX = []
        posY = []
        if len(nodes) > 1:
            for node in nodes:
                posX.append(node.pos().x())
                posY.append(node.pos().y())
        return QtCore.QRectF(min(posX), min(posY), (max(posX) - min(posX)), (max(posY) - min(posY)))

    def getNodeFromNodeName(self, nodeName):
        """
        Get graphNode item from given nodeName
        :param nodeName: Node label
        :type nodeName: str
        :return: Node matching with given nodeName
        :rtype: GraphNode
        """
        for node in self.getAllNodes():
            if node.nodeName == nodeName:
                return node

    def getNodeFromNodeId(self, nodeId):
        """
        Get graphNode item from given nodeName
        :param nodeId: Node id
        :type nodeId: str
        :return: Node matching with given nodeName
        :rtype: GraphNode
        """
        for node in self.getAllNodes():
            if node.nodeId == nodeId:
                return node

    def getNextNameIndex(self, name):
        """
        Get next free nodeName index
        :param name: Node name
        :type name: str
        :return: Clean name with extension
        :rtype: str
        """
        indList = []
        checkName = name
        if name.split('_')[-1].isdigit():
            checkName = '_'.join(name.split('_')[:-1])
        for item in self.getAllNodes():
            if item.nodeName.startswith(checkName):
                indList.append(int(item.nodeName.split('_')[-1]))
        if not indList:
            ind = "1"
        else:
            ind = str(max(indList) + 1)
        return "%s_%s" % (name, ind)

    def getSceneDict(self):
        """
        Get scene contents
        :return: Scene nodes and links
        :rtype: dict
        """
        sceneDict = {'nodes':{}, 'links': {}}
        for n, node in enumerate(self.getAllNodes()):
            sceneDict['nodes'][n] = node.getNodeParams()
            sceneDict['links'][n] = node.getConnectionsInfo()
        return sceneDict

    def clearNodeSelection(self):
        """
        Unselect all graph nodes
        """
        for node in self.getSelectedNodes():
            node.setSelected(False)

    def rf_nodesElementId(self):
        """
        Refresh graph nodes element id
        """
        for node in self.getAllNodes():
            if node._type == "nodeBase":
                if node.isSelected():
                    node.setElementId("selected")
                else:
                    node.setElementId("regular")

    def rf_connections(self):
        """
        Refresh graphScene connections line
        """
        self.log.debug("Refresh Graph Connections ...")
        cList = []
        for line in self.getAllLines():
            cList.append({'src': line.startItem, 'dst': line.endItem})
            line.deleteLine()
        for c in cList:
            if self.mainUi.editMode:
                self.createLine(c['src'], c['dst'])
            else:
                self.createLine(c['src'], c['dst'])

    def _drawLine(self):
        """
        Draw connection line
        """
        if self.line:
            #-- Tmp Line --#
            startItems = self.items(self.line.line().p1())
            if len(startItems) and startItems[0] == self.line:
                startItems.pop(0)
            endItems = self.items(self.line.line().p2())
            if len(endItems) and endItems[0] == self.line:
                endItems.pop(0)
            self.removeItem(self.line)
            #-- Draw Line --#
            if startItems and endItems:
                if hasattr(startItems[0], '_type') and hasattr(endItems[0], '_type'):
                    if startItems[0]._type == 'nodePlug' and endItems[0]._type == 'nodePlug':
                        if not startItems[0].isInputConnection and endItems[0].isInputConnection:
                            if self.mainUi.editMode:
                                self.createLine(startItems[0], endItems[0])
        self.line = None

    def createNode(self, nodeType):
        """
        Create given nodeType graphNode
        :param nodeType: GraphNode type
        :type nodeType: str
        :return: New graphNode
        :rtype: GraphNode
        """
        if nodeType == 'assetCastingNode':
            return self.mainUi.graphTools.tabUtil.assetCastingNode()
        elif nodeType == 'assetNode':
            return self.mainUi.graphTools.tabUtil.assetNode()
        elif nodeType == 'mayaNode':
            return self.mainUi.graphTools.tabUtil.mayaNode()
        elif nodeType == 'dataNode':
            return self.mainUi.graphTools.tabUtil.dataNode()

    def createLine(self, startItem, endItem):
        """
        Create connection line
        :param startItem: Start node connectionItem
        :type startItem: QtSvg.QGraphicsSvgItem
        :param endItem: End node connectionItem
        :type endItem: QtSvg.QGraphicsSvgItem
        """
        self.log.debug("Creating line: %s ---> %s ..." % (startItem._parent.nodeName, endItem._parent.nodeName))
        connectionLine = LinkConnection(self.mainUi, startItem, endItem)
        startItem.connections.append(connectionLine)
        endItem.connections.append(connectionLine)
        self.addItem(connectionLine)
        connectionLine.updatePosition()

    def dropFromTree(self, event):
        """
        Drop selected project tree item
        :param event: Mouse release rvent
        :type event: QtGui.QGraphicsSceneMouseEvent
        """
        if self.treeItemDragged is not None:
            if event.button() == QtCore.Qt.LeftButton:
                ext = self.treeItemDragged.itemName.split('.')[-1]
                if ext in ['cst']:
                    self.dropTreeNode(ext, event)
                elif ext in ['grp']:
                    self.mainUi.currentGraphZone.loadGraph(self.treeItemDragged.relPath)
            elif event.button() == QtCore.Qt.RightButton:
                self.log.debug("Tree drag canceled")
        self.treeItemDragged = None

    def dropTreeNode(self, ext, event):
        """
        Drop Selected tree item node to graphScene
        :param ext: Node type extension ('cst', 'a7')
        :type ext: str
        :param event: Mouse release rvent
        :type event: QtGui.QGraphicsSceneMouseEvent
        """
        #-- Create Node --#
        if ext == 'cst':
            newNode = self.createNode('assetCastingNode')
        else:
            newNode = None
        #-- Add Node Datas --#
        if newNode is not None:
            newNode.loadDatas(self.treeItemDragged.relPath)
            newNode.setPos(QtCore.QPointF(event.scenePos().x(), event.scenePos().y()))
        else:
            self.log.debug("Tree drag canceled")

    def keyPressEvent(self, event):
        """
        Add key press options: 'Delete' = Delete selected nodes or lines
                               'Control' = Store state for move options
        """
        if event.key() == QtCore.Qt.Key_Delete:
            if self.mainUi.editMode:
                for item in self.selectedItems():
                    if item._type == 'nodeLink':
                        item.deleteLine()
                    else:
                        item.deleteNode()
        elif event.key() == QtCore.Qt.Key_Control:
            self.ctrlKey = True

    def keyReleaseEvent(self, event):
        """
        Add key release options: 'Control' = Clear state storage
        """
        if event.key() == QtCore.Qt.Key_Control:
            self.ctrlKey = False

    def mousePressEvent(self, event):
        """
        Add mouse press options: 'Left' = - If itemType is 'nodePlug', store start position
                                            for line creation
                                          - If itemType is 'nodeBase', will connect node data to dataZone
                                          - If empty, will clear dataZone and update node.elementId
                                          - If empty and ctrlKey is False: Enable area selection
                                          - If empty and ctrlKey is True: Enable move by drag
        """
        self.mainUi.dataZone.clearDataZone()
        item = self.itemAt(event.scenePos())
        if item is not None and hasattr(item, '_type'):
            #-- Create Line --#
            if event.button() == QtCore.Qt.LeftButton and item._type == 'nodePlug':
                if self.mainUi.editMode:
                    self.line = QtGui.QGraphicsLineItem(QtCore.QLineF(event.scenePos(), event.scenePos()))
                    self.addItem(self.line)
            #-- Connect Node To DataZone --#
            elif event.button() == QtCore.Qt.LeftButton and item._type == 'nodeBase':
                self.mainUi.dataZone.connectNodeData(item)
            #-- Node Popup Menu --#
            elif event.button() == QtCore.Qt.RightButton and item._type == 'nodeBase':
                item._popupMenu()
        #-- Enable Area Selection Or Moving Scene --#
        elif item is None and not self.ctrlKey:
            self.mainUi.currentGraphZone.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        elif item is None and self.ctrlKey:
            self.mainUi.currentGraphZone.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
        super(GraphScene, self).mousePressEvent(event)
        #-- Check Node ElementId State --#
        self.rf_nodesElementId()

    def mouseMoveEvent(self, event):
        """
        Add mouse move options: 'left' = If line construction is detected, will draw the line
                                         and update endPoint position
        """
        if self.line:
            newLine = QtCore.QLineF(self.line.line().p1(), event.scenePos())
            self.line.setLine(newLine)
        super(GraphScene, self).mouseMoveEvent(event)
        self.update()

    def mouseReleaseEvent(self, event):
        """
        Add mouse release options: 'left' = If line construction is detected, will draw the final connection
                                            and clear construction line item.
                                            If treeItemDragged is not None, drop selected tree item in graphScene
        """
        self._drawLine()
        self.mainUi.currentGraphZone.setDragMode(QtGui.QGraphicsView.NoDrag)
        self.dropFromTree(event)
        for item in self.selectedItems():
            if item._type == 'nodeBase':
                item.setElementId("selected")
        super(GraphScene, self).mouseReleaseEvent(event)


class GraphNode(QtSvg.QGraphicsSvgItem):
    """
    Graphic svg item, child of grapher.graphScene. Contains node params and datas
    :param kwargs: Graph node dict (mainUi, nodeName, nodeId)
    :type kwargs: dict
    """

    _type = "nodeBase"

    def __init__(self, **kwargs):
        self.mainUi = kwargs['mainUi']
        self.log = self.mainUi.log
        self.dataTree = self.mainUi.twNodeData
        self.nodeId = kwargs['nodeId']
        self.nodeName = kwargs['nodeName']
        self.nodeEnabled = True
        super(GraphNode, self).__init__(self.iconFile)
        self.defaultBrush = QtGui.QPen()
        self._setupUi()

    @property
    def _menuFont(self):
        """
        Create node popup menu font
        :return: Menu font
        :rtype: QtGui.QFont
        """
        menuFont = QtGui.QFont()
        menuFont.setPixelSize(12)
        menuFont.setBold(True)
        return menuFont

    @property
    def _menuItemFont(self):
        """
        Create node popup menu item font
        :return: Menu item font
        :rtype: QtGui.QFont
        """
        menuItemFont = QtGui.QFont()
        menuItemFont.setPixelSize(11)
        return menuItemFont

    def _setupUi(self):
        """
        Setup svg graph node
        """
        self.defaultBrush.setWidth(2)
        self.defaultBrush.setColor(QtCore.Qt.white)
        self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable|
                      QtGui.QGraphicsItem.ItemIsMovable|
                      QtGui.QGraphicsItem.ItemIsFocusable)
        self.setCachingEnabled(False)
        self.setAcceptHoverEvents(True)
        self.setElementId("regular")
        self.rf_toolTip()
        self.addLabelNode()
        self.addConnectionPlugs()

    def _popupMenu(self):
        """
        Setup graph node popup menu
        """
        self.nodeMenu = QtGui.QMenu()
        self.nodeMenu.setFont(self._menuFont)
        # noinspection PyArgumentList
        self.nodeMenu.popup(QtGui.QCursor.pos())
        #-- Menu Launch --#
        if self.hasLaunchCmd:
            self.menuLaunch = QtGui.QMenu('Launch Node')
            self.menuLaunch.setFont(self._menuItemFont)
            self.miLaunch = self.menuLaunch.addAction('Launch')
            self.miLaunch.triggered.connect(self.on_launchNode)
            self.nodeMenu.addMenu(self.menuLaunch)
        #-- Menu Exec --#
        if self.hasLaunchCmd:
            self.menuExec = QtGui.QMenu('Exec Node')
            self.menuExec.setFont(self._menuItemFont)
            self.miExecLocal = self.menuExec.addAction('Local')
            self.miExecLocal.triggered.connect(partial(self.on_execNode, 'Local'))
            self.miExecFarm = self.menuExec.addAction('Farm')
            self.miExecFarm.triggered.connect(partial(self.on_execNode, 'Farm'))
            self.nodeMenu.addMenu(self.menuExec)
        #-- Exec --#
        self.nodeMenu.exec_()

    @property
    def nodeSize(self):
        """
        get graph node size
        :return: Node size (width, height)
        :rtype: (int, int)
        """
        size = (self.boundingRect().width(), self.boundingRect().height())
        return size

    @property
    def width(self):
        """
        get graph node width
        :return: Node width
        :rtype: int
        """
        return self.nodeSize[0]

    @property
    def height(self):
        """
        get graph node height
        :return: Node height
        :rtype: int
        """
        return self.nodeSize[1]

    def getNodeParams(self):
        """
        Get Node params and datas
        :return: Node params
        :rtype: dict
        """
        params = {'nodeType': self.nodeType, 'nodeName': self.nodeName, 'nodeId': self.nodeId,
                  'nodePosition': (self.scenePos().x(), self.scenePos().y())}
        for k in self.dataKeys:
            params[k] = getattr(self, k)
        return params

    def setNodeParams(self, **kwargs):
        """
        Set node params and datas
        :param kwargs: params and datas to set
        :type kwargs: dict
        """
        excludedKey = ['nodePosition', 'nodeType']
        for k, v in kwargs.iteritems():
            if not k in excludedKey:
                setattr(self, k, v)

    def getConnections(self):
        """
        Get graph node connections
        :return: Node connections
        :rtype: dict
        """
        cDict = {}
        if self.hasInputFilePlug:
            cDict['inputFile'] = {}
            for n, line  in enumerate(self.inputFilePlug.connections):
                cDict['inputFile'][n] = {}
                cDict['inputFile'][n]['line'] = line
                cDict['inputFile'][n]['srcItem'] = line.startItem
                cDict['inputFile'][n]['srcNode'] = line.startNode
                cDict['inputFile'][n]['dstItem'] = line.endItem
                cDict['inputFile'][n]['dstNode'] = line.endNode
        if self.hasInputDataPlug:
            cDict['inputData'] = {}
            for n, line  in enumerate(self.inputDataPlug.connections):
                cDict['inputData'][n] = {}
                cDict['inputData'][n]['line'] = line
                cDict['inputData'][n]['srcItem'] = line.startItem
                cDict['inputData'][n]['srcNode'] = line.startNode
                cDict['inputData'][n]['dstItem'] = line.endItem
                cDict['inputData'][n]['dstNode'] = line.endNode
        if self.hasOutputFilePlug:
            cDict['outputFile'] = {}
            for n, line  in enumerate(self.outputFilePlug.connections):
                cDict['outputFile'][n] = {}
                cDict['outputFile'][n]['line'] = line
                cDict['outputFile'][n]['srcItem'] = line.startItem
                cDict['outputFile'][n]['srcNode'] = line.startNode
                cDict['outputFile'][n]['dstItem'] = line.endItem
                cDict['outputFile'][n]['dstNode'] = line.endNode
        return cDict

    def getConnectionsInfo(self):
        """
        Get graph node connections readable info
        :return: Node connections info
        :rtype: dict
        """
        rDict = {}
        cDict = self.getConnections()
        for conn in sorted(cDict.keys()):
            rDict[conn] = {}
            for n in sorted(cDict[conn].keys()):
                rDict[conn][n] = {}
                for k, v in cDict[conn][n].iteritems():
                    if k == 'line':
                        rDict[conn][n][k] = v._type
                    elif k.endswith('Node'):
                        rDict[conn][n][k] = v.nodeName
                        rDict[conn][n][k.replace('Node', 'Id')] = v.nodeId
        return rDict

    def rf_toolTip(self):
        """
        Refresh node toolTip
        """
        self.setToolTip("Name = %s\nId = %s" % (self.nodeName, self.nodeId))

    def rf_nodeLabel(self):
        """
        Refresh label nodeText
        """
        self.nodeTextLabel.setPlainText(self.nodeName)

    def addLabelNode(self):
        """
        Add graph node label item
        """
        font = QtGui.QFont("SansSerif", 14)
        font.setStyleHint(QtGui.QFont.Helvetica)
        self.nodeTextLabel = QtGui.QGraphicsTextItem(self.nodeName, self)
        self.nodeTextLabel.setFont(font)
        self.nodeTextLabel.setDefaultTextColor(QtGui.QColor(QtCore.Qt.white))
        self.nodeTextLabel.setPos(0, self.height)

    def addConnectionPlugs(self):
        """
        Add graph node connections plug
        """
        if self.hasInputFilePlug:
            self.inputFilePlug = NodeConnection(mainUi=self.mainUi, nodeType='inputFilePlug',
                                                iconFile="gui/icon/svg/inputFilePlug.svg", parent=self)
            self.inputFilePlug.setPos(0 - self.inputFilePlug.width, - (self.inputFilePlug.height / 2))
            self.inputFilePlug.isInputConnection = True
        if self.hasInputDataPlug:
            self.inputDataPlug = NodeConnection(mainUi=self.mainUi, nodeType='inputDataPlug',
                                                iconFile="gui/icon/svg/inputDataPlug.svg", parent=self)
            self.inputDataPlug.setPos(0 - self.inputDataPlug.width, self.height - (self.inputDataPlug.height / 2))
            self.inputDataPlug.isInputConnection = True
        if self.hasOutputFilePlug:
            self.outputFilePlug = NodeConnection(mainUi=self.mainUi, nodeType='outputFilePlug',
                                                 iconFile="gui/icon/svg/outputFilePlug.svg", parent=self)
            self.outputFilePlug.setPos(self.width, (self.height / 2) - (self.outputFilePlug.height / 2))
            self.outputFilePlug.isInputConnection = False

    def loadDatas(self, dataRelPath):
        """
        Load data from grapher file
        :param dataRelPath: Node data file relative path
        :type dataRelPath: str
        """
        self.log.info("Loading %s" % dataRelPath)
        dataFile = os.path.join(self.mainUi.projectPath, dataRelPath)
        datas = pFile.readPyFile(dataFile)
        for data in self.dataKeys:
            setattr(self, data, datas[data])
        self.nodeName = "%s_cst" % self.assetName
        self.rf_nodeLabel()
        self.rf_toolTip()

    def deleteNode(self):
        """
        Delete graph node and connected lines
        """
        self.log.debug("Deleting node: %s ..." % self.nodeName)
        #-- Delete Connections --#
        cDict = self.getConnections()
        for conn in sorted(cDict.keys()):
            if cDict[conn].keys():
                for n in sorted(cDict[conn].keys()):
                    for k, v in cDict[conn][n].iteritems():
                        if k == 'line':
                            v.deleteLine()
        #-- Delete Node --#
        self.log.debug("Deleting node ...")
        self.scene().removeItem(self)

    def on_launchNode(self):
        """
        Command launched when 'Launch'
        :return:
        """
        self.launch()

    def on_execNode(self, execMethod='Local'):
        """
        Command launched when 'Exec Node' ('Local' or 'Farm') popupMenuItem is triggered.
        Execute node 'batchCmd'.
        :param execMethod: 'Local' or 'Farm'
        :type execMethod: str
        """
        if execMethod == 'Local':
            self.log.info("Exec node: %s ---> Local" % self.nodeName)
            self.batch()
        else:
            self.log.info("Exec node: %s ---> Farm" % self.nodeName)
            # ToDo

    def hoverMoveEvent(self, event):
        """
        Add hover move options: Change node style
        """
        self.setElementId("hover")

    def hoverLeaveEvent(self, event):
        """
        Add hover leave options: Change node style
        """
        if self.isSelected():
            self.setElementId("selected")
        else:
            self.setElementId("regular")


class NodeConnection(QtSvg.QGraphicsSvgItem):
    """
    Graphic svg item, child of graphNode. Contains graphNode connections
    :param kwargs: Graph node dict (mainUi, iconFile, nodeType, parent)
    :type kwargs: dict
    """

    _type = "nodePlug"

    def __init__(self, **kwargs):
        self.mainUi = kwargs['mainUi']
        self.iconFile = kwargs['iconFile']
        self.nodeType = kwargs['nodeType']
        self._parent = kwargs['parent']
        super(NodeConnection, self).__init__(self.iconFile, self._parent)
        self.connections = []
        self.isInputConnection = False
        self._setupUi()

    def _setupUi(self):
        """
        Setup svg graph node connections plug
        """
        self.setAcceptHoverEvents(True)
        self.setElementId("regular")

    @property
    def nodeSize(self):
        """
        get graph node plug size
        :return: Node plug size (width, height)
        :rtype: (int, int)
        """
        size = (self.boundingRect().width(), self.boundingRect().height())
        return size

    @property
    def width(self):
        """
        get graph node plug width
        :return: Node plug width
        :rtype: int
        """
        return self.nodeSize[0]

    @property
    def height(self):
        """
        get graph node plug height
        :return: Node plug height
        :rtype: int
        """
        return self.nodeSize[1]

    def hoverMoveEvent(self,event):
        """
        Add hover move options: Change node style
        """
        self.setElementId("hover")

    def hoverLeaveEvent(self, event):
        """
        Add hover leave options: Change node style
        """
        self.setElementId("regular")

    def mouseReleaseEvent(self, event):
        """
        Add mouse release options: Change node style
        """
        self.setElementId("regular")


class LinkConnection(QtGui.QGraphicsPathItem):
    """
    Graphic link item, child of grapher.graphScene. Contains link connection
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    :param startItem: Start node connection plug
    :type startItem: QtSvg.QGraphicsSvgItem
    :param endItem: End node connection plug
    :type endItem: QtSvg.QGraphicsSvgItem
    """

    _type = 'nodeLink'

    def __init__(self, mainUi, startItem, endItem):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        super(LinkConnection, self).__init__()
        self.startItem = startItem
        self.endItem = endItem
        self.lineColor = QtCore.Qt.cyan
        self.setZValue(-1.0)
        self.setFlags(QtGui.QGraphicsPathItem.ItemIsSelectable|QtGui.QGraphicsPathItem.ItemIsFocusable)
        self.setPen(QtGui.QPen(self.lineColor, 1.5, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))

    @property
    def startNode(self):
        """
        Get start graph node (_type='nodeBase')
        :return: Start node
        :rtype: QtSvg.QGraphicsSvgItem
        """
        return self.startItem._parent

    @property
    def endNode(self):
        """
        Get end graph node (_type='nodeBase')
        :return: end node
        :rtype: QtSvg.QGraphicsSvgItem
        """
        return self.endItem._parent

    def getLine(self):
        """
        Get link coords
        :return: Line coords
        :rtype: QtCore.QLineF
        """
        p1 = self.startItem.sceneBoundingRect().center()
        p2 = self.endItem.sceneBoundingRect().center()
        return QtCore.QLineF(self.mapFromScene(p1), self.mapFromScene(p2))

    def getCenterPoint(self):
        """
        Get link center point
        :return: Link center point
        :rtype: QtCore.QPointF
        """
        line = self.getLine()
        centerX = (line.p1().x() + line.p2().x()) / 2
        centerY = (line.p1().y() + line.p2().y()) / 2
        return QtCore.QPointF(centerX, centerY)

    def updatePosition(self):
        """
        Update link position
        """
        self.setPath(self.createPath())

    def deleteLine(self):
        """
        Delete link and remove connections plug storage
        """
        self.log.debug("Deleting line: %s ---> %s ..." % (self.startItem._parent.nodeName,
                                                          self.endItem._parent.nodeName))
        if self in self.startItem.connections:
            self.startItem.connections.remove(self)
        if self in self.endItem.connections:
            self.endItem.connections.remove(self)
        try:
            self.scene().removeItem(self)
        except:
            pass

    def boundingRect(self):
        """
        Calculate line bounding rect
        :return: Line bounding rect
        :rtype: QtCore.QRectF
        """
        extra = (self.pen().width() + 100) / 2.0
        line = self.getLine()
        p1 = line.p1()
        p2 = line.p2()
        return QtCore.QRectF(p1, QtCore.QSizeF(p2.x()-p1.x(), p2.y()-p1.y())).normalized().adjusted(-extra,-extra,extra,extra)

    def createPath(self):
        """
        Calculate link angle
        :return: Link path
        :rtype: QtGui.QPainterPath
        """
        line = self.getLine()
        centerPoint = self.getCenterPoint()
        coef = QtCore.QPointF(abs(centerPoint.x() - line.p1().x()), 0)
        control_1 = line.p1() + coef
        control_2 = line.p2() - coef
        path = QtGui.QPainterPath(line.p1())
        path.cubicTo(control_1, control_2, line.p2())
        return path

    def paint(self, painter, option, widget=None):
        """
        Draw line connection
        """
        myPen = self.pen()
        myPen.setColor(self.lineColor)
        if self.isSelected():
            painter.setBrush(QtCore.Qt.yellow)
            myPen.setColor(QtCore.Qt.yellow)
            myPen.setStyle(QtCore.Qt.DashLine)
        else:
            if self.mainUi.editMode:
                painter.setBrush(QtCore.Qt.lightGray)
                myPen.setColor(QtCore.Qt.lightGray)
            else:
                if self.getLine().p1().x() >= self.getLine().p2().x():
                    painter.setBrush(QtCore.Qt.red)
                    myPen.setColor(QtCore.Qt.red)
        painter.strokePath(self.createPath(), myPen)
