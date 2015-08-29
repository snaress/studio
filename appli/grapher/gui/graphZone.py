from functools import partial
from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from appli.grapher.gui import graphTree, graphScene


class GraphZone(object):
    """
    GraphZone widget, child of GrapherUi
    :param mainUi: Grapher mainUi class
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphZone Widget.")
        self.grapher = self.mainUi.grapher
        self.graphTree = None
        self._setupWidget()

    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphZone Widget.")
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
        return {0: {'type': 'item', 'title': 'Refresh', 'key': 'F5', 'cmd': self.on_miRefresh},
                1: {'type': 'item', 'title': 'Unselect All', 'key': 'Esc', 'cmd': self.on_miUnselectAll},
                3: {'type': 'sep', 'title': None, 'key': None, 'cmd': None},
                4: {'type': 'menu', 'title': 'New Node',
                    'children': {0: {'type': 'item', 'title': 'Modul', 'key': '1',
                                     'cmd': partial(self.on_miNewNode, 'modul')},
                                 1: {'type': 'item', 'title': 'SysData', 'key': '2',
                                     'cmd': partial(self.on_miNewNode, 'sysData')},
                                 2: {'type': 'item', 'title': 'CmdData', 'key': '3',
                                     'cmd': partial(self.on_miNewNode, 'cmdData')},
                                 3: {'type': 'item', 'title': 'PyData', 'key': '4',
                                     'cmd': partial(self.on_miNewNode, 'pyData')}}},
                5: {'type': 'menu', 'title': 'Expand / Collapse',
                    'children': {0: {'type': 'item', 'title': 'Auto Expand', 'key': "C",
                                     'cmd': self.on_miAutoExpand}}},
                6: {'type': 'sep', 'title': None, 'key': None, 'cmd': None},
                7: {'type': 'item', 'title': 'Del Selected', 'key': 'Del', 'cmd': self.on_miDelSelected}}

    def sceneMenuActions(self):
        """
        GraphScene specific menu actions
        :return: Scene menu actions
        :rtype: dict
        """
        return {0: {'type': 'item', 'title': 'Fit In Scene', 'key': 'H', 'cmd': self.sceneView.fitInScene},
                1: {'type': 'item', 'title': 'Fit In Selected', 'key': 'F', 'cmd': self.sceneView.fitInSelected}}

    def buildMenu(self, QMenu):
        """
        Build graph menu
        :param QMenu: Graph menu
        :type QMenu: QtGui.QMenu
        """
        QMenu.clear()
        #-- Collecte Menu Items --#
        if self.currentGraphMode == 'tree':
            dictList = [self.commonMenuActions()]
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
        self.log.debug("#-- Build Graph --#" , newLinesBefor=1)
        #-- Clear Before Build --#
        if clear:
            self.currentGraph.clear()
        #-- Build --#
        for n in sorted(treeDict.keys()):
            self.currentGraph.createGraphNode(nodeType=treeDict[n]['nodeType'],
                                              nodeName=treeDict[n]['nodeName'],
                                              nodeParent=treeDict[n]['parent'])

    def refreshGraph(self):
        """
        Refresh current graph
        """
        self.buildGraph(self.grapher.tree.getDatas(), clear=True)

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

    def on_miRefresh(self):
        """
        Command launched when 'Refresh' QMenuItem is triggered. Refresh current graph.
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
        self.log.detail(">>> Launch menuItem 'Auto Expand' ...")
        selItems = self.graphTree.selectedItems()
        if selItems:
            selItems[0]._widget.set_expanded(state=not selItems[0]._widget.isExpanded)

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
