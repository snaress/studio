import os
from PyQt4 import QtGui
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.fondation.gui.fondation.settings import userGroupsUi
from appli.fondation.gui.fondation.settings._ui import settingsUI, userGroupsUI


class SettingsUi(QtGui.QMainWindow, settingsUI.Ui_mw_toolSettings):
    """
    SettingsUi Class: Contains fondation settings, child of FondationUi

    :param logLvl : Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    :param mainUi: Parant main ui
    :type mainUi: FondationUi
    """

    log = pFile.Logger(title="ToolSettingsUi")

    def __init__(self, mainUi, logLvl='info'):
        self.log.level = logLvl
        self.mainUi = mainUi
        self.fondation = self.mainUi.fondation
        super(SettingsUi, self).__init__()
        self.iconEnable = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'enable.png'))
        self.iconDisable = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'disable.png'))
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup QtGui ToolSettings Ui
        """
        self.log.detail("#===== Setup ToolSettings Ui =====#", newLinesBefor=1)
        self.setupUi(self)
        self.setWindowTitle("Fondation | ToolSettings | %s" % self.fondation.__user__)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self._initWidgets()
        self.buildCategoryTree()
        self.tw_category.clicked.connect(self.on_category)
        self.qf_settingsWidget.setVisible(False)
        self.pb_save.setIcon(self.iconEnable)
        self.pb_close.setIcon(self.iconDisable)
        self.pb_close.clicked.connect(self.close)

    def _initWidgets(self):
        """
        Init ToolSettings widgets
        """
        self.wgUserGrps = userGroupsUi.UserGroupsUi(self)
        self.vl_settingsWidget.addWidget(self.wgUserGrps)
        self.wgUserGrps.setVisible(False)

    @property
    def category(self):
        """
        Get settings category

        :return: Category datas
        :rtype: dict
        """
        return {0: {'userGroups': {'widget': self.wgUserGrps,
                                   'code': 'userGroups',
                                   'label': 'User Groups',
                                   'subCat': {0: {'groups': {'widget': self.wgUserGrps.qf_userGroups,
                                                             'code': 'groups',
                                                             'label': 'Groups'}},
                                              1: {'users': {'widget': self.wgUserGrps.qf_users,
                                                            'code': 'users',
                                                            'label': 'Users'}}}}}}

    def buildCategoryTree(self):
        """
        Build category Tree widget
        """
        self.log.detail("Build Category Tree ...")
        self.tw_category.clear()
        catDict = self.category
        for n in sorted(catDict.keys()):
            cat = catDict[n].keys()[0]
            catItem = self.new_categoryItem('category',
                                            catDict[n][cat]['code'],
                                            catDict[n][cat]['label'],
                                            catDict[n][cat]['widget'])
            self.tw_category.addTopLevelItem(catItem)
            for nn in sorted(catDict[n][cat]['subCat'].keys()):
                    subCat = catDict[n][cat]['subCat'][nn].keys()[0]
                    subCatItem = self.new_categoryItem('subCategory',
                                                       catDict[n][cat]['subCat'][nn][subCat]['code'],
                                                       catDict[n][cat]['subCat'][nn][subCat]['label'],
                                                       catDict[n][cat]['subCat'][nn][subCat]['widget'])
                    catItem.addChild(subCatItem)

    @staticmethod
    def new_categoryItem(itemType, itemCode, itemLabel, itemWidget):
        """
        Create category tree item widget

        :param itemType: 'category' or 'subCategory'
        :type itemType: str
        :param itemCode: Tree item Code
        :type itemCode: str
        :param itemLabel: Tree item label
        :type itemLabel: str
        :param itemWidget: Widget to link to item
        :type itemWidget: QtGui.QWidget | QtGui.QFrame
        :return: New category item
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = QtGui.QTreeWidgetItem()
        newItem.itemType = itemType
        newItem.itemCode = itemCode
        newItem.itemLabel = itemLabel
        newItem.itemWidget = itemWidget
        newItem.setText(0, itemLabel)
        if itemType == 'category':
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setBold(True)
            newItem.setFont(0, font)
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
                    if item.itemLabel == selItems[0].parent().itemLabel or item.itemLabel == selItems[0].itemLabel:
                        item.itemWidget.setVisible(True)
                    else:
                        item.itemWidget.setVisible(False)
                selItems[0].parent().itemWidget.rf_widget(selItems[0].itemCode)