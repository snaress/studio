# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothEditor\ud\wgVtxMap.ui'
#
# Created: Sat May 23 20:28:03 2015
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

class Ui_wgVtxMap(object):
    def setupUi(self, wgVtxMap):
        wgVtxMap.setObjectName(_fromUtf8("wgVtxMap"))
        wgVtxMap.resize(546, 399)
        self.gridLayout_3 = QtGui.QGridLayout(wgVtxMap)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.splitter = QtGui.QSplitter(wgVtxMap)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.vlVtxMaps = QtGui.QVBoxLayout(self.layoutWidget)
        self.vlVtxMaps.setSpacing(0)
        self.vlVtxMaps.setContentsMargins(-1, 0, -1, 0)
        self.vlVtxMaps.setObjectName(_fromUtf8("vlVtxMaps"))
        self.twMaps = QtGui.QTreeWidget(self.layoutWidget)
        self.twMaps.setMinimumSize(QtCore.QSize(220, 0))
        self.twMaps.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.twMaps.setIndentation(0)
        self.twMaps.setItemsExpandable(False)
        self.twMaps.setExpandsOnDoubleClick(False)
        self.twMaps.setColumnCount(1)
        self.twMaps.setObjectName(_fromUtf8("twMaps"))
        self.twMaps.header().setVisible(False)
        self.vlVtxMaps.addWidget(self.twMaps)
        self.line_2 = QtGui.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.vlVtxMaps.addWidget(self.line_2)
        self.hlEditAll = QtGui.QHBoxLayout()
        self.hlEditAll.setSpacing(1)
        self.hlEditAll.setContentsMargins(-1, -1, -1, 0)
        self.hlEditAll.setObjectName(_fromUtf8("hlEditAll"))
        self.lEditType = QtGui.QLabel(self.layoutWidget)
        self.lEditType.setObjectName(_fromUtf8("lEditType"))
        self.hlEditAll.addWidget(self.lEditType)
        self.pbNone = QtGui.QPushButton(self.layoutWidget)
        self.pbNone.setMaximumSize(QtCore.QSize(50, 20))
        self.pbNone.setObjectName(_fromUtf8("pbNone"))
        self.hlEditAll.addWidget(self.pbNone)
        self.pbVertex = QtGui.QPushButton(self.layoutWidget)
        self.pbVertex.setMaximumSize(QtCore.QSize(50, 20))
        self.pbVertex.setObjectName(_fromUtf8("pbVertex"))
        self.hlEditAll.addWidget(self.pbVertex)
        self.pbTexture = QtGui.QPushButton(self.layoutWidget)
        self.pbTexture.setMaximumSize(QtCore.QSize(50, 20))
        self.pbTexture.setObjectName(_fromUtf8("pbTexture"))
        self.hlEditAll.addWidget(self.pbTexture)
        self.vlVtxMaps.addLayout(self.hlEditAll)
        self.tabVertex = QtGui.QTabWidget(self.splitter)
        self.tabVertex.setObjectName(_fromUtf8("tabVertex"))
        self.tabVtxTools = QtGui.QWidget()
        self.tabVtxTools.setObjectName(_fromUtf8("tabVtxTools"))
        self.gridLayout = QtGui.QGridLayout(self.tabVtxTools)
        self.gridLayout.setContentsMargins(1, 0, 1, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hlArtSmooth = QtGui.QHBoxLayout()
        self.hlArtSmooth.setSpacing(2)
        self.hlArtSmooth.setContentsMargins(-1, 0, -1, 0)
        self.hlArtSmooth.setObjectName(_fromUtf8("hlArtSmooth"))
        self.pbArtSmooth1 = QtGui.QPushButton(self.tabVtxTools)
        self.pbArtSmooth1.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbArtSmooth1.setObjectName(_fromUtf8("pbArtSmooth1"))
        self.hlArtSmooth.addWidget(self.pbArtSmooth1)
        self.pbArtSmooth2 = QtGui.QPushButton(self.tabVtxTools)
        self.pbArtSmooth2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbArtSmooth2.setObjectName(_fromUtf8("pbArtSmooth2"))
        self.hlArtSmooth.addWidget(self.pbArtSmooth2)
        self.pbArtSmooth3 = QtGui.QPushButton(self.tabVtxTools)
        self.pbArtSmooth3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbArtSmooth3.setObjectName(_fromUtf8("pbArtSmooth3"))
        self.hlArtSmooth.addWidget(self.pbArtSmooth3)
        self.pbArtSmooth4 = QtGui.QPushButton(self.tabVtxTools)
        self.pbArtSmooth4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbArtSmooth4.setObjectName(_fromUtf8("pbArtSmooth4"))
        self.hlArtSmooth.addWidget(self.pbArtSmooth4)
        self.pbArtSmooth5 = QtGui.QPushButton(self.tabVtxTools)
        self.pbArtSmooth5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbArtSmooth5.setObjectName(_fromUtf8("pbArtSmooth5"))
        self.hlArtSmooth.addWidget(self.pbArtSmooth5)
        self.gridLayout.addLayout(self.hlArtSmooth, 14, 0, 1, 1)
        self.line_13 = QtGui.QFrame(self.tabVtxTools)
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.gridLayout.addWidget(self.line_13, 18, 0, 1, 1)
        self.line_5 = QtGui.QFrame(self.tabVtxTools)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout.addWidget(self.line_5, 4, 0, 1, 1)
        self.hlClampVal = QtGui.QHBoxLayout()
        self.hlClampVal.setSpacing(2)
        self.hlClampVal.setContentsMargins(-1, 0, -1, -1)
        self.hlClampVal.setObjectName(_fromUtf8("hlClampVal"))
        self.lClampVal = QtGui.QLabel(self.tabVtxTools)
        self.lClampVal.setMinimumSize(QtCore.QSize(80, 0))
        self.lClampVal.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lClampVal.setObjectName(_fromUtf8("lClampVal"))
        self.hlClampVal.addWidget(self.lClampVal)
        self.cbClampMin = QtGui.QCheckBox(self.tabVtxTools)
        self.cbClampMin.setMinimumSize(QtCore.QSize(40, 0))
        self.cbClampMin.setMaximumSize(QtCore.QSize(40, 16777215))
        self.cbClampMin.setChecked(True)
        self.cbClampMin.setObjectName(_fromUtf8("cbClampMin"))
        self.hlClampVal.addWidget(self.cbClampMin)
        self.leClampMin = QtGui.QLineEdit(self.tabVtxTools)
        self.leClampMin.setMaximumSize(QtCore.QSize(70, 16777215))
        self.leClampMin.setAlignment(QtCore.Qt.AlignCenter)
        self.leClampMin.setObjectName(_fromUtf8("leClampMin"))
        self.hlClampVal.addWidget(self.leClampMin)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlClampVal.addItem(spacerItem)
        self.cbClampMax = QtGui.QCheckBox(self.tabVtxTools)
        self.cbClampMax.setMinimumSize(QtCore.QSize(40, 0))
        self.cbClampMax.setMaximumSize(QtCore.QSize(40, 16777215))
        self.cbClampMax.setChecked(True)
        self.cbClampMax.setObjectName(_fromUtf8("cbClampMax"))
        self.hlClampVal.addWidget(self.cbClampMax)
        self.leClampMax = QtGui.QLineEdit(self.tabVtxTools)
        self.leClampMax.setMaximumSize(QtCore.QSize(70, 16777215))
        self.leClampMax.setAlignment(QtCore.Qt.AlignCenter)
        self.leClampMax.setObjectName(_fromUtf8("leClampMax"))
        self.hlClampVal.addWidget(self.leClampMax)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlClampVal.addItem(spacerItem1)
        self.gridLayout.addLayout(self.hlClampVal, 9, 0, 1, 1)
        self.hlEditVal = QtGui.QHBoxLayout()
        self.hlEditVal.setSpacing(2)
        self.hlEditVal.setContentsMargins(-1, 0, -1, -1)
        self.hlEditVal.setObjectName(_fromUtf8("hlEditVal"))
        self.lEditVal = QtGui.QLabel(self.tabVtxTools)
        self.lEditVal.setMinimumSize(QtCore.QSize(80, 0))
        self.lEditVal.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lEditVal.setObjectName(_fromUtf8("lEditVal"))
        self.hlEditVal.addWidget(self.lEditVal)
        self.leEditVal = QtGui.QLineEdit(self.tabVtxTools)
        self.leEditVal.setMaximumSize(QtCore.QSize(70, 16777215))
        self.leEditVal.setAlignment(QtCore.Qt.AlignCenter)
        self.leEditVal.setObjectName(_fromUtf8("leEditVal"))
        self.hlEditVal.addWidget(self.leEditVal)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlEditVal.addItem(spacerItem2)
        self.gridLayout.addLayout(self.hlEditVal, 8, 0, 1, 1)
        self.hlDataStorage = QtGui.QHBoxLayout()
        self.hlDataStorage.setSpacing(2)
        self.hlDataStorage.setObjectName(_fromUtf8("hlDataStorage"))
        self.lDataStorage = QtGui.QLabel(self.tabVtxTools)
        self.lDataStorage.setMinimumSize(QtCore.QSize(70, 0))
        self.lDataStorage.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lDataStorage.setFont(font)
        self.lDataStorage.setObjectName(_fromUtf8("lDataStorage"))
        self.hlDataStorage.addWidget(self.lDataStorage)
        self.gridLayout.addLayout(self.hlDataStorage, 21, 0, 1, 1)
        self.line = QtGui.QFrame(self.tabVtxTools)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 5, 0, 1, 1)
        self.line_4 = QtGui.QFrame(self.tabVtxTools)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 20, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.tabVtxTools)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 12, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 152, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 24, 0, 1, 1)
        self.hlVtxStorage = QtGui.QHBoxLayout()
        self.hlVtxStorage.setSpacing(2)
        self.hlVtxStorage.setObjectName(_fromUtf8("hlVtxStorage"))
        self.lVtxStorage = QtGui.QLabel(self.tabVtxTools)
        self.lVtxStorage.setMinimumSize(QtCore.QSize(70, 0))
        self.lVtxStorage.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lVtxStorage.setFont(font)
        self.lVtxStorage.setObjectName(_fromUtf8("lVtxStorage"))
        self.hlVtxStorage.addWidget(self.lVtxStorage)
        self.gridLayout.addLayout(self.hlVtxStorage, 19, 0, 1, 1)
        self.hlFlood = QtGui.QHBoxLayout()
        self.hlFlood.setObjectName(_fromUtf8("hlFlood"))
        self.pbFlood = QtGui.QPushButton(self.tabVtxTools)
        self.pbFlood.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbFlood.setObjectName(_fromUtf8("pbFlood"))
        self.hlFlood.addWidget(self.pbFlood)
        self.lFloodIter = QtGui.QLabel(self.tabVtxTools)
        self.lFloodIter.setMaximumSize(QtCore.QSize(20, 16777215))
        self.lFloodIter.setAlignment(QtCore.Qt.AlignCenter)
        self.lFloodIter.setObjectName(_fromUtf8("lFloodIter"))
        self.hlFlood.addWidget(self.lFloodIter)
        self.sbFloodIter = QtGui.QSpinBox(self.tabVtxTools)
        self.sbFloodIter.setMaximumSize(QtCore.QSize(30, 16777215))
        self.sbFloodIter.setAlignment(QtCore.Qt.AlignCenter)
        self.sbFloodIter.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.sbFloodIter.setMinimum(1)
        self.sbFloodIter.setMaximum(25)
        self.sbFloodIter.setProperty("value", 1)
        self.sbFloodIter.setObjectName(_fromUtf8("sbFloodIter"))
        self.hlFlood.addWidget(self.sbFloodIter)
        self.gridLayout.addLayout(self.hlFlood, 10, 0, 1, 1)
        self.lVtxFlood = QtGui.QLabel(self.tabVtxTools)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lVtxFlood.setFont(font)
        self.lVtxFlood.setAlignment(QtCore.Qt.AlignCenter)
        self.lVtxFlood.setObjectName(_fromUtf8("lVtxFlood"))
        self.gridLayout.addWidget(self.lVtxFlood, 6, 0, 1, 1)
        self.line_10 = QtGui.QFrame(self.tabVtxTools)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.gridLayout.addWidget(self.line_10, 23, 0, 1, 1)
        self.hlEditMode = QtGui.QHBoxLayout()
        self.hlEditMode.setSpacing(2)
        self.hlEditMode.setContentsMargins(-1, 0, -1, -1)
        self.hlEditMode.setObjectName(_fromUtf8("hlEditMode"))
        self.lEditMode = QtGui.QLabel(self.tabVtxTools)
        self.lEditMode.setMinimumSize(QtCore.QSize(80, 0))
        self.lEditMode.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lEditMode.setObjectName(_fromUtf8("lEditMode"))
        self.hlEditMode.addWidget(self.lEditMode)
        self.rbEditReplace = QtGui.QRadioButton(self.tabVtxTools)
        self.rbEditReplace.setChecked(True)
        self.rbEditReplace.setAutoExclusive(True)
        self.rbEditReplace.setObjectName(_fromUtf8("rbEditReplace"))
        self.bgVtxEdition = QtGui.QButtonGroup(wgVtxMap)
        self.bgVtxEdition.setObjectName(_fromUtf8("bgVtxEdition"))
        self.bgVtxEdition.addButton(self.rbEditReplace)
        self.hlEditMode.addWidget(self.rbEditReplace)
        self.rbEditAdd = QtGui.QRadioButton(self.tabVtxTools)
        self.rbEditAdd.setAutoExclusive(True)
        self.rbEditAdd.setObjectName(_fromUtf8("rbEditAdd"))
        self.bgVtxEdition.addButton(self.rbEditAdd)
        self.hlEditMode.addWidget(self.rbEditAdd)
        self.rbEditMult = QtGui.QRadioButton(self.tabVtxTools)
        self.rbEditMult.setAutoExclusive(True)
        self.rbEditMult.setObjectName(_fromUtf8("rbEditMult"))
        self.bgVtxEdition.addButton(self.rbEditMult)
        self.hlEditMode.addWidget(self.rbEditMult)
        self.rbEditSmooth = QtGui.QRadioButton(self.tabVtxTools)
        self.rbEditSmooth.setEnabled(True)
        self.rbEditSmooth.setObjectName(_fromUtf8("rbEditSmooth"))
        self.bgVtxEdition.addButton(self.rbEditSmooth)
        self.hlEditMode.addWidget(self.rbEditSmooth)
        self.gridLayout.addLayout(self.hlEditMode, 7, 0, 1, 1)
        self.hlSelMode = QtGui.QHBoxLayout()
        self.hlSelMode.setContentsMargins(-1, 0, -1, -1)
        self.hlSelMode.setObjectName(_fromUtf8("hlSelMode"))
        self.lSelRange = QtGui.QLabel(self.tabVtxTools)
        self.lSelRange.setMinimumSize(QtCore.QSize(0, 0))
        self.lSelRange.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lSelRange.setObjectName(_fromUtf8("lSelRange"))
        self.hlSelMode.addWidget(self.lSelRange)
        self.rbVtxRange = QtGui.QRadioButton(self.tabVtxTools)
        self.rbVtxRange.setChecked(True)
        self.rbVtxRange.setObjectName(_fromUtf8("rbVtxRange"))
        self.bgVtxSelMode = QtGui.QButtonGroup(wgVtxMap)
        self.bgVtxSelMode.setObjectName(_fromUtf8("bgVtxSelMode"))
        self.bgVtxSelMode.addButton(self.rbVtxRange)
        self.hlSelMode.addWidget(self.rbVtxRange)
        self.rbVtxValue = QtGui.QRadioButton(self.tabVtxTools)
        self.rbVtxValue.setAutoExclusive(True)
        self.rbVtxValue.setObjectName(_fromUtf8("rbVtxValue"))
        self.bgVtxSelMode.addButton(self.rbVtxValue)
        self.hlSelMode.addWidget(self.rbVtxValue)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlSelMode.addItem(spacerItem4)
        self.gridLayout.addLayout(self.hlSelMode, 2, 0, 1, 1)
        self.hlSelRange = QtGui.QHBoxLayout()
        self.hlSelRange.setObjectName(_fromUtf8("hlSelRange"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlSelRange.addItem(spacerItem5)
        self.lRangeMin = QtGui.QLabel(self.tabVtxTools)
        self.lRangeMin.setObjectName(_fromUtf8("lRangeMin"))
        self.hlSelRange.addWidget(self.lRangeMin)
        self.leRangeMin = QtGui.QLineEdit(self.tabVtxTools)
        self.leRangeMin.setMaximumSize(QtCore.QSize(70, 16777215))
        self.leRangeMin.setInputMethodHints(QtCore.Qt.ImhNone)
        self.leRangeMin.setAlignment(QtCore.Qt.AlignCenter)
        self.leRangeMin.setObjectName(_fromUtf8("leRangeMin"))
        self.hlSelRange.addWidget(self.leRangeMin)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlSelRange.addItem(spacerItem6)
        self.lRangeMax = QtGui.QLabel(self.tabVtxTools)
        self.lRangeMax.setObjectName(_fromUtf8("lRangeMax"))
        self.hlSelRange.addWidget(self.lRangeMax)
        self.leRangeMax = QtGui.QLineEdit(self.tabVtxTools)
        self.leRangeMax.setMaximumSize(QtCore.QSize(70, 16777215))
        self.leRangeMax.setAlignment(QtCore.Qt.AlignCenter)
        self.leRangeMax.setObjectName(_fromUtf8("leRangeMax"))
        self.hlSelRange.addWidget(self.leRangeMax)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlSelRange.addItem(spacerItem7)
        self.pbVtxSelect = QtGui.QPushButton(self.tabVtxTools)
        self.pbVtxSelect.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbVtxSelect.setObjectName(_fromUtf8("pbVtxSelect"))
        self.hlSelRange.addWidget(self.pbVtxSelect)
        self.gridLayout.addLayout(self.hlSelRange, 3, 0, 1, 1)
        self.line_6 = QtGui.QFrame(self.tabVtxTools)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout.addWidget(self.line_6, 11, 0, 1, 1)
        self.lVtxStor = QtGui.QLabel(self.tabVtxTools)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lVtxStor.setFont(font)
        self.lVtxStor.setAlignment(QtCore.Qt.AlignCenter)
        self.lVtxStor.setObjectName(_fromUtf8("lVtxStor"))
        self.gridLayout.addWidget(self.lVtxStor, 17, 0, 1, 1)
        self.lVtxSel = QtGui.QLabel(self.tabVtxTools)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lVtxSel.setFont(font)
        self.lVtxSel.setAlignment(QtCore.Qt.AlignCenter)
        self.lVtxSel.setObjectName(_fromUtf8("lVtxSel"))
        self.gridLayout.addWidget(self.lVtxSel, 1, 0, 1, 1)
        self.line_9 = QtGui.QFrame(self.tabVtxTools)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.gridLayout.addWidget(self.line_9, 22, 0, 1, 1)
        self.label = QtGui.QLabel(self.tabVtxTools)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 13, 0, 1, 1)
        self.line_15 = QtGui.QFrame(self.tabVtxTools)
        self.line_15.setFrameShape(QtGui.QFrame.HLine)
        self.line_15.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_15.setObjectName(_fromUtf8("line_15"))
        self.gridLayout.addWidget(self.line_15, 16, 0, 1, 1)
        self.line_14 = QtGui.QFrame(self.tabVtxTools)
        self.line_14.setFrameShape(QtGui.QFrame.HLine)
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.gridLayout.addWidget(self.line_14, 15, 0, 1, 1)
        self.line_8 = QtGui.QFrame(self.tabVtxTools)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout.addWidget(self.line_8, 0, 0, 1, 1)
        self.tabVertex.addTab(self.tabVtxTools, _fromUtf8(""))
        self.tabVtxValues = QtGui.QWidget()
        self.tabVtxValues.setObjectName(_fromUtf8("tabVtxValues"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabVtxValues)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.twVtxValues = QtGui.QTreeWidget(self.tabVtxValues)
        self.twVtxValues.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.twVtxValues.setIndentation(0)
        self.twVtxValues.setObjectName(_fromUtf8("twVtxValues"))
        self.twVtxValues.header().setVisible(False)
        self.gridLayout_2.addWidget(self.twVtxValues, 2, 0, 1, 1)
        self.pbUpdateInf = QtGui.QPushButton(self.tabVtxValues)
        self.pbUpdateInf.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbUpdateInf.setObjectName(_fromUtf8("pbUpdateInf"))
        self.gridLayout_2.addWidget(self.pbUpdateInf, 0, 0, 1, 1)
        self.line_7 = QtGui.QFrame(self.tabVtxValues)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.gridLayout_2.addWidget(self.line_7, 1, 0, 1, 1)
        self.tabVertex.addTab(self.tabVtxValues, _fromUtf8(""))
        self.tabVtxFiles = QtGui.QWidget()
        self.tabVtxFiles.setObjectName(_fromUtf8("tabVtxFiles"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tabVtxFiles)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.vlVtxFiles = QtGui.QVBoxLayout()
        self.vlVtxFiles.setObjectName(_fromUtf8("vlVtxFiles"))
        self.gridLayout_4.addLayout(self.vlVtxFiles, 0, 0, 1, 1)
        self.tabVertex.addTab(self.tabVtxFiles, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(wgVtxMap)
        self.tabVertex.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wgVtxMap)

    def retranslateUi(self, wgVtxMap):
        wgVtxMap.setWindowTitle(_translate("wgVtxMap", "Vertex Map", None))
        self.twMaps.headerItem().setText(0, _translate("wgVtxMap", "Vertex Map Type", None))
        self.lEditType.setText(_translate("wgVtxMap", "Set All To:", None))
        self.pbNone.setText(_translate("wgVtxMap", "None", None))
        self.pbVertex.setText(_translate("wgVtxMap", "Vertex", None))
        self.pbTexture.setText(_translate("wgVtxMap", "Texture", None))
        self.pbArtSmooth1.setText(_translate("wgVtxMap", "x 5", None))
        self.pbArtSmooth2.setText(_translate("wgVtxMap", "x 10", None))
        self.pbArtSmooth3.setText(_translate("wgVtxMap", "x 15", None))
        self.pbArtSmooth4.setText(_translate("wgVtxMap", "x 20", None))
        self.pbArtSmooth5.setText(_translate("wgVtxMap", "x 25", None))
        self.lClampVal.setText(_translate("wgVtxMap", "Clamp Values:", None))
        self.cbClampMin.setText(_translate("wgVtxMap", "Min", None))
        self.leClampMin.setText(_translate("wgVtxMap", "0.0", None))
        self.cbClampMax.setText(_translate("wgVtxMap", "Max", None))
        self.leClampMax.setText(_translate("wgVtxMap", "1.0", None))
        self.lEditVal.setText(_translate("wgVtxMap", "Vertex Value:", None))
        self.leEditVal.setText(_translate("wgVtxMap", "0.0", None))
        self.lDataStorage.setText(_translate("wgVtxMap", "Data Storage:", None))
        self.lVtxStorage.setText(_translate("wgVtxMap", "Vtx Storage:", None))
        self.pbFlood.setText(_translate("wgVtxMap", "Flood", None))
        self.lFloodIter.setText(_translate("wgVtxMap", "X", None))
        self.lVtxFlood.setText(_translate("wgVtxMap", "Vertex Flood", None))
        self.lEditMode.setText(_translate("wgVtxMap", "Vertex Edition:", None))
        self.rbEditReplace.setText(_translate("wgVtxMap", "Replace", None))
        self.rbEditAdd.setText(_translate("wgVtxMap", "Add", None))
        self.rbEditMult.setText(_translate("wgVtxMap", "Multiply", None))
        self.rbEditSmooth.setText(_translate("wgVtxMap", "Smooth", None))
        self.lSelRange.setText(_translate("wgVtxMap", "Selection Mode: ", None))
        self.rbVtxRange.setText(_translate("wgVtxMap", "Range", None))
        self.rbVtxValue.setText(_translate("wgVtxMap", "Value", None))
        self.lRangeMin.setText(_translate("wgVtxMap", "Min=", None))
        self.leRangeMin.setText(_translate("wgVtxMap", "0.0", None))
        self.lRangeMax.setText(_translate("wgVtxMap", "Max=", None))
        self.leRangeMax.setText(_translate("wgVtxMap", "1.0", None))
        self.pbVtxSelect.setText(_translate("wgVtxMap", "Select", None))
        self.lVtxStor.setText(_translate("wgVtxMap", "Vertex Storage", None))
        self.lVtxSel.setText(_translate("wgVtxMap", "Vertex Selection", None))
        self.label.setText(_translate("wgVtxMap", "Artisan Flood Smooth", None))
        self.tabVertex.setTabText(self.tabVertex.indexOf(self.tabVtxTools), _translate("wgVtxMap", "Vtx Tools", None))
        self.twVtxValues.headerItem().setText(0, _translate("wgVtxMap", "Index", None))
        self.twVtxValues.headerItem().setText(1, _translate("wgVtxMap", "Influence", None))
        self.pbUpdateInf.setText(_translate("wgVtxMap", "Update Selection From Scene", None))
        self.tabVertex.setTabText(self.tabVertex.indexOf(self.tabVtxValues), _translate("wgVtxMap", "Vtx Values", None))
        self.tabVertex.setTabText(self.tabVertex.indexOf(self.tabVtxFiles), _translate("wgVtxMap", "Vtx Files", None))

