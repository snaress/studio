import os
from PyQt4 import QtGui
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.foundation_old.gui.common._ui import dial_toolSettingsUI


class ToolSettings(QtGui.QDialog, dial_toolSettingsUI.Ui_dial_projectSettings):
    """
    ToolSettings common Class: Edit tool settings

    :param parent: Parent Ui
    :type parent: ProjectSettings
    """

    iconPath = "%s/_lib/icon/png" % '/'.join(pFile.conformPath(os.path.dirname(__file__)).split('/')[:-1])

    def __init__(self, parent=None):
        super(ToolSettings, self).__init__(parent)
        self.iconEnable = QtGui.QIcon(os.path.join(self.iconPath, 'enable.png'))
        self.iconDisable = QtGui.QIcon(os.path.join(self.iconPath, 'disable.png'))
        self._initSettings()
        self._setupUi()

    def _initSettings(self):
        """
        Init tool settings
        """
        self.log.detail("#===== Init Tool Settings =====#", newLinesBefore=1)

    def _initWidgets(self):
        """
        Init ToolSettings widgets
        """
        self.setWindowTitle("ToolSettings | %s" % self.foundation.__user__)
        #-- Category Font --#
        self.categoryFont = QtGui.QFont()
        self.categoryFont.setPointSize(10)
        self.categoryFont.setBold(True)

    def _setupUi(self):
        """
        Setup ToolSettings Ui
        """
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        #-- Icons --#
        self.pb_save.setIcon(self.iconEnable)
        self.pb_close.setIcon(self.iconDisable)
        #-- Connect --#
        self.tw_category.clicked.connect(self.on_category)
        self.pb_save.clicked.connect(self.on_save)
        self.pb_close.clicked.connect(self.on_close)
        #-- Update --#
        self._initWidgets()
        self.buildCategoryTree()

    @property
    def category(self):
        """
        Get settings category

        :return: Category datas
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
                if item.itemWidget is not None:
                    if item.itemWidget.__edited__:
                        editedFont = QtGui.QFont()
                        editedFont.setItalic(True)
                        editedFont.setBold(True)
                        item.setFont(0, editedFont)
                        item.setTextColor(0, QtGui.QColor(100, 150, 255))
                    else:
                        editedFont = QtGui.QFont()
                        editedFont.setItalic(False)
                        editedFont.setBold(False)
                        item.setFont(0, editedFont)
                        item.setTextColor(0, QtGui.QColor(220, 220, 220))

    def buildCategoryTree(self):
        """
        Build category Tree widget
        """
        self.log.detail("Build Category Tree ...")
        self.tw_category.clear()
        categoryDict = self.category
        for n in sorted(categoryDict.keys()):
            cat = categoryDict[n].keys()[0]
            catItem = self.new_categoryItem('category', **categoryDict[n][cat])
            self.tw_category.addTopLevelItem(catItem)
            for nn in sorted(categoryDict[n][cat]['subCat'].keys()):
                subCat = categoryDict[n][cat]['subCat'][nn].keys()[0]
                subCatItem = self.new_categoryItem('subCategory', **categoryDict[n][cat]['subCat'][nn][subCat])
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
                if selItems[0].itemWidget is not None:
                    selItems[0].itemWidget.buildTree()

    def on_save(self):
        """
        Command launched when 'Save' QPushButton is clicked

        Save settings to disk
        """
        self.log.debug("#--- Save Settings ---#")

    def on_close(self):
        """
        Command launched when 'Close' QPushButton is clicked

        Close settings ui
        """
        editedItems = self.getEditedItems()
        #-- Edited Widget Found --#
        if editedItems:
            message = ["!!! Warning !!!",
                       "Unsaved category detected:"]
            for item in editedItems:
                message.append("---> %s" % item.itemLabel)
            self.cd_closeSettings = pQt.ConfirmDialog('\n'.join(message), ['Save', 'Discard'],
                                                      [self._saveSettings, self._discardSettings])
            self.cd_closeSettings.setStyleSheet(self.parent()._styleSheet)
            self.cd_closeSettings.exec_()
        #-- Close Settings --#
        else:
            self.close()

    def _saveSettings(self):
        """
        Save action confirmed
        """
        self.on_save()
        self.cd_closeSettings.close()
        self.close()

    def _discardSettings(self):
        """
        Discard action confirmed
        """
        self._initSettings()
        self.cd_closeSettings.close()
        self.close()
