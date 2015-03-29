from PyQt4 import QtGui
from functools import partial
from lib.qt import procQt as pQt
from tools.maya.cmds import pRigg
from tools.maya.cloth.clothEditor import clothEditorCmds as ceCmds
from tools.maya.cloth.clothEditor.ui import wgSceneNodesUI, wgVtxMapUI, wgVtxMapNodeUI


class SceneNodeUi(QtGui.QWidget, wgSceneNodesUI.Ui_wgSceneNodes):
    """ Widget SceneNodes, child of mainUi
        :param mainUi: VertexMap mainUi
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        print "\t ---> SceneNodeUi"
        self.mainUi = mainUi
        super(SceneNodeUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        self.pbRefresh.clicked.connect(self.on_refresh)
        self.twSceneNodes.itemClicked.connect(self.on_sceneNodeSingleClick)
        color = self.mainUi.getLabelColor('green')
        self.cbCloth.setStyleSheet("color: rgb(%s, %s, %s)" % (color[0], color[1], color[2]))
        self.cbCloth.clicked.connect(self.on_showClothType)
        color = self.mainUi.getLabelColor('blue')
        self.cbRigid.setStyleSheet("color: rgb(%s, %s, %s)" % (color[0], color[1], color[2]))
        self.cbRigid.clicked.connect(self.on_showClothType)
        self.cbFilters.clicked.connect(self.rf_filterVisibility)
        self.rf_filterVisibility()
        self.rf_sceneNodes()
        self.rf_sceneFilters()
        self.twFilters.header().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.twFilters.header().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)

    @property
    def itemAttrOrder(self):
        """ Get SceneNodeItem attribute list
            :return: Item attributes
            :rtype: list """
        return ['clothNode', 'clothNs', 'clothName', 'clothType', 'clothParent', 'clothMesh', 'clothShape']

    @property
    def filterParams(self):
        """ Get scene filter params
            :return: Filter params
            :rtype: dict """
        params = {}
        for item in pQt.getTopItems(self.twFilters):
            params[item.ns] = item._cb.isChecked()
        return params

    @property
    def selectedClothItem(self):
        """ Get selected sceneNode item
            :return: ClothNode item
            :rtype: QtGui.QTreeWidgetItem """
        selItems = self.twSceneNodes.selectedItems()
        if selItems:
            return selItems[0]

    @property
    def selectedClothNode(self):
        """ Get selected clothNode name
            :return: ClothNode name
            :rtype: str """
        if self.selectedClothItem is not None:
            return self.selectedClothItem.clothNode

    def rf_filterVisibility(self):
        """ Refresh 'Filters' QTreeWidget visibility """
        if self.cbFilters.isChecked():
            self.twFilters.setMaximumHeight(150)
        else:
            self.twFilters.setMaximumHeight(0)

    def rf_sceneNodes(self):
        """ Refresh QTreeWidget 'Scene Nodes' """
        self.twSceneNodes.clear()
        #-- Populate Nucleus node --#
        for nucleus in ceCmds.getAllNucleus():
            nucleusItem = self.add_sceneNode(nucleus)
            #-- Populate nCloth Node --#
            dynNodes = pRigg.findTypeInHistory(nucleus, ['nCloth', 'nRigid'], future=True, past=True)
            rigidNodes = []
            for node in dynNodes:
                nodeType = ceCmds.getClothType(node)
                if nodeType is not None:
                    if nodeType == 'nCloth':
                        self.add_sceneNode(node, parent=nucleusItem)
                    #-- Store nRigid Node (tree order) --#
                    elif nodeType == 'nRigid':
                        rigidNodes.append(node)
            #-- Populate nRigid Node --#
            for node in rigidNodes:
                self.add_sceneNode(node, parent=nucleusItem)

    def rf_sceneFilters(self):
        """ Refresh QTreeWidget 'Scene Nodes' """
        self.twFilters.clear()
        nsList = []
        for item in pQt.getAllItems(self.twSceneNodes):
            if not item.clothNs in nsList:
                nsList.append(item.clothNs)
                newItem = self.new_filterItem(item.clothNs)
                self.twFilters.addTopLevelItem(newItem)
                self.twFilters.setItemWidget(newItem, 0, newItem._cb)

    def rf_sceneItemToolTips(self):
        """ Refresh all sceneNodes item toolTip """
        for item in pQt.getAllItems(self.twSceneNodes):
            self.rf_sceneItemToolTip(item)

    def rf_sceneItemToolTip(self, item):
        """ Refresh given sceneNode item toolTip
            :param item: SceneNode  item
            :type item: QtGui.QTreeWidgetItem """
        txt = ""
        if self.mainUi.toolTipState:
            tips = []
            itemDict = item.__dict__
            for attr in item.attrOrder:
                if isinstance(itemDict[attr], str):
                    tips.append("%s = %r" % (attr, itemDict[attr]))
                else:
                    tips.append("%s = %s" % (attr, itemDict[attr]))
            txt = '\n'.join(tips)
        item.setToolTip(0, txt)

    def add_sceneNode(self, clothNode, parent=None):
        """ Add QTreeWidgetItem to 'SceneNodes' QTreeWidget
            :param clothNode: Cloth Node name
            :type clothNode: str
            :param parent: Parent item
            :type parent: QtGui.QTreeWidgetItem
            :return: New item
            :rtype: QtGui.QTreeWidgetItem """
        newItem = self.new_sceneNodeItem(clothNode)
        if parent is None:
            self.twSceneNodes.addTopLevelItem(newItem)
        else:
            parent.addChild(newItem)
        return newItem

    def on_refresh(self):
        """ Command launched when 'Refresh' QPushButton is clicked """
        self.cbCloth.setChecked(True)
        self.cbRigid.setChecked(True)
        self.rf_sceneNodes()
        self.rf_sceneFilters()

    def on_sceneNodeSingleClick(self):
        """ Command launched when 'SceneNode' QTreeWidgetItem is single clicked """
        if self.mainUi.currentTab == 'Preset':
            pass
        elif self.mainUi.currentTab == 'VtxMap':
            self.mainUi.wgVtxMaps.rf_vtxMapTree()

    def on_showClothType(self):
        """ Command launched when QCheckBox 'nCloth' or 'nRigid' is clicked,
            Update QTreeWidget with selected cloth type """
        for item in pQt.getAllItems(self.twSceneNodes):
            if item.clothType == 'nCloth':
                self.twSceneNodes.setItemHidden(item, not self.cbCloth.isChecked())
            elif item.clothType == 'nRigid':
                self.twSceneNodes.setItemHidden(item, not self.cbRigid.isChecked())

    def on_filter(self, ns):
        """ Command launched when 'Filter' QCheckBox is clicked
            :param ns: NameSpace
            :type ns: str """
        filterDict = self.filterParams
        for topItem in pQt.getTopItems(self.twSceneNodes):
            if topItem.clothNs == ns:
                self.twSceneNodes.setItemHidden(topItem, not filterDict[topItem.clothNs])

    def new_sceneNodeItem(self, clothNode):
        """ Create new 'clothNode' QTreeWidgetItem
            :param clothNode: Cloth Node name
            :type clothNode: str
            :return: Scene node QTreeWidgetItem
            :rtype: QtGui.QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        #-- Add Attributes --#
        ns, name = ceCmds.getNamespace(clothNode)
        newItem.clothNode = clothNode
        newItem.clothNs = ns
        newItem.clothName = name
        newItem.clothType = ceCmds.getClothType(clothNode)
        if newItem.clothType == 'nucleus':
            newItem.clothParent = clothNode
            newItem.clothMesh = None
            newItem.clothShape = None
        else:
            newItem.clothParent = ceCmds.getNodeParent(clothNode)
            newItem.clothMesh = ceCmds.getModelFromClothNode(clothNode)
            newItem.clothShape = ceCmds.getNodeShape(newItem.clothMesh)
        newItem.attrOrder = self.itemAttrOrder
        #-- Setup Item --#
        newFont = QtGui.QFont()
        newFont.setBold(True)
        color = (self.mainUi.getLabelColor('default'))
        if newItem.clothType == 'nucleus':
            newFont.setPointSize(10)
            newItem.setText(0, newItem.clothNode)
            color = self.mainUi.getLabelColor('yellow')
        elif newItem.clothType == 'nCloth':
            newItem.setText(0, newItem.clothMesh)
            color = self.mainUi.getLabelColor('green')
        elif newItem.clothType == 'nRigid':
            newItem.setText(0, newItem.clothMesh)
            color = self.mainUi.getLabelColor('blue')
        newItem.setTextColor(0, QtGui.QColor(color[0], color[1], color[2]))
        newItem.setFont(0, newFont)
        self.rf_sceneItemToolTip(newItem)
        return newItem

    # noinspection PyUnresolvedReferences
    def new_filterItem(self, ns):
        """ Create new 'filter' QTreeWidgetItem
            :param ns: NameSpace
            :type ns: str
            :return: Scene filter QTreeWidgetItem
            :rtype: QtGui.QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem.setText(1, ns)
        newItem.ns = ns
        #-- Add CheckBox --#
        newCb = QtGui.QCheckBox()
        newCb.setText("")
        newCb.setChecked(True)
        newCb.clicked.connect(partial(self.on_filter, ns))
        newItem._cb = newCb
        return newItem


class VtxMapUi(QtGui.QWidget, wgVtxMapUI.Ui_wgVtxMap):
    """ Widget VertxMap, child of mainUi
        :param mainUi: VertexMap mainUi
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        print "\t ---> VtxMapUi"
        self.mainUi = mainUi
        self.sceneUi = self.mainUi.wgSceneNodes
        super(VtxMapUi, self).__init__()
        self._setupUi()

    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        color = self.mainUi.getLabelColor('lightGrey')
        self.pbNone.setStyleSheet("color: rgb(%s, %s, %s)" % (color[0], color[1], color[2]))
        color = self.mainUi.getLabelColor('green')
        self.pbVertex.setStyleSheet("color: rgb(%s, %s, %s)" % (color[0], color[1], color[2]))
        color = self.mainUi.getLabelColor('blue')
        self.pbTexture.setStyleSheet("color: rgb(%s, %s, %s)" % (color[0], color[1], color[2]))
        self.rf_vtxMapTree()

    def rf_vtxMapTree(self):
        """ Refresh 'Vertex Map' QTreeWidget """
        self.twMaps.clear()
        clothItem = self.sceneUi.selectedClothItem
        if clothItem is not None:
            if not clothItem.clothType == 'nucleus':
                vtxMaps = ceCmds.getVtxMaps(clothItem.clothNode)
                for mapName in vtxMaps:
                    newItem = self.new_vtxMapItem(clothItem.clothNode, mapName)
                    self.twMaps.addTopLevelItem(newItem)
                    self.twMaps.setItemWidget(newItem, 0, newItem._widget)

    @staticmethod
    def new_vtxMapItem(clothNode, mapName):
        """ Create new mapType 'QTreeWidgetItem'
            :param clothNode: Cloth node name
            :type clothNode: str
            :param mapName: Vertex map name
            :type mapName: str """
        newItem = QtGui.QTreeWidgetItem()
        newItem._widget = VtxMapNode(clothNode, mapName)
        return newItem


class VtxMapNode(QtGui.QWidget, wgVtxMapNodeUI.Ui_wgVtxMapNode):
    """ Widget VertexMap item, child of VtxMapUi
        :param clothNode: Cloth node name
        :type clothNode: str
        :param mapName: Vertex map name
        :type mapName: str """

    def __init__(self, clothNode, mapName):
        self.clothNode = clothNode
        self.mapName = mapName
        self.typeName = "%sMapType" % self.mapName
        self.vtxName = "%sPerVertex" % self.mapName
        super(VtxMapNode, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        self.lVtxMap.setText(self.mapName)
