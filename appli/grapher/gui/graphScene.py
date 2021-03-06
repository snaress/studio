import os
from lib.qt import procQt as pQt
from PyQt4 import QtGui, QtCore, QtSvg
from appli.grapher.gui import graphWgts


class GraphScene(QtGui.QGraphicsScene):
    """
    GraphScene widget, child of GrapherUi.GraphView

    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    :param graphZone: GraphZone ui
    :type graphZone: GraphZone
    """

    def __init__(self, mainUi, graphZone):
        super(GraphScene, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphScene Widget.")
        self.graphZone = graphZone
        self.grapher = self.graphZone.grapher
        self.horizontaleSpace = 500
        self.verticaleSpace = 150
        self._setupWidget()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphScene Widget.")
        self.line = None
        self.ctrlKey = False
        self.selBuffer = {'_order': []}
        self.clickHandler = pQt.ClickHandler(singleClickCmd=self.graphZone._singleClick,
                                             doubleClickCmd=self.graphZone._doubleClick)
        self.selectionChanged.connect(self._selectionChanged)

    def _selectionChanged(self):
        """
        Store node selection order, clear node editor
        """
        selNodes = self.getSelectedNodes()
        #-- Store Selection --#
        if not selNodes:
            self.selBuffer = {'_order': []}
        else:
            for n, item in enumerate(selNodes):
                if not item._item._node.nodeName in self.selBuffer['_order']:
                    self.selBuffer['_order'].append(item._item._node.nodeName)
                    self.selBuffer[item._item._node.nodeName] = item
        #-- Node Editor --#
        if self.mainUi.nodeEditorIsEnabled:
            if not selNodes:
                self.mainUi.nodeEditor.clear()

    def getAllTopLevelNodes(self):
        """
        Get all nodes with 'nodeBase' _type in first column

        :return: All topLevel 'nodeBase' items
        :rtype: list
        """
        iDict = dict()
        if self.items():
            for item in self.items():
                if item._type == 'nodeBase':
                    if item._column == 0:
                        iDict[item.pos().y()] = item
        items = []
        for k, v in sorted(iDict.iteritems()):
            items.append(v)
        return items

    def getAllNodes(self):
        """
        Get all nodes with 'nodeBase' _type

        :return: All 'nodeBase' items
        :rtype: list
        """
        items = []
        for topItem in self.getAllTopLevelNodes():
            items.extend(self.getAllChildren(topItem))
        return items

    def getSelectedNodes(self):
        """
        Get selected nodes with 'nodeBase' _type

        :return: Selected 'nodeBase' items
        :rtype: list
        """
        items = []
        for item in self.selectedItems():
            if item._type == 'nodeBase':
                items.append(item)
        return items

    @staticmethod
    def getAllChildren(item, depth=-1):
        """
        Get all children of given 'nodeBase' item

        :param item: Recusion start item
        :type item: QtSvg.QGraphicsSvgItem
        :param depth: Number of recursion (-1 = infinite)
        :type depth: int
        :return: items list
        :rtype: list
        """
        items = []
        #-- Recurse Function --#
        def recurse(currentItem, depth):
            items.append(currentItem)
            if depth != 0:
                if currentItem._plugOut._children() is not None:
                    for n in range(len(currentItem._plugOut._children())):
                        recurse(currentItem._plugOut._children()[n], depth-1)
        #-- Launch Recursion --#
        recurse(item, depth)
        #-- Result --#
        return items

    @staticmethod
    def getMaxPos(items):
        """
        Get max position

        :param items: List of QGraphicsSvgItem
        :type items: list
        :return: MaxX, MaxY
        :rtype: float, float
        """
        maxX = 0
        maxY = 0
        for item in items:
            if item.x() > maxX:
                maxX = item.x()
            if item.y() > maxY:
                maxY = item.y()
        return maxX, maxY

    def futurPos(self, item, parentItem=None):
        """
        Get Item futur position

        :param item: New GraphItem
        :type item: QtSvg.QGraphicsSvgItem
        :param parentItem: Parent item
        :type parentItem: QtSvg.QGraphicsSvgItem
        :return: Item futur position
        :rtype: float, float
        """
        #-- Top Item Position --#
        if item._column == 0:
            allItems = self.getAllNodes()
            #-- First Top Item --#
            if not allItems:
                return 0, 0
            #-- Other Top Items --#
            maxX, maxY = self.getMaxPos(allItems)
            return 0, (maxY + self.verticaleSpace)
        #-- Child Position --#
        x = (item._column * self.horizontaleSpace)
        if len(parentItem._plugOut._children()) <= 1:
            maxY = parentItem.y()
        else:
            maxX, maxY = self.getMaxPos(self.getAllChildren(parentItem))
            maxY = (maxY + self.verticaleSpace)
        return x, maxY

    def createGraphNode(self, nodeType='modul', nodeName=None, nodeParent=None):
        """
        Add new graphNode to tree

        :param nodeType: Graph node type ('modul', 'sysData', 'cmdData', 'pyData', 'loop', 'condition')
        :type nodeType: str
        :param nodeName: Graph node name
        :type nodeName: str
        :param nodeParent: Parent node name
        :type nodeParent: str
        :return: New item
        :rtype: QtGui.QTreeWidgetItem
        """
        self.log.debug("#-- + Creating %s Node + : %s --#" % (nodeType, nodeName), newLinesBefore=1)
        #-- Create New Item --#
        grapherItem = self.grapher.tree.getItemFromNodeName(nodeName)
        newItem = GraphItem(self.mainUi, grapherItem)
        #-- Use Given Parent --#
        if nodeParent is not None:
            self.log.detail("\t ---> Parent graph item '%s' to '%s'" % (grapherItem._node.nodeName, nodeParent))
            parentItem = self.graphZone.getItemFromNodeName(nodeParent)
            parentItem.addChild(newItem)
            parentItem._widget.rf_expandIconVisibility()
        #-- Parent To World --#
        else:
            self.log.detail("\t ---> Adding graph item '%s' to world ..." % grapherItem._node.nodeName)
            self.addTopLevelItem(newItem)
        return newItem

    def addTopLevelItem(self, QGraphicsSvgItem):
        """
        Add topLevel item to scene

        :param QGraphicsSvgItem: Item to add
        :type QGraphicsSvgItem: QtSvg.QGraphicsSvgItem
        """
        QGraphicsSvgItem._column = 0
        x, y = self.futurPos(QGraphicsSvgItem)
        self.addItem(QGraphicsSvgItem)
        QGraphicsSvgItem.setY(y)

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
                            endItems[0]._item.setParent(startItems[0]._item)
                            self.graphZone.refreshGraph()
        self.line = None

    def createLine(self, startItem, endItem):
        """
        Create connection line

        :param startItem: Start node connectionItem
        :type startItem: QtSvg.QGraphicsSvgItem
        :param endItem: End node connectionItem
        :type endItem: QtSvg.QGraphicsSvgItem
        """
        self.log.debug("Creating line: %s ---> %s ..." % (startItem.parentItem()._item._node.nodeName,
                                                          endItem.parentItem()._item._node.nodeName))
        connectionLine = GraphLink(self.mainUi, startItem, endItem)
        startItem.connections.append(connectionLine)
        endItem.connections.append(connectionLine)
        self.addItem(connectionLine)
        connectionLine.updatePosition()

    def keyPressEvent(self, event):
        """
        Add key press options:

        'Control' = store State for move options
        """
        #-- Store State For Move Options --#
        if event.key() == QtCore.Qt.Key_Control:
            self.ctrlKey = True

    def keyReleaseEvent(self, event):
        """
        Add key release options:

        'Control' = Clear state for move options
        """
        #-- Clear State For Move Options --#
        if event.key() == QtCore.Qt.Key_Control:
            self.ctrlKey = False

    def mousePressEvent(self, event):
        """
        Add mouse press options:

        'Left' = - If itemType is 'nodePlug', store start position for line creation
                 - If empty and ctrlKey is False: Enable area selection
                 - If empty and ctrlKey is True: Enable move by drag
        """
        item = self.itemAt(event.scenePos())
        #-- Construction  Line --#
        if item is not None and hasattr(item, '_type'):
            if event.button() == QtCore.Qt.LeftButton and item._type == 'nodePlug':
                self.line = QtGui.QGraphicsLineItem(QtCore.QLineF(event.scenePos(), event.scenePos()))
                self.addItem(self.line)
        #-- Enable Area Selection --#
        if item is None and not self.ctrlKey:
            self.graphZone.sceneView.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        #-- Enable Moving Scene --#
        elif item is None and self.ctrlKey:
            self.graphZone.sceneView.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
        super(GraphScene, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """
        Add mouse move options:

        'left' = - If line construction is detected, will draw the line and update endPoint position
        """
        if self.line:
            newLine = QtCore.QLineF(self.line.line().p1(), event.scenePos())
            self.line.setLine(newLine)
        super(GraphScene, self).mouseMoveEvent(event)
        self.update()

    def mouseReleaseEvent(self, event):
        """
        Add mouse release options:

        'left' = - If line construction is detected, will draw the final connection and clear construction line item.
                 - Disable GraphView 'move by drag' mode.
                 - If no item under pointer, refresh element id.
                 - If nodeEditor is enabled, connect item.
        """
        self._drawLine()
        self.graphZone.sceneView.setDragMode(QtGui.QGraphicsView.NoDrag)
        super(GraphScene, self).mouseReleaseEvent(event)
        #-- Refresh Element Id --#
        for graphItem in self.getAllNodes():
            graphItem.rf_elementId()
        else:
            item = self.itemAt(event.scenePos())
            if item is not None:
                if item._type == 'nodeWidget':
                    item.parentItem().setSelected(True)
                    item.parentItem().rf_elementId()
        #-- Connect Node Editor --#
        self.clickHandler.__call__()


class GraphItem(QtSvg.QGraphicsSvgItem):
    """
    GraphScene item, child of GrapherUi.GraphView.GraphScene

    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    :param _item: Grapher item object
    :type _item: appli.grapher.core.grapher.GraphItem
    """

    _type = "nodeBase"

    def __init__(self, mainUi, _item):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.detail("\t ---> Init Graph Item --#")
        self._item = _item
        self.iconFile = os.path.join(self.mainUi.iconPath, 'svg', self._item._node._nodeIcon)
        super(GraphItem, self).__init__(self.iconFile)
        self._column = None
        self._setupItem()
        self._setupWidgets()

    def _setupItem(self):
        self.log.detail("\t ---> Setup Graph Item --#")
        self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable|
                      QtGui.QGraphicsItem.ItemIsMovable|
                      QtGui.QGraphicsItem.ItemIsFocusable)
        self.setCachingEnabled(False)
        self.setAcceptHoverEvents(True)
        self.setElementId("regular")

    def _setupWidgets(self):
        self.log.detail("\t ---> Setup Graph Item Widgets --#")
        self._label = GraphText(self._item._node.nodeName, txtType='label', parent=self)
        self._widget = GraphWidget(parent=self)
        self._plugIn = GraphPlug(self.mainUi, isInput=True, parent=self)
        self._plugOut = GraphPlug(self.mainUi, parent=self)

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
    def itemSize(self):
        """
        get graph item size (considering children items)

        :return: Item size (width, height)
        :rtype: (int, int)
        """
        size = ((self.boundingRect().width() + (self._plugIn.boundingRect().width() * 2)),
                (self.boundingRect().height() + self._widget.boundingRect().height()))
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

    def rf_elementId(self):
        """
        Refresh item element id
        """
        if self.isSelected():
            self.setElementId('selected')
        else:
            self.setElementId('regular')

    def addChild(self, QGraphicsSvgItem):
        """
        Add child item to scene

        :param QGraphicsSvgItem: Item to add
        :type QGraphicsSvgItem: QtSvg.QGraphicsSvgItem
        """
        self._widget.widget().set_expanded(True)
        QGraphicsSvgItem._column = self._column + 1
        self.scene().addItem(QGraphicsSvgItem)
        self.scene().createLine(self._plugOut, QGraphicsSvgItem._plugIn)
        x, y = self.scene().futurPos(QGraphicsSvgItem, parentItem=self)
        QGraphicsSvgItem.setPos(x, y)

    def hoverMoveEvent(self, event):
        """
        Add hover move options:

        Change node style
        """
        self.setElementId("hover")

    def hoverLeaveEvent(self, event):
        """
        Add hover leave options:

        Change node style
        """
        if self.isSelected():
            self.setElementId("selected")
        else:
            self.setElementId("regular")

    def mouseReleaseEvent(self, event):
        """
        Add mouse release options:

        'left' = - If node is topLevel, force x position to 0
        """
        super(GraphItem, self).mouseReleaseEvent(event)
        if self._column == 0:
            self.setPos(0, self.pos().y())

    def update(self, nodeDict):
        """
        Update GraphItem with given GrapherCore nodeDict

        :param nodeDict: Node params
        :type nodeDict: dict
        """
        for k, v in nodeDict.iteritems():
            if k == 'nodeIsEnabled':
                self._widget.widget().pbEnable.setChecked(v)
                if self._item._parent is not None:
                    if not self._item._parent._node.nodeIsActive:
                        self._widget.widget().pbEnable.setEnabled(False)
            elif k == 'nodeIsActive':
                self._widget.widget().lNodeName.setEnabled(v)


class GraphWidget(QtGui.QGraphicsProxyWidget):
    """
    GraphSceneItem widget, child of GrapherUi.GraphView.GraphScene.GraphItem

    :param parent: Parent item
    :type parent: QtSvg.QGraphicsSvgItem
    """

    _type = "nodeWidget"

    def __init__(self, parent=None):
        super(GraphWidget, self).__init__(parent)
        self.mainUi = self.parentItem().mainUi
        self._item = self.parentItem()._item
        self._setupItem()

    def _setupItem(self):
        self.setWidget(self.newWidget())
        self.widget().pbUnfold.clicked.connect(self.setUnfold)
        self.setMinimumSize(302, 44)
        self.setMaximumSize(302, 44)
        self.setPos(0, 80)
        self.rf_unfoldIcon()

    def rf_expandIconVisibility(self):
        """
        Refresh expand button visibility
        """
        self.widget().pbExpand.setVisible(False)

    def rf_unfoldIcon(self):
        """
        Refresh unfold state icon
        """
        if self.widget().pbUnfold.isChecked():
            self.widget().pbUnfold.setIcon(self.mainUi.graphZone.foldIcon)
        else:
            self.widget().pbUnfold.setIcon(self.mainUi.graphZone.unfoldIcon)

    def setUnfold(self):
        self.rf_unfoldIcon()

    def newWidget(self):
        """
        Create new graphItem widget

        :return: Graph item widget
        :rtype: graphWgts.ItemWidget
        """
        pbSize = 36
        widget = graphWgts.ItemWidget(self)
        widget.lNodeName.setVisible(False)
        for pb in [widget.pbEnable, widget.pbExpand, widget.pbUnfold]:
            pb.setMinimumSize(pbSize, pbSize)
            pb.setMaximumSize(pbSize, pbSize)
            pb.setIconSize(QtCore.QSize(pbSize, pbSize))
        return widget


class GraphText(QtGui.QGraphicsTextItem):
    """
    GraphTree text item, child of GraphItem

    :param text: Display text
    :type text: str
    :param txtType: 'label' or 'attr'
    :type txtType: str
    :param parent: Parent graphItem
    :type parent: QtSvg.QGraphicsSvgItem
    """

    _type = "nodeText"

    def __init__(self, text, txtType='label', parent=None):
        self._text = text
        self._txtType = txtType
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
            if self._txtType == 'label':
                fontSize = 24
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
            if self._txtType == 'label':
                qColor = QtGui.QColor(255, 120, 50)
            elif self._txtType == 'attr':
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


class GraphPlug(QtSvg.QGraphicsSvgItem):
    """
    GraphWidget item, child of GrapherUi.GraphScene.GraphItem

    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    :param isInput: Connection input stete
    :type isInput: bool
    :param parent: Grapher parent item
    :type parent: QtSvg.QGraphicsSvgItem
    """

    _type = 'nodePlug'

    def __init__(self, mainUi, isInput=False, parent=None):
        self.mainUi = mainUi
        self.iconFile = os.path.join(self.mainUi.iconPath, 'svg', 'plug.svg')
        super(GraphPlug, self).__init__(self.iconFile, parent)
        self._item = self.parentItem()._item
        self.connections = []
        self.isInputConnection = isInput
        self._setupItem()

    def _setupItem(self):
        self.setAcceptHoverEvents(True)
        self.setElementId("regular")
        if self.isInputConnection:
            self.setPos(-45, 80)
        else:
            self.setPos(self.parentItem().width + 2, 80)
        self.setScale(1.2)

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

    def _parent(self):
        """
        Get parent graph node

        :return: Parent graph node
        :rtype: QtSvg.QGraphicsSvgItem
        """
        if self.connections:
            return self.connections[0].startNode

    def _children(self):
        """
        Get children graph nodes

        :return: Children graph nodes
        :rtype: QtSvg.QGraphicsSvgItem
        """
        if self.connections:
            children = []
            for link in self.connections:
                children.append(link.endNode)
            return children

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


class GraphLink(QtGui.QGraphicsPathItem):
    """
    Graphic link item, child of grapher.graphScene. Contains link connection

    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    :param startItem: Start plug item
    :type startItem: QtSvg.QGraphicsSvgItem
    :param endItem: End plug item
    :type endItem: QtSvg.QGraphicsSvgItem
    """

    _type = "nodeLink"

    def __init__(self, mainUi, startItem, endItem):
        self.mainUi = mainUi
        super(GraphLink, self).__init__()
        self.startItem = startItem
        self.endItem = endItem
        self._setupItem()

    def _setupItem(self):
        self.lineColor = QtCore.Qt.gray
        self.setZValue(-1.0)
        self.setFlags(QtGui.QGraphicsPathItem.ItemIsSelectable|QtGui.QGraphicsPathItem.ItemIsFocusable)
        self.setPen(QtGui.QPen(self.lineColor, 4, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))

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
