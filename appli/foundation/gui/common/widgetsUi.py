import os
from PyQt4 import QtGui
from lib.system import procFile as pFile
from appli.foundation.gui.common._ui import wg_basicTreeUI


class BasicTree(QtGui.QWidget, wg_basicTreeUI.Ui_wg_basicTree):
    """
    BasicTree common Class: Category tree widget

    :param parent: Parent Ui
    :type parent: ProjectSettings || ToolSettings
    """

    iconPath = "%s/_lib/icon/png" % '/'.join(pFile.conformPath(os.path.dirname(__file__)).split('/')[:-1])

    def __init__(self, parent=None):
        super(BasicTree, self).__init__(parent)
        #-- Icons --#
        self.iconUp = QtGui.QIcon(os.path.join(self.iconPath, 'arrowUpBlue.png'))
        self.iconDn = QtGui.QIcon(os.path.join(self.iconPath, 'arrowDnBlue.png'))
        self.iconTpl = QtGui.QIcon(os.path.join(self.iconPath, 'template.png'))
        self.iconAdd = QtGui.QIcon(os.path.join(self.iconPath, 'add.png'))
        self.iconDel = QtGui.QIcon(os.path.join(self.iconPath, 'del.png'))
        self.iconEdit = QtGui.QIcon(os.path.join(self.iconPath, 'edit.png'))
        self.iconClear = QtGui.QIcon(os.path.join(self.iconPath, 'clear.png'))
        self.iconApply = QtGui.QIcon(os.path.join(self.iconPath, 'apply.png'))
        self.iconCancel = QtGui.QIcon(os.path.join(self.iconPath, 'cancel.png'))
        #-- Setup --#
        self._setupWidget()

    def _setupWidget(self):
        """
        Setup widget ui
        """
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.tw_tree.setIndentation(0)
        self.tw_tree.setAlternatingRowColors(True)
        self._setupIcons()
        self.rf_headers()
        self.rf_toolTips()

    def _setupIcons(self):
        """
        Setup widget icons
        """
        self.pb_itemUp.setIcon(self.iconUp)
        self.pb_itemDn.setIcon(self.iconDn)
        self.pb_template.setIcon(self.iconTpl)
        self.pb_add.setIcon(self.iconAdd)
        self.pb_del.setIcon(self.iconDel)
        self.pb_edit1.setIcon(self.iconEdit)
        self.pb_edit2.setIcon(self.iconEdit)
        self.pb_apply.setIcon(self.iconApply)
        self.pb_cancel.setIcon(self.iconCancel)

    def rf_headers(self, *args):
        """
        Refresh widget tree headers

        :param args: header labels
        :type args: list
        """
        newHeader = QtGui.QTreeWidgetItem()
        if not args:
            self.tw_tree.setColumnCount(1)
            newHeader.setText(0, 'None')
        else:
            self.tw_tree.setColumnCount(len(args))
            for n, label in enumerate(args):
                newHeader.setText(n, label)
        self.tw_tree.setHeaderItem(newHeader)

    def rf_toolTips(self):
        """
        Refresh widgets toolTips
        """
        if not self.mainUi.showToolTips:
            wList = [self.pb_itemUp, self.pb_itemDn, self.pb_template, self.cbb_filter, self.pb_add, self.pb_del,
                     self.pb_edit1, self.pb_edit2, self.pb_apply, self.pb_cancel]
            for widget in wList:
                widget.setToolTip('')

    def rf_treeColumns(self):
        """
        Refresh tree column size
        """
        for n in range(self.tw_tree.columnCount()):
            self.tw_tree.resizeColumnToContents(n)