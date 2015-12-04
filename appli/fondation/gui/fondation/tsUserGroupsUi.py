import os
from PyQt4 import QtGui
from lib.qt import procQt as pQt
from lib.system import procMath as pMath
from appli.fondation.gui.fondation.ui import tsUserGroupsUI


class UserGroupsUi(QtGui.QWidget, tsUserGroupsUI.Ui_wg_tsUserGroups):

    __groupsEdited__ = False
    __usersEdited__ = False

    def __init__(self, pWidget):
        self.pWidget = pWidget
        self.log = self.pWidget.log
        self.fondation = self.pWidget.fondation
        self.userGrps = self.fondation.userGrps
        super(UserGroupsUi, self).__init__()
        self.iconAdd = QtGui.QIcon(os.path.join(self.pWidget.mainUi.iconPath, 'add.png'))
        self.iconDel = QtGui.QIcon(os.path.join(self.pWidget.mainUi.iconPath, 'del.png'))
        self.iconEdit = QtGui.QIcon(os.path.join(self.pWidget.mainUi.iconPath, 'edit.png'))
        self.iconStyle = QtGui.QIcon(os.path.join(self.pWidget.mainUi.iconPath, 'style.png'))
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup QtGui UserGroups Widget
        """
        self.log.detail("#----- Setup UserGroups Ui -----#")
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.setMaximumHeight(250)
        #-- Groups --#
        for n in range(self.tw_groups.columnCount()):
            self.tw_groups.resizeColumnToContents(n)
        self.pb_addGrp.setIcon(self.iconAdd)
        self.pb_addGrp.clicked.connect(self.on_addGroup)
        self.pb_delGrp.setIcon(self.iconDel)
        self.pb_editGrp.setIcon(self.iconEdit)
        self.pb_styleGrp.setIcon(self.iconStyle)
        self.pb_styleGrp.clicked.connect(self.on_styleGroup)

    def rf_widget(self, categoryCode):
        """
        Refresh widget

        :param categoryCode: Category code
        :type categoryCode: str
        """
        if categoryCode == 'groups':
            self.buildGroupsTree()
        elif categoryCode == 'users':
            self.buildUsersTree()

    #=================================== GROUPS ===================================#

    def buildGroupsTree(self):
        """
        Build groups tree widget
        """
        self.log.detail("#----- Refresh UserGroups/Groups widget -----#")
        self.tw_groups.clear()
        if 'userGroups' in self.pWidget.toolSettings.keys():
            userGrpDict = self.pWidget.toolSettings['userGroups']
            for n in sorted(userGrpDict['groups'].keys()):
                itemCode = userGrpDict['groups'][n].keys()[0]
                itemName = userGrpDict['groups'][n][itemCode]
                newItem = self.new_groupItem(n, itemCode, itemName)
                self.tw_groups.addTopLevelItem(newItem)

    def rf_groupsStyle(self):
        """
        Auto refresh group style
        """
        N = len(pQt.getTopItems(self.tw_groups))
        for n, item in enumerate(pQt.getTopItems(self.tw_groups)):
            if n == 0:
                rgb = (255, 0, 0)
            elif n == (len(pQt.getTopItems(self.tw_groups)) - 1):
                rgb = (0, 0, 255)
            elif n < (N / 2):
                rgb = (pMath.linear(0, (N / 2), 255, 0, n), pMath.linear(0, (N / 2), 0, 255, n), 0)
            else:
                rgb = (0, pMath.linear((N / 2), N, 255, 0, n), pMath.linear((N / 2), N, 0, 255, n))
            item.setBackgroundColor((self.tw_groups.columnCount() - 1), QtGui.QColor(rgb[0], rgb[1], rgb[2]))

    def new_groupItem(self, id, grpCode, grpName):
        """
        Create group tree item widget

        :param id: Group id
        :type id: int
        :param grpCode: Group code
        :type grpCode: str
        :param grpName: Group name
        :type grpName: str
        :return: New group item
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = QtGui.QTreeWidgetItem()
        #-- Store Datas --#
        newItem.id = id
        newItem.code = grpCode
        newItem.name = grpName
        #-- Edit Item --#
        newItem.setText(0, str(newItem.id))
        newItem.setText(1, newItem.code)
        newItem.setText(2, newItem.name)
        newItem.setBackgroundColor((self.tw_groups.columnCount() - 1), QtGui.QColor(0, 0, 0))
        for n in range(self.tw_groups.columnCount()):
            newItem.setTextAlignment(n, 5)
        #-- Result --#
        return newItem

    def on_addGroup(self):
        """
        Command launched when 'Add' QPushButton is clisked

        Add new group to tree
        """
        self.log.detail(">>> Launch 'Add Group' <<<")
        newItem = self.new_groupItem(len(pQt.getTopItems(self.tw_groups)), 'None', 'None')
        self.tw_groups.addTopLevelItem(newItem)
        self.__groupsEdited__ = True

    def on_styleGroup(self):
        """
        Command launched when 'Style' QPushButton is clisked

        Replace style by auto generate color
        """
        self.log.detail(">>> Launch 'Style Group' <<<")
        self.rf_groupsStyle()

    #=================================== USERS ===================================#

    def buildUsersTree(self):
        """
        Build users tree widget
        """
        self.log.detail("#----- Refresh UserGroups/Users widget -----#")
        self.tw_users.clear()
        self.userGrps.collecteUsers(clearUsers=True)


