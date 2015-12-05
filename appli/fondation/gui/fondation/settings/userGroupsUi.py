import os, pprint
from PyQt4 import QtGui
from functools import partial
from lib.qt import procQt as pQt
from lib.system import procMath as pMath
from appli.fondation.gui.fondation.settings._ui import userGroupsUI, ugGroupsDialUI


class UserGroupsUi(QtGui.QWidget, userGroupsUI.Ui_wg_tsUserGroups):
    """
    UserGroupsUi Class: Contains user groups settings, child of ToolSettings

    :param pWidget : Parent widget
    :type pWidget: SettingsUi
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
        self.iconApply = QtGui.QIcon(os.path.join(self.pWidget.mainUi.iconPath, 'apply.png'))
        self.iconCancel = QtGui.QIcon(os.path.join(self.pWidget.mainUi.iconPath, 'cancel.png'))
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

    #=================================== GROUPS ===================================#

    # noinspection PyUnresolvedReferences
    def _setupGroupsWidget(self):
        """
        Setup QtGui Groups Widget
        """
        #-- Tree Widget --#
        self.rf_groupsTreeColumns()
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
        self.pb_grpApply.setIcon(self.iconApply)
        self.pb_grpCancel.setIcon(self.iconCancel)
        #-- ToolTips --#
        self.rf_groupsToolTips()

    def getGroupsDatas(self, asString=False):
        """
        Get groups datas from tree widget

        :param asString: Return string instead of dict
        :type asString: bool
        :return: Groups datas
        :rtype: dict
        """
        datas = dict()
        for n, item in enumerate(pQt.getTopItems(self.tw_groups)):
            for k, v in item.__dict__.iteritems():
                if k.startswith('grp'):
                    datas[n][k] = v
        if asString:
            return pprint.pformat(datas)
        return datas

    def rf_groupsTreeColumns(self):
        """
        Refresh tree column size
        """
        for n in range(self.tw_groups.columnCount()):
            self.tw_groups.resizeColumnToContents(n)

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

    def buildGroupsTree(self):
        """
        Build groups tree widget
        """
        self.log.detail("#----- Refresh UserGroups/Groups widget -----#")
        self.tw_groups.clear()
        if self.userGrps._groups:
            for grpObj in self.userGrps._groups:
                newItem = self.new_groupItem(grpObj.grpCode, grpObj.grpName, grpObj.grpColor)
                self.tw_groups.addTopLevelItem(newItem)
        else:
            defaultItem1 = self.new_groupItem('ADMIN', 'Administrator', (255, 0, 0))
            self.tw_groups.addTopLevelItem(defaultItem1)
        self.rf_groupsTreeColumns()

    def new_groupItem(self, grpCode, grpName, grpColor):
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
        newItem.grpCode = grpCode
        newItem.grpName = grpName
        newItem.grpColor = grpColor
        #-- Edit Item --#
        newItem.setText(0, grpCode)
        newItem.setText(1, grpName)
        newItem.setBackgroundColor((self.tw_groups.columnCount() - 1),
                                   QtGui.QColor(grpColor[0], grpColor[1], grpColor[2]))
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
                if index > 1:
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

    def on_applyGroups(self):
        """
        Command launched when 'Apply' QPushButton is clicked

        Store datas to Fondation.UserGroups object
        """
        self.log.detail(">>> Launch 'Apply Groups' <<<")




class GroupsDialog(QtGui.QDialog, ugGroupsDialUI.Ui_dial_groups):

    def __init__(self, selItem, parent=None):
        self.selItem = selItem
        self.log = parent.log
        super(GroupsDialog, self).__init__(parent)
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup QtGui Groups dialog
        """
        self.log.detail("#----- Setup GroupsDialog Ui -----#")
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.rf_dialog()
        #-- Color --#
        self.pb_userGrpStyle.clicked.connect(self.on_color)
        self.pb_userGrpStyle.setShortcut("H")
        self.sb_styleR.editingFinished.connect(self.on_rgb)
        self.sb_styleG.editingFinished.connect(self.on_rgb)
        self.sb_styleB.editingFinished.connect(self.on_rgb)
        #-- Edit --#
        self.pb_save.setIcon(self.parent().iconApply)
        self.pb_save.clicked.connect(self.on_save)
        self.pb_cancel.setIcon(self.parent().iconCancel)
        self.pb_cancel.clicked.connect(self.close)

    def rf_dialog(self):
        """
        Refresh dialog values
        """
        self.le_userGrpCode.setText(self.selItem.grpCode)
        self.le_userGrpName.setText(self.selItem.grpName)
        self.pb_userGrpStyle.setStyleSheet("background-color: rgb(%s, %s, %s)" % (self.selItem.grpColor[0],
                                                                                  self.selItem.grpColor[1],
                                                                                  self.selItem.grpColor[2]))
        self.sb_styleR.setValue(self.selItem.grpColor[0])
        self.sb_styleG.setValue(self.selItem.grpColor[1])
        self.sb_styleB.setValue(self.selItem.grpColor[2])

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
        self.selItem.grpCode = grpCode
        self.selItem.grpName = grpName
        self.selItem.grpColor = grpColor
        self.selItem.setText(0, grpCode)
        self.selItem.setText(1, grpName)
        self.selItem.setBackgroundColor((self.parent().tw_groups.columnCount() - 1),
                                        QtGui.QColor(grpColor[0], grpColor[1], grpColor[2]))
        #-- Quit --#
        self.parent().rf_groupsTreeColumns()
        self.close()
