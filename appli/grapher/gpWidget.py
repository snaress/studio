from PyQt4 import QtGui, QtCore
from functools import partial
from lib.qt import textEditor
from lib.qt import procQt as pQt
from appli.grapher.ui import wgVariablesUI


class Comment(textEditor.TextEditor):

    def __init__(self, ui):
        self._ui = ui
        self.log = self._ui.log
        super(Comment, self).__init__()
        self._setupWidget()

    def _setupWidget(self):
        """ Setup Comment widget """
        self.log.debug("#-- Setup Comment Widget --#")
        self._ui.cbComment.clicked.connect(self.rf_widgetVis)

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


class Variables(QtGui.QMainWindow, wgVariablesUI.Ui_mwVariables):

    def __init__(self, ui):
        self._ui = ui
        self.log = self._ui.log
        self.buffer = None
        super(Variables, self).__init__()
        self._setupWidget()

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
        self.connect(self.twVariables, QtCore.SIGNAL('customContextMenuRequested(const QPoint&)'),
                     self.on_popUpMenu)

    # noinspection PyUnresolvedReferences
    def _menuEdit(self):
        """ Setup menu 'Edit' """
        self.miAdd.triggered.connect(partial(self.on_addVar, index=None))
        self.miAdd.setShortcut("Ctrl+A")
        self.miDel.triggered.connect(self.on_delVar)
        self.miDel.setShortcut("Del")
        self.miCopy.triggered.connect(partial(self.on_copy, keepSelection=False))
        self.miCopy.setShortcut("Ctrl+C")
        self.miCut.triggered.connect(self.on_cut)
        self.miCut.setShortcut("Ctrl+X")
        self.miPaste.triggered.connect(partial(self.on_paste, newIdex=None))
        self.miPaste.setShortcut("Ctrl+V")
        self.miMoveUp.triggered.connect(partial(self.on_move, 'up'))
        self.miMoveUp.setShortcut("Ctrl+Up")
        self.miMoveDn.triggered.connect(partial(self.on_move, 'down'))
        self.miMoveDn.setShortcut("Ctrl+Down")

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
