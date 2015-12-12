from lib.system import procFile as pFile
from appli.fondation.gui.common import toolSettingsUi
from appli.fondation.gui.fondation import tsUserGroups


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
        self.log.info("########## Launching Tool Settings Ui ##########", newLinesBefor=1)
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
        #-- UserGroups --#
        self.wgGroups = tsUserGroups.Groups(self)
        self.wgGroups.setVisible(False)
        self.vl_settingsWidget.addWidget(self.wgGroups)
        self.wgUsers = tsUserGroups.Users(self)
        self.wgUsers.setVisible(False)
        self.vl_settingsWidget.addWidget(self.wgUsers)

    @property
    def category(self):
        """
        Get settings category

        :return: Category datas
        :rtype: dict
        """
        return {0: {'userGroups': {'code': 'userGroups',
                                   'label': 'User Groups',
                                   'subCat': {0: {'groups': {'widget': self.wgGroups,
                                                             'code': 'groups',
                                                             'label': 'Groups'}},
                                              1: {'users': {'widget': self.wgUsers,
                                                            'code': 'users',
                                                            'label': 'Users'}}}}},
                1: {'projectStructure': {'code': 'projectStructure',
                                         'label': 'Project Structure',
                                         'subCat': {1: {'entity': {'widget': None,
                                                                   'code': 'entity',
                                                                   'label': 'Entity'}}}}}}

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
            item.itemWidget.__edited__ = False
        #-- Write And Refresh --#
        self.fondation.writeSettings()
        self.rf_editedItemStyle()
