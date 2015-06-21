from PyQt4 import QtGui
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
        self.pItem = None
        self.defaultState = 'collapsed'
        super(DataNodeConnections, self).__init__()
        self.setupUi(self)

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
            newCat._widget = NodeConnectionGroup(self.mainUi, newCat, groupName=connType)
            self.twNodeConnections.addTopLevelItem(newCat)
            self.twNodeConnections.setItemWidget(newCat, 0, newCat._widget)

    def setDataFromNode(self, node):
        """ Update params from given node
            :param node: Graph node
            :type node: QtSvg.QGraphicsSvgItem """
        self.twNodeConnections.clear()
        self.addConnectionsType()
        connInfo = node.getConnections()
        for k in self.connectionsType:
            items = []
            if k in connInfo.keys():
                typeItem = self.getTypeItem(k)
                for n in sorted(connInfo[k].keys()):
                    if k == 'outputFile':
                        linkedNode = connInfo[k][n]['dstNode']
                    else:
                        linkedNode = connInfo[k][n]['srcNode']
                    newLink = QtGui.QTreeWidgetItem()
                    newLink._widget = NodeConnectionItem(self.mainUi, newLink, n, linkedNode)
                    typeItem.addChild(newLink)
                    self.twNodeConnections.setItemWidget(newLink, 0, newLink._widget)
                    items.append(newLink)
                if items:
                    typeItem._widget.lCount.setText(str(len(items)))
                    typeItem._widget.pbGrpName.setChecked(True)
                    typeItem._widget.on_icon()
                else:
                    typeItem._widget.lCount.setText("0")

    def clearData(self):
        """ Clear category params """
        self.twNodeConnections.clear()


class NodeConnectionGroup(QtGui.QWidget, wgDataConnGroupUI.Ui_wgConnGroup):
    """ Connection category group widget
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow
        :param pItem: Parent widget item
        :type pItem: QtGui.QTreeWidgetItem
        :param groupName: Connection category group name
        :type groupName: str """

    def __init__(self, mainUi, pItem, groupName='Untitled'):
        self.mainUi = mainUi
        self.pItem = pItem
        self.grpName = groupName
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
        self.pbGrpSelect.clicked.connect(self.on_select)
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

    def on_select(self):
        if self.pItem.isSelected():
            print 'sel'
        else:
            for n in range(self.pItem.childCount()):
                if self.pItem.child(n).isSelected():
                    print 'child sel'


class NodeConnectionItem(QtGui.QWidget, wgDataConnItemUI.Ui_wgDataConnItem):
    """ Connection category item widget
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow
        :param pItem: Parent widget item
        :type pItem: QtGui.QTreeWidgetItem
        :param index: Connection index
        :type index: int
        :param linkedNode: Linked graph node
        :type linkedNode: QtSvg.QGraphicsSvgItem"""

    def __init__(self, mainUi, pItem, index, linkedNode):
        self.mainUi = mainUi
        self.pItem = pItem
        self.index = index
        self.linkedNode = linkedNode
        super(NodeConnectionItem, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup Widget """
        self.setupUi(self)
        self.lIndex.setText(str(self.index))
        self.lConnectedNode.setText(self.linkedNode.nodeLabel)
