import os
from functools import partial
from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from tools.maya.cmds import pRigg
from lib.system import procFile as pFile
from tools.maya.cloth.dynEval import dynEvalCmds as deCmds
from tools.maya.cloth.dynEval.ui import wgSceneNodesUI, wgSceneNodeUI, wgDynEvalUI, wgCacheListUI,\
                                        wgCacheNodeUI, wgCacheInfoUI


class SceneNodeUi(QtGui.QWidget, wgSceneNodesUI.Ui_wgSceneNodes):
    """
    Widget SceneNodes, child of mainUi
    :param mainUi: ClothCache mainUi
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        print "\t ---> SceneNodeUi"
        self.mainUi = mainUi
        super(SceneNodeUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup widget ui
        """
        self.setupUi(self)
        self.twSceneNodes.itemClicked.connect(self.on_sceneNodeSingleClick)
        self.twSceneNodes.itemDoubleClicked.connect(self.on_sceneNodeDoubleClick)
        self.cbCloth.clicked.connect(self.on_showClothType)
        self.cbRigid.clicked.connect(self.on_showClothType)
        self.rf_sceneNodes()

    @property
    def itemAttrOrder(self):
        """
        Get SceneNodeItem attribute list
        :return: Item attributes
        :rtype: list
        """
        return ['clothNode', 'clothNs', 'clothName', 'clothType', 'clothParent', 'clothMesh', 'clothShape']

    @property
    def selectedClothItem(self):
        """
        Get selected sceneNode item
        :return: ClothNode item
        :rtype: QtGui.QTreeWidgetItem
        """
        selItems = self.twSceneNodes.selectedItems()
        if selItems:
            return selItems[0]

    @property
    def selectedClothNode(self):
        """
        Get selected clothNode name
        :return: ClothNode name
        :rtype: str
        """
        if self.selectedClothItem is not None:
            return self.selectedClothItem.clothNode

    @staticmethod
    def getRelativeCachePath(item):
        """
        Get cache file relative path
        :param item: ClothNode item
        :type item: QtGui.QTreeWidgetItem
        :return: Cache file relative path
        :rtype: str
        """
        nsFld = item.clothNs
        objFld = '_'.join(item.clothName.split('_')[:-1])
        cacheRelPath = pFile.conformPath(os.path.join(nsFld, objFld))
        return cacheRelPath

    def rf_sceneNodes(self):
        """
        Refresh QTreeWidget 'Scene Nodes'
        """
        self.twSceneNodes.clear()
        #-- Populate Nucleus node --#
        for nucleus in deCmds.getAllNucleus():
            nucleusItem = self.add_sceneNode(nucleus)
            #-- Populate nCloth Node --#
            dynNodes = pRigg.findTypeInHistory(nucleus, ['nCloth', 'nRigid'], future=True, past=True)
            rigidNodes = []
            for node in dynNodes:
                nodeType = deCmds.getClothType(node)
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
        """
        Refresh all widget toolTip
        """
        if self.mainUi.toolTipState:
            self.cbCloth.setToolTip("Show / Hide nCloth items")
            self.cbRigid.setToolTip("Show / Hide nRigid items")
        else:
            for widget in [self.cbCloth, self.cbRigid]:
                widget.setToolTip("")

    def rf_sceneItemToolTips(self):
        """
        Refresh all sceneNodes item toolTip
        """
        for item in pQt.getAllItems(self.twSceneNodes):
            self.rf_sceneItemToolTip(item)

    def rf_sceneItemToolTip(self, item):
        """
        Refresh given sceneNode item toolTip
        :param item: SceneNode  item
        :type item: QtGui.QTreeWidgetItem
        """
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

    def rf_namespaces(self):
        """
        Refresh all sceneNodes item namespace
        """
        for item in pQt.getAllItems(self.twSceneNodes):
            self.rf_namespace(item)

    def rf_namespace(self, item):
        """
        Refresh given sceneNode item namespace
        :param item: SceneNode  item
        :type item: QtGui.QTreeWidgetItem
        """
        if item.clothType == 'nucleus':
            if self.mainUi.namespaceState:
                item._widget.lSceneNode.setText(item.clothNode)
            else:
                item._widget.lSceneNode.setText(item.clothNode.split(':')[-1])
        elif item.clothType in ['nCloth', 'nRigid']:
            if self.mainUi.namespaceState:
                item._widget.lSceneNode.setText(item.clothMesh)
            else:
                item._widget.lSceneNode.setText(item.clothMesh.split(':')[-1])

    def add_sceneNode(self, clothNode, parent=None):
        """
        Add QTreeWidgetItem to 'SceneNodes' QTreeWidget
        :param clothNode: Cloth Node name
        :type clothNode: str
        :param parent: Parent item
        :type parent: QtGui.QTreeWidgetItem
        :return: New item
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = self.new_sceneNodeItem(clothNode)
        if parent is None:
            self.twSceneNodes.addTopLevelItem(newItem)
        else:
            parent.addChild(newItem)
        self.twSceneNodes.setItemWidget(newItem, 0, newItem._widget)
        return newItem

    def on_sceneNodeSingleClick(self):
        """
        Command launched when 'SceneNode' QTreeWidgetItem is clicked.
        """
        for item in pQt.getAllItems(self.twSceneNodes):
            item._widget.rf_label()
        self.rf_namespaces()
        if self.selectedClothItem is not None:
            self.mainUi.cacheList.rf_cacheList()
            self.mainUi.cacheList.ud_cacheAssigned()
        self.mainUi.cacheInfo.clearInfos()

    def on_sceneNodeDoubleClick(self):
        """
        Command launched when 'SceneNode' QTreeWidgetItem is double clicked.
        Select maya cloth node.
        """
        selItems = self.twSceneNodes.selectedItems()
        if selItems:
            deCmds.selectModel(selItems[0].clothNode)

    def on_showClothType(self):
        """
        Command launched when QCheckBox 'nCloth' or 'nRigid' is clicked,
        Update QTreeWidget with selected cloth type
        """
        for item in pQt.getAllItems(self.twSceneNodes):
            if item.clothType == 'nCloth':
                self.twSceneNodes.setItemHidden(item, not self.cbCloth.isChecked())
            elif item.clothType == 'nRigid':
                self.twSceneNodes.setItemHidden(item, not self.cbRigid.isChecked())

    def new_sceneNodeItem(self, clothNode):
        """
        Create new 'clothNode' QTreeWidgetItem
        :param clothNode: Cloth Node name
        :type clothNode: str
        :return: Scene node QTreeWidgetItem
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = QtGui.QTreeWidgetItem()
        #-- Add Attributes --#
        ns, name = deCmds.getNamespace(clothNode)
        newItem.clothNode = clothNode
        newItem.clothNs = ns
        newItem.clothName = name
        newItem.clothType = deCmds.getClothType(clothNode)
        if newItem.clothType == 'nucleus':
            newItem.clothParent = clothNode
            newItem.clothMesh = None
            newItem.clothShape = None
        else:
            newItem.clothParent = deCmds.getNodeParent(clothNode)
            newItem.clothMesh = deCmds.getModelFromClothNode(clothNode)
            newItem.clothShape = deCmds.getNodeShape(newItem.clothMesh)
        newItem.attrOrder = self.itemAttrOrder
        newItem._widget = SceneNode(self, newItem)
        self.rf_sceneItemToolTip(newItem)
        self.rf_namespace(newItem)
        return newItem


class SceneNode(QtGui.QWidget, wgSceneNodeUI.Ui_wgSceneNode):
    """
    Widget SceneNode QTreeWidgetItem, child of SceneNodeUi
    :param pWidget: Parent Widget
    :type pWidget: QtGui.QWidget
    :param pItem: Parent item
    :type pItem: QtGui.QTreeWidgetItem
    """

    def __init__(self, pWidget, pItem):
        self.pWidget = pWidget
        self.pItem = pItem
        self.mainUi = self.pWidget.mainUi
        super(SceneNode, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup widget ui
        """
        self.setupUi(self)
        self.rf_label()
        self.rf_nodeTypeIcon()
        self.rf_nodeEnableIcon(rfBtnState=True)
        self.pbEnable.clicked.connect(self.on_stateIcon)

    @property
    def enableState(self):
        """
        Get Attr enable state
        :return: Attr enable state
        :rtype: bool
        """
        return self.pbEnable.isChecked()

    def getConnectedCacheFileNodes(self):
        """
        Get connected cacheFile nodes
        :return: Connected cacheFileNodes
        :rtype: list
        """
        return deCmds.getCacheNodes(self.pItem.clothNode)

    def rf_label(self):
        """
        Refresh label text and color
        """
        newFont = QtGui.QFont()
        # newFont.setBold(True)
        color = (self.mainUi.getLabelColor('default'))
        if self.pItem.clothType == 'nucleus':
            newFont.setPointSize(10)
            self.lSceneNode.setText(self.pItem.clothNode)
            if not self.pItem.isSelected():
                color = self.mainUi.getLabelColor('yellow')
        elif self.pItem.clothType == 'nCloth':
            self.lSceneNode.setText(self.pItem.clothMesh)
            if not self.pItem.isSelected():
                color = self.mainUi.getLabelColor('green')
        elif self.pItem.clothType == 'nRigid':
            self.lSceneNode.setText(self.pItem.clothMesh)
            if not self.pItem.isSelected():
                color = self.mainUi.getLabelColor('blue')
        self.lSceneNode.setFont(newFont)
        self.lSceneNode.setStyleSheet("color: rgb(%s, %s, %s)" % (color[0], color[1], color[2]))

    def rf_nodeTypeIcon(self):
        """
        Refresh cloth node type icon
        """
        if self.pItem.clothType == 'nucleus':
            self.pbIcon.setIcon(self.mainUi.nucleusIcon)
        elif self.pItem.clothType == 'nCloth':
            self.pbIcon.setIcon(self.mainUi.nClothIcon)
        elif self.pItem.clothType == 'nRigid':
            self.pbIcon.setIcon(self.mainUi.nRigidIcon)

    def rf_nodeEnableIcon(self, rfBtnState=False):
        """
        Refresh state icon
        :param rfBtnState: Enable btn state refresh
        :type rfBtnState: bool
        """
        if self.pItem.clothType in ['nCloth', 'nRigid']:
            state = deCmds.getAttr(self.pItem.clothNode, 'isDynamic')
        else:
            state = deCmds.getAttr(self.pItem.clothNode, 'enable')
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
        """
        Command launched when 'pbEnable' QPushButton is clicked,
        Edit enable state (isDynamic state for nCloth and nRigid.
        """
        if self.pItem.clothType in ['nCloth', 'nRigid']:
            deCmds.setAttr(self.pItem.clothNode, 'isDynamic', self.enableState)
        else:
            deCmds.setAttr(self.pItem.clothNode, 'enable', self.enableState)
        self.rf_nodeEnableIcon()


class DynEvalCtrl(QtGui.QWidget, wgDynEvalUI.Ui_wgDynEval):
    """
    Widget CacheEval, child of mainUi
    :param mainUi: ClothCache mainUi
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        print "\t ---> DynEvalCtrl"
        self.mainUi = mainUi
        self.sceneNodes = self.mainUi.sceneNodes
        self.cacheList = None
        self.evalClothCacheIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'evalClothCache.png'))
        self.appendToCacheIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'appendToCache.png'))
        self.deleteCacheIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'deleteCache.png'))
        self.evalGeoCacheIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'evalGeoCache.png'))
        super(DynEvalCtrl, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup widget ui
        """
        self.setupUi(self)
        self.pbSet.clicked.connect(self.on_setTimeRange)
        self.pbFull.clicked.connect(self.on_fullTimeRange)
        self.pbReplace.clicked.connect(self.rf_overWriteMode)
        self.pbClothCache.setIcon(self.evalClothCacheIcon)
        self.pbClothCache.clicked.connect(partial(self.on_createCache, cacheMode='nCloth'))
        self.pbGeoCache.setIcon(self.evalGeoCacheIcon)
        self.pbGeoCache.clicked.connect(partial(self.on_createCache, cacheMode='geo'))
        self.pbAppendCache.setIcon(self.appendToCacheIcon)
        self.pbAppendCache.clicked.connect(self.on_appendToCache)
        self.pbClearCache.setIcon(self.deleteCacheIcon)
        self.pbClearCache.clicked.connect(self.on_delCacheNode)
        self.on_fullTimeRange()
        self.rf_overWriteMode()

    @property
    def startTime(self):
        """
        Get scene start time
        :return: Start time
        :rtype: int
        """
        return int(self.sbStart.value())

    @property
    def endTime(self):
        """
        Get scene stop time
        :return: Stop time
        :rtype: int
        """
        return int(self.sbStop.value())

    @property
    def cacheModeIndex(self):
        """
        Get Cacheable attributes mode index
        :return: Cache mode index
        :rtype: int
        """
        return self.cbCacheAttr.currentIndex()

    @property
    def cacheableMode(self):
        """
        Get Cacheable attributes mode
        :return: Cache mode ('positions', 'velocities' or 'internalState')
        :rtype: str
        """
        if self.cacheModeIndex == 0:
            return 'positions'
        if self.cacheModeIndex == 1:
            return 'velocities'
        if self.cacheModeIndex == 2:
            return 'internalState'

    @property
    def overWriteMode(self):
        """
        Get cache overWrite mode
        :return: Cache overWrite state
        :rtype: bool
        """
        return self.pbReplace.isChecked()

    def rf_widgetToolTips(self):
        """
        Refresh all widget toolTip
        """
        if self.mainUi.toolTipState:
            self.sbStart.setToolTip("Simulation start frame")
            self.sbStop.setToolTip("Simulation end frame")
            self.pbSet.setToolTip("Init startFrame and stopFrame with time slider values")
            self.pbFull.setToolTip("Init startFrame and stopFrame with time range values")
            self.cbCacheAttr.setToolTip("NCloth node cache mode: Edit nClothNode cacheable attributes."
                                        "\nUse 'InternalState' to allow 'Append Cache'")
            self.pbReplace.setToolTip("NCloth cache file overWrite mode: 'New' or 'Replace'")
            self.pbClothCache.setToolTip("Create nCloth cache from selected ui cloth item")
            self.pbAppendCache.setToolTip("Append to cache from selected ui cloth item")
            self.pbClearCache.setToolTip("Delete cache node from selected ui cloth item")
            self.pbGeoCache.setToolTip("Create geo cache from selected scene mesh")
        else:
            for widget in [self.sbStart, self.sbStop, self.pbSet, self.pbFull, self.cbCacheAttr, self.pbReplace,
                           self.pbClothCache, self.pbAppendCache, self.pbGeoCache, self.pbClearCache]:
                widget.setToolTip("")

    def rf_overWriteMode(self):
        """
        Refresh cache overWrite mode
        """
        if self.pbReplace.isChecked():
            self.pbReplace.setText("REPLACE")
            self.pbReplace.setStyleSheet("background-color: rgb(150, 0, 0)")
        else:
            self.pbReplace.setText("NEW")
            self.pbReplace.setStyleSheet("background-color: rgb(0, 150, 0)")

    def on_setTimeRange(self):
        """
        Refresh time range QSpinBox
        """
        range = deCmds.getTimeRange()
        self.sbStart.setValue(int(range['timeSliderStart']))
        self.sbStop.setValue(int(range['timeSliderStop']))

    def on_fullTimeRange(self):
        """
        Refresh time range QSpinBox
        """
        range = deCmds.getTimeRange()
        self.sbStart.setValue(int(range['timeRangeStart']))
        self.sbStop.setValue(int(range['timeRangeStop']))

    def on_createCache(self, cacheMode='nCloth'):
        """
        Command launched when 'Create nCloth Cache' QPushButton is clicked
        :param cacheMode: 'nCloth' or 'geo'
        :type cacheMode: str
        """
        print "\n#===== Create Cache =====#"
        self._checkCache(cacheMode)
        sceneItem = self.sceneNodes.selectedClothItem
        cacheFullPath = self._mkNClothCacheDir(sceneItem)
        cacheFileName = '%s-%s-%s' % (sceneItem.clothNs, '_'.join(sceneItem.clothName.split('_')[:-1]),
                                      cacheFullPath.split('/')[-1])
        if cacheMode == 'nCloth':
            deCmds.deleteCacheNode(sceneItem.clothNode)
            cacheNode = deCmds.newNCacheFile(cacheFullPath, cacheFileName, sceneItem.clothNode, self.startTime,
                                             self.endTime, self.mainUi.displayState, self.cacheModeIndex)
        elif cacheMode == 'geo':
            shapeName = deCmds.getNodeShape(deCmds.getSelectedNodes()[0])
            cacheNode = deCmds.newGeoCacheFile(cacheFullPath, cacheFileName, shapeName, self.startTime,
                                               self.endTime, self.mainUi.displayState)
        else:
            cacheNode = None
        print "// Result: New cacheFile node ---> %s" % cacheNode
        self.cacheList.rf_cacheList()
        self.cacheList.ud_cacheAssigned()

    def on_appendToCache(self):
        """
        Command launched when 'Append To Cache' QPushButton is clicked
        """
        assigned = self.cacheList.assignedVersionItem
        last = self.cacheList.lastVersionItem
        if assigned is not None and last is not None:
            #-- Check assigned chached is last version --#
            if not assigned.cacheFileName == last.cacheFileName:
                mess = "!!! Assigned version %r doesn't match with last version %r !!!" % (assigned.cacheVersion,
                                                                                           last.cacheVersion)
                raise ValueError, mess
            #-- Append To Cache --#
            print "\n#===== Append To Cache =====#"
            cacheItem = assigned
            infoDict = cacheItem._widget.infoDict
            cachePath = os.path.dirname(os.path.normpath(cacheItem.cacheFullPath))
            cacheFile = os.path.basename(os.path.normpath(cacheItem.cacheFullPath)).split('.')[0]
            if infoDict['cacheType'] == 'nCloth':
                deCmds.appendToNCacheFile(cachePath, cacheFile, cacheItem.cacheNodeName, deCmds.getCurrentFrame(),
                                          self.endTime, self.mainUi.displayState, infoDict['cacheModeIndex'],
                                          backup=self.mainUi.backupState)
            else:
                raise AttributeError, "!!! Append To Cache works only with clothNodes !!!"

    def on_delCacheNode(self):
        """
        Command launched when 'Delete Cache Node' QPushButton is clicked
        """
        clothItem = self.sceneNodes.selectedClothItem
        deCmds.deleteCacheNode(clothItem.clothNode)

    def _checkCache(self, cacheMode):
        """
        Check launched before cache creation
        :param cacheMode: 'nCloth' or 'geo'
        :type cacheMode: str
        """
        print "Checking Cache Args ..."
        #-- check Cache Root Path --#
        if self.cacheList.cachePath is None:
            raise IOError, "!!! CacheRootPath is not set !!!"
        #-- Check Selected Item --#
        if self.sceneNodes.selectedClothItem is None:
            raise IOError, "!!! No ClothItem selected !!!"
        if cacheMode == 'nCloth':
            #-- Check Selected Cloth Type --#
            clothType = self.sceneNodes.selectedClothItem.clothType
            if not clothType in ['nCloth', 'nRigid']:
                raise IOError, "!!! ClothItem should be 'nCloth' or 'nRigid', got %s" % clothType
        elif cacheMode == 'geo':
            #-- Check Selected Mesh --#
            sel = deCmds.getSelectedNodes()
            if not len(sel) == 1:
                raise ValueError, "!!! Select only one mesh !!!"
            #-- Check Shape --#
            shapeName = deCmds.getNodeShape(sel[0])
            if shapeName is None:
                raise AttributeError, "!!! Invalid shape for %s !!!" % sel[0]

    def _mkNClothCacheDir(self, clothItem):
        """
        Make cache folders
        :param clothItem: Selected sceneNode item
        :type clothItem: QtGui.QTreeWidgetItem
        :return: Cache full path
        :rtype: str
        """
        print 'Creating nCloth Cache Folders ...'
        cacheRootPath = self.cacheList.cachePath
        cacheRelPath = self.sceneNodes.getRelativeCachePath(clothItem)
        print '\t ---> OverWrite Mode: %s' % str(self.overWriteMode)
        if self.overWriteMode:
            vFld = deCmds.getLastVersion(os.path.join(cacheRootPath, cacheRelPath))
        else:
            vFld = deCmds.getNextVersion(os.path.join(cacheRootPath, cacheRelPath))
        print '\t ---> Version:', vFld
        if vFld is None:
            raise IOError, "!!! No version found to replace !!!"
        cacheFullPath = pFile.conformPath(os.path.join(cacheRootPath, cacheRelPath, vFld))
        pFile.mkPathFolders(os.path.normpath(cacheRootPath), os.path.normpath(cacheFullPath))
        return cacheFullPath


class CacheListUi(QtGui.QWidget, wgCacheListUI.Ui_wgCacheList):
    """
    Widget CacheList, child of mainUi
    :param mainUi: ClothCache mainUi
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        print "\t ---> CacheListUi"
        self.mainUi = mainUi
        self.cachePath = None
        self.sceneNodes = self.mainUi.sceneNodes
        self.cacheInfo = None
        self.assignedIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'assigned.png'))
        self.tagOkIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'tagOk.png'))
        super(CacheListUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup widget ui
        """
        self.setupUi(self)
        self.cachePath = self.defaultCachePath
        self.twCaches.itemClicked.connect(self.on_cacheNodeSingleClick)
        self.twCaches.itemDoubleClicked.connect(self.on_cacheNodeDoubleClick)
        self.cbVersionOnly.clicked.connect(self.rf_fileVersions)
        self.rf_cachePath()

    @property
    def defaultCachePath(self):
        """
        Get default cache path
        :return: Default cache path
        :rtype: str
        """
        return "D:/rndBin/dynEval"

    @property
    def versionOnly(self):
        """
        Get version only state
        :return: Version only state
        :rtype: bool
        """
        return self.cbVersionOnly.isChecked()

    @property
    def lastVersionItem(self):
        """
        Get last cache version item
        :return: Last version item
        :rtype: QtGui.QTreeWidgetItem
        """
        allItems = pQt.getTopItems(self.twCaches)
        if allItems:
            return allItems[0]

    @property
    def assignedVersionItem(self):
        """
        Get assigned cache version item
        :return: Assigned version item
        :rtype: QtGui.QTreeWidgetItem
        """
        for item in pQt.getTopItems(self.twCaches):
            if item._widget.isAssigned():
                return item

    def rf_widgetToolTips(self):
        """
        Refresh all widget toolTip
        """
        if self.mainUi.toolTipState:
            self.leCachePath.setToolTip("Dyn Eval cache root path")
            self.cbVersionOnly.setToolTip("Show version number instead of cache file name")
        else:
            for widget in [self.leCachePath, self.cbVersionOnly]:
                widget.setToolTip("")

    def rf_cachePath(self):
        """
        Refresh cache root path
        """
        self.leCachePath.setText(self.cachePath)

    def rf_cacheList(self):
        """
        Refresh QTreeWidget 'Caches'
        """
        self.twCaches.clear()
        clothItem = self.sceneNodes.selectedClothItem
        if clothItem is not None and self.cachePath is not None:
            if clothItem.clothType in ['nCloth', 'nRigid']:
                #-- Get Cloth Item Info --#
                cacheRootPath = self.cachePath
                cacheRelPath = self.sceneNodes.getRelativeCachePath(clothItem)
                cacheFullPath = pFile.conformPath(os.path.join(cacheRootPath, cacheRelPath))
                #-- Get Cloth Item Versions --#
                cacheItems = []
                if os.path.exists(os.path.normpath(cacheFullPath)):
                    for fld in os.listdir(os.path.normpath(cacheFullPath)):
                        vPath = os.path.normpath(os.path.join(cacheFullPath, fld))
                        if os.path.isdir(vPath) and fld.startswith('v') and len(fld) == 4:
                            cacheFileName = '%s-%s-%s' % (clothItem.clothNs,
                                                          '_'.join(clothItem.clothName.split('_')[:-1]),
                                                          fld)
                            newItem = self.new_cacheItem(cacheRootPath, cacheRelPath, fld, cacheFileName,
                                                         clothItem.clothNode)
                            cacheItems.append(newItem)
                #-- Add Cache Versions --#
                if cacheItems:
                    cacheItems.reverse()
                    for cacheItem in cacheItems:
                        self.twCaches.addTopLevelItem(cacheItem)
                        self.twCaches.setItemWidget(cacheItem, 0, cacheItem._widget)
                    self.ud_cacheAssigned()

    def rf_fileVersions(self):
        """
        Update all cache file name label
        """
        for item in pQt.getTopItems(self.twCaches):
            self.rf_fileVersion(item)

    def rf_fileVersion(self, item):
        """
        Update given item cache file name label
        :param item: Cache version item
        :type item: QtGui.QTreeWidgetItem
        """
        if self.versionOnly:
            item._widget.lCacheFile.setText(item.cacheFileName.split('-')[-1])
        else:
            item._widget.lCacheFile.setText(item.cacheFileName)

    def ud_cacheAssigned(self):
        """
        Update cache assigned from maya scene
        """
        clothItem = self.sceneNodes.selectedClothItem
        if clothItem is not None:
            if clothItem.clothType in ['nCloth', 'nRigid']:
                cacheFileNodes = clothItem._widget.getConnectedCacheFileNodes()
                if cacheFileNodes:
                    cacheItem = None
                    for item in pQt.getTopItems(self.twCaches):
                        if item.cacheFileName.replace('-', '_') == cacheFileNodes[0].replace('dynEval_', ''):
                            cacheItem = item
                            break
                    if cacheItem is not None:
                        cacheItem._widget.pbAssign.setChecked(True)
                        cacheItem._widget.rf_cacheAssigned()

    def clearAssigned(self):
        """
        Uncheck all 'Cache Assigned' QPushButton
        """
        for item in pQt.getTopItems(self.twCaches):
            item._widget.pbAssign.setChecked(False)
            item._widget.rf_cacheAssigned()

    def on_cacheNodeSingleClick(self):
        """
        Command launched when 'CacheNode' QTreeWidgetItem is single clicked.
        Refresh cache file info.
        """
        selCacheItems = self.twCaches.selectedItems()
        if len(selCacheItems) == 1:
            if selCacheItems[0]._widget.infoDict is not None:
                notes = selCacheItems[0]._widget.infoDict['note']
                self.cacheInfo.cacheItem = selCacheItems[0]
                self.cacheInfo.teNotes.setText(notes)

    def on_cacheNodeDoubleClick(self):
        """
        Command launched when 'CacheNode' QTreeWidgetItem is double clicked.
        Assign selected cache file..
        """
        selCacheItems = self.twCaches.selectedItems()
        if len(selCacheItems) == 1:
            selCacheItems[0]._widget.on_cacheAssigned()

    def new_cacheItem(self, cacheRootPath, cacheRelPath, version, fileName, nodeName):
        """
        Create cache QTreeWidgetItem
        :param cacheRootPath: Cache root path
        :type cacheRootPath: str
        :param cacheRelPath: Cache relative path
        :type cacheRelPath: str
        :param version: Cache version folder
        :type: str
        :param fileName: Cache file name
        :type fileName: str
        :param nodeName: Node name attached to cacheNode
        :type nodeName: str
        :return: New cache item
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = QtGui.QTreeWidgetItem()
        newItem.cacheRootPath = cacheRootPath
        newItem.cacheRelPath = cacheRelPath
        newItem.cacheVersion = version
        newItem.cacheFileName = fileName
        newItem.cacheNodeName = nodeName
        newItem.cacheFullPath = pFile.conformPath(os.path.join(newItem.cacheRootPath, newItem.cacheRelPath,
                                                               newItem.cacheVersion, '%s.xml' % newItem.cacheFileName))
        newItem.cacheFileInfo = newItem.cacheFullPath.replace('.xml', '.py')
        newItem.cacheTagAsOk = False
        newItem._widget = CacheNode(self, newItem)
        return newItem


class CacheNode(QtGui.QWidget, wgCacheNodeUI.Ui_wgCacheNode):
    """
    Widget CacheNode QTreeWidgetItem, child of CacheListUi
    :param pWidget: Parent Widget
    :type pWidget: QtGui.QWidget
    :param pItem: Parent item
    :type pItem: QtGui.QTreeWidgetItem
    """

    def __init__(self, pWidget, pItem):
        self.pWidget = pWidget
        self.pItem = pItem
        self.mainUi = self.pWidget.mainUi
        self.infoDict = None
        super(CacheNode, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup widget ui
        """
        self.setupUi(self)
        if self.pWidget.versionOnly:
            self.lCacheFile.setText(self.pItem.cacheFileName.split('-')[-1])
        else:
            self.lCacheFile.setText(self.pItem.cacheFileName)
        self.pbAssign.clicked.connect(self.on_cacheAssigned)
        self.loadInfoDict()
        self.rf_pbCacheType()
        self.rf_cacheMode()

    def _popupMenu(self):
        """
        Setup popupMenu
        """
        self.cacheNodeMenu = QtGui.QMenu()
        # noinspection PyArgumentList
        self.cacheNodeMenu.popup(QtGui.QCursor.pos())
        #-- Add Menu Item --#
        self.miMaterialized = self.cacheNodeMenu.addAction('Materialize')
        self.miMaterialized.triggered.connect(self.on_miMaterializeCache)
        self.cacheNodeMenu.addSeparator()
        self.miDuplicate = self.cacheNodeMenu.addAction('Duplicate')
        self.miDuplicate.triggered.connect(self.on_miDuplicateCache)
        self.cacheNodeMenu.addSeparator()
        self.miAssignToSel = self.cacheNodeMenu.addAction('Assign To Selected')
        self.miAssignToSel.triggered.connect(self.on_miAssignToSel)
        self.cacheNodeMenu.addSeparator()
        self.miDelete = self.cacheNodeMenu.addAction('Delete')
        self.miDelete.triggered.connect(self.on_miDeleteCache)
        #-- Exec Menu --#
        self.rf_popupMenuVisibility()
        self.cacheNodeMenu.exec_()

    def loadInfoDict(self):
        """
        Load cache info file
        """
        if not os.path.exists(os.path.normpath(self.pItem.cacheFullPath)):
            self.pbCacheType.setStyleSheet('background-color: rgb(200, 0, 0)')
        if not os.path.exists(os.path.normpath(self.pItem.cacheFileInfo)):
            self.pbCacheType.setStyleSheet('background-color: rgb(100, 0, 0)')
        else:
            self.infoDict = pFile.readPyFile(self.pItem.cacheFileInfo)

    def isAssigned(self):
        """
        Get cacheNode assigned state
        :return: Assigned state
        :rtype: bool
        """
        return self.pbAssign.isChecked()

    def rf_pbCacheType(self):
        """
        Refresh cache type QPushButton
        """
        if self.infoDict is not None:
            if self.infoDict['cacheType'] == 'nCloth':
                self.pbCacheType.setStyleSheet('background-color: rgb(0, 200, 200)')
            else:
                self.pbCacheType.setStyleSheet('background-color: rgb(50, 100, 255)')

    def rf_cacheMode(self):
        """
        Refresh cache mode QLabel
        """
        if self.infoDict is not None:
            cMode = self.infoDict['cacheModeIndex']
            if cMode == 0:
                self.lCacheAttr.setText('P')
            elif cMode == 1:
                self.lCacheAttr.setText('V')
            elif cMode == 2:
                self.lCacheAttr.setText('IS')

    def rf_cacheAssigned(self):
        """
        Refresh cache file assigned state icon
        """
        if self.pbAssign.isChecked():
            self.pbAssign.setIcon(self.pWidget.assignedIcon)
        else:
            self.pbAssign.setIcon(QtGui.QIcon())

    def rf_popupMenuVisibility(self):
        """
        Refresh popup menu item visibility
        """
        selItems = self.pWidget.twCaches.selectedItems()
        if not selItems:
            self.miDuplicate.setEnabled(False)
            self.miMaterialized.setEnabled(False)
            self.miAssignToSel.setEnabled(False)
            self.miDelete.setEnabled(False)
        else:
            if len(selItems) == 1:
                self.miDuplicate.setEnabled(True)
                self.miMaterialized.setEnabled(True)
                self.miAssignToSel.setEnabled(True)
                self.miDelete.setEnabled(True)
            else:
                self.miDuplicate.setEnabled(False)
                self.miMaterialized.setEnabled(False)
                self.miAssignToSel.setEnabled(False)
                self.miDelete.setEnabled(True)

    def on_cacheAssigned(self):
        """
        Command launched when 'Assigned' QPushButton is clicked.
        Assign cache version
        """
        print "Assigning %r to %r ..." % (self.pItem.cacheFileName, self.pItem.cacheNodeName)
        self.pWidget.clearAssigned()
        cachePath = pFile.conformPath(os.path.join(self.pItem.cacheRootPath, self.pItem.cacheRelPath,
                                                   self.pItem.cacheVersion))
        cacheNode = deCmds.assignNCacheFile(cachePath, self.pItem.cacheFileName, self.pItem.cacheNodeName,
                                            self.pItem._widget.infoDict['cacheModeIndex'])
        self.pbAssign.setChecked(True)
        self.rf_cacheAssigned()
        print "// Result: New cacheFile node ---> %s" % cacheNode

    def on_miMaterializeCache(self):
        """
        Command launched when 'Materialize' QMenuItem is triggered.
        Materialize cache version
        """
        #-- Check --#
        if not os.path.exists(os.path.normpath(self.pItem.cacheFullPath)):
            raise IOError, "!!! Cache file not found: %s !!!" % self.pItem.cacheFullPath
        #-- Materialize Version --#
        print "\n#===== Materialize Cache File =====#"
        print 'Materialize %s' % self.pItem.cacheFileName
        clothItem = self.pWidget.sceneNodes.selectedClothItem
        cachePath = '/'.join(self.pItem.cacheFullPath.split('/')[:-1])
        cacheFile = self.pItem.cacheFullPath.split('/')[-1]
        cacheNode = deCmds.materializeCacheVersion(cachePath, cacheFile, clothItem.clothMesh)
        print "// Result: New cacheFile node ---> %s" % cacheNode

    def on_miDuplicateCache(self):
        """
        Command launched when 'Duplicate' QMenuItem is triggered.
        Duplicate cache version
        """
        #-- Check --#
        if not os.path.exists(os.path.normpath(self.pItem.cacheFullPath)):
            raise IOError, "!!! Cache file not found: %s !!!" % self.pItem.cacheFullPath
        #-- Duplicate Version --#
        print "\n#===== Duplicate Cache File =====#"
        print 'Duplicate %s' % self.pItem.cacheFileName
        cachePath = '/'.join(self.pItem.cacheFullPath.split('/')[:-2])
        cacheVersion = self.pItem.cacheFullPath.split('/')[-2]
        deCmds.duplicateCacheVersion(cachePath, cacheVersion)
        #-- Refresh Ui --#
        self.pWidget.rf_cacheList()
        self.pWidget.lastVersionItem._widget.on_cacheAssigned()

    def on_miAssignToSel(self):
        """
        Command launched when 'AssignToSel' QMenuItem is triggered.
        Assign cache version to selected mesh
        """
        #-- Check --#
        if not os.path.exists(os.path.normpath(self.pItem.cacheFullPath)):
            raise IOError, "!!! Cache file not found: %s !!!" % self.pItem.cacheFullPath
        #-- Assign Version --#
        print "\n#===== Assign Cache File =====#"
        print 'Assign %s' % self.pItem.cacheFileName
        cachePath = '/'.join(self.pItem.cacheFullPath.split('/')[:-1])
        cacheFile = self.pItem.cacheFullPath.split('/')[-1]
        cacheNode = deCmds.assignCacheFileToSel(cachePath, cacheFile)
        print "// Result: New cacheFile node ---> %s" % cacheNode

    def on_miDeleteCache(self):
        """
        Command launched when 'Delete' QMenuItem is triggered.
        Delete cache files version
        """
        #-- Get Selected Versions --#
        print "\n#===== Delete Cache File =====#"
        selItems = self.pWidget.twCaches.selectedItems()
        for item in selItems:
            cachePath = os.path.dirname(item.cacheFullPath)
            #-- Check --#
            if not os.path.exists(os.path.normpath(cachePath)):
                raise IOError, "!!! Cache version not found: %s !!!" % item.cacheFileName
            #-- Delete Version --#
            print 'Delete %s' % item.cacheFileName
            deCmds.deleteCacheVersion(cachePath)
        self.pWidget.rf_cacheList()

    def mouseReleaseEvent(self, event):
        """
        Add mouse press options: 'Right' = Popup cacheNode menu
        """
        if event.button() == QtCore.Qt.RightButton:
            self._popupMenu()
        super(CacheNode, self).mousePressEvent(event)


class CacheInfoUi(QtGui.QWidget, wgCacheInfoUI.Ui_wgCacheInfo):
    """
    Widget CacheInfo, child of mainUi
    :param mainUi: ClothCache mainUi
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        print "\t ---> CacheInfoUi"
        self.mainUi = mainUi
        self.cacheItem = None
        self.textEditIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'textEdit.png'))
        super(CacheInfoUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup widget ui
        """
        self.setupUi(self)
        self.pbEditNotes.setIcon(self.textEditIcon)
        self.pbEditNotes.clicked.connect(self.on_editNotes)

    def clearInfos(self):
        """
        Clear widget info
        """
        self.cacheItem = None
        self.teNotes.clear()

    def rf_widgetToolTips(self):
        """
        Refresh all widget toolTip
        """
        if self.mainUi.toolTipState:
            self.pbEditNotes.setToolTip("Save comment to cache file info")
        else:
            for widget in [self.pbEditNotes]:
                widget.setToolTip("")

    def on_editNotes(self):
        """
        Command launched when 'Edit Notes' QPushButton is clicked.
        Update cache file info notes
        """
        if self.cacheItem is not None:
            infoDict = self.cacheItem._widget.infoDict
            if infoDict is not None:
                fileInfo = self.cacheItem.cacheFileInfo
                #-- Check file info --#
                if not os.path.exists(os.path.normpath(fileInfo)):
                    raise IOError, "!!! File info not found for text edition !!!"
                #-- Update tmp file info --#
                print "Editing cache notes ..."
                infoDict['note'] = str(self.teNotes.toPlainText())
                txt = []
                for k, v in infoDict.iteritems():
                    if isinstance(v, str):
                        txt.append('%s = "%s"' % (k, v))
                    else:
                        txt.append('%s = %s' % (k, v))
                #-- Write file info --#
                try:
                    print "Writing file info ..."
                    pFile.writeFile(os.path.normpath(fileInfo), str('\n'.join(txt)))
                except:
                    raise IOError, "!!! Can not write file info: %s !!!" % fileInfo
                #-- Reload cache file info --#
                self.cacheItem._widget.loadInfoDict()
