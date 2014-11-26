from PyQt4 import QtGui, QtCore
from functools import partial
from lib.qt import procQt as pQt
from lib.qt import textEditor, scriptEditor
from appli.grapher.ui import wgVariablesUI, nodeEditorUI


class Comment(textEditor.TextEditor):

    def __init__(self, ui):
        self._ui = ui
        self.log = self._ui.log
        self.buffer = None
        super(Comment, self).__init__()
        self._setupWidget()

    @property
    def comment(self):
        return {'html': str(self.teText.toHtml()), 'text': str(self.teText.toPlainText())}

    def _setupWidget(self):
        """ Setup Comment widget """
        self.log.debug("#-- Setup Comment Widget --#")
        self._ui.cbComment.clicked.connect(self.rf_widgetVis)
        self.bClearText.setToolTip("Cancel Edition")
        self.bLoadFile.setToolTip("Start Edition")
        self.bSaveFile.setToolTip("Save Edition")

    def rf_widgetVis(self):
        """ Refresh Comment visibility """
        self.log.debug("\t Refresh Comment widget visibility ...")
        if self._ui.cbComment.isChecked():
            self.setVisible(True)
            self.parent().setMinimumHeight(40)
            self.parent().setMaximumHeight(self._ui.maximumHeight())
        else:
            self.setVisible(False)
            self.parent().setMinimumHeight(20)
            self.parent().setMaximumHeight(20)

    def rf_menuVis(self, state=False):
        """ Refresh menu visibility
            :param state: (bool) : Visibility state """
        self.log.debug("\t Refresh Comment menu visibility ...")
        self.bClearText.setEnabled(state)
        self.bLoadFile.setEnabled(not state)
        self.bSaveFile.setEnabled(state)
        for grp in [self.editActionGrp, self.textActionGrp, self.fontActionGrp]:
            for widget in grp:
                widget.setEnabled(state)
        self.teText.setReadOnly(not state)

    def rf_comment(self, textHtml):
        """ Refresh Grapher comment
            :param textHtml: (str) : Comment in html form """
        self.log.debug("\t Refresh Comment ...")
        self.teText.setHtml(textHtml)

    def on_clearText(self):
        """ Switch widget visibility to disable edition and restore text """
        self.log.debug("\t Restore text ...")
        super(Comment, self).on_clearText()
        self.teText.setHtml(self.buffer)
        self.rf_menuVis()
        self.buffer = None

    def on_loadFile(self):
        """ Switch widget visibility to enable edition """
        self.log.debug("\t Enable edition ...")
        self.buffer = self.teText.toHtml()
        self.rf_menuVis(state=True)

    def on_saveFile(self):
        """ Switch widget visibility to disable edition and save text """
        self.log.debug("\t Disable Edition ...")
        self.buffer = None
        self.rf_menuVis()
        if self._ui.objectName() == 'mwGrapher':
            self._ui.gp.gpComment = self.comment

    def clearComment(self):
        """ Reset Grapher comment """
        self.log.debug("\t Clear Comment ...")
        self.teText.clear()


class Variables(QtGui.QMainWindow, wgVariablesUI.Ui_mwVariables):

    def __init__(self, ui):
        self._ui = ui
        self.log = self._ui.log
        self.buffer = None
        super(Variables, self).__init__()
        self._setupWidget()

    @property
    def varData(self):
        """ Get variable data
            :return: (dict) : Variable data """
        varDict = {}
        items = pQt.getTopItems(self.twVariables)
        for n, item in enumerate(items):
            index = str(n + 1).zfill(2)
            varDict['var%s' % index] = self.getItemDict(item)
        return varDict

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        """ Setup Variables widget """
        self.log.debug("#-- Setup Variables Widget --#")
        self.setupUi(self)
        self._ui.cbVariables.clicked.connect(self.rf_widgetVis)
        self._menuEdit()
        self.twVariables.header().setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        self.twVariables.header().setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        self.twVariables.header().setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        self.connect(self.twVariables, QtCore.SIGNAL('customContextMenuRequested(const QPoint&)'), self.on_popUpMenu)

    # noinspection PyUnresolvedReferences
    def _menuEdit(self):
        """ Setup menu 'Edit' """
        self.miAdd.triggered.connect(partial(self.on_addVar, index=None))
        self.miAdd.setShortcut("Ctrl+A")
        self.miDel.triggered.connect(self.on_delVar)
        self.miDel.setShortcut("Ctrl+Del")
        self.miCopy.triggered.connect(partial(self.on_copy, keepSelection=False))
        self.miCopy.setShortcut("Ctrl+C")
        self.miCut.triggered.connect(self.on_cut)
        self.miCut.setShortcut("Ctrl+X")
        self.miPaste.triggered.connect(partial(self.on_paste, newIndex=None))
        self.miPaste.setShortcut("Ctrl+V")
        self.miMoveUp.triggered.connect(partial(self.on_move, 'up'))
        self.miMoveUp.setShortcut("Ctrl+Up")
        self.miMoveDn.triggered.connect(partial(self.on_move, 'down'))
        self.miMoveDn.setShortcut("Ctrl+Down")
        self.miPush.triggered.connect(self.on_push)
        self.miPush.setShortcut("Alt+C")
        self.miPull.triggered.connect(self.on_pull)
        self.miPull.setShortcut("Alt+V")

    def rf_widgetVis(self):
        """ Refresh Variables visibility """
        self.log.debug("\t Refresh Variables widget visibility ...")
        if self._ui.cbVariables.isChecked():
            self.setVisible(True)
            self.parent().setMinimumHeight(40)
            self.parent().setMaximumHeight(self._ui.maximumHeight())
        else:
            self.setVisible(False)
            self.parent().setMinimumHeight(20)
            self.parent().setMaximumHeight(20)

    def rf_variables(self, **kwargs):
        """ Refresh Variables tree
            :param kwargs: (dict) : VarData dict """
        self.log.debug("\t Refresh Variables ...")
        self.twVariables.clear()
        for var in sorted(kwargs.keys()):
            newItem = self.on_addVar()
            self.setItem(newItem, **kwargs[var])
            self.on_varEnable(newItem)

    def on_addVar(self, index=None):
        """ Add new variable
            :param index: (int) : Index for item insertion
            :return: (object) : QTreeWidgetItem """
        self.log.debug("\t Add Variable ...")
        newItem = self.new_varItem()
        if index is None:
            self.twVariables.addTopLevelItem(newItem)
        else:
            self.twVariables.insertTopLevelItem(index, newItem)
        self.twVariables.setItemWidget(newItem, 1, newItem.wdgEnabled)
        self.twVariables.setItemWidget(newItem, 2, newItem.wdgLabel)
        self.twVariables.setItemWidget(newItem, 3, newItem.wdgType)
        self.twVariables.setItemWidget(newItem, 4, newItem.wdgValue)
        self.twVariables.setItemWidget(newItem, 5, newItem.wdgComment)
        newItem.wdgEnabled.clicked.connect(partial(self.on_varEnable ,newItem))
        return newItem

    def on_delVar(self):
        """ Delete selected variables """
        self.log.debug("\t Delete Variables ...")
        pQt.delSelItems(self.twVariables)
        self.reindexVar()

    def on_copy(self, keepSelection=False):
        """ Store selected items in buffer """
        self.log.debug("\t Copy Variables ...")
        selItems = self.twVariables.selectedItems() or []
        self.buffer = []
        for item in selItems:
            self.buffer.append(self.getItemDict(item))
        if not keepSelection:
            pQt.deselectAllItems(self.twVariables)

    def on_cut(self):
        """ Store and delete selected items """
        self.on_copy(keepSelection=True)
        self.log.debug("\t Copy Variables ...")
        self.on_delVar()

    def on_paste(self, newIndex=None):
        """ Paste items from buffer
            :param newIndex: (int) : New tree position
            :return: (list) : Pasted QTreeWidgetItems """
        self.log.debug("\t Paste Variables ...")
        selItems = self.twVariables.selectedItems() or []
        newItems = []
        for n, itemDict in enumerate(self.buffer):
            if newIndex is None:
                if len(selItems) == 1:
                    ind = self.twVariables.indexOfTopLevelItem(selItems[0])
                    newItem = self.on_addVar(index=(ind + n + 1))
                else:
                    newItem = self.on_addVar(index=None)
            else:
                newItem = self.on_addVar(index=newIndex)
            self.setItem(newItem, **itemDict)
            newItems.append(newItem)
        return newItems

    def on_move(self, side):
        """ Move up or down selected items
            :param side: (str) : 'up' or 'down' """
        self.log.debug("\t Move Variables %s ..." % side)
        selItems = self.twVariables.selectedItems() or []
        maxInd = (len(pQt.getAllItems(self.twVariables)) - 1)
        newItems = []
        if side == 'down':
            selItems.reverse()
        for item in selItems:
            ind = self.twVariables.indexOfTopLevelItem(item)
            pQt.deselectAllItems(self.twVariables)
            self.twVariables.setItemSelected(item, True)
            self.on_cut()
            if side == 'up':
                if not ind == 0:
                    result = self.on_paste(newIndex=(ind - 1))
                    newItems.append(result[0])
            elif side == 'down':
                if not ind == maxInd:
                    result = self.on_paste(newIndex=(ind + 1))
                    newItems.append(result[0])
        pQt.deselectAllItems(self.twVariables)
        self.reindexVar()
        for newItem in newItems:
            self.twVariables.setItemSelected(newItem, True)

    def on_push(self):
        self.log.warning("!!! Command to do !!!")
        #todo: Push variables

    def on_pull(self):
        self.log.warning("!!! Command to do !!!")
        #todo: pull variables

    def on_popUpMenu(self, point):
        """ Command launched when right click is done
            :param point: (object) : Qt position """
        self.mEdit.exec_(self.twVariables.mapToGlobal(point))

    @staticmethod
    def on_varEnable(item):
        """ Enable or disable variable when QCheckBox is clicked
            :param item: (object) : QTreeWidgetItem"""
        state = item.wdgEnabled.isChecked()
        item.wdgLabel.setEnabled(state)
        item.wdgType.setEnabled(state)
        item.wdgValue.setEnabled(state)
        item.wdgComment.setEnabled(state)

    def reindexVar(self):
        """ Reindex variable items """
        for n, item in enumerate(pQt.getTopItems(self.twVariables)):
            item.setText(0, "%s" % (n + 1))

    @staticmethod
    def getItemDict(item):
        """ Get given treeItem dict
            :param item: (object) : QTreeWidgetItem
            :return: (dict) : Given item params """
        newDict = {}
        itemDict = item.__dict__
        newDict['enabled'] = itemDict['wdgEnabled'].isChecked()
        newDict['label'] = str(itemDict['wdgLabel'].text())
        newDict['type'] = str(itemDict['wdgType'].currentText())
        newDict['value'] = str(itemDict['wdgValue'].text())
        newDict['comment'] = str(itemDict['wdgComment'].text())
        return newDict

    @staticmethod
    def setItem(item, **kwargs):
        """ Set item with given params
            :param item: (object) : QTreeWidgetItem
            :param kwargs: (dict) : Item params """
        item.wdgEnabled.setChecked(kwargs['enabled'])
        item.wdgLabel.setText(kwargs['label'])
        item.wdgType.setCurrentIndex(item.wdgType.findText(kwargs['type']))
        item.wdgValue.setText(kwargs['value'])
        item.wdgComment.setText(kwargs['comment'])

    def new_varItem(self):
        """ Create new variable item
            :return: (object) : QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem.setText(0, str(len(pQt.getTopItems(self.twVariables)) + 1))
        newItem.wdgEnabled = self.new_varEnabledWidget()
        newItem.wdgLabel = self.new_varTextWidget()
        newItem.wdgType = self.new_varTypeWidget()
        newItem.wdgValue = self.new_varTextWidget()
        newItem.wdgComment = self.new_varTextWidget()
        return newItem

    @staticmethod
    def new_varEnabledWidget():
        """ Create new varEnable checkBox
            :return: (object) : QCheckBox """
        newWidget = QtGui.QCheckBox()
        newWidget.setChecked(True)
        return newWidget

    @staticmethod
    def new_varTypeWidget():
        """ Create new varType comboBox
            :return: (object) : QComboBox """
        newWidget = QtGui.QComboBox()
        newWidget.addItems(['=', '+', 'num'])
        return newWidget

    @staticmethod
    def new_varTextWidget():
        """ Create new varText lineEdit
            :return: (object) : QLineEdit """
        newWidget = QtGui.QLineEdit()
        return newWidget


class ScriptEditor(scriptEditor.ScriptEditor):

    def __init__(self, parent):
        self.parent = parent
        super(ScriptEditor, self).__init__()
        self._setupWidget()

    def _setupWidget(self):
        """ Setup ScriptEditor widget """
        self.tbEdit.setVisible(False)

    @property
    def script(self):
        """ Get script
            :return: (str) : Script """
        return str(self._widget.toPlainText())


class NodeEditor(QtGui.QWidget, nodeEditorUI.Ui_nodeEditor):

    def __init__(self, mainUi, ui):
        self.mainUi = mainUi
        self._ui = ui
        self.log = self._ui.log
        self.graphNode = None
        super(NodeEditor, self).__init__()
        self._setupUi()
        self._initUi()

    @property
    def nodeData(self):
        """ Get nodeDataClass from stored graphNode
            :return: (object) : NodeData class """
        if self.graphNode is not None:
            return self.graphNode.nodeData

    @property
    def nodeType(self):
        """ Ge current nodeType
            :return: (srt) : Node type """
        return str(self.cbNodeType.itemText(self.cbNodeType.currentIndex()))

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup NodeEditor widget """
        self.log.debug("#-- Setup Node Editor --#")
        self.setupUi(self)
        self.wgComment = Comment(self)
        self.vlComment.addWidget(self.wgComment)
        self.wgVariables = Variables(self)
        self.vlVariables.addWidget(self.wgVariables)
        self.wgScript = ScriptEditor(self)
        self.vlScript.addWidget(self.wgScript)
        self.cbNodeType.currentIndexChanged.connect(self.on_nodeType)
        self.cbTrash.clicked.connect(self.rf_trashVis)
        self.bSave.clicked.connect(self.on_save)

    def _initUi(self):
        """ Init NodeEditor widget """
        self.wgComment.rf_widgetVis()
        self.wgComment.rf_menuVis()
        self.wgVariables.rf_widgetVis()
        self.rf_trashVis()
        if self._ui.objectName() == 'mwGrapher':
            self.bClose.setVisible(False)
        self.on_nodeType()

    def _updateUi(self, graphNode=None):
        """ Update nodeEditor ui
            :param graphNode: (object) : QWidget """
        if graphNode is not None:
            self.graphNode = graphNode
        self.rf_nodeName()
        self.rf_nodeType()
        self.on_nodeType()

    def rf_nodeName(self):
        """ Refresh nodeName """
        if self.graphNode is None:
            self.leNodeName.clear()
        else:
            self.leNodeName.setText(self.nodeData.nodeName)

    def rf_nodeType(self):
        """ Refresh nodeType """
        if self.graphNode is None:
            self.cbNodeType.setCurrentIndex(self.cbNodeType.findText('modul'))
        else:
            self.cbNodeType.setCurrentIndex(self.cbNodeType.findText(self.nodeData.nodeType))

    def rf_trashVis(self):
        """ Refresh trash visibility """
        if self.cbTrash.isChecked():
            self.teTrash.setVisible(True)
            self.flTrash.setMinimumHeight(40)
            self.flTrash.setMaximumHeight(300)
        else:
            self.teTrash.setVisible(False)
            self.flTrash.setMinimumHeight(20)
            self.flTrash.setMaximumHeight(20)

    def ud_nodeType(self):
        """ Update graphNode type """
        self.nodeData.nodeType = self.nodeType

    def on_nodeType(self):
        """ Command launched when nodeType has changed """
        if self.nodeType in ['sysData', 'cmdData', 'purData']:
            self.qfLoop.setVisible(False)
            self.qfScript.setVisible(True)
            self.qfScriptSpacer.setVisible(False)
            if self.nodeType == 'cmdData':
                self.qfCmd.setVisible(True)
            else:
                self.qfCmd.setVisible(False)
        elif self.nodeType == 'loop':
            self.qfLoop.setVisible(True)
            self.qfScript.setVisible(False)
            self.qfScriptSpacer.setVisible(True)
            # self.on_loopType()
        elif self.nodeType == 'modul' or self.graphNode is None:
            self.qfLoop.setVisible(False)
            self.qfScript.setVisible(False)
            self.qfScriptSpacer.setVisible(True)
        if self.nodeType not in ['sysData', 'cmdData']:
            self.cbExecNode.setChecked(False)
            self.cbExecNode.setEnabled(False)
        else:
            self.cbExecNode.setEnabled(True)

    def on_save(self):
        """ Command launched when QPushButton 'Save' is clicked """
        self.ud_nodeType()
        self.graphNode.rf_nodeBgc()
