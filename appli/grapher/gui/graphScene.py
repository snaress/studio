import os
from PyQt4 import QtGui, QtCore, QtSvg


class GraphScene(QtGui.QGraphicsScene):
    """
    GraphScene widget, child of Grapher.GraphView
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi, graphZone):
        super(GraphScene, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphScene Widget.")
        self.graphZone = graphZone
        self.grapher = self.graphZone.grapher
        self._setupWidget()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphScene Widget.")
        self.ctrlKey = False
        self.selBuffer = {'_order': []}

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
        self.addItem(QGraphicsSvgItem)
        QGraphicsSvgItem._column = 0

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
        Add mouse press options: 'Left' = - If empty and ctrlKey is False: Enable area selection
                                          - If empty and ctrlKey is True: Enable move by drag
        """
        item = self.itemAt(event.scenePos())
        #-- Enable Area Selection Or Moving Scene --#
        if item is None and not self.ctrlKey:
            self.graphZone.sceneView.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        elif item is None and self.ctrlKey:
            self.graphZone.sceneView.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
        super(GraphScene, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """
        Add mouse release options: 'left' = - Disable GraphView 'move by drag' mode.
        """
        self.graphZone.sceneView.setDragMode(QtGui.QGraphicsView.NoDrag)
        super(GraphScene, self).mouseReleaseEvent(event)


class GraphItem(QtSvg.QGraphicsSvgItem):
    """
    GraphTree item, child of GrapherUi.GraphScene
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

    def addChild(self, QGraphicsSvgItem):
        """
        Add child item to scene
        :param QGraphicsSvgItem: Item to add
        :type QGraphicsSvgItem: QtSvg.QGraphicsSvgItem
        """
        # self._widget.set_expanded(True)
        self.scene().addItem(QGraphicsSvgItem)
        QGraphicsSvgItem._column = self._column + 1


class GraphWidget(QtGui.QGraphicsRectItem):

    _type = "nodeWidget"

    def __init__(self, parent=None):
        super(GraphWidget, self).__init__(parent)
        self._item = self.parentItem()._item
        self._setupItem()

    def _setupItem(self):
        self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable|
                      QtGui.QGraphicsItem.ItemIsFocusable)
        self.setRect(0, 0, 300, 50)
        self.setZValue(-1)
        self.setPos(0, 76)

    def paint(self, painter, option, QWidget_widget=None):
        """
        Draw graphWidget
        """
        fillColor = QtGui.QColor(self._item._node._nodeColor[0], self._item._node._nodeColor[1],
                                 self._item._node._nodeColor[2], self._item._node._nodeColor[3])
        borderColor = QtGui.QColor(255, 0, 0)
        pen = QtGui.QPen()
        pen.setWidthF(2)
        pen.setColor(borderColor)
        brush = QtGui.QBrush(fillColor)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawRect(self.rect())


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
