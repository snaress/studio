# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\vtxMap\ui\wgVtxEdit.ui'
#
# Created: Fri Mar 20 00:25:44 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_wgVtxEdit(object):
    def setupUi(self, wgVtxEdit):
        wgVtxEdit.setObjectName(_fromUtf8("wgVtxEdit"))
        wgVtxEdit.resize(517, 305)
        self.gridLayout = QtGui.QGridLayout(wgVtxEdit)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line = QtGui.QFrame(wgVtxEdit)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 4, 0, 1, 1)
        self.hlClampVal = QtGui.QHBoxLayout()
        self.hlClampVal.setSpacing(2)
        self.hlClampVal.setContentsMargins(-1, 0, -1, -1)
        self.hlClampVal.setObjectName(_fromUtf8("hlClampVal"))
        self.lClampVal = QtGui.QLabel(wgVtxEdit)
        self.lClampVal.setMinimumSize(QtCore.QSize(80, 0))
        self.lClampVal.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lClampVal.setObjectName(_fromUtf8("lClampVal"))
        self.hlClampVal.addWidget(self.lClampVal)
        self.cbClampMin = QtGui.QCheckBox(wgVtxEdit)
        self.cbClampMin.setMinimumSize(QtCore.QSize(40, 0))
        self.cbClampMin.setMaximumSize(QtCore.QSize(40, 16777215))
        self.cbClampMin.setChecked(True)
        self.cbClampMin.setObjectName(_fromUtf8("cbClampMin"))
        self.hlClampVal.addWidget(self.cbClampMin)
        self.sbClampMin = QtGui.QDoubleSpinBox(wgVtxEdit)
        self.sbClampMin.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.sbClampMin.setDecimals(4)
        self.sbClampMin.setMinimum(-99.0)
        self.sbClampMin.setObjectName(_fromUtf8("sbClampMin"))
        self.hlClampVal.addWidget(self.sbClampMin)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlClampVal.addItem(spacerItem)
        self.cbClampMax = QtGui.QCheckBox(wgVtxEdit)
        self.cbClampMax.setMinimumSize(QtCore.QSize(40, 0))
        self.cbClampMax.setMaximumSize(QtCore.QSize(40, 16777215))
        self.cbClampMax.setChecked(True)
        self.cbClampMax.setObjectName(_fromUtf8("cbClampMax"))
        self.hlClampVal.addWidget(self.cbClampMax)
        self.sbClampMax = QtGui.QDoubleSpinBox(wgVtxEdit)
        self.sbClampMax.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.sbClampMax.setDecimals(4)
        self.sbClampMax.setMinimum(-99.0)
        self.sbClampMax.setProperty("value", 1.0)
        self.sbClampMax.setObjectName(_fromUtf8("sbClampMax"))
        self.hlClampVal.addWidget(self.sbClampMax)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlClampVal.addItem(spacerItem1)
        self.gridLayout.addLayout(self.hlClampVal, 7, 0, 1, 1)
        self.line_2 = QtGui.QFrame(wgVtxEdit)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 11, 0, 1, 1)
        self.line_3 = QtGui.QFrame(wgVtxEdit)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 14, 0, 1, 1)
        self.pbFlood = QtGui.QPushButton(wgVtxEdit)
        self.pbFlood.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbFlood.setObjectName(_fromUtf8("pbFlood"))
        self.gridLayout.addWidget(self.pbFlood, 8, 0, 1, 1)
        self.hlSelBtn = QtGui.QHBoxLayout()
        self.hlSelBtn.setSpacing(2)
        self.hlSelBtn.setContentsMargins(-1, 0, -1, -1)
        self.hlSelBtn.setObjectName(_fromUtf8("hlSelBtn"))
        self.pbVtxSelect = QtGui.QPushButton(wgVtxEdit)
        self.pbVtxSelect.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbVtxSelect.setObjectName(_fromUtf8("pbVtxSelect"))
        self.hlSelBtn.addWidget(self.pbVtxSelect)
        self.pbVtxClear = QtGui.QPushButton(wgVtxEdit)
        self.pbVtxClear.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbVtxClear.setObjectName(_fromUtf8("pbVtxClear"))
        self.hlSelBtn.addWidget(self.pbVtxClear)
        self.gridLayout.addLayout(self.hlSelBtn, 2, 0, 1, 1)
        self.hlEditVal = QtGui.QHBoxLayout()
        self.hlEditVal.setSpacing(2)
        self.hlEditVal.setContentsMargins(-1, 0, -1, -1)
        self.hlEditVal.setObjectName(_fromUtf8("hlEditVal"))
        self.lEditVal = QtGui.QLabel(wgVtxEdit)
        self.lEditVal.setMinimumSize(QtCore.QSize(80, 0))
        self.lEditVal.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lEditVal.setObjectName(_fromUtf8("lEditVal"))
        self.hlEditVal.addWidget(self.lEditVal)
        self.sbEditVal = QtGui.QDoubleSpinBox(wgVtxEdit)
        self.sbEditVal.setInputMethodHints(QtCore.Qt.ImhNone)
        self.sbEditVal.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.sbEditVal.setDecimals(4)
        self.sbEditVal.setMinimum(-99.0)
        self.sbEditVal.setObjectName(_fromUtf8("sbEditVal"))
        self.hlEditVal.addWidget(self.sbEditVal)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlEditVal.addItem(spacerItem2)
        self.gridLayout.addLayout(self.hlEditVal, 6, 0, 1, 1)
        self.hlSelMode = QtGui.QHBoxLayout()
        self.hlSelMode.setContentsMargins(-1, 0, -1, -1)
        self.hlSelMode.setObjectName(_fromUtf8("hlSelMode"))
        self.lSelRange = QtGui.QLabel(wgVtxEdit)
        self.lSelRange.setMinimumSize(QtCore.QSize(0, 0))
        self.lSelRange.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lSelRange.setObjectName(_fromUtf8("lSelRange"))
        self.hlSelMode.addWidget(self.lSelRange)
        self.rbVtxRange = QtGui.QRadioButton(wgVtxEdit)
        self.rbVtxRange.setChecked(True)
        self.rbVtxRange.setObjectName(_fromUtf8("rbVtxRange"))
        self.bgVtxSelection = QtGui.QButtonGroup(wgVtxEdit)
        self.bgVtxSelection.setObjectName(_fromUtf8("bgVtxSelection"))
        self.bgVtxSelection.addButton(self.rbVtxRange)
        self.hlSelMode.addWidget(self.rbVtxRange)
        self.rbVtxValue = QtGui.QRadioButton(wgVtxEdit)
        self.rbVtxValue.setAutoExclusive(True)
        self.rbVtxValue.setObjectName(_fromUtf8("rbVtxValue"))
        self.bgVtxSelection.addButton(self.rbVtxValue)
        self.hlSelMode.addWidget(self.rbVtxValue)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlSelMode.addItem(spacerItem3)
        self.gridLayout.addLayout(self.hlSelMode, 0, 0, 1, 1)
        self.line_6 = QtGui.QFrame(wgVtxEdit)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout.addWidget(self.line_6, 10, 0, 1, 1)
        self.line_5 = QtGui.QFrame(wgVtxEdit)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout.addWidget(self.line_5, 3, 0, 1, 1)
        self.hlDataStorage = QtGui.QHBoxLayout()
        self.hlDataStorage.setSpacing(2)
        self.hlDataStorage.setObjectName(_fromUtf8("hlDataStorage"))
        self.lDataStorage = QtGui.QLabel(wgVtxEdit)
        self.lDataStorage.setMinimumSize(QtCore.QSize(70, 0))
        self.lDataStorage.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lDataStorage.setFont(font)
        self.lDataStorage.setObjectName(_fromUtf8("lDataStorage"))
        self.hlDataStorage.addWidget(self.lDataStorage)
        self.gridLayout.addLayout(self.hlDataStorage, 15, 0, 1, 1)
        self.hlEditMode = QtGui.QHBoxLayout()
        self.hlEditMode.setSpacing(2)
        self.hlEditMode.setContentsMargins(-1, 0, -1, -1)
        self.hlEditMode.setObjectName(_fromUtf8("hlEditMode"))
        self.lEditMode = QtGui.QLabel(wgVtxEdit)
        self.lEditMode.setMinimumSize(QtCore.QSize(80, 0))
        self.lEditMode.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lEditMode.setObjectName(_fromUtf8("lEditMode"))
        self.hlEditMode.addWidget(self.lEditMode)
        self.rbEditReplace = QtGui.QRadioButton(wgVtxEdit)
        self.rbEditReplace.setChecked(True)
        self.rbEditReplace.setAutoExclusive(True)
        self.rbEditReplace.setObjectName(_fromUtf8("rbEditReplace"))
        self.bgVtxEdition = QtGui.QButtonGroup(wgVtxEdit)
        self.bgVtxEdition.setObjectName(_fromUtf8("bgVtxEdition"))
        self.bgVtxEdition.addButton(self.rbEditReplace)
        self.hlEditMode.addWidget(self.rbEditReplace)
        self.rbEditAdd = QtGui.QRadioButton(wgVtxEdit)
        self.rbEditAdd.setAutoExclusive(True)
        self.rbEditAdd.setObjectName(_fromUtf8("rbEditAdd"))
        self.bgVtxEdition.addButton(self.rbEditAdd)
        self.hlEditMode.addWidget(self.rbEditAdd)
        self.rbEditMult = QtGui.QRadioButton(wgVtxEdit)
        self.rbEditMult.setAutoExclusive(True)
        self.rbEditMult.setObjectName(_fromUtf8("rbEditMult"))
        self.bgVtxEdition.addButton(self.rbEditMult)
        self.hlEditMode.addWidget(self.rbEditMult)
        self.gridLayout.addLayout(self.hlEditMode, 5, 0, 1, 1)
        self.hlSelRange = QtGui.QHBoxLayout()
        self.hlSelRange.setObjectName(_fromUtf8("hlSelRange"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlSelRange.addItem(spacerItem4)
        self.lRangeMin = QtGui.QLabel(wgVtxEdit)
        self.lRangeMin.setObjectName(_fromUtf8("lRangeMin"))
        self.hlSelRange.addWidget(self.lRangeMin)
        self.sbRangeMin = QtGui.QDoubleSpinBox(wgVtxEdit)
        self.sbRangeMin.setMinimumSize(QtCore.QSize(70, 0))
        self.sbRangeMin.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.sbRangeMin.setDecimals(4)
        self.sbRangeMin.setSingleStep(0.01)
        self.sbRangeMin.setObjectName(_fromUtf8("sbRangeMin"))
        self.hlSelRange.addWidget(self.sbRangeMin)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlSelRange.addItem(spacerItem5)
        self.lRangeMax = QtGui.QLabel(wgVtxEdit)
        self.lRangeMax.setObjectName(_fromUtf8("lRangeMax"))
        self.hlSelRange.addWidget(self.lRangeMax)
        self.sbRangeMax = QtGui.QDoubleSpinBox(wgVtxEdit)
        self.sbRangeMax.setMinimumSize(QtCore.QSize(70, 0))
        self.sbRangeMax.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.sbRangeMax.setDecimals(4)
        self.sbRangeMax.setProperty("value", 1.0)
        self.sbRangeMax.setObjectName(_fromUtf8("sbRangeMax"))
        self.hlSelRange.addWidget(self.sbRangeMax)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlSelRange.addItem(spacerItem6)
        self.gridLayout.addLayout(self.hlSelRange, 1, 0, 1, 1)
        self.hlVtxStorage = QtGui.QHBoxLayout()
        self.hlVtxStorage.setSpacing(2)
        self.hlVtxStorage.setObjectName(_fromUtf8("hlVtxStorage"))
        self.lVtxStorage = QtGui.QLabel(wgVtxEdit)
        self.lVtxStorage.setMinimumSize(QtCore.QSize(70, 0))
        self.lVtxStorage.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lVtxStorage.setFont(font)
        self.lVtxStorage.setObjectName(_fromUtf8("lVtxStorage"))
        self.hlVtxStorage.addWidget(self.lVtxStorage)
        self.gridLayout.addLayout(self.hlVtxStorage, 13, 0, 1, 1)
        self.line_7 = QtGui.QFrame(wgVtxEdit)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.gridLayout.addWidget(self.line_7, 16, 0, 1, 1)
        self.line_4 = QtGui.QFrame(wgVtxEdit)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 20, 0, 1, 1)
        self.line_8 = QtGui.QFrame(wgVtxEdit)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout.addWidget(self.line_8, 17, 0, 1, 1)
        self.tabFile = QtGui.QTabWidget(wgVtxEdit)
        self.tabFile.setObjectName(_fromUtf8("tabFile"))
        self.tiLoad = QtGui.QWidget()
        self.tiLoad.setObjectName(_fromUtf8("tiLoad"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tiLoad)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lImportTitle = QtGui.QLabel(self.tiLoad)
        self.lImportTitle.setMinimumSize(QtCore.QSize(0, 14))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lImportTitle.setFont(font)
        self.lImportTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lImportTitle.setObjectName(_fromUtf8("lImportTitle"))
        self.gridLayout_3.addWidget(self.lImportTitle, 0, 0, 1, 2)
        self.hlRootPath = QtGui.QHBoxLayout()
        self.hlRootPath.setSpacing(2)
        self.hlRootPath.setObjectName(_fromUtf8("hlRootPath"))
        self.lRootPath = QtGui.QLabel(self.tiLoad)
        self.lRootPath.setMinimumSize(QtCore.QSize(80, 0))
        self.lRootPath.setMaximumSize(QtCore.QSize(80, 20))
        self.lRootPath.setObjectName(_fromUtf8("lRootPath"))
        self.hlRootPath.addWidget(self.lRootPath)
        self.leRootPath = QtGui.QLineEdit(self.tiLoad)
        self.leRootPath.setObjectName(_fromUtf8("leRootPath"))
        self.hlRootPath.addWidget(self.leRootPath)
        self.pbSet = QtGui.QPushButton(self.tiLoad)
        self.pbSet.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbSet.setObjectName(_fromUtf8("pbSet"))
        self.hlRootPath.addWidget(self.pbSet)
        self.gridLayout_3.addLayout(self.hlRootPath, 1, 0, 2, 2)
        self.pushButton = QtGui.QPushButton(self.tiLoad)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_3.addWidget(self.pushButton, 3, 0, 1, 2)
        self.tabFile.addTab(self.tiLoad, _fromUtf8(""))
        self.tiSave = QtGui.QWidget()
        self.tiSave.setObjectName(_fromUtf8("tiSave"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tiSave)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lExportTitle = QtGui.QLabel(self.tiSave)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lExportTitle.setFont(font)
        self.lExportTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lExportTitle.setObjectName(_fromUtf8("lExportTitle"))
        self.gridLayout_2.addWidget(self.lExportTitle, 0, 0, 1, 1)
        self.hlExportPath = QtGui.QHBoxLayout()
        self.hlExportPath.setSpacing(2)
        self.hlExportPath.setObjectName(_fromUtf8("hlExportPath"))
        self.lExportPath = QtGui.QLabel(self.tiSave)
        self.lExportPath.setMinimumSize(QtCore.QSize(80, 0))
        self.lExportPath.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lExportPath.setObjectName(_fromUtf8("lExportPath"))
        self.hlExportPath.addWidget(self.lExportPath)
        self.leExportPath = QtGui.QLineEdit(self.tiSave)
        self.leExportPath.setObjectName(_fromUtf8("leExportPath"))
        self.hlExportPath.addWidget(self.leExportPath)
        self.pbOpen = QtGui.QPushButton(self.tiSave)
        self.pbOpen.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbOpen.setObjectName(_fromUtf8("pbOpen"))
        self.hlExportPath.addWidget(self.pbOpen)
        self.gridLayout_2.addLayout(self.hlExportPath, 1, 0, 1, 1)
        self.pbSave = QtGui.QPushButton(self.tiSave)
        self.pbSave.setObjectName(_fromUtf8("pbSave"))
        self.gridLayout_2.addWidget(self.pbSave, 2, 0, 1, 1)
        self.tabFile.addTab(self.tiSave, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabFile, 18, 0, 1, 1)

        self.retranslateUi(wgVtxEdit)
        self.tabFile.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(wgVtxEdit)

    def retranslateUi(self, wgVtxEdit):
        wgVtxEdit.setWindowTitle(_translate("wgVtxEdit", "VtxEdit", None))
        self.lClampVal.setText(_translate("wgVtxEdit", "Clamp Values:", None))
        self.cbClampMin.setText(_translate("wgVtxEdit", "Min", None))
        self.cbClampMax.setText(_translate("wgVtxEdit", "Max", None))
        self.pbFlood.setText(_translate("wgVtxEdit", "Flood", None))
        self.pbVtxSelect.setText(_translate("wgVtxEdit", "Select", None))
        self.pbVtxClear.setText(_translate("wgVtxEdit", "Clear", None))
        self.lEditVal.setText(_translate("wgVtxEdit", "Vertex Value:", None))
        self.lSelRange.setText(_translate("wgVtxEdit", "Vertex Selection: ", None))
        self.rbVtxRange.setText(_translate("wgVtxEdit", "Range", None))
        self.rbVtxValue.setText(_translate("wgVtxEdit", "Value", None))
        self.lDataStorage.setText(_translate("wgVtxEdit", "Data Storage:", None))
        self.lEditMode.setText(_translate("wgVtxEdit", "Vertex Edition:", None))
        self.rbEditReplace.setText(_translate("wgVtxEdit", "Replace", None))
        self.rbEditAdd.setText(_translate("wgVtxEdit", "Add", None))
        self.rbEditMult.setText(_translate("wgVtxEdit", "Multiply", None))
        self.lRangeMin.setText(_translate("wgVtxEdit", "Min=", None))
        self.lRangeMax.setText(_translate("wgVtxEdit", "Max=", None))
        self.lVtxStorage.setText(_translate("wgVtxEdit", "Vtx Storage:", None))
        self.lImportTitle.setText(_translate("wgVtxEdit", "Import Vertex Map", None))
        self.lRootPath.setText(_translate("wgVtxEdit", "Map Root Path:", None))
        self.pbSet.setText(_translate("wgVtxEdit", "Set", None))
        self.pushButton.setText(_translate("wgVtxEdit", "Load", None))
        self.tabFile.setTabText(self.tabFile.indexOf(self.tiLoad), _translate("wgVtxEdit", "Load", None))
        self.lExportTitle.setText(_translate("wgVtxEdit", "Export Vertex Map", None))
        self.lExportPath.setText(_translate("wgVtxEdit", "Vtx Map Path:", None))
        self.pbOpen.setText(_translate("wgVtxEdit", "Open", None))
        self.pbSave.setText(_translate("wgVtxEdit", "Save", None))
        self.tabFile.setTabText(self.tabFile.indexOf(self.tiSave), _translate("wgVtxEdit", "Save", None))

