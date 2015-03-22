import os
from PyQt4 import QtGui, QtCore, Qt
from functools import partial
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from tools.maya.cloth.vtxMap import vtxMapCmds as vmCmds
from tools.maya.cloth.vtxMap.ui import wgSceneNodesUI, wgVtxTypeUI, wgVtxMapUI, wgVtxEditUI
from tools.maya.cloth.vtxMap.ui import wgVtxInfoUI, wgVtxFileUI

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

    def getParams(self):
        """ Get all vertex map data
            :return: Vertex maps data
            :rtype: dict """
        mapsDict = {}
        allItems = pQt.getAllItems(self.twMapType)
        for item in allItems:
            node = item._widget
            mapsDict[node.mapName] = {'mapType': node.vtxMapIndex}
            if node.vtxMapType == 'Vertex':
                mapsDict[node.mapName]['mapData'] = vmCmds.getVtxMapData(self.clothNode, node.vtxMap)
            else:
                mapsDict[node.mapName]['mapData'] = None
        return mapsDict

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


class VtxFileUi(QtGui.QWidget, wgVtxFileUI.Ui_wgVtxFile):
    """ Widget VtxFile, child of mainUi
        :param mainUi: VertexMap mainUi
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.maps = self.mainUi.wgVtxType
        super(VtxFileUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        self.pbSetImpPath.clicked.connect(partial(self.on_setRootPath, 'load'))
        self.pbSetExpPath.clicked.connect(partial(self.on_setRootPath, 'save'))
        self.pbLoad.clicked.connect(self.on_load)
        self.pbSave.clicked.connect(self.on_save)

    @property
    def clothNode(self):
        """ Get cloth node name from ui
            :return: Initialized cloth node name
            :rtype: str """
        return self.mainUi.clothNode

    def getRootPath(self, fileMode):
        """ Get root path from ui
            :param fileMode: Vertex file mode ('load' or 'save')
            :type fileMode: str
            :return: Root path
            :rtype: str """
        if fileMode == 'load':
            return str(self.leImpRootPath.text())
        elif fileMode == 'save':
            return str(self.leExpRootPath.text())

    def getMode(self, fileMode):
        """ Get load or save mode from ui
            :param fileMode: Vertex file mode ('load' or 'save')
            :type fileMode: str
            :return: Load or save mode ('all' or 'sel')
            :rtype: str """
        if fileMode == 'load':
            state = self.cbImpAll.isChecked()
        else:
            state = self.cbExpAll.isChecked()
        if state:
            return 'all'
        else:
            return 'sel'

    def getPathInfo(self, path, fileMode):
        """ Get path info from given path
            :param path: Absolute path
            :type path: str
            :param fileMode: Vertex file mode ('load' or 'save')
            :type fileMode: str
            :return: Path info
            :rtype: dict """
        #-- Get Path Info --#
        fileAbsPath = path
        filePath = os.path.dirname(fileAbsPath)
        fileName = os.path.basename(fileAbsPath)
        fileExt = os.path.splitext(fileName)[1]
        #-- Check Extension --#
        if not fileExt == '.py':
            fileExt = '.py'
        fileExt = fileExt.replace('.', '')
        fileName = "%s.%s" % (os.path.splitext(fileName)[0], fileExt)
        fileAbsPath = pFile.conformPath(os.path.join(filePath, fileName))
        #-- Check Map File --#
        if not os.path.exists(fileAbsPath):
            mode = 'all'
        else:
            mode = self.getMode(fileMode)
        #-- Result --#
        return {'filePath': filePath, 'fileName': fileName, 'fileExt': fileExt,
                'absPath': fileAbsPath, 'mode': mode}

    def on_setRootPath(self, fileMode):
        """ Command launch when pbSetExpPath is clicked, launch fileDialog
            :param fileMode: Vertex file mode ('load' or 'save')
            :type fileMode: str """
        root = self.getRootPath(fileMode)
        self.fdRootPath = pQt.fileDialog(fdRoot=root, fdCmd=partial(self.ud_rootPath, fileMode))
        self.fdRootPath.setFileMode(QtGui.QFileDialog.DirectoryOnly)
        self.fdRootPath.exec_()

    def on_load(self):
        """ Command launch when pbLoad is clicked, launch fileDialog """
        if self.checkMap():
            root = self.getRootPath('load')
            self.fdLoadMap = pQt.fileDialog(fdMode='load', fdRoot=root, fdCmd=self.loadMap, fdFilters=['*.py'])
            self.fdLoadMap.setFileMode(QtGui.QFileDialog.AnyFile)
            self.fdLoadMap.exec_()

    def on_save(self):
        """ Command launch when pbSave is clicked, launch fileDialog """
        if self.checkMap():
            root = self.getRootPath('save')
            self.fdSaveMap = pQt.fileDialog(fdMode='save', fdRoot=root,
                                            fdCmd=self.saveMap, fdFilters=['*.py'])
            self.fdSaveMap.setFileMode(QtGui.QFileDialog.AnyFile)
            self.fdSaveMap.exec_()

    def ud_rootPath(self, fileMode):
        """ Update root path
            :param fileMode: Vertex file mode ('load' or 'save')
            :type fileMode: str """
        selPath = self.fdRootPath.selectedFiles()
        if selPath:
            if fileMode == 'load':
                self.leImpRootPath.setText(str(selPath[0]))
            elif fileMode == 'save':
                self.leExpRootPath.setText(str(selPath[0]))

    def checkMap(self):
        """ Check map before load or save
            :return: Check result
            :rtype: bool """
        check = True
        if self.clothNode is None:
            print "!!! VTX MAP: No cloth node selected !!!"
            check = False
        else:
            if self.getMode('save') == 'sel':
                selItems = self.maps.twMapType.selectedItems()
                if not selItems:
                    print "!!! VTX MAP: No vertex map selected !!!"
                    check = False
        return check

    def loadMap(self):
        """ Load vertex map file """
        selPath = self.fdLoadMap.selectedFiles()
        if selPath:
            pathInfo = self.getPathInfo(str(selPath[0]), 'load')
            params = pFile.readPyFile(pathInfo['absPath'])
            #-- Load All Vertex Maps --#
            if pathInfo['mode'] == 'all':
                for mapName in params.keys():
                    mapType = params[mapName]['mapType']
                    vmCmds.setVtxMapType(self.clothNode, "%sMapType" % mapName, mapType)
                    if mapType == 1:
                        vmCmds.setVtxMapData(self.clothNode, "%sPerVertex" % mapName, params[mapName]['mapData'])
            #-- Load Selected Vertex Map --#
            else:
                selItems = self.maps.twMapType.selectedItems()
                if selItems:
                    node = selItems[0]._widget
                    vmCmds.setVtxMapType(self.clothNode, node.mapType, params[node.mapName]['mapType'])
                    if params[node.mapName]['mapType'] == 1:
                        vmCmds.setVtxMapData(self.clothNode, node.vtxMap, params[node.mapName]['mapData'])
            self.maps.rf_mapType()

    def saveMap(self):
        """ Save vertex map file """
        selPath = self.fdSaveMap.selectedFiles()
        if selPath:
            pathInfo = self.getPathInfo(str(selPath[0]), 'save')
            #-- Save All Vertex Maps --#
            if pathInfo['mode'] == 'all':
                mapsDict = self.maps.getParams()
                txt = []
                for k in sorted(mapsDict.keys()):
                    txt.append("%s = %s" % (str(k), mapsDict[k]))
            #-- Save Selected Vertex Map --#
            else:
                #-- Get Vertex File Params --#
                params = pFile.readPyFile(pathInfo['absPath'])
                selItems = self.maps.twMapType.selectedItems()
                if selItems:
                    mapsDict = self.maps.getParams()
                    node = selItems[0]._widget
                    params[node.mapName] = mapsDict[node.mapName]
                #-- Params To String --#
                txt = []
                for k in sorted(params.keys()):
                    txt.append("%s = %s" % (str(k), params[k]))
            #-- Write File --#
            try:
                print "#-- Save Vertex Maps --#"
                pFile.writeFile(pathInfo['absPath'], '\n'.join(txt))
                print "ClothMesh: ", vmCmds.getModelFromClothNode(self.clothNode)
                print "ClothNode: ", self.clothNode
                print "FilePath: ", pathInfo['filePath']
                print "FileName: ", pathInfo['fileName']
                print "FullPath: ", pathInfo['absPath']
                print "Mode: ", pathInfo['mode']
            except:
                print "!!! VTX MAP: Can not write file %s !!!" % pathInfo['absPath']
