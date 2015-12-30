import os
from PyQt4 import QtGui
from lib.qt import procQt as pQt
from appli.fondation.gui.common import treeWidgetUi
from appli.fondation.gui.fondation._ui import tsEntitiesDialUI


class Entities(treeWidgetUi.TreeWidgetSettings):
    """
    ToolSettings Entities Class: Contains Entities settings, child of ToolSettings

    :param pWidget: Parent widget
    :type mainUi: ToolSettings
    """

    __edited__ = False

    def __init__(self, pWidget):
        self.pWidget = pWidget
        self.log = self.pWidget.log
        self.mainUi = self.pWidget.mainUi
        self.fondation = self.pWidget.fondation
        self.entities = self.fondation.entities
        super(Entities, self).__init__()

    def _setupUi(self):
        """
        Setup Groups widget
        """
        super(Entities, self)._setupUi()
        self.l_title.setText('Entities')
        self.qf_treeEdit_R.setVisible(False)
        self.tw_tree.setIndentation(15)
        self.tw_tree.header().setStretchLastSection(False)
        self.rf_headers('Entities', 'Types', 'SubTypes')
        self.rf_treeColumns()

    def _setupIcons(self):
        """
        Setup Groups icons
        """
        super(Entities, self)._setupIcons()
        #-- Init Icons --#
        self.iconClear = QtGui.QIcon(os.path.join(self.iconPath, 'clear.png'))
        #-- Add Icons --#
        self.pb_edit2.setIcon(self.iconClear)
        #-- Edit Label --#
        self.pb_edit1.setText("Edit")
        self.pb_edit2.setText("Clear")

    def rf_toolTips(self):
        """
        Refresh widgets toolTips
        """
        super(Entities, self).rf_toolTips()
        if self.mainUi.showToolTips:
            self.pb_itemUp.setToolTip("Move up selected entity")
            self.pb_itemDn.setToolTip("Move down selected entity")
            self.pb_add.setToolTip("Create new entity")
            self.pb_del.setToolTip("Delete selected entity")
            self.pb_edit1.setToolTip("Edit selected entity")
            self.pb_edit2.setToolTip("Clear selection")
            self.pb_apply.setToolTip("Apply datas to Fondation object")
            self.pb_cancel.setToolTip("Restore datas from Fondation object")

    def buildTree(self):
        """
        Build Groups tree widget
        """
        super(Entities, self).buildTree()
        if self.entities._entities:
            for entityObj in self.entities._entities:
                newItem = self.new_treeItem(entityObj)
                if entityObj.entityParent is None:
                    self.tw_tree.addTopLevelItem(newItem)
                else:
                    parent = self.getItemFromAttrValue('entityName', entityObj.entityParent)
                    if parent is not None:
                        parent.addChild(newItem)
        self.tw_tree.expandAll()
        self.rf_treeColumns()

    def ud_treeItem(self, item, **kwargs):
        """
        Update item datas and settings

        :param item: Entity tree item
        :type item: QtGui.QTreeWidgetItem
        :param kwargs: Entity item datas
        :type kwargs: dict
        """
        super(Entities, self).ud_treeItem(item, **kwargs)
        #-- Edit Item --#
        if item.itemObj.entityType == 'entity':
            item.setText(0, str(item.itemObj.entityLabel))
            item.setToolTip(0, item.itemObj.getDatas(asString=True))
        elif item.itemObj.entityType == 'type':
            item.setText(1, str(item.itemObj.entityLabel))
            item.setToolTip(1, item.itemObj.getDatas(asString=True))
        elif item.itemObj.entityType == 'subType':
            item.setText(2, str(item.itemObj.entityLabel))
            item.setToolTip(2, item.itemObj.getDatas(asString=True))

    def on_addItem(self):
        """
        Command launched when 'Add' QPushButton is clicked

        Add new entity to tree
        """
        super(Entities, self).on_addItem()
        selItems = self.tw_tree.selectedItems() or []
        #-- Create Entity Object --#
        if not selItems:
            entityObj = self.entities.newEntity(entityName='None', entityType='entity', entityParent=None)
            newItem = self.new_treeItem(entityObj)
            self.tw_tree.addTopLevelItem(newItem)
        else:
            if selItems[0].itemObj.entityType == 'entity':
                entityObj = self.entities.newEntity(entityName='None', entityType='type',
                                                    entityParent=selItems[0].itemObj.entityName)
            else:
                entityObj = self.entities.newEntity(entityName='None', entityType='subType',
                                                    entityParent=selItems[0].itemObj.entityName)
            newItem = self.new_treeItem(entityObj)
            selItems[0].addChild(newItem)
            #-- Refresh --#
            self.tw_tree.setItemExpanded(selItems[0], True)

    def on_editItem1(self):
        """
        Command launched when 'Edit' QPushButton is clicked

        Launch Entities editing dialog
        """
        super(Entities, self).on_editItem1()
        selItems = self.tw_tree.selectedItems() or []
        if selItems:
            self.dialEntities = EntitiesDialog(selItems[0], parent=self)
            self.dialEntities.exec_()
        else:
            message = "!!! Select at least one entity item !!!"
            pQt.errorDialog(message, self)

    def on_editItem2(self):
        """
        Command launched when 'Clear' QPushButton is clicked

        Clear selection
        """
        super(Entities, self).on_editItem2()
        self.tw_tree.clearSelection()

    def on_apply(self):
        """
        Command launched when 'Apply' QPushButton is clicked

        Store datas to itemObject
        """
        super(Entities, self).on_apply()
        ind = 0
        exclusionList = ['', ' ', 'None', None]
        #-- Parse Entity Tree --#
        entityDict = dict()
        treeDict = self.getDatas()
        for n in sorted(treeDict.keys()):
            if (not treeDict[n]['entityName'] in exclusionList and not treeDict[n]['entityLabel'] in exclusionList
                and not treeDict[n]['entityFolder'] in exclusionList):
                entityDict[ind] = treeDict[n]
                ind += 1
            else:
                self.log.warning("!!! ERROR: Entity values not valide, skipp %s !!!" % treeDict[n]['entityName'])
        #-- Store and refresh --#
        self.entities.buildEntitiesFromDict(entityDict)
        self.pWidget.rf_editedItemStyle()
        self.buildTree()


class EntitiesDialog(QtGui.QDialog, tsEntitiesDialUI.Ui_dial_entity):
    """
    ToolSettings Entities Dialog: edition, child of Entities

    :param selItem: Selected entity item
    :type selItem: QtGui.QTreeWidgetItem
    :param parent: Parent Ui
    :type parent: Entities
    """

    def __init__(self, selItem, parent=None):
        self.selItem = selItem
        self.log = parent.log
        super(EntitiesDialog, self).__init__(parent)
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup QtGui Entities dialog
        """
        self.log.detail("#----- Setup EntitiesDialog Ui -----#")
        self.setupUi(self)
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
        self.le_entityType.setText(str(self.selItem.itemObj.entityType))
        self.le_entityName.setText(str(self.selItem.itemObj.entityName))
        self.le_entityLabel.setText(str(self.selItem.itemObj.entityLabel))
        self.le_entityFolder.setText(str(self.selItem.itemObj.entityFolder))

    def rf_toolTips(self):
        """
        Refresh dialog toolTips
        """
        if self.parent().pWidget.mainUi.showToolTips:
            self.le_entityType.setToolTip("Entity type")
            self.le_entityName.setToolTip("Entity name")
            self.le_entityLabel.setToolTip("Entity label")
            self.le_entityFolder.setToolTip("Entity folder")
        else:
            wList = [self.le_entityType, self.le_entityName, self.le_entityLabel, self.le_entityFolder]
            for widget in wList:
                widget.setToolTip('')

    def on_save(self):
        """
        Command launched when 'Save' QPushButton is clicked

        Save entity datas
        """
        #-- Get Datas --#
        excludes = ['', ' ', 'None']
        entityType = str(self.le_entityType.text())
        entityName = str(self.le_entityName.text())
        entityLabel = str(self.le_entityLabel.text())
        entityFolder = str(self.le_entityFolder.text())
        #-- Check Datas --#
        if entityName in excludes or entityLabel in excludes or entityFolder in excludes:
            message = "!!! 'name', 'label' or 'folder' invalid: %s -- %s -- %s !!!" % (entityName, entityLabel,
                                                                                       entityFolder)
            pQt.errorDialog(message, self)
            raise AttributeError(message)
        #-- Check New Entity Datas --#
        message = None
        entitiesDatas = self.parent().getDatas()
        for n in sorted(entitiesDatas.keys()):
            if entityType == entitiesDatas[n]['entityType']:
                if not entityName == self.selItem.itemObj.entityName:
                    if entitiesDatas[n]['entityName'] is not None:
                        if entityName == entitiesDatas[n]['entityName']:
                            message = "!!! Entity name %s already exists !!!" % entityName
                elif not entityLabel == self.selItem.itemObj.entityLabel:
                    if entitiesDatas[n]['entityLabel'] is not None:
                        if entityLabel == entitiesDatas[n]['entityLabel']:
                            message = "!!! Entity label %s already exists !!!" % entityLabel
                elif not entityFolder == self.selItem.itemObj.entityFolder:
                    if entitiesDatas[n]['entityFolder'] is not None:
                        if entityFolder == entitiesDatas[n]['entityFolder']:
                            message = "!!! Entity folder %s already exists !!!" % entityFolder
        if message is not None:
            pQt.errorDialog(message, self)
            raise AttributeError(message)
        #-- Edit Entity --#
        self.parent().ud_treeItem(self.selItem, entityName=entityName, entityLabel=entityLabel,
                                  entityFolder=entityFolder)
        #-- Quit --#
        self.parent().rf_treeColumns()
        self.close()
