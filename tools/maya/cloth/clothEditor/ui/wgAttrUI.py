# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothEditor\ui\wgAttr.ui'
#
# Created: Fri Apr 03 01:39:32 2015
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
        wgPreset.resize(191, 300)
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
        self.vlPreset.setMargin(0)
        self.vlPreset.setObjectName(_fromUtf8("vlPreset"))
        self.twPreset = QtGui.QTreeWidget(self.verticalLayoutWidget)
        self.twPreset.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.twPreset.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.twPreset.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
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
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.vlTools.addItem(spacerItem)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(wgPreset)
        QtCore.QMetaObject.connectSlotsByName(wgPreset)

    def retranslateUi(self, wgPreset):
        wgPreset.setWindowTitle(_translate("wgPreset", "Preset", None))

