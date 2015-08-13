from pprint import pprint
from PyQt4 import QtGui
from lib.qt import procQt as pQt
from appli.fondation.gui.ui import graphNodeUI


class GraphTree(QtGui.QTreeWidget):
    """
    GraphTree widget, child of FondationUi
    :param mainUi: Fondation main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        super(GraphTree, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphTree Widget.")
        self._setupWidget()

    def _setupWidget(self):
        """
        Setup widget
        """
        self.log.debug("\t ---> Setup GraphTree Widget.")
        self.setStyleSheet("background-color: rgb(35, 35, 35)")
        self.setSelectionMode(QtGui.QTreeWidget.ExtendedSelection)
        self.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.setExpandsOnDoubleClick(False)
        self.setHeaderHidden(True)
        self.setColumnCount(12)
        self.setIndentation(0)
        self.rf_graphColumns()

    def _checkNodeName(self, nodeName):
        """
        Check new nodeName and return a unique name
        :param nodeName: New nodeName
        :type nodeName: str
        :return: New valide node name
        :rtype: str
        """
        rejected = [' ', '-', ',', ';', ':', '.', '/', '!', '?', '*', '$', '=', '+', '\'', '\\', '"', '&']
        #-- Check Rejected --#
        for r in rejected:
            if r in nodeName:
                nodeName.replace(r, '')
        #-- Check CamelCase --#
        if '_' in nodeName:
            if not nodeName.split('_')[-1].isdigit():
                nodeName.replace('_', '')
        #-- Check Index --#
        if not '_' in nodeName:
            nodeName = '%s_1' % nodeName
        #-- Check Unique Name --#
        founds = []
        for item in pQt.getAllItems(self):
            if nodeName == item.nodeName:
                if not item.nodeName in founds:
                    founds.append(item.nodeName)
            elif item.nodeName.startswith(nodeName.split('_')[0]):
                if not item.nodeName in founds:
                    founds.append(item.nodeName)
        #-- Result --#
        if not founds:
            return nodeName
        iList = []
        for f in founds:
            iList.append(int(f.split('_')[-1]))
        return '%s_%s' % (nodeName.split('_')[0], (max(iList) + 1))

    def _addGraphWidget(self, index, item):
        """
        Add graphNode widge to given item
        :param item: GraphNode item
        :type item: QtGui.QTreeWidgetItem
        """
        self.setItemWidget(item, index, item._widget)
        item._index = index
        item._widget.rf_nodeName()

    def rf_graphColumns(self):
        """
        Refresh graphTree column size
        """
        for n in range(self.columnCount()):
            self.resizeColumnToContents(n)

    def add_graphNode(self, nodeType='modul', nodeName=None):
        """
        Add new graphNode to tree
        :param nodeType: Graph node type ('modul', 'sysData', 'cmdData', 'pyData', 'loop', 'condition')
        :type nodeType: str
        :param nodeName: Graph node name
        :type nodeName: str
        """
        if nodeName is None:
            nodeName = '%s_1' % nodeType
        newNodeName = self._checkNodeName(nodeName)
        newItem = GraphItem(self.mainUi, nodeType, newNodeName)
        selItems = self.selectedItems()
        if len(selItems) == 1:
            selItems[0]._widget.pbExpand.setChecked(True)
            selItems[0]._widget.on_expandNode()
            selItems[0].addChild(newItem)
        else:
            self.addTopLevelItem(newItem)

    def selectionChanged(self, event, options):
        """
        Add options: Update selected / deselected node color
        """
        for item in pQt.getAllItems(self):
            if item in self.selectedItems():
                item._widget.rf_nodeColor(rgba=(255, 255, 0, 255))
            else:
                item._widget.rf_nodeColor()

    def addTopLevelItem(self, QTreeWidgetItem):
        """
        Add options: Insert widget, rf columns
        """
        super(GraphTree, self).addTopLevelItem(QTreeWidgetItem)
        self._addGraphWidget(0, QTreeWidgetItem)
        self.rf_graphColumns()

    def addTopLevelItems(self, list_of_QTreeWidgetItem):
        """
        Add options: Insert widget, rf columns
        """
        super(GraphTree, self).addTopLevelItems(list_of_QTreeWidgetItem)
        for QTreeWidgetItem in list_of_QTreeWidgetItem:
            self._addGraphWidget(0, QTreeWidgetItem)
        self.rf_graphColumns()


class GraphItem(QtGui.QTreeWidgetItem):
    """
    GraphTree item, child of FondationUi.GraphTree
    :param mainUi: Fondation main window
    :type mainUi: QtGui.QMainWindow
    :param nodeType: Graph node type ('modul', 'sysData', 'cmdData', 'pyData', 'loop', 'condition')
    :type nodeType: str
    :param nodeName: Graph node name
    :type nodeName: str
    """

    def __init__(self, mainUi, nodeType, nodeName):
        super(GraphItem, self).__init__()
        self.mainUi = mainUi
        self.nodeType = nodeType
        self.nodeName = nodeName
        self._index = None
        self._setupItem()

    def _setupItem(self):
        """
        Setup item
        """
        if self.nodeType == 'modul':
            self._widget = self.mainUi._graphNodes.Modul(pItem=self)
        elif self.nodeType == 'sysData':
            self._widget = self.mainUi._graphNodes.SysData(pItem=self)
        elif self.nodeType == 'cmdData':
            self._widget = self.mainUi._graphNodes.CmdData(pItem=self)
        elif self.nodeType == 'pyData':
            self._widget = self.mainUi._graphNodes.PyData(pItem=self)
        else:
            self._widget = self.mainUi._graphNodes.Modul(pItem=self)

    def addChild(self, QTreeWidgetItem):
        """
        Add options: Insert widget, rf columns
        """
        super(GraphItem, self).addChild(QTreeWidgetItem)
        self.treeWidget()._addGraphWidget((int(self._index) + 1), QTreeWidgetItem)
        self.treeWidget().rf_graphColumns()
        self._widget.rf_childEnableIcon()

    def addChildren(self, list_of_QTreeWidgetItem):
        """
        Add options: Insert widget, rf columns
        """
        super(GraphItem, self).addChildren(list_of_QTreeWidgetItem)
        for QTreeWidgetItem in list_of_QTreeWidgetItem:
            self.treeWidget()._addGraphWidget((int(self._index) + 1), QTreeWidgetItem)
        self.treeWidget().rf_graphColumns()
        self._widget.rf_childEnableIcon()


class GraphNode(QtGui.QWidget, graphNodeUI.Ui_wgGraphNode):

    def __init__(self, **kwargs):
        super(GraphNode, self).__init__()
        self._pItem = kwargs['pItem']
        self._pWidget = self._pItem.treeWidget()
        self._setupWidget()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        """
        Setup widget
        """
        self.setupUi(self)
        self.pbEnable.clicked.connect(self.on_enableNode)
        self.pbExpand.clicked.connect(self.on_expandNode)
        self.rf_nodeColor()
        self.rf_nodeEnableIcon()
        self.rf_nodeExpandIcon()

    @property
    def isEnable(self):
        """
        Get node enable state
        :return: Node enable state
        :rtype: bool
        """
        return self.pbEnable.isChecked()

    @property
    def isExpanded(self):
        """
        Get node expanded state
        :return: Node expanded state
        :rtype: bool
        """
        return self.pbExpand.isChecked()

    def rf_nodeName(self):
        """
        Refresh graphNode label
        """
        self.lNodeName.setText(self._pItem.nodeName)

    def rf_nodeColor(self, rgba=None):
        """
        Refresh graphNode color
        :param rgba: GraphNode color
        :type rgba: tuple
        """
        if rgba is None:
            rgba = self._nodeColor
        self.setStyleSheet("background-color: rgba(%s, %s, %s, %s)" % (rgba[0], rgba[1], rgba[2], rgba[3]))

    def rf_nodeEnableIcon(self):
        """
        Refresh enable state icon
        """
        if self.isEnable:
            self.pbEnable.setIcon(self._pItem.mainUi.enabledIcon)
        else:
            self.pbEnable.setIcon(self._pItem.mainUi.disabledIcon)

    def rf_childEnableIcon(self):
        """
        Refresh children enable state icon
        """
        for child in pQt.getAllChildren(self._pItem):
            if not child.nodeName == self._pItem.nodeName:
                #-- Edit Child Node --#
                if child.parent()._widget.isEnable and child.parent()._widget.lNodeName.isEnabled():
                    child._widget.pbEnable.setEnabled(self.isEnable)
                    if child._widget.isEnable:
                        child._widget.lNodeName.setEnabled(self.isEnable)
                    else:
                        child._widget.lNodeName.setEnabled(False)
                else:
                    child._widget.lNodeName.setEnabled(False)
                    child._widget.pbEnable.setEnabled(False)
            #-- Refresh --#
            child._widget.rf_nodeEnableIcon()

    def rf_nodeExpandIcon(self):
        """
        Refresh expand state icon
        """
        if self.isExpanded:
            self.pbExpand.setIcon(self._pItem.mainUi.collapseIcon)
        else:
            self.pbExpand.setIcon(self._pItem.mainUi.expandIcon)

    def on_enableNode(self):
        """
        Command launched when 'Enable' QPushButton is clicked.
        Refresh graphNodes enable state
        """
        self.lNodeName.setEnabled(self.isEnable)
        self.rf_childEnableIcon()
        self.rf_nodeEnableIcon()

    def on_expandNode(self):
        """
        Command launched when 'Expand' QPushButton is clicked.
        Expand item
        """
        self._pItem.setExpanded(self.isExpanded)
        self.rf_nodeExpandIcon()
