import pprint
from PyQt4 import QtGui
from lib.qt import procQt as pQt
from appli.grapher.gui.ui import graphNodeUI


class GraphTree(QtGui.QTreeWidget):
    """
    GraphTree widget, child of GrapherUi
    :param _mainUi: Fondation main window
    :type _mainUi: QtGui.QMainWindow
    """

    def __init__(self, _mainUi):
        super(GraphTree, self).__init__()
        self._mainUi = _mainUi
        self.log = self._mainUi.log
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

    def _addGraphWidget(self, cIndex, item):
        """
        Add graphNode widget to given item
        :param cIndex: Column index
        :type cIndex: int
        :param item: GraphNode item
        :type item: QtGui.QTreeWidgetItem
        """
        self.setItemWidget(item, cIndex, item._widget)
        item._column = cIndex
        item._widget.rf_nodeName()

    def getSelectedNodes(self):
        """
        Get selected node names
        :return: Selected node nales
        :rtype: list
        """
        nodes = []
        for item in self.selectedItems() or []:
            nodes.append(item.nodeName)
        return nodes

    def getItemFromNodeName(self, nodeName):
        """
        Get graphItem from given node name
        :param nodeName: Graph node name
        :type nodeName: str
        :return: Graph item
        :rtype: QtGui.QTreeWidgetItem
        """
        for item in pQt.getAllItems(self):
            if item.nodeName == nodeName:
                return item

    def rf_graphColumns(self):
        """
        Refresh graphTree column size
        """
        for n in range(self.columnCount()):
            self.resizeColumnToContents(n)

    def add_graphNode(self, nodeType='modul', nodeName=None, nodeParent=None, index=None):
        """
        Add new graphNode to tree
        :param nodeType: Graph node type ('modul', 'sysData', 'cmdData', 'pyData', 'loop', 'condition')
        :type nodeType: str
        :param nodeName: Graph node name
        :type nodeName: str
        :param nodeParent: Parent node name
        :type nodeParent: str
        :param index: Index for insertion
        :type index: int
        :return: New item
        :rtype: QtGui.QTreeWidgetItem
        """
        #-- Create New Item --#
        if nodeName is None:
            nodeName = '%s_1' % nodeType
        newNodeName = self._checkNodeName(nodeName)
        self._mainUi.log.debug("#-- + Creating %s Node + : %s --#" % (nodeType, newNodeName))
        newItem = GraphItem(self._mainUi, nodeType, newNodeName)

        #-- Add Node Method --#
        def __addNode(item):
            """ Add given item dans refreh ui """
            item._widget.pbExpand.setChecked(True)
            item._widget.on_expandNode()
            if index is None:
                item.addChild(newItem)
            else:
                item.insertChild(index, newItem)
            item._widget.rf_expandVis()

        #-- Use Given Parent --#
        if nodeParent is not None:
            item = self.getItemFromNodeName(nodeParent)
            __addNode(item)
        #-- Use Ui Selection --#
        else:
            selItems = self.selectedItems()
            #-- Parent To Selected Node --#
            if len(selItems) == 1:
                __addNode(selItems[0])
            #-- Parent To World --#
            else:
                if index is None:
                    self.addTopLevelItem(newItem)
                else:
                    self.insertTopLevelItem(index, newItem)
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

    def foldUnfold(self, expand=True, _mode='sel', toggle=False):
        """
        Manage graphNodes folding and unfolding command
        :param expand: Expand state
        :type expand: bool
        :param _mode: 'sel', 'branch', 'active', or 'all'
        :type _mode: str
        :param toggle: Enable automatic switch
        :type toggle: bool
        """
        if _mode in ['sel', 'branch']:
            for item in self.selectedItems() or []:
                if toggle:
                    item._widget.pbExpand.setChecked(not item._widget.pbExpand.isChecked())
                else:
                    item._widget.pbExpand.setChecked(expand)
                    if _mode == 'branch':
                        if item.childCount():
                            for cItem in pQt.getAllChildren(item):
                                if not cItem.nodeName == item.nodeName:
                                    cItem._widget.pbExpand.setChecked(expand)
                                    cItem._widget.on_expandNode()
                item._widget.on_expandNode()
        elif _mode in ['active', 'inactive', 'all']:
            for item in pQt.getAllItems(self):
                if _mode == 'all':
                    item._widget.pbExpand.setChecked(expand)
                elif _mode == 'active':
                    if item._widget.isEnable:
                        item._widget.pbExpand.setChecked(expand)
                    else:
                        item._widget.pbExpand.setChecked(not expand)
                elif _mode == 'inactive':
                    if not item._widget.isEnable:
                        item._widget.pbExpand.setChecked(expand)
                    else:
                        item._widget.pbExpand.setChecked(not expand)
                item._widget.on_expandNode()

    def copyNodes(self, items=None, _mode='nodes', rm=False):
        """
        Copy / Cut selected nodes or branch
        :param items: Force using given nodes
        :type items: list
        :param _mode: 'nodes' or 'branch'
        :type _mode: str
        :param rm: Remove selected nodes (cut)
        :type rm: bool
        """
        #-- Collecte Info --#
        self.buffer = dict()
        if items is None:
            selItems = self.selectedItems() or []
        else:
            if items == '':
                selItems = []
            else:
                selItems = items
        treeDict = self.__repr__()
        if selItems:
            self.log.debug("Storing selected nodes ...")
            #-- Store Selected Nodes --#
            for n, item in enumerate(selItems):
                nodeDict = self._mainUi.getNodeDictFromNodeName(treeDict, item.nodeName)
                self.buffer[n] = dict(nodeName=item.nodeName, nodeChildren={}, nodeDict=nodeDict)
                if _mode == 'branch':
                    if item.childCount():
                        #-- Store Children --#
                        for c, child in enumerate(pQt.getAllChildren(item)):
                            if not child.nodeName == item.nodeName:
                                childDict = self._mainUi.getNodeDictFromNodeName(treeDict, child.nodeName)
                                self.buffer[n]['nodeChildren'][c] = childDict
            #-- Delete For cut --#
            if rm:
                self.deleteSelectedNodes()

    def pasteNodes(self, dstItem=None, index=None):
        """
        Paste stored node
        :param dstItem: Destination graph item
        :type dstItem: QtGui.QTreeWidgetItem
        :param index: Index for insertion
        :type index: int
        :return: Pasted items
        :rtype: list
        """
        if self.buffer is not None:
            self.log.debug("Pasting Stored nodes ...")
            #-- Get Destination items --#
            if dstItem is None:
                selItems = self.selectedItems() or []
            else:
                selItems = [dstItem]
            #-- Paste Nodes --#
            items = {}
            for n in sorted(self.buffer.keys()):
                nodeDict = self.buffer[n]
                newNodeName = self._checkNodeName(nodeDict['nodeName'])
                newItem = None
                #-- Parent To World --#
                if len(selItems) == 0:
                    self.log.detail("\t ---> Paste Node to world ...")
                    newItem = self.add_graphNode(nodeType=nodeDict['nodeDict']['_nodeType'],
                                                 nodeName=newNodeName, index=index)
                #-- Parent To Node --#
                elif len(selItems) == 1:
                    self.log.detail("\t ---> Paste Node to %s ..." % selItems[0].nodeName)
                    newItem = self.add_graphNode(nodeType=nodeDict['nodeDict']['_nodeType'], nodeName=newNodeName,
                                                 nodeParent=selItems[0].nodeName, index=index)
                #-- Parent Child Node --#
                if newItem is not None:
                    items[newItem] = nodeDict['nodeDict']
                    if nodeDict['nodeChildren'].keys():
                        #-- Check First Parent --#
                        for c in sorted(nodeDict['nodeChildren'].keys()):
                            if nodeDict['nodeChildren'][c]['_nodeParent'] == self.buffer[n]['nodeName']:
                                nodeDict['nodeChildren'][c]['_nodeParent'] = newNodeName
                        #-- Build Child Branch --#
                        self.buildGraph(nodeDict['nodeChildren'])
            #-- Edit Nodes --#
            if items:
                for k, v in items.iteritems():
                    k._widget.update(**v)
                return items.keys()

    def moveNodes(self, side='up'):
        """
        Move selected nodes
        :param side: 'up', 'down'
        :type side: str
        """
        #-- Collecte Info --#
        selItems = self.selectedItems() or []
        if selItems:
            self.log.debug("Moving selected nodes ...")
            pastedItems = None
            for n, item in enumerate(selItems):
                pItem = item.parent()
                newIndex = self._insertIndex(item, pItem, side)
                #-- Move Nodes --#
                if newIndex is not None:
                    self.copyNodes(items=[item], _mode='branch', rm=True)
                    pastedItems = self.pasteNodes(dstItem=pItem, index=newIndex)
                else:
                    self.log.detail("!!! WARNING: Can not move item outside range !!!")
            #-- Reselect --#
            if pastedItems is not None:
                self.clearSelection()
                for item in pastedItems:
                    item.setSelected(True)
            #-- Clear Buffer --#
            self.buffer = None

    def _insertIndex(self, item, pItem, side):
        """
        Get new insertion index
        :param item: Graph item to move
        :type item: QtGui.QTreeWidgetItem
        :param pItem: Graph parent item
        :type pItem: QtGui.QTreeWidgetItem
        :param side: 'up', 'down'
        :type side: str
        :return: New index
        :rtype: int
        """
        #-- Get Current Index --#
        if pItem is None:
            index = self.indexOfTopLevelItem(item)
            iCount = self.topLevelItemCount()
        else:
            index = pItem.indexOfChild(item)
            iCount = pItem.childCount()
        #- Side Up New Index --#
        if side == 'up':
            if index > 0:
                newIndex = index - 1
            else:
                newIndex = None
        #-- Side Down New Index --#
        else:
            if index < (iCount - 1):
                newIndex = index + 1
            else:
                newIndex = None
        return newIndex

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
            self._mainUi.log.debug("#-- - Deleting %s Node - : %s --#" % (item._nodeType, item.nodeName))
            if not item._column == 0:
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
        Add options: Insert widget, refresh columns
        """
        super(GraphTree, self).addTopLevelItem(QTreeWidgetItem)
        self._addGraphWidget(0, QTreeWidgetItem)
        self.rf_graphColumns()

    def addTopLevelItems(self, list_of_QTreeWidgetItem):
        """
        Add options: Insert widget, refresh columns
        """
        super(GraphTree, self).addTopLevelItems(list_of_QTreeWidgetItem)
        for QTreeWidgetItem in list_of_QTreeWidgetItem:
            self._addGraphWidget(0, QTreeWidgetItem)
        self.rf_graphColumns()

    def insertTopLevelItem(self, p_int, QTreeWidgetItem):
        """
        Add options: Insert widget, refresh columns
        """
        super(GraphTree, self).insertTopLevelItem(p_int, QTreeWidgetItem)
        self._addGraphWidget(0, QTreeWidgetItem)
        self.rf_graphColumns()

    def insertTopLevelItems(self, p_int, list_of_QTreeWidgetItem):
        """
        Add options: Insert widget, refresh columns
        """
        super(GraphTree, self).insertTopLevelItems(p_int, list_of_QTreeWidgetItem)
        for QTreeWidgetItem in list_of_QTreeWidgetItem:
            self._addGraphWidget(0, QTreeWidgetItem)
        self.rf_graphColumns()


class GraphItem(QtGui.QTreeWidgetItem):
    """
    GraphTree item, child of GrapherUi.GraphTree
    :param _mainUi: Fondation main window
    :type _mainUi: QtGui.QMainWindow
    :param nodeType: Graph node type ('modul', 'sysData', 'cmdData', 'pyData', 'loop', 'condition')
    :type nodeType: str
    :param nodeName: Graph node name
    :type nodeName: str
    """

    def __init__(self, _mainUi, nodeType, nodeName):
        super(GraphItem, self).__init__()
        self._mainUi = _mainUi
        self._nodeType = nodeType
        self.nodeName = nodeName
        self._column = None
        self._setupItem()

    def _setupItem(self):
        if self._nodeType == 'modul':
            self._widget = self._mainUi._graphNodes.Modul(_pItem=self)
        elif self._nodeType == 'sysData':
            self._widget = self._mainUi._graphNodes.SysData(_pItem=self)
        elif self._nodeType == 'cmdData':
            self._widget = self._mainUi._graphNodes.CmdData(_pItem=self)
        elif self._nodeType == 'pyData':
            self._widget = self._mainUi._graphNodes.PyData(_pItem=self)
        else:
            self._widget = self._mainUi._graphNodes.Modul(_pItem=self)

    def addChild(self, QTreeWidgetItem):
        """
        Add options: Insert widget, refresh columns
        """
        super(GraphItem, self).addChild(QTreeWidgetItem)
        self.treeWidget()._addGraphWidget((int(self._column) + 1), QTreeWidgetItem)
        self.treeWidget().rf_graphColumns()
        self._widget.rf_childEnableIcon()

    def addChildren(self, list_of_QTreeWidgetItem):
        """
        Add options: Insert widget, refresh columns
        """
        super(GraphItem, self).addChildren(list_of_QTreeWidgetItem)
        for QTreeWidgetItem in list_of_QTreeWidgetItem:
            self.treeWidget()._addGraphWidget((int(self._column) + 1), QTreeWidgetItem)
        self.treeWidget().rf_graphColumns()
        self._widget.rf_childEnableIcon()

    def insertChild(self, p_int, QTreeWidgetItem):
        """
        Add options: Insert widget, refresh columns
        """
        super(GraphItem, self).insertChild(p_int, QTreeWidgetItem)
        self.treeWidget()._addGraphWidget((int(self._column) + 1), QTreeWidgetItem)
        self.treeWidget().rf_graphColumns()
        self._widget.rf_childEnableIcon()

    def insertChildren(self, p_int, list_of_QTreeWidgetItem):
        """
        Add options: Insert widget, refresh columns
        """
        super(GraphItem, self).insertChildren(p_int, list_of_QTreeWidgetItem)
        for QTreeWidgetItem in list_of_QTreeWidgetItem:
            self.treeWidget()._addGraphWidget((int(self._column) + 1), QTreeWidgetItem)
        self.treeWidget().rf_graphColumns()
        self._widget.rf_childEnableIcon()


class GraphNode(QtGui.QWidget, graphNodeUI.Ui_wgGraphNode):
    """
    GraphTreeItem widget, child of GrapherUi.GraphTree.GraphItem
    :param kwargs: GraphNode internal params
    :type kwargs: dict
    """

    def __init__(self, **kwargs):
        super(GraphNode, self).__init__()
        self._pItem = kwargs['_pItem']
        self._pWidget = self._pItem.treeWidget()
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
        if self._pItem.parent() is None:
            nodeParent = None
        else:
            nodeParent = self._pItem.parent().nodeName
        #-- Fill Internal --#
        nodeDict = dict(_nodeName=self._pItem.nodeName, _nodeType=self._pItem._nodeType, _nodeParent=nodeParent,
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
            self.pbEnable.setIcon(self._pItem._mainUi.enabledIcon)
        else:
            self.pbEnable.setIcon(self._pItem._mainUi.disabledIcon)

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

    def rf_expandVis(self):
        """
        Refresh expand button visibility
        """
        if self._pItem.childCount():
            self.pbExpand.setVisible(True)
        else:
            self.pbExpand.setVisible(False)

    def rf_nodeExpandIcon(self):
        """
        Refresh expand state icon
        """
        if self.isExpanded:
            self.pbExpand.setIcon(self._pItem._mainUi.collapseIcon)
        else:
            self.pbExpand.setIcon(self._pItem._mainUi.expandIcon)

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
