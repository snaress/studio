from PyQt4 import QtGui
from appli.foundation.gui.foundation._ui import wg_projectTreeUI


class ProjectTree(QtGui.QWidget, wg_projectTreeUI.Ui_wg_projectTree):

    def __init__(self, parent=None):
        self.log = parent.log
        self.foundation = parent.foundation
        self.project = self.foundation.project
        self.entities = self.project.entities
        super(ProjectTree, self).__init__(parent)
        self._setupWidget()

    def _setupWidget(self):
        """
        Setup widget ui
        """
        self.log.info("#----- Setup Project Tree -----#")
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.rb_asset.clicked.connect(self.buildTree)
        self.rb_shot.clicked.connect(self.buildTree)

    @property
    def context(self):
        """
        Get current context

        :return: Current context ('asset' or 'shot')
        :rtype: str
        """
        if self.rb_asset.isChecked():
            return 'asset'
        if self.rb_shot.isChecked():
            return 'shot'

    def buildTree(self):
        """
        Build project tree
        """
        self.log.detail(">>> Build project tree: %s ..." % self.context)
        self.tw_project.clear()
        for entityObj in self.entities.contextTree(self.context):
            mainEntityItem = self.new_treeItem(entityObj)
            self.tw_project.addTopLevelItem(mainEntityItem)
            for childObj in entityObj._childs:
                subEntityItem = self.new_treeItem(childObj)
                mainEntityItem.addChild(subEntityItem)

    @staticmethod
    def new_treeItem(itemObj):
        """
        Create project tree item

        :param itemObj: Entity object
        :type itemObj: Entity | Asset | Shot
        :return: New project tree item
        :rtype: QtGui.QTreeWidgetItem
        """
        newItem = QtGui.QTreeWidgetItem()
        newItem.itemObj = itemObj
        newItem.setText(0, itemObj.entityLabel)
        return newItem
