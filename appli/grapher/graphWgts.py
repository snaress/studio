import os, math
from PyQt4 import QtGui, QtSvg, QtCore
from appli.grapher.ui import wgGraphZoneUI


class GraphZone(QtGui.QWidget, wgGraphZoneUI.Ui_wgGraphZone):

    def __init__(self, mainUi, graphScene):
        super(GraphZone, self).__init__()
        self.mainUi = mainUi
        self.graphScene = graphScene
        self._setupUi()

    def _setupUi(self):
        self.setupUi(self)
        self.gvGraphZone.setScene(self.graphScene)
        self.gvGraphZone.setSceneRect(0, 0, 1000, 1000)
        self.gvGraphZone.wheelEvent = self.graphZoneWheelEvent
        self.gvGraphZone.resizeEvent = self.graphZoneResizeEvent
        self.gvGraphZone.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(60, 60, 60, 255), QtCore.Qt.SolidPattern))

    def graphZoneWheelEvent(self, event):
        factor = 1.41 ** ((event.delta()*.5) / 240.0)
        self.gvGraphZone.scale(factor, factor)

    def graphZoneResizeEvent(self, event):
        self.graphScene.setSceneRect(0, 0, self.gvGraphZone.width(), self.gvGraphZone.height())


class GraphScene(QtGui.QGraphicsScene):

    def __init__(self, mainUi):
        self.mainUi = mainUi
        super(GraphScene, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        self.line = None
        self.selBuffer = {'_order': []}
        self.connections = []
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
            if hasattr(item, 'nodeType'):
                if item.nodeType == "node":
                    items.append(item)
        return items

    def getSelectedNodes(self):
        items = []
        for item in self.selectedItems():
            if item.nodeType == "node":
                items.append(item)
        return items

    def getNextNameIndex(self, name):
        indList = []
        for item in self.getAllNodes():
            if item.nodeName.startswith(name):
                indList.append(int(item.nodeName.split('_')[-1]))
        if not indList:
            ind = "1"
        else:
            ind = str(max(indList) + 1)
        return "%s_%s" % (name, ind)

    def mousePressEvent(self, event):
        item = self.itemAt(event.scenePos())
        if item is not None and hasattr(item, 'nodeType'):
            if event.button() == QtCore.Qt.LeftButton and item.nodeType == 'nodeConnection':
                self.line = QtGui.QGraphicsLineItem(QtCore.QLineF(event.scenePos(), event.scenePos()))
                self.addItem(self.line)
        super(GraphScene, self).mousePressEvent(event)
        #-- Check Node ElementId State --#
        for node in self.getAllNodes():
            if node.nodeType == "node":
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
                if hasattr(startItems[0], 'nodeType') and hasattr(endItems[0], 'nodeType'):
                    if startItems[0].nodeType == 'nodeConnection' and endItems[0].nodeType == 'nodeConnection':
                        if not startItems[0].isInputConnection and endItems[0].isInputConnection:
                            connectionLine = LineConnection(startItems[0], endItems[0])
                            self.addItem(connectionLine)
                            connectionLine.updatePosition()
        self.line = None
        super(GraphScene, self).mouseReleaseEvent(event)


class GraphNode(QtSvg.QGraphicsSvgItem):

    def __init__(self, mainUi, iconFile, parent=None):
        self.mainUi = mainUi
        self.graphScene = self.mainUi.currentGraphScene
        self.iconFile = iconFile
        self.nodeType = "node"
        self.nodeName = "node_1"
        self.nodeLabel = "Node_1"
        super(GraphNode, self).__init__(self.iconFile, parent)
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
        connFile = os.path.join(self.mainUi.iconPath, "inConnection.svg")
        self.outConnectionNode = NodeConnection(mainUi=self.mainUi, iconFile=connFile, parent=self)
        self.outConnectionNode.setPos(self.width,
                                      (self.height / 2) - (self.outConnectionNode.height / 2))
        self.outConnectionNode.isInputConnection = False
        self.inConnectionNode = NodeConnection(mainUi=self.mainUi, iconFile=connFile, parent=self)
        self.inConnectionNode.setPos(0 - self.inConnectionNode.width,
                                     (self.height / 2) - (self.inConnectionNode.height / 2))
        self.inConnectionNode.isInputConnection = True

    def hoverMoveEvent(self, event):
        self.setElementId("hover")

    def hoverLeaveEvent(self, event):
        if self.isSelected():
            self.setElementId("selected")
        else:
            self.setElementId("regular")


class NodeConnection(QtSvg.QGraphicsSvgItem):

    lineConnected = QtCore.pyqtSignal()

    def __init__(self, **kwargs):
        self.mainUi = kwargs['mainUi']
        self.iconFile = kwargs['iconFile']
        self.nodeType = "nodeConnection"
        self._parent = kwargs['parent']
        super(NodeConnection, self).__init__(self.iconFile, self._parent)
        self.isInputConnection = False
        self.connectedLine = []
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
        self.startNode = startNode
        self.endNode = endNode
        self.nodeType = 'lineConnection'
        super(LineConnection, self).__init__()
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
        self.startNode.connectedLine.append(self)
        self.endNode.connectedLine.append(self)

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

    def paint(self, painter, option, widget=None):
        arrowSize = 20.0
        line = self.getLine()
        painter.setBrush(self.lineColor)
        myPen = self.pen()
        myPen.setColor(self.lineColor)
        painter.setPen(myPen)
        #-- Selected Color --#
        if self.isSelected():
            painter.setBrush(QtCore.Qt.yellow)
            myPen.setColor(QtCore.Qt.yellow)
            myPen.setStyle(QtCore.Qt.DashLine)
            painter.setPen(myPen)
        #-- Calculating Angle --#
        if line.length() > 0.0:
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
            #-- Draw Line --#
            if line:
                painter.drawPolygon(self.arrowHead)
                painter.drawLine(line)
