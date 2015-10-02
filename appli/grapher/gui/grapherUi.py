import os, sys, pprint
from appli import grapher
from functools import partial
from PyQt4 import QtGui, QtCore
from lib.qt import procQt, textEditor
from lib.system import procFile as pFile
from appli.grapher.gui.ui import grapherUI
from appli.grapher.core.grapher import Grapher
from appli.grapher.gui import graphZone, toolsWgts, nodeEditor, graphWgts


class GrapherUi(QtGui.QMainWindow, grapherUI.Ui_mwGrapher):
    """
    Grapher main ui

    :param logLvl: Verbose ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """

    def __init__(self, logLvl='info'):
        self.log = pFile.Logger(title="GrapherUi", level=logLvl)
        self.log.info("########## Launching Grapher Ui ##########")
        self.grapher = Grapher(logLvl)
        self.user = self.grapher.user
        self.userPath = self.grapher.userPath
        self.userFile = os.path.join(self.userPath, '%s.py' % self.user)
        self.iconPath = grapher.iconPath
        super(GrapherUi, self).__init__()
        self.checkUserPath()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        self.log.info("#-- Setup Main Ui --#", newLinesBefor=1)
        self.setupUi(self)
        self.varBuffer = None
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self._initWidgets()
        self._initMenu()
        self.rf_nodeGroupVisibility(self.gbComment, self.graphComment)
        self.rf_nodeGroupVisibility(self.gbVariables, self.graphVar)

    # noinspection PyUnresolvedReferences
    def _initWidgets(self):
        self.log.info("#-- Init Widgets --#", newLinesBefor=1)
        #-- Node Comment --#
        self.graphComment = textEditor.TextEditor()
        self.graphComment.bLoadFile.setEnabled(False)
        self.graphComment.bSaveFile.setEnabled(False)
        self.glComment.addWidget(self.graphComment, 0, 0)
        self.gbComment.clicked.connect(partial(self.rf_nodeGroupVisibility, self.gbComment, self.graphComment))
        #-- GraphZone --#
        self.graphZone = graphZone.GraphZone(self)
        #-- Node Variables --#
        self.graphVar = graphWgts.Variables(self, self)
        self.glVariables.addWidget(self.graphVar, 0, 0)
        self.gbVariables.clicked.connect(partial(self.rf_nodeGroupVisibility, self.gbVariables, self.graphVar))
        #-- GraphTools --#
        self.graphTools = toolsWgts.GraphTools(self)
        self.tbTools.addWidget(self.graphTools)
        self.tbTools.orientationChanged.connect(partial(self.on_miToolsOrientChanged, orient=False, force=False))
        #-- Node Editor --#
        self.nodeEditor = nodeEditor.NodeEditor(self)
        self.nodeEditor.pbClose.setVisible(False)
        self.vlNodeEditor.insertWidget(0, self.nodeEditor)
        #-- Grapher Logs --#
        self.graphLogs = graphWgts.Logs(self)
        self.vlLogs.addWidget(self.graphLogs)

    def _initMenu(self):
        self.log.info("#-- Init Menus --#", newLinesBefor=1)
        self._menuFiles()
        self._menuGraph()
        self._menuExec()
        self._menuDisplay()
        self._menuHelp()
        self.on_miNodeEditor()
        self.on_miLogs()

    # noinspection PyUnresolvedReferences
    def _menuFiles(self):
        self.log.debug("\t ---> Menu Files ...")
        #-- Load --#
        self.miLoad.triggered.connect(self.on_miLoad)
        self.miLoad.setShortcut('Ctrl+L')
        self.menuRecentFiles.aboutToShow.connect(self.buildRecentFilesMenu)
        #-- Save --#
        self.miSave.triggered.connect(self.on_miSave)
        self.miSave.setShortcut('Ctrl+S')
        self.miSaveAs.triggered.connect(self.on_miSaveAs)
        self.miSaveAs.setShortcut('Ctrl+Shift+S')

    # noinspection PyUnresolvedReferences
    def _menuGraph(self):
        self.log.debug("\t ---> Menu Graph ...")
        self.menuGraph.aboutToShow.connect(partial(self.graphZone.buildMenu, self.menuGraph))
        self.graphZone.buildMenu(self.menuGraph)

    # noinspection PyUnresolvedReferences
    def _menuExec(self):
        self.log.debug("\t ---> Menu Exec ...")
        #-- Launcher --#
        self.miXplorer.triggered.connect(self.on_miXplorer)
        self.miXplorer.setShortcut('F3')
        self.miXterm.triggered.connect(self.on_miXterm)
        self.miXterm.setShortcut('F4')
        #-- Exec --#
        self.miExecGraph.triggered.connect(self.on_miExecGraph)
        self.miExecGraph.setShortcut('Alt+E')

    # noinspection PyUnresolvedReferences
    def _menuDisplay(self):
        self.log.debug("\t ---> Menu Display ...")
        #-- Widgets Visibility --#
        self.miToolsVisibility.triggered.connect(self.on_miToolsVisibility)
        self.miToolsVisibility.setShortcut('T')
        self.miNodeEditor.triggered.connect(self.on_miNodeEditor)
        self.miNodeEditor.setShortcut('E')
        self.miGraphScene.triggered.connect(self.on_miGraphScene)
        self.miGraphScene.setShortcut('Tab')
        self.miLogs.triggered.connect(self.on_miLogs)
        self.miLogs.setShortcut('L')
        #-- SubMenu 'Tools Bar Orient' --#
        self.miBarHorizontal.triggered.connect(partial(self.on_miToolsOrientChanged,
                                                       orient='horizontal', force=True))
        self.miBarVertical.triggered.connect(partial(self.on_miToolsOrientChanged,
                                                     orient='vertical', force=True))
        #-- SubMenu 'Tools Tab Orient' --#
        self.miTabNorth.triggered.connect(partial(self.on_miTabOrientChanged, 'North'))
        self.miTabSouth.triggered.connect(partial(self.on_miTabOrientChanged, 'South'))
        self.miTabWest.triggered.connect(partial(self.on_miTabOrientChanged, 'West'))
        self.miTabEast.triggered.connect(partial(self.on_miTabOrientChanged, 'East'))
        #-- Tools Options --#
        self.miToolsIconOnly.triggered.connect(self.on_miToolsIconOnly)
        self.miToolsIconOnly.setShortcut('Ctrl+T')

    # noinspection PyUnresolvedReferences
    def _menuHelp(self):
        self.log.debug("\t ---> Menu Help ...")
        #-- Datas --#
        self.miGrapherDatas.triggered.connect(self.on_miGrapherDatas)
        self.miTreeDatas.triggered.connect(self.on_miTreeDatas)
        self.miNodeDatas.triggered.connect(self.on_miNodeDatas)
        #-- Verbose --#
        self.logLevels = []
        if hasattr(self, 'log'):
            for lvl in self.log.levels:
                newItem = self.menuVerbose.addAction(lvl)
                newItem.setCheckable(True)
                newItem.triggered.connect(partial(self.on_miVerbose, lvl))
                self.logLevels.append(newItem)
        self.on_miVerbose(self.log.level)

    @property
    def toolsIconOnly(self):
        """
        Get tools icon only state

        :return: Tools icon only state
        :rtype: bool
        """
        return self.miToolsIconOnly.isChecked()

    @property
    def nodeEditorIsEnabled(self):
        """
        Get nodeEditor state

        :return: NodeEditor state
        :rtype: bool
        """
        return self.miNodeEditor.isChecked()

    @property
    def userDatas(self):
        """
        Get user datas from user file

        :return: User datas
        :rtype: dict
        """
        return pFile.readPyFile(os.path.normpath(self.userFile))

    @staticmethod
    def rf_nodeGroupVisibility(groupBox, widget):
        """
        Refresh given QGroupBox visibility

        :param groupBox: Node editor groupBox
        :type groupBox: QtGui.QGroupBox
        :param widget: GroupBox child widget
        :type widget: textEditor.TextEditor | QtGui.QTextEdit | graphWgts.NodeVariables
        """
        widget.setVisible(groupBox.isChecked())
        if groupBox.isChecked():
            groupBox.setMaximumHeight(16777215)
        else:
            groupBox.setMaximumHeight(15)

    def checkUserPath(self):
        """
        Check if user path and files, needed by Grapher, exists
        """
        self.log.info("Check user path ...")
        #-- User Files --#
        if not os.path.exists(self.userFile):
            userDatas = ["recentFiles = []"]
            try:
                pFile.writeFile(self.userFile, '\n'.join(userDatas))
                self.log.info("Create user file: %s" % self.userFile)
            except:
                raise IOError("!!! Can not create user file: %s !!!" % self.userFile)

    def updateUi(self):
        """
        Update Grapher ui
        """
        self.setWindowTitle(self.grapher.graphFullPath)
        self.graphComment.teText.setHtml(self.grapher.comment)
        self.graphVar.buildTree(self.grapher.variables)

    def updateCore(self):
        """
        Update Grapher core
        """
        self.grapher.setComment(str(self.graphComment.teText.toHtml()))
        self.grapher.variables = self.graphVar.getDatas()

    def load(self, graphFile=None):
        """
        Load graphFile

        :param graphFile: GraphFile full path
        :type graphFile: str
        """
        if graphFile is None:
            selFiles = self.fdLoadGraph.selectedFiles() or []
            if selFiles:
                graphFile = selFiles[0]
            self.fdLoadGraph.close()
        self.grapher.load(str(graphFile))
        self.updateUi()
        self.graphZone.refreshGraph()

    def saveAs(self):
        """
        Save graph as given fileDialog result
        """
        gpFiles = self.fdSaveGraph.selectedFiles()
        if gpFiles:
            graphFile = gpFiles[0]
            if not graphFile.endsWith('.gp.py'):
                graphFile = '%s.gp.py' % graphFile.split('.')[0]
            self.updateCore()
            result = self.grapher.saveAs(str(graphFile))
            if result:
                self.setWindowTitle(graphFile)
                self.addToRecentFiles()

    def addToRecentFiles(self):
        """
        Add current graphFile to recent files
        """
        #-- Update Recent Files --#
        userDatas = self.userDatas
        if not self.grapher.graphFullPath in userDatas['recentFiles']:
            if len(userDatas['recentFiles']) == 10:
                userDatas['recentFiles'].pop(len(userDatas['recentFiles']) - 1)
            userDatas['recentFiles'].insert(0, self.grapher.graphFullPath)
            #-- Write Datas --#
            userTxt = []
            for k , v in sorted(userDatas.iteritems()):
                if isinstance(v, basestring):
                    userTxt.append("%s = %r" % (k, v))
                else:
                    userTxt.append("%s = %s" % (k, v))
            try:
                pFile.writeFile(self.userFile, '\n'.join(userTxt))
                self.log.debug("Recent files updated")
            except:
                raise IOError("!!! Can not update recent files !!!")

    def buildRecentFilesMenu(self):
        """
        Build 'Recent Files' QMenu
        """
        recentFiles = self.userDatas['recentFiles']
        self.menuRecentFiles.clear()
        for f in recentFiles:
            newItem = self.menuRecentFiles.addAction(f)
            newItem.triggered.connect(partial(self.load, graphFile=f))

    def on_miLoad(self):
        """
        Command launched when 'Load' QMenuItem is triggered

        Launch fileDialog
        """
        self.log.detail(">>> Launch menuItem 'Load' ...")
        if self.grapher._graphFile is not None:
            root = self.grapher.graphPath
        else:
            root = 'D:/prods'
        self.fdLoadGraph = procQt.fileDialog(fdFileMode='ExistingFile', fdRoot=root, fdFilters=['*.gp.py'],
                                             fdCmd=self.load)
        self.fdLoadGraph.exec_()

    def on_miSave(self):
        """
        Command launched when 'Save' QMenuItem is triggered

        Save graph if 'graphFile' is not None, else launch fileDialog
        """
        self.log.detail(">>> Launch menuItem 'Save' ...")
        if self.grapher._graphFile is None:
            self.on_miSaveAs()
        else:
            self.updateCore()
            self.grapher.save()

    def on_miSaveAs(self):
        """
        Command launched when 'Save As' QMenuItem is triggered

        Launch fileDialog
        """
        self.log.detail(">>> Launch menuItem 'Save As' ...")
        if self.grapher._graphFile is not None:
            root = self.grapher.graphPath
        else:
            root = 'D:/prods'
        self.fdSaveGraph = procQt.fileDialog(fdMode='save', fdRoot=root, fdFilters=['*.gp.py'],
                                             fdCmd=self.saveAs)
        self.fdSaveGraph.exec_()

    def on_miXplorer(self):
        """
        Command launched when 'Xplorer' QMenuItem is triggered

        Launch Explorer
        """
        self.log.detail(">>> Launch menuItem 'Xplorer' ...")
        if self.grapher._graphFile is not None:
            os.system('start %s' % os.path.normpath(self.grapher.graphPath))
        else:
            self.log.info("GraphFile not setted, can not launch Xplorer !!!")

    def on_miXterm(self):
        """
        Command launched when 'Xterm' QMenuItem is triggered

        Launch Xterm
        """
        self.log.detail(">>> Launch menuItem 'Xterm' ...")
        if self.grapher._graphFile is not None:
            os.system('start')
        else:
            self.log.info("GraphFile not setted, can not launch Xterm !!!")

    def on_miExecGraph(self):
        """
        Command launched when 'Exec Graph' QMenuItem is triggered

        Exec Graph
        """
        self.log.detail(">>> Launch menuItem 'Exec Graph' ...")
        self.grapher.save()
        logFile = self.grapher.execGraph(xTerm=self.graphLogs.showXterm, wait=self.graphLogs.waitAtEnd)
        if not self.graphLogs.cbShowXterm.isChecked():
            self.graphLogs.addJob(logFile)

    def on_miToolsOrientChanged(self, orient=False, force=False):
        """
        Orient toolsTab and their contents

        :param orient: 'horizontal' or 'vertical'
        :type orient: str
        :param force: Force orientation
        :type force: bool
        """
        self.log.detail(">>> Launch menuItem 'Tools Orient' ...")
        #-- Force Orient --#
        if force:
            if orient == 'horizontal':
                self.tbTools.setOrientation(QtCore.Qt.Horizontal)
            elif orient == 'vertical':
                self.tbTools.setOrientation(QtCore.Qt.Vertical)
        #-- Refresh ToolBar Display --#
        if self.tbTools.orientation() == 1:
            self.graphTools.tabOrientation('North')
            self.miToolsIconOnly.setChecked(True)
        else:
            self.graphTools.tabOrientation('West')
            self.miToolsIconOnly.setChecked(False)
        self.graphTools.toolsAspect()

    def on_miTabOrientChanged(self, orient):
        """
        Command launched when 'Tab Orient' QMenuItem is triggered

        Orient tab contents
        :param orient: 'North', 'South', 'West' or 'East'
        :type orient: str
        """
        self.log.detail(">>> Launch menuItem 'Tab Orient' ...")
        self.graphTools.tabOrientation(orient)

    def on_miToolsVisibility(self):
        """
        Command launched when 'Tools Visibility' QMenuItem is triggered

        Turn on or off tools bar visibility
        """
        self.log.detail(">>> Launch menuItem 'Tools Visibility' ...")
        self.tbTools.setVisible(self.miToolsVisibility.isChecked())

    def on_miNodeEditor(self):
        """
        Command launched when 'Node Editor' QMenuItem is triggered

        Show / Hide node editor
        """
        self.log.detail(">>> Launch menuItem 'Node Editor' ...")
        self.vfNodeEditor.setVisible(self.miNodeEditor.isChecked())
        selItems = self.graphZone.currentGraph.selectedItems() or []
        self.nodeEditor.clear()
        if len(selItems) == 1:
            self.nodeEditor.connectItem(selItems[0])

    def on_miGraphScene(self):
        """
        Command launched when 'Graph View' QMenuItem is triggered

        Show / Hide Graph View
        """
        self.log.detail(">>> Launch menuItem 'Switch Graph Mode' ...")
        self.graphZone.graphTree.setVisible(not self.miGraphScene.isChecked())
        self.graphZone.sceneView.setVisible(self.miGraphScene.isChecked())
        self.graphZone.refreshGraph()

    def on_miLogs(self):
        """
        Command launched when 'Logs' QMenuItem is triggered

        Show / Hide logs
        """
        self.log.detail(">>> Launch menuItem 'Logs' ...")
        self.vfLogs.setVisible(self.miLogs.isChecked())

    def on_miToolsIconOnly(self):
        """
        Command launched when 'Tools Icon Only' QMenuItem is triggered

        Switch toolsTab aspect
        """
        self.log.detail(">>> Launch menuItem 'Tools Icon Only' ...")
        self.graphTools.toolsAspect()

    def on_miGrapherDatas(self):
        """
        Command launched when 'Grapher Datas' QMenuItem is triggered

        Print grapher datas
        """
        self.log.detail(">>> Launch menuItem 'Grapher Datas' ...")
        print pprint.pformat(self.grapher.getDatas()['graphDatas'])

    def on_miTreeDatas(self):
        """
        Command launched when 'Tree Datas' QMenuItem is triggered

        Print tree datas
        """
        self.log.detail(">>> Launch menuItem 'Tree Datas' ...")
        self.grapher.tree.printData()

    def on_miNodeDatas(self):
        """
        Command launched when 'Node Datas' QMenuItem is triggered

        Print selected nodes datas
        """
        self.log.detail(">>> Launch menuItem 'Node Datas' ...")
        if self.graphZone.currentGraphMode == 'tree':
            selItems = self.graphZone.graphTree.selectedItems() or []
        else:
            selItems = self.graphZone.graphScene.getSelectedNodes()
        if selItems:
            for item in selItems:
                self.log.info("Node Datas: %s" % item._item._node.nodeName)
                print item._item.getDatas(asString=True)

    def on_miVerbose(self, logLvl):
        """
        Command launched when 'Verbose' log level QMenuItem is triggered

        Set log level
        :param logLvl: Verbose ('critical', 'error', 'warning', 'info', 'debug', 'detail')
        :type logLvl: str
        """
        self.log.detail(">>> Launch menuItem 'Verbose': %s ..." % logLvl)
        #-- Uncheck All --#
        for item in self.logLevels:
            item.setChecked(False)
        #-- Check Given LogLvl --#
        for item in self.logLevels:
            if str(item.text()) == logLvl:
                item.setChecked(True)
                break
        #-- Set LogLvl --#
        self.log.level = logLvl
        self.log.lvlIndex = self.log.levels.index(self.log.level)
        self.grapher.log.level = logLvl
        self.grapher.log.lvlIndex = self.grapher.log.levels.index(self.grapher.log.level)


def launch(logLvl='info'):
    """
    Grapher launcher

    :param logLvl: Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """
    app = QtGui.QApplication(sys.argv)
    window = GrapherUi(logLvl=logLvl)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch(logLvl='detail')