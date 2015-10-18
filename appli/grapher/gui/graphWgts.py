import os, pprint
from functools import partial
from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.grapher.gui.ui import graphNodeUI, nodeRenameUI, wgVariablesUI, wgLogsUI


class ItemWidget(QtGui.QWidget, graphNodeUI.Ui_wgGraphNode):
    """
    GraphTreeItem widget, child of GrapherUi.GraphTree.GraphItem

    :param pItem: Parent item
    :type pItem: QtGui.QTreeWidgetItem | QtSvg.QGraphicsProxyWidget
    """

    def __init__(self, pItem):
        self.pItem = pItem
        self.mainUi = self.pItem.mainUi
        self.log = self.mainUi.log
        self.log.detail("\t ---> Init Graph Widget --#")
        self._item = self.pItem._item
        super(ItemWidget, self).__init__()
        self._setupWidget()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        self.log.detail("\t ---> Setup Graph Widget --#")
        self.setupUi(self)
        self.pbEnable.clicked.connect(self.set_enabled)
        self.pbExpand.clicked.connect(self.set_expanded)
        self.pbExpand.setVisible(False)
        self.pbExec.setVisible(False)
        self.pbExec.clicked.connect(self.on_execButton)
        self.pbExec.setStyleSheet("background-color: rgb(255, 80, 80)")
        self.rf_nodeColor()
        self.rf_enableIcon()
        self.rf_expandIcon()
        self.rf_execButton()

    @property
    def isEnabled(self):
        """
        Get node enable state from grapher nodeObject

        :return: Node enable state
        :rtype: bool
        """
        return self._item._node.nodeIsEnabled

    @property
    def isActive(self):
        """
        Get node active state from grapher nodeObject

        :return: Node active state
        :rtype: bool
        """
        return self._item._node.nodeIsActive

    @property
    def isExpanded(self):
        """
        Get node expanded state from grapher nodeObject

        :return: Node expanded state
        :rtype: bool
        """
        return self._item._node.nodeIsExpanded

    def rf_nodeColor(self):
        """
        Refresh graphNode color
        """
        self.set_nodeColor(self._item._node._nodeColor)

    def rf_enableIcon(self):
        """
        Refresh enable state icon
        """
        if self._item._node.nodeIsEnabled:
            self.pbEnable.setIcon(self.mainUi.graphZone.enabledIcon)
        else:
            self.pbEnable.setIcon(self.mainUi.graphZone.disabledIcon)
        self.lNodeName.setEnabled(self.isActive)

    def rf_expandIcon(self):
        """
        Refresh expand state icon
        """
        if self.mainUi.graphZone.currentGraphMode == 'tree':
            if self._item._node.nodeIsExpanded:
                self.pbExpand.setIcon(self.mainUi.graphZone.collapseIcon)
            else:
                self.pbExpand.setIcon(self.mainUi.graphZone.expandIcon)

    def rf_execButton(self):
        """
        refresh exec button visibility
        """
        if hasattr(self._item._node, 'nodeExecMode'):
            self.pbExec.setVisible(self._item._node.nodeExecMode[self._item._node.nodeVersion])
        else:
            self.pbExec.setVisible(False)

    def set_nodeColor(self, rgba):
        """
        Set graphNode color (used for highlighting selected items)

        :param rgba: GraphNode color
        :type rgba: tuple
        """
        self.setStyleSheet("background-color: rgba(%s, %s, %s, %s)" % (rgba[0], rgba[1], rgba[2], rgba[3]))

    def set_enabled(self, state=None):
        """
        Set node enable state with given value

        :param state: Node enable state
        :type state: bool
        """
        if state is None:
            state = not self.isEnabled
        else:
            self.pbEnable.setChecked(state)
        self.log.detail(">>> Set enable state: %s ---> %s" % (self._item._node.nodeName, state))
        self._item.setEnabled(state)
        self.lNodeName.setEnabled(self.isActive)
        self.rf_enableIcon()
        if self.mainUi.graphZone.currentGraphMode == 'tree':
            self.mainUi.graphZone.refreshGraph()

    def set_expanded(self, state=None):
        """
        Set graphNode expanded with given state

        :param state: Expand state
        :type state: bool
        """
        if self.mainUi.graphZone.currentGraphMode == 'tree':
            if state is None:
                state = not self.isExpanded
            else:
                self.pbExpand.setChecked(state)
            self.log.detail(">>> Set expand state: %s ---> %s" % (self._item._node.nodeName, state))
            self._item.setExpanded(state)
            self.pItem.setExpanded(state)
            self.rf_expandIcon()

    def on_execButton(self):
        """
        Command launched when 'Exec' QPushButton is clicked

        Exec node
        """
        self.mainUi.on_miExecNode(item=self.pItem)


class NodeRenamer(QtGui.QDialog, nodeRenameUI.Ui_dialNodeRename):
    """
    Node renamer QDialog, child of mainUi

    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    :param selItem: Selected graphItem
    :type selItem: graphTree.GraphItem | graphScene.GraphItem
    """

    def __init__(self, mainUi, selItem):
        self.mainUi = mainUi
        self.item = selItem
        super(NodeRenamer, self).__init__(self.mainUi)
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        self.setupUi(self)
        self.lCurrentNodeVal.setText(self.item._item._node.nodeName)
        self.leNewName.textChanged.connect(self.updateResult)
        self.pbOk.clicked.connect(self.accept)
        self.pbCancel.clicked.connect(self.close)

    def updateResult(self):
        """
        Update new node name result
        """
        self.lResultVal.setText(self.mainUi.grapher.conformNewNodeName(str(self.leNewName.text())))

    def accept(self):
        """
        Rename node and update node
        """
        super(NodeRenamer, self).accept()
        self.item._item._node.nodeName = str(self.lResultVal.text())
        if self.mainUi.graphZone.currentGraphMode == 'tree':
            self.item._widget.rf_label()
        else:
            self.item._label._text = self.item._item._node.nodeName
            self.item._label.setText()


class Variables(QtGui.QWidget, wgVariablesUI.Ui_wgVariables):
    """
    Node Variables QWidget, child of mainUi and NodeEditor

    :param mainUi: Grapher main window
    :type mainUi: GrapherUi
    :param pWidget: Parent widget
    :type: GrapherUi | NodeEditor
    """

    def __init__(self, mainUi, pWidget):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.pWidget = pWidget
        super(Variables, self).__init__()
        self._setupWidget()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        self.setupUi(self)
        self.menu = QtGui.QMenu()
        self.pbAddVar.clicked.connect(partial(self.on_addVar, index=None))
        self.pbDupVar.clicked.connect(self.on_dupVar)
        self.pbDelVar.clicked.connect(partial(self.on_delVar, items=None))
        self.pbVarDn.setIcon(self.mainUi.graphZone.unfoldIcon)
        self.pbVarDn.clicked.connect(partial(self.on_moveVar, 'down'))
        self.pbVarUp.setIcon(self.mainUi.graphZone.foldIcon)
        self.pbVarUp.clicked.connect(partial(self.on_moveVar, 'up'))
        self.twVar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.twVar.connect(self.twVar, QtCore.SIGNAL('customContextMenuRequested(const QPoint&)'), self.on_popUpMenu)
        self.buildMenu()
        self.rf_columnSize()

    def menuActions(self):
        """
        Get popup menu actions

        :return: Menu actions
        :rtype: dict
        """
        return {0: {'type': 'item', 'title': 'Copy Var', 'key': None, 'cmd': self.on_copyVar},
                1: {'type': 'item', 'title': 'Paste Var', 'key': None, 'cmd': self.on_pasteVar}}

    def buildMenu(self):
        """
        Build variable tree menu
        """
        #-- Build Menu --#
        menuDict = self.menuActions()
        for n in sorted(menuDict.keys()):
            #-- Add Sub Menu --#
            if menuDict[n]['type'] == 'menu':
                newMenu = self.menu.addMenu(menuDict[n]['title'])
                #-- Add Sub Item --#
                for i in sorted(menuDict[n]['children']):
                    childDict = menuDict[n]['children'][i]
                    self.newMenuItem(newMenu, childDict['type'], childDict['title'],
                                              childDict['key'], childDict['cmd'])
            #-- Add Item --#
            elif menuDict[n]['type'] in ['item', 'sep']:
                self.mainUi.graphZone.newMenuItem(self.menu, menuDict[n]['type'], menuDict[n]['title'],
                                                             menuDict[n]['key'], menuDict[n]['cmd'])

    def getDatas(self, asString=False):
        """
        Get variable tree datas

        :param asString: Return string instead of dict
        :type asString: bool
        :return: Variable tree datas
        :rtype: dict | str
        """
        treeVarDict = dict()
        #-- Parsing --#
        for n, item in enumerate(pQt.getTopItems(self.twVar)):
            treeVarDict[n] = dict(state=item._wState.isChecked(),
                                  label=str(item._wLabel.text()),
                                  type=item._wType.currentIndex(),
                                  value=eval(str(item._wValue.text())),
                                  comment=str(item._wComment.text()))
        #-- Result --#
        if asString:
            return pprint.pformat(treeVarDict)
        return treeVarDict

    def getVarDatas(self, index, asString=False):
        """
        Get given varItem datas

        :param index: VarItem index
        :type index: int
        :param asString: Return string instead of dict
        :type asString: bool
        :return: Variable item datas
        :rtype: dict | str
        """
        varDatas =  self.getDatas()[index]
        if asString:
            return pprint.pformat(varDatas)
        return varDatas

    def setDatas(self, item, varDict):
        """
        Set given varItem datas

        :param item: Variable item
        :type item: QtGui.QTreeWidgetItem
        :param varDict: Variable datas
        :type varDict: dict
        """
        item._wState.setChecked(varDict['state'])
        item._wLabel.setText(varDict['label'])
        item._wType.setCurrentIndex(varDict['type'])
        if isinstance(varDict['value'], str):
            item._wValue.setText('%r' % varDict['value'])
        else:
            item._wValue.setText(str(varDict['value']))
        item._wComment.setText(varDict['comment'])
        self.on_stateButton(item)

    def rf_columnSize(self):
        """
        Refresh tree column size
        """
        self.twVar.resizeColumnToContents(0)
        self.twVar.resizeColumnToContents(1)
        self.twVar.resizeColumnToContents(3)

    def rf_stateIcon(self, widget):
        """
        Refresh enable state icon
        """
        if widget.isChecked():
            widget.setIcon(self.mainUi.graphZone.enabledIcon)
        else:
            widget.setIcon(self.mainUi.graphZone.disabledIcon)

    def buildTree(self, varDict):
        """
        Build variable tree

        :param varDict: Variable datas
        :type varDict: dict
        """
        for n, d in sorted(varDict.iteritems()):
            newItem = self.on_addVar()
            self.setDatas(newItem, d)

    def on_popUpMenu(self, point):
        """
        Command launched when right mouse button is clicked

        :param point: Cursor position
        :type point: QtGui.QPoint
        """
        self.menu.exec_(self.mapToGlobal(point))

    def on_addVar(self, index=None):
        """
        Command launched when 'Add Var' QPushButton is clicked

        Add variable
        :param index: Insert new variable at given index
        :type index: int
        :return: Variable item
        :rtype: QtGui.QTreeWidgetItem
        """
        #-- Create Item --#
        newItem = self.new_varItem()
        if index is None:
            self.twVar.addTopLevelItem(newItem)
        else:
            self.twVar.insertTopLevelItem(index, newItem)
        newItem.setText(0, str(self.twVar.indexOfTopLevelItem(newItem) + 1))
        #-- Add Widgets --#
        self.twVar.setItemWidget(newItem, 1, newItem._wState)
        self.twVar.setItemWidget(newItem, 2, newItem._wLabel)
        self.twVar.setItemWidget(newItem, 3, newItem._wType)
        self.twVar.setItemWidget(newItem, 4, newItem._wValue)
        self.twVar.setItemWidget(newItem, 5, newItem._wComment)
        #-- refresh --#
        self.rf_columnSize()
        return newItem

    def on_dupVar(self):
        """
        Command launched when 'Dup Var' QPushButton is clicked

        Duplicate selected variables
        :return: Duplicated items
        :rtype: list
        """
        newItems = []
        selItems = self.twVar.selectedItems() or []
        for item in selItems:
            srcDatas = self.getVarDatas(self.twVar.indexOfTopLevelItem(item))
            newItem = self.on_addVar()
            self.setDatas(newItem, srcDatas)
            newItems.append(newItem)
        self.twVar.clearSelection()
        for item in selItems:
            item.setSelected(True)
        return newItems

    def on_delVar(self, items=None):
        """
        Command launched when 'DelVar' QPushButton is clicked

        Delete selected variables
        :param items: Delete given varItems
        :type items: list
        """
        if items is None:
            selItems = self.twVar.selectedItems() or []
        else:
            selItems = items
        for item in selItems:
            self.twVar.takeTopLevelItem(self.twVar.indexOfTopLevelItem(item))
        self.rf_columnSize()

    def on_moveVar(self, side):
        """
        Move selected variable up or down

        :param side: 'up' or 'down'
        :type side: str
        :return: Moved index
        :rtype: list
        """
        movedIndex = []
        selItems = self.twVar.selectedItems() or []
        if side == 'down':
            selItems.reverse()
        for n, item in enumerate(selItems):
            #-- Get new index and datas --#
            newIndex = None
            curIndex = self.twVar.indexOfTopLevelItem(item)
            datas = self.getVarDatas(curIndex)
            if side == 'up':
                if curIndex > 0:
                    newIndex = (curIndex - 1)
            elif side == 'down':
                if curIndex < (len(pQt.getTopItems(self.twVar)) - 1):
                    newIndex = (curIndex + 1)
            #-- Move Var --#
            if newIndex is not None:
                self.on_delVar(items=[item])
                newItem = self.on_addVar(index=newIndex)
                self.setDatas(newItem, datas)
                movedIndex.append(newIndex)
        #-- Refresh Tree --#
        treeDatas = self.getDatas()
        self.twVar.clear()
        self.buildTree(treeDatas)
        #-- select Back --#
        allItems = pQt.getTopItems(self.twVar)
        for index in sorted(movedIndex):
            allItems[index].setSelected(True)
        return sorted(movedIndex)

    def on_copyVar(self):
        """
        Command launched when 'Copy Var' QAction is triggered

        Copy selected items datas to buffer
        """
        self.log.detail(">>> Copy var datas ...")
        selItems = self.twVar.selectedItems() or []
        self.mainUi.varBuffer = dict()
        for n, item in enumerate(selItems):
            self.mainUi.varBuffer[n] = self.getVarDatas(self.twVar.indexOfTopLevelItem(item))

    def on_pasteVar(self):
        """
        Command launched when 'Paste Var' QAction is triggered

        Paste stored items datas from buffer
        :return: Pasted items
        :rtype: list
        """
        self.log.detail(">>> Paste var datas ...")
        pastedItems = []
        if self.mainUi.varBuffer:
            for n, varDict in sorted(self.mainUi.varBuffer.iteritems()):
                newItem = self.on_addVar()
                self.setDatas(newItem, varDict)
                pastedItems.append(newItem)
        return pastedItems

    def on_stateButton(self, item):
        """
        Command launched when 'State' QPushButton is clicked

        :param item: Variable item
        :type item: QtGui.QTreeWidgetItem
        """
        self.rf_stateIcon(item._wState)
        for w in [item._wLabel, item._wType, item._wValue, item._wComment]:
            w.setEnabled(item._wState.isChecked())

    def new_varItem(self):
        """
        Create variable item

        :return: Variable item
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = QtGui.QTreeWidgetItem()
        newItem.setTextAlignment(0, 5)
        newItem._wState = self.new_itemButton(icon=self.mainUi.graphZone.enabledIcon,
                                              checkable=True, checked=True)
        # noinspection PyUnresolvedReferences
        newItem._wState.clicked.connect(partial(self.on_stateButton, newItem))
        newItem._wLabel = QtGui.QLineEdit()
        newItem._wType = QtGui.QComboBox()
        newItem._wType.addItems([' = ', ' + '])
        newItem._wValue = QtGui.QLineEdit()
        newItem._wComment = QtGui.QLineEdit()
        return newItem

    @staticmethod
    def new_itemButton(icon=None, checkable=False, checked=False, flat=False, cmd=None):
        """
        Create pushButton

        :param icon: Icon widget
        :type icon: QtGui.QIcon
        :param checkable: Chackable state
        :type checkable:bool
        :param checked: Checked state
        :type checked: bool
        :param flat: Flat mode
        :type flat: bool
        :param cmd: Command launched when clicked
        :type cmd: function
        :return: New button
        :rtype: QtGui.QPushButton
        """
        newWidget = QtGui.QPushButton()
        if icon is not None:
            newWidget.setIcon(icon)
        newWidget.setCheckable(checkable)
        newWidget.setChecked(checked)
        newWidget.setFlat(flat)
        if cmd is not None:
            # noinspection PyUnresolvedReferences
            newWidget.clicked.connect(cmd)
        return newWidget


class Logs(QtGui.QWidget, wgLogsUI.Ui_wgLogs):

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.detail("\t ---> Init Logs Widget.")
        super(Logs, self).__init__()
        self._setupWidget()
        self.rf_waitVisibility()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        self.log.detail("\t ---> Setup Logs Widget.")
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        #-- Jobs --#
        self.twJobs.itemClicked.connect(self.updateLog)
        self.pbGetJobs.clicked.connect(self.on_getJobs)
        self.pbDelJobs.clicked.connect(self.on_delJobs)
        self.cbWordWrap.clicked.connect(self.rf_wordWrap)
        self.cbShowXterm.clicked.connect(self.rf_waitVisibility)
        #-- Logs --#
        scriptFont = QtGui.QFont('Courier', 8, QtGui.QFont.Monospace)
        scriptFont.setFixedPitch(True)
        metrics = QtGui.QFontMetrics(scriptFont)
        self.teLogs.setTabStopWidth(4 * metrics.width(' '))
        self.teLogs.setFont(scriptFont)
        self.teLogs.setStyleSheet("background-color: rgb(35, 35, 35);"
                                  "color: rgb(220, 220, 220);")

    @property
    def showXterm(self):
        """
        Get 'Show Xterm' QCheckBox state

        :return: Show xterm state
        :type: bool
        """
        return self.cbShowXterm.isChecked()

    @property
    def waitAtEnd(self):
        """
        Get 'Wait At End' QCheckBox state

        :return: Wait at end state
        :type: bool
        """
        return self.cbWaitAtEnd.isChecked()

    def rf_wordWrap(self):
        if self.cbWordWrap.isChecked():
            self.teLogs.setWordWrapMode(QtGui.QTextOption.WrapAnywhere)
        else:
            self.teLogs.setWordWrapMode(QtGui.QTextOption.NoWrap)

    def rf_waitVisibility(self):
        self.cbWaitAtEnd.setEnabled(self.cbShowXterm.isChecked())

    def addJob(self, logFile):
        """
        Add job to 'Jobs' tree

        :param logFile: Log file
        :type logFile: str
        """
        self.twJobs.clearSelection()
        self.teLogs.clear()
        newItem = QtGui.QTreeWidgetItem()
        newItem.logFile = logFile
        newItem.setText(0, '--'.join(os.path.basename(logFile).split('.')[0].split('--')[1:]))
        self.twJobs.insertTopLevelItem(0, newItem)

    def updateLog(self):
        """
        Update log with selected job item
        """
        self.teLogs.clear()
        selItems = self.twJobs.selectedItems() or []
        if len(selItems) == 1:
            #-- Update Text --#
            log = pFile.readFile(selItems[0].logFile)
            self.teLogs.setPlainText(''.join(log))
            #-- Scroll To Bottom --#
            sb = self.teLogs.verticalScrollBar()
            sb.setValue(sb.maximum())

    def on_getJobs(self):
        """
        Command launched when 'Get Jobs' QPushButton is clicked.

        Import jobs for current graphFile
        """
        self.twJobs.clear()
        logPath = os.path.join(self.mainUi.grapher.graphTmpPath, 'logs')
        logFiles = os.listdir(logPath) or []
        for logFile in logFiles:
            self.addJob(os.path.join(logPath, logFile))
        if not logFiles:
            self.log.info("No log files to import: %s" % pFile.conformPath(logPath))

    def on_delJobs(self):
        """
        Command launched when 'Del Jobs' QPushButton is clicked.

        Delete selected jobs for current graphFile
        """
        self.teLogs.clear()
        selItems = self.twJobs.selectedItems() or []
        for item in selItems:
            try:
                os.remove(item.logFile)
                self.log.detail("delete %s" % item.logFile)
            except:
                self.log.error("!!! Can not delete logFile: %s !!!" % item.logFile)
        self.on_getJobs()
