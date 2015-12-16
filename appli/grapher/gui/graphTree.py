from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from appli.grapher.gui import graphWgts


class GraphTree(QtGui.QTreeWidget):
    """
    GraphTree widget, child of GrapherUi.GraphZone

    :param mainUi: Grapher mainUi class
    :type mainUi: QtGui.QMainWindow
    :param graphZone: GraphZone ui
    :type graphZone: GraphZone
    """

    def __init__(self, mainUi, graphZone):
        super(GraphTree, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphTree Widget.")
        self.graphZone = graphZone
        self.grapher = self.graphZone.grapher
        self.menu = QtGui.QMenu()
        self._setupWidget()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphTree Widget.")
        self.setStyleSheet("background-color: rgb(35, 35, 35)")
        self.setSelectionMode(QtGui.QTreeWidget.ExtendedSelection)
        self.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.itemClicked.connect(pQt.ClickHandler(singleClickCmd=self.graphZone._singleClick,
                                                  doubleClickCmd=self.graphZone._doubleClick))
        self.setExpandsOnDoubleClick(False)
        self.setHeaderHidden(True)
        self.setColumnCount(12)
        self.setIndentation(0)
        self.rf_graphColumns()
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self, QtCore.SIGNAL('customContextMenuRequested(const QPoint&)'), self.on_popupMenu)

    def rf_graphColumns(self):
        """
        Refresh graphTree column size
        """
        for n in range(self.columnCount()):
            self.resizeColumnToContents(n)

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
        newItem._widget = GraphWidget(newItem)
        #-- Use Given Parent --#
        if nodeParent is not None:
            self.log.detail("\t ---> Use given parent: %s" % nodeParent)
            parentItem = self.graphZone.getItemFromNodeName(nodeParent)
            parentItem.addChild(newItem)
            parentItem._widget.rf_expandIconVisibility()
        #-- Parent To World --#
        else:
            self.log.detail("\t ---> Adding graph item '%s' to world ..." % grapherItem._node.nodeName)
            self.addTopLevelItem(newItem)
        return newItem

    def selectionChanged(self, event, options):
        """
        Add options:

        Update selected / deselected node color
        """
        super(GraphTree, self).selectionChanged(event, options)
        #-- Node Color --#
        for item in pQt.getAllItems(self):
            if item in self.selectedItems():
                item._widget.set_nodeColor((255, 255, 0, 255))
            else:
                item._widget.rf_nodeColor()
        #-- Node Editor --#
        if self.mainUi.nodeEditorIsEnabled:
            if not self.selectedItems():
                self.mainUi.nodeEditor.clear()

    def addTopLevelItem(self, QTreeWidgetItem):
        """
        Add options:

        Insert widget, refresh columns
        """
        super(GraphTree, self).addTopLevelItem(QTreeWidgetItem)
        QTreeWidgetItem._column = 0
        self.setItemWidget(QTreeWidgetItem, QTreeWidgetItem._column, QTreeWidgetItem._widget)
        self.rf_graphColumns()

    def on_popupMenu(self, point):
        """
        Build and launch popup menu

        :param point: Cursor position
        :type point: QtGui.QPoint
        """
        self.graphZone.buildMenu(self.menu)
        self.menu.exec_(self.mapToGlobal(point))


class GraphItem(QtGui.QTreeWidgetItem):
    """
    GraphTree item, child of GrapherUi.GraphTree

    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    :param _item: Grapher item object
    :type _item: appli.grapher.core.grapher.GraphItem
    """

    def __init__(self, mainUi, _item):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.detail("\t ---> Init Graph Item --#")
        super(GraphItem, self).__init__()
        self._item = _item
        self._widget = None
        self._column = None

    def addChild(self, QTreeWidgetItem):
        """
        Add options:

        Add widget, refresh columns
        """
        super(GraphItem, self).addChild(QTreeWidgetItem)
        self._widget.set_expanded(True)
        QTreeWidgetItem._column = self._column + 1
        self.treeWidget().setItemWidget(QTreeWidgetItem, QTreeWidgetItem._column, QTreeWidgetItem._widget)
        self.treeWidget().rf_graphColumns()

    def update(self, nodeDict):
        """
        Update GraphItem with given GrapherCore nodeDict

        :param nodeDict: Node params
        :type nodeDict: dict
        """
        for k, v in nodeDict.iteritems():
            if k == 'nodeIsEnabled':
                self._widget.pbEnable.setChecked(v)
                if self._item._parent is not None:
                    if not self._item._parent._node.nodeIsActive:
                        self._widget.pbEnable.setEnabled(False)
            elif k == 'nodeIsActive':
                self._widget.lNodeName.setEnabled(v)
            elif k == 'nodeIsExpanded':
                self._widget.set_expanded(state=v)


class GraphWidget(graphWgts.ItemWidget):
    """
    GraphTreeItem widget, child of GrapherUi.GraphTree.GraphItem

    :param pItem: Parent item
    :type pItem: QtGui.QTreeWidgetItem
    """

    def __init__(self, pItem):
        self.pItem = pItem
        super(GraphWidget, self).__init__(self.pItem)
        self.pTree = self.pItem.treeWidget()
        self._setupNode()

    def _setupNode(self):
        self.qfUnfold.setVisible(False)
        self.rf_label()

    def rf_label(self):
        """
        Refresh graphNode label
        """
        self.lNodeName.setText(self._item._node.nodeName)

    def rf_expandIconVisibility(self):
        """
        Refresh expand button visibility
        """
        if self.pItem.childCount():
            self.pbExpand.setVisible(True)
        else:
            self.pbExpand.setVisible(False)
