import os
from PyQt4 import QtGui
from lib.qt import procQt as pQt
from tools.maya.cmds import pRigg
from tools.maya.cloth.clothCache import clothCacheCmds as ccCmds
from tools.maya.cloth.clothCache.ui import wgSceneNodesUI, wgSceneNodeUI, wgCacheEvalUI, wgCacheListUI,\
                                           wgCacheInfoUI


class SceneNodeUi(QtGui.QWidget, wgSceneNodesUI.Ui_wgSceneNodes):
    """ Widget SceneNodes, child of mainUi
        :param mainUi: ClothCache mainUi
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
        # self.twSceneNodes.itemClicked.connect(self.on_sceneNodeSingleClick)
        self.twSceneNodes.itemDoubleClicked.connect(self.on_sceneNodeDoubleClick)
        self.cbCloth.clicked.connect(self.on_showClothType)
        self.cbRigid.clicked.connect(self.on_showClothType)
        self.rf_sceneNodes()

    @property
    def itemAttrOrder(self):
        """ Get SceneNodeItem attribute list
            :return: Item attributes
            :rtype: list """
        return ['clothNode', 'clothNs', 'clothName', 'clothType', 'clothParent', 'clothMesh', 'clothShape']

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

    def rf_sceneNodes(self):
        """ Refresh QTreeWidget 'Scene Nodes' """
        self.twSceneNodes.clear()
        #-- Populate Nucleus node --#
        for nucleus in ccCmds.getAllNucleus():
            nucleusItem = self.add_sceneNode(nucleus)
            #-- Populate nCloth Node --#
            dynNodes = pRigg.findTypeInHistory(nucleus, ['nCloth', 'nRigid'], future=True, past=True)
            rigidNodes = []
            for node in dynNodes:
                nodeType = ccCmds.getClothType(node)
                if nodeType is not None:
                    if nodeType == 'nCloth':
                        self.add_sceneNode(node, parent=nucleusItem)
                    #-- Store nRigid Node (tree order) --#
                    elif nodeType == 'nRigid':
                        rigidNodes.append(node)
            #-- Populate nRigid Node --#
            for node in rigidNodes:
                self.add_sceneNode(node, parent=nucleusItem)

    def rf_widgetToolTips(self):
        """ Refresh all widget toolTip """
        if self.mainUi.toolTipState:
            self.cbCloth.setToolTip("Show / Hide nCloth items")
            self.cbRigid.setToolTip("Show / Hide nRigid items")
        else:
            for widget in [self.cbCloth, self.cbRigid]:
                widget.setToolTip("")

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
        self.twSceneNodes.setItemWidget(newItem, 0, newItem._widget)
        return newItem

    def on_sceneNodeSingleClick(self):
        """ Command launched when 'SceneNode' QTreeWidgetItem is single clicked """
        # Todo: Cloth node selection
        pass

    def on_sceneNodeDoubleClick(self):
        """ Command launched when 'SceneNode' QTreeWidgetItem is double clicked """
        selItems = self.twSceneNodes.selectedItems()
        if selItems:
            ccCmds.selectModel(selItems[0].clothNode)

    def on_showClothType(self):
        """ Command launched when QCheckBox 'nCloth' or 'nRigid' is clicked,
            Update QTreeWidget with selected cloth type """
        for item in pQt.getAllItems(self.twSceneNodes):
            if item.clothType == 'nCloth':
                self.twSceneNodes.setItemHidden(item, not self.cbCloth.isChecked())
            elif item.clothType == 'nRigid':
                self.twSceneNodes.setItemHidden(item, not self.cbRigid.isChecked())

    def new_sceneNodeItem(self, clothNode):
        """ Create new 'clothNode' QTreeWidgetItem
            :param clothNode: Cloth Node name
            :type clothNode: str
            :return: Scene node QTreeWidgetItem
            :rtype: QtGui.QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        #-- Add Attributes --#
        ns, name = ccCmds.getNamespace(clothNode)
        newItem.clothNode = clothNode
        newItem.clothNs = ns
        newItem.clothName = name
        newItem.clothType = ccCmds.getClothType(clothNode)
        if newItem.clothType == 'nucleus':
            newItem.clothParent = clothNode
            newItem.clothMesh = None
            newItem.clothShape = None
        else:
            newItem.clothParent = ccCmds.getNodeParent(clothNode)
            newItem.clothMesh = ccCmds.getModelFromClothNode(clothNode)
            newItem.clothShape = ccCmds.getNodeShape(newItem.clothMesh)
        newItem.attrOrder = self.itemAttrOrder
        newItem._widget = SceneNode(self, newItem)
        self.rf_sceneItemToolTip(newItem)
        return newItem


class SceneNode(QtGui.QWidget, wgSceneNodeUI.Ui_wgSceneNode):
    """ Widget SceneNode QTreeWidgetItem, child of SceneNodeUi
        :param pWidget: Parent Widget
        :type pWidget: QtGui.QWidget
        :param pItem: Parent item
        :type pItem: QtGui.QTreeWidgetItem """

    def __init__(self, pWidget, pItem):
        self.pWidget = pWidget
        self.pItem = pItem
        self.mainUi = self.pWidget.mainUi
        super(SceneNode, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        self.rf_label()
        self.rf_nodeTypeIcon()
        self.rf_nodeEnableIcon(rfBtnState=True)
        self.pbEnable.clicked.connect(self.on_stateIcon)

    @property
    def enableState(self):
        """ Get Attr enable state
            :return: Attr enable state
            :rtype: bool """
        return self.pbEnable.isChecked()

    def rf_label(self):
        """ Refresh label text and color """
        newFont = QtGui.QFont()
        newFont.setBold(True)
        color = (self.mainUi.getLabelColor('default'))
        if self.pItem.clothType == 'nucleus':
            newFont.setPointSize(10)
            self.lSceneNode.setText(self.pItem.clothNode)
            color = self.mainUi.getLabelColor('yellow')
        elif self.pItem.clothType == 'nCloth':
            self.lSceneNode.setText(self.pItem.clothMesh)
            color = self.mainUi.getLabelColor('green')
        elif self.pItem.clothType == 'nRigid':
            self.lSceneNode.setText(self.pItem.clothMesh)
            color = self.mainUi.getLabelColor('blue')
        self.lSceneNode.setFont(newFont)
        self.lSceneNode.setStyleSheet("color: rgb(%s, %s, %s)" % (color[0], color[1], color[2]))

    def rf_nodeTypeIcon(self):
        """ Refresh cloth node type icon """
        if self.pItem.clothType == 'nucleus':
            self.pbIcon.setIcon(self.mainUi.nucleusIcon)
        elif self.pItem.clothType == 'nCloth':
            self.pbIcon.setIcon(self.mainUi.nClothIcon)
        elif self.pItem.clothType == 'nRigid':
            self.pbIcon.setIcon(self.mainUi.nRigidIcon)

    def rf_nodeEnableIcon(self, rfBtnState=False):
        """ Refresh state icon
            :param rfBtnState: Enable btn state refresh
            :type rfBtnState: bool """
        if self.pItem.clothType in ['nCloth', 'nRigid']:
            state = ccCmds.getAttr(self.pItem.clothNode, 'isDynamic')
        else:
            state = ccCmds.getAttr(self.pItem.clothNode, 'enable')
        if state:
            stateIcon = self.mainUi.enableIcon
            if rfBtnState:
                self.pbEnable.setChecked(True)
        else:
            stateIcon = self.mainUi.disableIcon
            if rfBtnState:
                self.pbEnable.setChecked(False)
        self.pbEnable.setIcon(stateIcon)

    def on_stateIcon(self):
        """ Command launched when 'pbEnable' QPushButton is clicked,
            Edit enable state (isDynamic state for nCloth and nRigid. """
        if self.pItem.clothType in ['nCloth', 'nRigid']:
            ccCmds.setAttr(self.pItem.clothNode, 'isDynamic', self.enableState)
        else:
            ccCmds.setAttr(self.pItem.clothNode, 'enable', self.enableState)
        self.rf_nodeEnableIcon()


class CacheEvalUi(QtGui.QWidget, wgCacheEvalUI.Ui_wgCacheEval):
    """ Widget CacheEval, child of mainUi
        :param mainUi: ClothCache mainUi
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        print "\t ---> CacheEvalUi"
        self.mainUi = mainUi
        self.evalClothCacheIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'evalClothCache.png'))
        self.appendToCacheIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'appendToCache.png'))
        self.deleteCacheIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'deleteCache.png'))
        self.evalGeoCacheIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'evalGeoCache.png'))
        super(CacheEvalUi, self).__init__()
        self._setupUi()

    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        self.pbClothCache.setIcon(self.evalClothCacheIcon)
        self.pbAppendCache.setIcon(self.appendToCacheIcon)
        self.pbClearCache.setIcon(self.deleteCacheIcon)
        self.pbGeoCache.setIcon(self.evalGeoCacheIcon)

    def rf_widgetToolTips(self):
        """ Refresh all widget toolTip """
        if self.mainUi.toolTipState:
            self.pbClothCache.setToolTip("Create nCloth cache from selected ui cloth item")
            self.pbAppendCache.setToolTip("Append to cache from selected ui cloth item")
            self.pbClearCache.setToolTip("Delete cache node from selected ui cloth item")
            self.pbGeoCache.setToolTip("Create geo cache from selected scene mesh")
        else:
            for widget in [self.pbClothCache, self.pbAppendCache, self.pbClearCache, self.pbGeoCache]:
                widget.setToolTip("")


class CacheListUi(QtGui.QWidget, wgCacheListUI.Ui_wgCacheList):
    """ Widget CacheList, child of mainUi
        :param mainUi: ClothCache mainUi
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        print "\t ---> CacheListUi"
        self.mainUi = mainUi
        super(CacheListUi, self).__init__()
        self._setupUi()

    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)


class CacheInfoUi(QtGui.QWidget, wgCacheInfoUI.Ui_wgCacheInfo):
    """ Widget CacheInfo, child of mainUi
        :param mainUi: ClothCache mainUi
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        print "\t ---> CacheInfoUi"
        self.mainUi = mainUi
        super(CacheInfoUi, self).__init__()
        self._setupUi()

    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)