from PyQt4 import QtGui, Qt
from functools import partial
from lib.qt import procQt as pQt
from tools.maya.util.proc import procUi as pUi
from tools.maya.cloth.vtxMap.ui import vtxMapUI, wgVtxMapUI
from tools.maya.cloth.vtxMap import vtxMapCmds as vmCmds
try:
    import maya.cmds as mc
    import maya.mel as ml
except:
    pass


class VtxMapUi(QtGui.QMainWindow, vtxMapUI.Ui_mwVtxMap):

    def __init__(self, parent=None):
        super(VtxMapUi, self).__init__(parent)
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup main ui """
        self.setupUi(self)
        #-- Init Cloth Node -- #
        self.pbInit.clicked.connect(partial(self.on_init, shapeName=None))
        self.pbSelect.clicked.connect(self.on_selectClothNode)
        #-- Scene Cloth Nodes --#
        self.vfSceneNodes.setVisible(False)
        self.cbSceneNodes.clicked.connect(self.on_sceneNodesVis)
        self.twSceneNodes.itemClicked.connect(self.on_sceneNodes)
        self.cbCloth.clicked.connect(self.on_showClothType)
        self.cbRigid.clicked.connect(self.on_showClothType)
        #-- Vertex Map Type Nodes --#
        self.twMapType.itemClicked.connect(self.on_mapTypeNodes)
        self.twMapType.itemDoubleClicked.connect(self.on_mapTypeEdit)
        self.pbNone.setStyleSheet("color: rgb(175, 175, 175)")
        self.pbNone.clicked.connect(partial(self.on_editAll, 'None'))
        self.pbVertex.setStyleSheet("color: rgb(0, 255, 0)")
        self.pbVertex.clicked.connect(partial(self.on_editAll, 'Vertex'))
        self.pbTexture.setStyleSheet("color: rgb(0, 150, 255)")
        self.pbTexture.clicked.connect(partial(self.on_editAll, 'Texture'))
        #-- Vertex Map Tools --#
        self.pbVtxSelect.clicked.connect(self.on_vtxRangeSel)
        self.pbVtxClear.clicked.connect(self.on_vtxClearSel)
        #-- Vertex Map Influence --#
        self.pbUpdateInf.clicked.connect(self.on_updateInfFromScene)
        self.twVtxValues.setHeaderHidden(False)
        self.twVtxValues.resizeColumnToContents(0)
        self.twVtxValues.resizeColumnToContents(1)
        self.twVtxValues.itemSelectionChanged.connect(self.on_selectInfluence)

    @property
    def clothNode(self):
        """ Get cloth node name from ui
            :return: (str) : Initialized cloth shape node name """
        clothNode = str(self.leInit.text())
        if clothNode in ['', ' ', '  ']:
            return None
        return clothNode

    def rf_nodeType(self):
        """ Refresh QLabel 'Node Type' """
        if self.clothNode is None:
            self.lNodeType.setText("Node Type: ")
        else:
            nodeType = vmCmds.getNodeType(self.clothNode)
            if nodeType is not None:
                self.lNodeType.setText("Node Type: %s" % nodeType)
            else:
                self.lNodeType.setText("Node Type: ")

    def rf_sceneNodes(self, nCloth=True, nRigid=True):
        """ Refresh QTreeWidget 'Scene Nodes' """
        nodes = {}
        types = []
        if nCloth:
            types.append('nCloth')
        if nRigid:
            types.append('nRigid')
        self.twSceneNodes.clear()
        #-- Get All ClothNodes --#
        for clothType in types:
            for node in vmCmds.getAllClothNodes(clothType):
                nodes[node] = clothType
        #-- Populate --#
        items = []
        for k in sorted(nodes.keys()):
            newItem = self.new_clothItem(k, nodes[k])
            items.append(newItem)
        self.twSceneNodes.addTopLevelItems(items)

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
        self.rf_vtxInfluence()

    def rf_vtxInfluence(self):
        """ Refresh QTreeWidget 'vertex map influence' """
        self.twVtxValues.clear()
        if self.tabVertex.currentIndex() == 1:
            if self.clothNode is not None:
                model = vmCmds.getModelFromClothNode(self.clothNode)
                if model is not None:
                    selItems = self.twMapType.selectedItems()
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

    def on_init(self, shapeName=None):
        """ Command launched when QPushButton 'Init' is clicked """
        self.leInit.clear()
        if shapeName is None:
            clothNode, log = vmCmds.getClothNode(returnLog=True)
            if clothNode is None:
                print log
            else:
                self.leInit.setText(clothNode)
        else:
            self.leInit.setText(shapeName)
        self.rf_nodeType()
        self.rf_mapType()

    def on_selectClothNode(self):
        """ Command launched when QPushButton 'Select' is clicked """
        if self.clothNode is None:
            raise ValueError, "!!! WARNING: Empty string, init first !!!"
        vmCmds.selectClothNode(self.clothNode)

    def on_sceneNodesVis(self):
        """ Command launched when QCheckButton 'Scene Nodes' is clicked """
        if self.cbSceneNodes.isChecked():
            self.vfSceneNodes.setVisible(True)
            self.rf_sceneNodes()
        else:
            self.vfSceneNodes.setVisible(False)
            self.twSceneNodes.clear()

    def on_sceneNodes(self):
        """ Command launched when QTreeWidgetItem 'Scene Nodes' is clicked """
        selItems = self.twSceneNodes.selectedItems()
        if selItems:
            self.on_init(shapeName=selItems[0].nodeShape)

    def on_showClothType(self):
        """ Command launched when QCheckButton 'nCloth' or 'nRigid' is clicked """
        self.rf_sceneNodes(nCloth=self.cbCloth.isChecked(), nRigid=self.cbRigid.isChecked())

    def on_mapTypeNodes(self):
        """ Command launched when QTreeWidgetItem 'MapType Nodes' is clicked """
        self.rf_vtxInfluence()

    def on_mapTypeEdit(self):
        """ Command launched when QTreeWidgetItem 'MapType Nodes' is double clicked """
        selItems = self.twMapType.selectedItems()
        if selItems:
            if selItems[0]._widget.vtxMapType == 'Vertex':
                model = vmCmds.getModelFromClothNode(selItems[0]._widget.clothNode)
                mc.select(model, add=True)
                ml.eval('setNClothMapType("%s","",1);' % selItems[0]._widget.mapName)
                ml.eval('artAttrNClothToolScript 3 %s;' % selItems[0]._widget.mapName)

    def on_editAll(self, mapType):
        """ Command launched when QPushButton 'None', 'Vertex' or 'Texture' is clicked """
        vtxMaps = pQt.getAllItems(self.twMapType)
        for item in vtxMaps:
            if mapType == 'None':
                item._widget.cbState.setCurrentIndex(0)
            elif mapType == 'Vertex':
                item._widget.cbState.setCurrentIndex(1)
            elif mapType == 'Texture':
                item._widget.cbState.setCurrentIndex(2)

    def on_vtxRangeSel(self):
        """ Command launched when QPushButton 'Select' (range) is clicked """
        minInf = self.sbRangeMin.value()
        maxInf = self.sbRangeMax.value()
        selItems = self.twMapType.selectedItems()
        if selItems:
            data = vmCmds.getVtxMapData(selItems[0]._widget.clothNode, selItems[0]._widget.vtxMap)
            if data is not None:
                vtxSel = []
                model = vmCmds.getModelFromClothNode(selItems[0]._widget.clothNode)
                if model is not None:
                    for n, val in enumerate(data):
                        if minInf <= val <= maxInf:
                            vtxSel.append("%s.vtx[%s]" % (model, n))
                mc.select(vtxSel, r=True)

    @staticmethod
    def on_vtxClearSel():
        """ Command launched when QPushButton 'Clear' (range) is clicked """
        mc.select(cl=True)

    def on_updateInfFromScene(self):
        """ Command launched when QPushButton 'Update From Scene' is clicked """
        selVtx = vmCmds.getModelSelVtx(self.clothNode, indexOnly=True)
        if selVtx:
            allItems = pQt.getAllItems(self.twVtxValues)
            for n, item in enumerate(allItems):
                if n in selVtx:
                    self.twVtxValues.setItemSelected(item, True)
                else:
                    self.twVtxValues.setItemSelected(item, False)

    def on_selectInfluence(self):
        """ Command launched when QTreeWidgetItem selection changed """
        #-- Get selection from ui --#
        selItems = self.twVtxValues.selectedItems()
        selVtx = []
        if selItems:
            for item in selItems:
                selVtx.append("%s.vtx[%s]" % (item.model, item.vtxIndex))
        #-- Select vertex --#
        if not selVtx:
            mc.select(cl=True)
        else:
            mc.select(selVtx, r=True)

    @staticmethod
    def new_clothItem(clothNode, nodeType):
        """ Create new clothNode 'QTreeWidgetItem'
            :param clothNode: (str) : Cloth node name
            :param nodeType: (str) : 'nCloth' or 'nRigid'
            :return: (object) : QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        #-- Set label --#
        label = vmCmds.getClothNodeParent(clothNode)
        if label is None:
            raise ValueError
        newItem.setText(0, label)
        #-- Set Color --#
        if nodeType == 'nCloth':
            newItem.setTextColor(0, Qt.QColor(0, 255, 0))
        elif nodeType == 'nRigid':
            newItem.setTextColor(0, Qt.QColor(0, 125, 255))
        #-- Store Data --#
        newItem.nodeName = label
        newItem.nodeShape = clothNode
        newItem.nodeType = nodeType
        return newItem

    @staticmethod
    def new_vtxMapItem(clothNode, mapName):
        """ Create new mapType 'QTreeWidgetItem'
            :param clothNode: (str) : Cloth node name
            :param mapName: (str) : Cloth node map type
            :return: (object) : QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem._widget = VtxMapNode(clothNode, mapName)
        return newItem

    @staticmethod
    def new_vtxInfluenceItem(model, n, val):
        """ Create new vtx influence 'QTreeWidgetItem'
            :param n: (int) : Vertex index
            :param val: (float) : Influence
            :return: (object) : QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        #-- Set label --#
        newItem.setText(0, str(n))
        newItem.setText(1, str(val))
        #-- Store Data --#
        newItem.model = model
        newItem.vtxIndex = n
        newItem.vtxInf = val
        return newItem


class VtxMapNode(QtGui.QWidget, wgVtxMapUI.Ui_wgVtxMap):

    def __init__(self, clothNode, mapName):
        self.clothNode = clothNode
        self.mapName = mapName
        self.mapType = "%sMapType" % self.mapName
        self.vtxMap = "%sPerVertex" % self.mapName
        super(VtxMapNode, self).__init__()
        self._setupUi()

    @property
    def vtxMapIndex(self):
        """ Get vtxMap current type
            :return: (int) : VtxMap type (0 = None, 1 = Vertex, 2 = Texture) """
        return self.cbState.currentIndex()

    @property
    def vtxMapType(self):
        """ Get vtxMap current type
            :return: (str) : VtxMap type (None, Vertex or Texture) """
        return str(self.cbState.currentText())

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        self.lVtxMap.setText(self.mapName)
        self.cbState.setCurrentIndex(vmCmds.getVtxMapType(self.clothNode, self.mapType))
        self.cbState.currentIndexChanged.connect(self.on_mapType)
        self.rf_vtxMapLabel()

    def rf_vtxMapLabel(self):
        """ Refresh mapType label color """
        if self.vtxMapIndex == 0:
            self.lVtxMap.setStyleSheet("color: rgb(175, 175, 175)")
        elif self.vtxMapIndex == 1:
            self.lVtxMap.setStyleSheet("color: rgb(0, 255, 0)")
        elif self.vtxMapIndex == 2:
            self.lVtxMap.setStyleSheet("color: rgb(0, 125, 255)")

    def on_mapType(self):
        """ Command launched when QComboBox 'mapType' current index changed """
        vmCmds.setVtxMapType(self.clothNode, self.mapType, self.cbState.currentIndex())
        self.rf_vtxMapLabel()


def launch():
    """ Launch VtxMap
        :return: (object) : Launched window """
    toolName = 'mwVtxMap'
    if mc.window(toolName, q=True, ex=True):
        mc.deleteUI(toolName, wnd=True)
    global window
    window = VtxMapUi(parent=pUi.getMayaMainWindow())
    window.show()
    return window
