import os, sys
from PyQt4 import QtGui
from lib.qt import preview
from lib.env import studio
from functools import partial
from lib.qt import procQt as pQt
from appli.factory import factory
from lib.system import procFile as pFile
from appli.factory.ui import factoryUI, wgtThumbnailUI, dialTransfertUI


class FactoryUi(QtGui.QMainWindow, factoryUI.Ui_factory, pQt.Style):
    """ FactoryUi MainWindow
        :param logLvl : ('critical', 'error', 'warning', 'info', 'debug')
        :type logLvl: str """

    def __init__(self, parent=None, logLvl='info'):
        self.log = pFile.Logger(title="Factory-UI", level=logLvl)
        self.log.info("#-- Launching Factory --#")
        self.factory = factory.Factory()
        if parent is None:
            self.inMaya = False
        else:
            self.inMaya = True
        super(FactoryUi, self).__init__(parent)
        self._setupUi()
        self.rf_tree()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup main ui """
        self.log.debug("#-- Setup Factory Ui --#")
        self.setupUi(self)
        self.setStyleSheet(self.applyStyle(styleName='darkOrange'))
        self.miClearTexture.triggered.connect(partial(self.on_clear, self.twTexture))
        self.miClearShader.triggered.connect(partial(self.on_clear, self.twShader))
        self.miClearStockShot.triggered.connect(partial(self.on_clear, self.twStockShot))
        self.miStoredTexture.triggered.connect(partial(self.on_transfert, self.twTexture))
        self.miStoredShader.triggered.connect(partial(self.on_transfert, self.twShader))
        self.miStoredStockShot.triggered.connect(partial(self.on_transfert, self.twStockShot))
        self.mThumbnail.aboutToShow.connect(self.rf_thumbnailMenu)
        self.miCreateSelPreviewFiles.triggered.connect(partial(self.on_createPreviewFiles, 'sel'))
        self.miCreateAllPreviewFiles.triggered.connect(partial(self.on_createPreviewFiles, 'all'))
        self.miCreateSelMovies.triggered.connect(partial(self.on_createMovieFile, 'sel'))
        self.miCreateAllMovies.triggered.connect(partial(self.on_createMovieFile, 'all'))
        self.wgPreview = Preview(self)
        self.vlLeftZone.insertWidget(0, self.wgPreview)
        self.rbTexture.clicked.connect(self.on_switch)
        self.rbShader.clicked.connect(self.on_switch)
        self.rbStockShot.clicked.connect(self.on_switch)
        self.twTree.itemClicked.connect(self.rf_thumbnail)
        self.twTexture.itemClicked.connect(partial(self.on_storageItem, 'texture'))
        self.twShader.itemClicked.connect(partial(self.on_storageItem, 'shader'))
        self.twStockShot.itemClicked.connect(partial(self.on_storageItem, 'stockShot'))
        self.sbColumns.editingFinished.connect(self.rf_thumbnail)
        self.cbStorage.clicked.connect(self.on_showStorage)
        if not self.inMaya:
            self.tabShader.deleteLater()

    def rf_tree(self):
        """ Refresh factory tree """
        self.twTree.clear()
        treeNode = getattr(self.factory, self.getSelTree())
        if treeNode is not None:
            for node in getattr(treeNode, 'tree'):
                newItem = self._newTreeItem(node)
                self.twTree.addTopLevelItem(newItem)
                for child in node._children:
                    newChild = self._newTreeItem(child)
                    newItem.addChild(newChild)

    def rf_thumbnail(self):
        """ Refresh factory thumbnail """
        self.twThumbnail.clear()
        self.rf_thumbnailColumns()
        selTreeItems = self.twTree.selectedItems()
        if selTreeItems:
            node = selTreeItems[0].node
            if node.nodeType == 'subCategory':
                NC = self.twThumbnail.columnCount()
                nc = 0
                for child in node._children:
                    if nc == 0:
                        newItem = self._newThumbnailItem()
                        self.twThumbnail.addTopLevelItem(newItem)
                    newPreview = Thumbnail(self, newItem, child)
                    newItem._widgets.append(newPreview)
                    self.twThumbnail.setItemWidget(newItem, nc, newPreview)
                    if self.getStorageItem(self.getStorageTree(), child.nodePath):
                        newPreview.cbPreview.setChecked(True)
                    nc += 1
                    if nc == NC:
                        nc = 0

    def rf_thumbnailMenu(self):
        """ Refresh thumbnail menu """
        self.miCreateSelPreviewFiles.setEnabled(False)
        self.miCreateAllPreviewFiles.setEnabled(False)
        self.miCreateSelMovies.setEnabled(False)
        self.miCreateAllMovies.setEnabled(False)
        selItems = self.twTree.selectedItems()
        if selItems:
            if selItems[0].node.nodeType == 'subCategory':
                self.miCreateAllPreviewFiles.setEnabled(True)
                if self.getSelTree() == 'stockShot':
                    self.miCreateAllMovies.setEnabled(True)
                else:
                    self.miCreateAllMovies.setEnabled(False)
                if self.getSelThumbnails():
                    self.miCreateSelPreviewFiles.setEnabled(True)
                    if self.getSelTree() == 'stockShot':
                        self.miCreateSelMovies.setEnabled(True)
                    else:
                        self.miCreateSelMovies.setEnabled(False)

    def rf_thumbnailColumns(self):
        """ Refresh factory thumbnail columns """
        self.twThumbnail.setColumnCount(self.sbColumns.value())
        for n in range(self.twThumbnail.columnCount()):
            self.twThumbnail.header().setResizeMode(n, QtGui.QHeaderView.ResizeToContents)

    def on_clear(self, storageTree):
        """ Clear given storage tree
            :param storageTree: object) : QTreeWidget """
        storageTree.clear()
        self.rf_thumbnail()

    def on_transfert(self, storageTree):
        """ Launch transfert dialog
            :param storageTree: (object) : QTreeWidget """
        dt = Transfert(self, storageTree)
        dt.exec_()

    def on_createPreviewFiles(self, mode):
        """ Command launched when 'Create Preview Files' menuItems are clicked
            :param mode: (str) : 'sel' or 'all' """
        if mode == 'sel':
            wList = self.getSelThumbnails()
        else:
            wList = self.getAllThumbnails()
        for w in wList:
            self.log.info("\n")
            self.log.info("#-- Create Preview Files %s --#" % w.node.nodeName)
            self.factory.ud_thumbnailImages(w.node.nodePath, 'icon')
            self.factory.ud_thumbnailImages(w.node.nodePath, 'preview')
            if not self.getSelTree() == 'shader':
                self.factory.ud_thumbnailDatas(w.node.nodePath, self.getSelTree())

    def on_createMovieFile(self, mode):
        """ Command launched when 'Create Movie File' menuItems are clicked
            :param mode: (str) : 'sel' or 'all' """
        if mode == 'sel':
            wList = self.getSelThumbnails()
        else:
            wList = self.getAllThumbnails()
        for w in wList:
            self.log.info("\n")
            self.log.info("#-- Create Movie File %s --#" % w.node.nodeName)
            pathIn = os.path.join(os.path.dirname(w.node.nodePath), 'seq', w.node.nodeName)
            pathOut = os.path.join(os.path.dirname(w.node.nodePath), 'mov')
            frame = '%04d'
            fileIn = os.path.join(pathIn, "%s.%s.jpg" % (w.node.nodeName, frame))
            fileOut = os.path.join(pathOut, "%s.mov" % w.node.nodeName)
            self.factory.ud_movie(os.path.normpath(fileIn), os.path.normpath(fileOut))

    def on_switch(self):
        """ Command launched when treeSwitch QRadioButton is clicked """
        tree = getattr(self.factory, self.getSelTree())
        self.factory.parseTree(tree)
        self.rf_tree()
        self.rf_thumbnail()

    def on_showStorage(self):
        """ Command launched when 'Storage' QCheckBox is clicked """
        self.qfRightZone.setVisible(self.cbStorage.isChecked())

    def on_storageItem(self, treeName):
        """ Command lanched when 'Storage Item' is clicked
            :param treeName: (str) : 'texture', 'shader' or 'stockShot' """
        twTree = self.getStorageTreeFromName(treeName)
        selItem = twTree.selectedItems()[0]
        self.setTree(treeName)
        item = self.getTreeItem(selItem.nodePath)
        item.setSelected(True)
        self.twTree.setCurrentItem(item)
        self.rf_thumbnail()

    @staticmethod
    def _newTreeItem(node):
        """ Create new treeItem
            :param node: (object) : Factory node
            :return: (object) : QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem.setText(0, node.nodeName)
        newItem.node = node
        return newItem

    @staticmethod
    def _newThumbnailItem():
        """ Create new thumbnailItem
            :return: (object) : QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem._widgets = []
        return newItem

    @staticmethod
    def _newStorageItem(node):
        """ Create new storage treeItem
            :param node: (object) : Factory node
            :return: (object) : QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem.setText(0, node.nodeName)
        newItem.nodePath = node.nodePath
        newItem.nodeName = node.nodeName
        return newItem

    def getSelTree(self):
        """ Get selected tree
            :return: (str) : Selected tree """
        if self.rbTexture.isChecked():
            return 'texture'
        elif self.rbShader.isChecked():
            return 'shader'
        elif self.rbStockShot.isChecked():
            return 'stockShot'

    def setTree(self, treeName):
        """ Set selected tree
            :param treeName: (str) : Tree name """
        if treeName == 'texture':
            self.rbTexture.setChecked(True)
        elif treeName == 'shader':
            self.rbShader.setChecked(True)
        elif treeName == 'stockShot':
            self.rbStockShot.setChecked(True)
        self.on_switch()

    def getTreeItem(self, nodePath):
        """ Get treeItem from given nodePath
            :param nodePath: (str) : Node absolute path
            :return: (object) : QTreeWidgetItem """
        allItems = pQt.getAllItems(self.twTree)
        for item in allItems:
            if item.node.nodeType == 'subCategory' and item.node.nodePath == os.path.dirname(nodePath):
                return item

    def getAllThumbnails(self):
        """ Get all thumbnail widgets
            :return: (list) : Thumbnail QWidgets list """
        allItems = pQt.getTopItems(self.twThumbnail)
        allWidgets = []
        for item in allItems:
            for w in item._widgets:
                allWidgets.append(w)
        return allWidgets

    def getSelThumbnails(self):
        """ Get selected thumbnail widgets
            :return: (list) : Thumbnail QWidgets list """
        selWidgets = []
        for w in self.getAllThumbnails():
            if w.cbPreview.isChecked():
                selWidgets.append(w)
        return selWidgets

    def getStorageTree(self):
        """ Get storage QTreeWidget from selected tree
            :return: (object) : QTreeWidget """
        if self.getSelTree() == 'texture':
            return self.twTexture
        elif self.getSelTree() == 'shader':
            return self.twShader
        elif self.getSelTree() == 'stockShot':
            return self.twStockShot

    def getStorageTreeFromName(self, treeName):
        """ Get storage QTreeWidget from given treeName
            :return: (object) : QTreeWidget """
        if treeName == 'texture':
            return self.twTexture
        elif treeName == 'shader':
            return self.twShader
        elif treeName == 'stockShot':
            return self.twStockShot

    @staticmethod
    def getStorageItem(twTree, nodePath):
        """ Get storage item from given storageTree and nodePath
            :param twTree: (object) : QTreeWidgetItem
            :param nodePath: (str) : Node absolute path
            :return: (object) : QTreeWidgetItem """
        allItems = pQt.getTopItems(twTree)
        for item in allItems:
            if item.nodePath == nodePath:
                return item


class Thumbnail(QtGui.QWidget, wgtThumbnailUI.Ui_thumbnail):
    """ Thumbnail widget
        :param mainUi : (object) : QMainWindow
        :param item : (object) : QTreeWidgetItem
        :param node : (object) : Factory.node """

    def __init__(self, mainUi, item, node):
        self.mainUi = mainUi
        self.noImage = os.path.join(self.mainUi.factory.libPath, 'ima', 'noImage_100.jpg')
        self._item = item
        self.node = node
        super(Thumbnail, self).__init__()
        self._setupUi()

    @property
    def iconFile(self):
        """ Get icon file
            :return: (str) : Icon absolute path """
        iconPath = os.path.join(os.path.dirname(self.node.nodePath), '_icon')
        return pFile.conformPath(os.path.join(iconPath, '%s.png' % self.node.nodeName))

    @property
    def previewFile(self):
        """ Get preview file
            :return: (str) : Preview absolute path """
        previewPath = os.path.join(os.path.dirname(self.node.nodePath), '_preview')
        return pFile.conformPath(os.path.join(previewPath, '%s.png' % self.node.nodeName))

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget """
        self.setupUi(self)
        self.bPreview.clicked.connect(self.on_icon)
        self.cbPreview.clicked.connect(self.on_selBox)
        self.rf_icon()

    def rf_icon(self):
        """ Refresh thumbnail icon """
        self.lName.setText(self.node.nodeName)
        #-- Icone --#
        if not os.path.exists(self.iconFile):
            self.bPreview.setIcon(QtGui.QIcon(self.noImage))
        else:
            self.bPreview.setIcon(QtGui.QIcon(self.iconFile))
        #-- Preview --#
        if not os.path.exists(self.previewFile):
            self.cbPreview.setText("No Preview")
        else:
            self.cbPreview.setText("")

    def rf_info(self):
        """ Refresh file info """
        if self.node.datas is not None:
            self.mainUi.teInfo.setText(self.node.datasString)
        else:
            self.mainUi.teInfo.clear()

    def rf_preview(self):
        """ Refresh factory preview """
        if os.path.exists(self.previewFile):
            self.mainUi.wgPreview.previewFile = self.previewFile
            self.mainUi.wgPreview.imagePath = self.node.nodePath
        else:
            self.mainUi.wgPreview.previewFile = None
            self.mainUi.wgPreview.imagePath = None
        if self.node.hasMovie():
            self.mainUi.wgPreview.moviePath = self.node.movieFile
        else:
            self.mainUi.wgPreview.moviePath = None
        if self.node.hasSequence():
            path = os.path.join(self.node.sequencePath, "%s.####.jpg" % self.node.nodeName)
            self.mainUi.wgPreview.sequencePath = path
        else:
            self.mainUi.wgPreview.sequencePath = None
        self.mainUi.wgPreview.rf_preview()
        self.mainUi.wgPreview.rf_btnsVisibility()

    def on_icon(self):
        """ Command launched when thumbnail icon is clicked """
        self.rf_info()
        self.rf_preview()

    def on_selBox(self):
        """ Command launched when thumbnail QCheckBox is clicked """
        twTree = self.mainUi.getStorageTree()
        if self.cbPreview.isChecked():
            newItem = self.mainUi._newStorageItem(self.node)
            twTree.addTopLevelItem(newItem)
        else:
            storageItem = self.mainUi.getStorageItem(twTree, self.node.nodePath)
            twTree.takeTopLevelItem(twTree.indexOfTopLevelItem(storageItem))


class Preview(preview.Preview):
    """ Factory preview widget
        :param mainUi : (object) : QMainWindow """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        super(Preview, self).__init__(widgetSize=(250, 250), previewSize=(245, 245))
        self._setupWidget()

    def _setupWidget(self):
        """ Setup widget """
        self.qfButtonsDn.setVisible(False)
        self.bImage.setEnabled(False)
        self.bSequence.setEnabled(False)
        self.bMovie.setEnabled(False)


class Transfert(QtGui.QDialog, dialTransfertUI.Ui_transfert, pQt.Style):
    """ Factory transfert dialog
        :param mainUi: (objec) : QMainWindow
        :param storageTree: (object) : QTreeWidget """

    def __init__(self, mainUi, storageTree):
        self.mainUi = mainUi
        self.storageTree = storageTree
        super(Transfert, self).__init__()
        self._setupUi()
        self.on_tmpFolder()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        self.setupUi(self)
        self.setStyleSheet(self.applyStyle(styleName='darkOrange'))
        self.lTransfert.setText("Transfert %s:" % self.storageTree.objectName().replace('tw', ''))
        self.bOpen.clicked.connect(self.on_open)
        self.cbTmpFolder.clicked.connect(self.on_tmpFolder)
        self.bTransfert.clicked.connect(self.on_transfert)
        self.bCancel.clicked.connect(self.close)

    def on_open(self):
        """ Command launched when 'Open' QPushButton is clicked """
        self.fdPath = pQt.fileDialog(fdRoot=studio.prodPath, fdFileMode='DirectoryOnly', fdCmd=self.ud_path)
        self.fdPath.exec_()

    def on_tmpFolder(self):
        """ Command launched when 'TmpFolder' QCheckBox is clicked """
        if self.cbTmpFolder.isChecked():
            self.leTmpFolder.setEnabled(True)
        else:
            self.leTmpFolder.setEnabled(False)

    def on_transfert(self):
        """ Command launched when 'Transfert' QPushButton is clicked """
        if not self._checkDest():
            raise IOError, "Destination path doesn't exist: %s" % str(self.leDestination.text())
        if not self.getStoredItems():
            raise IOError, "No item found in %s" % self.storageTree.objectName()
        destPath = self._checkTmpFolder()
        if destPath is not None:
            for item in self.getStoredItems():
                if self.storageTree.objectName() == 'twTexture':
                    self.mainUi.factory.transfertTexture(item.nodePath, destPath)
                elif self.storageTree.objectName() == 'twShader':
                    self.log.info("Command in DEV")
                elif self.storageTree.objectName() == 'twStockShot':
                    self.mainUi.factory.transfertStockShot(item.nodePath, destPath)

    def ud_path(self):
        """ Update path widget """
        selPath = self.fdPath.selectedFiles()
        if selPath:
            self.leDestination.setText(str(selPath[0]))

    def getStoredItems(self):
        """ Get QTreeWidgetItems
            :return: (list) : List of QTreeWidgetItems """
        return pQt.getAllItems(self.storageTree)

    def _checkDest(self):
        """ Check if destination path is valid
            :return: (bool) : True if exists, else False """
        dest = str(self.leDestination.text())
        if dest not in ['', ' ']:
            if os.path.exists(dest):
                return True
            else:
                return False
        else:
            return False

    def _checkTmpFolder(self):
        """ Create tmp folder if needed
            :return: (str) : Destination path """
        destPath = str(self.leDestination.text())
        if self.cbTmpFolder.isChecked():
            tmpPath = str(self.leTmpFolder.text())
            if not tmpPath in ['', ' ']:
                for fld in tmpPath.split('/'):
                    destPath = pFile.conformPath(os.path.join(destPath, fld))
                    if not os.path.exists(destPath):
                        self.mainUi.log.info("Create Tmp folder %s" % fld)
                        try:
                            os.mkdir(destPath)
                        except:
                            raise IOError, "Can not create folder %s: %s" % (fld, destPath)
        return destPath



def launch(logLvl='info'):
    """ Factory launcher
        :param logLvl: (str) : Log level ('critical', 'error', 'warning', 'info', 'debug') """
    app = QtGui.QApplication(sys.argv)
    window = FactoryUi(logLvl=logLvl)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch(logLvl='debug')
