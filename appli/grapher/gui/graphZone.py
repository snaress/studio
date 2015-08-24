from functools import partial
from PyQt4 import QtGui, QtCore
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

    def commonMenuActions(self):
        """
        Common gaph menu actions
        :return: Graph menu actions
        :rtype: dict
        """
        return {0: {'type': 'item', 'title': 'Refresh', 'key': 'F5', 'cmd': None},
                1: {'type': 'item', 'title': 'Unselect All', 'key': 'Esc', 'cmd': None},
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
                5: {'type': 'sep', 'title': None, 'key': None, 'cmd': None},
                6: {'type': 'item', 'title': 'Delete', 'key': 'Del', 'cmd': None}}

    def buildMenu(self, QMenu):
        """
        Build graph menu
        :param QMenu: Graph menu
        :type QMenu: QtGui.QMenu
        """
        QMenu.clear()
        menuDict = self.commonMenuActions()
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

    def on_miNewNode(self, nodeType):
        """
        Command launched when 'New Node' QMenuItem is triggered.
        Create new node (modul)
        :param nodeType: Graph node type ('modul', 'sysData', 'cmdData', 'pyData', 'loop', 'condition')
        :type nodeType: str
        """
        self.log.detail(">>> Launch menuItem 'New Node' ...")
        newNode = self.grapher.tree.createItem(nodeType)


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
