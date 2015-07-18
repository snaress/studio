import os
from PyQt4 import QtGui
from lib.env import studio
from functools import partial
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from lib.qt.scriptEditor import ScriptZone
from appli.grapher.core import grapher as gpCore
from appli.grapher.gui.ui import wgDataGroupUI, wgDataNodeIdUI, wgDataPlugItemUI, wgDataNodeConnUI, wgDataConnGroupUI,\
                                 wgDataConnItemUI, wgDataAssetCastingUI, wgDataNodeScriptUI


#======================================== GENERAL ========================================#

class DataZone(object):
    """
    Data zone constructor class
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("---> Setup DataZone ...")
        self.dataTree = self.mainUi.twNodeData
        self.dataGrpState = {}

    def getDataWidgetFromGroupName(self, groupName):
        """
        Get QWidget from data group name
        :param groupName: Data group name
        :type groupName: str
        :return: Data widget
        :rtype: QtGui.QWidget
        """
        for item in pQt.getTopItems(self.mainUi.twNodeData):
            if item._widget.grpName == groupName:
                return item.child(0)._widget

    def getGroupItemIndexFromGroupName(self, grpName):
        """
        Get topLevelItem position index
        :param grpName: Data group name
        :type grpName: str
        :return: Group item index
        :rtype: int
        """
        for n, item in enumerate(pQt.getTopItems(self.dataTree)):
            if item._widget.grpName == grpName:
                return n

    def addCategory(self, groupName, QWidget):
        """
        Add data category
        :param groupName: New category name
        :type groupName: str
        :param QWidget: Widget parent to new category
        :type QWidget: QtGui.QWidget
        """
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

    def addNodeCategory(self, node):
        """
        Add specific node data zone category
        :param node: Selected graph node
        :type node: QtSvg.QGraphicsSvgItem
        """
        for dWidget in node.dataWidgets():
             self.addCategory(dWidget['name'], dWidget['class'])

    def connectNodeData(self, node):
        """
        Connect graph node data to dataZone
        :param node: Selected graph node
        :type node: QtSvg.QGraphicsSvgItem
        """
        self.log.debug("Connecting node data: %s ..." % node.nodeName)
        self.addNodeCategory(node)
        groups = pQt.getTopItems(self.dataTree)
        for grpItem in groups:
            dataItem = grpItem.child(0)._widget
            dataItem.setDataFromNode(node)
        self.restoreDataGrpState()

    def restoreDataGrpState(self):
        """
        Restore data group state
        """
        for item in pQt.getTopItems(self.dataTree):
            if item._widget.grpName in self.dataGrpState.keys():
                storeState = self.dataGrpState[item._widget.grpName]
                itemState = item.isExpanded()
                if not storeState == itemState:
                    if itemState:
                        item._widget.pbGrpName.setChecked(False)
                    else:
                        item._widget.pbGrpName.setChecked(True)
                    item._widget.rf_icon()
                    item.setExpanded(self.dataGrpState[item._widget.grpName])

    def clearDataZone(self):
        """
        Clear grapher data zone
        """
        self.dataTree.clear()


class DataGroup(QtGui.QWidget, wgDataGroupUI.Ui_wgDataGroup):
    """
    Data category group widget
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    :param pItem: Parent widget item
    :type pItem: QtGui.QTreeWidgetItem
    :param groupName: Category group name
    :type groupName: str
    """

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
        """
        Setup category group
        """
        self.setupUi(self)
        self.lGrpName.setText(self.grpName)
        self.pbGrpName.clicked.connect(self.on_icon)
        self.rf_icon()

    def rf_icon(self):
        """
        Refresh category group icon button
        """
        if self.pbGrpName.isChecked():
            self.pbGrpName.setIcon(self.collapseIcon)
        else:
            self.pbGrpName.setIcon(self.expandIcon)

    def on_icon(self):
        """
        Command launched when category group button is clicked,
        Expand category group
        """
        self.pItem.treeWidget().setItemExpanded(self.pItem, self.pbGrpName.isChecked())
        self.rf_icon()
        self.mainUi.dataZone.dataGrpState[self.pItem._widget.grpName] = self.pItem.isExpanded()


class DataConnections(QtGui.QWidget, wgDataNodeConnUI.Ui_wgNodeConnections):
    """
    Data category widget. Contains node connections data
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.pItem = None
        self.currentNode = None
        self.connectionInfo = None
        super(DataConnections, self).__init__()
        self.upIcon = QtGui.QIcon("gui/icon/png/arrowUpBlue.png")
        self.dnIcon = QtGui.QIcon("gui/icon/png/arrowDnBlue.png")
        self.delIcon = QtGui.QIcon("gui/icon/png/buttonDel.png")
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup 'Node Connections' data category
        """
        self.setupUi(self)
        self.pbUp.setIcon(self.upIcon)
        self.pbUp.clicked.connect(partial(self.on_moveConnection, side='up'))
        self.pbDn.setIcon(self.dnIcon)
        self.pbDn.clicked.connect(partial(self.on_moveConnection, side='down'))
        self.pbDel.setIcon(self.delIcon)
        self.pbDel.clicked.connect(self.on_deleteConnection)
        self.rf_editModeState()

    def setDataFromNode(self, node):
        """
        Update params from given node
        :param node: Graph node
        :type node: QtSvg.QGraphicsSvgItem
        """
        self.currentNode = node
        self.connectionInfo = self.currentNode.getConnections()
        self.twNodeConnections.clear()
        items = []
        if self._plugType in self.connectionInfo.keys():
            for n in sorted(self.connectionInfo[self._plugType].keys()):
                if self._plugType == 'outputFile':
                    direction = 'dst'
                else:
                    direction = 'src'
                newLink = QtGui.QTreeWidgetItem()
                newLink.index = n
                newLink.connType = self._plugType
                newLink.linkedLine = self.connectionInfo[self._plugType][n]['line']
                newLink.linkedNode = self.connectionInfo[self._plugType][n]['%sNode' % direction]
                newLink.linkedPlug = self.connectionInfo[self._plugType][n]['%sItem' % direction]
                newLink._widget = DataConnectionItem(self.mainUi, self, newLink)
                self.twNodeConnections.addTopLevelItem(newLink)
                self.twNodeConnections.setItemWidget(newLink, 0, newLink._widget)
                items.append(newLink)

    def rf_editModeState(self):
        """
        Refresh connections buttons state
        """
        self.pbUp.setEnabled(self.mainUi.editMode)
        self.pbDn.setEnabled(self.mainUi.editMode)
        self.pbDel.setEnabled(self.mainUi.editMode)

    def on_moveConnection(self, side='up'):
        """
        Edit connection order
        :param side: 'up' or 'down'
        :type side: str
        """
        selItems = self.twNodeConnections.selectedItems()
        if selItems and self.currentNode is not None and self.mainUi.editMode:
            item = selItems[0]
            linkedNodeName = item.linkedNode.nodeName
            plug = getattr(self.currentNode, '%sPlug' % item.connType)
            if side == 'up':
                if item.index > 0:
                    self.log.debug("Moving connection up: %s ..." % linkedNodeName)
                    link = plug.connections.pop(item.index)
                    plug.connections.insert((item.index - 1), link)
            else:
                if item.index < (len(pQt.getTopItems(self.twNodeConnections)) - 1):
                    self.log.debug("Moving connection down: %s ..." % linkedNodeName)
                    link = plug.connections.pop(item.index)
                    plug.connections.insert((item.index + 1), link)
            self.setDataFromNode(self.currentNode)
            #-- Keep Item Selected --#
            for item in pQt.getTopItems(self.twNodeConnections):
                if item.linkedNode.nodeName == linkedNodeName:
                    self.twNodeConnections.setItemSelected(item, True)

    def on_deleteConnection(self):
        """
        Command launched when 'Delete' QPushButton is clicked,
        Delete selected connection
        """
        if self.mainUi.editMode and self.currentNode is not None:
            for item in self.twNodeConnections.selectedItems():
                item._widget.lineConnection.deleteLine()
                self.setDataFromNode(self.currentNode)


class DataConnectionItem(QtGui.QWidget, wgDataPlugItemUI.Ui_wgDataPlugItem):
    """
    Connection category item widget
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    :param pItem: Parent widget item
    :type pItem: QtGui.QTreeWidgetItem
    """

    def __init__(self, mainUi, pWidget, pItem):
        self.mainUi = mainUi
        self.pWidget = pWidget
        self.pItem = pItem
        self.index = self.pItem.index
        self.plugType = self.pWidget._plugType
        self.lineConnection = self.pItem.linkedLine
        self.linkedNode = self.pItem.linkedNode
        self.linkedPlug = self.pItem.linkedPlug
        super(DataConnectionItem, self).__init__()
        self.enableIcon = QtGui.QIcon("gui/icon/png/enable.png")
        self.disableIcon = QtGui.QIcon("gui/icon/png/disable.png")
        self._setupUi()

    def _setupUi(self):
        """
        Setup Widget
        """
        self.setupUi(self)
        if not self.plugType == "inputFile":
            self.qfInputFile.setVisible(False)
        self.lIndex.setText(str(self.index))
        self.lConnectedNode.setText(self.linkedNode.nodeName)
        self._addEnableIcon()

    # noinspection PyUnresolvedReferences
    def _addEnableIcon(self):
        """
        Add enable connection state icon
        """
        self.pbEnable.clicked.connect(self.rf_enableIcon)
        self.rf_enableIcon()

    def rf_enableIcon(self):
        """
        Refresh enable icon state
        """
        if self.pbEnable.isChecked():
            self.pbEnable.setIcon(self.enableIcon)
        else:
            self.pbEnable.setIcon(self.disableIcon)

    def mouseDoubleClickEvent(self, event):
        """
        Add mouse double click options: Select linked node in graphScene
        """
        if self.pItem.isSelected():
            self.mainUi.currentGraphScene.clearNodeSelection()
            self.pItem._widget.linkedNode.setSelected(True)
            self.mainUi.currentGraphScene.rf_nodesElementId()
            self.mainUi.dataZone.clearDataZone()
            self.mainUi.dataZone.connectNodeData(self.pItem._widget.linkedNode)

#======================================== NODE ID ========================================#

class DataNodeId(QtGui.QWidget, wgDataNodeIdUI.Ui_wgNodeId):
    """
    Data category widget. Contains node id data
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.pItem = None
        self.currentNode = None
        super(DataNodeId, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup 'Node Id' data category
        """
        self.setupUi(self)
        self.leNodeName.editingFinished.connect(self.on_name)
        self.rf_editModeState()

    @property
    def params(self):
        """
        Get category ui params
        :return: Category params
        :rtype: dict
        """
        return {'nodeType': self.leNodeType, 'nodeName': self.leNodeName, 'nodeId': self.leNodeId}

    def rf_editModeState(self):
        """
        Refresh label read only state
        """
        self.leNodeName.setReadOnly(not self.mainUi.editMode)
        # self.leNodeName.setEnabled(self.mainUi.editMode)

    def setDataFromNode(self, node):
        """
        Update params from given node
        :param node: Graph node
        :type node: QtSvg.QGraphicsSvgItem
        """
        self.currentNode = node
        for k, QWidget in self.params.iteritems():
            QWidget.setText(getattr(node, k))

    def on_name(self):
        """
        Command launched when 'Node Label' QLineEdit is edited.
        Will renome the node is in edit mode.
        """
        if not self.mainUi.editMode:
            self.leNodeName.setText(self.currentNode.nodeName)
        else:
            if self.currentNode is not None:
                self.currentNode.nodeName = str(self.leNodeName.text())
                self.currentNode.rf_toolTip()
                self.currentNode.rf_nodeLabel()
            else:
                self.leNodeName.clear()

#=================================== INPUT FILE PLUG =====================================#

class DataInputFilePlug(DataConnections):

    _plugType = "inputFile"

    def __init__(self, mainUi):
        super(DataInputFilePlug, self).__init__(mainUi)

#=================================== INPUT DATA PLUG =====================================#

class DataInputDataPlug(DataConnections):

    _plugType = "inputData"

    def __init__(self, mainUi):
        super(DataInputDataPlug, self).__init__(mainUi)

#================================== OUTPUT FILE PLUG =====================================#

class DataOutputFilePlug(DataConnections):

    _plugType = "outputFile"

    def __init__(self, mainUi):
        super(DataOutputFilePlug, self).__init__(mainUi)

#=================================== NODE CONNECTIONS ====================================#

# class DataNodeConnections(QtGui.QWidget, wgDataNodeConnUI.Ui_wgNodeConnections):
#     """
#     Data category widget. Contains node connections data
#     :param mainUi: Grapher main window
#     :type mainUi: QtGui.QMainWindow
#     """
#
#     def __init__(self, mainUi):
#         self.mainUi = mainUi
#         self.log = self.mainUi.log
#         self.pItem = None
#         self.currentNode = None
#         super(DataNodeConnections, self).__init__()
#         self.upIcon = QtGui.QIcon("gui/icon/png/arrowUpBlue.png")
#         self.dnIcon = QtGui.QIcon("gui/icon/png/arrowDnBlue.png")
#         self.delIcon = QtGui.QIcon("gui/icon/png/buttonDel.png")
#         self._setupUi()
#
#     # noinspection PyUnresolvedReferences
#     def _setupUi(self):
#         """
#         Setup 'Node Connections' data category
#         """
#         self.setupUi(self)
#         self.pbUp.setIcon(self.upIcon)
#         self.pbUp.clicked.connect(partial(self.on_moveConnection, side='up'))
#         self.pbDn.setIcon(self.dnIcon)
#         self.pbDn.clicked.connect(partial(self.on_moveConnection, side='down'))
#         self.pbDel.setIcon(self.delIcon)
#         self.pbDel.clicked.connect(self.on_deleteConnection)
#         self.rf_editModeState()
#
#     @property
#     def connectionsType(self):
#         """
#         Get allowed connection type
#         :return: Node connection type
#         :rtype: list
#         """
#         return ['inputFile', 'inputData', 'outputFile']
#
#     def getTypeItem(self, typeName):
#         """
#         Get connection type item
#         :param typeName: Connection type name
#         :type typeName: str
#         :return: Connection type item
#         :rtype: QtGui.QTreeWidgetItem
#         """
#         for item in pQt.getTopItems(self.twNodeConnections):
#             if item.connType == typeName:
#                 return item
#
#     def addConnectionsType(self):
#         """
#         Add Connection type item
#         """
#         for connType in self.connectionsType:
#             newCat = QtGui.QTreeWidgetItem()
#             newCat.connType = connType
#             newCat._widget = NodeConnectionGroup(self.mainUi, newCat)
#             self.twNodeConnections.addTopLevelItem(newCat)
#             self.twNodeConnections.setItemWidget(newCat, 0, newCat._widget)
#
#     def setDataFromNode(self, node):
#         """
#         Update params from given node
#         :param node: Graph node
#         :type node: QtSvg.QGraphicsSvgItem
#         """
#         self.currentNode = node
#         self.twNodeConnections.clear()
#         self.addConnectionsType()
#         connInfo = self.currentNode.getConnections()
#         for k in self.connectionsType:
#             items = []
#             if k in connInfo.keys():
#                 typeItem = self.getTypeItem(k)
#                 for n in sorted(connInfo[k].keys()):
#                     if k == 'outputFile':
#                         direction = 'dst'
#                     else:
#                         direction = 'src'
#                     newLink = QtGui.QTreeWidgetItem()
#                     newLink.index = n
#                     newLink.connType = typeItem.connType
#                     newLink.linkedLine = connInfo[k][n]['line']
#                     newLink.linkedNode = connInfo[k][n]['%sNode' % direction]
#                     newLink.linkedPlug = connInfo[k][n]['%sItem' % direction]
#                     newLink._widget = NodeConnectionItem(self.mainUi, self, newLink)
#                     typeItem.addChild(newLink)
#                     self.twNodeConnections.setItemWidget(newLink, 0, newLink._widget)
#                     items.append(newLink)
#                 if items:
#                     typeItem._widget.lCount.setText(str(len(items)))
#                     typeItem._widget.pbGrpName.setChecked(True)
#                     typeItem._widget.on_icon()
#                 else:
#                     typeItem._widget.lCount.setText("0")
#
#     def rf_editModeState(self):
#         """
#         Refresh connections buttons state
#         """
#         self.pbUp.setEnabled(self.mainUi.editMode)
#         self.pbDn.setEnabled(self.mainUi.editMode)
#         self.pbDel.setEnabled(self.mainUi.editMode)
#
#     def on_moveConnection(self, side='up'):
#         """
#         Edit connection order
#         :param side: 'up' or 'down'
#         :type side: str
#         """
#         selItems = self.twNodeConnections.selectedItems()
#         if selItems and self.currentNode is not None and self.mainUi.editMode:
#             item = selItems[0]
#             parent = item.parent()
#             linkedNodeName = item.linkedNode.nodeName
#             plug = getattr(self.currentNode, '%sPlug' % parent.connType)
#             if side == 'up':
#                 if item.index > 0:
#                     self.log.debug("Moving connection up: %s ..." % linkedNodeName)
#                     link = plug.connections.pop(item.index)
#                     plug.connections.insert((item.index - 1), link)
#             else:
#                 if item.index < (parent.childCount() - 1):
#                     self.log.debug("Moving connection down: %s ..." % linkedNodeName)
#                     link = plug.connections.pop(item.index)
#                     plug.connections.insert((item.index + 1), link)
#             self.setDataFromNode(self.currentNode)
#             #-- Keep Item Selected --#
#             for n in range(self.twNodeConnections.topLevelItemCount()):
#                 grpItem = self.twNodeConnections.topLevelItem(n)
#                 if grpItem.connType == parent.connType:
#                     for c in range(grpItem.childCount()):
#                         if grpItem.child(c).linkedNode.nodeName == linkedNodeName:
#                             self.twNodeConnections.setItemSelected(grpItem.child(c), True)
#
#     def on_deleteConnection(self):
#         """
#         Command launched when 'Delete' QPushButton is clicked,
#         Delete selected connection
#         """
#         if self.mainUi.editMode and self.currentNode is not None:
#             for item in self.twNodeConnections.selectedItems():
#                 if item.parent() is not None:
#                     item._widget.lineConnection.deleteLine()
#                     self.setDataFromNode(self.currentNode)


# class NodeConnectionGroup(QtGui.QWidget, wgDataConnGroupUI.Ui_wgConnGroup):
#     """
#     Connection category group widget
#     :param mainUi: Grapher main window
#     :type mainUi: QtGui.QMainWindow
#     :param pItem: Parent widget item
#     :type pItem: QtGui.QTreeWidgetItem
#     """
#
#     def __init__(self, mainUi, pItem):
#         self.mainUi = mainUi
#         self.pItem = pItem
#         self.grpName = self.pItem.connType
#         self.collapsedIcon= QtGui.QIcon("gui/icon/png/itemCollapsed.png")
#         self.expandedIcon = QtGui.QIcon("gui/icon/png/itemExpanded.png")
#         super(NodeConnectionGroup, self).__init__()
#         self._setupUi()
#
#     # noinspection PyUnresolvedReferences
#     def _setupUi(self):
#         """
#         Setup widget
#         """
#         self.setupUi(self)
#         self.lGrpName.setText(self.grpName)
#         self.pbGrpName.clicked.connect(self.on_icon)
#         self.rf_icon()
#
#     def rf_icon(self):
#         """
#         Refresh category group icon button
#         """
#         if self.pbGrpName.isChecked():
#             self.pbGrpName.setIcon(self.expandedIcon)
#         else:
#             self.pbGrpName.setIcon(self.collapsedIcon)
#
#     def on_icon(self):
#         """
#         Command launched when category group button is clicked,
#         Expand category group
#         """
#         self.pItem.treeWidget().setItemExpanded(self.pItem, self.pbGrpName.isChecked())
#         self.rf_icon()


# class NodeConnectionItem(QtGui.QWidget, wgDataConnItemUI.Ui_wgDataConnItem):
#     """
#     Connection category item widget
#     :param mainUi: Grapher main window
#     :type mainUi: QtGui.QMainWindow
#     :param pItem: Parent widget item
#     :type pItem: QtGui.QTreeWidgetItem
#     """
#
#     def __init__(self, mainUi, pWidget, pItem):
#         self.mainUi = mainUi
#         self.pWidget = pWidget
#         self.pItem = pItem
#         self.index = self.pItem.index
#         self.lineConnection = self.pItem.linkedLine
#         self.linkedNode = self.pItem.linkedNode
#         self.linkedPlug = self.pItem.linkedPlug
#         super(NodeConnectionItem, self).__init__()
#         self.enableIcon = QtGui.QIcon("gui/icon/png/enable.png")
#         self.disableIcon = QtGui.QIcon("gui/icon/png/disable.png")
#         self._setupUi()
#
#     def _setupUi(self):
#         """
#         Setup Widget
#         """
#         self.setupUi(self)
#         self.lIndex.setText(str(self.index))
#         self.lConnectedNode.setText(self.linkedNode.nodeName)
#         self._addEnableIcon()
#
#     # noinspection PyUnresolvedReferences
#     def _addEnableIcon(self):
#         """
#         Add enable connection state icon
#         """
#         if self.pItem.connType not in ['outputFile']:
#             self.pbEnable.clicked.connect(self.rf_enableIcon)
#             self.rf_enableIcon()
#         else:
#             self.pbEnable.setVisible(False)
#
#     def rf_enableIcon(self):
#         """
#         Refresh enable icon state
#         """
#         if self.pbEnable.isChecked():
#             self.pbEnable.setIcon(self.enableIcon)
#         else:
#             self.pbEnable.setIcon(self.disableIcon)
#
#     def mouseDoubleClickEvent(self, event):
#         """
#         Add mouse double click options: Select linked node in graphScene
#         """
#         if self.pItem.isSelected():
#             self.mainUi.currentGraphScene.clearNodeSelection()
#             self.pItem._widget.linkedNode.setSelected(True)
#             self.mainUi.currentGraphScene.rf_nodesElementId()
#             self.mainUi.dataZone.clearDataZone()
#             self.mainUi.dataZone.connectNodeData(self.pItem._widget.linkedNode)

#==================================== ASSET CASTING =====================================#

class DataNodeAssetCasting(QtGui.QWidget, wgDataAssetCastingUI.Ui_wgDataAssetCasting):
    """
    Data category widget. Contains node asset casting data
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.pItem = None
        self.log = self.mainUi.log
        super(DataNodeAssetCasting, self).__init__()
        self._setupUi()

    def _setupUi(self):
        """
        Setup 'Node Connections' data category
        """
        self.setupUi(self)

    @property
    def params(self):
        """
        Get category ui params
        :return: Category params
        :rtype: dict
        """
        return {'assetEntity': self.leAssetEntity, 'assetType': self.leAssetType, 'assetSpec': self.leAssetSpec,
                'assetName': self.leAssetName, 'assetNs': self.leNamespace}

    def setDataFromNode(self, node):
        """
        Update params from given node
        :param node: Graph node
        :type node: QtSvg.QGraphicsSvgItem
        """
        self.currentNode = node
        for k, QWidget in self.params.iteritems():
            if hasattr(node, k):
                v = getattr(node, k)
                if v is not None:
                    QWidget.setText(getattr(node, k))
                else:
                    QWidget.setText("None")
            else:
                setattr(node, k, None)
                QWidget.setText("None")

#===================================== PYTHON DATA ======================================#

class DataNodeScript(QtGui.QWidget, wgDataNodeScriptUI.Ui_wgDataScript):
    """
    Data category widget. Contains node script data
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.pItem = None
        self.externEditor = studio.pyCharm
        self.externIcon = QtGui.QIcon("gui/icon/png/arrowUpBlue.png")
        self.updatIcon = QtGui.QIcon("gui/icon/png/arrowDnGreen.png")
        super(DataNodeScript, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup 'Node Connections' data category
        """
        self.setupUi(self)
        self.setMinimumHeight(self.mainUi.twNodeData.height() - 100)
        self.scriptZone = ScriptZone()
        self.vlScriptZone.addWidget(self.scriptZone)
        self.pbExtern.setIcon(self.externIcon)
        self.pbExtern.clicked.connect(self.on_externScript)
        self.pbExtern.setToolTip("External Edit")
        self.pbUpdate.setIcon(self.updatIcon)
        self.pbUpdate.clicked.connect(self.on_updateScript)
        self.pbUpdate.setToolTip("Update Script")
        self.pbSave.clicked.connect(self.on_save)
        self.pbCancel.clicked.connect(self.on_cancel)
        self.rf_editModeState()

    def setDataFromNode(self, node):
        """
        Update params from given node
        :param node: Graph node
        :type node: QtSvg.QGraphicsSvgItem
        """
        self.currentNode = node
        if hasattr(node, 'scriptTxt'):
            self.scriptZone.setCode(node.scriptTxt)
        else:
            setattr(node, 'scriptTxt', "")
            self.scriptZone.setCode("")
        self.rf_sciptButtonsState()

    def rf_editModeState(self):
        """
        Refresh script buttons state
        """
        self.pbExtern.setVisible(self.mainUi.editMode)
        self.pbUpdate.setVisible(self.mainUi.editMode)
        self.pbSave.setEnabled(self.mainUi.editMode)
        self.pbCancel.setEnabled(self.mainUi.editMode)

    def rf_sciptButtonsState(self):
        """
        Refresh external edit buttons state
        """
        if self.currentNode is None:
            self.pbExtern.setEnabled(True)
            self.pbUpdate.setEnabled(False)
        else:
            if self.currentNode.externFile is None:
                self.pbExtern.setEnabled(True)
                self.pbUpdate.setEnabled(False)
            else:
                self.pbExtern.setEnabled(False)
                self.pbUpdate.setEnabled(True)

    def on_externScript(self):
        """
        Command launched when 'External Edit' QPuchButton is clicked.
        Write current script in tmpFile, then launched it in external script editor
        """
        if self.mainUi.projectFullName is not None:
            externPath = os.path.join(self.mainUi.grapherRootPath, 'users', self.mainUi.userName, 'tmp', 'externData')
            externProjectPath = gpCore.createExternPath(externPath, self.mainUi.projectFullName)
            self.currentNode.externFile = os.path.join(externProjectPath, '%s.py' % self.currentNode.nodeName)
            self.log.debug("External edtion: %s" % self.currentNode.externFile)
            try:
                pFile.writeFile(self.currentNode.externFile, str(self.scriptZone.getCode()))
            except:
                raise IOError, "!!! Can not write tmpFile for external edit !!!"
            self.rf_sciptButtonsState()
            os.system('%s %s' % (os.path.normpath(self.externEditor), os.path.normpath(self.currentNode.externFile)))
        else:
            self.log.error("!!! No project loaded !!!")

    def on_updateScript(self):
        """
        Command launched when 'Update Script' QPuchButton is clicked. Update current script from tmpFile.
        """
        if self.currentNode.externFile is None:
            raise IOError, "!!! Can not find extern file!!!"
        self.log.debug("Update script from %s" % self.currentNode.externFile)
        self.scriptZone.setCode(''.join(pFile.readFile(self.currentNode.externFile)))
        self.currentNode.externFile = None
        self.rf_sciptButtonsState()

    def on_save(self):
        """
        Command launched when 'Save' QPuchButton is clicked. Save script state
        """
        self.log.info("Saving script to data node ...")
        self.currentNode.scriptTxt = str(self.scriptZone.getCode())

    def on_cancel(self):
        """
        Command launched when 'Cancel' QPuchButton is clicked.
        Restore script to last save state
        """
        self.log.info("Canceling script edition ...")
        self.scriptZone.setCode(self.currentNode.scripTxt)
