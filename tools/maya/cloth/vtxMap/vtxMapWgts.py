from PyQt4 import QtGui, QtCore, Qt
from functools import partial
from lib.qt import procQt as pQt
from tools.maya.cloth.vtxMap import vtxMapCmds as vmCmds
from tools.maya.cloth.vtxMap.ui import wgSceneNodesUI, wgVtxTypeUI, wgVtxMapUI, wgVtxEditUI, wgVtxInfoUI


class SceneNodeUi(QtGui.QWidget, wgSceneNodesUI.Ui_wgSceneNodes):
    """ Widget SceneNodes, child of mainUi
        :param mainUi: VertexMap mainUi
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        super(SceneNodeUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        self.pbUpdate.clicked.connect(self.on_update)
        self.twSceneNodes.itemClicked.connect(self.on_sceneNodes)
        self.twSceneNodes.itemDoubleClicked.connect(self.on_selectSceneNode)
        self.cbCloth.clicked.connect(self.on_showClothType)
        self.cbRigid.clicked.connect(self.on_showClothType)

    def rf_sceneNodes(self, nCloth=True, nRigid=True):
        """ Refresh QTreeWidget 'Scene Nodes'
            :param nCloth: Enable nCloth type node listing
            :type nCloth: bool
            :param nRigid: Enable nRigid type node listing
            :type nRigid: bool """
        self.twSceneNodes.clear()
        items = []
        for node in vmCmds.getAllClothNodes():
            if nCloth:
                if vmCmds.getClothType(node) == 'nCloth':
                    newItem = self.new_sceneNodeItem(node)
                    items.append(newItem)
            if nRigid:
                if vmCmds.getClothType(node) == 'nRigid':
                    newItem = self.new_sceneNodeItem(node)
                    items.append(newItem)
        self.twSceneNodes.addTopLevelItems(items)

    def on_update(self):
        """ Command launched when QPushButton 'Update From Scene' is clicked,
            Update scene nodes with current selected (if only one object is selected)"""
        self.rf_sceneNodes()
        allItems = pQt.getAllItems(self.twSceneNodes)
        selected = vmCmds.getClothNodesFromSel()
        if selected:
            for item in allItems:
                if item.nodeShape == selected[0]:
                    self.twSceneNodes.setItemSelected(item, True)
                    break

    def on_sceneNodes(self):
        """ Command launched when QTreeWidgetItem 'Scene Nodes' is clicked,
            Update mainUi with selected clothNode """
        selItems = self.twSceneNodes.selectedItems()
        if selItems:
            self.mainUi.on_init(shapeName=selItems[0].nodeShape)

    def on_selectSceneNode(self):
        """ Command launched when QTreeWidgetItem 'Scene Nodes' is double clicked,
            Update maya Ui with selected clothNode """
        selItems = self.twSceneNodes.selectedItems()
        if selItems:
            self.on_sceneNodes()
            vmCmds.selectModel(self.mainUi.clothNode)

    def on_showClothType(self):
        """ Command launched when QCheckButton 'nCloth' or 'nRigid' is clicked,
            Update QTreeWidget with selected cloth type """
        self.rf_sceneNodes(nCloth=self.cbCloth.isChecked(), nRigid=self.cbRigid.isChecked())

    @staticmethod
    def new_sceneNodeItem(clothNode):
        """ Create new clothNode 'QTreeWidgetItem'
            :param clothNode: Cloth node name
            :type clothNode: str
            :return: Scene node QTreeWidgetItem
            :rtype: QtGui.QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        #-- Set label --#
        label = vmCmds.getClothNodeParent(clothNode)
        if label is None:
            raise ValueError
        newItem.setText(0, label)
        #-- Set Color --#
        nodeType = vmCmds.getClothType(clothNode)
        if nodeType == 'nCloth':
            newItem.setTextColor(0, Qt.QColor(0, 255, 0))
        elif nodeType == 'nRigid':
            newItem.setTextColor(0, Qt.QColor(0, 150, 255))
        #-- Store Data --#
        newItem.nodeName = label
        newItem.nodeShape = clothNode
        newItem.nodeType = nodeType
        return newItem


class VtxMapUi(QtGui.QWidget, wgVtxTypeUI.Ui_wgVtxType):
    """ Widget VtxMapType, child of mainUi
        :param mainUi: VertexMap mainUi
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        super(VtxMapUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        self.twMapType.itemClicked.connect(self.on_mapTypeNode)
        self.twMapType.itemDoubleClicked.connect(self.on_mapTypePaint)
        self.pbNone.setStyleSheet("color: rgb(175, 175, 175)")
        self.pbNone.clicked.connect(partial(self.on_editAll, 'None'))
        self.pbVertex.setStyleSheet("color: rgb(0, 255, 0)")
        self.pbVertex.clicked.connect(partial(self.on_editAll, 'Vertex'))
        self.pbTexture.setStyleSheet("color: rgb(0, 150, 255)")
        self.pbTexture.clicked.connect(partial(self.on_editAll, 'Texture'))

    @property
    def clothNode(self):
        """ Get cloth node name from ui
            :return: Initialized cloth node name
            :rtype: str """
        return self.mainUi.clothNode

    def rf_mapType(self):
        """ Refresh QTreeWidget 'Vertex Map Type' """
        self.twMapType.clear()
        if self.clothNode is not None:
            vtxMaps = vmCmds.getVtxMaps(self.clothNode)
            mapItems = []
            for mapType in vtxMaps:
                newItem = self.new_vtxMapItem(self.clothNode, mapType)
                mapItems.append(newItem)
            self.twMapType.addTopLevelItems(mapItems)
            for item in mapItems:
                self.twMapType.setItemWidget(item, 0, item._widget)

    def on_mapTypeNode(self):
        """ Command launched when QTreeWidgetItem 'MapType Nodes' is clicked
            Refresh vertexInfo """
        self.mainUi.wgVtxInfo.rf_vtxInfluence()

    def on_mapTypePaint(self):
        """ Command launched when QTreeWidgetItem 'MapType Nodes' is double clicked
            Enable vertex map painting """
        selItems = self.twMapType.selectedItems()
        if selItems:
            vmCmds.paintVtxMap(selItems[0]._widget.clothNode, selItems[0]._widget.mapName)

    def on_editAll(self, mapType):
        """ Command launched when QPushButton 'None', 'Vertex' or 'Texture' is clicked,
            Set all items to given vertexMap type, update clothNode
            :param mapType: Vertex map type ('None', 'Vertex', 'Texture')
            :type mapType: str """
        vtxMaps = pQt.getAllItems(self.twMapType)
        for item in vtxMaps:
            if mapType == 'None':
                item._widget.cbState.setCurrentIndex(0)
            elif mapType == 'Vertex':
                item._widget.cbState.setCurrentIndex(1)
            elif mapType == 'Texture':
                item._widget.cbState.setCurrentIndex(2)

    @staticmethod
    def new_vtxMapItem(clothNode, mapName):
        """ Create new mapType 'QTreeWidgetItem'
            :param clothNode: (str) : Cloth node name
            :param mapName: (str) : Cloth node map type """
        newItem = QtGui.QTreeWidgetItem()
        newItem._widget = VtxMapNode(clothNode, mapName)
        return newItem


class VtxMapNode(QtGui.QWidget, wgVtxMapUI.Ui_wgVtxMap):
    """ Widget VertexMap item, child of VtxMapUi
        :param clothNode: Cloth node name
        :type clothNode: str
        :param mapName: Vertex map name
        :type mapName: str """

    def __init__(self, clothNode, mapName):
        self.clothNode = clothNode
        self.mapName = mapName
        self.mapType = "%sMapType" % self.mapName
        self.vtxMap = "%sPerVertex" % self.mapName
        super(VtxMapNode, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        self.lVtxMap.setText(self.mapName)
        self.cbState.setCurrentIndex(vmCmds.getVtxMapType(self.clothNode, self.mapType))
        self.cbState.currentIndexChanged.connect(self.on_mapType)
        self.rf_vtxMapLabel()

    @property
    def vtxMapIndex(self):
        """ Get vtxMap current type
            :return: VtxMap type (0 = None, 1 = Vertex, 2 = Texture)
            :rtype: int """
        return self.cbState.currentIndex()

    @property
    def vtxMapType(self):
        """ Get vtxMap current type
            :return: VtxMap type (None, Vertex or Texture)
            :rtype: str """
        return str(self.cbState.currentText())

    def rf_vtxMapLabel(self):
        """ Refresh mapType label color """
        if self.vtxMapIndex == 0:
            self.lVtxMap.setStyleSheet("color: rgb(175, 175, 175)")
        elif self.vtxMapIndex == 1:
            self.lVtxMap.setStyleSheet("color: rgb(0, 255, 0)")
        elif self.vtxMapIndex == 2:
            self.lVtxMap.setStyleSheet("color: rgb(0, 125, 255)")

    def on_mapType(self):
        """ Command launched when QComboBox 'mapType' current index changed
            Set clothNode mapType, and refresh ui """
        vmCmds.setVtxMapType(self.clothNode, self.mapType, self.cbState.currentIndex())
        self.rf_vtxMapLabel()


class VtxEditUi(QtGui.QWidget, wgVtxEditUI.Ui_wgVtxEdit):
    """ Widget VtxMapEdit, child of mainUi
        :param mainUi: VertexMap mainUi
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        super(VtxEditUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        self.rbVtxRange.clicked.connect(self.rf_vtxSelMode)
        self.rbVtxValue.clicked.connect(self.rf_vtxSelMode)
        self.pbVtxSelect.clicked.connect(self.on_vtxSelection)
        self.pbVtxClear.clicked.connect(self.on_vtxClear)
        self.pbFlood.clicked.connect(self.on_flood)
        for n in range(5):
            newButton = VtxStorageButton('Set_%s' % (n+1), 'vtxSet', self.mainUi)
            self.hlVtxStorage.addWidget(newButton)
        for n in range(5):
            newButton = VtxStorageButton('Data_%s' % (n+1), 'vtxData', self.mainUi)
            self.hlDataStorage.addWidget(newButton)

    @property
    def clothNode(self):
        """ Get cloth node name from ui
            :return: Initialized cloth node name
            :rtype: str """
        return self.mainUi.clothNode

    @property
    def vtxMode(self):
        """ Get vertex edit mode
            :return: 'replace', 'add' or 'mult'
            :rtype: str """
        if self.rbEditReplace.isChecked():
            return 'replace'
        elif self.rbEditAdd.isChecked():
            return 'add'
        elif self.rbEditMult.isChecked():
            return 'mult'

    @property
    def vtxValue(self):
        """ Get vertex edition value
            :return: Edition value
            :rtype: float """
        return self.sbEditVal.value()

    @property
    def vtxClamp(self):
        """ Get clamp min and max state and value
            :return: Minimum clamp value (None if disable), Maximum clamp value (None if disable)
            :rtype: (float, float) """
        clampMin = None
        clampMax = None
        if self.cbClampMin.isChecked():
            clampMin = self.sbClampMin.value()
        if self.cbClampMax.isChecked():
            clampMax = self.sbClampMax.value()
        return clampMin, clampMax

    def rf_vtxSelMode(self):
        """ Refresh 'Vertex Selection Mode' """
        if self.rbVtxRange.isChecked():
            self.lRangeMin.setText("Min=")
            self.lRangeMax.setVisible(True)
            self.sbRangeMax.setVisible(True)
        else:
            self.lRangeMin.setText("Value=")
            self.lRangeMax.setVisible(False)
            self.sbRangeMax.setVisible(False)

    def on_vtxSelection(self):
        """ Command launched when QPushButton 'Select' is clicked,
            Select vertex which vtxMap value match with range edition """
        selItems = self.mainUi.wgVtxType.twMapType.selectedItems()
        if selItems:
            if self.rbVtxRange.isChecked():
                vmCmds.selectVtxInfluence(selItems[0]._widget.clothNode, selItems[0]._widget.vtxMap, 'range',
                                          minInf=self.sbRangeMin.value(), maxInf=self.sbRangeMax.value())
            elif self.rbVtxValue.isChecked():
                vmCmds.selectVtxInfluence(selItems[0]._widget.clothNode, selItems[0]._widget.vtxMap, 'value',
                                          value=self.sbRangeMin.value())

    @staticmethod
    def on_vtxClear():
        """ Command launched when QPushButton 'Clear' (range) is clicked,
            Clear scene selection """
        vmCmds.clearVtxSelection()

    def on_flood(self):
        """ Command launched when QPushButton 'Flood' is clicked,
            Edit selected vertex map influence with new edited influence """
        #-- Get Vertex Data Info --#
        selItems = self.mainUi.wgVtxType.twMapType.selectedItems()
        if selItems:
            clothNode = selItems[0]._widget.clothNode
            vtxMap = selItems[0]._widget.vtxMap
            vtxSel = vmCmds.getModelSelVtx(clothNode, indexOnly=True)
            vtxData = vmCmds.getVtxMapData(clothNode, vtxMap)
            for ind in vtxSel:
                newVal = None
                #-- Get New Vertex Value --#
                if self.vtxMode == 'replace':
                    newVal = self.vtxValue
                elif self.vtxMode == 'add':
                    newVal = float(vtxData[ind] + self.vtxValue)
                elif self.vtxMode == 'mult':
                    newVal = float(vtxData[ind] * self.vtxValue)
                if newVal is not None:
                    #-- Check Vertex Clamp --#
                    clampMin, clampMax = self.vtxClamp
                    if clampMin is not None:
                        if newVal < clampMin:
                            newVal = clampMin
                    if clampMax is not None:
                        if newVal > clampMax:
                            newVal = clampMax
                    #-- Edit Vertex Data --#
                    vtxData[ind] = newVal
            #-- Set Vertex Map --#
            vmCmds.setVtxMapData(clothNode, vtxMap, vtxData)


class VtxStorageButton(QtGui.QPushButton):

    def __init__(self, btnLabel, btnType, mainUi, parent=None):
        self.btnLabel = btnLabel
        self.btnType = btnType
        self.mainUi = mainUi
        self.storage = []
        super(VtxStorageButton,self).__init__(parent)
        self._setupUi()

    def _setupUi(self):
        """ Setup widget ui """
        self.setText(self.btnLabel)
        self.setToolTip("Empty")

    def mousePressEvent(self, event):
        """ Detect left or right click on QPushButton
            :param event: event
            :type event: QtGui.QEvent """
        if event.button() == QtCore.Qt.LeftButton:
            self.on_leftClick()
        elif event.button() == QtCore.Qt.RightButton:
            self.on_rightClick()

    def on_leftClick(self):
        """ Command launched when QPushButton is left clicked, Restore stored selection """
        if self.storage:
            if self.btnType == 'vtxSet':
                self.on_vtxSet()
            elif self.btnType == 'vtxData':
                self.on_vtxData()

    def on_vtxSet(self):
        """ Command launched QPushButton is clicked, restore vertex set selection """
        vmCmds.selectVtxOnModel(self.storage)

    def on_vtxData(self):
        """ Command launched QPushButton is clicked, restore vertex data storage """
        items = self.mainUi.wgVtxType.twMapType.selectedItems()
        if items:
            curData = vmCmds.getVtxMapData(items[0]._widget.clothNode, items[0]._widget.vtxMap)
            if not len(curData) == len(self.storage):
                print "!!! WARNING: Topo not the same !"
            else:
                vmCmds.setVtxMapData(items[0]._widget.clothNode, items[0]._widget.vtxMap, self.storage)

    def on_rightClick(self):
        """ Command launched when QPushButton is right clicked, launch popupMenu """
        menuDict = self._getPmItems()
        if menuDict:
            self.pmMenu = pQt.popupMenu(menuDict)
            #-- Refresh Menu Items Visibility --#
            if not self.storage:
                self.pmMenu.items[0].setEnabled(False)
                self.pmMenu.items[2].setEnabled(False)
            else:
                self.pmMenu.items[1].setEnabled(False)
            #-- Pop Menu --#
            self.pmMenu.exec_()

    def _getPmItems(self):
        """ get menuDict considering btnType
            :return: Menu data
            :rtype: dict """
        menuDict = {0: ['Edit ToolTip', self.on_editToolTip]}
        if self.btnType == 'vtxSet':
            menuDict[1] = ['Store Selected Vertex', self.on_storeVtxSet]
            menuDict[2] = ['Clear Vertex Storage', self.on_clearStorage]
        elif self.btnType == 'vtxData':
            menuDict[1] = ['Store Selected Data', self.on_storeVtxData]
            menuDict[2] = ['Clear Data Storage', self.on_clearStorage]
        return menuDict

    def on_editToolTip(self):
        """ Command launched when QAction 'Edit ToolTip' is clicked, Launch promp dialog """
        self.dialToolTip = pQt.PromptDialog("Edit ToolTip", self._dialToolTipAccept)
        self.dialToolTip.exec_()

    def _dialToolTipAccept(self):
        """ Command launched when QDialog 'dialToolTip' is accepted, edit button toolTip """
        self.setToolTip(self.dialToolTip.result()['result_1'])
        self.dialToolTip.close()

    def on_storeVtxSet(self):
        """ Command launched when QAction 'Store Vertex Selection' is clicked,
            Store selected vertex in 'storage' """
        vtxList = self.mainUi.cleanVtxIndexList()
        if vtxList:
            self.storage = vtxList
            print "// Vertex storage: %s : Success !" % self.btnLabel
        else:
            print "!!! WARNING: No vertex found to store !!!"

    def on_storeVtxData(self):
        """ Command launched when QAction 'Store Vertex Data' is clicked,
            Store selected data in 'storage' """
        items = self.mainUi.wgVtxType.twMapType.selectedItems()
        if items:
            data = vmCmds.getVtxMapData(items[0]._widget.clothNode, items[0]._widget.vtxMap)
            if data:
                self.storage = data
                print "// Data storage: %s : Success !" % self.btnLabel
            else:
                print "!!! WARNING: No data found to store !!!"

    def on_clearStorage(self):
        """ Command launched when QAction 'Clear ... Storage' is clicked,
            reset 'storage' """
        self.storage = []
        self.setToolTip("Empty")


class VtxInfoUi(QtGui.QWidget, wgVtxInfoUI.Ui_wgVtxInfo):
    """ Widget VtxMapInfo, child of mainUi
        :param mainUi: VertexMap mainUi
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        super(VtxInfoUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        self.pbUpdateInf.clicked.connect(self.on_updateInfFromScene)
        self.twVtxValues.setHeaderHidden(False)
        self.twVtxValues.resizeColumnToContents(0)
        self.twVtxValues.resizeColumnToContents(1)
        self.twVtxValues.itemSelectionChanged.connect(self.on_selectInfluence)

    @property
    def clothNode(self):
        """ Get cloth node name from ui
            :return: Initialized cloth node name
            :rtype: str """
        return self.mainUi.clothNode

    def rf_vtxInfluence(self):
        """ Refresh QTreeWidget 'vertex map influence' """
        self.twVtxValues.clear()
        if self.mainUi.tabVertex.currentIndex() == 1:
            if self.clothNode is not None:
                model = vmCmds.getModelFromClothNode(self.clothNode)
                if model is not None:
                    selItems = self.mainUi.wgVtxType.twMapType.selectedItems()
                    if selItems:
                        if selItems[0]._widget.vtxMapType == 'Vertex':
                            data = vmCmds.getVtxMapData(self.clothNode, selItems[0]._widget.vtxMap)
                            if data is not None:
                                items = []
                                for n, val in enumerate(data):
                                    newItem = self.new_vtxInfluenceItem(model, n, val)
                                    items.append(newItem)
                                self.twVtxValues.addTopLevelItems(items)
                        else:
                            print "!!! Warning: Vertex map disabled !!!"

    def on_updateInfFromScene(self):
        """ Command launched when QPushButton 'Update From Scene' is clicked
            Update vertexMap info QTreeWidgetItem selection from scene """
        selVtx = vmCmds.getModelSelVtx(self.clothNode, indexOnly=True)
        if selVtx:
            allItems = pQt.getAllItems(self.twVtxValues)
            for n, item in enumerate(allItems):
                if n in selVtx:
                    self.twVtxValues.setItemSelected(item, True)
                else:
                    self.twVtxValues.setItemSelected(item, False)

    def on_selectInfluence(self):
        """ Command launched when QTreeWidgetItem selection changed
            Update vertex model selection """
        selItems = self.twVtxValues.selectedItems()
        selVtx = []
        if selItems:
            for item in selItems:
                selVtx.append("%s.vtx[%s]" % (item.model, item.vtxIndex))
        if not selVtx:
            vmCmds.clearVtxSelection()
        else:
            vmCmds.selectVtxOnModel(selVtx)

    @staticmethod
    def new_vtxInfluenceItem(model, n, val):
        """ Create new vtx influence 'QTreeWidgetItem'
            :param n: Vertex index
            :type n: int
            :param val: Influence
            :type val: float
            :return: Vertex Influence item
            :rtype: QtGui.QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        #-- Set label --#
        newItem.setText(0, str(n))
        newItem.setText(1, str(val))
        #-- Store Data --#
        newItem.model = model
        newItem.vtxIndex = n
        newItem.vtxInf = val
        return newItem
