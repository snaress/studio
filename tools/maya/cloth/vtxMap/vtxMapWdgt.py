from PyQt4 import QtGui
from tools.maya.cloth.vtxMap import vtxMapCmds as vmCmds
from tools.maya.cloth.vtxMap.ui import wgVtxMapUI, wgVtxEditUI
try:
    import maya.cmds as mc
except:
    pass


class VtxMapNode(QtGui.QWidget, wgVtxMapUI.Ui_wgVtxMap):

    def __init__(self, clothNode, mapName):
        self.clothNode = clothNode
        self.mapName = mapName
        self.mapType = "%sMapType" % self.mapName
        self.vtxMap = "%sPerVertex" % self.mapName
        super(VtxMapNode, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        self.lVtxMap.setText(self.mapName)
        self.cbState.setCurrentIndex(vmCmds.getVtxMapType(self.clothNode, self.mapType))
        self.cbState.currentIndexChanged.connect(self.on_mapType)
        self.rf_vtxMapLabel()

    @property
    def vtxMapIndex(self):
        """ Get vtxMap current type
            :return: (int) : VtxMap type (0 = None, 1 = Vertex, 2 = Texture) """
        return self.cbState.currentIndex()

    @property
    def vtxMapType(self):
        """ Get vtxMap current type
            :return: (str) : VtxMap type (None, Vertex or Texture) """
        return str(self.cbState.currentText())

    def rf_vtxMapLabel(self):
        """ Refresh mapType label color """
        if self.vtxMapIndex == 0:
            self.lVtxMap.setStyleSheet("color: rgb(175, 175, 175)")
        elif self.vtxMapIndex == 1:
            self.lVtxMap.setStyleSheet("color: rgb(0, 255, 0)")
        elif self.vtxMapIndex == 2:
            self.lVtxMap.setStyleSheet("color: rgb(0, 125, 255)")

    def on_mapType(self):
        """ Command launched when QComboBox 'mapType' current index changed """
        vmCmds.setVtxMapType(self.clothNode, self.mapType, self.cbState.currentIndex())
        self.rf_vtxMapLabel()


class VtxEditUi(QtGui.QWidget, wgVtxEditUI.Ui_wgVtxEdit):

    def __init__(self, mainUi):
        self.mainUi = mainUi
        super(VtxEditUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        self.setupUi(self)
        self.rbVtxRange.clicked.connect(self.rf_vtxSelMode)
        self.rbVtxValue.clicked.connect(self.rf_vtxSelMode)
        self.pbVtxSelect.clicked.connect(self.on_vtxSelection)
        self.pbVtxClear.clicked.connect(self.on_vtxClear)

    def rf_vtxSelMode(self):
        """ Refresh 'Vertex Selection Mode' """
        if self.rbVtxRange.isChecked():
            self.lRangeMin.setText("Min=")
            self.lRangeMax.setVisible(True)
            self.sbRangeMax.setVisible(True)
        else:
            self.lRangeMin.setText("Value=")
            self.lRangeMax.setVisible(False)
            self.sbRangeMax.setVisible(False)

    def on_vtxSelection(self):
        """ Command launched when QPushButton 'Select' (range) is clicked """
        selItems = self.twMapType.selectedItems()
        if selItems:
            if self.rbVtxRange.isChecked():
                vmCmds.selectVtx(selItems[0]._widget.clothNode, selItems[0]._widget.vtxMap, 'range',
                                 minInf=self.sbRangeMin.value(), maxInf=self.sbRangeMax.value())
            elif self.rbVtxValue.isChecked():
                vmCmds.selectVtx(selItems[0]._widget.clothNode, selItems[0]._widget.vtxMap, 'value',
                                 value=self.sbRangeMin.value())

    @staticmethod
    def on_vtxClear():
        """ Command launched when QPushButton 'Clear' (range) is clicked """
        mc.select(cl=True)
