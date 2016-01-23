from PyQt4 import QtGui
from lib.qt import procQt as pQt
from appli.foundation.gui.common import widgetsUi
from appli.foundation.gui.foundation._ui import ts_entitiesDialUI


class Assets(widgetsUi.BasicTree):
    """
    Assets Class: Contains Assets settings, child of ToolSettings

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
        self.entities = self.foundation.project.entities
        super(Assets, self).__init__(pWidget)

    def _setupWidget(self):
        """
        Setup Assets widget
        """
        super(Assets, self)._setupWidget()
        self.l_title.setText('Assets')
        self.cbb_filter.setVisible(False)
        self.qf_treeEdit_R.setVisible(False)
        self.tw_tree.setIndentation(20)
        self.tw_tree.header().setStretchLastSection(False)
        self.rf_headers('Asset Type', 'Asset SubType')
        self.rf_treeColumns()

    def _setupIcons(self):
        """
        Setup Assets icons
        """
        super(Assets, self)._setupIcons()
        #-- Edit Label --#
        self.pb_edit1.setText("Edit")
        self.pb_edit2.setText("Clear")
        self.pb_edit2.setIcon(self.iconClear)
        #-- Edit Grade --#
        if not self.userGroups._user.grade == 0:
            self.pb_del.setEnabled(False)

    def rf_toolTips(self):
        """
        Refresh widgets toolTips
        """
        super(Assets, self).rf_toolTips()
        if self.mainUi.showToolTips:
            self.pb_itemUp.setToolTip("Move up selected entity")
            self.pb_itemDn.setToolTip("Move down selected entity")
            self.pb_add.setToolTip("Create new entity")
            self.pb_del.setToolTip("Delete selected entity")
            self.pb_edit1.setToolTip("Edit selected entity")
            self.pb_edit2.setToolTip("Clear selection")
            self.pb_apply.setToolTip("Apply datas to Foundation object")
            self.pb_cancel.setToolTip("Restore datas from Foundation object")
            #-- Edit Grade --#
            if not self.userGroups._user.grade == 0:
                self.pb_del.setToolTip("Delete selected entity (Disabled for your grade)")

    def buildTree(self):
        """
        Build Assets tree widget
        """
        super(Assets, self).buildTree()
        self.log.detail("---> Assets tree")
        for entityObj in self.entities.contextTree('asset'):
            entityItem = self.new_treeItem(entityObj)
            self.tw_tree.addTopLevelItem(entityItem)
            for subEntityObj in entityObj._childs:
                subEntityItem = self.new_treeItem(subEntityObj)
                entityItem.addChild(subEntityItem)
        self.rf_treeColumns()

    def ud_treeItem(self, item, **kwargs):
        """
        Update item datas and settings

        :param item: Entity tree item
        :type item: QtGui.QTreeWidgetItem
        :param kwargs: Entity item datas (key must starts with 'entity')
        :type kwargs: dict
        """
        super(Assets, self).ud_treeItem(item, **kwargs)
        #-- Edit Item --#
        if item.itemObj.entityType == 'mainType':
            item.setText(0, str(item.itemObj.entityLabel))
        else:
            item.setText(1, str(item.itemObj.entityLabel))

    def on_addItem(self):
        """
        Command launched when 'Add' QPushButton is clicked

        Add new entity to tree
        """
        super(Assets, self).on_addItem()
        selItems = self.tw_tree.selectedItems() or []
        if selItems:
            if selItems[0].itemObj.entityType == 'mainType':
                self.dial_entities = EntitiesDialog('asset', 'add', selItem=selItems[0], parent=self)
            else:
                self.dial_entities = EntitiesDialog('asset', 'add', selItem=selItems[0].parent(), parent=self)
        else:
            self.dial_entities = EntitiesDialog('asset', 'add', parent=self)
        self.dial_entities.exec_()

    def on_editItem1(self):
        """
        Command launched when 'Edit' QPushButton is clicked

        Launch Entity editing dialog
        """
        super(Assets, self).on_editItem1()
        selItems = self.tw_tree.selectedItems() or []
        if selItems:
            self.dial_entities = EntitiesDialog('asset', 'edit', selItem=selItems[0], parent=self)
            self.dial_entities.exec_()
        else:
            message = "!!! Select at least one entity item !!!"
            pQt.errorDialog(message, self)

    def on_editItem2(self):
        """
        Command launched when 'Clear' QPushButton is clicked

        Clear selection
        """
        super(Assets, self).on_editItem1()
        self.tw_tree.clearSelection()

    def on_apply(self):
        """
        Command launched when 'Apply' QPushButton is clicked

        Store datas to itemObject
        """
        super(Assets, self).on_apply()
        #-- Parse Tree --#
        treeDict = self.getDatas()
        self.entities.updateEntitiesFromDict('asset', treeDict)
        self.pWidget.rf_editedItemStyle()
        self.buildTree()


class Shots(widgetsUi.BasicTree):
    """
    Shots Class: Contains Shots settings, child of ToolSettings

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
        self.entities = self.foundation.project.entities
        super(Shots, self).__init__(pWidget)

    def _setupWidget(self):
        """
        Setup Assets widget
        """
        super(Shots, self)._setupWidget()
        self.l_title.setText('Shots')
        self.cbb_filter.setVisible(False)
        self.qf_treeEdit_R.setVisible(False)
        self.tw_tree.setIndentation(20)
        self.tw_tree.header().setStretchLastSection(False)
        self.rf_headers('Shot Type', 'Shot SubType')
        self.rf_treeColumns()

    def _setupIcons(self):
        """
        Setup Assets icons
        """
        super(Shots, self)._setupIcons()
        #-- Edit Label --#
        self.pb_edit1.setText("Edit")
        self.pb_edit2.setText("Clear")
        self.pb_edit2.setIcon(self.iconClear)
        #-- Edit Grade --#
        if not self.userGroups._user.grade == 0:
            self.pb_del.setEnabled(False)

    def rf_toolTips(self):
        """
        Refresh widgets toolTips
        """
        super(Shots, self).rf_toolTips()
        if self.mainUi.showToolTips:
            self.pb_itemUp.setToolTip("Move up selected entity")
            self.pb_itemDn.setToolTip("Move down selected entity")
            self.pb_add.setToolTip("Create new entity")
            self.pb_del.setToolTip("Delete selected entity")
            self.pb_edit1.setToolTip("Edit selected entity")
            self.pb_edit2.setToolTip("Clear selection")
            self.pb_apply.setToolTip("Apply datas to Foundation object")
            self.pb_cancel.setToolTip("Restore datas from Foundation object")
            #-- Edit Grade --#
            if not self.userGroups._user.grade == 0:
                self.pb_del.setToolTip("Delete selected entity (Disabled for your grade)")

    def ud_treeItem(self, item, **kwargs):
        """
        Update item datas and settings

        :param item: Entity tree item
        :type item: QtGui.QTreeWidgetItem
        :param kwargs: Entity item datas (key must starts with 'entity')
        :type kwargs: dict
        """
        super(Shots, self).ud_treeItem(item, **kwargs)
        #-- Edit Item --#
        if item.itemObj.entityType == 'mainType':
            item.setText(0, str(item.itemObj.entityLabel))
        else:
            item.setText(1, str(item.itemObj.entityLabel))

    def on_addItem(self):
        """
        Command launched when 'Add' QPushButton is clicked

        Add new entity to tree
        """
        super(Shots, self).on_addItem()
        selItems = self.tw_tree.selectedItems() or []
        if selItems:
            if selItems[0].itemObj.entityType == 'mainType':
                self.dial_entities = EntitiesDialog('shot', 'add', selItem=selItems[0], parent=self)
            else:
                self.dial_entities = EntitiesDialog('shot', 'add', selItem=selItems[0].parent(), parent=self)
        else:
            self.dial_entities = EntitiesDialog('shot', 'add', parent=self)
        self.dial_entities.exec_()

    def on_editItem1(self):
        """
        Command launched when 'Edit' QPushButton is clicked

        Launch Entity editing dialog
        """
        super(Shots, self).on_editItem1()
        selItems = self.tw_tree.selectedItems() or []
        if selItems:
            self.dial_entities = EntitiesDialog('shot', 'edit', selItem=selItems[0], parent=self)
            self.dial_entities.exec_()
        else:
            message = "!!! Select at least one entity item !!!"
            pQt.errorDialog(message, self)

    def on_editItem2(self):
        """
        Command launched when 'Clear' QPushButton is clicked

        Clear selection
        """
        super(Shots, self).on_editItem1()
        self.tw_tree.clearSelection()


class EntitiesDialog(QtGui.QDialog, ts_entitiesDialUI.Ui_Dial_entities):
    """
    Entities Dialog: Entities edition, child of Assets, Shots

    :param entity: 'asset' or 'shot'
    :type entity: str
    :param dialogMode: 'add' or 'edit'
    :type dialogMode: str
    :param selItem: Selected entity item
    :type selItem: QtGui.QTreeWidgetItem
    :param parent: Parent Ui
    :type parent: Assets || Shots
    """

    def __init__(self, entity, dialogMode, selItem=None, parent=None):
        self.entity = entity
        self.dialogMode = dialogMode
        self.selItem = selItem
        self.log = parent.log
        self.log.title = 'TS_entities'
        super(EntitiesDialog, self).__init__(parent)
        self._setupUi()

    def _setupUi(self):
        """
        Setup QtGui Entities dialog
        """
        self.log.detail("#----- Setup entitiesDialog Ui -----#")
        self.setupUi(self)
        #-- Labels --#
        self.l_message.setText("Edit %s Entity" % self.entity.title())
        for label in [self.l_context, self.l_type, self.l_code, self.l_name, self.l_label, self.l_folder]:
            label.setText("Entity %s" % str(label.text()))
        #-- Mode --#
        self.le_context.setReadOnly(True)
        self.le_type.setReadOnly(True)
        if self.dialogMode == 'edit':
            self.le_code.setReadOnly(True)
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
        if self.dialogMode == 'add':
            if self.selItem is None:
                self.le_type.setText("mainType")
                self.le_context.setText(str(self.entity))
            else:
                self.le_type.setText("subType")
                self.le_context.setText(str(self.selItem.itemObj.entityContext))
        else:
            self.le_context.setText(str(self.selItem.itemObj.entityContext))
            self.le_type.setText(str(self.selItem.itemObj.entityType))
            self.le_code.setText(str(self.selItem.itemObj.entityCode))
            self.le_name.setText(str(self.selItem.itemObj.entityName))
            self.le_label.setText(str(self.selItem.itemObj.entityLabel))
            self.le_folder.setText(str(self.selItem.itemObj.entityFolder))

    def rf_toolTips(self):
        """
        Refresh dialog toolTips
        """
        if self.parent().mainUi.showToolTips:
            self.le_type.setToolTip("%s context ('asset', 'shot')" % self.entity)
            self.le_type.setToolTip("%s type ('mainType', 'subType')" % self.entity)
            self.le_code.setToolTip("%s code ('char', 'prop')" % self.entity)
            self.le_name.setToolTip("%s name ('character', 'prop')" % self.entity)
            self.le_label.setToolTip("%s label ('Character', 'Prop')" % self.entity)
            self.le_folder.setToolTip("%s folder ('chars', 'props')" % self.entity)
        else:
            wList = [self.le_context, self.le_type, self.le_code, self.le_name, self.le_label, self.le_folder]
            for widget in wList:
                widget.setToolTip('')

    def on_save(self):
        """
        Command launched when 'Save' QPushButton is clicked

        Save entity datas
        """
        #-- Get Datas --#
        excludes = ['', ' ', 'None', None]
        entityContext = str(self.le_context.text())
        entityType = str(self.le_type.text())
        entityCode = str(self.le_code.text())
        entityName = str(self.le_name.text())
        entityLabel = str(self.le_label.text())
        entityFolder = str(self.le_folder.text())
        #-- Check Datas --#
        if entityCode in excludes or entityName in excludes or entityLabel in excludes or entityFolder in excludes:
            mess = "%s -- %s -- %s -- %s" % (entityCode, entityName, entityLabel, entityFolder)
            message = "!!! 'code', 'name', 'label' or 'folder' invalid: %s  !!!" % mess
            pQt.errorDialog(message, self)
            raise AttributeError(message)
        #-- Check New Code --#
        if self.dialogMode == 'add':
            if self.selItem is None:
                items = pQt.getTopItems(self.parent().tw_tree)
            else:
                items = pQt.getAllChildren(self.selItem)
            for item in items:
                for attr in ['entityCode', 'entityName']:
                    if entityCode == getattr(item.itemObj, attr):
                        message = "!!! %s already exists !!!" % entityCode
                        pQt.errorDialog(message, self)
                        raise AttributeError(message)
        #-- Add Entity --#
        if self.dialogMode == 'add':
            self.log.detail("Adding new %s entity %s: %s" % (entityContext, entityType, entityName))
            if self.selItem is None:
                itemObj = None
            else:
                itemObj = self.selItem.itemObj
            entityObj = self.parent().entities.newEntity(parent=itemObj,
                                                         entityContext=entityContext, entityType=entityType,
                                                         entityCode=entityCode, entityName=entityName,
                                                         entityLabel=entityLabel, entityFolder=entityFolder)
            entityItem = self.parent().new_treeItem(entityObj)
            if self.selItem is None:
                self.parent().tw_tree.addTopLevelItem(entityItem)
            else:
                self.selItem.addChild(entityItem)
            self.parent().ud_treeItem(entityItem)
        #-- Edit Entity --#
        elif self.dialogMode == 'edit':
            self.log.detail("Editing %s entity %s: %s" % (entityContext, entityType, entityName))
            self.parent().ud_treeItem(self.selItem, entityName=entityName, entityLabel=entityLabel,
                                      entityFolder=entityFolder)
        #-- Quit --#
        self.parent().rf_treeColumns()
        self.close()
