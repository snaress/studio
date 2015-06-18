import math
from PyQt4 import QtGui, QtSvg, QtCore
# from appli.grapher import grapherTest as gpTest


class GraphZone(QtGui.QGraphicsView):

    def __init__(self, mainUi, graphScene):
        super(GraphZone, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.graphScene = graphScene
        self.ctrlKey = False
        self._setupUi()

    def _setupUi(self):
        self.log.debug("---> Setup GraphZone ...")
        self.setScene(self.graphScene)
        self.setSceneRect(0, 0, 10000, 10000)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(60, 60, 60, 255), QtCore.Qt.SolidPattern))

    def wheelEvent(self, event):
        factor = 1.41 ** ((event.delta()*.5) / 240.0)
        self.scale(factor, factor)

    def resizeEvent(self, event):
        self.graphScene.setSceneRect(0, 0, self.width(), self.height())


class GraphScene(QtGui.QGraphicsScene):

    def __init__(self, mainUi):
        super(GraphScene, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        self.log.debug("---> Setup GraphScene ...")
        self.ctrlKey = False
        self.line = None
        self.selBuffer = {'_order': []}
        self.selectionChanged.connect(self._selectionChanged)

    def _selectionChanged(self):
        selNodes = self.getSelectedNodes()
        if not selNodes:
            self.selBuffer = {'_order': []}
        else:
            for n, item in enumerate(selNodes):
                if not item.nodeName in self.selBuffer['_order']:
                    self.selBuffer['_order'].append(item.nodeName)
                    self.selBuffer[item.nodeName] = item

    def getAllNodes(self):
        items = []
        for item in self.items():
            if hasattr(item, '_type'):
                if item._type == "nodeBase":
                    items.append(item)
        return items

    def getSelectedNodes(self):
        items = []
        for item in self.selectedItems():
            if hasattr(item, '_type'):
                if item._type == "nodeBase":
                    items.append(item)
        return items

    def getNextNameIndex(self, name):
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

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Delete:
            for item in self.selectedItems():
                if item._type == 'lineConnection':
                    item.deleteLine()
                else:
                    item.deleteNode()
        if event.key() == QtCore.Qt.Key_Control:
            self.ctrlKey = True

    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.ctrlKey = False

    def mousePressEvent(self, event):
        item = self.itemAt(event.scenePos())
        if item is not None and hasattr(item, '_type'):
            if event.button() == QtCore.Qt.LeftButton and item._type == 'nodeConnection':
                self.line = QtGui.QGraphicsLineItem(QtCore.QLineF(event.scenePos(), event.scenePos()))
                self.addItem(self.line)
        super(GraphScene, self).mousePressEvent(event)
        #-- Check Node ElementId State --#
        for node in self.getAllNodes():
            if node._type == "nodeBase":
                if not node.isSelected():
                    node.setElementId("regular")

    def mouseMoveEvent(self, event):
        if self.line:
            newLine = QtCore.QLineF(self.line.line().p1(), event.scenePos())
            self.line.setLine(newLine)
        super(GraphScene, self).mouseMoveEvent(event)
        self.update()

    def mouseReleaseEvent(self, event):
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
                            connectionLine = LineConnection(startItems[0], endItems[0])
                            startItems[0].connections.append(connectionLine)
                            endItems[0].connections.append(connectionLine)
                            # connectionLine = gpTest.LineConnection(startItems[0], endItems[0])
                            self.addItem(connectionLine)
                            connectionLine.updatePosition()
        self.line = None
        super(GraphScene, self).mouseReleaseEvent(event)


class GraphNode(QtSvg.QGraphicsSvgItem):

    def __init__(self, **kwargs):
        self.mainUi = kwargs['mainUi']
        self._type = "nodeBase"
        self.nodeName = kwargs['nodeName']
        if not 'nodeLabel' in kwargs.keys():
            self.nodeLabel = self.nodeName
        else:
            self.nodeLable = kwargs['nodeLabel']
        super(GraphNode, self).__init__(self.iconFile)
        self.defaultBrush = QtGui.QPen()
        self._setupUi()

    @property
    def nodeSize(self):
        size = (self.boundingRect().width(), self.boundingRect().height())
        return size

    @property
    def width(self):
        return self.nodeSize[0]

    @property
    def height(self):
        return self.nodeSize[1]

    def getConnections(self):
        cDict = {}
        if self.hasInputFileConnection:
            cDict['inputFile'] = self.inputFileConnection.connections
        if self.hasInputDataConnection:
            cDict['inputData'] = self.inputDataConnection.connections
        if self.hasOutputFileConnection:
            cDict['outputFile'] = self.outputFileConnection.connections
        return cDict

    def _setupUi(self):
        self.defaultBrush.setWidth(2)
        self.defaultBrush.setColor(QtCore.Qt.white)
        self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable|
                      QtGui.QGraphicsItem.ItemIsMovable|
                      QtGui.QGraphicsItem.ItemIsFocusable)
        self.setCachingEnabled(False)
        self.setAcceptHoverEvents(True)
        self.setElementId("regular")
        self.setToolTip(self.nodeLabel)
        self.addConnectionNodes()

    def addConnectionNodes(self):
        if self.hasInputFileConnection:
            self.inputFileConnection = NodeConnection(mainUi=self.mainUi, nodeType='inputFileConnection',
                                                      iconFile="icon/inputFileConnNode.svg", parent=self)
            self.inputFileConnection.setPos(0 - self.inputFileConnection.width,
                                            - (self.inputFileConnection.height / 2))
            self.inputFileConnection.isInputConnection = True
        if self.hasInputDataConnection:
            self.inputDataConnection = NodeConnection(mainUi=self.mainUi, nodeType='inputDataConnection',
                                                      iconFile="icon/inputDataConnNode.svg", parent=self)
            self.inputDataConnection.setPos(0 - self.inputDataConnection.width,
                                            self.height - (self.inputDataConnection.height / 2))
            self.inputDataConnection.isInputConnection = True
        if self.hasOutputFileConnection:
            self.outputFileConnection = NodeConnection(mainUi=self.mainUi, nodeType='outputFileConnection',
                                                      iconFile="icon/outputFileConnNode.svg", parent=self)
            self.outputFileConnection.setPos(self.width, (self.height / 2) - (self.outputFileConnection.height / 2))
            self.outputFileConnection.isInputConnection = False

    def deleteNode(self):
        #-- Delete Connections --#
        cDict = self.getConnections()
        for k, v in cDict.iteritems():
            deletedItems = []
            for item in v:
                deletedItems.append(item)
                item.deleteLine()
            #-- Update Node connections --#
            for item in deletedItems:
                if k == 'inputFile':
                    self.inputFileConnection.connections.remove(item)
                elif k == 'inputData':
                    self.inputDataConnection.connections.remove(item)
                elif k == 'outputFile':
                    self.outputFileConnection.connections.remove(item)
        #-- Delete Node --#
        self.scene().removeItem(self)

    def hoverMoveEvent(self, event):
        self.setElementId("hover")

    def hoverLeaveEvent(self, event):
        if self.isSelected():
            self.setElementId("selected")
        else:
            self.setElementId("regular")


class NodeConnection(QtSvg.QGraphicsSvgItem):

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

    @property
    def nodeSize(self):
        size = (self.boundingRect().width(), self.boundingRect().height())
        return size

    @property
    def width(self):
        return self.nodeSize[0]

    @property
    def height(self):
        return self.nodeSize[1]

    def _setupUi(self):
        self.setAcceptHoverEvents(True)
        self.setElementId("regular")

    def hoverMoveEvent(self,event):
        self.setElementId("hover")

    def hoverLeaveEvent(self, event):
        self.setElementId("regular")

    def mouseReleaseEvent(self, event):
        self.setElementId("regular")


class LineConnection(QtGui.QGraphicsLineItem):

    def __init__(self, startNode, endNode):
        super(LineConnection, self).__init__()
        self.startNode = startNode
        self.endNode = endNode
        self._type = 'lineConnection'
        self.lineColor = QtCore.Qt.black
        self.arrowHead = QtGui.QPolygonF()
        self.setZValue(-1.0)
        self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable|QtGui.QGraphicsItem.ItemIsFocusable)
        self.setPen(QtGui.QPen(self.lineColor, 1, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))

    def getLine(self):
        p1 = self.startNode.sceneBoundingRect().center()
        p2 = self.endNode.sceneBoundingRect().center()
        return QtCore.QLineF(self.mapFromScene(p1), self.mapFromScene(p2))

    def getCenterPoint(self):
        line = self.getLine()
        centerX = (line.p1().x() + line.p2().x()) / 2
        centerY = (line.p1().y() + line.p2().y()) / 2
        return QtCore.QPointF(centerX, centerY)

    def updatePosition(self):
        self.setLine(self.getLine())

    def deleteLine(self):
        self.scene().removeItem(self)

    def boundingRect(self):
        extra = (self.pen().width() + 100) / 2.0
        line = self.getLine()
        p1 = line.p1()
        p2 = line.p2()
        return QtCore.QRectF(p1, QtCore.QSizeF(p2.x()-p1.x(), p2.y()-p1.y())).normalized().adjusted(-extra,-extra,extra,extra)

    def shape(self):
        path = super(LineConnection, self).shape()
        path.addPolygon(self.arrowHead)
        return path

    def _arrowHeadCalculation(self, line, arrowSize):
        try:
            angle = math.acos(line.dx() / line.length())
        except ZeroDivisionError:
            angle = 0
        if line.dy() >= 0:
            angle = (math.pi * 2.0) - angle
        #-- Arrow Direction --#
        if self.startNode.isInputConnection:
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

    def paint(self, painter, option, widget=None):
        arrowSize = 20.0
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
            self._arrowHeadCalculation(line, arrowSize)
            #-- Draw Line --#
            if line:
                painter.drawPolygon(self.arrowHead)
                painter.drawLine(line)
