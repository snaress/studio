import os
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
                if not item._item._node.nodeName in self.selBuffer['_order']:
                    self.selBuffer['_order'].append(item._item._node.nodeName)
                    self.selBuffer[item._item._node.nodeName] = item

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
            if item.isVisible():
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
        self.log.debug("#-- + Creating %s Node + : %s --#" % (nodeType, nodeName), newLinesBefor=1)
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
        connectionLine = graphWgts.GraphLink(self.mainUi, startItem, endItem)
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
                 - If no item under pointer, refresh element id
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
        self._label = graphWgts.GraphText(self._item._node.nodeName, txtType='label', parent=self)
        self._widget = GraphWidget(parent=self)
        self._plugIn = graphWgts.GraphPlug(self.mainUi, isInput=True, parent=self)
        self._plugOut = graphWgts.GraphPlug(self.mainUi, parent=self)

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
            if k == 'nodeIsExpanded':
                self._widget.widget().set_expanded(v)


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
        if self.parentItem()._plugOut._children():
            self.widget().pbExpand.setVisible(True)
        else:
            self.widget().pbExpand.setVisible(True)

    def rf_unfoldIcon(self):
        """
        Refresh unfold state icon
        """
        if self.widget().pbUnfold.isChecked():
            self.widget().pbUnfold.setIcon(self.mainUi.graphZone.foldIcon)
        else:
            self.widget().pbUnfold.setIcon(self.mainUi.graphZone.unfoldIcon)

    def setExpanded(self, state):
        """
        Set GraphItem expanded

        :param state: Item expanded state
        :type state: bool
        """
        items = self.scene().getAllChildren(self.parentItem())
        for n, item in enumerate(items):
            if item._plugOut.connections:
                for link in item._plugOut.connections:
                    link.setVisible(state)
            if n > 0:
                item.setVisible(item._plugIn._parent()._widget.widget().isExpanded)
                item._plugIn.connections[0].setVisible(item._plugIn._parent()._widget.widget().isExpanded)

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
