import os
from PyQt4 import QtGui
from functools import partial
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

    def rf_label(self):
        """
        Refresh label text and color
        """
        newFont = QtGui.QFont()
        newFont.setBold(True)
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
        print "#===== Create Cache =====#"
        if cacheMode == 'nCloth':
            self._checkNClothCache()
            clothItem = self.sceneNodes.selectedClothItem
            cacheFullPath = self._mkNClothCacheDir(clothItem)
            cacheFileName = '%s-%s-%s' % (clothItem.clothNs, '_'.join(clothItem.clothName.split('_')[:-1]),
                                          cacheFullPath.split('/')[-1])
            deCmds.delCacheNode(clothItem.clothNode)
            cacheNode = deCmds.newNCacheFile(cacheFullPath, cacheFileName, clothItem.clothNode, self.startTime,
                                             self.endTime, self.mainUi.displayState, self.cacheModeIndex)
            print "New cacheFile node:", cacheNode

    def on_delCacheNode(self):
        """
        Command launched when 'Delete Cache Node' QPushButton is clicked
        """
        clothItem = self.sceneNodes.selectedClothItem
        deCmds.delCacheNode(clothItem.clothNode)

    def _checkNClothCache(self):
        """
        Check launched before cache creation
        """
        print "Checking Cache Args ..."
        #-- check Cache Root Path --#
        if self.cacheList.cachePath is None:
            raise IOError, "!!! CacheRootPath is not set !!!"
        #-- Check Selected Item --#
        if self.sceneNodes.selectedClothItem is None:
            raise IOError, "!!! No ClothItem selected !!!"
        #-- Check Selected Cloth Type --#
        clothType = self.sceneNodes.selectedClothItem.clothType
        if not clothType in ['nCloth', 'nRigid']:
            raise IOError, "!!! ClothItem should be 'nCloth' or 'nRigid', got %s" % clothType

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
        super(CacheListUi, self).__init__()
        self._setupUi()

    def _setupUi(self):
        """
        Setup widget ui
        """
        self.setupUi(self)
        self.cachePath = self.defaultCachePath
        self.rf_cachePath()

    @property
    def defaultCachePath(self):
        """
        Get default cache path
        :return: Default cache path
        :rtype: str
        """
        return "D:/rndBin/dynEval"

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
                            newItem = self.new_cacheItem(cacheRootPath, cacheRelPath, fld, cacheFileName)
                            cacheItems.append(newItem)
                #-- Add Cache Versions --#
                if cacheItems:
                    for cacheItem in cacheItems:
                        self.twCaches.addTopLevelItem(cacheItem)
                        self.twCaches.setItemWidget(cacheItem, 0, cacheItem._widget)

    def new_cacheItem(self, cacheRootPath, cacheRelPath, version, fileName):
        """
        Create cache QTreeWidgetItem
        :param cacheRootPath: Cache root path
        :type cacheRootPath: str
        :param cacheRelPath: Cache relative path
        :type cacheRelPath: str
        :param version: Cache version folder
        :type: str
        :return: New cache item
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = QtGui.QTreeWidgetItem()
        newItem.cacheRootPath = cacheRootPath
        newItem.cacheRelPath = cacheRelPath
        newItem.cacheVersion = version
        newItem.cacheFileName = fileName
        newItem.cacheFullPath = pFile.conformPath(os.path.join(newItem.cacheRootPath, newItem.cacheRelPath,
                                                               newItem.cacheVersion, '%s.xml' % newItem.cacheFileName))
        newItem.cacheFileInfo = newItem.cacheFullPath.replace('.xml', '.py')
        newItem.cacheType = pFile.readPyFile(newItem.cacheFileInfo)['cacheType']
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
        super(CacheNode, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup widget ui
        """
        self.setupUi(self)
        self.lCacheFile.setText(self.pItem.cacheFileName)
        self.rf_pbCacheType()

    def rf_pbCacheType(self):
        """
        Refresh cache type QPushButton
        """
        #-- Check File Existence --#
        if not os.path.exists(os.path.normpath(self.pItem.cacheFullPath)):
            self.pbCacheType.setStyleSheet('background-color: rgb(200, 0, 0)')
            return False
        if not os.path.exists(os.path.normpath(self.pItem.cacheFileInfo)):
            self.pbCacheType.setStyleSheet('background-color: rgb(100, 0, 0)')
            return False
        #-- Refresh --#
        infoDict = pFile.readPyFile(self.pItem.cacheFileInfo)
        if infoDict['cacheType'] == 'nCloth':
            self.pbCacheType.setStyleSheet('background-color: rgb(0, 200, 200)')
        else:
            self.pbCacheType.setStyleSheet('background-color: rgb(50, 100, 255)')
        return True



class CacheInfoUi(QtGui.QWidget, wgCacheInfoUI.Ui_wgCacheInfo):
    """
    Widget CacheInfo, child of mainUi
    :param mainUi: ClothCache mainUi
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        print "\t ---> CacheInfoUi"
        self.mainUi = mainUi
        super(CacheInfoUi, self).__init__()
        self._setupUi()

    def _setupUi(self):
        """
        Setup widget ui
        """
        self.setupUi(self)
