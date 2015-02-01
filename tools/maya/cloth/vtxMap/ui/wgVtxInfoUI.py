# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\vtxMap\ui\wgVtxInfo.ui'
#
# Created: Sun Feb 01 03:51:45 2015
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

class Ui_wgVtxInfo(object):
    def setupUi(self, wgVtxInfo):
        wgVtxInfo.setObjectName(_fromUtf8("wgVtxInfo"))
        wgVtxInfo.resize(256, 217)
        self.gridLayout = QtGui.QGridLayout(wgVtxInfo)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pbUpdateInf = QtGui.QPushButton(wgVtxInfo)
        self.pbUpdateInf.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbUpdateInf.setObjectName(_fromUtf8("pbUpdateInf"))
        self.gridLayout.addWidget(self.pbUpdateInf, 0, 0, 1, 1)
        self.twVtxValues = QtGui.QTreeWidget(wgVtxInfo)
        self.twVtxValues.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.twVtxValues.setIndentation(0)
        self.twVtxValues.setObjectName(_fromUtf8("twVtxValues"))
        self.twVtxValues.header().setVisible(False)
        self.gridLayout.addWidget(self.twVtxValues, 1, 0, 1, 1)
        self.line_4 = QtGui.QFrame(wgVtxInfo)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 2, 0, 1, 1)

        self.retranslateUi(wgVtxInfo)
        QtCore.QMetaObject.connectSlotsByName(wgVtxInfo)

    def retranslateUi(self, wgVtxInfo):
        wgVtxInfo.setWindowTitle(_translate("wgVtxInfo", "VtxInfo", None))
        self.pbUpdateInf.setText(_translate("wgVtxInfo", "Update From Scene", None))
        self.twVtxValues.headerItem().setText(0, _translate("wgVtxInfo", "Index", None))
        self.twVtxValues.headerItem().setText(1, _translate("wgVtxInfo", "Influence", None))

