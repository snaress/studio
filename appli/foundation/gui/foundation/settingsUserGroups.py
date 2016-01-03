import os
from PyQt4 import QtGui
from lib.qt import procQt as pQt
from lib.system import procMath as pMath
from appli.foundation.gui.common import widgetsUi
from appli.foundation.gui.foundation._ui import ts_ugGroupsDialUI


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
            self.pb_apply.setToolTip("Apply datas to Fondation object")
            self.pb_cancel.setToolTip("Restore datas from Fondation object")

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
        itemObj = self.userGroups.newGroup(grpCode='None', grpName='None', grpGrade=9, grpColor=(0, 0, 0))
        newItem = self.new_treeItem(itemObj)
        self.tw_tree.addTopLevelItem(newItem)
        self.rf_treeColumns()
        self.tw_tree.clearSelection()
        self.tw_tree.setItemSelected(newItem, True)

    def on_editItem1(self):
        """
        Command launched when 'Edit' QPushButton is clicked

        Launch Group editing dialog
        """
        super(Groups, self).on_editItem1()
        selItems = self.tw_tree.selectedItems() or []
        if selItems:
            self.dial_groups = GroupsDialog(selItems[0], parent=self)
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

    :param selItem: Selected group item
    :type selItem: QtGui.QTreeWidgetItem
    :param parent: Parent Ui
    :type parent: Groups
    """

    def __init__(self, selItem, parent=None):
        self.selItem = selItem
        self.log = parent.log
        super(GroupsDialog, self).__init__(parent)
        self._setupUi()

    def _setupUi(self):
        """
        Setup QtGui Groups dialog
        """
        self.log.detail("#----- Setup GroupsDialog Ui -----#")
        self.setupUi(self)
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
        self.le_userGrpCode.setText(str(self.selItem.itemObj.grpCode))
        self.le_userGrpName.setText(str(self.selItem.itemObj.grpName))
        self.cb_grade.setCurrentIndex(self.selItem.itemObj.grpGrade)
        self.pb_userGrpStyle.setStyleSheet("background-color: rgb(%s, %s, %s)" % (self.selItem.itemObj.grpColor[0],
                                                                                  self.selItem.itemObj.grpColor[1],
                                                                                  self.selItem.itemObj.grpColor[2]))
        self.sb_styleR.setValue(self.selItem.itemObj.grpColor[0])
        self.sb_styleG.setValue(self.selItem.itemObj.grpColor[1])
        self.sb_styleB.setValue(self.selItem.itemObj.grpColor[2])

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
        #-- Check New Code Name --#
        if not grpCode == self.selItem.itemObj.grpCode:
            grpDatas = self.parent().getDatas()
            for n in grpDatas.keys():
                if grpCode == grpDatas[n]['grpCode']:
                    message = "!!! %s already exists !!!" % grpCode
                    pQt.errorDialog(message, self)
                    raise AttributeError(message)
        #-- Edit Group --#
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
        super(Users, self).__init__(pWidget)
        self.usersCollected = False
        self.editedItems = []

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
        self.tw_tree.header().setStretchLastSection(False)
        self.rf_headers('User Name', 'Group', 'First Name', 'Last Name')
        self.rf_treeColumns()

    def _setupIcons(self):
        """
        Setup Users icons
        """
        super(Users, self)._setupIcons()
        self.pb_edit1.setText("Edit")

    def rf_toolTips(self):
        """
        Refresh widgets toolTips
        """
        super(Users, self).rf_toolTips()
        if self.mainUi.showToolTips:
            self.pb_add.setToolTip("Create new user")
            self.pb_del.setToolTip("Delete selected User")
            self.pb_edit1.setToolTip("Edit selected User")
            self.pb_apply.setToolTip("Apply datas to Fondation object")
            self.pb_cancel.setToolTip("Restore datas from Fondation object")

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
        userItems = []
