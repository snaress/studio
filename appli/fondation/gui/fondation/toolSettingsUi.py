from lib.system import procFile as pFile
from appli.fondation.gui.common import toolSettingsUi
from appli.fondation.gui.fondation import tsUserGroups, tsEntities


class ToolSettings(toolSettingsUi.ToolSettings):
    """
    ToolSettings Class: Contains fondation settings, child of FondationUi

    :param logLvl : Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    :param mainUi: Parent main ui
    :type mainUi: FondationUi
    """

    log = pFile.Logger(title="ToolSettingsUi")

    def __init__(self, mainUi, logLvl='info'):
        self.mainUi = mainUi
        self.log.level = logLvl
        self.log.info("########## Launching Tool Settings Ui ##########", newLinesBefore=1)
        self.fondation = self.mainUi.fondation
        self.userGrps = self.fondation.userGrps
        super(ToolSettings, self).__init__()

    def _initSettings(self):
        """
        Init Fondation settings
        """
        super(ToolSettings, self)._initSettings()
        self.fondation.storeSettings()
        self.fondation.userGrps.collecteUsers(userName=self.fondation.__user__)
        self.fondation.userGrps.buildGroupsFromSettings()

    def _initWidgets(self):
        """
        Init Fondation toolSettings widgets
        """
        super(ToolSettings, self)._initWidgets()
        self.setStyleSheet(self.mainUi._styleSheet)
        #-- UserGroups --#
        self.wgGroups = tsUserGroups.Groups(self)
        self.wgGroups.setVisible(False)
        self.vl_settingsWidget.addWidget(self.wgGroups)
        self.wgUsers = tsUserGroups.Users(self)
        self.wgUsers.setVisible(False)
        self.vl_settingsWidget.addWidget(self.wgUsers)
        #-- Entities --#
        self.wgEntities = tsEntities.Entities(self)
        self.wgEntities.setVisible(False)
        self.vl_settingsWidget.addWidget(self.wgEntities)

    @property
    def category(self):
        """
        Get settings category

        :return: Category datas
        :rtype: dict
        """
        return {0: self._userGroups,
                1: self._entities}

    @property
    def _userGroups(self):
        """
        Get UserGroups category

        :return: UserGroups category
        :rtype: dict
        """
        return {'userGroups': {'code': 'userGroups',
                               'label': 'User Groups',
                               'subCat': {0: {'groups': {'widget': self.wgGroups,
                                                         'code': 'groups',
                                                         'label': 'Groups'}},
                                          1: {'users': {'widget': self.wgUsers,
                                                        'code': 'users',
                                                        'label': 'Users'}}}}}

    @property
    def _entities(self):
        """
        Get Structure category

        :return: Structure category
        :rtype: dict
        """
        return {'entities': {'code': 'entities',
                             'label': 'Entities',
                             'subCat': {0: {'structure': {'widget': self.wgEntities,
                                                          'code': 'structure',
                                                          'label': 'Structure'}},
                                        1: {'attributes': {'widget': None,
                                                           'code': 'attributes',
                                                           'label': 'Attributes'}}}}}

    def on_save(self):
        """
        Command launched when 'Save' QPushButton is clicked

        Save settings to disk
        """
        super(ToolSettings, self).on_save()
        for item in self.getEditedItems():
            self.log.detail("---> %s | %s" % (item.parent().itemCode, item.itemCode))
            #-- Save UserGroups --#
            if item.parent().itemCode == 'userGroups':
                if item.itemCode == 'groups':
                    self.userGrps.pushGroupsToSettings()
                elif item.itemCode == 'users':
                    for editedItem in self.wgUsers.editedItems:
                        editedItem.itemObj.writeFile()
                    self.wgUsers.editedItems = []
            item.itemWidget.__edited__ = False
        #-- Write And Refresh --#
        self.fondation.writeSettings()
        self.rf_editedItemStyle()

    def _discardSettings(self):
        """
        Discard action confirmed
        """
        if self.wgUsers.editedItems:
            for editedItem in self.wgUsers.editedItems:
                self.userGrps.deleteUser(editedItem.itemObj.userName)
            self.wgUsers.editedItems = []
        super(ToolSettings, self)._discardSettings()
