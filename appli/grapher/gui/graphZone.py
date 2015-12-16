import os
from functools import partial
from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.grapher.gui import graphTree, graphScene, graphWgts, nodeEditor


class GraphZone(object):
    """
    GraphZone widget, child of GrapherUi

    :param mainUi: Grapher mainUi class
    :type mainUi: grapherUi..GrapherUi
    """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphZone Widget.")
        self.grapher = self.mainUi.grapher
        self.graphTree = None
        self.editors = []
        self.enabledIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'png', 'enabled.png'))
        self.disabledIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'png', 'disabled.png'))
        self.expandIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'png', 'expand.png'))
        self.collapseIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'png', 'collapse.png'))
        self.unfoldIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'png', 'arrowDnBlue.png'))
        self.foldIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'png', 'arrowUpBlue.png'))
        self.pullIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'png', 'arrowDnGreen.png'))
        self._setupWidget()

    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphZone Widget.")
        self.cpBuffer = None
        #-- Add GraphTree --#
        self.graphTree = graphTree.GraphTree(self.mainUi, self)
        self.mainUi.vlGraphZone.insertWidget(0, self.graphTree)
        #-- Add GraphScene --#
        self.graphScene = graphScene.GraphScene(self.mainUi, self)
        self.sceneView = GraphView(self.mainUi, self.graphScene)
        self.mainUi.vlGraphZone.insertWidget(0, self.sceneView)

    @property
    def currentGraphMode(self):
        """
        Get GraphZone mode

        :return: GraphZone mode ('tree' or 'scene')
        :rtype: str
        """
        if self.mainUi.miGraphScene.isChecked():
            return 'scene'
        else:
            return 'tree'

    @property
    def currentGraph(self):
        """
        Get current GraphZone widget

        :return: GraphZone widget ('self.graphTree' or 'self.graphScene')
        :rtype: GrapherUi.GraphTree | GrapherUi.GraphScene
        """
        if self.currentGraphMode == 'tree':
            return self.graphTree
        elif self.currentGraphMode == 'scene':
            return self.graphScene

    def commonMenuActions(self):
        """
        Common gaph menu actions

        :return: Graph menu actions
        :rtype: dict
        """
        return {0: {'type': 'menu', 'title': 'New Node',
                    'children': {0: {'type': 'item', 'title': 'Modul', 'key': '1',
                                     'cmd': partial(self.on_miNewNode, 'modul')},
                                 1: {'type': 'item', 'title': 'SysData', 'key': '2',
                                     'cmd': partial(self.on_miNewNode, 'sysData')},
                                 2: {'type': 'item', 'title': 'CmdData', 'key': '3',
                                     'cmd': partial(self.on_miNewNode, 'cmdData')},
                                 3: {'type': 'item', 'title': 'PurData', 'key': '4',
                                     'cmd': partial(self.on_miNewNode, 'purData')},
                                 4: {'type': 'item', 'title': 'Loop', 'key': '5',
                                     'cmd': partial(self.on_miNewNode, 'loop')}}},
                1: {'type': 'item', 'title': 'Rename Node', 'key': 'F2', 'cmd': self.on_miRenameNode},
                2: {'type': 'sep', 'title': None, 'key': None, 'cmd': None},
                3: {'type': 'menu', 'title': 'Copy / Paste',
                    'children': {0: {'type': 'item', 'title': 'Copy Nodes', 'key': 'Ctrl+C',
                                     'cmd': partial(self.on_miCopyNodes, _mode='nodes', rm=False)},
                                 1: {'type': 'item', 'title': 'Copy Branch', 'key': 'Alt+C',
                                     'cmd': partial(self.on_miCopyNodes, _mode='branch', rm=False)},
                                 2: {'type': 'item', 'title': 'Cut Branch', 'key': 'Ctrl+X',
                                     'cmd': partial(self.on_miCopyNodes, _mode='branch', rm=True)},
                                 3: {'type': 'item', 'title': 'Paste Nodes', 'key': 'Ctrl+V',
                                     'cmd': self.on_miPasteNodes}}},
                4: {'type': 'menu', 'title': 'Move Nodes',
                    'children': {0: {'type': 'item', 'title': 'Move Up', 'key': 'Ctrl+Up',
                                     'cmd': partial(self.on_miMoveNodes, side='up')},
                                 1: {'type': 'item', 'title': 'Move Down', 'key': 'Ctrl+Down',
                                     'cmd': partial(self.on_miMoveNodes, side='down')}}},
                5: {'type': 'sep', 'title': None, 'key': None, 'cmd': None},
                6: {'type': 'item', 'title': 'Del Selected', 'key': 'Del', 'cmd': self.on_miDelSelected},
                7: {'type': 'sep', 'title': None, 'key': None, 'cmd': None},
                8: {'type': 'item', 'title': 'Refresh Graph', 'key': 'F5', 'cmd': self.on_miRefresh},
                9: {'type': 'item', 'title': 'Unselect All', 'key': 'Esc', 'cmd': self.on_miUnselectAll},
                10: {'type': 'sep', 'title': None, 'key': None, 'cmd': None},
                11: {'type': 'item', 'title': 'Clear CheckFiles', 'key': 'Ctrl+Del', 'cmd': self.on_miDelCheckFiles}}

    def treeMenuActions(self):
        """
        GraphTree specific menu actions

        :return: Tree menu actions
        :rtype: dict
        """
        return {0: {'type': 'sep', 'title': None, 'key': None, 'cmd': None},
                1: {'type': 'item', 'title': 'Auto Expand', 'key': 'C', 'cmd': self.on_miAutoExpand}}

    def sceneMenuActions(self):
        """
        GraphScene specific menu actions

        :return: Scene menu actions
        :rtype: dict
        """
        return {0: {'type': 'sep', 'title': None, 'key': None, 'cmd': None},
                1: {'type': 'item', 'title': 'Fit In Scene', 'key': 'H', 'cmd': self.sceneView.fitInScene},
                2: {'type': 'item', 'title': 'Fit In Selected', 'key': 'F', 'cmd': self.sceneView.fitInSelected}}

    def buildMenu(self, QMenu):
        """
        Build graph menu

        :param QMenu: Graph menu
        :type QMenu: QtGui.QMenu
        """
        QMenu.clear()
        #-- Collecte Menu Items --#
        if self.currentGraphMode == 'tree':
            dictList = [self.commonMenuActions(), self.treeMenuActions()]
        else:
            dictList = [self.commonMenuActions(), self.sceneMenuActions()]
        #-- Build Menu --#
        for menuDict in dictList:
            for n in sorted(menuDict.keys()):
                #-- Add Sub Menu --#
                if menuDict[n]['type'] == 'menu':
                    newMenu = QMenu.addMenu(menuDict[n]['title'])
                    #-- Add Sub Item --#
                    for i in sorted(menuDict[n]['children']):
                        childDict = menuDict[n]['children'][i]
                        self.newMenuItem(newMenu, childDict['type'], childDict['title'],
                                                  childDict['key'], childDict['cmd'])
                #-- Add Item --#
                elif menuDict[n]['type'] in ['item', 'sep']:
                    self.newMenuItem(QMenu, menuDict[n]['type'], menuDict[n]['title'],
                                            menuDict[n]['key'], menuDict[n]['cmd'])

    @staticmethod
    def newMenuItem(QMenu, _type, title, key, cmd):
        """
        Add menu item to given menu

        :param QMenu: Menu to build
        :type QMenu: QtGui.QMenu
        :param _type: Item type ('menu', 'item' or 'sep')
        :type _type: str
        :param title: Item title
        :type title: str
        :param key: Item shortcut
        :type key: str
        :param cmd: Item command
        :type cmd: str
        """
        if _type == 'item':
            newItem = QMenu.addAction(title)
            if key is not None:
                newItem.setShortcut(key)
            if cmd is not None:
                newItem.triggered.connect(cmd)
        elif _type == 'sep':
            QMenu.addSeparator()

    def buildGraph(self, treeDict, clear=False):
        """
        Build graph tree from given params

        :param treeDict: Tree params
        :type treeDict: dict
        """
        self.log.debug("#-- Build Graph --#" , newLinesBefore=1)
        #-- Clear Before Build --#
        if clear:
            self.currentGraph.clear()
        #-- Build --#
        datasDict = {}
        for n in sorted(treeDict.keys()):
            newItem = self.currentGraph.createGraphNode(nodeType=treeDict[n]['nodeType'],
                                                        nodeName=treeDict[n]['nodeName'],
                                                        nodeParent=treeDict[n]['parent'])
            datasDict[n] = {newItem: treeDict[n]}
        #-- Update --#
        for n in sorted(datasDict.keys()):
            for k, v in datasDict[n].iteritems():
                k.update(v)

    def refreshGraph(self):
        """
        Refresh current graph
        """
        self.buildGraph(self.grapher.tree.getDatas(), clear=True)

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
        self.cpBuffer = dict(_mode=_mode)
        #-- Collecte Info --#
        if items is None:
            selItems = self.currentGraph.selectedItems() or []
        else:
            if items == '':
                selItems = []
            else:
                selItems = items
        if selItems:
            self.log.debug("Storing selected nodes ...")
            #-- Store Selected Nodes --#
            for n, item in enumerate(selItems):
                nodeDict = eval(item._item.getDatas(asString=True)) # Clone: asString=False
                self.cpBuffer[n] = dict(nodeName=item._item._node.nodeName, nodeChildren={}, nodeDict=nodeDict)
                if _mode == 'branch':
                    if item._item._children:
                        #-- Store Children --#
                        for c, child in enumerate(item._item.allChildren()):
                            self.cpBuffer[n]['nodeChildren'][c] = eval(child.getDatas(asString=True))
            #-- Delete For cut --#
            if rm:
                self.deleteGraphNodes(selItems)

    def pasteNodes(self, dstItem=None):
        """
        Paste stored node

        :param dstItem: Destination graph item
        :type dstItem: QtGui.QTreeWidgetItem
        :return: Pasted items
        :rtype: list
        """
        if self.cpBuffer is not None:
            self.log.debug("Pasting Stored nodes ...")
            #-- Get Destination items --#
            if dstItem is None:
                selItems = self.currentGraph.selectedItems() or []
            else:
                selItems = [dstItem]
            #-- Paste Nodes --#
            items = {}
            for n in sorted(self.cpBuffer.keys()):
                if isinstance(n, int):
                    nodeDict = self.cpBuffer[n]
                    newNodeName = self.grapher.conformNewNodeName(nodeDict['nodeName'])
                    newItem = None
                    #-- Parent To World --#
                    if len(selItems) == 0:
                        self.log.detail("\t ---> Paste Node to world ...")
                        newItem = self.grapher.tree.createItem(nodeType=nodeDict['nodeDict']['nodeType'],
                                                               nodeName=newNodeName)
                    #-- Parent To Node --#
                    elif len(selItems) == 1:
                        self.log.detail("\t ---> Paste Node to %s ..." % selItems[0]._item._node.nodeName)
                        selItems[0]._item.setExpanded(True)
                        newItem = self.grapher.tree.createItem(nodeType=nodeDict['nodeDict']['nodeType'],
                                                               nodeName=newNodeName,
                                                               nodeParent=selItems[0]._item._node.nodeName)
                    newItem._node.setDatas(**nodeDict['nodeDict'])
                    #-- Parent Child Node --#
                    if newItem is not None:
                        items[newItem] = nodeDict['nodeDict']
                        if nodeDict['nodeChildren'].keys():
                            #-- Check First Parent --#
                            renameDict = dict()
                            for c in sorted(nodeDict['nodeChildren'].keys()):
                                newChildName = self.grapher.conformNewNodeName(nodeDict['nodeChildren'][c]['nodeName'])
                                renameDict[nodeDict['nodeChildren'][c]['nodeName']] = newChildName
                                if nodeDict['nodeChildren'][c]['parent'] == self.cpBuffer[n]['nodeName']:
                                    nodeParent = newNodeName
                                else:
                                    _name = nodeDict['nodeChildren'][c]['parent']
                                    if _name in renameDict.keys():
                                        nodeParent = renameDict[_name]
                                    else:
                                        nodeParent = newNodeName
                                nodeDict['nodeChildren'][c]['parent'] = nodeParent
                                newChild = self.grapher.tree.createItem(nodeType=nodeDict['nodeChildren'][c]['nodeType'],
                                                                        nodeName=newChildName,
                                                                        nodeParent=nodeParent)
                                newChild._node.setDatas(**nodeDict['nodeChildren'][c])
                                items[newChild] = nodeDict
            #-- Clear CpBuffer --#
            if self.cpBuffer['_mode'] == 'branch':
                self.cpBuffer = None
            #-- Result --#
            return items.keys()
        self.log.warning("!!! Nothing to paste !!!")

    def moveNodes(self, side='up'):
        """
        Move selected nodes

        :param side: 'up', 'down'
        :type side: str
        :return: Moved items
        :rtype: list
        """
        #-- Collecte Info --#
        selItems = self.currentGraph.selectedItems() or []
        if selItems:
            self.log.debug("Moving selected nodes ...")
            movedItems = []
            for n, item in enumerate(selItems):
                item._item.move(side)
                movedItems.append(item)
            return movedItems

    def deleteGraphNodes(self, items):
        """
        Delete given items

        :param items: Graph items
        :type items: list
        """
        for item in items:
            item._item.delete()
        self.refreshGraph()

    def getItemFromNodeName(self, nodeName):
        """
        Get graphItem from given node name

        :param nodeName: Node name
        :type nodeName: str
        :return: graphTree item
        :rtype: QtGui.QTreeWidgetItem | QtSvg.QGraphicsSvgItem
        """
        if self.currentGraphMode == 'tree':
            allItems = pQt.getAllItems(self.graphTree)
        else:
            allItems = self.graphScene.getAllNodes()
        for item in allItems:
            if item._item._node.nodeName == nodeName:
                return item

    def getSelectedNodeNames(self):
        """
        Get selected node names

        :return: Selected node names
        :rtype: list
        """
        selItems = self.currentGraph.selectedItems() or []
        selNodeNames = []
        for selItem in selItems:
            selNodeNames.append(selItem._item._node.nodeName)
        return selNodeNames

    def reselectNodes(self, selNodeNames):
        """
        Reselect nodes from given node names list

        :param selNodeNames: Selected node names
        :type selNodeNames: list
        """
        if self.currentGraphMode == 'tree':
            allItems = pQt.getAllItems(self.graphTree)
        else:
            allItems = self.graphScene.getAllNodes()
        for item in allItems:
            if item._item._node.nodeName in selNodeNames:
                item.setSelected(True)
            else:
                item.setSelected(False)
            if self.currentGraphMode == 'scene':
                item.rf_elementId()

    def _singleClick(self):
        """
        Connect graphNode to nodeEditor
        """
        if self.mainUi.nodeEditorIsEnabled:
            if self.currentGraphMode == 'tree':
                selItems = self.graphTree.selectedItems() or []
            else:
                selItems = self.graphScene.getSelectedNodes()
            self.mainUi.nodeEditor.clear()
            if len(selItems) == 1:
                self.mainUi.nodeEditor.connectItem(selItems[0])

    def _doubleClick(self):
        """
        Connect graphNode to an external nodeEditor
        """
        if self.currentGraphMode == 'tree':
            selItems = self.graphTree.selectedItems() or []
        else:
            selItems = self.graphScene.getSelectedNodes()
        if len(selItems) == 1:
            editor = nodeEditor.NodeEditor(self.mainUi)
            editor.connectItem(selItems[0])
            self.editors.append(editor)
        self.editors[-1].show()

    def on_miRenameNode(self):
        """
        Command launched when 'Rename Node' QMenuItem is triggered.

        Refresh selected node.
        """
        self.log.detail(">>> Launch menuItem 'Rename Node' ...")
        selItems = self.currentGraph.selectedItems() or []
        if len(selItems) == 1:
            self.nodeRenamer = graphWgts.NodeRenamer(self.mainUi, selItems[0])
            self.nodeRenamer.exec_()

    def on_miRefresh(self):
        """
        Command launched when 'Refresh' QMenuItem is triggered.

        Refresh current graph.
        """
        self.log.detail(">>> Launch menuItem 'Refresh' ...")
        self.refreshGraph()

    def on_miUnselectAll(self):
        """
        Command launched when 'Unselect All' QMenuItem is triggered.

        Clear graph selection.
        """
        self.log.detail(">>> Launch menuItem 'Unselect All' ...")
        self.currentGraph.clearSelection()
        if self.currentGraphMode == 'scene':
            for item in self.graphScene.getAllNodes():
                item.rf_elementId()

    def on_miNewNode(self, nodeType):
        """
        Command launched when 'New Node' QMenuItem is triggered.

        Create new node (modul)
        :param nodeType: Graph node type ('modul', 'sysData', 'cmdData', 'pyData', 'loop', 'condition')
        :type nodeType: str
        """
        self.log.detail(">>> Launch menuItem 'New Node' ...")
        selItems = self.currentGraph.selectedItems()
        parent = None
        if len(selItems) == 1:
            parent = selItems[0]._item._node.nodeName
        newGrapherItem = self.grapher.tree.createItem(nodeType, nodeParent=parent)
        self.buildGraph({0: newGrapherItem.getDatas()})

    def on_miAutoExpand(self):
        """
        Command launched when 'Auto Expand' QMenuItem is triggered.

        Expand or collapse node
        """
        selItems = self.currentGraph.selectedItems()
        if selItems:
            if self.currentGraphMode == 'tree':
                self.log.detail(">>> Launch menuItem 'Auto Expand' ...")
                for item in selItems:
                    item._widget.set_expanded(state=not item._widget.isExpanded)

    def on_miCopyNodes(self, _mode='nodes', rm=False):
        """
        Command launched when 'Copy Nodes / Branch' or 'Cut Nodes' QMenuItem is triggered.

        Copy / Cut selected nodes or branch
        :param _mode: 'nodes' or 'branch'
        :type _mode: str
        :param rm: Remove selected nodes (cut)
        :type rm: bool
        """
        if not rm:
            self.log.detail(">>> Launch menuItem 'Copy %s' ..." % _mode)
        else:
            self.log.detail(">>> Launch menuItem 'Cut Nodes' ...")
        self.copyNodes(_mode=_mode, rm=rm)

    def on_miPasteNodes(self):
        """
        Command launched when 'Paste' QMenuItem is triggered.

        Paste stored nodes and refresh ui
        """
        self.log.detail(">>> Launch menuItem 'Paste Nodes' ...")
        pastedItems = self.pasteNodes()
        if pastedItems:
            selNodeNames = self.getSelectedNodeNames()
            self.refreshGraph()
            self.reselectNodes(selNodeNames)

    def on_miMoveNodes(self, side='up'):
        """
        Command launched when 'Move Up / Down' QMenuItem is triggered.

        Move up or down selected nodes
        :param side: 'up' or 'down'
        :type side: str
        """
        self.log.detail(">>> Launch menuItem 'Move Nodes': %s ..." % side)
        movedItems = self.moveNodes(side=side)
        if movedItems:
            selNodeNames = self.getSelectedNodeNames()
            self.refreshGraph()
            self.reselectNodes(selNodeNames)

    def on_miDelSelected(self):
        """
        Command launched when 'Del Selected' QMenuItem is triggered.

        Delete selected nodes
        """
        self.log.detail(">>> Launch menuItem 'Del Selected' ...")
        if self.currentGraphMode == 'tree':
            self.deleteGraphNodes(self.graphTree.selectedItems())
        else:
            self.deleteGraphNodes(self.graphScene.getSelectedNodes())

    def on_miDelCheckFiles(self):
        self.log.detail(">>> Launch menuItem 'Clear CheckFiles' ...")
        #-- Get Selected Items --#
        if self.currentGraphMode == 'tree':
            selItems = self.graphTree.selectedItems() or []
        else:
            selItems = self.graphScene.getSelectedNodes()
        #-- Get CheckFile BaseName --#
        loopChecks = dict()
        for item in selItems:
            node = item._item._node
            if node.nodeType == 'loop':
                self.log.debug("Loop found: %s" % node.nodeName)
                loopChecks[node.nodeName] = node.nodeLoopParams[node.nodeVersion]['checkFiles']
        #-- Clear CheckFiles --#
        if loopChecks.keys():
            tmpPath = pFile.conformPath(os.path.join(self.grapher.graphTmpPath, 'tmpFiles'))
            for tmpFile in os.listdir(tmpPath):
                for k, v in loopChecks.iteritems():
                    if tmpFile.startswith('%s.' % v) and tmpFile.endswith('.py'):
                        try:
                            os.remove(pFile.conformPath(os.path.join(tmpPath, tmpFile)))
                            self.log.detail("\t ---> %s" % tmpFile)
                        except:
                            self.log.warning("\t !!! Can not delete %s" % tmpFile)


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

    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphView Widget.")
        self.setSceneRect(0, 0, 10000, 10000)
        self.scale(0.5, 0.5)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemShape)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(35, 35, 35, 255), QtCore.Qt.SolidPattern))
        self.setVisible(False)

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
