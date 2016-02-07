from PyQt4 import QtGui, QtCore
from lib.qt import procQt as pQt
from appli.foundation.gui.common import widgetsUi
from appli.foundation.gui.foundation._ui import ts_entitiesDialUI


class CommonEntity(widgetsUi.BasicTree):
    """
    Groups Class: Contains UserGroups settings, child of ToolSettings

    :param pWidget: Parent widget
    :type pWidget: ToolSettings | ProjectSettings
    :param settingsMode: 'tool' or 'project'
    :type settingsMode: str
    """

    def __init__(self, pWidget, settingsMode='tool'):
        self.pWidget = pWidget
        self.settingsMode = settingsMode
        self.log = self.pWidget.log
        self.mainUi = self.pWidget.parent()
        self.foundation = self.fdn = self.pWidget.foundation
        self.userGrps = self.fdn.userGrps
        self.users = self.fdn.users
        self.entities = self.fdn.project.entities
        super(CommonEntity, self).__init__(pWidget)

    def _initWidget(self):
        """
        Init widget core
        """
        super(CommonEntity, self)._initWidget()
        self.entities.buildFromSettings()

    def _setupWidget(self):
        """
        Setup CommonEntity widget
        """
        super(CommonEntity, self)._setupWidget()
        self.l_title.setText('%ss' % self.__context__.capitalize())
        self.qf_treeEdit_R.setVisible(False)
        self.tw_tree.setIndentation(20)
        self.tw_tree.header().setStretchLastSection(False)
        self.rf_headers('%s Type' % self.__context__.capitalize(),
                        '%s SubType' % self.__context__.capitalize())
        if self.settingsMode == 'tool':
            self.pb_template.setVisible(False)
        self.rf_treeColumns()

    def _setupIcons(self):
        """
        Setup CommonEntity icons
        """
        super(CommonEntity, self)._setupIcons()
        #-- Edit Label --#
        self.pb_edit1.setText("Edit")
        self.pb_edit2.setText("Clear")
        self.pb_edit2.setIcon(self.iconClear)
        #-- Edit Filters --#
        self.buildFilters()
        #-- Edit Grade --#
        if self.settingsMode == 'tool':
            if not self.users._user.grade == 0:
                self.pb_del.setEnabled(False)
        elif self.settingsMode == 'project':
            if not self.users._user.grade <= 3:
                self.pb_del.setEnabled(False)

    def rf_toolTips(self):
        """
        Refresh widgets toolTips
        """
        super(CommonEntity, self).rf_toolTips()
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
            if not self.users._user.grade == 0:
                self.pb_del.setToolTip("Delete selected entity (Disabled for your grade)")

    def buildFilters(self):
        """
        Build comboBox filters
        """
        super(CommonEntity, self).buildFilters()
        self.cbb_filter.addItems(['Code', 'Name', 'Label'])
        self.cbb_filter.setEditable(True)
        self.cbb_filter.lineEdit().setReadOnly(True)
        self.cbb_filter.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        for n in range(self.cbb_filter.count()):
            self.cbb_filter.setItemData(n, QtCore.Qt.AlignCenter, QtCore.Qt.TextAlignmentRole)

    def buildTree(self):
        """
        Build CommonEntity tree widget
        """
        super(CommonEntity, self).buildTree()
        self.log.detail("---> %ss tree" % self.__context__.capitalize())
        for entityObj in self.entities.contextTree(self.__context__):
            entityItem = self.new_treeItem(entityObj)
            self.tw_tree.addTopLevelItem(entityItem)
            for subEntityObj in entityObj._childs:
                subEntityItem = self.new_treeItem(subEntityObj)
                entityItem.addChild(subEntityItem)
        self.rf_treeColumns()

    def ud_treeItem(self, item, **kwargs):
        """
        Update item data and settings

        :param item: Entity tree item
        :type item: QtGui.QTreeWidgetItem
        :param kwargs: Entity item datas (key must starts with 'entity')
        :type kwargs: dict
        """
        super(CommonEntity, self).ud_treeItem(item, **kwargs)
        #-- Edit Item --#
        if item.itemObj.entityType == 'mainType':
            index = 0
        else:
            index = 1
        item.setText(index, str(getattr(item.itemObj, 'entity%s' % str(self.cbb_filter.currentText()))))

    def on_filter(self):
        """
        Command launched when 'Filter' QComboBox item is clicked

        Update use tree display
        """
        super(CommonEntity, self).on_filter()
        for item in pQt.getAllItems(self.tw_tree):
            self.ud_treeItem(item)
        self.rf_treeColumns()

    def on_addItem(self):
        """
        Command launched when 'Add' QPushButton is clicked

        Add new entity to tree
        """
        super(CommonEntity, self).on_addItem()
        selItems = self.tw_tree.selectedItems() or []
        if selItems:
            if selItems[0].itemObj.entityType == 'mainType':
                self.dial_entities = EntitiesDialog(self.__context__, 'add', selItem=selItems[0], parent=self)
            else:
                self.dial_entities = EntitiesDialog(self.__context__, 'add', selItem=selItems[0].parent(), parent=self)
        else:
            self.dial_entities = EntitiesDialog(self.__context__, 'add', parent=self)
        self.dial_entities.exec_()

    def on_delItem(self):
        """
        Command launched when 'Del' QPushButton is clicked

        Delete selected entity from tree
        """
        selItems = self.tw_tree.selectedItems() or []
        if selItems:
            if not selItems[0] in self.__editedItems__['deleted']:
                self.__editedItems__['deleted'].append(selItems[0])
                if selItems[0] in self.__editedItems__['added']:
                    self.__editedItems__['added'].remove(selItems[0])
                if selItems[0] in self.__editedItems__['edited']:
                    self.__editedItems__['edited'].remove(selItems[0])
        self.rf_itemStyle()

    def on_editItem1(self):
        """
        Command launched when 'Edit' QPushButton is clicked

        Launch Entity editing dialog
        """
        super(CommonEntity, self).on_editItem1()
        selItems = self.tw_tree.selectedItems() or []
        if selItems:
            self.dial_entities = EntitiesDialog(self.__context__, 'edit', selItem=selItems[0], parent=self)
            self.dial_entities.exec_()
        else:
            message = "!!! Select at least one entity item !!!"
            pQt.errorDialog(message, self)

    def on_editItem2(self):
        """
        Command launched when 'Clear' QPushButton is clicked

        Clear selection
        """
        super(CommonEntity, self).on_editItem1()
        self.tw_tree.clearSelection()


class Assets(CommonEntity):
    """
    Assets Class: Contains Assets settings, child of ToolSettings

    :param pWidget: Parent widget
    :type pWidget: ToolSettings | ProjectSettings
    :param settingsMode: 'tool' or 'project'
    :type settingsMode: str
    """

    __context__ = 'asset'

    def __init__(self, pWidget, settingsMode='tool'):
        super(Assets, self).__init__(pWidget, settingsMode=settingsMode)


class Shots(CommonEntity):
    """
    Shots Class: Contains Shots settings, child of ToolSettings

    :param pWidget: Parent widget
    :type pWidget: ToolSettings | ProjectSettings
    :param settingsMode: 'tool' or 'project'
    :type settingsMode: str
    """

    __context__ = 'shot'

    def __init__(self, pWidget, settingsMode='tool'):
        super(Shots, self).__init__(pWidget, settingsMode=settingsMode)


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
        for label in [self.l_context, self.l_type, self.l_code, self.l_name]:
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

    def rf_toolTips(self):
        """
        Refresh dialog toolTips
        """
        if self.parent().mainUi.showToolTips:
            self.le_context.setToolTip("%s context ('asset', 'shot')" % self.entity)
            self.le_type.setToolTip("%s type ('mainType', 'subType')" % self.entity)
            self.le_code.setToolTip("%s code ('char', 'prop')" % self.entity)
            self.le_name.setToolTip("%s name ('character', 'prop')" % self.entity)
        else:
            wList = [self.le_context, self.le_type, self.le_code, self.le_name]
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
        #-- Check Datas --#
        if entityCode in excludes or entityName in excludes:
            mess = "%s -- %s" % (entityCode, entityName)
            message = "!!! 'code', 'name', 'label' invalid: %s  !!!" % mess
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
            #-- Get ItemObj --#
            if self.selItem is None:
                itemObj = None
            else:
                itemObj = self.selItem.itemObj
            #-- Create Entity --#
            entityObj = self.parent().entities.newEntity(parent=itemObj,
                                                         entityContext=entityContext, entityType=entityType,
                                                         entityCode=entityCode, entityName=entityName)
            entityItem = self.parent().new_treeItem(entityObj)
            #-- Add Entity --#
            if self.selItem is None:
                self.parent().tw_tree.addTopLevelItem(entityItem)
            else:
                self.selItem.addChild(entityItem)
            #-- Store edition and refresh --#
            if not entityItem in self.parent().__editedItems__['added']:
                self.parent().__editedItems__['added'].append(entityItem)
            self.parent().ud_treeItem(entityItem)
        #-- Edit Entity --#
        elif self.dialogMode == 'edit':
            self.log.detail("Editing %s entity %s: %s" % (entityContext, entityType, entityName))
            #-- Store edition and refresh --#
            if not self.selItem in self.parent().__editedItems__['edited']:
                if not self.selItem in self.parent().__editedItems__['added']:
                    self.parent().__editedItems__['edited'].append(self.selItem)
            self.parent().ud_treeItem(self.selItem, entityName=entityName)
        #-- Quit --#
        self.parent().rf_treeColumns()
        self.parent().rf_itemStyle()
        self.close()
