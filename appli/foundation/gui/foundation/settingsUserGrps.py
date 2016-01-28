import os
from PyQt4 import QtGui
from appli.foundation.gui.common import widgetsUi


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
        self.foundation = self.fdn = self.pWidget.foundation
        self.userGrps = self.fdn.userGrps
        self.users = self.fdn.users
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
        if not self.users._user.grade == 0:
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
            if not self.users._user.grade == 0:
                self.pb_del.setToolTip("Delete selected group (Disabled for your grade)")
