from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from appli.grapher.ui import graphNodeUI


class GraphTree(QtGui.QTreeWidget):

    def __init__(self, ui):
        self._ui = ui
        self.log = self._ui.log
        super(GraphTree, self).__init__()
        self._setupWidget()

    def _setupWidget(self):
        """ Setup Graph widget """
        self.log.debug("#-- Setup Graph Widget --#")
        self.setHeaderHidden(True)
        self.setItemsExpandable(True)
        self.setColumnCount(10)
        self.setIndentation(0)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.setSelectionMode(QtGui.QTreeWidget.ExtendedSelection)
        self.connect(self, QtCore.SIGNAL('customContextMenuRequested(const QPoint&)'), self.on_popUpMenu)

    def rf_graphColumns(self):
        """ Refresh graph columns size """
        for item in pQt.getAllItems(self):
            item._widget.rf_childIndicator()
        for column in range(self.columnCount()):
            self.resizeColumnToContents(column)

    def on_popUpMenu(self, point):
        """ Command launched when right click is done
            :param point: (object) : Qt position """
        self._ui.mGraph.exec_(self.mapToGlobal(point))

    def on_newNode(self):
        """ Command launch when menuItem 'New Node' is clicked
            :return: (object) : QTreeWidgetItem """
        selItems = self.selectedItems()
        defaultAttr = {'nodeName': "New Node", 'nodeType': "modul", 'nodeInstance': None, 'nodeVersion': "001",
                       'nodeVTitle': {'001': "New Version"}}
        if not len(selItems) > 1:
            if selItems:
                newItem = self.addGraphNode(parent=selItems[0], index=(selItems[0]._index + 1), **defaultAttr)
            else:
                newItem = self.addGraphNode(**defaultAttr)
            return newItem
        else:
            self._ui._errorDialog("!!! Warning: Select only one node !!!", self)

    def addGraphNode(self, parent=None, **kwargs):
        """ Add new QTreeWidgetItem
            :param kwargs: (dict) : Node params
            :return: (object) : QTreeWidgetItem """
        if parent is None:
            index = 0
        else:
            index = (parent._index + 1)
        newItem = self.new_graphItem(index)
        if parent is None:
            self.addTopLevelItem(newItem)
        else:
            parent.addChild(newItem)
        self.setItemWidget(newItem, index, newItem._widget)
        self.rf_graphColumns()
        return newItem

    @staticmethod
    def new_graphItem(index):
        """ Create new graph QTreeWidgetItem
            :param index: (int) : Column index
            :return: (object) : QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem._index = index
        newItem._widget = GraphNode(newItem)
        return newItem


class GraphNode(QtGui.QWidget, graphNodeUI.Ui_graphNode):

    def __init__(self, graphItem):
        self.graphItem = graphItem
        super(GraphNode, self).__init__()
        self._setupUi()

    @property
    def tree(self):
        return self.graphItem.treeWidget()

    @property
    def _ui(self):
        return self.tree._ui

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup GraphNode widget """
        self.setupUi(self)
        self.pbExpand.clicked.connect(self.on_expandNode)

    def rf_childIndicator(self):
        """ Refresh children indicator """
        if self.graphItem.childCount() > 0:
            self.lChildIndicator.setText(" c ")
        else:
            self.lChildIndicator.setText("")

    def on_expandNode(self):
        """ Expand or collapse item """
        self.setGraphNodeExpanded(not self.graphItem.isExpanded())

    def setGraphNodeExpanded(self, state):
        """ Edit graphNode QTreeWidgetItem state
            :param state: (bool) : QTreeWidgetItem state """
        self.graphItem.setExpanded(state)
        if state:
            self.pbExpand.setText('-')
        else:
            self.pbExpand.setText('+')
        self.tree.rf_graphColumns()
