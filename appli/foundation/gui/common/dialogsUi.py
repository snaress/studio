import os
from PyQt4 import QtGui
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.foundation.gui.common._ui import dial_settingsUI


class ToolSettings(QtGui.QDialog, dial_settingsUI.Ui_dial_settings):
    """
    ToolSettings common Class: Edit tool settings

    :param parent: Parent Ui
    :type parent: Foundation
    """

    iconPath = "%s/_lib/icon/png" % '/'.join(pFile.conformPath(os.path.dirname(__file__)).split('/')[:-1])

    def __init__(self, parent=None):
        super(ToolSettings, self).__init__(parent)
        #-- Icons --#
        self.iconEnable = QtGui.QIcon(os.path.join(self.iconPath, 'enable.png'))
        self.iconDisable = QtGui.QIcon(os.path.join(self.iconPath, 'disable.png'))
        #-- Setup --#
        self._initSettings()
        self._setupUi()

    def _initSettings(self):
        """
        Init dialog settings
        """
        self.log.detail("#===== Init Settings Dialog =====#", newLinesBefore=1)

    def _initWidgets(self):
        """
        Init ToolSettings widgets
        """
        self.setWindowTitle("Settings | %s" % self.foundation.__user__)
        #-- Category Font --#
        self.categoryFont = QtGui.QFont()
        self.categoryFont.setPointSize(10)
        self.categoryFont.setBold(True)
        #-- Edited SubCategory Font --#
        self.editedSubCategoryFont = QtGui.QFont()
        self.editedSubCategoryFont.setItalic(True)
        self.editedSubCategoryFont.setBold(True)

    def _setupUi(self):
        """
        Setup dialog settings Ui
        """
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        #-- Icons --#
        self.pb_save.setIcon(self.iconEnable)
        self.pb_close.setIcon(self.iconDisable)
        #-- Connect --#
        self.tw_category.clicked.connect(self.on_category)
        #-- Update --#
        self._initWidgets()
        self.buildTree()

    @property
    def category(self):
        """
        Get settings category

        :return: Category data
        :rtype: dict
        """
        return dict()

    def getEditedItems(self):
        """
        Get edited subCategory items

        :return: Edited subCategory items
        :rtype: list
        """
        editedItems = []
        for item in pQt.getAllItems(self.tw_category):
            if item.itemType == 'subCategory':
                if item.itemWidget is not None:
                    if item.itemWidget.__edited__:
                        editedItems.append(item)
        return editedItems

    def rf_editedItemStyle(self):
        """
        Refresh catecory style
        """
        for item in pQt.getAllItems(self.tw_category):
            if item.itemType == 'subCategory':
                if item in self.getEditedItems():
                    item.setFont(0, self.editedSubCategoryFont)
                    item.setTextColor(0, QtGui.QColor(100, 150, 255))
                else:
                    item.setFont(0, QtGui.QFont())
                    item.setTextColor(0, QtGui.QColor(220, 220, 220))

    def buildTree(self):
        """
        Build category Tree widget
        """
        self.log.detail("Build Category Tree ...")
        self.tw_category.clear()
        categoryDict = self.category
        for n in sorted(categoryDict.keys()):
            cat = categoryDict[n].keys()[0]
            catDict = categoryDict[n][cat]
            catItem = self.new_categoryItem('category', **catDict)
            self.tw_category.addTopLevelItem(catItem)
            for nn in sorted(catDict['subCat'].keys()):
                subCat = catDict['subCat'][nn].keys()[0]
                subCatItem = self.new_categoryItem('subCategory', **catDict['subCat'][nn][subCat])
                catItem.addChild(subCatItem)
        self.tw_category.expandAll()

    def new_categoryItem(self, itemType, **kwargs):
        """
        Create category tree item widget

        :param itemType: 'category' or 'subCategory'
        :type itemType: str
        :param kwargs: Category params ('code', 'label', 'widget')
        :type kwargs: dict
        :return: New category item
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = QtGui.QTreeWidgetItem()
        #-- Set Datas --#
        newItem.itemType = itemType
        newItem.itemCode = kwargs['code']
        newItem.itemLabel = kwargs['label']
        if itemType == 'subCategory':
            newItem.itemWidget = kwargs['widget']
        #-- Edit Item --#
        newItem.setText(0, newItem.itemLabel)
        if itemType == 'category':
            newItem.setFont(0, self.categoryFont)
        return newItem

    def on_category(self):
        """
        Command launched when 'Category' tree item widget is clicked

        Update settings
        """
        selItems = self.tw_category.selectedItems() or []
        #-- Update Display --#
        if not selItems:
            self.qf_settingsWidget.setVisible(False)
        else:
            if selItems[0].itemType == 'category':
                self.qf_settingsWidget.setVisible(False)
            else:
                self.qf_settingsWidget.setVisible(True)
                #-- Reset Visibility (resize bug) --#
                for item in pQt.getAllItems(self.tw_category):
                    if hasattr(item, 'itemWidget'):
                        if item.itemWidget is not None:
                            item.itemWidget.setVisible(False)
                #-- Edit Visibility --#
                for item in pQt.getAllItems(self.tw_category):
                    if hasattr(item, 'itemWidget'):
                        if item.itemWidget is not None:
                            if item.itemLabel == selItems[0].itemLabel:
                                item.itemWidget.setVisible(True)
                #-- Build Tree --#
                # if selItems[0].itemWidget is not None:
                #     selItems[0].itemWidget.buildTree()