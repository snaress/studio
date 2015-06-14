from functools import partial
from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from appli.grapherOld.ui import graphNodeUI


class GraphTree(QtGui.QTreeWidget):

    def __init__(self, ui):
        self._ui = ui
        self.gp = self._ui.gp
        self.log = self._ui.log
        super(GraphTree, self).__init__()
        self._setupWidget()

    @property
    def graphData(self):
        """ Get graphTree data
            :return: (dict) : Graph dict """
        graphDict = {'_order': []}
        items = pQt.getAllItems(self)
        for item in items:
            parents = pQt.getAllParent(item)
            parents.reverse()
            itemPath = []
            for parent in parents:
                itemPath.append(parent._widget.nodeData.nodeName)
            itemPath = '/'.join(itemPath)
            graphDict['_order'].append(itemPath)
            graphDict[itemPath] = item._widget.nodeData.data
        return graphDict

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

    def rf_graph(self):
        """ Refresh graph tree """
        self.clear()
        for itemPath in self._ui.gp.gpGraph['_order']:
            nodeDict = self._ui.gp.gpGraph[itemPath]
            if not '/' in itemPath:
                self.addGraphNode(**nodeDict)
            else:
                parentItem = self.getItemFromNodeName(itemPath.split('/')[-2])
                self.addGraphNode(parent=parentItem, **nodeDict)
        self.rf_graphColumns()

    def on_popUpMenu(self, point):
        """ Command launched when right click is done
            :param point: (object) : Qt position """
        self._ui.mGraph.exec_(self.mapToGlobal(point))

    def on_newNode(self):
        """ Command launch when menuItem 'New Node' is clicked
            :return: (object) : QTreeWidgetItem """
        selItems = self.selectedItems()
        if not len(selItems) > 1:
            if selItems:
                newItem = self.addGraphNode(parent=selItems[0], **self.gp.defaultNodeDict)
            else:
                newItem = self.addGraphNode(**self.gp.defaultNodeDict)
            return newItem
        else:
            self._ui._errorDialog("!!! Warning: Select only one node !!!", self)

    def on_renameNode(self):
        """ Command launch when menuItem 'Rename Node' is clicked """
        selItems = self.selectedItems()
        if len(selItems) == 1:
            message = "Enter New Node Name"
            self.renameDialog = pQt.PromptDialog(message, partial(self.renameNode, selItems[0]))
            self.renameDialog.exec_()

    def addGraphNode(self, parent=None, **kwargs):
        """ Add new QTreeWidgetItem
            :param kwargs: (dict) : Node params
            :return: (object) : QTreeWidgetItem """
        nodeDict = kwargs
        nodeDict['nodeName'] = self._checkNodeName(kwargs['nodeName'])
        #-- Get Index --#
        if parent is None:
            index = 0
        else:
            index = (parent._index + 1)
        #-- Add New Node --#
        newItem = self.new_graphItem(index, **nodeDict)
        if parent is None:
            self.addTopLevelItem(newItem)
        else:
            parent.addChild(newItem)
        self.setItemWidget(newItem, index, newItem._widget)
        self.setItem(newItem, **nodeDict)
        newItem._widget.rf_nodeBgc()
        self.rf_graphColumns()
        return newItem

    def renameNode(self, selItem):
        """ Rename selected node
            :param selItem: (object) : QTreeWidgetItem """
        self.log.debug("#-- Rename Node --#")
        result = self.renameDialog.result()['result_1']
        newNodeName = self._checkNodeName(result)
        self.log.debug("Rename %s ---> %s" % (selItem._widget.nodeData.data['nodeName'], newNodeName))
        selItem._widget.setGraphNodeName(newNodeName)
        setattr(selItem._widget.nodeData, 'nodeName', newNodeName)
        self.renameDialog.close()
        self.rf_graphColumns()

    @staticmethod
    def new_graphItem(index, **kwargs):
        """ Create new graph QTreeWidgetItem
            :param index: (int) : Column index
            :return: (object) : QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem._index = index
        newItem._widget = GraphNode(newItem, **kwargs)
        return newItem

    def getNodeNames(self):
        """ Get all node names
            :return: (list) : Node name list """
        items = pQt.getAllItems(self)
        nodeNames = []
        for item in items:
            nodeNames.append(item._widget.nodeData.nodeName)
        return nodeNames

    def getItemFromNodeName(self, nodeName):
        """ Get QTreeWidgetItem from given nodeName
            :param nodeName: (str) : Node name
            :return: (object) : QTreeWidgetItem """
        if nodeName is not None:
            allItems = pQt.getAllItems(self)
            for item in allItems:
                if item._widget.nodeData.nodeName == nodeName:
                    return item

    @staticmethod
    def setItem(item, **kwargs):
        """ Edit node params
            :param item: (object) : QTreeWidgetItem
            :param kwargs: (dict) : Node params """
        item._widget.setGraphNodeName(kwargs['nodeName'])
        item._widget.setGraphNodeEnabled(kwargs['nodeEnabled'])
        item._widget.setGraphNodeExpanded(kwargs['nodeExpanded'])

    def _checkNodeName(self, nodeName):
        """ Check if nodeName is valide, add suffixe if needed
            :param nodeName: (str) : Node name
            :return: (str) : Valide node name """
        #-- Check Prefix --#
        if ' ' in nodeName or '/' in nodeName:
            nodeName = nodeName.replace(' ', '_')
        #-- Check if exists --#
        items = pQt.getAllItems(self)
        rename = False
        for item in items:
            if item._widget.nodeData.nodeName == nodeName:
                rename = True
                break
        #-- Rename --#
        if rename:
            nodeNames = self.getNodeNames()
            tmpNames = []
            for name in nodeNames:
                if name.startswith('%s_' % nodeName):
                    tmpNames.append(name)
            if not tmpNames:
                nodeName = '%s_1' % nodeName
            else:
                #-- Get New Suffixe --#
                suffixes = []
                for tmpName in tmpNames:
                    prefixe = '_'.join(tmpName.split('_')[:-1])
                    suffixe = tmpName.split('_')[-1]
                    if suffixe.isdigit() and prefixe == nodeName:
                        suffixes.append(suffixe)
                if not suffixes:
                    nodeName = '%s_1' % nodeName
                else:
                    index = (int(sorted(suffixes)[-1]) + 1)
                    nodeName = '%s_%s' % (nodeName, index)
        return nodeName

    @staticmethod
    def graphNodeBgc(nodeType):
        """ Graph node background color
            :param nodeType: (str) : 'modul', 'loop', 'sysData', 'cmdData', 'purData'
            :return: (str) : Background color """
        if nodeType == 'modul':
            return "background-color:rgb(80,80,80);"
        elif nodeType == 'loop':
            return "background-color:rgb(0,70,0);"
        elif nodeType == 'sysData':
            return "background-color:rgb(50,140,175);"
        elif nodeType == 'cmdData':
            return "background-color:rgb(10,50,150);"
        elif nodeType == 'purData':
            return "background-color:rgb(35,135,35);"


class GraphNode(QtGui.QWidget, graphNodeUI.Ui_graphNode, pQt.Style):

    def __init__(self, graphItem, **kwargs):
        self.graphItem = graphItem
        self.nodeData = NodeData(**kwargs)
        super(GraphNode, self).__init__()
        self._setupUi()

    @property
    def tree(self):
        """ Get parent QTreeWidget
            :return: (object) : QTreeWidget """
        return self.graphItem.treeWidget()

    @property
    def _ui(self):
        """ Get parent widget
            :return: (object) : QWidget or QMainWindow """
        return self.tree._ui

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup GraphNode widget """
        self.setupUi(self)
        self.pbExpand.clicked.connect(self.on_expandNode)
        self.cbNode.clicked.connect(self.on_enableNode)
        click_handler = pQt.ClickHandler(singleClickCmd=self._singleClick, doubleClickCmd=self._doubleClick)
        self.pbNode.clicked.connect(click_handler)
        self.rf_execNode()

    def rf_nodeBgc(self):
        """ Refresh graphNode background color """
        self.setStyleSheet(self.tree.graphNodeBgc(self.nodeData.nodeType))

    def rf_childIndicator(self):
        """ Refresh children indicator """
        if self.graphItem.childCount() > 0:
            self.lChildIndicator.setText(" c ")
        else:
            self.lChildIndicator.setText("")

    def rf_execNode(self):
        """ Refresh execNode visibility """
        self.pbExecNode.setVisible(self.nodeData.nodeExec)

    def on_expandNode(self):
        """ Expand or collapse item """
        self.setGraphNodeExpanded(not self.graphItem.isExpanded())

    def on_enableNode(self):
        """ Enable or disable graphNode """
        self.setGraphNodeEnabled(self.cbNode.isChecked())

    def _singleClick(self):
        """ Connect graphNode to nodeEditor """
        if self._ui.miNodeEditor.isChecked():
            self._ui.wgNodeEditor._updateUi(graphNode=self)

    def _doubleClick(self):
        """ Connect graphNode in an external nodeEditor """

    def setGraphNodeName(self, nodeName):
        """ Edit graphNode button name
            :param nodeName: (str) : Node name"""
        self.pbNode.setText(nodeName)

    def setGraphNodeExpanded(self, state):
        """ Edit graphNode QTreeWidgetItem state
            :param state: (bool) : QTreeWidgetItem state """
        self.graphItem.setExpanded(state)
        if state:
            self.pbExpand.setText(' - ')
        else:
            self.pbExpand.setText(' + ')
        self.tree.rf_graphColumns()
        self.nodeData.nodeExpanded = state

    def setGraphNodeEnabled(self, state):
        """ Edit graphNode checkBox state
            :param state: (bool) : Node state """
        self.cbNode.setChecked(state)
        self.pbNode.setEnabled(state)
        self.pbExecNode.setEnabled(state)
        self.nodeData.nodeEnabled = state


class NodeData(object):

    def __init__(self, **kwargs):
        self.setData(**kwargs)

    @property
    def data(self):
        """ Get node data
            :return: (dict) : Node dict """
        nodeDict = {}
        for k, v in self.__dict__.iteritems():
            if k.startswith('node'):
                nodeDict[k] = v
        return nodeDict

    def setData(self, **kwargs):
        """ Set node data
            :param kwargs: (dict) : Node dict """
        for k, v in kwargs.iteritems():
            if k.startswith('node'):
                setattr(self, k, v)
