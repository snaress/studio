import math
from lib.qt import procQt as pQt
from PyQt4 import QtGui, QtSvg, QtCore


class GraphZone(QtGui.QGraphicsView):
    """ Graphic view widget, child of grapher.tagGraph. Contains graphScene
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow
        :param graphScene: Graph scene
        :type graphScene: QtGui.QGraphicsScene """

    def __init__(self, mainUi, graphScene):
        super(GraphZone, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.graphScene = graphScene
        self.ctrlKey = False
        self._setupUi()

    def _setupUi(self):
        """ Setup graphZone """
        self.log.debug("---> Setup GraphZone ...")
        self.setScene(self.graphScene)
        self.setSceneRect(0, 0, 10000, 10000)
        self.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemShape)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(60, 60, 60, 255), QtCore.Qt.SolidPattern))

    def wheelEvent(self, event):
        """ Scale graph view (zoom fit) """
        factor = 1.41 ** ((event.delta()*.5) / 240.0)
        self.scale(factor, factor)

    def resizeEvent(self, event):
        """ Resize graph view (widget size) """
        self.graphScene.setSceneRect(0, 0, self.width(), self.height())


class GraphScene(QtGui.QGraphicsScene):
    """ Graphic scene widget, child of grapher.graphZone. Contains graphNodes
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        super(GraphScene, self).__init__()
        self.mainUi = mainUi
        self.dataTree = self.mainUi.twNodeData
        self.log = self.mainUi.log
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup graphScene """
        self.log.debug("---> Setup GraphScene ...")
        self.line = None
        self.selBuffer = {'_order': []}
        self.selectionChanged.connect(self._selectionChanged)

    def _selectionChanged(self):
        """ Store node selection order """
        selNodes = self.getSelectedNodes()
        if not selNodes:
            self.selBuffer = {'_order': []}
        else:
            for n, item in enumerate(selNodes):
                if not item.nodeName in self.selBuffer['_order']:
                    self.selBuffer['_order'].append(item.nodeName)
                    self.selBuffer[item.nodeName] = item

    def getAllNodes(self):
        """ Get all graphScene nodes (_type=='nodeBase')
            :return: GraphScene nodes
            :rtype: list """
        items = []
        for item in self.items():
            if hasattr(item, '_type'):
                if item._type == "nodeBase":
                    items.append(item)
        return items

    def getAllLines(self):
        """ Get all graphScene lines (_type in ['lineConnection', 'linkConnection'])
            :return: GraphScene lines
            :rtype: list """
        lines = []
        for item in self.items():
            if hasattr(item, '_type'):
                if item._type in ['lineConnection', 'linkConnection']:
                    lines.append(item)
        return lines

    def getSelectedNodes(self):
        """ Get selected graphScene nodes (_type=='nodeBase')
            :return: Selected graphScene nodes
            :rtype: list """
        items = []
        for item in self.selectedItems():
            if hasattr(item, '_type'):
                if item._type == "nodeBase":
                    items.append(item)
        return items

    def getSelectedNodesArea(self):
        """ Get selected nodes bbox
            :return: Bounding box region (minX, maxX, minY, maxY)
            :rtype: (int, int, int, int) """
        nodes = self.getSelectedNodes()
        posX = []
        posY = []
        for node in nodes:
            posX.append(node.pos().x())
            posY.append(node.pos().y())
        return min(posX), max(posX), min(posY), max(posY)

    def getNextNameIndex(self, name):
        """ Get next free nodeName index
            :param name: Node name
            :type name: str
            :return: Clean name with extension
            :rtype: str """
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

    def clearNodeSelection(self):
        """ Unselect all graph nodes """
        for node in self.getSelectedNodes():
            node.setSelected(False)

    def rf_nodesElementId(self):
        """ Refresh graph nodes element id """
        for node in self.getAllNodes():
            if node._type == "nodeBase":
                if node.isSelected():
                    node.setElementId("selected")
                else:
                    node.setElementId("regular")

    def rf_connections(self):
        """ Refresh graphScene connections line """
        self.log.debug("Refresh Graph Connections ...")
        cList = []
        for line in self.getAllLines():
            cList.append({'src': line.startItem, 'dst': line.endItem})
            line.deleteLine()
        for c in cList:
            if self.mainUi.editMode:
                self.createLine(c['src'], c['dst'], lineType='line')
            else:
                self.createLine(c['src'], c['dst'], lineType='link')

    def createLine(self, startItem, endItem, lineType='line'):
        """ Create connection line
            :param startItem: Start node connectionItem
            :type startItem: QtSvg.QGraphicsSvgItem
            :param endItem: End node connectionItem
            :type endItem: QtSvg.QGraphicsSvgItem
            :param lineType: Connection line type ('line' or 'link')
            :type lineType: str """
        self.log.debug("Creating line: %s ---> %s ..." % (startItem._parent.nodeName, endItem._parent.nodeName))
        if lineType == 'line':
            connectionLine = LineConnection(self.mainUi, startItem, endItem)
        else:
            connectionLine = LinkConnection(self.mainUi, startItem, endItem)
        startItem.connections.append(connectionLine)
        endItem.connections.append(connectionLine)
        self.addItem(connectionLine)
        connectionLine.updatePosition()

    def keyPressEvent(self, event):
        """ Add key press options: 'Delete' = Delete selected nodes or lines
                                   'Control' = Draw selection region """
        if event.key() == QtCore.Qt.Key_Delete:
            if self.mainUi.editMode:
                for item in self.selectedItems():
                    if item._type == 'lineConnection':
                        item.deleteLine()
                    else:
                        item.deleteNode()
        if event.key() == QtCore.Qt.Key_Control:
            self.mainUi.currentGraphZone.setDragMode(QtGui.QGraphicsView.RubberBandDrag)

    def keyReleaseEvent(self, event):
        """ Add key release options: 'Control' = Select nodes and lines in selection area """
        if event.key() == QtCore.Qt.Key_Control:
            self.mainUi.currentGraphZone.setDragMode(QtGui.QGraphicsView.NoDrag)
            for item in self.selectedItems():
                if item._type == 'nodeBase':
                    item.setElementId("selected")

    def mousePressEvent(self, event):
        """ Add mouse press options: 'Left' = - If itemType is 'nodeConnection', store start position
                                                for line creation
                                              - If itemType is 'nodeBase', will connect node data to dataZone
                                              - If empty, will clear dataZone and update node.elementId """
        item = self.itemAt(event.scenePos())
        if item is not None and hasattr(item, '_type'):
            if event.button() == QtCore.Qt.LeftButton and item._type == 'nodeConnection':
                if self.mainUi.editMode:
                    self.line = QtGui.QGraphicsLineItem(QtCore.QLineF(event.scenePos(), event.scenePos()))
                    self.addItem(self.line)
            elif event.button() == QtCore.Qt.LeftButton and item._type == 'nodeBase':
                item.connectNodeData()
        else:
            groups = pQt.getTopItems(self.dataTree)
            for grpItem in groups:
                dataItem = grpItem.child(0)._widget
                dataItem.clearData()
        super(GraphScene, self).mousePressEvent(event)
        #-- Check Node ElementId State --#
        self.rf_nodesElementId()

    def mouseMoveEvent(self, event):
        """ Add mouse move options: 'left' = If line construction is detected, will draw the line
                                             and update endPoint position """
        if self.line:
            newLine = QtCore.QLineF(self.line.line().p1(), event.scenePos())
            self.line.setLine(newLine)
        super(GraphScene, self).mouseMoveEvent(event)
        self.update()

    def mouseReleaseEvent(self, event):
        """ Add mouse release options: 'left' = If line construction is detected, will draw the final connection
                                                and clear construction line item """
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
                    if startItems[0]._type == 'nodeConnection' and endItems[0]._type == 'nodeConnection':
                        if not startItems[0].isInputConnection and endItems[0].isInputConnection:
                            if self.mainUi.editMode:
                                self.createLine(startItems[0], endItems[0], lineType='line')
        self.line = None
        super(GraphScene, self).mouseReleaseEvent(event)


class GraphNode(QtSvg.QGraphicsSvgItem):
    """ Graphic svg item, child of grapher.graphScene. Contains node params and datas
        :param kwargs: Graph node dict (mainUi, nodeName, nodeLabel)
        :type kwargs: dict """

    def __init__(self, **kwargs):
        self.mainUi = kwargs['mainUi']
        self.log = self.mainUi.log
        self.dataTree = self.mainUi.twNodeData
        self._type = "nodeBase"
        self.nodeName = kwargs['nodeName']
        if not 'nodeLabel' in kwargs.keys():
            self.nodeLabel = self.nodeName
        else:
            self.nodeLabel = kwargs['nodeLabel']
        super(GraphNode, self).__init__(self.iconFile)
        self.defaultBrush = QtGui.QPen()
        self._setupUi()

    def _setupUi(self):
        """ Setup svg graph node """
        self.defaultBrush.setWidth(2)
        self.defaultBrush.setColor(QtCore.Qt.white)
        self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable|
                      QtGui.QGraphicsItem.ItemIsMovable|
                      QtGui.QGraphicsItem.ItemIsFocusable)
        self.setCachingEnabled(False)
        self.setAcceptHoverEvents(True)
        self.setElementId("regular")
        self.setToolTip("Name = %s\nLabel = %s" % (self.nodeName, self.nodeLabel))
        self.addLabelNode()
        self.addConnectionNodes()

    @property
    def nodeSize(self):
        """ get graph node size
            :return: Node size (width, height)
            :rtype: (int, int) """
        size = (self.boundingRect().width(), self.boundingRect().height())
        return size

    @property
    def width(self):
        """ get graph node width
            :return: Node width
            :rtype: int """
        return self.nodeSize[0]

    @property
    def height(self):
        """ get graph node height
            :return: Node height
            :rtype: int """
        return self.nodeSize[1]

    def getConnections(self):
        """ Get graph node connections
            :return: Node connections
            :rtype: dict """
        cDict = {}
        if self.hasInputFileConnection:
            cDict['inputFile'] = {}
            for n, line  in enumerate(self.inputFileConnection.connections):
                cDict['inputFile'][n] = {}
                cDict['inputFile'][n]['line'] = line
                cDict['inputFile'][n]['srcItem'] = line.startItem
                cDict['inputFile'][n]['srcNode'] = line.startNode
                cDict['inputFile'][n]['dstItem'] = line.endItem
                cDict['inputFile'][n]['dstNode'] = line.endNode
        if self.hasInputDataConnection:
            cDict['inputData'] = {}
            for n, line  in enumerate(self.inputDataConnection.connections):
                cDict['inputData'][n] = {}
                cDict['inputData'][n]['line'] = line
                cDict['inputData'][n]['srcItem'] = line.startItem
                cDict['inputData'][n]['srcNode'] = line.startNode
                cDict['inputData'][n]['dstItem'] = line.endItem
                cDict['inputData'][n]['dstNode'] = line.endNode
        if self.hasOutputFileConnection:
            cDict['outputFile'] = {}
            for n, line  in enumerate(self.outputFileConnection.connections):
                cDict['outputFile'][n] = {}
                cDict['outputFile'][n]['line'] = line
                cDict['outputFile'][n]['srcItem'] = line.startItem
                cDict['outputFile'][n]['srcNode'] = line.startNode
                cDict['outputFile'][n]['dstItem'] = line.endItem
                cDict['outputFile'][n]['dstNode'] = line.endNode
        return cDict

    def getConnectionsInfo(self):
        """ Get graph node connections readable info
            :return: Node connections info
            :rtype: dict """
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
        return rDict

    def addLabelNode(self):
        """ Add graph node label item """
        font = QtGui.QFont("SansSerif", 14)
        font.setStyleHint(QtGui.QFont.Helvetica)
        self.nodeTextLabel = QtGui.QGraphicsTextItem(self.nodeLabel, self)
        self.nodeTextLabel.setFont(font)
        self.nodeTextLabel.setDefaultTextColor(QtGui.QColor(QtCore.Qt.white))
        self.nodeTextLabel.setPos(0, self.height)

    def addConnectionNodes(self):
        """ Add graph node connections plug """
        if self.hasInputFileConnection:
            self.inputFileConnection = NodeConnection(mainUi=self.mainUi, nodeType='inputFileConnection',
                                                      iconFile="gui/icon/svg/inputFileConnNode.svg", parent=self)
            self.inputFileConnection.setPos(0 - self.inputFileConnection.width,
                                            - (self.inputFileConnection.height / 2))
            self.inputFileConnection.isInputConnection = True
        if self.hasInputDataConnection:
            self.inputDataConnection = NodeConnection(mainUi=self.mainUi, nodeType='inputDataConnection',
                                                      iconFile="gui/icon/svg/inputDataConnNode.svg", parent=self)
            self.inputDataConnection.setPos(0 - self.inputDataConnection.width,
                                            self.height - (self.inputDataConnection.height / 2))
            self.inputDataConnection.isInputConnection = True
        if self.hasOutputFileConnection:
            self.outputFileConnection = NodeConnection(mainUi=self.mainUi, nodeType='outputFileConnection',
                                                      iconFile="gui/icon/svg/outputFileConnNode.svg", parent=self)
            self.outputFileConnection.setPos(self.width, (self.height / 2) - (self.outputFileConnection.height / 2))
            self.outputFileConnection.isInputConnection = False

    def deleteNode(self):
        """ Delete graph node and connected lines """
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

    def connectNodeData(self):
        """ Connect graph node data to dataZone """
        self.log.debug("Connecting node data: %s ..." % self.nodeName)
        groups = pQt.getTopItems(self.dataTree)
        for grpItem in groups:
            dataItem = grpItem.child(0)._widget
            dataItem.setDataFromNode(self)

    def hoverMoveEvent(self, event):
        """ Add hover move options: Change node style """
        self.setElementId("hover")

    def hoverLeaveEvent(self, event):
        """ Add hover leave options: Change node style """
        if self.isSelected():
            self.setElementId("selected")
        else:
            self.setElementId("regular")


class NodeConnection(QtSvg.QGraphicsSvgItem):
    """ Graphic svg item, child of graphNode. Contains graphNode connections
        :param kwargs: Graph node dict (mainUi, iconFile, nodeType, parent)
        :type kwargs: dict """

    def __init__(self, **kwargs):
        self.mainUi = kwargs['mainUi']
        self.iconFile = kwargs['iconFile']
        self._type = "nodeConnection"
        self.nodeType = kwargs['nodeType']
        self._parent = kwargs['parent']
        super(NodeConnection, self).__init__(self.iconFile, self._parent)
        self.connections = []
        self.isInputConnection = False
        self._setupUi()

    def _setupUi(self):
        """ Setup svg graph node connections plug """
        self.setAcceptHoverEvents(True)
        self.setElementId("regular")

    @property
    def nodeSize(self):
        """ get graph node plug size
            :return: Node plug size (width, height)
            :rtype: (int, int) """
        size = (self.boundingRect().width(), self.boundingRect().height())
        return size

    @property
    def width(self):
        """ get graph node plug width
            :return: Node plug width
            :rtype: int """
        return self.nodeSize[0]

    @property
    def height(self):
        """ get graph node plug height
            :return: Node plug height
            :rtype: int """
        return self.nodeSize[1]

    def hoverMoveEvent(self,event):
        """ Add hover move options: Change node style """
        self.setElementId("hover")

    def hoverLeaveEvent(self, event):
        """ Add hover leave options: Change node style """
        self.setElementId("regular")

    def mouseReleaseEvent(self, event):
        """ Add mouse release options: Change node style """
        self.setElementId("regular")


class LineConnection(QtGui.QGraphicsLineItem):
    """ Graphic line item, child of grapher.graphScene. Contains line connection
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow
        :param startItem: Start node connection plug
        :type startItem: QtSvg.QGraphicsSvgItem
        :param endItem: End node connection plug
        :type endItem: QtSvg.QGraphicsSvgItem """

    def __init__(self, mainUi, startItem, endItem):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        super(LineConnection, self).__init__()
        self.startItem = startItem
        self.endItem = endItem
        self._type = 'lineConnection'
        self.lineColor = QtCore.Qt.black
        self.arrowHead = QtGui.QPolygonF()
        self.setZValue(-1.0)
        self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable|QtGui.QGraphicsItem.ItemIsFocusable)
        self.setPen(QtGui.QPen(self.lineColor, 2, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))

    @property
    def startNode(self):
        """ Get start graph node (_type='nodeBase')
            :return: Start node
            :rtype: QtSvg.QGraphicsSvgItem """
        return self.startItem._parent

    @property
    def endNode(self):
        """ Get end graph node (_type='nodeBase')
            :return: End node
            :rtype: QtSvg.QGraphicsSvgItem """
        return self.endItem._parent

    def getLine(self):
        """ Get line coords
            :return: Line coords
            :rtype: QtCore.QLineF """
        p1 = self.startItem.sceneBoundingRect().center()
        p2 = self.endItem.sceneBoundingRect().center()
        return QtCore.QLineF(self.mapFromScene(p1), self.mapFromScene(p2))

    def getCenterPoint(self):
        """ Get line center point
            :return: Line center point
            :rtype: QtCore.QPointF """
        line = self.getLine()
        centerX = (line.p1().x() + line.p2().x()) / 2
        centerY = (line.p1().y() + line.p2().y()) / 2
        return QtCore.QPointF(centerX, centerY)

    def updatePosition(self):
        """ Update line position """
        self.setLine(self.getLine())

    def deleteLine(self):
        """ Delete line and remove connections plug storage """
        self.log.debug("Deleting line: %s ---> %s ..." % (self.startItem._parent.nodeName,
                                                         self.endItem._parent.nodeName))
        self.startItem.connections.remove(self)
        self.endItem.connections.remove(self)
        self.scene().removeItem(self)

    def _arrowHeadCalculation(self, line):
        """ Calculate and update arrow orientation
            :param line: Connection line point position
            :type line: QtCore.QLineF """
        arrowSize = 20.0
        try:
            angle = math.acos(line.dx() / line.length())
        except ZeroDivisionError:
            angle = 0
        if line.dy() >= 0:
            angle = (math.pi * 2.0) - angle
        #-- Arrow Direction --#
        if self.startItem.isInputConnection:
            revArrow = 1
        else:
            revArrow = -1
        #-- Arrow Points --#
        centerPoint = self.getCenterPoint()
        arrowP1 = centerPoint + QtCore.QPointF(math.sin(angle + math.pi / 3.0) * arrowSize * revArrow,
                                               math.cos(angle + math.pi / 3) * arrowSize * revArrow)
        arrowP2 = centerPoint + QtCore.QPointF(math.sin(angle + math.pi - math.pi / 3.0) * arrowSize * revArrow,
                                               math.cos(angle + math.pi - math.pi / 3.0) * arrowSize * revArrow)
        #-- Clear arrowHead --#
        self.arrowHead.clear()
        #-- ArrowHead Polygon --#
        for point in [centerPoint, arrowP1, arrowP2]:
            self.arrowHead.append(point)

    def boundingRect(self):
        """ Calculate line bounding rect
            :return: Line bounding rect
            :rtype: QtCore.QRectF """
        extra = (self.pen().width() + 100) / 2.0
        line = self.getLine()
        p1 = line.p1()
        p2 = line.p2()
        return QtCore.QRectF(p1, QtCore.QSizeF(p2.x()-p1.x(), p2.y()-p1.y())).normalized().adjusted(-extra,-extra,extra,extra)

    def shape(self):
        """ Line shape with arrow
            :return: Line shape
            :rtype: QtGui.QPainterPath """
        path = super(LineConnection, self).shape()
        path.addPolygon(self.arrowHead)
        return path

    def paint(self, painter, option, widget=None):
        """ Draw line connection """
        line = self.getLine()
        painter.setBrush(self.lineColor)
        myPen = self.pen()
        myPen.setColor(self.lineColor)
        #-- Selected Color --#
        if self.isSelected():
            painter.setBrush(QtCore.Qt.yellow)
            myPen.setColor(QtCore.Qt.yellow)
            myPen.setStyle(QtCore.Qt.DashLine)
        painter.setPen(myPen)
        #-- Calculating Angle --#
        if line.length() > 0.0:
            self._arrowHeadCalculation(line)
            #-- Draw Line --#
            if line:
                painter.drawPolygon(self.arrowHead)
                painter.drawLine(line)


class LinkConnection(QtGui.QGraphicsPathItem):
    """ Graphic link item, child of grapher.graphScene. Contains link connection
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow
        :param startItem: Start node connection plug
        :type startItem: QtSvg.QGraphicsSvgItem
        :param endItem: End node connection plug
        :type endItem: QtSvg.QGraphicsSvgItem """

    def __init__(self, mainUi, startItem, endItem):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        super(LinkConnection, self).__init__()
        self.startItem = startItem
        self.endItem = endItem
        self._type = 'linkConnection'
        self.lineColor = QtCore.Qt.cyan
        self.setZValue(-1.0)
        self.setPen(QtGui.QPen(self.lineColor, 1.5, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))

    @property
    def startNode(self):
        """ Get start graph node (_type='nodeBase')
            :return: Start node
            :rtype: QtSvg.QGraphicsSvgItem """
        return self.startItem._parent

    @property
    def endNode(self):
        """ Get end graph node (_type='nodeBase')
            :return: end node
            :rtype: QtSvg.QGraphicsSvgItem """
        return self.endItem._parent

    def getLine(self):
        """ Get link coords
            :return: Line coords
            :rtype: QtCore.QLineF """
        p1 = self.startItem.sceneBoundingRect().center()
        p2 = self.endItem.sceneBoundingRect().center()
        return QtCore.QLineF(self.mapFromScene(p1), self.mapFromScene(p2))

    def getCenterPoint(self):
        """ Get link center point
            :return: Link center point
            :rtype: QtCore.QPointF """
        line = self.getLine()
        centerX = (line.p1().x() + line.p2().x()) / 2
        centerY = (line.p1().y() + line.p2().y()) / 2
        return QtCore.QPointF(centerX, centerY)

    def updatePosition(self):
        """ Update link position """
        self.setPath(self.createPath())

    def deleteLine(self):
        """ Delete link and remove connections plug storage """
        self.log.debug("Deleting line: %s ---> %s ..." % (self.startItem._parent.nodeName,
                                                          self.endItem._parent.nodeName))
        self.startItem.connections.remove(self)
        self.endItem.connections.remove(self)
        self.scene().removeItem(self)

    def createPath(self):
        """ Calculate link angle
            :return: Link path
            :rtype: QtGui.QPainterPath """
        line = self.getLine()
        centerPoint = self.getCenterPoint()
        coef = QtCore.QPointF(abs(centerPoint.x() - line.p1().x()), 0)
        control_1 = line.p1() + coef
        control_2 = line.p2() - coef
        path = QtGui.QPainterPath(line.p1())
        path.cubicTo(control_1, control_2, line.p2())
        return path

    def paint(self, painter, option, widget=None):
        """ Draw line connection """
        myPen = self.pen()
        myPen.setColor(self.lineColor)
        painter.setPen(myPen)
        painter.drawPath(self.createPath())
