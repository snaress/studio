from PyQt4 import QtGui
from functools import partial
from lib.qt import procQt as pQt
from appli.grapher.gui.ui import wgDataGroupUI, wgDataNodeIdUI, wgDataNodeConnUI, wgDataConnGroupUI,\
                                 wgDataConnItemUI


#======================================== GENERAL ========================================#

class DataZone(object):
    """ Data zone constructor class
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("---> Setup DataZone ...")
        self.dataTree = self.mainUi.twNodeData
        self.addAllCategory()

    def addCategory(self, groupName, QWidget):
        """ Add data category
            :param groupName: New category name
            :type groupName: str
            :param QWidget: Widget parent to new category
            :type QWidget: QtGui.QWidget """
        #-- Add Data Group --#
        dataGrp = QtGui.QTreeWidgetItem()
        dataGrp.setBackgroundColor(0, QtGui.QColor(200, 200, 200))
        dataGrp._widget = DataGroup(self.mainUi, dataGrp, groupName=groupName)
        self.dataTree.addTopLevelItem(dataGrp)
        self.dataTree.setItemWidget(dataGrp, 0, dataGrp._widget)
        #-- Add Data Params --#
        dataParams = QtGui.QTreeWidgetItem()
        dataParams._widget = QWidget
        dataGrp.addChild(dataParams)
        self.dataTree.setItemWidget(dataParams, 0, dataParams._widget)
        dataParams._widget.pItem = dataParams
        #-- Init Item Default State --#
        if dataParams._widget.defaultState == 'expanded':
            dataGrp._widget.pbGrpName.setChecked(True)
            dataGrp._widget.on_icon()

    def addAllCategory(self):
        """ Add all data zone category """
        self.addCategory('Node Id', DataNodeId(self.mainUi))
        self.addCategory('Node Connections', DataNodeConnections(self.mainUi))


class DataGroup(QtGui.QWidget, wgDataGroupUI.Ui_wgDataGroup):
    """ Data category group widget
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow
        :param pItem: Parent widget item
        :type pItem: QtGui.QTreeWidgetItem
        :param groupName: Category group name
        :type groupName: str """

    def __init__(self, mainUi, pItem, groupName='Untitled'):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t\t ---> %s" % groupName)
        self.pItem = pItem
        self.grpName = groupName
        self.collapseIcon = QtGui.QIcon("gui/icon/png/treeCollapse.png")
        self.expandIcon = QtGui.QIcon("gui/icon/png/treeExpand.png")
        super(DataGroup, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup category group """
        self.setupUi(self)
        self.lGrpName.setText(self.grpName)
        self.pbGrpName.clicked.connect(self.on_icon)
        self.rf_icon()

    def rf_icon(self):
        """ Refresh category group icon button """
        if self.pbGrpName.isChecked():
            self.pbGrpName.setIcon(self.collapseIcon)
        else:
            self.pbGrpName.setIcon(self.expandIcon)

    def on_icon(self):
        """ Command launched when category group button is clicked,
            Expand category group """
        self.pItem.treeWidget().setItemExpanded(self.pItem, self.pbGrpName.isChecked())
        self.rf_icon()

#======================================== NODE ID ========================================#

class DataNodeId(QtGui.QWidget, wgDataNodeIdUI.Ui_wgNodeId):
    """ Data category widget. Contains node id data
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.pItem = None
        self.defaultState = 'expanded'
        super(DataNodeId, self).__init__()
        self.setupUi(self)

    @property
    def params(self):
        """ Get category ui params
            :return: Category params
            :rtype: dict """
        return {'nodeType': self.leNodeType, 'nodeName': self.leNodeName, 'nodeLabel': self.leNodeLabel}

    def setDataFromNode(self, node):
        """ Update params from given node
            :param node: Graph node
            :type node: QtSvg.QGraphicsSvgItem """
        for k, QWidget in self.params.iteritems():
            QWidget.setText(getattr(node, k))

    def clearData(self):
        """ Clear category params """
        for k, QWidget in self.params.iteritems():
            QWidget.clear()

#=================================== NODE CONNECTIONS ====================================#

class DataNodeConnections(QtGui.QWidget, wgDataNodeConnUI.Ui_wgNodeConnections):
    """ Data category widget. Contains node connections data
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.pItem = None
        self.currentNode = None
        self.defaultState = 'collapsed'
        super(DataNodeConnections, self).__init__()
        self.upIcon = QtGui.QIcon("gui/icon/png/arrowUpBlue.png")
        self.dnIcon = QtGui.QIcon("gui/icon/png/arrowDnBlue.png")
        self.delIcon = QtGui.QIcon("gui/icon/png/buttonDel.png")
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup 'Node Connections' data category """
        self.setupUi(self)
        self.pbUp.setIcon(self.upIcon)
        self.pbUp.clicked.connect(partial(self.on_moveConnection, side='up'))
        self.pbDn.setIcon(self.dnIcon)
        self.pbDn.clicked.connect(partial(self.on_moveConnection, side='down'))
        self.pbDel.setIcon(self.delIcon)
        self.pbDel.clicked.connect(self.on_deleteConnection)

    @property
    def connectionsType(self):
        """ Get allowed connection type
            :return: Node connection type
            :rtype: list """
        return ['inputFile', 'inputData', 'outputFile']

    def getTypeItem(self, typeName):
        """ Get connection type item
            :param typeName: Connection type name
            :type typeName: str
            :return: Connection type item
            :rtype: QtGui.QTreeWidgetItem """
        for item in pQt.getTopItems(self.twNodeConnections):
            if item.connType == typeName:
                return item

    def addConnectionsType(self):
        """ Add Connection type item """
        for connType in self.connectionsType:
            newCat = QtGui.QTreeWidgetItem()
            newCat.connType = connType
            newCat._widget = NodeConnectionGroup(self.mainUi, newCat)
            self.twNodeConnections.addTopLevelItem(newCat)
            self.twNodeConnections.setItemWidget(newCat, 0, newCat._widget)

    def setDataFromNode(self, node):
        """ Update params from given node
            :param node: Graph node
            :type node: QtSvg.QGraphicsSvgItem """
        self.currentNode = node
        self.twNodeConnections.clear()
        self.addConnectionsType()
        connInfo = self.currentNode.getConnections()
        for k in self.connectionsType:
            items = []
            if k in connInfo.keys():
                typeItem = self.getTypeItem(k)
                for n in sorted(connInfo[k].keys()):
                    if k == 'outputFile':
                        direction = 'dst'
                    else:
                        direction = 'src'
                    newLink = QtGui.QTreeWidgetItem()
                    newLink.index = n
                    newLink.linkedLine = connInfo[k][n]['line']
                    newLink.linkedNode = connInfo[k][n]['%sNode' % direction]
                    newLink.linkedPlug = connInfo[k][n]['%sItem' % direction]
                    newLink._widget = NodeConnectionItem(self.mainUi, newLink)
                    typeItem.addChild(newLink)
                    self.twNodeConnections.setItemWidget(newLink, 0, newLink._widget)
                    items.append(newLink)
                if items:
                    typeItem._widget.lCount.setText(str(len(items)))
                    typeItem._widget.pbGrpName.setChecked(True)
                    typeItem._widget.on_icon()
                else:
                    typeItem._widget.lCount.setText("0")

    def on_moveConnection(self, side='up'):
        """ Edit connection order
            :param side: 'up' or 'down'
            :type side: str """
        selItems = self.twNodeConnections.selectedItems()
        if selItems and self.currentNode is not None and self.mainUi.editMode:
            item = selItems[0]
            parent = item.parent()
            linkedNodeName = item.linkedNode.nodeLabel
            plug = getattr(self.currentNode, '%sConnection' % parent.connType)
            if side == 'up':
                if item.index > 0:
                    self.log.debug("Moving connection up: %s ..." % linkedNodeName)
                    link = plug.connections.pop(item.index)
                    plug.connections.insert((item.index - 1), link)
            else:
                if item.index < (parent.childCount() - 1):
                    self.log.debug("Moving connection down: %s ..." % linkedNodeName)
                    link = plug.connections.pop(item.index)
                    plug.connections.insert((item.index + 1), link)
            self.setDataFromNode(self.currentNode)
            #-- Keep Item Selected --#
            for n in range(self.twNodeConnections.topLevelItemCount()):
                grpItem = self.twNodeConnections.topLevelItem(n)
                if grpItem.connType == parent.connType:
                    for c in range(grpItem.childCount()):
                        if grpItem.child(c).linkedNode.nodeLabel == linkedNodeName:
                            self.twNodeConnections.setItemSelected(grpItem.child(c), True)

    def on_deleteConnection(self):
        """ Command launched when 'Delete' QPushButton is clicked,
            Delete selected connection """
        if self.mainUi.editMode and self.currentNode is not None:
            for item in self.twNodeConnections.selectedItems():
                if item.parent() is not None:
                    item._widget.lineConnection.deleteLine()
                    self.setDataFromNode(self.currentNode)

    def clearData(self):
        """ Clear category params """
        self.twNodeConnections.clear()


class NodeConnectionGroup(QtGui.QWidget, wgDataConnGroupUI.Ui_wgConnGroup):
    """ Connection category group widget
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow
        :param pItem: Parent widget item
        :type pItem: QtGui.QTreeWidgetItem """

    def __init__(self, mainUi, pItem):
        self.mainUi = mainUi
        self.pItem = pItem
        self.grpName = self.pItem.connType
        self.collapsedIcon= QtGui.QIcon("gui/icon/png/itemCollapsed.png")
        self.expandedIcon = QtGui.QIcon("gui/icon/png/itemExpanded.png")
        super(NodeConnectionGroup, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget """
        self.setupUi(self)
        self.lGrpName.setText(self.grpName)
        self.pbGrpName.clicked.connect(self.on_icon)
        self.rf_icon()

    def rf_icon(self):
        """ Refresh category group icon button """
        if self.pbGrpName.isChecked():
            self.pbGrpName.setIcon(self.expandedIcon)
        else:
            self.pbGrpName.setIcon(self.collapsedIcon)

    def on_icon(self):
        """ Command launched when category group button is clicked,
            Expand category group """
        self.pItem.treeWidget().setItemExpanded(self.pItem, self.pbGrpName.isChecked())
        self.rf_icon()


class NodeConnectionItem(QtGui.QWidget, wgDataConnItemUI.Ui_wgDataConnItem):
    """ Connection category item widget
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow
        :param pItem: Parent widget item
        :type pItem: QtGui.QTreeWidgetItem """

    def __init__(self, mainUi, pItem):
        self.mainUi = mainUi
        self.pItem = pItem
        self.index = self.pItem.index
        self.lineConnection = self.pItem.linkedLine
        self.linkedNode = self.pItem.linkedNode
        self.linkedPlug = self.pItem.linkedPlug
        super(NodeConnectionItem, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup Widget """
        self.setupUi(self)
        self.lIndex.setText(str(self.index))
        self.lConnectedNode.setText(self.linkedNode.nodeLabel)

    def mouseDoubleClickEvent(self, event):
        """ Add mouse double click options: Select linked node in graphScene """
        if self.pItem.isSelected():
            graphScene = self.mainUi.currentGraphScene
            graphScene.clearNodeSelection()
            self.pItem._widget.linkedNode.setSelected(True)
            graphScene.rf_nodesElementId()
            self.pItem._widget.linkedNode.connectNodeData()
