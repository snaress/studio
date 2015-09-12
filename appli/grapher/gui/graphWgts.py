import os
from PyQt4 import QtGui, QtSvg, QtCore
from appli.grapher.gui.ui import graphNodeUI


class ItemWidget(QtGui.QWidget, graphNodeUI.Ui_wgGraphNode):
    """
    GraphTreeItem widget, child of GrapherUi.GraphTree.GraphItem

    :param pItem: Parent item
    :type pItem: QtGui.QTreeWidgetItem | QtSvg.QGraphicsProxyWidget
    """

    def __init__(self, pItem):
        self.pItem = pItem
        self.mainUi = self.pItem.mainUi
        self.log = self.mainUi.log
        self.log.detail("\t ---> Init Graph Widget --#")
        self._item = self.pItem._item
        super(ItemWidget, self).__init__()
        self._setupWidget()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        self.log.detail("\t ---> Setup Graph Widget --#")
        self.setupUi(self)
        self.pbEnable.clicked.connect(self.set_enabled)
        self.pbExpand.clicked.connect(self.set_expanded)
        self.pbExpand.setVisible(False)
        self.rf_nodeColor()
        self.rf_enableIcon()
        self.rf_expandIcon()

    @property
    def isEnabled(self):
        """
        Get node enable state from grapher nodeObject

        :return: Node enable state
        :rtype: bool
        """
        return self._item._node.nodeIsEnabled

    @property
    def isActive(self):
        """
        Get node active state from grapher nodeObject

        :return: Node active state
        :rtype: bool
        """
        return self._item._node.nodeIsActive

    @property
    def isExpanded(self):
        """
        Get node expanded state from grapher nodeObject

        :return: Node expanded state
        :rtype: bool
        """
        return self._item._node.nodeIsExpanded

    def rf_nodeColor(self):
        """
        Refresh graphNode color
        """
        self.set_nodeColor(self._item._node._nodeColor)

    def rf_enableIcon(self):
        """
        Refresh enable state icon
        """
        if self._item._node.nodeIsEnabled:
            self.pbEnable.setIcon(self.mainUi.graphZone.enabledIcon)
        else:
            self.pbEnable.setIcon(self.mainUi.graphZone.disabledIcon)
        self.lNodeName.setEnabled(self.isActive)

    def rf_expandIcon(self):
        """
        Refresh expand state icon
        """
        if self._item._node.nodeIsExpanded:
            self.pbExpand.setIcon(self.mainUi.graphZone.collapseIcon)
        else:
            self.pbExpand.setIcon(self.mainUi.graphZone.expandIcon)

    def set_nodeColor(self, rgba):
        """
        Set graphNode color (used for highlighting selected items)

        :param rgba: GraphNode color
        :type rgba: tuple
        """
        self.setStyleSheet("background-color: rgba(%s, %s, %s, %s)" % (rgba[0], rgba[1], rgba[2], rgba[3]))

    def set_enabled(self, state=None):
        """
        Set node enable state with given value

        :param state: Node enable state
        :type state: bool
        """
        if state is None:
            state = not self.isEnabled
        else:
            self.pbEnable.setChecked(state)
        self._item.setEnabled(state)
        self.lNodeName.setEnabled(self.isActive)
        self.rf_enableIcon()

    def set_expanded(self, state=None):
        """
        Set graphNode expanded with given state

        :param state: Expand state
        :type state: bool
        """
        if state is None:
            state = not self.isExpanded
        else:
            self.pbExpand.setChecked(state)
        self._item.setExpanded(state)
        self.pItem.setExpanded(state)
        self.rf_expandIcon()


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
