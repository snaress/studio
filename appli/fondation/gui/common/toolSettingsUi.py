import os
from PyQt4 import QtGui
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.fondation.gui.common._ui import toolSettingsDialogUI


class ToolSettings(QtGui.QMainWindow, toolSettingsDialogUI.Ui_mw_toolSettings):
    """
    ToolSettings common Class: Contain settings templates.
    """

    iconPath = "%s/_lib/icon/png" % '/'.join(pFile.conformPath(os.path.dirname(__file__)).split('/')[:-1])

    def __init__(self):
        super(ToolSettings, self).__init__()
        self.iconEnable = QtGui.QIcon(os.path.join(self.iconPath, 'enable.png'))
        self.iconDisable = QtGui.QIcon(os.path.join(self.iconPath, 'disable.png'))
        self._initSettings()
        self._setupUi()

    def _initSettings(self):
        """
        Init tool settings
        """
        self.log.detail("#===== Init Tool Settings =====#")

    def _initWidgets(self):
        """
        Init ToolSettings widgets
        """
        self.log.detail("#===== Init Tool Widgets =====#")
        #-- Category Font --#
        self.categoryFont = QtGui.QFont()
        self.categoryFont.setPointSize(10)
        self.categoryFont.setBold(True)

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup ToolSettings Ui
        """
        self.log.detail("#===== Setup ToolSettings Ui =====#")
        self.setupUi(self)
        self.setWindowTitle("ToolSettings | %s" % self.fondation.__user__)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.pb_save.setIcon(self.iconEnable)
        self.pb_save.clicked.connect(self.on_save)
        self.pb_close.setIcon(self.iconDisable)
        self.pb_close.clicked.connect(self.on_close)
        self.tw_category.clicked.connect(self.on_category)
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
                        item.setTextColor(0, QtGui.QColor(20, 20, 255))
                    else:
                        editedFont = QtGui.QFont()
                        editedFont.setItalic(False)
                        editedFont.setBold(False)
                        item.setFont(0, editedFont)
                        item.setTextColor(0, QtGui.QColor(0, 0, 0))

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
        if not selItems:
            self.qf_settingsWidget.setVisible(False)
        else:
            if selItems[0].itemType == 'category':
                self.qf_settingsWidget.setVisible(False)
            else:
                self.qf_settingsWidget.setVisible(True)
                for item in pQt.getAllItems(self.tw_category):
                    if hasattr(item, 'itemWidget'):
                        if item.itemWidget is not None:
                            if item.itemLabel == selItems[0].itemLabel:
                                item.itemWidget.setVisible(True)
                            else:
                                item.itemWidget.setVisible(False)
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
