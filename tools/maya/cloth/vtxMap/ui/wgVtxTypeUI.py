# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\vtxMap\ui\wgVtxType.ui'
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

class Ui_wgVtxType(object):
    def setupUi(self, wgVtxType):
        wgVtxType.setObjectName(_fromUtf8("wgVtxType"))
        wgVtxType.resize(256, 219)
        self.gridLayout = QtGui.QGridLayout(wgVtxType)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.twMapType = QtGui.QTreeWidget(wgVtxType)
        self.twMapType.setMinimumSize(QtCore.QSize(0, 0))
        self.twMapType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.twMapType.setIndentation(0)
        self.twMapType.setItemsExpandable(False)
        self.twMapType.setExpandsOnDoubleClick(False)
        self.twMapType.setColumnCount(1)
        self.twMapType.setObjectName(_fromUtf8("twMapType"))
        self.twMapType.header().setVisible(False)
        self.gridLayout.addWidget(self.twMapType, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(wgVtxType)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)
        self.hlEditType = QtGui.QHBoxLayout()
        self.hlEditType.setSpacing(2)
        self.hlEditType.setContentsMargins(-1, -1, -1, 0)
        self.hlEditType.setObjectName(_fromUtf8("hlEditType"))
        self.lEditType = QtGui.QLabel(wgVtxType)
        self.lEditType.setObjectName(_fromUtf8("lEditType"))
        self.hlEditType.addWidget(self.lEditType)
        self.pbNone = QtGui.QPushButton(wgVtxType)
        self.pbNone.setMaximumSize(QtCore.QSize(50, 20))
        self.pbNone.setObjectName(_fromUtf8("pbNone"))
        self.hlEditType.addWidget(self.pbNone)
        self.pbVertex = QtGui.QPushButton(wgVtxType)
        self.pbVertex.setMaximumSize(QtCore.QSize(50, 20))
        self.pbVertex.setObjectName(_fromUtf8("pbVertex"))
        self.hlEditType.addWidget(self.pbVertex)
        self.pbTexture = QtGui.QPushButton(wgVtxType)
        self.pbTexture.setMaximumSize(QtCore.QSize(50, 20))
        self.pbTexture.setObjectName(_fromUtf8("pbTexture"))
        self.hlEditType.addWidget(self.pbTexture)
        self.gridLayout.addLayout(self.hlEditType, 2, 0, 1, 1)

        self.retranslateUi(wgVtxType)
        QtCore.QMetaObject.connectSlotsByName(wgVtxType)

    def retranslateUi(self, wgVtxType):
        wgVtxType.setWindowTitle(_translate("wgVtxType", "VtxType", None))
        self.twMapType.headerItem().setText(0, _translate("wgVtxType", "Vertex Map Type", None))
        self.lEditType.setText(_translate("wgVtxType", "Set All To:", None))
        self.pbNone.setText(_translate("wgVtxType", "None", None))
        self.pbVertex.setText(_translate("wgVtxType", "Vertex", None))
        self.pbTexture.setText(_translate("wgVtxType", "Texture", None))

