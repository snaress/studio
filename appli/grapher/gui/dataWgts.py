from PyQt4 import QtGui
from appli.grapher.gui.ui import wgDataGroupUI, wgDataNodeIdUI


class DataZone(object):

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("---> Setup DataZone ...")
        self.addAllCategory()

    def addCategory(self, groupName, QWidget):
        #-- Add Data Group --#
        dataGrp = QtGui.QTreeWidgetItem()
        dataGrp.setBackgroundColor(0, QtGui.QColor(200, 200, 200))
        dataGrp._widget = DataGroup(self.mainUi, dataGrp, groupName=groupName)
        self.mainUi.twNodeData.addTopLevelItem(dataGrp)
        self.mainUi.twNodeData.setItemWidget(dataGrp, 0, dataGrp._widget)
        #-- Add Data Params --#
        dataParams = QtGui.QTreeWidgetItem()
        dataParams._widget = QWidget
        dataGrp.addChild(dataParams)
        self.mainUi.twNodeData.setItemWidget(dataParams, 0, dataParams._widget)

    def addAllCategory(self):
        self.addCategory('Node Id', DataNodeId(self.mainUi))


class DataGroup(QtGui.QWidget, wgDataGroupUI.Ui_wgDataGroup):

    def __init__(self, mainUi, pItem, groupName='Untitled'):
        self.mainUi = mainUi
        self.pItem = pItem
        self.grpName = groupName
        self.collapseIcon = QtGui.QIcon("gui/ui/icon/treeCollapse.png")
        self.expandIcon = QtGui.QIcon("gui/ui/icon/treeExpand.png")
        super(DataGroup, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        self.setupUi(self)
        self.lGrpName.setText(self.grpName)
        self.pbGrpName.clicked.connect(self.on_icon)
        self.rf_icon()

    def rf_icon(self):
        if self.pbGrpName.isChecked():
            self.pbGrpName.setIcon(self.collapseIcon)
        else:
            self.pbGrpName.setIcon(self.expandIcon)

    def on_icon(self):
        self.mainUi.twNodeData.setItemExpanded(self.pItem, self.pbGrpName.isChecked())
        self.rf_icon()


class DataNodeId(QtGui.QWidget, wgDataNodeIdUI.Ui_wgNodeId):

    def __init__(self, mainUi):
        self.mainUi = mainUi
        super(DataNodeId, self).__init__()
        self.setupUi(self)
