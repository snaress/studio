# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgDataConnItem.ui'
#
# Created: Sat Jun 20 21:24:08 2015
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

class Ui_wgDataConnItem(object):
    def setupUi(self, wgDataConnItem):
        wgDataConnItem.setObjectName(_fromUtf8("wgDataConnItem"))
        wgDataConnItem.resize(380, 20)
        self.gridLayout = QtGui.QGridLayout(wgDataConnItem)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_2 = QtGui.QFrame(wgDataConnItem)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 0, 3, 1, 1)
        self.line = QtGui.QFrame(wgDataConnItem)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)
        self.lConnectedNode = QtGui.QLabel(wgDataConnItem)
        self.lConnectedNode.setObjectName(_fromUtf8("lConnectedNode"))
        self.gridLayout.addWidget(self.lConnectedNode, 0, 2, 1, 1)
        self.lIndex = QtGui.QLabel(wgDataConnItem)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lIndex.sizePolicy().hasHeightForWidth())
        self.lIndex.setSizePolicy(sizePolicy)
        self.lIndex.setMinimumSize(QtCore.QSize(30, 20))
        self.lIndex.setMaximumSize(QtCore.QSize(30, 20))
        self.lIndex.setAlignment(QtCore.Qt.AlignCenter)
        self.lIndex.setObjectName(_fromUtf8("lIndex"))
        self.gridLayout.addWidget(self.lIndex, 0, 0, 1, 1)

        self.retranslateUi(wgDataConnItem)
        QtCore.QMetaObject.connectSlotsByName(wgDataConnItem)

    def retranslateUi(self, wgDataConnItem):
        wgDataConnItem.setWindowTitle(_translate("wgDataConnItem", "Connection Item", None))
        self.lConnectedNode.setText(_translate("wgDataConnItem", "Connected Node", None))
        self.lIndex.setText(_translate("wgDataConnItem", "Ind", None))
