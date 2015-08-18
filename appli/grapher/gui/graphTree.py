import pprint
from PyQt4 import QtGui
from lib.qt import procQt as pQt
from appli.grapher.gui import graphNodes
from appli.grapher.gui.ui import graphNodeUI


class TreeView(object):
    """
    TreeView widget, child of GrapherUi
    :param mainUi: Fondation main window
    :type mainUi: QtGui.QMainWindow
    """
    
    def __init__(self, mainUi, graphTree):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init TreeView Widget.")
        self.tree = graphTree
        self.tree.view = self
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
            index = self.tree.indexOfTopLevelItem(item)
            iCount = self.tree.topLevelItemCount()
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

    def newNode(self):
        """
        Create a default new node (modul)
        :return: New GraphItem
        :rtype: QtGui.QTreeWidgetItem
        """
        return self.tree.createGraphNode()

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
            #-- Mode Selection --#
            for item in self.tree.selectedItems() or []:
                if toggle:
                    item._widget.setExpanded(not item._widget.pbExpand.isChecked())
                else:
                    item._widget.setExpanded(expand)
                    #-- Mode Branch --#
                    if _mode == 'branch':
                        if item.childCount():
                            for cItem in pQt.getAllChildren(item):
                                if not cItem.nodeName == item.nodeName:
                                    cItem._widget.setExpanded(expand)
        elif _mode in ['active', 'all']:
            for item in pQt.getAllItems(self.tree):
                #-- Mode All --#
                if _mode == 'all':
                    item._widget.setExpanded(expand)
                #-- Mode Active --#
                elif _mode == 'active':
                    if item._widget.isEnable:
                        item._widget.setExpanded(expand)
                    else:
                        item._widget.setExpanded(not expand)

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
            selItems = self.tree.selectedItems() or []
        else:
            if items == '':
                selItems = []
            else:
                selItems = items
        treeDict = self.tree.__repr__()
        if selItems:
            self.log.debug("Storing selected nodes ...")
            #-- Store Selected Nodes --#
            for n, item in enumerate(selItems):
                nodeDict = self.mainUi.getNodeDictFromNodeName(treeDict, item.nodeName)
                self.buffer[n] = dict(nodeName=item.nodeName, nodeChildren={}, nodeDict=nodeDict)
                if _mode == 'branch':
                    if item.childCount():
                        #-- Store Children --#
                        for c, child in enumerate(pQt.getAllChildren(item)):
                            if not child.nodeName == item.nodeName:
                                childDict = self.mainUi.getNodeDictFromNodeName(treeDict, child.nodeName)
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
                selItems = self.tree.selectedItems() or []
            else:
                selItems = [dstItem]
            #-- Paste Nodes --#
            items = {}
            for n in sorted(self.buffer.keys()):
                nodeDict = self.buffer[n]
                newNodeName = self.mainUi._checkNodeName(nodeDict['nodeName'], pQt.getAllItems(self.tree))
                newItem = None
                #-- Parent To World --#
                if len(selItems) == 0:
                    self.log.detail("\t ---> Paste Node to world ...")
                    newItem = self.tree.createGraphNode(nodeType=nodeDict['nodeDict']['_nodeType'],
                                                        nodeName=newNodeName, index=index)
                #-- Parent To Node --#
                elif len(selItems) == 1:
                    self.log.detail("\t ---> Paste Node to %s ..." % selItems[0].nodeName)
                    newItem = self.tree.createGraphNode(nodeType=nodeDict['nodeDict']['_nodeType'],
                                                        nodeName=newNodeName, nodeParent=selItems[0].nodeName,
                                                        index=index)
                #-- Parent Child Node --#
                if newItem is not None:
                    items[newItem] = nodeDict['nodeDict']
                    if nodeDict['nodeChildren'].keys():
                        #-- Check First Parent --#
                        for c in sorted(nodeDict['nodeChildren'].keys()):
                            if nodeDict['nodeChildren'][c]['_nodeParent'] == self.buffer[n]['nodeName']:
                                nodeDict['nodeChildren'][c]['_nodeParent'] = newNodeName
                        #-- Build Child Branch --#
                        self.tree.buildGraph(nodeDict['nodeChildren'])
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
        selItems = self.tree.selectedItems() or []
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
                self.tree.clearSelection()
                for item in pastedItems:
                    item.setSelected(True)
            #-- Clear Buffer --#
            self.buffer = None

    def deleteSelectedNodes(self):
        """
        Delete selected graphNodes
        """
        selItems = self.tree.selectedItems()
        if selItems:
            self.tree.deleteNodes(selItems)


class GraphTree(QtGui.QTreeWidget):
    """
    GraphTree widget, child of GrapherUi
    :param mainUi: Fondation main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        super(GraphTree, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphTree Widget.")
        self.view = None
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

    def buildGraph(self, treeDict):
        """
        Build graph tree from given params
        :param treeDict: Tree params
        :type treeDict: dict
        """
        self.log.debug("#-- Build Graph --#" , newLinesBefor=1)
        #-- Create Nodes --#
        self.log.debug("Creating Nodes ...")
        for n in sorted(treeDict.keys()):
            newItem = self.createGraphNode(nodeType=treeDict[n]['_nodeType'], nodeName=treeDict[n]['_nodeName'],
                                           nodeParent=treeDict[n]['_nodeParent'])
            newItem._widget.update(**treeDict[n])

    def createGraphNode(self, nodeType='modul', nodeName=None, nodeParent=None, index=None):
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
        newNodeName = self.mainUi._checkNodeName(nodeName, pQt.getAllItems(self))
        self.mainUi.log.debug("#-- + Creating %s Node + : %s --#" % (nodeType, newNodeName),
                              newLinesBefor=1)
        newItem = GraphItem(self.mainUi, nodeType, newNodeName)
        #-- Use Given Parent --#
        if nodeParent is not None:
            self.log.detail("\t ---> Use given parent: %s" % nodeParent)
            item = self.getItemFromNodeName(nodeParent)
            self.addGraphNode(item, newItem, index=index)
        #-- Use Ui Selection --#
        else:
            selItems = self.selectedItems()
            #-- Parent To Selected Node --#
            if len(selItems) == 1:
                self.log.detail("\t ---> Parent to selected node: %s" % selItems[0].nodeName)
                self.addGraphNode(selItems[0], newItem, index=index)
            #-- Parent To World --#
            else:
                if index is None:
                    self.log.detail("\t ---> Adding graph item '%s' to world ..." % newItem.nodeName)
                    self.addTopLevelItem(newItem)
                else:
                    self.log.detail("\t ---> Inserting graph item '%s' to world ..." % newItem.nodeName)
                    self.insertTopLevelItem(index, newItem)
        #-- Result --#
        return newItem

    def addGraphNode(self, item, newItem, index=None):
        """
        Add given item dans refreh ui
        :param item: Parent item
        :type item: QtGui.QTreeWidgetItem
        :param newItem: New item
        :type: QtGui.QTreeWidgetItem
        """
        item._widget.pbExpand.setChecked(True)
        item._widget.on_expandNode()
        if index is None:
            self.log.detail("\t ---> Adding graph item '%s', child of '%s' ..." % (newItem.nodeName,
                                                                                   item.nodeName))
            item.addChild(newItem)
        else:
            self.log.detail("\t ---> Inserting graph item '%s', child of '%s', index %s ..." % (newItem.nodeName,
                                                                                                item.nodeName,
                                                                                                index))
            item.insertChild(index, newItem)
        item._widget.rf_expandVis()

    def addGraphWidget(self, cIndex, item):
        """
        Add graphNode widget to given item
        :param cIndex: Column index
        :type cIndex: int
        :param item: GraphNode item
        :type item: QtGui.QTreeWidgetItem
        """
        self.log.detail("\t ---> Adding item widget ...")
        self.setItemWidget(item, cIndex, item._widget)
        item._column = cIndex
        item._widget.rf_nodeName()

    def deleteNodes(self, selItems):
        """
        Delete selected graph nodes without consideration for GraphTree selection
        :param selItems: Items to delete
        :type selItems: list
        """
        selItems.reverse()
        #-- Deleting Nodes --#
        for item in selItems:
            self.mainUi.log.debug("#-- - Deleting %s Node - : %s --#" % (item._nodeType, item.nodeName),
                                  newLinesBefor=1)
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
        self.addGraphWidget(0, QTreeWidgetItem)
        self.rf_graphColumns()

    def addTopLevelItems(self, list_of_QTreeWidgetItem):
        """
        Add options: Insert widget, refresh columns
        """
        super(GraphTree, self).addTopLevelItems(list_of_QTreeWidgetItem)
        for QTreeWidgetItem in list_of_QTreeWidgetItem:
            self.addGraphWidget(0, QTreeWidgetItem)
        self.rf_graphColumns()

    def insertTopLevelItem(self, p_int, QTreeWidgetItem):
        """
        Add options: Insert widget, refresh columns
        """
        super(GraphTree, self).insertTopLevelItem(p_int, QTreeWidgetItem)
        self.addGraphWidget(0, QTreeWidgetItem)
        self.rf_graphColumns()

    def insertTopLevelItems(self, p_int, list_of_QTreeWidgetItem):
        """
        Add options: Insert widget, refresh columns
        """
        super(GraphTree, self).insertTopLevelItems(p_int, list_of_QTreeWidgetItem)
        for QTreeWidgetItem in list_of_QTreeWidgetItem:
            self.addGraphWidget(0, QTreeWidgetItem)
        self.rf_graphColumns()


class GraphItem(QtGui.QTreeWidgetItem):
    """
    GraphTree item, child of GrapherUi.GraphTree
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
        self._column = None
        self._setupItem()

    def _setupItem(self):
        if self._nodeType == 'modul':
            self._widget = GraphNode(pItem=self, _datas=graphNodes.Modul())
        elif self._nodeType == 'sysData':
            self._widget = GraphNode(pItem=self, _datas=graphNodes.SysData())
        elif self._nodeType == 'cmdData':
            self._widget = GraphNode(pItem=self, _datas=graphNodes.CmdData())
        elif self._nodeType == 'pyData':
            self._widget = GraphNode(pItem=self, _datas=graphNodes.PyData())
        else:
            self._widget = GraphNode(pItem=self, _datas=graphNodes.Modul())

    def addChild(self, QTreeWidgetItem):
        """
        Add options: Insert widget, refresh columns
        """
        super(GraphItem, self).addChild(QTreeWidgetItem)
        self.treeWidget().addGraphWidget((int(self._column) + 1), QTreeWidgetItem)
        self.treeWidget().rf_graphColumns()
        self._widget.rf_childEnableIcon()

    def addChildren(self, list_of_QTreeWidgetItem):
        """
        Add options: Insert widget, refresh columns
        """
        super(GraphItem, self).addChildren(list_of_QTreeWidgetItem)
        for QTreeWidgetItem in list_of_QTreeWidgetItem:
            self.treeWidget().addGraphWidget((int(self._column) + 1), QTreeWidgetItem)
        self.treeWidget().rf_graphColumns()
        self._widget.rf_childEnableIcon()

    def insertChild(self, p_int, QTreeWidgetItem):
        """
        Add options: Insert widget, refresh columns
        """
        super(GraphItem, self).insertChild(p_int, QTreeWidgetItem)
        self.treeWidget().addGraphWidget((int(self._column) + 1), QTreeWidgetItem)
        self.treeWidget().rf_graphColumns()
        self._widget.rf_childEnableIcon()

    def insertChildren(self, p_int, list_of_QTreeWidgetItem):
        """
        Add options: Insert widget, refresh columns
        """
        super(GraphItem, self).insertChildren(p_int, list_of_QTreeWidgetItem)
        for QTreeWidgetItem in list_of_QTreeWidgetItem:
            self.treeWidget().addGraphWidget((int(self._column) + 1), QTreeWidgetItem)
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
        self.pItem = kwargs['pItem']
        self._datas = kwargs['_datas']
        self.pWidget = self.pItem.treeWidget()
        self._setupWidget()

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
        for k, v in self._datas.__repr__().iteritems():
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

    def setEnabled(self, state):
        """
        Set node enable state with given value
        :param state: Node enable state
        :type state: bool
        """
        self.pbEnable.setChecked(state)
        self.lNodeName.setEnabled(state)
        self.rf_nodeEnableIcon()

    def setExpanded(self, state):
        """
        Set node expand state with given value
        :param state: Node expanded state
        :type state: bool
        """
        self.pItem.setExpanded(state)
        self.pbExpand.setChecked(state)
        self.rf_nodeExpandIcon()

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
            rgba = self._datas._nodeColor
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
                if child.parent()._widget.lNodeName.isEnabled():
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
        self.setEnabled(self.isEnable)
        self.rf_childEnableIcon()

    def on_expandNode(self):
        """
        Command launched when 'Expand' QPushButton is clicked.
        Expand item
        """
        self.setExpanded(self.isExpanded)

    def update(self, **kwargs):
        """
        Update node params
        :param kwargs: Node params
        :type kwargs: dict
        """
        #-- Update Internal --#
        self.setEnabled(kwargs['_nodeIsEnabled'])
        self.setExpanded(kwargs['_nodeIsExpanded'])
        #-- Update Datas --#
