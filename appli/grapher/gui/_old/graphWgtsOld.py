import os
from PyQt4 import QtGui, QtSvg, QtCore


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
