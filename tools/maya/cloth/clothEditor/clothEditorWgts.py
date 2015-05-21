import os
from functools import partial
from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from tools.maya.cmds import pRigg
from lib.system import procFile as pFile
from tools.maya.cloth.clothEditor import clothEditorCmds as ceCmds
from tools.maya.cloth.clothEditor.ui import wgSceneNodesUI, wgSceneNodeUI, wgAttrUI, wgAttrNodeUI, wgVtxMapUI,\
                                            wgVtxMapNodeUI, wgFilesUI, dialSaveFileUI


class SceneNodeUi(QtGui.QWidget, wgSceneNodesUI.Ui_wgSceneNodes):
    """ Widget SceneNodes, child of mainUi
        :param mainUi: ClothEditor mainUi
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
        self.twSceneNodes.itemClicked.connect(self.on_sceneNodeSingleClick)
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

    def rf_widgetToolTips(self):
        """ Refresh all widget toolTip """
        if self.mainUi.toolTipState:
            self.cbCloth.setToolTip("Show / Hide nCloth items")
            self.cbRigid.setToolTip("Show / Hide nRigid items")
        else:
            for widget in [self.pbRefresh, self.cbCloth, self.cbRigid]:
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
        if self.mainUi.currentTab == 'Attrs':
            self.mainUi.wgAttributes.rf_attrTree()
        elif self.mainUi.currentTab == 'VtxMap':
            self.mainUi.wgVtxMaps.rf_vtxMapTree()

    def on_sceneNodeDoubleClick(self):
        """ Command launched when 'SceneNode' QTreeWidgetItem is double clicked """
        selItems = self.twSceneNodes.selectedItems()
        if selItems:
            ceCmds.selectModel(selItems[0].clothNode)

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
        newItem._widget = SceneNode(self, newItem)
        self.rf_sceneItemToolTip(newItem)
        return newItem


class SceneNode(QtGui.QWidget, wgSceneNodeUI.Ui_wgSceneNode):
    """ Widget SceneNode QTreeWidgetItem node, child of SceneNodeUi
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
            state = ceCmds.getAttr(self.pItem.clothNode, 'isDynamic')
        else:
            state = ceCmds.getAttr(self.pItem.clothNode, 'enable')
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
            ceCmds.setAttr(self.pItem.clothNode, 'isDynamic', self.enableState)
        else:
            ceCmds.setAttr(self.pItem.clothNode, 'enable', self.enableState)
        self.rf_nodeEnableIcon()


class AttrUi(QtGui.QWidget, wgAttrUI.Ui_wgPreset):
    """ Widget VertxMap, child of mainUi
        :param mainUi: ClothEditor MainUi
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        print "\t ---> PresetUi"
        self.mainUi = mainUi
        self.sceneUi = self.mainUi.wgSceneNodes
        super(AttrUi, self).__init__()
        self._setupUi()
        self.rf_attrTree()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        #-- Preset storage --#
        for n in range(5):
            newButton = AttrStorageButton('Attr_%s' % (n+1), self.mainUi, self)
            self.hlAttrStorage.addWidget(newButton)

    @property
    def nodePreset(self):
        """ Get node preset
            :return: Preset
            :rtype: dict """
        preset = {}
        detectedType = False
        for item in pQt.getAllItems(self.twPreset):
            if item.itemType == 'attr':
                if not detectedType:
                    preset['_clothType'] = str(ceCmds.getClothType(item.clothNode))
                    detectedType = True
                preset[item.clothAttr] = {'type': item.attrType, 'val': item._widget.attrValue}
        return preset

    def rf_attrTree(self):
        """ Refresh attribute tree """
        self.twPreset.clear()
        clothItem = self.sceneUi.selectedClothItem
        if clothItem is not None:
            clothNode = clothItem.clothNode
            clothDict = ceCmds.defaultAttrs(clothItem.clothType)
            #-- Add Top Level Item --#
            for n in sorted(clothDict.keys()):
                grpName = clothDict[n].keys()[0]
                newGrpItem = self.new_presetItem('group', grpName, None, None)
                self.twPreset.addTopLevelItem(newGrpItem)
                self.twPreset.setItemWidget(newGrpItem, 0, newGrpItem._widget)
                newGrpItem.setExpanded(True)
                #-- Add Children --#
                for attr in clothDict[n][grpName]:
                    attrType = ceCmds.getAttrType(clothNode, attr)
                    newAttrItem = self.new_presetItem('attr', clothNode, attr, attrType)
                    newGrpItem.addChild(newAttrItem)
                    self.twPreset.setItemWidget(newAttrItem, 0, newAttrItem._widget)

    def rf_widgetToolTips(self):
        """ Refresh all widget toolTip """
        if self.mainUi.toolTipState:
            self.lAttrStorage.setToolTip("Store selected preset")
        else:
            for widget in [self.lAttrStorage]:
                widget.setToolTip("")

    def new_presetItem(self, itemType, clothNode, clothAttr, attrType):
        """ Create attributes tree new QTreeWidgetItem
            :param itemType: New tree item type ('group', 'attr')
            :type itemType: str
            :param clothNode: Cloth node name
            :type clothNode: str
            :param clothAttr: Attribute long name
            :type clothAttr: str | None
            :param attrType: Attribute type
            :type attrType: str | None
            :return: New attr tree item
            :rtype: QtGui.QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem.itemType = itemType
        newItem.clothNode = clothNode
        newItem.clothAttr = clothAttr
        newItem.attrType = attrType
        newItem._widget = AttrNode(self, newItem)
        return newItem


class AttrNode(QtGui.QWidget, wgAttrNodeUI.Ui_wgPresetNode):
    """ Widget Preset QTreeWidgetItem node, child of PresetUi
        :param pWidget: Parent Widget
        :type pWidget: QtGui.QWidget
        :param pItem: Parent item
        :type pItem: QtGui.QTreeWidgetItem """

    def __init__(self, pWidget, pItem):
        self.pWidget = pWidget
        self.pItem = pItem
        self.mainUi = self.pWidget.mainUi
        super(AttrNode, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        if self.pItem.itemType == 'group':
            self.lGroup.setText(self.pItem.clothNode)
            self.qfValue.setVisible(False)
        else:
            self.lPreset.setText(self.pItem.clothAttr)
            self.lGroup.setVisible(False)
            self._initWidget()
        self.rf_attrLock(rfBtnState=True)
        self.pbLock.clicked.connect(self.on_attrLock)

    def _initWidget(self):
        """ Init attrWidget """
        if self.pItem.attrType in ['long', 'float', 'floatAngle']:
            self._attrWdgt = self.new_lineEdit(self.pItem.attrType)
            self.hlValue.insertWidget(0, self._attrWdgt)
            self.hfValue.setMaximumWidth(70)
        elif self.pItem.attrType == 'bool':
            self._attrWdgt = self.new_checkBox()
            self.hlValue.insertWidget(0, self._attrWdgt)
            self.hfValue.setMinimumWidth(14)
            self.hfValue.setMaximumWidth(14)
        elif self.pItem.attrType == 'enum':
            self._attrWdgt = self.new_comboBox()
            self.hlValue.insertWidget(0, self._attrWdgt)
            self.hfValue.setMaximumWidth(100)
        elif self.pItem.attrType == 'float3':
            self._attrWdgtX = self.new_lineEdit('tripleX')
            self._attrWdgtY = self.new_lineEdit('tripleY')
            self._attrWdgtZ = self.new_lineEdit('tripleZ')
            self.hlValue.insertWidget(0, self._attrWdgtX)
            self.hlValue.insertWidget(1, self._attrWdgtY)
            self.hlValue.insertWidget(2, self._attrWdgtZ)
            self.hfValue.setMaximumWidth(210)

    @property
    def attrValue(self):
        """ Get itemNode value
            :return: Item node value
            :rtype: int | float | tuple """
        if self.pItem.attrType == 'bool':
            val = self._attrWdgt.isChecked()
        elif self.pItem.attrType == 'enum':
            if self.pItem.clothAttr in ceCmds.enumFilter():
                val = int(self._attrWdgt.currentIndex())
            else:
                val = int(self._attrWdgt.currentIndex() + 1)
        elif self.pItem.attrType in ['float', 'floatAngle']:
            val = float(self._attrWdgt.text())
        elif self.pItem.attrType == 'long':
            val = int(self._attrWdgt.text())
        elif self.pItem.attrType == 'float3':
            val = (float(self._attrWdgtX.text()), float(self._attrWdgtY.text()), float(self._attrWdgtZ.text()))
        else:
            val = None
        return val

    @property
    def attrLock(self):
        """ Get Attr lock state
            :return: Attr lock state
            :rtype: bool """
        return self.pbLock.isChecked()

    def setValue(self, val):
        """ Set attribute widget value
            :param val: Attr value
            :type val: float | int | str | tuple """
        if self.pItem.attrType == 'bool':
            self._attrWdgt.setChecked(val)
        elif self.pItem.attrType == 'enum':
            if self.pItem.clothAttr in ceCmds.enumFilter():
                self._attrWdgt.setCurrentIndex(val)
            else:
                self._attrWdgt.setCurrentIndex(val - 1)
        elif self.pItem.attrType in ['float', 'floatAngle', 'long']:
            self._attrWdgt.setText(str(val))
        elif self.pItem.attrType == 'float3':
            self._attrWdgtX.setText(str(val[0]))
            self._attrWdgtY.setText(str(val[1]))
            self._attrWdgtZ.setText(str(val[2]))
        self.on_attr()

    # noinspection PyUnresolvedReferences
    def rf_attrLock(self, rfBtnState=False):
        """ Refresh attribute lock icon
            :param rfBtnState: Enable lock btn state refresh
            :type rfBtnState: bool """
        if self.pItem.itemType == 'attr':
            lockAttr = ceCmds.attrIsLocked("%s.%s" % (self.pItem.clothNode, self.pItem.clothAttr))
            if lockAttr:
                lockIcon = self.mainUi.lockIconOn
                if rfBtnState:
                    self.pbLock.setChecked(True)
            else:
                lockIcon = self.mainUi.lockIconOff
                if rfBtnState:
                    self.pbLock.setChecked(False)
            self.pbLock.setIcon(lockIcon)
            self.hfValue.setEnabled(not lockAttr)

    def on_attr(self):
        """ Command launched when 'ItemNode' QWidget is clicked, Set clothNode attribute """
        if self.attrValue is not None:
            ceCmds.setAttr(self.pItem.clothNode, self.pItem.clothAttr, self.attrValue)
        else:
            print "!!! WARNING: Can not find item node value !!!"

    def on_attrLock(self):
        """ Command launched when 'Lock' QPushButton is clicked
            Set clothNode attribute losk state """
        ceCmds.setAttrLock("%s.%s" % (self.pItem.clothNode, self.pItem.clothAttr), self.attrLock)
        self.rf_attrLock()

    # noinspection PyUnresolvedReferences
    def new_lineEdit(self, attrType):
        """ Create new QLineEdit attr
            :param attrType: Attribute type ('long', 'float', 'floatAngle', 'tripleX', 'tripleY', 'tripleZ')
            :type attrType: str
            :return: Line edit attr
            :rtype: QtGui.QLineEdit """
        newWidget = QtGui.QLineEdit()
        if attrType == 'long':
            newWidget.setText(str(ceCmds.getAttr(self.pItem.clothNode, self.pItem.clothAttr)))
        if attrType in ['float', 'floatAngle', 'tripleX', 'tripleY', 'tripleZ']:
            val = self.floatVal(attrType)
            newWidget.setText(val)
        newWidget.editingFinished.connect(self.on_attr)
        return newWidget

    def floatVal(self, attrType, decimal=4):
        """ Conform float value with given decimal
            :param attrType: attrType: Attribute type ('long', 'float', 'floatAngle', 'tripleX', 'tripleY', 'tripleZ')
            :type attrType: str
            :param decimal: Decimal num
            :type decimal: int
            :return: Conformed value
            :rtype: str """
        val = ceCmds.getAttr(self.pItem.clothNode, self.pItem.clothAttr)
        if attrType == 'tripleX':
            newVal = "%s.%s" % (str(val[0][0]).split('.')[0], str(val[0][0]).split('.')[-1][0:decimal])
        elif attrType == 'tripleY':
            newVal = "%s.%s" % (str(val[0][1]).split('.')[0], str(val[0][1]).split('.')[-1][0:decimal])
        elif attrType == 'tripleZ':
            newVal = "%s.%s" % (str(val[0][2]).split('.')[0], str(val[0][2]).split('.')[-1][0:decimal])
        else:
            newVal = "%s.%s" % (str(val).split('.')[0], str(val).split('.')[-1][0:decimal])
        return newVal

    # noinspection PyUnresolvedReferences
    def new_checkBox(self):
        """ Create new QCheckBox attr
            :return: Check box attr
            :rtype: QtGui.QCheckBox """
        newWidget = QtGui.QCheckBox()
        newWidget.setText("")
        newWidget.setChecked(ceCmds.getAttr(self.pItem.clothNode, self.pItem.clothAttr))
        newWidget.setStyleSheet("background-color: rgb(125, 125, 125)")
        newWidget.stateChanged.connect(self.on_attr)
        return newWidget

    # noinspection PyUnresolvedReferences
    def new_comboBox(self):
        """ Create new QComboBox attr
            :return: Combo box attr
            :rtype: QtGui.QComboBox """
        newWidget = QtGui.QComboBox()
        newWidget.addItems(ceCmds.enumAttrs()[self.pItem.clothAttr])
        if self.pItem.clothAttr in ceCmds.enumFilter():
            newWidget.setCurrentIndex(ceCmds.getAttr(self.pItem.clothNode, self.pItem.clothAttr))
        else:
            newWidget.setCurrentIndex(ceCmds.getAttr(self.pItem.clothNode, self.pItem.clothAttr) - 1)
        newWidget.currentIndexChanged.connect(self.on_attr)
        return newWidget


class AttrStorageButton(QtGui.QPushButton):
    """ Widget vertex storage QPushButton, child of vtxMapUi
        :param btnLabel: Button label
        :type btnLabel: str
        :param mainUi: ClothEditor MainUi
        :type mainUi: QtGui.QMainWindow
        :param pWidget: Parent widget
        :type pWidget: QtGui.QWidget """

    def __init__(self, btnLabel, mainUi, pWidget):
        self.btnLabel = btnLabel
        self.mainUi = mainUi
        self.pWidget = pWidget
        self.storage = {}
        super(AttrStorageButton,self).__init__()
        self._setupUi()

    def _setupUi(self):
        """ Setup widget ui """
        self.setText(self.btnLabel)
        self.setToolTip("Empty")
        self.setMaximumHeight(20)

    def popupMenuItems(self):
        """ get menuDict
            :return: Menu data
            :rtype: dict """
        menuDict = {0: ['Edit ToolTip', self.on_editToolTip],
                    1: ['Store Selected Preset', self.on_storePreset],
                    2: ['Clear Preset Storage', self.on_clearStorage]}
        return menuDict

    def mousePressEvent(self, event):
        """ Detect left or right click on QPushButton
            :param event: event
            :type event: QtGui.QEvent """
        if event.button() == QtCore.Qt.LeftButton:
            self.on_leftClick()
        elif event.button() == QtCore.Qt.RightButton:
            self.on_rightClick()

    def on_leftClick(self):
        """ Command launched when QPushButton is left clicked, Restore stored preset """
        if self.storage:
            #-- Cloth Type --#
            clothType = None
            for item in pQt.getAllItems(self.pWidget.twPreset):
                if item.itemType == 'attr':
                    clothType = ceCmds.getClothType(item.clothNode)
                    break
            if not clothType == self.storage['_clothType']:
                raise TypeError, "!!! Cloth type doesn't match, should be %s !!!" % self.storage['_clothType']
            #-- Set Values --#
            for item in pQt.getAllItems(self.pWidget.twPreset):
                if item.itemType == 'attr':
                    if not item._widget.attrLock:
                        item._widget.setValue(self.storage[item.clothAttr]['val'])

    def on_rightClick(self):
        """ Command launched when QPushButton is right clicked, launch popupMenu """
        self.pmMenu = pQt.popupMenu(self.popupMenuItems())
        #-- Refresh Menu Items Visibility --#
        if not self.storage.keys():
            self.pmMenu.items[0].setEnabled(False)
            self.pmMenu.items[2].setEnabled(False)
        else:
            self.pmMenu.items[1].setEnabled(False)
        #-- Pop Menu --#
        self.pmMenu.exec_()

    def on_editToolTip(self):
        """ Command launched when QAction 'Edit ToolTip' is clicked, Launch promp dialog """
        self.dialToolTip = pQt.PromptDialog("Edit ToolTip", self._dialToolTipAccept)
        self.dialToolTip.exec_()

    def _dialToolTipAccept(self):
        """ Command launched when QDialog 'dialToolTip' is accepted, edit button toolTip """
        self.setToolTip(self.dialToolTip.result()['result_1'])
        self.dialToolTip.close()

    def on_storePreset(self):
        """ Command launched when QAction 'Store Selected Preset' is clicked,
            Store selected preset in 'storage' """
        self.storage = self.pWidget.nodePreset
        self.setToolTip("Used")
        print "// Preset storage: %s : Success !" % self.btnLabel

    def on_clearStorage(self):
        """ Command launched when QAction 'Clear ... Storage' is clicked """
        self.storage = {}
        self.setToolTip("Empty")


class VtxMapUi(QtGui.QWidget, wgVtxMapUI.Ui_wgVtxMap):
    """ Widget VertxMap, child of mainUi
        :param mainUi: ClothEditor mainUi
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        print "\t ---> VtxMapUi"
        self.mainUi = mainUi
        self.sceneUi = self.mainUi.wgSceneNodes
        super(VtxMapUi, self).__init__()
        self._setupUi()
        self.rf_rampOptionsVisibility()
        self.rf_vtxMapTree()
        self.rf_floodIterVisibility()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        #-- VtxMap tree --#
        self.cbArtisan.clicked.connect(self.rf_rampOptionsVisibility)
        self.cbVtxColor.clicked.connect(self.rf_rampOptionsVisibility)
        self.pbExit.clicked.connect(self.on_vtxColorExit)
        self.twMaps.itemClicked.connect(self.on_vtxMapNodeSingleClick)
        self.twMaps.itemDoubleClicked.connect(self.on_vtxMapNodeDoubleClick)
        #-- VtxMap global edition --#
        color = self.mainUi.getLabelColor('lightGrey')
        self.pbNone.setStyleSheet("color: rgb(%s, %s, %s)" % (color[0], color[1], color[2]))
        self.pbNone.clicked.connect(partial(self.on_editAll, 'None'))
        color = self.mainUi.getLabelColor('green')
        self.pbVertex.setStyleSheet("color: rgb(%s, %s, %s)" % (color[0], color[1], color[2]))
        self.pbVertex.clicked.connect(partial(self.on_editAll, 'Vertex'))
        color = self.mainUi.getLabelColor('blue')
        self.pbTexture.setStyleSheet("color: rgb(%s, %s, %s)" % (color[0], color[1], color[2]))
        self.pbTexture.clicked.connect(partial(self.on_editAll, 'Texture'))
        #-- VtxMap selection --#
        self.rbVtxRange.clicked.connect(self.rf_vtxSelMode)
        self.rbVtxValue.clicked.connect(self.rf_vtxSelMode)
        self.pbVtxClear.clicked.connect(self.on_vtxClear)
        self.pbVtxSelect.clicked.connect(self.on_vtxSelection)
        #-- VtxMap flood --#
        self.rbEditReplace.clicked.connect(self.rf_floodIterVisibility)
        self.rbEditAdd.clicked.connect(self.rf_floodIterVisibility)
        self.rbEditMult.clicked.connect(self.rf_floodIterVisibility)
        self.rbEditSmooth.clicked.connect(self.rf_floodIterVisibility)
        self.pbFlood.clicked.connect(self.on_flood)
        #-- VtxMap storage --#
        for n in range(5):
            newButton = VtxStorageButton('Set_%s' % (n+1), 'vtxSet', self.mainUi, self)
            self.hlVtxStorage.addWidget(newButton)
        for n in range(5):
            newButton = VtxStorageButton('Data_%s' % (n+1), 'vtxData', self.mainUi, self)
            self.hlDataStorage.addWidget(newButton)
        #-- VtxMap info --#
        self.pbUpdateInf.clicked.connect(self.on_updateVtxInfo)
        self.twVtxValues.setHeaderHidden(False)
        self.twVtxValues.resizeColumnToContents(0)
        self.twVtxValues.resizeColumnToContents(1)
        self.twVtxValues.itemSelectionChanged.connect(self.on_vtxMapInfo)

    @property
    def paintMode(self):
        """ Get vertex paint mode
            :return: Vertex paint mode ('artisan' or 'vtxColor')
            :rtype: str """
        if self.cbArtisan.isChecked():
            return 'artisan'
        elif self.cbVtxColor.isChecked():
            return 'vtxColor'

    @property
    def rampStyle(self):
        """ Get ramp style
            :return: 'grey' or 'color'
            :rtype: str """
        if self.cbGreyRamp.isChecked():
            return 'grey'
        elif self.cbColorRamp.isChecked():
            return 'color'

    @property
    def selectedVtxMapItem(self):
        """ Get selected vertexMap item
            :return: Selected vertexMap item
            :rtype: QtGui.QTreeWidgetItem """
        selItems = self.twMaps.selectedItems()
        if selItems:
            return selItems[0]

    def nodeVtxData(self):
        """ Get all vertex map data
            :return: Vertex maps data
            :rtype: dict """
        mapsDict = {}
        detectedType = False
        for item in pQt.getAllItems(self.twMaps):
            node = item._widget
            if not detectedType:
                mapsDict['_clothType'] = str(ceCmds.getClothType(node.clothNode))
                detectedType = True
            mapsDict[node.mapName] = {'mapType': node.vtxMapIndex}
            if node.vtxMapType == 'Vertex':
                mapsDict[node.mapName]['mapData'] = ceCmds.getVtxMapData(node.clothNode, node.mapVtx)
            else:
                mapsDict[node.mapName]['mapData'] = None
        return mapsDict

    @property
    def floodMode(self):
        """ Get flood mode
            :return: 'replace', 'add', 'mult' or smooth
            :rtype: str """
        if self.rbEditReplace.isChecked():
            return 'replace'
        elif self.rbEditAdd.isChecked():
            return 'add'
        elif self.rbEditMult.isChecked():
            return 'mult'
        elif self.rbEditSmooth.isChecked():
            return 'smooth'

    @property
    def floodValue(self):
        """ Get flood vertex value
            :return: Edition value
            :rtype: float """
        return float(self.leEditVal.text())

    @property
    def floodIter(self):
        """ Get flood iter value
            :return: Flood itertions
            :rtype: int """
        return int(self.sbFloodIter.value())

    @property
    def vtxClamp(self):
        """ Get clamp min and max state and value
            :return: Minimum clamp value (None if disable), Maximum clamp value (None if disable)
            :rtype: (float, float) """
        clampMin = None
        clampMax = None
        if self.cbClampMin.isChecked():
            clampMin = float(self.leClampMin.text())
        if self.cbClampMax.isChecked():
            clampMax = float(self.leClampMax.text())
        return clampMin, clampMax

    def rf_rampOptionsVisibility(self):
        """ Refresh vertex color ramp options visibility """
        if self.paintMode == 'vtxColor':
            self.hfColorRamp.setVisible(True)
        else:
            self.hfColorRamp.setVisible(False)

    def rf_vtxMapTree(self):
        """ Refresh 'Vertex Map' QTreeWidget """
        self.twMaps.clear()
        self.pbFlood.setEnabled(True)
        clothItem = self.sceneUi.selectedClothItem
        if clothItem is not None:
            if not clothItem.clothType == 'nucleus':
                vtxMaps = ceCmds.getVtxMaps(clothItem.clothNode)
                for mapName in vtxMaps:
                    newItem = self.new_vtxMapItem(clothItem.clothNode, mapName)
                    self.twMaps.addTopLevelItem(newItem)
                    self.twMaps.setItemWidget(newItem, 0, newItem._widget)

    def rf_vtxSelMode(self):
        """ Refresh 'Vertex Selection Mode' """
        if self.rbVtxRange.isChecked():
            self.lRangeMin.setText("Min=")
            self.lRangeMax.setVisible(True)
            self.leRangeMax.setVisible(True)
        else:
            self.lRangeMin.setText("Value=")
            self.lRangeMax.setVisible(False)
            self.leRangeMax.setVisible(False)

    def rf_floodIterVisibility(self):
        """ Refresh flood iter visibility """
        if self.floodMode == 'smooth':
            self.sbFloodIter.setEnabled(True)
        else:
            self.sbFloodIter.setEnabled(False)

    def rf_vtxInfluence(self):
        """ Refresh QTreeWidget 'vertex map influence' """
        self.twVtxValues.clear()
        if self.tabVertex.currentIndex() == 1:
            item = self.selectedVtxMapItem
            if item is not None:
                clothNode = item._widget.clothNode
                model = ceCmds.getModelFromClothNode(clothNode)
                if model is not None:
                    if item._widget.vtxMapType == 'Vertex':
                        data = ceCmds.getVtxMapData(clothNode, item._widget.mapVtx)
                        if data is not None:
                            items = []
                            for n, val in enumerate(data):
                                newItem = self.new_vtxInfluenceItem(model, n, val)
                                items.append(newItem)
                            self.twVtxValues.addTopLevelItems(items)
                    else:
                        print "!!! Warning: Vertex map disabled !!!"

    def rf_widgetToolTips(self):
        """ Refresh all widget toolTip """
        if self.mainUi.toolTipState:
            self.cbArtisan.setToolTip("Use 'Maya Artisan' for vertexMap display")
            self.cbVtxColor.setToolTip("Use 'Maya VertexColor' for vertexMap display")
            self.pbNone.setToolTip("Switch all unlocked vtxMap type to 'None'")
            self.pbVertex.setToolTip("Switch all unlocked vtxMap type to 'Vertex'")
            self.pbTexture.setToolTip("Switch all unlocked vtxMap type to 'Texture'")
            self.rbVtxRange.setToolTip("Use min and max value for vertex selction")
            self.rbVtxValue.setToolTip("Use single value for vertex selction")
            self.pbVtxSelect.setToolTip("Select matching vertex influence")
            self.pbVtxClear.setToolTip("Clear scene selection")
            self.rbEditReplace.setToolTip("Replace selected vtxMap influence with 'Vertex Value'")
            self.rbEditAdd.setToolTip("Add 'Vertex Value' to selected vtxMap influence")
            self.rbEditMult.setToolTip("Multiply 'Vertex Value' to selected vtxMap influence")
            self.rbEditSmooth.setToolTip("Smooth selected vtxMap influence")
            self.cbClampMin.setToolTip("Enable / Disable flood min clamp")
            self.cbClampMax.setToolTip("Enable / Disable flood max clamp")
            self.leClampMin.setToolTip("flood min clamp value")
            self.leClampMax.setToolTip("flood max clamp value")
            self.pbFlood.setToolTip("Flood selected vtxMap influence")
            self.sbFloodIter.setToolTip("Flood iteration (max=25),\nOnly available in 'Smooth' mode")
            self.lVtxStorage.setToolTip("Store selected vertex")
            self.lDataStorage.setToolTip("Store selected vertex data")
            self.pbUpdateInf.setToolTip("Update selection from current scene")
        else:
            for widget in [self.cbArtisan, self.cbVtxColor, self.pbNone, self.pbVertex, self.pbTexture,
                           self.rbVtxRange, self.rbVtxValue, self.pbVtxSelect, self.pbVtxClear, self.rbEditReplace,
                           self.rbEditAdd, self.rbEditMult, self.rbEditSmooth, self.cbClampMin, self.cbClampMax,
                           self.leClampMin, self.leClampMax, self.pbFlood, self.sbFloodIter, self.lVtxStorage,
                           self.lDataStorage, self.pbUpdateInf]:
                widget.setToolTip("")

    def on_vtxColorExit(self):
        """ Command launched when 'Exit' QPushButton is clicked """
        clothNode = self.sceneUi.selectedClothNode
        if clothNode is not None:
            ceCmds.exitVtxColor(clothNode)

    def on_vtxMapNodeSingleClick(self):
        """ Command launched when 'VtxMap Node' QTreeWidgetItem is single clicked """
        item = self.selectedVtxMapItem
        if item is not None:
            if item._widget.vtxMapLock:
                self.pbFlood.setEnabled(False)
            else:
                self.pbFlood.setEnabled(True)
        else:
            self.pbFlood.setEnabled(True)
        self.rf_vtxInfluence()

    def on_vtxMapNodeDoubleClick(self):
        """ Command launched when 'VtxMap Node' QTreeWidgetItem is double clicked """
        item = self.selectedVtxMapItem
        if item is not None:
            if not item._widget.vtxMapLock:
                ceCmds.paintVtxMap(self.paintMode, item._widget.clothNode, item._widget.mapName,
                                   rampStyle=self.rampStyle)
            else:
                print "!!! Warning: Can not switch to vertex paint view on locked vertex map !!!"

    def on_editAll(self, mapType):
        """ Command launched when QPushButton 'None', 'Vertex' or 'Texture' is clicked,
            Set all items to given vertexMap type, update clothNode
            :param mapType: Vertex map type ('None', 'Vertex', 'Texture')
            :type mapType: str """
        vtxMaps = pQt.getAllItems(self.twMaps)
        for item in vtxMaps:
            if not item._widget.vtxMapLock:
                if mapType == 'None':
                    item._widget.cbState.setCurrentIndex(0)
                elif mapType == 'Vertex':
                    item._widget.cbState.setCurrentIndex(1)
                elif mapType == 'Texture':
                    item._widget.cbState.setCurrentIndex(2)

    def on_vtxSelection(self):
        """ Command launched when QPushButton 'Select' is clicked,
            Select vertex which vtxMap value match with range edition """
        item = self.selectedVtxMapItem
        if item is not None:
            if self.rbVtxRange.isChecked():
                ceCmds.selectVtxInfluence(item._widget.clothNode, item._widget.mapVtx, 'range',
                                          minInf=float(self.leRangeMin.text()), maxInf=float(self.leRangeMax.text()))
            elif self.rbVtxValue.isChecked():
                ceCmds.selectVtxInfluence(item._widget.clothNode, item._widget.mapVtx, 'value',
                                          value=float(self.leRangeMin.text()))

    @staticmethod
    def on_vtxClear():
        """ Command launched when QPushButton 'Clear' (range) is clicked,
            Clear scene selection """
        ceCmds.clearVtxSelection()

    def on_flood(self):
        """ Command launched when QPushButton 'Flood' is clicked,
            Edit selected vertex map influence with new edited influence """
        #-- Get Vertex Data Info --#
        print "#-- Flood Value --#"
        print "Flood Mode: %s" % self.floodMode
        print "Flood Iter: %s" % self.floodIter
        item = self.selectedVtxMapItem
        if item is not None:
            clothNode = item._widget.clothNode
            vtxMap = item._widget.mapVtx
            vtxSel = ceCmds.getModelSelVtx(clothNode, indexOnly=True)
            vtxData = ceCmds.getVtxMapData(clothNode, vtxMap)
            if self.floodMode == 'smooth':
                for n in range(self.floodIter):
                    print "Iter %s" % (n + 1)
                    vtxData = self.smoothValues(clothNode, vtxSel, vtxData)
            else:
                for ind in vtxSel:
                    newVal = vtxData[ind]
                    #-- Get New Vertex Value --#
                    if self.floodMode == 'replace':
                        newVal = self.floodValue
                    elif self.floodMode == 'add':
                        newVal = float(newVal + self.floodValue)
                    elif self.floodMode == 'mult':
                        newVal = float(newVal * self.floodValue)
                    #-- Check Vertex Clamp --#
                    if newVal is not None:
                        vtxData[ind] = self.clampValue(newVal)
            #-- Set Vertex Map --#
            ceCmds.setVtxMapData(clothNode, vtxMap, vtxData)
            if self.paintMode == 'vtxColor':
                self.on_vtxMapNodeDoubleClick()

    def smoothValues(self, clothNode, vtxSel, vtxData):
        """ Smooth selected vertex influence value
            :param clothNode: Cloth node name
            :type clothNode: str
            :param vtxSel: Selected vertex
            :type vtxSel: list
            :param vtxData: VtxMap influences
            :type vtxData: list
            :return: New vertex data
            :rtype: list """
        newVtxData = vtxData
        for vtx in vtxSel:
            val = 0
            connectedVtx = ceCmds.getConnectedVtx(clothNode, vtx)
            for sel in connectedVtx:
                val = val + vtxData[sel]
            val = float(val / len(connectedVtx))
            newVtxData[vtx] = self.clampValue(val)
        return newVtxData

    def clampValue(self, value):
        """ Clamp given value if enable
            :param value: Value to clamp
            :type value: float
            :return: New value
            :rtype: float """
        if value is not None:
            clampMin, clampMax = self.vtxClamp
            if clampMin is not None:
                if value < clampMin:
                    value = clampMin
            if clampMax is not None:
                if value > clampMax:
                    value = clampMax
        return value

    def on_vtxMapInfo(self):
        """ Command launched when 'Tree Values' QTreeWidget selection changed
            Update vertex selection in scene """
        selItems = self.twVtxValues.selectedItems()
        selVtx = []
        if selItems:
            for item in selItems:
                selVtx.append("%s.vtx[%s]" % (item.model, item.vtxIndex))
        if not selVtx:
            ceCmds.clearVtxSelection()
        else:
            ceCmds.selectVtxOnModel(selVtx)

    def on_updateVtxInfo(self):
        """ Command launched when QPushButton 'Update From Scene' is clicked
            Update vertexMap info QTreeWidgetItem selection from scene """
        vtxItem = self.selectedVtxMapItem
        if vtxItem is not None:
            selVtx = ceCmds.getModelSelVtx(vtxItem._widget.clothNode, indexOnly=True)
            if selVtx:
                allItems = pQt.getAllItems(self.twVtxValues)
                for n, item in enumerate(allItems):
                    if n in selVtx:
                        self.twVtxValues.setItemSelected(item, True)
                    else:
                        self.twVtxValues.setItemSelected(item, False)

    def new_vtxMapItem(self, clothNode, mapName):
        """ Create new mapType 'QTreeWidgetItem'
            :param clothNode: Cloth node name
            :type clothNode: str
            :param mapName: Vertex map name
            :type mapName: str """
        newItem = QtGui.QTreeWidgetItem()
        newItem._widget = VtxMapNode(self, clothNode, mapName)
        return newItem

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


class VtxMapNode(QtGui.QWidget, wgVtxMapNodeUI.Ui_wgVtxMapNode):
    """ Widget VertexMap QTreeWidgetItem node, child of VtxMapUi
        :param pWidget: Parent Widget
        :type pWidget: QtGui.QWidget
        :param clothNode: Cloth node name
        :type clothNode: str
        :param mapName: Vertex map name
        :type mapName: str """

    def __init__(self, pWidget, clothNode, mapName):
        self.pWidget = pWidget
        self.mainUi = self.pWidget.mainUi
        self.clothNode = clothNode
        self.mapName = mapName
        self.mapType = "%sMapType" % self.mapName
        self.mapVtx = "%sPerVertex" % self.mapName
        super(VtxMapNode, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        self.lVtxMap.setText(self.mapName)
        self.cbState.setCurrentIndex(ceCmds.getVtxMapType(self.clothNode, self.mapType))
        self.cbState.currentIndexChanged.connect(self.on_mapType)
        self.rf_vtxMapLabel()
        self.rf_vtxMapLock(rfBtnState=True)
        self.pbLock.clicked.connect(self.on_mapLock)

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

    @property
    def vtxMapLock(self):
        """ Get vtxMap lock state
            :return: VtxMap lock state
            :rtype: bool """
        return self.pbLock.isChecked()

    def setMapData(self, mapIndex, mapData):
        """ Set vertex map data
            :param mapIndex: VtxMap type (0 = None, 1 = Vertex, 2 = Texture)
            :type mapIndex: int
            :param mapData: Influence list per vertex
            :type mapData: list """
        self.cbState.setCurrentIndex(mapIndex)
        self.on_mapType()
        if mapIndex == 1:
            ceCmds.setVtxMapData(self.clothNode, self.mapVtx, mapData)

    def rf_vtxMapLabel(self):
        """ Refresh mapType label color """
        if self.vtxMapIndex == 0:
            color = self.mainUi.getLabelColor('lightGrey')
        elif self.vtxMapIndex == 1:
            color = self.mainUi.getLabelColor('green')
        elif self.vtxMapIndex == 2:
            color = self.mainUi.getLabelColor('blue')
        else:
            color = self.mainUi.getLabelColor('default')
        self.lVtxMap.setStyleSheet("color: rgb(%s, %s, %s)" % (color[0], color[1], color[2]))

    def rf_vtxMapLock(self, rfBtnState=False):
        """ Refresh mapType lock icon """
        lockType = ceCmds.attrIsLocked("%s.%s" % (self.clothNode, self.mapType))
        lockVtx = ceCmds.attrIsLocked("%s.%s" % (self.clothNode, self.mapVtx))
        if lockType or lockVtx:
            lockIcon = self.mainUi.lockIconOn
            if rfBtnState:
                self.pbLock.setChecked(True)
        else:
            lockIcon = self.mainUi.lockIconOff
            if rfBtnState:
                self.pbLock.setChecked(False)
        self.pbLock.setIcon(lockIcon)
        self.cbState.setEnabled(not self.vtxMapLock)

    def on_mapType(self):
        """ Command launched when QComboBox 'mapType' current index changed
            Set clothNode mapType, and refresh ui """
        ceCmds.setVtxMapType(self.clothNode, self.mapType, self.cbState.currentIndex())
        self.rf_vtxMapLabel()

    def on_mapLock(self):
        """ Command launched when 'Lock' QPushButton is clicked
            Set clothNode attribute losk state """
        ceCmds.setAttrLock("%s.%s" % (self.clothNode, self.mapType), self.vtxMapLock)
        ceCmds.setAttrLock("%s.%s" % (self.clothNode, self.mapVtx), self.vtxMapLock)
        self.rf_vtxMapLock()
        self.pWidget.pbFlood.setEnabled(not self.vtxMapLock)


class VtxStorageButton(QtGui.QPushButton):
    """ Widget vertex storage QPushButton, child of vtxMapUi
        :param btnLabel: Button label
        :type btnLabel: str
        :param btnType: Button storage type ('vtxSet' or 'vtxData')
        :type btnType: str
        :param mainUi: ClothEditor MainUi
        :type mainUi: QtGui.QMainWindow
        :param pWidget: Parent widget
        :type pWidget: QtGui.QWidget """

    def __init__(self, btnLabel, btnType, mainUi, pWidget):
        self.btnLabel = btnLabel
        self.btnType = btnType
        self.mainUi = mainUi
        self.pWidget = pWidget
        self.storage = []
        super(VtxStorageButton,self).__init__()
        self._setupUi()

    def _setupUi(self):
        """ Setup widget ui """
        self.setText(self.btnLabel)
        self.setToolTip("Empty")
        self.setMaximumHeight(20)

    def popupMenuItems(self):
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
        sceneSel = ceCmds.getSceneSelection()
        if len(sceneSel) == 1:
            if not '.vtx' in sceneSel:
                setSel = self.storage[0].split('.')[0]
                if not setSel == sceneSel[0]:
                    newStorage = []
                    for sel in self.storage:
                        newStorage.append(sel.replace(setSel, sceneSel[0]))
                    ceCmds.selectVtxOnModel(newStorage)
                else:
                    ceCmds.selectVtxOnModel(self.storage)
            else:
                ceCmds.selectVtxOnModel(self.storage)
        else:
            ceCmds.selectVtxOnModel(self.storage)

    def on_vtxData(self):
        """ Command launched QPushButton is clicked, restore vertex data storage """
        item = self.pWidget.selectedVtxMapItem
        if item is not None:
            curData = ceCmds.getVtxMapData(item._widget.clothNode, item._widget.mapVtx)
            if not len(curData) == len(self.storage):
                print "!!! WARNING: Topo not the same !"
            else:
                ceCmds.setVtxMapData(item._widget.clothNode, item._widget.mapVtx, self.storage)

    def on_rightClick(self):
        """ Command launched when QPushButton is right clicked, launch popupMenu """
        self.pmMenu = pQt.popupMenu(self.popupMenuItems())
        #-- Refresh Menu Items Visibility --#
        if not self.storage:
            self.pmMenu.items[0].setEnabled(False)
            self.pmMenu.items[2].setEnabled(False)
        else:
            self.pmMenu.items[1].setEnabled(False)
        #-- Pop Menu --#
        self.pmMenu.exec_()

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
        vtxList = ceCmds.getModelSelVtx(self.mainUi.wgSceneNodes.selectedClothNode)
        if vtxList:
            self.storage = vtxList
            self.setToolTip("Used")
            print "// Vertex storage: %s : Success !" % self.btnLabel
        else:
            print "!!! WARNING: No vertex found to store !!!"

    def on_storeVtxData(self):
        """ Command launched when QAction 'Store Vertex Data' is clicked,
            Store selected data in 'storage' """
        item = self.pWidget.selectedVtxMapItem
        if item is not None:
            data = ceCmds.getVtxMapData(item._widget.clothNode, item._widget.mapVtx)
            if data:
                self.storage = data
                print "// Data storage: %s : Success !" % self.btnLabel
            else:
                print "!!! WARNING: No data found to store !!!"

    def on_clearStorage(self):
        """ Command launched when QAction 'Clear ... Storage' is clicked """
        self.storage = []
        self.setToolTip("Empty")


class FilesUi(QtGui.QWidget, wgFilesUI.Ui_wgFiles):
    """ Widget Files, child of AttrUi and VtxMapUi
        :param mainUi: ClothEditor MainUi
        :type mainUi: QtGui.QMainWindow
        :param fileMode: 'attrs' or 'vtxMap'
        :type fileMode: str
        :param pWidget: Parent widget
        :type pWidget: QtGui.QWidget """

    def __init__(self, mainUi, fileMode, pWidget):
        if fileMode == 'attrs':
            print "\t ---> Preset Files"
        else:
            print "\t ---> VtxMap Files"
        self.mainUi = mainUi
        self.fileMode = fileMode
        self.pWidget = pWidget
        super(FilesUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        if self.mainUi.filesRootPath is None:
            self.mainUi.filesRootPath = self.defaultRootPath
        self.rf_rootPath()
        self.pbNewProject.clicked.connect(self.on_newProject)
        self.pbNewFolder.clicked.connect(self.on_newFolder)
        self.pbRefresh.clicked.connect(self.rf_directories)
        self.twDir.itemClicked.connect(self.rf_files)
        self.pbSave.clicked.connect(self.on_save)
        self.pbLoad.clicked.connect(self.on_load)

    @property
    def defaultRootPath(self):
        """ Get default files root path
            :return: Files root path
            :rtype: str """
        return os.path.normpath("D:/rndBin/clothEditor")

    def getItemFromRelPath(self, relPath):
        """ Get directory item from given relative path
            :param relPath: Item relPath
            :type relPath: str
            :return: Directory item
            :rtype: QtGui.QTreeWidgetItem """
        allItems = pQt.getAllItems(self.twDir)
        for item in allItems:
            if item.relPath == relPath:
                return item

    def rf_rootPath(self):
        """ Refresh Files Root Path """
        self.lRootPathVal.setText(pFile.conformPath(self.mainUi.filesRootPath))

    # noinspection PyTypeChecker
    def rf_directories(self):
        """ Refresh directories tree """
        self.twDir.clear()
        if not os.path.exists(self.mainUi.filesRootPath):
            raise IOError, "!!! Files Root Path doesn't exists: %s !!!" % self.mainUi.filesRootPath
        pathDict = pFile.pathToDict(self.mainUi.filesRootPath)
        for path in pathDict['_order']:
            if not path == self.mainUi.filesRootPath:
                newItem = self.new_dirItem(path)
                if newItem.parent is None:
                    self.twDir.addTopLevelItem(newItem)
                else:
                    parent = self.getItemFromRelPath(newItem.parent)
                    parent.addChild(newItem)

    def rf_files(self):
        """ Refresh files tree """
        self.twFiles.clear()
        selItems = self.twDir.selectedItems()
        if selItems:
            for f in os.listdir(selItems[0].absPath):
                if f.endswith('%s.py' % self.fileMode):
                    fileItem = self.new_fileItem(selItems[0].absPath, f)
                    self.twFiles.addTopLevelItem(fileItem)

    def rf_widgetToolTips(self):
        """ Refresh all widget toolTip """
        if self.mainUi.toolTipState:
            self.pbNewProject.setToolTip("Create new project in root directory")
            self.pbNewFolder.setToolTip("Create new folder in selected project")
            self.pbRefresh.setToolTip("Refresh directory tree")
            self.twDir.setToolTip("Directory tree")
            self.twFiles.setToolTip("Files tree")
            self.pbSave.setToolTip("Save params to selected folder")
            self.pbLoad.setToolTip("Load selected params file")
        else:
            for widget in [self.pbNewProject, self.pbNewFolder, self.pbRefresh, self.twDir, self.twFiles,
                           self.pbSave, self.pbLoad]:
                widget.setToolTip("")

    def on_newProject(self):
        """ Command launched when 'New Project' QPushButton is clicked """
        if not os.path.exists(self.mainUi.filesRootPath):
            raise IOError, "!!! Files Root Path doesn't exists: %s !!!" % self.mainUi.filesRootPath
        self.pdProject = pQt.PromptDialog("New Project Name", self.newProject)
        self.pdProject.exec_()

    def newProject(self):
        """ Create new project directory
            :return: Project path
            :rtype: str """
        projectName = self.pdProject.result()['result_1']
        if projectName is None or projectName in ['', ' ']:
            raise KeyError, "!!! Project name can not be empty !!!"
        projectPath = os.path.join(self.mainUi.filesRootPath, projectName)
        if os.path.exists(projectPath):
            raise IOError, "!!! Project name already exists: %s !!!" % projectName
        try:
            os.mkdir(projectPath)
            print "Create new clothEditor project: %s" % projectName
        except:
            raise IOError, "!!! Can not create directory %s !!!" % projectPath
        self.pdProject.close()
        self.rf_directories()
        return projectPath

    def on_newFolder(self):
        """ Command launched when 'New Folder' QPushButton is clicked """
        if not os.path.exists(self.mainUi.filesRootPath):
            raise IOError, "!!! Files Root Path doesn't exists: %s !!!" % self.mainUi.filesRootPath
        selItems = self.twDir.selectedItems()
        if not selItems:
            raise ValueError, "!!! Folder must be selected to create new folder !!!"
        self.pdFolder = pQt.PromptDialog("New Folder Name", partial(self.newFolder, selItems[0]))
        self.pdFolder.exec_()

    def newFolder(self, item):
        """ Create new project directory
            :param item: Selected directory item
            :type item: QtGui.QTreeWidgetItem
            :return: Project path
            :rtype: str """
        folderName = self.pdFolder.result()['result_1']
        if folderName is None or folderName in ['', ' ']:
            raise KeyError, "!!! Project name can not be empty !!!"
        folderPath = os.path.join(self.mainUi.filesRootPath, os.path.normpath(item.relPath), folderName)
        if os.path.exists(folderPath):
            raise IOError, "!!! Project name already exists: %s !!!" % folderName
        try:
            os.mkdir(folderPath)
            print "Create new clothEditor folder: %s" % folderName
        except:
            raise IOError, "!!! Can not create directory %s !!!" % folderPath
        self.pdFolder.close()
        self.rf_directories()
        return folderPath

    def on_save(self):
        """ Command launched when 'Save' QPushButton is clicked """
        if not os.path.exists(self.mainUi.filesRootPath):
            raise IOError, "!!! Files Root Path doesn't exists: %s !!!" % self.mainUi.filesRootPath
        selItems = self.twDir.selectedItems()
        if not selItems:
            raise ValueError, "!!! Folder must be selected to save new file !!!"
        selNode = self.mainUi.wgSceneNodes.selectedClothNode
        if selNode is None:
            raise ValueError, "!!! Scene Node item must be selected to save new file !!!"
        if self.fileMode == 'vtxMap' and ceCmds.getClothType(selNode) not in ['nCloth', 'nRigid']:
            raise ValueError, "!!! Can only save vertexMap of nCloth and nRigid node !!!"
        self.dialSave = SaveFileDialog(self, selItems[0])
        self.dialSave.exec_()

    def saveFile(self, fileAbsPath):
        """ Save params to given file
            :param fileAbsPath: File absolute path
            :type fileAbsPath: str """
        fileName = fileAbsPath.split('/')[-1]
        filePath = '/'.join(fileAbsPath.split('/')[:-1])
        clothNode = self.mainUi.wgSceneNodes.selectedClothNode
        #-- Get Params --#
        if self.fileMode == 'attrs':
            print "#-- Save Preset --#"
            params = self.mainUi.wgAttributes.nodePreset
        else:
            print "#-- save Vertex Map --#"
            params = self.mainUi.wgVtxMaps.nodeVtxData()
        #-- Genere Text --#
        txt = []
        for k, v in params.iteritems():
            if isinstance(v, str):
                txt.append("%s = %r" % (k, v))
            else:
                txt.append("%s = %s" % (k, v))
        txtParam = '\n'.join(txt)
        #-- Save File --#
        print "File Name: ", fileName
        print "File Path: ", filePath
        print "Cloth Node: ", clothNode
        try:
            pFile.writeFile(fileAbsPath, str(txtParam))
            print "%s file saved: %s" % (self.fileMode, fileAbsPath)
        except:
            raise IOError, "!!! Can not save file %s !!!" % fileAbsPath
        self.rf_files()

    def on_load(self):
        """ Command launched when 'Load' QPushButton is clicked """
        if not os.path.exists(self.mainUi.filesRootPath):
            raise IOError, "!!! Files Root Path doesn't exists: %s !!!" % self.mainUi.filesRootPath
        selNode = self.mainUi.wgSceneNodes.selectedClothNode
        if selNode is None:
            raise ValueError, "!!! Scene Node item must be selected to load file !!!"
        selFiles = self.twFiles.selectedItems()
        if not selFiles:
            raise ValueError, "!!! File item must be selected to load file !!!"
        self.loadFile(selFiles[0])

    def loadFile(self, selFile):
        """ Load params from given file
            :param selFile: File Select file item
            :type selFile: QtGui.QTreeWidgetItem """
        selNodes = self.mainUi.wgSceneNodes.twSceneNodes.selectedItems()
        if selNodes:
            if not selNodes[0].clothType == selFile.params['_clothType']:
                raise TypeError, "!!! Cloth type doesn't match, should be %s !!!" % selFile.params['_clothType']
            if self.fileMode == 'attrs':
                print "Loading Preset %s" % selFile.label
                for item in pQt.getAllItems(self.pWidget.twPreset):
                    if item.itemType == 'attr':
                        if not item._widget.attrLock:
                            item._widget.setValue(selFile.params[item.clothAttr]['val'])
            elif self.fileMode == 'vtxMap':
                print "Loading VtxMap %s" % selFile.label
                for item in pQt.getAllItems(self.pWidget.twMaps):
                    if not item._widget.vtxMapLock:
                        item._widget.setMapData(selFile.params[item._widget.mapName]['mapType'],
                                                selFile.params[item._widget.mapName]['mapData'])

    def new_dirItem(self, path):
        """ Create new directory item
            :param path: New item absolut path
            :type path: str
            :return: New dir item
            :rtype: QtGui.QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem.absPath = pFile.conformPath(path)
        newItem.folder = path.split(os.sep)[-1]
        newItem.relPath = pFile.conformPath(path.replace(self.mainUi.filesRootPath, ''))
        if newItem.relPath.startswith('/'):
            newItem.relPath = newItem.relPath[1:]
        newItem.parent = '/'.join(newItem.relPath.split('/')[:-1])
        if newItem.parent == "":
            newItem.parent = None
        newItem.setText(0, newItem.folder)
        return newItem

    def new_fileItem(self, filePath, fileName):
        """ Create new directory item
            :param filePath: New item absolut path
            :type filePath: str
            :param fileName: New item file name
            :type fileName: str
            :return: New file item
            :rtype: QtGui.QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem.filePath = filePath
        newItem.fileName = fileName
        newItem.label = fileName.split('.')[0]
        newItem.params = pFile.readPyFile(os.path.normpath('%s/%s' % (newItem.filePath, newItem.fileName)))
        if newItem.params['_clothType'] == 'nCloth':
            color = self.mainUi.getLabelColor('green')
        elif newItem.params['_clothType'] == 'nRigid':
            color = self.mainUi.getLabelColor('blue')
        elif newItem.params['_clothType'] == 'nucleus':
            color = self.mainUi.getLabelColor('yellow')
        else:
            color = self.mainUi.getLabelColor('default')
        newItem.setTextColor(0, QtGui.QColor(color[0], color[1], color[2]))
        newItem.setText(0, newItem.label)
        return newItem


class SaveFileDialog(QtGui.QDialog, dialSaveFileUI.Ui_dialSaveFile):

    def __init__(self, pWidget, item):
        self.pWidget = pWidget
        self.item = item
        self.mainUi = self.pWidget.mainUi
        super(SaveFileDialog, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup dialog ui """
        self.setupUi(self)
        if self.pWidget.fileMode == 'attrs':
            self.lTitle.setText("Save Preset")
        elif self.pWidget.fileMode == 'vtxMap':
            self.lTitle.setText("Save Vertex Map")
        self.lRootPathVal.setText(pFile.conformPath(self.mainUi.filesRootPath))
        self.lFilePathVal.setText(self.item.relPath)
        self.leFileNameEdit.editingFinished.connect(self.rf_result)
        self.pbSave.clicked.connect(self.on_save)
        self.pbCancel.clicked.connect(self.close)

    def rf_result(self):
        """ Refresh result path """
        fileName = "%s.%s.py" % (str(self.leFileNameEdit.text()), self.pWidget.fileMode)
        self.lFileNameVal.setText(fileName)
        absPath = '%s/%s/%s' % (str(self.lRootPathVal.text()), str(self.lFilePathVal.text()), fileName)
        self.lAbsPathVal.setText(absPath)

    def on_save(self):
        """ Command launched when 'Save' QPushButton is clicked """
        self.rf_result()
        self.pWidget.saveFile(str(self.lAbsPathVal.text()))
        self.close()
