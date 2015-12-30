import os, pprint
from PyQt4 import QtGui
from functools import partial
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.fondation.gui.common._ui import treeWidgetSettingsUI


class TreeWidgetSettings(QtGui.QWidget, treeWidgetSettingsUI.Ui_wg_treeWidget):

    iconPath = "%s/_lib/icon/png" % '/'.join(pFile.conformPath(os.path.dirname(__file__)).split('/')[:-1])

    def __init__(self):
        super(TreeWidgetSettings, self).__init__()
        self._setupUi()

    def _setupUi(self):
        """
        Setup TreeWidgetSettings widget
        """
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.tw_tree.setIndentation(0)
        self.tw_tree.setAlternatingRowColors(True)
        self._setupIcons()
        self._setupConnections()
        self.rf_headers()
        self.rf_toolTips()

    def _setupIcons(self):
        """
        Setup TreeWidgetSettings icons
        """
        #-- Init Icons --#
        self.iconUp = QtGui.QIcon(os.path.join(self.iconPath, 'arrowUpBlue.png'))
        self.iconDn = QtGui.QIcon(os.path.join(self.iconPath, 'arrowDnBlue.png'))
        self.iconAdd = QtGui.QIcon(os.path.join(self.iconPath, 'add.png'))
        self.iconDel = QtGui.QIcon(os.path.join(self.iconPath, 'del.png'))
        self.iconEdit = QtGui.QIcon(os.path.join(self.iconPath, 'edit.png'))
        self.iconApply = QtGui.QIcon(os.path.join(self.iconPath, 'apply.png'))
        self.iconCancel = QtGui.QIcon(os.path.join(self.iconPath, 'cancel.png'))
        #-- Add Icons --#
        self.pb_itemUp.setIcon(self.iconUp)
        self.pb_itemDn.setIcon(self.iconDn)
        self.pb_add.setIcon(self.iconAdd)
        self.pb_del.setIcon(self.iconDel)
        self.pb_edit1.setIcon(self.iconEdit)
        self.pb_edit2.setIcon(self.iconEdit)
        self.pb_apply.setIcon(self.iconApply)
        self.pb_cancel.setIcon(self.iconCancel)

    # noinspection PyUnresolvedReferences
    def _setupConnections(self):
        """
        Setup TreeWidgetSettings connections
        """
        self.pb_itemUp.clicked.connect(partial(self.on_moveItem, 'up'))
        self.pb_itemDn.clicked.connect(partial(self.on_moveItem, 'down'))
        self.pb_add.clicked.connect(self.on_addItem)
        self.pb_del.clicked.connect(self.on_delItem)
        self.pb_edit1.clicked.connect(self.on_editItem1)
        self.pb_edit2.clicked.connect(self.on_editItem2)
        self.pb_apply.clicked.connect(self.on_apply)
        self.pb_cancel.clicked.connect(self.on_cancel)

    def getDatas(self, asString=False):
        """
        Get tree datas

        :param asString: Return string instead of dict
        :type asString: bool
        :return: Tree datas
        :rtype: dict
        """
        datas = dict()
        for n, item in enumerate(pQt.getAllItems(self.tw_tree)):
            datas[n] = item.itemObj.getDatas()
        if asString:
            return pprint.pformat(datas)
        return datas

    def getItemFromAttrValue(self, attr, value):
        """
        Get tree item from attribute and value

        :param attr: Item attribute name
        :type attr: str
        :param value: Item attribute value
        :type value: str
        :return: Tree item
        :rtype: QtGui.QtreeWidgetItem
        """
        for item in pQt.getAllItems(self.tw_tree):
            if hasattr(item.itemObj, attr):
                if getattr(item.itemObj, attr) == value:
                    return item

    def rf_toolTips(self):
        """
        Refresh widgets toolTips
        """
        self.log.detail("#----- Refresh ToolTips -----#")
        if not self.mainUi.showToolTips:
            wList = [self.pb_itemUp, self.pb_itemDn, self.pb_add, self.pb_del, self.pb_edit1, self.pb_edit2,
                     self.pb_apply, self.pb_cancel]
            for widget in wList:
                widget.setToolTip('')

    def rf_headers(self, *args):
        """
        Refresh treeWidget headers

        :param args: header labels
        :type args: list
        """
        newHeader = QtGui.QTreeWidgetItem()
        if not args:
            self.tw_tree.setColumnCount(1)
            newHeader.setText(0, 'None')
        else:
            self.tw_tree.setColumnCount(len(args))
            for n, label in enumerate(args):
                newHeader.setText(n, label)
        self.tw_tree.setHeaderItem(newHeader)

    def rf_treeColumns(self):
        """
        Refresh tree column size
        """
        for n in range(self.tw_tree.columnCount()):
            self.tw_tree.resizeColumnToContents(n)

    def buildTree(self):
        """
        Build tree widget
        """
        self.log.detail(">>> Build tree ...")
        self.tw_tree.clear()

    def new_treeItem(self, itemObj):
        """
        Create or update group tree item widget

        :param itemObj: Group core object
        :type itemObj: appli.fondation.core.fondation.userGroups.Group
        :return: New group item
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = QtGui.QTreeWidgetItem()
        newItem.itemObj = itemObj
        self.ud_treeItem(newItem)
        for n in range(self.tw_tree.columnCount()):
            newItem.setTextAlignment(n, 5)
        return newItem

    def ud_treeItem(self, item, **kwargs):
        """
        Update item datas and settings

        :param item: Tree item
        :type item: QtGui.QTreeWidgetItem
        :param kwargs: Item datas
        :type kwargs: dict
        """
        #-- Store Datas --#
        item.itemObj.setDatas(**kwargs)

    def on_moveItem(self, side):
        """
        Command launched when 'Up' or 'Down' QPushButton is clicked

        Move selected item
        :param side: 'up' or 'down'
        :type side: str
        """
        self.log.detail(">>> Launch 'Move Item': %s <<<" % side)
        selItems = self.tw_tree.selectedItems() or []
        if selItems:
            movedItem = None
            #-- Get Current Index --#
            if selItems[0].parent() is None:
                parent = None
                index = self.tw_tree.indexOfTopLevelItem(selItems[0])
            else:
                parent = selItems[0].parent()
                index = parent.indexOfChild(selItems[0])
            #-- Move Up --#
            if side == 'up':
                if index > 0:
                    if parent is None:
                        movedItem = self.tw_tree.takeTopLevelItem(self.tw_tree.indexOfTopLevelItem(selItems[0]))
                        self.tw_tree.insertTopLevelItem((index - 1), movedItem)
                    else:
                        movedItem = parent.takeChild(parent.indexOfChild(selItems[0]))
                        parent.insertChild((index - 1), movedItem)
            #-- Move Down --#
            else:
                if index < (self.tw_tree.topLevelItemCount() - 1):
                    if parent is None:
                        movedItem = self.tw_tree.takeTopLevelItem(self.tw_tree.indexOfTopLevelItem(selItems[0]))
                        self.tw_tree.insertTopLevelItem((index + 1), movedItem)
                    else:
                        movedItem = parent.takeChild(parent.indexOfChild(selItems[0]))
                        parent.insertChild((index + 1), movedItem)
            #-- Select Moved Item --#
            if movedItem is not None:
                self.tw_tree.clearSelection()
                for item in pQt.getAllItems(self.tw_tree):
                    if item == movedItem:
                        self.tw_tree.setItemSelected(movedItem, True)

    def on_addItem(self):
        """
        Command launched when 'Add' QPushButton is clicked

        Add new item to tree
        """
        self.log.detail(">>> Launch 'Add' <<<")

    def on_delItem(self):
        """
        Command launched when 'Del' QPushButton is clicked

        Delete selected item from tree
        """
        self.log.detail(">>> Launch 'Del' <<<")
        selItems = self.tw_tree.selectedItems() or []
        if selItems:
            if selItems[0].parent() is None:
                self.tw_tree.takeTopLevelItem(self.tw_tree.indexOfTopLevelItem(selItems[0]))
            else:
                selItems[0].parent().takeChild(selItems[0].parent().indexOfChild(selItems[0]))

    def on_editItem1(self):
        """
        Command launched when 'Edit1' QPushButton is clicked

        Launch editing dialog
        """
        self.log.detail(">>> Launch 'Edit Item 1' <<<")

    def on_editItem2(self):
        """
        Command launched when 'Edit2' QPushButton is clicked

        Launch editing dialog
        """
        self.log.detail(">>> Launch 'Edit Item 2' <<<")

    def on_apply(self):
        """
        Command launched when 'Apply' QPushButton is clicked

        Store datas to itemObject
        """
        self.log.detail(">>> Launch 'Apply' <<<")
        self.__edited__ = True

    def on_cancel(self):
        """
        Command launched when 'Cancel' QPushButton is clicked

        Restore datas from itemObject
        """
        self.log.detail(">>> Launch 'Cancel' <<<")
        self.buildTree()
