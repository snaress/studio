import os, pprint
from PyQt4 import QtGui
from functools import partial
from lib.qt import procQt as pQt
from lib.system import procMath as pMath
from appli.fondationOld.gui.fondation.ui import tsUserGroupsUI, tsUserGroupsDialUI


class UserGroupsUi(QtGui.QWidget, tsUserGroupsUI.Ui_wg_tsUserGroups):
    """
    UserGroupsUi Class: Contains user groups settings, child of ToolSettings

    :param pWidget : Parent widget
    :type pWidget: ToolSettingsUi
    """
    __groupsEdited__ = False
    __usersEdited__ = False

    def __init__(self, pWidget):
        self.pWidget = pWidget
        self.log = self.pWidget.log
        self.fondation = self.pWidget.fondation
        self.userGrps = self.fondation.userGrps
        super(UserGroupsUi, self).__init__()
        self.iconUp = QtGui.QIcon(os.path.join(self.pWidget.mainUi.iconPath, 'arrowUpBlue.png'))
        self.iconDn = QtGui.QIcon(os.path.join(self.pWidget.mainUi.iconPath, 'arrowDnBlue.png'))
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
        self.setMaximumHeight(300)
        self._setupGroupsWidget()

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

    # noinspection PyUnresolvedReferences
    def _setupGroupsWidget(self):
        """
        Setup QtGui Groups Widget
        """
        #-- Tree Widget --#
        for n in range(self.tw_groups.columnCount()):
            self.tw_groups.resizeColumnToContents(n)
        #-- Add Icons --#
        self.pb_upGrp.setIcon(self.iconUp)
        self.pb_dnGrp.setIcon(self.iconDn)
        self.pb_addGrp.setIcon(self.iconAdd)
        self.pb_delGrp.setIcon(self.iconDel)
        self.pb_editGrp.setIcon(self.iconEdit)
        self.pb_styleGrp.setIcon(self.iconStyle)
        #-- Connect --#
        self.pb_upGrp.clicked.connect(partial(self.on_moveGroup, 'up'))
        self.pb_dnGrp.clicked.connect(partial(self.on_moveGroup, 'down'))
        self.pb_addGrp.clicked.connect(self.on_addGroup)
        self.pb_delGrp.clicked.connect(self.on_delGroup)
        self.pb_editGrp.clicked.connect(self.on_editGroup)
        self.pb_styleGrp.clicked.connect(self.on_styleGroup)
        #-- ToolTips --#
        self.rf_groupsToolTips()

    def getGroupsDatas(self, asString=False):
        """
        Get groups datas

        :param asString: Return string instead of dict
        :type asString: bool
        :return: Groups datas
        :rtype dict | str
        """
        grpDict = dict()
        for n, item in enumerate(pQt.getTopItems(self.tw_groups)):
            grpDict[n] = {'code': item.code, 'name': item.name, 'rgb': item.rgb}
        if asString:
            return pprint.pformat(grpDict)
        return grpDict

    def rf_groupsToolTips(self):
        """
        Refresh widgets toolTips
        """
        if self.pWidget.mainUi.showToolTips:
            self.pb_upGrp.setToolTip("Move up selected group")
            self.pb_dnGrp.setToolTip("Move down selected group")
            self.pb_addGrp.setToolTip("Create new user group")
            self.pb_delGrp.setToolTip("Delete selected group")
            self.pb_editGrp.setToolTip("Edit selected group")
            self.pb_styleGrp.setToolTip("Update style auto")
        else:
            wList = [self.pb_upGrp, self.pb_dnGrp, self.pb_addGrp, self.pb_delGrp, self.pb_editGrp, self.pb_styleGrp]
            for widget in wList:
                widget.setToolTip('')

    def buildGroupsTree(self):
        """
        Build groups tree widget
        """
        self.log.detail("#----- Refresh UserGroups/Groups widget -----#")
        self.tw_groups.clear()
        if 'userGroups' in self.pWidget.toolSettings.keys():
            userGrpDict = self.pWidget.toolSettings['userGroups']
            for n in sorted(userGrpDict['groups'].keys()):
                newItem = self.new_groupItem(userGrpDict['groups'][n]['code'],
                                             userGrpDict['groups'][n]['name'],
                                             userGrpDict['groups'][n]['rgb'])
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
            item.rgb = rgb
            item.setBackgroundColor((self.tw_groups.columnCount() - 1), QtGui.QColor(rgb[0], rgb[1], rgb[2]))

    def new_groupItem(self, grpCode, grpName, rgb):
        """
        Create group tree item widget

        :param grpCode: Group code
        :type grpCode: str
        :param grpName: Group name
        :type grpName: str
        :return: New group item
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = QtGui.QTreeWidgetItem()
        #-- Store Datas --#
        newItem.code = grpCode
        newItem.name = grpName
        newItem.rgb = rgb
        #-- Edit Item --#
        newItem.setText(0, newItem.code)
        newItem.setText(1, newItem.name)
        newItem.setBackgroundColor((self.tw_groups.columnCount() - 1),
                                   QtGui.QColor(newItem.rgb[0], newItem.rgb[1], newItem.rgb[2]))
        for n in range(self.tw_groups.columnCount()):
            newItem.setTextAlignment(n, 5)
        #-- Result --#
        return newItem

    def on_moveGroup(self, side):
        """
        Command launched when 'Del' QPushButton is clicked

        Add new group to tree
        """
        self.log.detail(">>> Launch 'Move Group': %s <<<" % side)
        selItems = self.tw_groups.selectedItems() or []
        if selItems:
            movedItem = None
            index = self.tw_groups.indexOfTopLevelItem(selItems[0])
            #-- Move Up --#
            if side == 'up':
                if index > 0:
                    movedItem = self.tw_groups.takeTopLevelItem(self.tw_groups.indexOfTopLevelItem(selItems[0]))
                    self.tw_groups.insertTopLevelItem((index - 1), movedItem)
            #-- Move Down --#
            else:
                if index < (self.tw_groups.topLevelItemCount() - 1):
                    movedItem = self.tw_groups.takeTopLevelItem(self.tw_groups.indexOfTopLevelItem(selItems[0]))
                    self.tw_groups.insertTopLevelItem((index + 1), movedItem)
            #-- Select Moved Item --#
            if movedItem is not None:
                self.tw_groups.clearSelection()
                for item in pQt.getTopItems(self.tw_groups):
                    if item == movedItem:
                        self.tw_groups.setItemSelected(movedItem, True)
                self.__groupsEdited__ = True

    def on_addGroup(self):
        """
        Command launched when 'Add' QPushButton is clicked

        Add new group to tree
        """
        self.log.detail(">>> Launch 'Add Group' <<<")
        newItem = self.new_groupItem('None', 'None', (0, 0, 0))
        self.tw_groups.addTopLevelItem(newItem)
        self.__groupsEdited__ = True

    def on_delGroup(self):
        """
        Command launched when 'Del' QPushButton is clicked

        Delete selected group from tree
        """
        self.log.detail(">>> Launch 'Add Group' <<<")
        selItems = self.tw_groups.selectedItems() or []
        if selItems:
            self.tw_groups.takeTopLevelItem(self.tw_groups.indexOfTopLevelItem(selItems[0]))
            self.__groupsEdited__ = True

    def on_editGroup(self):
        """
        Command launched when 'Edit' QPushButton is clicked

        Launch group dialog
        """
        self.log.detail(">>> Launch 'Edit Group' <<<")
        selItems = self.tw_groups.selectedItems() or []
        if selItems:
            self.dialGrp = GroupsDialog(selItems[0], parent=self)
            self.dialGrp.exec_()

    def on_styleGroup(self):
        """
        Command launched when 'Style' QPushButton is clicked

        Replace style by auto generate color
        """
        self.log.detail(">>> Launch 'Style Group' <<<")
        self.rf_groupsStyle()
        self.__groupsEdited__ = True

    #=================================== USERS ===================================#

    def buildUsersTree(self):
        """
        Build users tree widget
        """
        self.log.detail("#----- Refresh UserGroups/Users widget -----#")
        self.tw_users.clear()
        self.userGrps.collecteUsers(clearUsers=True)


class GroupsDialog(QtGui.QDialog, tsUserGroupsDialUI.Ui_dial_groups):

    def __init__(self, selItem, parent=None):
        self.selItem = selItem
        super(GroupsDialog, self).__init__(parent)
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup QtGui Groups dialog
        """
        self.setupUi(self)
        self.rf_dialog()
        self.sb_styleR.editingFinished.connect(self.on_rgb)
        self.sb_styleG.editingFinished.connect(self.on_rgb)
        self.sb_styleB.editingFinished.connect(self.on_rgb)
        self.pb_save.clicked.connect(self.on_save)
        self.pb_cancel.clicked.connect(self.close)

    def rf_dialog(self):
        """
        Refresh dialog values
        """
        self.le_userGrpCode.setText(self.selItem.code)
        self.le_userGrpName.setText(self.selItem.name)
        self.pb_userGrpStyle.setStyleSheet("background-color: rgb(%s, %s, %s)" % (self.selItem.rgb[0],
                                                                                  self.selItem.rgb[1],
                                                                                  self.selItem.rgb[2]))
        self.sb_styleR.setValue(self.selItem.rgb[0])
        self.sb_styleG.setValue(self.selItem.rgb[1])
        self.sb_styleB.setValue(self.selItem.rgb[2])

    def on_rgb(self):
        """
        Command launched when 'RGB' QSpinBoxes are edited

        Edit and refresh color
        """
        grpColor = (self.sb_styleR.value(), self.sb_styleG.value(), self.sb_styleB.value())
        self.pb_userGrpStyle.setStyleSheet("background-color: rgb(%s, %s, %s)" % (grpColor[0], grpColor[1], grpColor[2]))

    def on_save(self):
        """
        Command launched when 'Save' QPushButton is clicked

        Save group datas
        """
        #-- Get Datas --#
        excludes = ['', ' ', 'None']
        grpCode = self.le_userGrpCode.text()
        grpName = self.le_userGrpName.text()
        grpColor = (self.sb_styleR.value(), self.sb_styleG.value(), self.sb_styleB.value())
        #-- Check Datas --#
        if grpCode in excludes or grpName in excludes:
            message = "!!! 'code' or 'name' invalid: %s -- %s !!!" % (grpCode, grpName)
            pQt.errorDialog(message, self)
            raise AttributeError(message)
        #-- Edit Group --#
        self.selItem.code = grpCode
        self.selItem.name = grpName
        self.selItem.rgb = grpColor
        self.selItem.setText(0, grpCode)
        self.selItem.setText(1, grpName)
        self.selItem.setBackgroundColor((self.parent().tw_groups.columnCount() - 1),
                                        QtGui.QColor(grpColor[0], grpColor[1], grpColor[2]))
        #-- Quit --#
        self.close()
