import pprint
from PyQt4 import QtGui, QtCore
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
        self.buffer = None
        self._setupWidget()

    def __repr__(self):
        """
        GraphTree representation as dict
        :return: Tree contents
        :rtype: dict
        """
        treeDict = dict()
        #-- Collecte Nodes Dict --#
        for n, item in enumerate(pQt.getAllItems(self)):
            treeDict[n] = item._widget.__repr__()
            item._widget.__repr__()
        #-- Result --#
        return treeDict

    def __str__(self):
        """
        GraphTree representation as str
        :return: Tree contents
        :rtype: str
        """
        return pprint.pformat(self.__repr__())

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
        #-- Find Same Base Name --#
        founds = []
        for item in pQt.getAllItems(self):
            if nodeName == item.nodeName:
                if not item.nodeName in founds:
                    founds.append(item.nodeName)
            elif item.nodeName.startswith(nodeName.split('_')[0]):
                if not item.nodeName in founds:
                    founds.append(item.nodeName)
        #-- Result: Name Is Unique --#
        if not founds or not nodeName in founds:
            return nodeName
        #-- Result: Generate Unique Name --#
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

    def getSelectedNodes(self):
        nodes = []
        for item in self.selectedItems() or []:
            nodes.append(item.nodeName)
        return nodes

    def getItemFromNodeName(self, nodeName):
        for item in pQt.getAllItems(self):
            if item.nodeName == nodeName:
                return item

    def rf_graphColumns(self):
        """
        Refresh graphTree column size
        """
        for n in range(self.columnCount()):
            self.resizeColumnToContents(n)

    def add_graphNode(self, nodeType='modul', nodeName=None, nodeParent=None):
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
        #-- Create New Item --#
        if nodeName is None:
            nodeName = '%s_1' % nodeType
        newNodeName = self._checkNodeName(nodeName)
        self.mainUi.log.debug("#-- + Creating %s Node + : %s --#" % (nodeType, newNodeName))
        newItem = GraphItem(self.mainUi, nodeType, newNodeName)
        #-- Use Given Parent --#
        if nodeParent is not None:
            item = self.getItemFromNodeName(nodeParent)
            item._widget.pbExpand.setChecked(True)
            item._widget.on_expandNode()
            item.addChild(newItem)
            item._widget.rf_expandVis()
        #-- Use Ui Selection --#
        else:
            selItems = self.selectedItems()
            #-- Parent To Selected Node --#
            if len(selItems) == 1:
                selItems[0]._widget.pbExpand.setChecked(True)
                selItems[0]._widget.on_expandNode()
                selItems[0].addChild(newItem)
                selItems[0]._widget.rf_expandVis()
            #-- Parent To World --#
            else:
                self.addTopLevelItem(newItem)
        #-- Result --#
        return newItem

    def buildGraph(self, treeDict):
        """
        Build graph tree from given params
        :param treeDict: Tree params
        :type treeDict: dict
        """
        self.log.debug("Building Graph ...")
        #-- Create Nodes --#
        items = {}
        for n in sorted(treeDict.keys()):
            newItem = self.add_graphNode(nodeType=treeDict[n]['_nodeType'], nodeName=treeDict[n]['_nodeName'],
                                         nodeParent=treeDict[n]['_nodeParent'])
            items[newItem] = treeDict[n]
        #-- Edit Nodes --#
        for k, v in items.iteritems():
            k._widget.update(**v)

    def foldUnfold(self, expand=True, _mode='sel'):
        """
        Manage graphNodes folding and unfolding command
        :param expand: Expand state
        :type expand: bool
        :param _mode: 'sel' or 'all'
        :type _mode: str
        """
        if _mode == 'sel':
            for item in self.selectedItems() or []:
                item._widget.pbExpand.setChecked(not item._widget.pbExpand.isChecked())
                item._widget.on_expandNode()
        else:
            for item in pQt.getAllItems(self):
                item._widget.pbExpand.setChecked(expand)
                item._widget.on_expandNode()

    def copyNodes(self, _mode='nodes', rm=False):
        """
        Copy / Cut selected nodes or branch
        :param _mode: 'nodes' or 'branch'
        :type _mode: str
        :param rm: Remove selected nodes (cut)
        :type rm: bool
        """
        #-- Collecte Info --#
        self.buffer = dict()
        selItems = self.selectedItems() or []
        treeDict = self.__repr__()
        if selItems:
            self.log.debug("Storing selected nodes ...")
            #-- Store Selected Nodes --#
            for n, item in enumerate(selItems):
                nodeDict = self.mainUi.getNodeDictFromNodeName(treeDict, item.nodeName)
                self.buffer[n] = dict(nodeName=item.nodeName, nodeChildren={}, nodeDict=nodeDict)
                if _mode == 'branch':
                    if item.childCount() and len:
                        #-- Store Children --#
                        for c, child in enumerate(pQt.getAllChildren(item)):
                            if not child.nodeName == item.nodeName:
                                childDict = self.mainUi.getNodeDictFromNodeName(treeDict, child.nodeName)
                                self.buffer[n]['nodeChildren'][c] = childDict
            #-- Delete For cut --#
            if rm:
                self.deleteSelectedNodes()

    def pasteNodes(self):
        """
        Paste stored node
        """
        if self.buffer is not None:
            self.log.debug("Pasting Stored nodes ...")
            items = {}
            selItems = self.selectedItems() or []
            #-- Parent Top Node --#
            for n in sorted(self.buffer.keys()):
                nodeDict = self.buffer[n]
                newNodeName = self._checkNodeName(nodeDict['nodeName'])
                newItem = None
                #-- Parent To World --#
                if len(selItems) == 0:
                    self.log.detail("\t ---> Paste Node to world ...")
                    newItem = self.add_graphNode(nodeType=nodeDict['nodeDict']['_nodeType'],
                                                 nodeName=newNodeName)
                #-- Parent To Node --#
                elif len(selItems) == 1:
                    self.log.detail("\t ---> Paste Node to %s ..." % selItems[0].nodeName)
                    newItem = self.add_graphNode(nodeType=nodeDict['nodeDict']['_nodeType'],
                                                 nodeName=newNodeName, nodeParent=selItems[0].nodeName)
                #-- Parent Child Node --#
                if newItem is not None:
                    items[newItem] = nodeDict['nodeDict']
                    if nodeDict['nodeChildren'].keys():
                        for c in sorted(nodeDict['nodeChildren'].keys()):
                            childDict = nodeDict['nodeChildren'][c]
                            #-- Check First Parent --#
                            if childDict['_nodeParent'] == self.buffer[n]['nodeName']:
                                nodeParent = newNodeName
                            else:
                                nodeParent = childDict['_nodeParent']
                            #-- Parent To Node --#
                            self.log.detail("\t\t ---> Paste Child to %s ..." % nodeParent)
                            newItem = self.add_graphNode(nodeType=childDict['_nodeType'],
                                                         nodeName=childDict['_nodeName'], nodeParent=nodeParent)
                            items[newItem] = childDict
            #-- Edit Nodes --#
            if items:
                for k, v in items.iteritems():
                    k._widget.update(**v)

    def deleteSelectedNodes(self, nodes=None):
        """
        Delete selected graph nodes
        :param nodes: Delete given nodes without consideration for GraphTree selection
        :type nodes: list
        """
        #-- Collecte Info --#
        if nodes is None:
            selItems = self.selectedItems() or []
        else:
            selItems = nodes
        selItems.reverse()
        #-- Deleting Nodes --#
        for item in selItems:
            self.mainUi.log.debug("#-- - Deleting %s Node - : %s --#" % (item._nodeType, item.nodeName))
            if not item._index == 0:
                for n in range(item.parent().childCount()):
                    if item.parent() is not None:
                        parentItem = item.parent()
                        if item.nodeName == parentItem.child(n).nodeName:
                            parentItem.removeChild(item)
                            #-- Refresh --#
                            parentItem._widget.rf_expandVis()
                            parentItem._widget.rf_nodeExpandIcon()
            else:
                self.takeTopLevelItem(self.indexOfTopLevelItem(item))

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
        self._nodeType = nodeType
        self.nodeName = nodeName
        self._index = None
        self._setupItem()

    def _setupItem(self):
        if self._nodeType == 'modul':
            self._widget = self.mainUi._graphNodes.Modul(pItem=self)
        elif self._nodeType == 'sysData':
            self._widget = self.mainUi._graphNodes.SysData(pItem=self)
        elif self._nodeType == 'cmdData':
            self._widget = self.mainUi._graphNodes.CmdData(pItem=self)
        elif self._nodeType == 'pyData':
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
    """
    GraphTreeItem widget, child of FondationUi.GraphTree.GraphItem
    :param kwargs: GraphNode internal params
    :type kwargs: dict
    """

    def __init__(self, **kwargs):
        super(GraphNode, self).__init__()
        self.pItem = kwargs['pItem']
        self.pWidget = self.pItem.treeWidget()
        self._setupWidget()
        #-- Common Attributes --#
        self.nodeVersions = {0: "Default Version"}
        self.nodeVersion = 0

    def __repr__(self):
        """
        Node params representation as dict
        :return: Node params
        :rtype: dict
        """
        #-- Get Parent Node Name --#
        if self.pItem.parent() is None:
            nodeParent = None
        else:
            nodeParent = self.pItem.parent().nodeName
        #-- Fill Internal --#
        nodeDict = dict(_nodeName=self.pItem.nodeName, _nodeType=self.pItem._nodeType, _nodeParent=nodeParent,
                        _nodeIsEnabled=self.isEnable, _nodeIsExpanded=self.isExpanded)
        #-- Fill Node Params --#
        for k, v in self.__dict__.iteritems():
            if k.startswith('node'):
                nodeDict[k] = v
        #-- Result --#
        return nodeDict

    def __str__(self):
        """
        Node params representation as str
        :return: Node params
        :rtype: str
        """
        return pprint.pformat(self.__repr__())

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        self.setupUi(self)
        self.pbEnable.clicked.connect(self.on_enableNode)
        self.pbExpand.clicked.connect(self.on_expandNode)
        self.pbExpand.setVisible(False)
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
        self.lNodeName.setText(self.pItem.nodeName)

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
            self.pbEnable.setIcon(self.pItem.mainUi.enabledIcon)
        else:
            self.pbEnable.setIcon(self.pItem.mainUi.disabledIcon)

    def rf_childEnableIcon(self):
        """
        Refresh children enable state icon
        """
        for child in pQt.getAllChildren(self.pItem):
            if not child.nodeName == self.pItem.nodeName:
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

    def rf_expandVis(self):
        """
        Refresh expand button visibility
        """
        if self.pItem.childCount():
            self.pbExpand.setVisible(True)
        else:
            self.pbExpand.setVisible(False)

    def rf_nodeExpandIcon(self):
        """
        Refresh expand state icon
        """
        if self.isExpanded:
            self.pbExpand.setIcon(self.pItem.mainUi.collapseIcon)
        else:
            self.pbExpand.setIcon(self.pItem.mainUi.expandIcon)

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
        self.pItem.setExpanded(self.isExpanded)
        self.rf_nodeExpandIcon()

    def update(self, **kwargs):
        """
        Update node params
        :param kwargs: Node params
        :type kwargs: dict
        """
        #-- Update Internal --#
        self.pbEnable.setChecked(kwargs['_nodeIsEnabled'])
        self.on_enableNode()
        self.pbExpand.setChecked(kwargs['_nodeIsExpanded'])
        self.on_expandNode()
