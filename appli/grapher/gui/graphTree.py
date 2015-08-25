from PyQt4 import QtGui
from lib.qt import procQt as pQt
from appli.grapher.gui.ui import graphNodeUI


class GraphTree(QtGui.QTreeWidget):
    """
    GraphTree widget, child of GrapherUi.GraphZone
    :param mainUi: Grapher mainUi class
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi, graphZone):
        super(GraphTree, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphTree Widget.")
        self.graphZone = graphZone
        self.grapher = self.graphZone.grapher
        self._setupWidget()

    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphTree Widget.")
        self.setStyleSheet("background-color: rgb(35, 35, 35)")
        self.setSelectionMode(QtGui.QTreeWidget.ExtendedSelection)
        self.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.setExpandsOnDoubleClick(False)
        self.setHeaderHidden(True)
        self.setColumnCount(12)
        self.setIndentation(0)
        self.rf_graphColumns()

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
        self.log.debug("#-- + Creating %s Node + : %s --#" % (nodeType, nodeName), newLinesBefor=1)
        #-- Create New Item --#
        grapherItem = self.grapher.tree.getItemFromNodeName(nodeName)
        newItem = GraphItem(self.mainUi, grapherItem)
        newItem._widget = GraphWidget(newItem)
        #-- Use Given Parent --#
        if nodeParent is not None:
            self.log.detail("\t ---> Use given parent: %s" % nodeParent)
            parentItem = self.graphZone.getItemFromNodeName(nodeParent)
            parentItem.addChild(newItem)
        #-- Parent To World --#
        else:
            self.log.detail("\t ---> Adding graph item '%s' to world ..." % grapherItem._node.nodeName)
            self.addTopLevelItem(newItem)
        return newItem

    def selectionChanged(self, event, options):
        """
        Add options: Update selected / deselected node color
        """
        super(GraphTree, self).selectionChanged(event, options)
        for item in pQt.getAllItems(self):
            if item in self.selectedItems():
                item._widget.set_nodeColor((255, 255, 0, 255))
            else:
                item._widget.rf_nodeColor()

    def addTopLevelItem(self, QTreeWidgetItem):
        """
        Add options: Insert widget, refresh columns
        """
        super(GraphTree, self).addTopLevelItem(QTreeWidgetItem)
        QTreeWidgetItem._column = 0
        self.setItemWidget(QTreeWidgetItem, QTreeWidgetItem._column, QTreeWidgetItem._widget)
        self.rf_graphColumns()


class GraphItem(QtGui.QTreeWidgetItem):
    """
    GraphTree item, child of GrapherUi.GraphTree
    :param mainUi: Fondation main window
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
        Add options: Insert widget, refresh columns
        """
        super(GraphItem, self).addChild(QTreeWidgetItem)
        self._widget.set_expanded(True)
        QTreeWidgetItem._column = self._column + 1
        self.treeWidget().setItemWidget(QTreeWidgetItem, QTreeWidgetItem._column, QTreeWidgetItem._widget)
        self.treeWidget().rf_graphColumns()


class GraphWidget(QtGui.QWidget, graphNodeUI.Ui_wgGraphNode):
    """
    GraphTreeItem widget, child of GrapherUi.GraphTree.GraphItem
    :param pItem: Parent item
    :type pItem: QtGui.QTreeWidgetItem
    """

    def __init__(self, pItem):
        self.pItem = pItem
        self.mainUi = self.pItem.mainUi
        self.log = self.mainUi.log
        self.log.detail("\t ---> Init Graph Widget --#")
        self.pTree = self.pItem.treeWidget()
        self._item = self.pItem._item
        super(GraphWidget, self).__init__()
        self._setupWidget()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        self.log.detail("\t ---> Setup Graph Widget --#")
        self.setupUi(self)
        self.pbExpand.clicked.connect(self.set_expanded)
        self.rf_label()
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

    def rf_label(self):
        """
        Refresh graphNode label
        """
        self.lNodeName.setText(self._item._node.nodeName)

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
            self.pbEnable.setIcon(self.mainUi.enabledIcon)
        else:
            self.pbEnable.setIcon(self.mainUi.disabledIcon)

    def rf_expandIcon(self):
        """
        Refresh expand state icon
        """
        if self._item._node.nodeIsExpanded:
            self.pbExpand.setIcon(self.mainUi.collapseIcon)
        else:
            self.pbExpand.setIcon(self.mainUi.expandIcon)

    def set_nodeColor(self, rgba):
        """
        Set graphNode color (used for highlighting selected items)
        :param rgba: GraphNode color
        :type rgba: tuple
        """
        self.setStyleSheet("background-color: rgba(%s, %s, %s, %s)" % (rgba[0], rgba[1], rgba[2], rgba[3]))

    def set_expanded(self, state=None):
        """
        Set graphNode expanded with given state
        :param state: Expand state
        :type state: bool
        """
        if state is None:
            state = self.pbExpand.isChecked()
        else:
            self.pbExpand.setChecked(state)
        self._item._node.nodeIsExpanded = state
        self.pItem.setExpanded(state)
        self.rf_expandIcon()
