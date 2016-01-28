from appli.foundation.gui.common import dialogsUi
from appli.foundation.gui.foundation import settingsUserGrps


class ToolSettings(dialogsUi.ToolSettings):
    """
    ToolSettings Dialog: Contains Foundation tool settings, child of FoundationUi

    :param parent: Parent Ui
    :type parent: FoundationUi
    """

    def __init__(self, parent=None):
        self.log = parent.log
        self.log.title = 'ToolSettingsUi'
        self.foundation = self.fdn = parent.foundation
        self.userGrps = self.fdn.userGrps
        super(ToolSettings, self).__init__(parent)

    def _initSettings(self):
        """
        Init Foundation settings
        """
        super(ToolSettings, self)._initSettings()

    def _initWidgets(self):
        """
        Init tool widgets
        """
        super(ToolSettings, self)._initWidgets()
        #-- UserGroups --#
        self.wg_groups = settingsUserGrps.Groups(self)
        #-- Refresh --#
        for widget in [self.wg_groups]:
            widget.setVisible(False)
            self.vl_settingsWidget.addWidget(widget)

    @property
    def category(self):
        """
        Get settings category

        :return: Category datas
        :rtype: dict
        """
        return {0: self.userGrpsCategory}

    @property
    def userGrpsCategory(self):
        """
        Get UserGroups category

        :return: UserGroups category
        :rtype: dict
        """
        return {'userGroups': {'code': 'userGroups',
                               'label': 'User Groups',
                               'subCat': {0: {'groups': {'widget': self.wg_groups,
                                                         'code': 'groups',
                                                         'label': 'Groups'}},
                                          1: {'users': {'widget': None,
                                                        'code': 'users',
                                                        'label': 'Users'}}}}}
