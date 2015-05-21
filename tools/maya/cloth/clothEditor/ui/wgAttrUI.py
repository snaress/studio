# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothEditor\ud\wgAttr.ui'
#
# Created: Thu May 21 22:31:59 2015
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

class Ui_wgPreset(object):
    def setupUi(self, wgPreset):
        wgPreset.setObjectName(_fromUtf8("wgPreset"))
        wgPreset.resize(527, 300)
        self.gridLayout = QtGui.QGridLayout(wgPreset)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(wgPreset)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.verticalLayoutWidget = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.vlPreset = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vlPreset.setSpacing(0)
        self.vlPreset.setContentsMargins(-1, -1, -1, 0)
        self.vlPreset.setObjectName(_fromUtf8("vlPreset"))
        self.twPreset = QtGui.QTreeWidget(self.verticalLayoutWidget)
        self.twPreset.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.twPreset.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.twPreset.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.twPreset.setIndentation(12)
        self.twPreset.setColumnCount(1)
        self.twPreset.setObjectName(_fromUtf8("twPreset"))
        self.twPreset.headerItem().setText(0, _fromUtf8("1"))
        self.twPreset.header().setVisible(False)
        self.vlPreset.addWidget(self.twPreset)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.vlTools = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vlTools.setSpacing(0)
        self.vlTools.setContentsMargins(0, -1, 0, -1)
        self.vlTools.setObjectName(_fromUtf8("vlTools"))
        self.tabAttr = QtGui.QTabWidget(self.verticalLayoutWidget_2)
        self.tabAttr.setObjectName(_fromUtf8("tabAttr"))
        self.tabAttrTools = QtGui.QWidget()
        self.tabAttrTools.setObjectName(_fromUtf8("tabAttrTools"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabAttrTools)
        self.gridLayout_2.setContentsMargins(1, 0, 1, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.line = QtGui.QFrame(self.tabAttrTools)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.lVtxStor = QtGui.QLabel(self.tabAttrTools)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lVtxStor.setFont(font)
        self.lVtxStor.setAlignment(QtCore.Qt.AlignCenter)
        self.lVtxStor.setObjectName(_fromUtf8("lVtxStor"))
        self.gridLayout_2.addWidget(self.lVtxStor, 0, 0, 1, 1)
        self.hlAttrStorage = QtGui.QHBoxLayout()
        self.hlAttrStorage.setSpacing(2)
        self.hlAttrStorage.setContentsMargins(-1, 0, -1, 0)
        self.hlAttrStorage.setObjectName(_fromUtf8("hlAttrStorage"))
        self.lAttrStorage = QtGui.QLabel(self.tabAttrTools)
        self.lAttrStorage.setMinimumSize(QtCore.QSize(70, 0))
        self.lAttrStorage.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lAttrStorage.setFont(font)
        self.lAttrStorage.setObjectName(_fromUtf8("lAttrStorage"))
        self.hlAttrStorage.addWidget(self.lAttrStorage)
        self.gridLayout_2.addLayout(self.hlAttrStorage, 2, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.tabAttrTools)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 3, 0, 1, 1)
        self.tabAttr.addTab(self.tabAttrTools, _fromUtf8(""))
        self.tabAttrFiles = QtGui.QWidget()
        self.tabAttrFiles.setObjectName(_fromUtf8("tabAttrFiles"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tabAttrFiles)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.vlAttrFiles = QtGui.QVBoxLayout()
        self.vlAttrFiles.setSpacing(0)
        self.vlAttrFiles.setObjectName(_fromUtf8("vlAttrFiles"))
        self.gridLayout_3.addLayout(self.vlAttrFiles, 0, 0, 1, 1)
        self.tabAttr.addTab(self.tabAttrFiles, _fromUtf8(""))
        self.vlTools.addWidget(self.tabAttr)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(wgPreset)
        self.tabAttr.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wgPreset)

    def retranslateUi(self, wgPreset):
        wgPreset.setWindowTitle(_translate("wgPreset", "Preset", None))
        self.lVtxStor.setText(_translate("wgPreset", "Preset Storage", None))
        self.lAttrStorage.setText(_translate("wgPreset", "Attr Storage:", None))
        self.tabAttr.setTabText(self.tabAttr.indexOf(self.tabAttrTools), _translate("wgPreset", "Attr Tools", None))
        self.tabAttr.setTabText(self.tabAttr.indexOf(self.tabAttrFiles), _translate("wgPreset", "Attr Files", None))

