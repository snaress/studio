import os, shutil, pprint
from PyQt4 import QtGui
from functools import partial
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.grapher.gui.ui import wgBankUI


class Bank(QtGui.QWidget, wgBankUI.Ui_wgBank):
    """
    Grapher bank QWidget, child of mainUi

    :param mainUi: Grapher main window
    :type mainUi: GrapherUi
    """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.detail("\t ---> Init Bank Widget.")
        self.graphTree = self.mainUi.graphZone.graphTree
        super(Bank, self).__init__()
        self._setupWidget()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        self.log.detail("\t ---> Setup Bank Widget.")
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        #-- Text Font --#
        scriptFont = QtGui.QFont('Courier', 8, QtGui.QFont.Monospace)
        scriptFont.setFixedPitch(True)
        metrics = QtGui.QFontMetrics(scriptFont)
        for wg in [self.teComment, self.teRequires, self.teScript]:
            wg.setTabStopWidth(4 * metrics.width(' '))
            wg.setFont(scriptFont)
        #-- Tree --#
        self.pbRefresh.clicked.connect(self.on_refresh)
        self.twTree.clicked.connect(self.on_treeItem)
        self.pbSendToGraph.clicked.connect(self.on_sendToGraph)
        self.cbScript.clicked.connect(self.rf_itemVisibility)
        self.cbScript.setStyleSheet("color: rgb(0, 80, 255)")
        self.cbNode.clicked.connect(self.rf_itemVisibility)
        self.cbNode.setStyleSheet("color: rgb(0, 170, 0)")
        self.cbBranch.clicked.connect(self.rf_itemVisibility)
        self.cbBranch.setStyleSheet("color: rgb(180, 120, 120)")
        #-- Edition --#
        self.pbEdit.clicked.connect(self.rf_editMode)
        self.pbExplorer.clicked.connect(self.on_xPlorer)
        self.pbAddFolder.clicked.connect(partial(self.on_add, addType='folder'))
        self.pbAddScript.clicked.connect(partial(self.on_add, addType='script'))
        self.pbAddNode.clicked.connect(partial(self.on_add, addType='node'))
        self.pbAddBranch.clicked.connect(partial(self.on_add, addType='branch'))
        self.pbDelSelFile.clicked.connect(self.on_delSelFile)
        self.pbDelSelFolder.clicked.connect(self.on_delSelFolder)
        self.pbSave.clicked.connect(self.on_save)
        self.pbCancel.clicked.connect(self.updateInfo)
        #-- Refresh --#
        self.rf_editMode()
        self.rf_tree()
        self.rf_infoVisibility()

    def getTreeItemFromPath(self, pathType, path):
        """
        Get tree item from given pathType and path

        :param pathType: 'relPath' or 'fullPath'
        :type pathType: str
        :param path: Path
        :type path: str
        :return: Tree item matching given path
        :rtype: QtGui.QTreeWidgetItem
        """
        for item in pQt.getAllItems(self.twTree):
            if getattr(item, pathType) == path:
                return item

    def getScriptDatas(self, asString=False):
        """
        Get script datas

        :param asString: Return string instead of dict
        :type asString: bool
        :return: Script datas
        :rtype: dict | str
        """
        #-- get Datas --#
        scriptDict = dict(comment=str(self.teComment.toPlainText()),
                          requires=str(self.teRequires.toPlainText()),
                          script=str(self.teScript.toPlainText()))
        #-- Result --#
        if asString:
            return pprint.pformat(scriptDict)
        return scriptDict

    def getNodeDatas(self, asString=False):
        """
        Get node datas

        :param asString: Return string instead of dict
        :type asString: bool
        :return: Node datas
        :rtype: dict | str
        """
        nodeDict = dict(comment=str(self.teComment.toPlainText()),
                        script=str(self.teScript.toPlainText()))
        #-- Result --#
        if asString:
            return pprint.pformat(nodeDict)
        return nodeDict

    def rf_editMode(self):
        """
        Refresh edit mode visibility
        """
        self.qfEditTree.setVisible(self.pbEdit.isChecked())
        self.qfInfoEdit.setVisible(self.pbEdit.isChecked())
        self.rf_editOptions()

    def rf_editOptions(self):
        """
        Refresh edit options visibility
        """
        widgets = [self.pbAddFolder, self.pbAddScript, self.pbAddNode, self.pbAddBranch,
                   self.pbDelSelFile, self.pbDelSelFolder]
        #-- Tree Options --#
        if self.pbEdit.isChecked():
            selItems = self.twTree.selectedItems() or []
            if not selItems:
                for wg in widgets:
                    wg.setEnabled(False)
            else:
                if selItems[0].itemType == 'root':
                    for wg in widgets:
                        wg.setEnabled(False)
                    self.pbAddFolder.setEnabled(True)
                elif selItems[0].itemType == 'folder':
                    for wg in widgets:
                        wg.setEnabled(True)
                    selGraphItems = self.graphTree.selectedItems() or []
                    if not len(selGraphItems) == 1:
                        self.pbAddNode.setEnabled(False)
                        self.pbAddBranch.setEnabled(False)
                    else:
                        if selGraphItems[0]._item.children:
                            self.pbAddBranch.setEnabled(True)
                        else:
                            self.pbAddBranch.setEnabled(False)
                    self.pbDelSelFile.setEnabled(False)
                elif selItems[0].itemType in ['script', 'node', 'branch']:
                    for wg in widgets:
                        wg.setEnabled(False)
                    self.pbDelSelFile.setEnabled(True)
        #-- Info Options --#
        self.teComment.setReadOnly(not self.pbEdit.isChecked())
        self.teRequires.setReadOnly(not self.pbEdit.isChecked())
        self.teScript.setReadOnly(not self.pbEdit.isChecked())

    def rf_tree(self, treeDict=None):
        """
        Refresh Tree topItems

        :param treeDict: Path to dict
        :type treeDict: dict
        """
        bankDir = os.path.join(self.mainUi.grapher.binPath, 'bank')
        rootPath = pFile.conformPath(bankDir)
        #-- Init Tree --#
        if treeDict is None:
            treeDict = pFile.pathToDict(bankDir, conformed=True)
            self.twTree.clear()
        else:
            item = self.getTreeItemFromPath('fullPath', treeDict['_order'][0])
            if item is not None:
                item.takeChildren()
        #-- Populate --#
        for root in treeDict['_order']:
            parent = self.getTreeItemFromPath('fullPath', root)
            #-- Populate Folders --#
            for folder in treeDict[root]['folders']:
                fullPath = pFile.conformPath(os.path.join(root, folder))
                #-- Top Items --#
                if root == rootPath:
                    relPath = folder
                    topItem = self.new_treeItem('root', folder, rootPath, relPath, fullPath)
                    self.twTree.addTopLevelItem(topItem)
                #-- Child Items --#
                else:
                    relPath = root.replace('%s/' % rootPath, '')
                    fldItem = self.new_treeItem('folder', folder, rootPath, relPath, fullPath)
                    parent.addChild(fldItem)
            #-- Populate Files --#
            for file in treeDict[root]['files']:
                relPath = root.replace('%s/' % rootPath, '')
                fullPath = pFile.conformPath(os.path.join(root, file))
                if file.endswith('.sc.py'):
                    fileItem = self.new_treeItem('script', file.split('.')[0], rootPath, relPath, fullPath)
                elif file.endswith('.nd.py'):
                    fileItem = self.new_treeItem('node', file.split('.')[0], rootPath, relPath, fullPath)
                elif file.endswith('.br.py'):
                    fileItem = self.new_treeItem('branch', file.split('.')[0], rootPath, relPath, fullPath)
                else:
                    fileItem = None
                if fileItem is not None:
                    parent.addChild(fileItem)
        #-- Refresh --#
        self.rf_itemVisibility()

    def rf_itemVisibility(self):
        """
        Refresh item visibility
        """
        for item in pQt.getAllItems(self.twTree):
            if item.itemType == 'script':
                self.twTree.setItemHidden(item, not self.cbScript.isChecked())
            elif item.itemType == 'node':
                self.twTree.setItemHidden(item, not self.cbNode.isChecked())
            elif item.itemType == 'branch':
                self.twTree.setItemHidden(item, not self.cbBranch.isChecked())

    def rf_infoVisibility(self):
        """
        Refresh info widgets visibility
        """
        selItems = self.twTree.selectedItems() or []
        if selItems:
            if selItems[0].itemType in ['script', 'node', 'branch']:
                self.splitScript.setVisible(True)
                self.teComment.clear()
                self.teRequires.clear()
                self.teScript.clear()
                self.vfSpacer.setEnabled(False)
                if selItems[0].itemType in ['node', 'branch']:
                    self.lRequires.setText('Info')
                    self.pbSendToGraph.setEnabled(True)
                else:
                    self.lRequires.setText('Requires')
                    self.pbSendToGraph.setEnabled(False)
            else:
                self.splitScript.setVisible(False)
                self.vfSpacer.setEnabled(True)
                self.pbSendToGraph.setEnabled(False)
        else:
            self.vfSpacer.setEnabled(True)
            self.pbSendToGraph.setEnabled(False)

    @staticmethod
    def new_treeItem(itemType, label, rootPath, relPath, fullPath):
        """
        Create tree item

        :param itemType: 'root', 'folder', 'script', 'node', 'branch'
        :type itemType: str
        :param label: Item label
        :type label: str
        :param rootPath: Item root path
        :type rootPath: str
        :param relPath: Item relative path
        :type relPath: str
        :param fullPath: Item full path
        :type fullPath: str
        :return: New tree item
        :rtype: QtGui.QTreeWidgetItem
        """
        #-- Item --#
        newFont = QtGui.QFont()
        newFont.setBold(True)
        newItem = QtGui.QTreeWidgetItem()
        if itemType == 'root':
            newItem.setFont(0, newFont)
        elif itemType == 'script':
            newItem.setTextColor(0, QtGui.QColor(0, 80, 255))
        elif itemType == 'node':
            newItem.setTextColor(0, QtGui.QColor(0, 170, 0))
        elif itemType == 'branch':
            newItem.setTextColor(0, QtGui.QColor(180, 120, 120))
        newItem.setText(0, label)
        #-- Datas --#
        newItem.itemType = itemType
        newItem.label = label
        newItem.rootPath = rootPath
        newItem.relPath = relPath
        newItem.fullPath = fullPath
        #-- Result --#
        return newItem

    def updateInfo(self):
        """
        Update info widgets
        """
        selItems = self.twTree.selectedItems() or []
        if selItems:
            fp = selItems[0].fullPath
            if selItems[0].itemType in ['script', 'node', 'branch']:
                infoDict = pFile.readPyFile(fp)
                self.teComment.setPlainText(infoDict['comment'])
                if selItems[0].itemType == 'script':
                    self.teRequires.setPlainText(infoDict['requires'])
                    self.teScript.setPlainText(infoDict['script'])
                elif selItems[0].itemType == 'node':
                    datas = infoDict['nodeDatas']
                    self.teRequires.setPlainText("%s (%s)" % (datas['nodeName'], datas['nodeType']))
                    self.teScript.setPlainText(datas['nodeScript'][datas['nodeVersion']])
                elif selItems[0].itemType == 'branch':
                    txt = []
                    for n in sorted(infoDict['branchDatas'].keys()):
                        nodeDatas = infoDict['branchDatas'][n]
                        txt.append("%s (%s)" % (nodeDatas['nodeName'], nodeDatas['nodeType']))
                    self.teRequires.setPlainText('\n'.join(txt))

    def on_refresh(self):
        """
        Command launched when 'Refresh' QPushButton is clicked

        Refresh tree
        """
        selItems = self.twTree.selectedItems() or []
        if not selItems:
            self.rf_tree()
        else:
            path = selItems[0].fullPath
            if os.path.isdir(path):
                self.rf_tree(treeDict=pFile.pathToDict(path, conformed=True))

    def on_treeItem(self):
        """
        Command launched when 'Tree' QTreeWidget is clicked

        Refresh Ui
        """
        self.rf_editOptions()
        self.rf_infoVisibility()
        self.updateInfo()

    def on_sendToGraph(self):
        """
        Command launched when 'Send To Graph' QPushButton is clicked

        Add selected node or branch to graph
        """
        selItem = self.twTree.selectedItems()[0]
        #-- Store Node In Buffer --#
        if selItem.itemType == 'node':
            nodeDatas = pFile.readPyFile(selItem.fullPath)['nodeDatas']
            self.mainUi.graphZone.cpBuffer = dict(_mode='nodes')
            self.mainUi.graphZone.cpBuffer[0] = dict(nodeName=selItem.label, nodeChildren={}, nodeDict=nodeDatas)
        #-- Store Branch In Buffer --#
        elif selItem.itemType == 'branch':
            branchDatas = pFile.readPyFile(selItem.fullPath)['branchDatas']
            self.mainUi.graphZone.cpBuffer = dict(_mode='branch')
            self.mainUi.graphZone.cpBuffer[0] = dict(nodeName=selItem.label, nodeChildren={}, nodeDict=branchDatas[0])
            for n in sorted(branchDatas.keys()):
                if n > 0:
                    self.mainUi.graphZone.cpBuffer[0]['nodeChildren'][n-1] = branchDatas[n]
        #-- Paste Nodes --#
        graphItems = self.mainUi.graphZone.graphTree.selectedItems() or []
        if graphItems:
            self.mainUi.graphZone.pasteNodes(dstItem=graphItems[0])
        else:
            self.mainUi.graphZone.pasteNodes()
        self.mainUi.graphZone.refreshGraph()

    def on_xPlorer(self):
        """
        Command launched when 'Wplorer' QPushButton is clicked

        Launch bank path in explorer
        """
        os.system('start %s' % os.path.normpath(os.path.join(self.mainUi.grapher.binPath, 'bank')))

    def on_add(self, addType=None):
        """
        Command launched when 'Add Folder' QPushButton is clicked

        Launch new folder prompt dialog
        :param addType: 'folder', 'script', 'node', 'branch'
        :type addType: str
        """
        if addType == 'folder':
            self.pdAdd = pQt.PromptDialog("New Folder Name", self.addFolder)
        elif addType == 'script':
            self.pdAdd = pQt.PromptDialog("New Script Name (no extension)", self.addScipt)
        elif addType == 'node':
            self.pdAdd = pQt.PromptDialog("New Node Title", self.addNode)
        elif addType == 'branch':
            self.pdAdd = pQt.PromptDialog("New Branch Title", self.addBranch)
        self.pdAdd.setMinimumHeight(80)
        self.pdAdd.setMaximumHeight(80)
        self.pdAdd.exec_()

    def addFolder(self):
        """
        Add tree folder
        """
        #-- Get Folder Info --#
        selItem = self.twTree.selectedItems()[0]
        folderPath = selItem.fullPath
        folderName = self.pdAdd.result()['result_1']
        #-- Create Folder --#
        newPath = os.path.join(folderPath, folderName)
        if not os.path.exists(newPath):
            try:
                os.mkdir(newPath)
                self.log.info("New folder created: %s" % pFile.conformPath(newPath))
            except:
                raise IOError("!!! Can not create folder: %s !!!" % pFile.conformPath(newPath))
        else:
            mess = ["!!! Folder already exists !!!",
                    "Folder Path: %s" % pFile.conformPath(folderPath),
                    "Folder Name: %s" % folderName]
            self.edFolder = pQt.errorDialog(mess, self.pdAdd)
        #-- Refresh --#
        self.pdAdd.close()
        treeDict = pFile.pathToDict(folderPath, conformed=True)
        self.rf_tree(treeDict=treeDict)

    def addScipt(self):
        """
        Add script
        """
        #-- Get Script Info --#
        selItem = self.twTree.selectedItems()[0]
        scriptPath = selItem.fullPath
        scriptName = self.pdAdd.result()['result_1']
        #-- Create Script --#
        newScript = os.path.join(scriptPath, '%s.sc.py' % scriptName)
        if not os.path.exists(newScript):
            txt = ["comment = 'No Comment !!!'", "requires = ''", "script = ''"]
            try:
                pFile.writeFile(newScript, '\n'.join(txt))
                self.log.info("New script created: %s" % pFile.conformPath(newScript))
            except:
                raise IOError("!!! Can not create script: %s !!!" % pFile.conformPath(newScript))
        else:
            mess = ["!!! Script already exists !!!",
                    "Script Path: %s" % pFile.conformPath(scriptPath),
                    "Script Name: %s.sc.py" % scriptName]
            self.edFolder = pQt.errorDialog(mess, self.pdAdd)
        #-- Refresh --#
        self.pdAdd.close()
        treeDict = pFile.pathToDict(scriptPath, conformed=True)
        self.rf_tree(treeDict=treeDict)

    def addNode(self):
        """
        Add selected graphNode
        """
        #-- Get Script Info --#
        selItem = self.twTree.selectedItems()[0]
        nodePath = selItem.fullPath
        nodeTitle = self.pdAdd.result()['result_1']
        #-- Create Node File --#
        newNodeFile = os.path.join(nodePath, '%s.nd.py' % nodeTitle)
        if not os.path.exists(newNodeFile):
            graphItem = self.graphTree.selectedItems()[0]
            txt = ["comment = 'No comment !!!'", "nodeDatas = %s" % graphItem._item.getDatas()]
            try:
                pFile.writeFile(newNodeFile, '\n'.join(txt))
                self.log.info("New node file created: %s" % pFile.conformPath(newNodeFile))
            except:
                raise IOError("!!! Can not create node file: %s !!!" % pFile.conformPath(newNodeFile))
        else:
            mess = ["!!! Node file already exists !!!",
                    "Node Path: %s" % pFile.conformPath(nodePath),
                    "Node Title: %s.nd.py" % nodeTitle]
            self.edFolder = pQt.errorDialog(mess, self.pdAdd)
        #-- Refresh --#
        self.pdAdd.close()
        treeDict = pFile.pathToDict(nodePath, conformed=True)
        self.rf_tree(treeDict=treeDict)

    def addBranch(self):
        """
        Add selected branch
        """
        #-- Get Script Info --#
        selItem = self.twTree.selectedItems()[0]
        branchPath = selItem.fullPath
        branchTitle = self.pdAdd.result()['result_1']
        #-- Create Branch File --#
        newBranchFile = os.path.join(branchPath, '%s.br.py' % branchTitle)
        if not os.path.exists(newBranchFile):
            graphItem = self.graphTree.selectedItems()[0]
            treeDatas = {0: graphItem._item.getDatas()}
            #-- Store Children --#
            if graphItem._item._children:
                for n, child in enumerate(graphItem._item.allChildren()):
                    treeDatas[n+1] = child.getDatas()
            txt = ["comment = 'No comment !!!'", "branchDatas = %s" % treeDatas]
            try:
                pFile.writeFile(newBranchFile, '\n'.join(txt))
                self.log.info("New branch file created: %s" % pFile.conformPath(newBranchFile))
            except:
                raise IOError("!!! Can not create branch file: %s !!!" % pFile.conformPath(newBranchFile))
        else:
            mess = ["!!! Branch file already exists !!!",
                    "Branch Path: %s" % pFile.conformPath(branchPath),
                    "Branch Title: %s.br.py" % branchTitle]
            self.edFolder = pQt.errorDialog(mess, self.pdAdd)
        #-- Refresh --#
        self.pdAdd.close()
        treeDict = pFile.pathToDict(branchPath, conformed=True)
        self.rf_tree(treeDict=treeDict)

    def on_delSelFile(self):
        """
        Command launched when 'Del Sel File' QPushButton is clicked

        Launch confirm dialog
        """
        selItems = self.twTree.selectedItems() or []
        if selItems:
            if selItems[0].itemType in ['script', 'node', 'branch']:
                ffp = selItems[0].fullPath
                self.cdDelFile = pQt.ConfirmDialog('Delete Selected File ?\n%s' % ffp, ['Delete'],
                                                   [partial(self.delFile, ffp, refresh=True)])
                self.cdDelFile.exec_()

    def delFile(self, fileFullPath, refresh=False):
        """
        Delete given file

        :param fileFullPath: File to delete
        :type fileFullPath: str
        :param refresh: Enable tree refresh
        :type refresh: bool
        """
        self.cdDelFile.close()
        #-- Delete --#
        try:
            os.remove(fileFullPath)
            self.log.info("File deleted: %s" % fileFullPath)
        except:
            raise IOError("Can not delete file: %s !!!" % fileFullPath)
        #-- Refresh --#
        if refresh:
            parentItem = self.twTree.selectedItems()[0].parent()
            treeDict = pFile.pathToDict(parentItem.fullPath, conformed=True)
            self.rf_tree(treeDict=treeDict)

    def on_delSelFolder(self):
        """
        Command launched when 'Del Sel Folder' QPushButton is clicked

        Launch confirm dialog
        """
        selItems = self.twTree.selectedItems() or []
        if selItems:
            if selItems[0].itemType == 'folder':
                ffp = selItems[0].fullPath
                if selItems[0].childCount():
                    mess = 'Delete Selected Folder and its contents ?\n %s' % ffp
                else:
                    mess = 'Delete Selected Folder ?\n %s' % ffp
                self.cdDelFolder = pQt.ConfirmDialog(mess, ['Delete'], [partial(self.delFolder, ffp, refresh=True)])
                self.cdDelFolder.exec_()

    def delFolder(self, folderFullPath, refresh=False):
        """
        Delete given folder

        :param folderFullPath: Folder to delete
        :type folderFullPath: str
        :param refresh: Enable tree refresh
        :type refresh: bool
        """
        self.cdDelFolder.close()
        #-- Delete --#
        try:
            shutil.rmtree(folderFullPath)
            self.log.info("Folder deleted: %s" % folderFullPath)
        except:
            raise IOError("Can not delete folder: %s !!!" % folderFullPath)
        #-- Refresh --#
        if refresh:
            parentItem = self.twTree.selectedItems()[0].parent()
            treeDict = pFile.pathToDict(parentItem.fullPath, conformed=True)
            self.rf_tree(treeDict=treeDict)

    def on_save(self):
        """
        Command launched when 'Save' QPushButton is clicked

        Launch confirm dialog
        """
        selItems = self.twTree.selectedItems() or []
        if selItems:
            if selItems[0].itemType in ['script', 'node', 'branch']:
                ffp = selItems[0].fullPath
                self.cdSaveFile = pQt.ConfirmDialog('Save Selected File ?\n%s' % ffp, ['Save'],
                                                    [partial(self.save, ffp)])
                self.cdSaveFile.exec_()

    def save(self, fileFullPath):
        """
        Save datas to given file

        :param fileFullPath: File path
        :type fileFullPath: str
        """
        self.cdSaveFile.close()
        datas = []
        #-- Script File --#
        if '.sc.py' in fileFullPath:
            for k, v in self.getScriptDatas().iteritems():
                datas.append("%s = %r" % (k, v))
        #-- Node File --#
        elif '.nd.py' in fileFullPath or '.br.py' in fileFullPath:
            nodeDict = pFile.readPyFile(fileFullPath)
            _datas = self.getNodeDatas()
            nodeDict['comment'] = _datas['comment']
            if '.nd.py' in fileFullPath:
                nodeDict['nodeDatas']['nodeScript'][nodeDict['nodeDatas']['nodeVersion']] = _datas['script']
            for k, v in nodeDict.iteritems():
                if isinstance(v, str):
                    datas.append("%s = %r" % (k, v))
                else:
                    datas.append("%s = %s" % (k, v))
        #-- Save File --#
        try:
            pFile.writeFile(fileFullPath, '\n'.join(datas))
            self.log.info("File saved: %s" % fileFullPath)
        except:
            raise IOError("!!! Can not save file: %s !!!" % fileFullPath)
