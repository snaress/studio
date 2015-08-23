import os, pprint
from PyQt4 import QtGui, QtSvg, QtCore
from appli.grapher.core import graphNodes
from appli.grapher.gui import graphWgtsOld


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

    def getDatas(self, asString=False):
        treeDict = dict()
        #-- Parse Datas --#
        for n, item in enumerate(self.scene().getAllNodes()):
            nodeDatas = item._datas.getDatas()
            nodeDatas['isEnabled'] = True
            nodeDatas['isExpanded'] = True
            if item._plugIn._parent() is None:
                nodeDatas['parent'] = None
            else:
                nodeDatas['parent'] = item._plugIn._parent()._datas.nodeName
            treeDict[n] = nodeDatas
        #-- Return Datas --#
        if asString:
            pprint.pformat(treeDict)
        return treeDict

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

    def deleteSelectedNodes(self):
        """
        Delete selected graphNodes
        """
        selItems = self.scene().getSelectedNodes()
        if selItems:
            for item in selItems:
                item.delete()

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

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphScene Widget.")
        self.line = None
        self.buffer = None
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
                if not item._datas.nodeName in self.selBuffer['_order']:
                    self.selBuffer['_order'].append(item._datas.nodeName)
                    self.selBuffer[item._datas.nodeName] = item

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
                    if item.isRoot:
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
        """ Get all children of given 'nodeBase' item
            :param item: Recusion start item
            :type item: QtGui.QTreeWidgetItem
            :param depth: Number of recursion (-1 = infinite)
            :type depth: int
            :return: items list
            :rtype: list """
        items = []

        def recurse(currentItem, depth):
            items.append(currentItem)
            if depth != 0:
                if currentItem._plugOut._children() is not None:
                    for n in range(len(currentItem._plugOut._children())):
                        recurse(currentItem._plugOut._children()[n], depth-1)

        recurse(item, depth)
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

    def getItemFromNodeName(self, nodeName):
        """
        Get graphItem from given node name
        :param nodeName: Graph node name
        :type nodeName: str
        :return: Graph item
        :rtype: QtGui.QTreeWidgetItem
        """
        for item in self.getAllNodes():
            if item._datas.nodeName == nodeName:
                return item

    def buildGraph(self, treeDict):
        self.log.debug("#-- Build Graph --#" , newLinesBefor=1)
        #-- Create Nodes --#
        # items = dict()
        self.log.debug("Creating Nodes ...")
        for n in sorted(treeDict.keys()):
            self.createGraphNode(nodeType=treeDict[n]['nodeType'], nodeName=treeDict[n]['nodeName'],
                                 nodeParent=treeDict[n]['parent'])
            # items[newItem] = treeDict[n]['isExpanded']

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
        self.mainUi.log.debug("#-- + Creating %s Node + : %s --#" % (nodeType, newNodeName))
        newItem = self.newGraphItem(nodeType, newNodeName)
        #-- Use Given Parent --#
        if nodeParent is not None:
            self.log.detail("\t ---> Use given parent: %s" % nodeParent)
            item = self.getItemFromNodeName(nodeParent)
            if index is None:
                self.addGraphWidget(newItem, isRoot=False, parent=item)
                self.addItem(newItem)
            self.createLine(item._plugOut, newItem._plugIn)
        else:
            selItems = self.selectedItems()
            #-- Parent To Selected Node --#
            if len(selItems) == 1:
                self.log.detail("\t ---> Parent to selected node: %s" % selItems[0]._datas.nodeName)
                if index is None:
                    self.addGraphWidget(newItem, isRoot=False)
                    self.addItem(newItem)
                self.createLine(selItems[0]._plugOut, newItem._plugIn)
            #-- Parent To World --#
            else:
                self.log.detail("\t ---> Parent to world")
                if index is None:
                    self.log.detail("\t ---> Adding graph item '%s' to world ..." % newItem._datas.nodeName)
                    self.addGraphWidget(newItem, isRoot=True)
                    self.addItem(newItem)
                else:
                    self.log.detail("\t ---> Inserting graph item '%s' to world ..." % newItem._datas.nodeName)
        return newItem

    def newGraphItem(self, nodeType, nodeName):
        """
        Create new graphItem and graphNode
        :param nodeType: Graph node type ('modul', 'sysData', 'cmdData', 'pyData', 'loop', 'condition')
        :type nodeType: str
        :param nodeName: Graph node name
        :type nodeName: str
        :return: New graphNode
        :rtype: QtSvg.QGraphicsSvgItem
        """
        if nodeType == 'modul':
            newItem = GraphItem(self.mainUi, graphNodes.Modul(nodeName))
        elif nodeType == 'sysData':
            newItem = GraphItem(self.mainUi, graphNodes.SysData(nodeName))
        elif nodeType == 'cmdData':
            newItem =  GraphItem(self.mainUi, graphNodes.CmdData(nodeName))
        elif nodeType == 'pyData':
            newItem = GraphItem(self.mainUi, graphNodes.PyData(nodeName))
        else:
            newItem = GraphItem(self.mainUi, graphNodes.Modul(nodeName))
        newItem._widget = GraphNode(newItem)
        return newItem

    def addGraphWidget(self, QGraphicsSvgItem, isRoot=False, parent=None):
        """
        Add graphNode widget to given item
        :param QGraphicsSvgItem: Item widget parent
        :type QGraphicsSvgItem: QtSvg.QGraphicsSvgItem
        :param isRoot: GraphNode is top level item
        :type isRoot: bool
        """
        self.log.detail("\t ---> Adding item widget ...")
        #-- Get Items --#
        if isRoot:
            allItems = self.getAllNodes()
        else:
            if parent is None:
                allItems = self.selectedItems()
            else:
                allItems = [parent]
        #-- Get Position --#
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
        #-- Apply Position --#
        if isRoot:
            QGraphicsSvgItem.setY(posY)
        else:
            QGraphicsSvgItem.setX(posX)
            if parent is not None:
                parent.branchWorldBBox()
                if parent._plugOut._children() is not None:
                    posY = (posY + (150 * (len(parent._plugOut._children()) - 1 )))
                    QGraphicsSvgItem.setY(posY)
                else:
                    QGraphicsSvgItem.setY(allItems[0].y())
            else:
                QGraphicsSvgItem.setY(allItems[0].y())
        QGraphicsSvgItem.isRoot = isRoot

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
                            if not endItems[0].connections:
                                self.createLine(startItems[0], endItems[0])
                            else:
                                log = "\t\t >>> %s is already connected !!!" % endItems[0].parentItem().nodeName
                                self.log.detail(log)
        self.line = None

    def createLine(self, startItem, endItem):
        """
        Create connection line
        :param startItem: Start node connectionItem
        :type startItem: QtSvg.QGraphicsSvgItem
        :param endItem: End node connectionItem
        :type endItem: QtSvg.QGraphicsSvgItem
        """
        self.log.debug("Creating line: %s ---> %s ..." % (startItem.parentItem()._datas.nodeName,
                                                          endItem.parentItem()._datas.nodeName))
        connectionLine = graphWgtsOld.GraphLink(self.mainUi, startItem, endItem)
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

    def __init__(self, mainUi, nodeObject):
        self.mainUi = mainUi
        self._datas = nodeObject
        self.isRoot = True
        self.iconFile = os.path.join(self.mainUi.iconPath, 'svg', self._datas._nodeIcon)
        super(GraphItem, self).__init__(self.iconFile)
        self._setupItem()

    def _setupItem(self):
        self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable|
                      QtGui.QGraphicsItem.ItemIsMovable|
                      QtGui.QGraphicsItem.ItemIsFocusable)
        self.setCachingEnabled(False)
        self._widget = GraphNode(parent=self)
        self._label = graphWgtsOld.GraphText('label', self._datas.nodeName, parent=self)
        self._plugIn = graphWgtsOld.GraphPlug(mainUi=self.mainUi, isInput=True, parent=self)
        self._plugOut = graphWgtsOld.GraphPlug(mainUi=self.mainUi, isInput=False, parent=self)

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

    def branchWorldBBox(self):
        branchItems = self.scene().getAllChildren(self)
        print branchItems

    def delete(self):
        """
        Delete node and links
        """
        self.log.debug("#-- - Deleting %s Node - : %s --#" % (self._nodeType, self.nodeName), newLinesBefor=1)

    def mouseReleaseEvent(self, event):
        """
        Add mouse release options: 'left' = - If node is topLevel, force x position to 0
        """
        super(GraphItem, self).mouseReleaseEvent(event)
        if self.isRoot:
            self.setPos(0, self.pos().y())


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
