# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgDataPlugItem.ui'
#
# Created: Sat Jul 18 00:55:45 2015
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

class Ui_wgDataPlugItem(object):
    def setupUi(self, wgDataPlugItem):
        wgDataPlugItem.setObjectName(_fromUtf8("wgDataPlugItem"))
        wgDataPlugItem.resize(400, 45)
        self.gridLayout = QtGui.QGridLayout(wgDataPlugItem)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hlPlug = QtGui.QHBoxLayout()
        self.hlPlug.setSpacing(0)
        self.hlPlug.setObjectName(_fromUtf8("hlPlug"))
        self.line_4 = QtGui.QFrame(wgDataPlugItem)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.hlPlug.addWidget(self.line_4)
        self.lIndex = QtGui.QLabel(wgDataPlugItem)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lIndex.sizePolicy().hasHeightForWidth())
        self.lIndex.setSizePolicy(sizePolicy)
        self.lIndex.setMinimumSize(QtCore.QSize(30, 20))
        self.lIndex.setMaximumSize(QtCore.QSize(30, 20))
        self.lIndex.setAlignment(QtCore.Qt.AlignCenter)
        self.lIndex.setObjectName(_fromUtf8("lIndex"))
        self.hlPlug.addWidget(self.lIndex)
        self.line = QtGui.QFrame(wgDataPlugItem)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.hlPlug.addWidget(self.line)
        self.lConnectedNode = QtGui.QLabel(wgDataPlugItem)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lConnectedNode.sizePolicy().hasHeightForWidth())
        self.lConnectedNode.setSizePolicy(sizePolicy)
        self.lConnectedNode.setObjectName(_fromUtf8("lConnectedNode"))
        self.hlPlug.addWidget(self.lConnectedNode)
        self.line_3 = QtGui.QFrame(wgDataPlugItem)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.hlPlug.addWidget(self.line_3)
        self.pbEnable = QtGui.QPushButton(wgDataPlugItem)
        self.pbEnable.setMinimumSize(QtCore.QSize(20, 0))
        self.pbEnable.setMaximumSize(QtCore.QSize(20, 16777215))
        self.pbEnable.setText(_fromUtf8(""))
        self.pbEnable.setCheckable(True)
        self.pbEnable.setChecked(True)
        self.pbEnable.setFlat(True)
        self.pbEnable.setObjectName(_fromUtf8("pbEnable"))
        self.hlPlug.addWidget(self.pbEnable)
        self.line_2 = QtGui.QFrame(wgDataPlugItem)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.hlPlug.addWidget(self.line_2)
        self.gridLayout.addLayout(self.hlPlug, 0, 0, 1, 1)
        self.qfInputFile = QtGui.QFrame(wgDataPlugItem)
        self.qfInputFile.setObjectName(_fromUtf8("qfInputFile"))
        self.hlInputFile = QtGui.QHBoxLayout(self.qfInputFile)
        self.hlInputFile.setSpacing(0)
        self.hlInputFile.setMargin(0)
        self.hlInputFile.setObjectName(_fromUtf8("hlInputFile"))
        self.comboBox = QtGui.QComboBox(self.qfInputFile)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.hlInputFile.addWidget(self.comboBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlInputFile.addItem(spacerItem)
        self.gridLayout.addWidget(self.qfInputFile, 1, 0, 1, 1)

        self.retranslateUi(wgDataPlugItem)
        QtCore.QMetaObject.connectSlotsByName(wgDataPlugItem)

    def retranslateUi(self, wgDataPlugItem):
        wgDataPlugItem.setWindowTitle(_translate("wgDataPlugItem", "Plug Item", None))
        self.lIndex.setText(_translate("wgDataPlugItem", "Ind", None))
        self.lConnectedNode.setText(_translate("wgDataPlugItem", "Connected Node", None))

