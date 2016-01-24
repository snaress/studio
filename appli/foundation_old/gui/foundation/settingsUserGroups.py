import os
from functools import partial
from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from lib.system import procMath as pMath
from appli.foundation_old.gui.common import widgetsUi
from appli.foundation_old.gui.foundation._ui import ts_ugGroupsDialUI, ts_ugUsersDialUI


class Groups(widgetsUi.BasicTree):
    """
    Groups Class: Contains UserGroups settings, child of ToolSettings

    :param pWidget: Parent widget
    :type pWidget: ProjectSettings
    """

    __edited__ = False

    def __init__(self, pWidget):
        self.pWidget = pWidget
        self.log = self.pWidget.log
        self.mainUi = self.pWidget.parent()
        self.foundation = self.pWidget.foundation
        self.userGroups = self.foundation.userGroups
        super(Groups, self).__init__(pWidget)

    def _setupWidget(self):
        """
        Setup Groups widget
        """
        super(Groups, self)._setupWidget()
        self.l_title.setText('Groups')
        self.pb_template.setVisible(False)
        self.cbb_filter.setVisible(False)
        self.qf_treeEdit_R.setVisible(False)
        self.tw_tree.header().setStretchLastSection(False)
        self.rf_headers('Code', 'Name', 'Grade', 'Style')
        self.rf_treeColumns()

    def _setupIcons(self):
        """
        Setup Groups icons
        """
        super(Groups, self)._setupIcons()
        #-- Init Icons --#
        self.iconStyle = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'style.png'))
        #-- Add Icons --#
        self.pb_edit2.setIcon(self.iconStyle)
        #-- Edit Label --#
        self.pb_edit1.setText("Edit")
        self.pb_edit2.setText("Style")
        #-- Edit Grade --#
        if not self.userGroups._user.grade == 0:
            self.pb_del.setEnabled(False)

    def rf_toolTips(self):
        """
        Refresh widgets toolTips
        """
        super(Groups, self).rf_toolTips()
        if self.mainUi.showToolTips:
            self.pb_itemUp.setToolTip("Move up selected group")
            self.pb_itemDn.setToolTip("Move down selected group")
            self.pb_add.setToolTip("Create new user group")
            self.pb_del.setToolTip("Delete selected group")
            self.pb_edit1.setToolTip("Edit selected group")
            self.pb_edit2.setToolTip("Update style auto")
            self.pb_apply.setToolTip("Apply datas to Foundation object")
            self.pb_cancel.setToolTip("Restore datas from Foundation object")
            #-- Edit Grade --#
            if not self.userGroups._user.grade == 0:
                self.pb_del.setToolTip("Delete selected group (Disabled for your grade)")

    def buildTree(self):
        """
        Build Groups tree widget
        """
        super(Groups, self).buildTree()
        self.log.detail("---> Groups tree")
        if self.userGroups._groups:
            grpItems = []
            for grpObj in self.userGroups._groups:
                newItem = self.new_treeItem(grpObj)
                grpItems.append(newItem)
            self.tw_tree.addTopLevelItems(grpItems)
        self.rf_treeColumns()

    def ud_treeItem(self, item, **kwargs):
        """
        Update item datas and settings

        :param item: Group tree item
        :type item: QtGui.QTreeWidgetItem
        :param kwargs: Group item datas (key must starts with 'grp')
        :type kwargs: dict
        """
        super(Groups, self).ud_treeItem(item, **kwargs)
        #-- Edit Item --#
        item.setText(0, item.itemObj.grpCode)
        item.setText(1, item.itemObj.grpName)
        item.setText(2, str(item.itemObj.grpGrade))
        item.setBackgroundColor((self.tw_tree.columnCount() - 1), QtGui.QColor(item.itemObj.grpColor[0],
                                                                               item.itemObj.grpColor[1],
                                                                               item.itemObj.grpColor[2]))

    def on_addItem(self):
        """
        Command launched when 'Add' QPushButton is clicked

        Add new group to tree
        """
        super(Groups, self).on_addItem()
        self.dial_groups = GroupsDialog(dialogMode='add', parent=self)
        self.dial_groups.exec_()

    def on_editItem1(self):
        """
        Command launched when 'Edit' QPushButton is clicked

        Launch Group editing dialog
        """
        super(Groups, self).on_editItem1()
        selItems = self.tw_tree.selectedItems() or []
        if selItems:
            self.dial_groups = GroupsDialog(dialogMode='edit', selItem=selItems[0], parent=self)
            self.dial_groups.exec_()
        else:
            message = "!!! Select at least one group item !!!"
            pQt.errorDialog(message, self)

    def on_editItem2(self):
        """
        Command launched when 'Style' QPushButton is clicked

        Auto assign color to all items
        """
        super(Groups, self).on_editItem2()
        N = len(pQt.getTopItems(self.tw_tree))
        for n, item in enumerate(pQt.getTopItems(self.tw_tree)):
            if n == 0:
                rgb = (255, 0, 0)
            elif n == (len(pQt.getTopItems(self.tw_tree)) - 1):
                rgb = (0, 0, 255)
            elif n < (N / 2):
                rgb = (pMath.linear(0, (N / 2), 255, 0, n), pMath.linear(0, (N / 2), 0, 255, n), 0)
            else:
                rgb = (0, pMath.linear((N / 2), N, 255, 0, n), pMath.linear((N / 2), N, 0, 255, n))
            self.ud_treeItem(item, grpColor=rgb)

    def on_apply(self):
        """
        Command launched when 'Apply' QPushButton is clicked

        Store datas to itemObject
        """
        super(Groups, self).on_apply()
        ind = 0
        #-- Parse Group Tree --#
        grpDict = dict()
        treeDict = self.getDatas()
        for n in sorted(treeDict.keys()):
            if not treeDict[n]['grpCode'] in ['', ' ', 'None', None]:
                if not ind in grpDict.keys():
                    grpDict[ind] = dict()
                for k, v in treeDict[n].iteritems():
                    grpDict[ind][k] = v
                ind += 1
            else:
                self.log.warning("!!! ERROR: Group 'code' value not valide, skipp %s !!!" % treeDict[n]['grpCode'])
        #-- Store and refresh --#
        self.userGroups.buildGroupsFromDict(grpDict)
        self.pWidget.rf_editedItemStyle()
        self.buildTree()


class GroupsDialog(QtGui.QDialog, ts_ugGroupsDialUI.Ui_dial_groups):
    """
    Groups Dialog: UserGroups edition, child of Groups

    :param dialogMode: 'add' or 'edit'
    :type dialogMode: str
    :param selItem: Selected group item
    :type selItem: QtGui.QTreeWidgetItem
    :param parent: Parent Ui
    :type parent: Groups
    """

    def __init__(self, dialogMode='add', selItem=None, parent=None):
        self.dialogMode = dialogMode
        self.selItem = selItem
        self.log = parent.log
        self.log.title = 'TS_ugGroups'
        super(GroupsDialog, self).__init__(parent)
        self._setupUi()

    def _setupUi(self):
        """
        Setup QtGui Groups dialog
        """
        self.log.detail("#----- Setup GroupsDialog Ui -----#")
        self.setupUi(self)
        #-- Mode --#
        if self.dialogMode == 'add':
            self.le_userGrpCode.setEnabled(True)
        else:
            self.le_userGrpCode.setEnabled(False)
        #-- Grade --#
        for n in range(10):
            self.cb_grade.addItem(str(n))
        #-- Color --#
        self.pb_userGrpStyle.clicked.connect(self.on_color)
        self.sb_styleR.editingFinished.connect(self.on_rgb)
        self.sb_styleG.editingFinished.connect(self.on_rgb)
        self.sb_styleB.editingFinished.connect(self.on_rgb)
        #-- Edit --#
        self.pb_save.setIcon(self.parent().iconApply)
        self.pb_save.clicked.connect(self.on_save)
        self.pb_cancel.setIcon(self.parent().iconCancel)
        self.pb_cancel.clicked.connect(self.close)
        #-- Refresh --#
        self.rf_dialog()
        self.rf_toolTips()

    def rf_dialog(self):
        """
        Refresh dialog values
        """
        if self.selItem is not None:
            self.le_userGrpCode.setText(str(self.selItem.itemObj.grpCode))
            self.le_userGrpName.setText(str(self.selItem.itemObj.grpName))
            self.cb_grade.setCurrentIndex(self.selItem.itemObj.grpGrade)
            self.pb_userGrpStyle.setStyleSheet("background-color: rgb(%s, %s, %s)" % (self.selItem.itemObj.grpColor[0],
                                                                                      self.selItem.itemObj.grpColor[1],
                                                                                      self.selItem.itemObj.grpColor[2]))
            self.sb_styleR.setValue(self.selItem.itemObj.grpColor[0])
            self.sb_styleG.setValue(self.selItem.itemObj.grpColor[1])
            self.sb_styleB.setValue(self.selItem.itemObj.grpColor[2])
        else:
            self.pb_userGrpStyle.setStyleSheet("background-color: rgb(0, 0, 0)")
            self.sb_styleR.setValue(0)
            self.sb_styleG.setValue(0)
            self.sb_styleB.setValue(0)

    def rf_toolTips(self):
        """
        Refresh dialog toolTips
        """
        if self.parent().mainUi.showToolTips:
            self.le_userGrpCode.setToolTip("Group code ('ADMIN', 'DEV')")
            self.le_userGrpName.setToolTip("Group name")
            self.cb_grade.setToolTip("Group grade index (min=0, max=9")
            self.sb_styleR.setToolTip("Red color value (0, 255)")
            self.sb_styleG.setToolTip("Green color value (0, 255)")
            self.sb_styleB.setToolTip("Blue color value (0, 255)")
            self.pb_userGrpStyle.setToolTip("Click to pick a color")
        else:
            wList = [self.sb_styleR, self.sb_styleG, self.sb_styleB, self.pb_userGrpStyle]
            for widget in wList:
                widget.setToolTip('')

    def on_color(self):
        """
        Command launched when 'Color' QPushButton is clicked

        Launch color dialog
        """
        # noinspection PyArgumentList
        color = QtGui.QColorDialog.getColor()
        if color.isValid():
            rgba = color.getRgb()
            self.sb_styleR.setValue(rgba[0])
            self.sb_styleG.setValue(rgba[1])
            self.sb_styleB.setValue(rgba[2])
            self.on_rgb()

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
        excludes = ['', ' ', 'None', None]
        grpCode = str(self.le_userGrpCode.text())
        grpName = str(self.le_userGrpName.text())
        grpGrade = int(self.cb_grade.currentText())
        grpColor = (self.sb_styleR.value(), self.sb_styleG.value(), self.sb_styleB.value())
        #-- Check Datas --#
        if grpCode in excludes or grpName in excludes:
            message = "!!! 'code' or 'name' invalid: %s -- %s !!!" % (grpCode, grpName)
            pQt.errorDialog(message, self)
            raise AttributeError(message)
        #-- Check New Code --#
        if self.dialogMode == 'add':
            grpDatas = self.parent().getDatas()
            for n in grpDatas.keys():
                if grpCode == grpDatas[n]['grpCode']:
                    message = "!!! %s already exists !!!" % grpCode
                    pQt.errorDialog(message, self)
                    raise AttributeError(message)
        #-- Edit Group --#
        if self.dialogMode == 'add':
            itemObj = self.parent().userGroups.newGroup(grpCode=grpCode, grpName=grpName, grpGrade=grpGrade,
                                                        grpColor=grpColor)
            self.selItem = self.parent().new_treeItem(itemObj)
            self.parent().tw_tree.addTopLevelItem(self.selItem)
            self.parent().tw_tree.clearSelection()
            self.parent().tw_tree.setItemSelected(self.selItem, True)
        self.parent().ud_treeItem(self.selItem, grpCode=grpCode, grpName=grpName, grpGrade=grpGrade, grpColor=grpColor)
        #-- Quit --#
        self.parent().rf_treeColumns()
        self.close()


class Users(widgetsUi.BasicTree):
    """
    ToolSettings Users Class: Contains User settings, child of ToolSettings

    :param pWidget: Parent widget
    :type mainUi: ToolSettings
    """

    __edited__ = False

    def __init__(self, pWidget):
        self.pWidget = pWidget
        self.log = self.pWidget.log
        self.mainUi = self.pWidget.parent()
        self.foundation = self.pWidget.foundation
        self.userGroups = self.foundation.userGroups
        self.project = self.foundation.project
        super(Users, self).__init__(pWidget)
        self.usersCollected = False
        self.editedItems = dict(added=[], edited=[], deleted=[])

    def _setupWidget(self):
        """
        Setup Users widget
        """
        super(Users, self)._setupWidget()
        self.l_title.setText('Users')
        self.qf_moveItem.setVisible(False)
        self.pb_template.setVisible(False)
        self.pb_edit2.setVisible(False)
        self.qf_treeEdit_R.setVisible(False)
        self.tw_tree.setSortingEnabled(True)
        self.tw_tree.header().setStretchLastSection(False)
        self.rf_headers('User Name', 'Group', 'First Name', 'Last Name', 'Watch')
        self.rf_treeColumns()

    def _setupIcons(self):
        """
        Setup Users icons
        """
        super(Users, self)._setupIcons()
        #-- Init Icons --#
        self.iconWatch = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'pinGreen.png'))
        self.iconNotWatch = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'pinRed.png'))
        #-- Edit Label --#
        self.buildFilters()
        self.pb_edit1.setText("Edit")
        #-- Edit Grade --#
        if not self.userGroups._user.grade == 0:
            self.pb_del.setEnabled(False)

    def rf_toolTips(self):
        """
        Refresh widgets toolTips
        """
        super(Users, self).rf_toolTips()
        if self.mainUi.showToolTips:
            self.cbb_filter.setToolTip("User index filter")
            self.pb_add.setToolTip("Create new user")
            self.pb_del.setToolTip("Delete selected user")
            self.pb_edit1.setToolTip("Edit selected user")
            self.pb_apply.setToolTip("Apply datas to Foundation object")
            self.pb_cancel.setToolTip("Restore datas from Foundation object")
            #-- Edit Grade --#
            if not self.userGroups._user.grade == 0:
                self.pb_del.setToolTip("Delete selected user (Disabled for your grade)")

    def rf_watchState(self, itemWidget):
        """
        Refresh watch button icon

        :param itemWidget: User item button
        :type itemWidget: QtGui.QPushButton
        """
        if itemWidget.isChecked():
            itemWidget.setIcon(self.iconWatch)
        else:
            itemWidget.setIcon(self.iconNotWatch)

    def buildFilters(self):
        """
        Build comboBox filters
        """
        super(Users, self).buildFilters()
        self.cbb_filter.addItems(['All', 'Added', 'Edited', 'Deleted', 'Changed'])
        self.cbb_filter.addItems(self.userGroups.getIndexes(capital=True))
        self.cbb_filter.insertSeparator(5)
        self.cbb_filter.setEditable(True)
        self.cbb_filter.lineEdit().setReadOnly(True)
        self.cbb_filter.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        for n in range(self.cbb_filter.count()):
            self.cbb_filter.setItemData(n, QtCore.Qt.AlignCenter, QtCore.Qt.TextAlignmentRole)

    # noinspection PyUnresolvedReferences
    def buildTree(self):
        """
        Build Users tree widget
        """
        super(Users, self).buildTree()
        self.log.detail("---> Users tree")
        #-- Collecte Users --#
        if not self.usersCollected:
            self.userGroups.collecteUsers(clearUsers=True)
            self.usersCollected = True
        #-- Populate Tree --#
        if self.userGroups._users:
            for userObj in self.userGroups._users:
                newItem = self.new_treeItem(userObj)
                #-- Add Button --#
                if userObj.userName in self.project.projectUsers:
                    newItem.itemWidget = self.new_itemButton(True)
                else:
                    newItem.itemWidget = self.new_itemButton(False)
                #-- Add Item --#
                newItem.itemWidget.clicked.connect(partial(self.on_watchState, newItem))
                self.tw_tree.addTopLevelItem(newItem)
                self.tw_tree.setItemWidget(newItem, 4, newItem.itemWidget)
        #-- Refresh --#
        self.rf_treeColumns()
        self.tw_tree.sortItems(0, QtCore.Qt.AscendingOrder)
        self.buildFilters()

    def ud_treeItem(self, item, **kwargs):
        """
        Update item datas and settings

        :param item: Group tree item
        :type item: QtGui.QTreeWidgetItem
        :param kwargs: Group item datas (key must starts with 'user')
        :type kwargs: dict
        """
        super(Users, self).ud_treeItem(item, **kwargs)
        #-- Edit Item --#
        item.setText(0, str(item.itemObj.userName))
        item.setText(1, str(item.itemObj.userGroup))
        item.setText(2, str(item.itemObj.userFirstName))
        item.setText(3, str(item.itemObj.userLastName))

    def new_itemButton(self, state):
        """
        Create tree item button

        :param state: Check state
        :type state: bool
        :return: Tree item button
        :rtype: QtGui.QPushButton
        """
        newButton = QtGui.QPushButton()
        newButton.setText('')
        newButton.setCheckable(True)
        newButton.setChecked(state)
        newButton.setIconSize(QtCore.QSize(18, 18))
        self.rf_watchState(newButton)
        return newButton

    def on_filter(self):
        """
        Command launched when 'Filter' QComboBox item is clicked

        Update use tree display
        """
        super(Users, self).on_filter()
        filter = str(self.cbb_filter.currentText())
        for item in pQt.getAllItems(self.tw_tree):
            #-- Prefix --#
            if len(filter) == 1:
                if item.itemObj.userPrefixFolder == filter.lower():
                    item.setHidden(False)
                else:
                    item.setHidden(True)
            #-- All --#
            elif filter == 'All':
                item.setHidden(False)
            #-- Added, Edited, Deleted --#
            elif filter in ['Added', 'Edited', 'Deleted']:
                if item in self.editedItems[filter.lower()]:
                    item.setHidden(False)
                else:
                    item.setHidden(True)
            #-- Changed --#
            elif filter == 'Changed':
                if (item in self.editedItems['added'] or item in self.editedItems['edited']
                    or item in self.editedItems['deleted']):
                    item.setHidden(False)
                else:
                    item.setHidden(True)

    def on_addItem(self):
        """
        Command launched when 'Add' QPushButton is clicked

        Create new user
        """
        super(Users, self).on_addItem()
        self.dial_user = UsersDialog(dialogMode='add', parent=self)
        self.dial_user.exec_()

    def on_delItem(self):
        """
        Command launched when 'Del' QPushButton is clicked

        Delete selected user from tree
        """
        selItems = self.tw_tree.selectedItems() or []
        if selItems:
            if not selItems[0] in self.editedItems['deleted']:
                self.editedItems['deleted'].append(selItems[0])
                if selItems[0] in self.editedItems['added']:
                    self.editedItems['added'].remove(selItems[0])
                if selItems[0] in self.editedItems['edited']:
                    self.editedItems['edited'].remove(selItems[0])
        self.rf_itemStyle()

    def on_editItem1(self):
        """
        Command launched when 'Edit' QPushButton is clicked

        Launch User editing dialog
        """
        super(Users, self).on_editItem1()
        selItems = self.tw_tree.selectedItems() or []
        if selItems:
            self.dialUser = UsersDialog(dialogMode='edit', selItem=selItems[0], parent=self)
            self.dialUser.exec_()
        else:
            message = "!!! Select at least one user item !!!"
            pQt.errorDialog(message, self)

    # noinspection PyUnresolvedReferences
    def on_watchState(self, item):
        """
        Command launched when 'Watch' QPushButton is clicked

        Tag user as project watcher
        :param item: User tree item
        :type item: QtGui.QTreeWidgetItem
        """
        #-- Store Edition --#
        if (not item in self.editedItems['edited'] and not item in self.editedItems['added']
            and not item in self.editedItems['deleted']):
            self.editedItems['edited'].append(item)
        #-- Refresh Item Style --#
        self.rf_watchState(item.itemWidget)

    def on_apply(self):
        """
        Command launched when 'Apply' QPushButton is clicked

        Store datas to itemObject
        """
        super(Users, self).on_apply()
        #-- Add New User --#
        for item in self.editedItems['added']:
            if not item.itemObj.userName in self.userGroups.users:
                self.userGroups._users.append(item.itemObj)
        #-- Edited User --#
        for item in self.editedItems['edited']:
            watchState = item.itemWidget.isChecked()
            if watchState:
                self.project.addProjectUser(item.itemObj.userName)
            else:
                self.project.removeProjectUser(item.itemObj.userName)
        #-- Del User --#
        for item in self.editedItems['deleted']:
            if item.itemObj.userName in self.userGroups.users:
                self.userGroups.deleteUser(userObj=item.itemObj)
        #-- Refresh --#
        self.pWidget.rf_editedItemStyle()
        self.buildTree()

    def on_cancel(self):
        """
        Command launched when 'Cancel' QPushButton is clicked

        Restore datas from itemObject
        """
        #-- Remove Added UserObj --#
        for item in self.editedItems['added']:
            self.userGroups.deleteUser(userObj=item.itemObj)
        self.editedItems['added'] = []
        #-- Restore Edited UserObj --#
        for item in self.editedItems['edited']:
            item.itemObj.setDatasFromUserFile()
        self.editedItems['edited'] = []
        #-- Refresh Tree --#
        super(Users, self).on_cancel()


class UsersDialog(QtGui.QDialog, ts_ugUsersDialUI.Ui_dial_users):
    """
    Users Dialog: User edition, child of Users

    :param dialogMode: 'add' or 'edit'
    :type dialogMode: str
    :param selItem: Selected user item
    :type selItem: QtGui.QTreeWidgetItem
    :param parent: Parent Ui
    :type parent: Users
    """

    def __init__(self, dialogMode='add', selItem=None, parent=None):
        self.dialogMode = dialogMode
        self.selItem = selItem
        self.log = parent.log
        self.log.title = 'TS_ugUsers'
        super(UsersDialog, self).__init__(parent)
        self._setupUi()

    def _setupUi(self):
        """
        Setup QtGui Groups dialog
        """
        self.log.detail("#----- Setup UsersDialog Ui -----#")
        self.setupUi(self)
        #-- Mode --#
        if self.dialogMode == 'add':
            self.le_userName.setEnabled(True)
        elif self.dialogMode == 'edit':
            self.le_userName.setEnabled(False)
        #-- Edit --#
        self.pb_save.setIcon(self.parent().iconApply)
        self.pb_save.clicked.connect(self.on_save)
        self.pb_cancel.setIcon(self.parent().iconCancel)
        self.pb_cancel.clicked.connect(self.close)
        #-- Refresh --#
        self.rf_dialog()
        self.rf_toolTips()

    def rf_dialog(self):
        """
        Refresh dialog values
        """
        self.cb_userGroup.addItems(self.parent().userGroups.groupsCode)
        if self.selItem is not None:
            self.le_userName.setText(str(self.selItem.itemObj.userName))
            self.cb_userGroup.setCurrentIndex(self.cb_userGroup.findText(self.selItem.itemObj.userGroup))
            self.le_userFirstName.setText(str(self.selItem.itemObj.userFirstName))
            self.le_userLastName.setText(str(self.selItem.itemObj.userLastName))
        else:
            self.cb_userGroup.setCurrentIndex(self.cb_userGroup.findText('VST'))

    def rf_toolTips(self):
        """
        Refresh dialog toolTips
        """
        if self.parent().mainUi.showToolTips:
            self.le_userName.setToolTip("User login")
            self.cb_userGroup.setToolTip("User group")
            self.le_userFirstName.setToolTip("User first name")
            self.le_userLastName.setToolTip("User last name")
        else:
            wList = [self.le_userName, self.cb_userGroup, self.le_userFirstName, self.le_userLastName]
            for widget in wList:
                widget.setToolTip('')

    def on_save(self):
        """
        Command launched when 'Save' QPushButton is clicked

        Save user datas
        """
        #-- Get Datas --#
        excludes = ['', ' ', 'newUser', 'None', None]
        userName = str(self.le_userName.text())
        userGroup = str(self.cb_userGroup.currentText())
        userFirstName = str(self.le_userFirstName.text())
        userLastName = str(self.le_userLastName.text())
        #-- Check Datas --#
        if userName in excludes:
            message = "!!! 'userName' invalid: %s !!!" % userName
            pQt.errorDialog(message, self)
            raise AttributeError(message)
        #-- Check New Code --#
        if self.dialogMode == 'add':
            userDatas = self.parent().getDatas()
            for n in sorted(userDatas.keys()):
                if userName == userDatas[n]['userName']:
                    message = "!!! %s already exists !!!" % userName
                    pQt.errorDialog(message, self)
                    raise AttributeError(message)
        #-- Edit User --#
        if self.dialogMode == 'add':
            self.log.detail("Adding new user: %s" % userName)
            userObj = self.parent().userGroups.newUser(userName=userName)
            self.selItem = self.parent().new_treeItem(userObj)
            self.parent().tw_tree.addTopLevelItem(self.selItem)
            #-- Store Edition --#
            if not self.selItem in self.parent().editedItems['added']:
                self.parent().editedItems['added'].append(self.selItem)
            #-- Update Filters --#
            if not userName[0].upper() in pQt.getComboBoxItems(self.parent().cbb_filter):
                self.parent().cbb_filter.addItem(userName[0].upper())
                self.parent().cbb_filter.setCurrentIndex(self.parent().cbb_filter.findText(userName[0].upper()))
        #-- Store Edition --#
        elif self.dialogMode == 'edit':
            self.log.detail("Editing user: %s" % userName)
            if not self.selItem in self.parent().editedItems['edited']:
                if not self.selItem in self.parent().editedItems['added']:
                    self.parent().editedItems['edited'].append(self.selItem)
        #-- Update Item --#
        self.parent().ud_treeItem(self.selItem, userName=userName, userGroup=userGroup,
                                  userFirstName=userFirstName, userLastName=userLastName)
        #-- Quit --#
        self.parent().rf_treeColumns()
        self.parent().rf_itemStyle()
        self.close()
