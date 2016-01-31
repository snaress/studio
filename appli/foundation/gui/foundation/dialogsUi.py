import os
from PyQt4 import QtGui
from lib.system import procFile as pFile
from appli.foundation.gui.common import dialogsUi
from appli.foundation.gui.foundation import settingsUserGrps
from appli.foundation.gui.foundation._ui import newProjectUI


class NewProject(QtGui.QDialog, newProjectUI.Ui_dial_newProject):
    """
    NewProject Dialog: Project creation, child of FoundationUi

    :param mainUi: Parent Ui
    :type mainUi: Foundation
    """

    def __init__(self, mainUi):
        super(NewProject, self).__init__(mainUi)
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.foundation = self.fdn = self.mainUi.foundation
        self.iconSave = QtGui.QIcon(pFile.conformPath(os.path.join(self.mainUi.iconPath, 'apply.png')))
        self.iconCancel = QtGui.QIcon(pFile.conformPath(os.path.join(self.mainUi.iconPath, 'cancel.png')))
        self._setupDial()

    def _setupDial(self):
        """
        Setup NewProject dialog
        """
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        #-- Icons --#
        self.pb_save.setIcon(self.iconSave)
        self.pb_cancel.setIcon(self.iconCancel)
        #-- Connect --#
        self.pb_save.clicked.connect(self.on_save)
        self.pb_cancel.clicked.connect(self.close)

    def on_save(self):
        """
        Command launched when 'Save' QPushButton is clicked

        Create New Project
        """
        self.log.detail(">>> Save New Project Dialog")


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
        self.users = self.fdn.users
        super(ToolSettings, self).__init__(parent)

    def _initSettings(self):
        """
        Init Foundation settings
        """
        super(ToolSettings, self)._initSettings()
        self.users.collecteUsers(userName=self.fdn.__user__)

    def _initWidgets(self):
        """
        Init tool widgets
        """
        super(ToolSettings, self)._initWidgets()
        #-- UserGroups --#
        self.wg_groups = settingsUserGrps.Groups(self)
        self.wg_users = settingsUserGrps.Users(self)
        #-- Refresh --#
        for widget in [self.wg_groups, self.wg_users]:
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
                                          1: {'users': {'widget': self.wg_users,
                                                        'code': 'users',
                                                        'label': 'Users'}}}}}
