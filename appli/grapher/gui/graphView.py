import os
from PyQt4 import QtGui, QtSvg, QtCore
from appli.grapher.gui import graphNodes


class GraphView(QtGui.QGraphicsView):
    """
    GraphView widget, child of Fondation
    :param mainUi: Fondation main window
    :type mainUi: QtGui.QMainWindow
    :param graphScene: Graph scene
    :type graphScene: QtGui.QGraphicsScene
    """

    def __init__(self, mainUi, graphScene):
        super(GraphView, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphView Widget.")
        self.setScene(graphScene)
        self._setupWidget()

    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphView Widget.")
        self.setSceneRect(0, 0, 10000, 10000)
        self.scale(0.5, 0.5)
        self.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemShape)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(35, 35, 35, 255), QtCore.Qt.SolidPattern))
        self.setVisible(False)

    def newNode(self):
        """
        Create a default new node (modul)
        :return: New GraphItem
        :rtype: QtSvg.QGraphicsSvgItem
        """
        print 'nodal'
        return self.scene().createGraphNode()

    def fitInScene(self):
        """
        Fit graphZone to graphScene
        """
        self.fitInView(self.scene().itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)

    def fitInSelected(self):
        """
        Fit graphZone to selected nodes
        """
        if len(self.scene().selectedItems()) == 1:
            self.fitInView(self.scene().selectedItems()[0], QtCore.Qt.KeepAspectRatio)

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
            super(GraphView, self).mouseMoveEvent(event)

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
        self.scene().setSceneRect(0, 0, self.width(), self.height())


class GraphScene(QtGui.QGraphicsScene):
    """
    GraphScene widget, child of Fondation.GraphView
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        super(GraphScene, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphScene Widget.")
        self._setupWidget()

    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphScene Widget.")
        self.line = None
        self.buffer = None
        self.ctrlKey = False

    def getAllNodes(self):
        """
        Get all nodes with 'nodeBase' _type
        :return: All 'nodeBase' items
        :rtype: list
        """
        items = []
        if self.items():
            for item in self.items():
                if item._type == 'nodeBase':
                    items.append(item)
        return items

    def getAllTopLevelNodes(self):
        """
        Get all nodes with 'nodeBase' _type in first column
        :return: All topLevel 'nodeBase' items
        :rtype: list
        """
        items = []
        for item in self.getAllNodes():
            if item.isRoot:
                items.append(item)
        return items

    def createGraphNode(self, nodeType='modul', nodeName=None, nodeParent=None, index=None):
        """
        Add new graphNode to scene
        :param nodeType: Graph node type ('modul', 'sysData', 'cmdData', 'pyData', 'loop', 'condition')
        :type nodeType: str
        :param nodeName: Graph node name
        :type nodeName: str
        :param nodeParent: Parent node name
        :type nodeParent: str
        :param index: Index for insertion
        :type index: int
        :return: New item
        :rtype: QtSvg.QGraphicsSvgItem
        """
        if nodeName is None:
            nodeName = '%s_1' % nodeType
        newNodeName = self.mainUi._checkNodeName(nodeName, self.getAllNodes())
        self.mainUi.log.debug("#-- + Creating %s ViewNode + : %s --#" % (nodeType, newNodeName))
        newItem = GraphItem(self.mainUi, nodeType, newNodeName)
        #-- Use Given Parent --#
        if nodeParent is not None:
            self.log.detail("\t ---> Use given parent: %s" % nodeParent)
            pass
        else:
            selItems = self.selectedItems()
            #-- Parent To Selected Node --#
            if len(selItems) == 1:
                self.log.detail("\t ---> Parent to selected node: %s" % selItems[0].nodeName)
                if index is None:
                    self.addGraphWidget(newItem, isRoot=False)
                    self.addItem(newItem)
            #-- Parent To World --#
            else:
                self.log.detail("\t ---> Parent to world")
                if index is None:
                    self.log.detail("\t ---> Adding graph item '%s' to world ..." % newItem.nodeName)
                    self.addGraphWidget(newItem, isRoot=True)
                    self.addItem(newItem)
                else:
                    self.log.detail("\t ---> Inserting graph item '%s' to world ..." % newItem.nodeName)
        return newItem

    def addGraphWidget(self, QGraphicsSvgItem, isRoot=False):
        self.log.detail("\t ---> Adding item widget ...")
        if isRoot:
            allItems = self.getAllTopLevelNodes()
        else:
            allItems = self.selectedItems()
        posX = 0
        posY = 0
        if allItems:
            maxX = 0
            maxY = 0
            for item in allItems:
                if item.y() > maxY:
                    maxY = item.y()
                if item.x() > maxX:
                    maxX = item.x()
            posX = maxX + 450
            posY = maxY + 150
        if isRoot:
            QGraphicsSvgItem.setY(posY)
        else:
            QGraphicsSvgItem.setX(posX)
            QGraphicsSvgItem.setY(allItems[0].y())
        QGraphicsSvgItem._column = isRoot

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
                            self.createLine(startItems[0], endItems[0])
        self.line = None

    def createLine(self, startItem, endItem):
        """
        Create connection line
        :param startItem: Start node connectionItem
        :type startItem: QtSvg.QGraphicsSvgItem
        :param endItem: End node connectionItem
        :type endItem: QtSvg.QGraphicsSvgItem
        """
        self.log.debug("Creating line: %s ---> %s ..." % (startItem.parentItem().nodeName,
                                                          endItem.parentItem().nodeName))
        connectionLine = GraphLink(self.mainUi, startItem, endItem)
        startItem.connections.append(connectionLine)
        endItem.connections.append(connectionLine)
        self.addItem(connectionLine)
        connectionLine.updatePosition()

    def keyPressEvent(self, event):
        """
        Add key press options: 'Control' = store State for move options
        """
        #-- Store State For Move Options --#
        if event.key() == QtCore.Qt.Key_Control:
            self.ctrlKey = True

    def keyReleaseEvent(self, event):
        """
        Add key release options: 'Control' = Clear state for move options
        """
        #-- Clear State For Move Options --#
        if event.key() == QtCore.Qt.Key_Control:
            self.ctrlKey = False

    def mousePressEvent(self, event):
        """
        Add mouse press options: 'Left' = - If itemType is 'nodePlug', store start position for line creation
                                          - If empty and ctrlKey is False: Enable area selection
                                          - If empty and ctrlKey is True: Enable move by drag
        """
        item = self.itemAt(event.scenePos())
        if item is not None and hasattr(item, '_type'):
            #-- Create Line --#
            if event.button() == QtCore.Qt.LeftButton and item._type == 'nodePlug':
                self.line = QtGui.QGraphicsLineItem(QtCore.QLineF(event.scenePos(), event.scenePos()))
                self.addItem(self.line)
        #-- Enable Area Selection Or Moving Scene --#
        if item is None and not self.ctrlKey:
            self.mainUi.graphView.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        elif item is None and self.ctrlKey:
            self.mainUi.graphView.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
        super(GraphScene, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """
        Add mouse move options: 'left' = - If line construction is detected, will draw the line
                                           and update endPoint position
        """
        if self.line:
            newLine = QtCore.QLineF(self.line.line().p1(), event.scenePos())
            self.line.setLine(newLine)
        super(GraphScene, self).mouseMoveEvent(event)
        self.update()

    def mouseReleaseEvent(self, event):
        """
        Add mouse release options: 'left' = - If line construction is detected, will draw the final connection
                                              and clear construction line item.
                                            - Disable GraphView 'move by drag' mode.
        """
        self._drawLine()
        self.mainUi.graphView.setDragMode(QtGui.QGraphicsView.NoDrag)
        super(GraphScene, self).mouseReleaseEvent(event)


class GraphItem(QtSvg.QGraphicsSvgItem):
    """
    Graphic svg item, child of Fondation.GraphView.graphScene
    :param mainUi: Fondation main window
    :type mainUi: QtGui.QMainWindow
    :param nodeType: Graph node type ('modul', 'sysData', 'cmdData', 'pyData', 'loop', 'condition')
    :type nodeType: str
    :param nodeName: Graph node name
    :type nodeName: str
    """

    _type = "nodeBase"

    def __init__(self, mainUi, nodeType, nodeName):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.nodeName = nodeName
        self._nodeType = nodeType
        self._datas = self._initDatas()
        self.isRoot = True
        self.iconFile = os.path.join(self.mainUi.iconPath, 'svg', self._datas._nodeIcon)
        super(GraphItem, self).__init__(self.iconFile)
        self._setupItem()

    def _initDatas(self):
        """
        Init node datas object
        :return: Datas object
        :rtype: Modul | SysData | CmdData | PyData
        """
        if self._nodeType == 'modul':
            return graphNodes.Modul()
        elif self._nodeType == 'sysData':
            return graphNodes.SysData()
        elif self._nodeType == 'cmdData':
            return graphNodes.CmdData()
        elif self._nodeType == 'pyData':
            return graphNodes.PyData()

    def _setupItem(self):
        self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable|
                      QtGui.QGraphicsItem.ItemIsMovable|
                      QtGui.QGraphicsItem.ItemIsFocusable)
        self.setCachingEnabled(False)
        self._label = GraphText('label', self.nodeName, parent=self)
        self._widget = GraphNode(parent=self)
        self._plugIn = GraphPlug(mainUi=self.mainUi, isInput=True, parent=self)
        self._plugOut = GraphPlug(mainUi=self.mainUi, isInput=False, parent=self)

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


class GraphPlug(QtSvg.QGraphicsSvgItem):

    _type = 'nodePlug'

    def __init__(self, **kwargs):
        self.mainUi = kwargs['mainUi']
        self.iconFile = os.path.join(self.mainUi.iconPath, 'svg', 'plug.svg')
        super(GraphPlug, self).__init__(self.iconFile, kwargs['parent'])
        self.connections = []
        self.isInputConnection = kwargs['isInput']
        self._setupItem()

    def _setupItem(self):
        self.setAcceptHoverEvents(True)
        self.setElementId("regular")
        if self.isInputConnection:
            self.setPos(-38, 77)
        else:
            self.setPos(self.parentItem().width + 2, 77)

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


class GraphText(QtGui.QGraphicsTextItem):

    _type = "nodeText"

    def __init__(self, _type, text, parent=None):
        self._type = _type
        self._text = text
        super(GraphText, self).__init__(parent)
        self._setupItem()

    def _setupItem(self):
        self.setText()
        self.setTextFont()
        self.setTextColor()
        self.setTextPosition()

    def setTextFont(self, qFont=None):
        """
        Set GraphText font. Create default or update if 'qFont' is None
        :param qFont: GraphText font
        :type: QtGui.QFont
        """
        if qFont is None:
            if self._type == 'label':
                fontSize = 20
                bold = True
            else:
                fontSize = 14
                bold = False
            qFont = QtGui.QFont("SansSerif", fontSize)
            qFont.setStyleHint(QtGui.QFont.Helvetica)
            qFont.setBold(bold)
        self.setFont(qFont)

    def setText(self, label=None):
        """
        Set GraphText text. Create default or update if 'label' is None
        :param label: GraphText text
        :type label: str
        """
        if label is None:
            label = self._text
        self.setPlainText(label)

    def setTextColor(self, qColor=None):
        """
        Set GraphText color. Create default or update if 'qColor' is None
        :param qColor: GraphText color
        :type qColor: QtGui.QColor
        """
        if qColor is None:
            if self._type == 'label':
                qColor = QtGui.QColor(255, 120, 50)
            elif self._type == 'attr':
                qColor = QtGui.QColor(180, 180, 180)
        self.setDefaultTextColor(qColor)

    def setTextPosition(self, pos=None):
        """
        Set GraphText position. Create default or update if 'pos' is None
        :param pos: GraphText position
        :type pos: tuple
        """
        if pos is None:
            pos = (82, ((self.parentItem().height / 2) - self.font().pointSize()))
        self.setPos(pos[0], pos[1])


class GraphNode(QtGui.QGraphicsRectItem):

    _type = "nodeAttrs"

    def __init__(self, parent=None):
        super(GraphNode, self).__init__(parent)
        self._datas = self.parentItem()._datas
        self._setupItem()

    def _setupItem(self):
        self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable|
                      QtGui.QGraphicsItem.ItemIsFocusable)
        self.setRect(0, 0, 300, 38)
        self.setZValue(-1)
        self.setPos(0, 76)

    def paint(self, painter, option, QWidget_widget=None):
        fillColor = QtGui.QColor(self.parentItem()._datas._nodeColor[0],
                                 self.parentItem()._datas._nodeColor[1],
                                 self.parentItem()._datas._nodeColor[2], 220)
        borderColor = QtGui.QColor(255, 0, 0)
        pen = QtGui.QPen()
        pen.setWidthF(2)
        pen.setColor(borderColor)
        brush = QtGui.QBrush(fillColor)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawRect(self.rect())


class GraphLink(QtGui.QGraphicsPathItem):

    _type = "nodeLink"

    def __init__(self, mainUi, startItem, endItem):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        super(GraphLink, self).__init__()
        self.startItem = startItem
        self.endItem = endItem
        self._setupItem()

    def _setupItem(self):
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
        return self.startItem.parentItem()

    @property
    def endNode(self):
        """
        Get end graph node (_type='nodeBase')
        :return: end node
        :rtype: QtSvg.QGraphicsSvgItem
        """
        return self.endItem.parentItem()

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

    def updatePosition(self):
        """
        Update link position
        """
        self.setPath(self.createPath())

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
        return QtCore.QRectF(p1, QtCore.QSizeF(p2.x()-p1.x(),
                                               p2.y()-p1.y())).normalized().adjusted(-extra, -extra, extra, extra)

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
        painter.strokePath(self.createPath(), myPen)

