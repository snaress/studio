# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgDataNodeId.ui'
#
# Created: Thu Jul 09 22:48:05 2015
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

class Ui_wgNodeId(object):
    def setupUi(self, wgNodeId):
        wgNodeId.setObjectName(_fromUtf8("wgNodeId"))
        wgNodeId.resize(330, 69)
        self.glNodeId = QtGui.QGridLayout(wgNodeId)
        self.glNodeId.setSpacing(0)
        self.glNodeId.setContentsMargins(2, 0, 2, 0)
        self.glNodeId.setObjectName(_fromUtf8("glNodeId"))
        self.hlNodeType = QtGui.QHBoxLayout()
        self.hlNodeType.setSpacing(6)
        self.hlNodeType.setObjectName(_fromUtf8("hlNodeType"))
        self.lNodeType = QtGui.QLabel(wgNodeId)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lNodeType.sizePolicy().hasHeightForWidth())
        self.lNodeType.setSizePolicy(sizePolicy)
        self.lNodeType.setMinimumSize(QtCore.QSize(65, 0))
        self.lNodeType.setMaximumSize(QtCore.QSize(65, 16777215))
        self.lNodeType.setObjectName(_fromUtf8("lNodeType"))
        self.hlNodeType.addWidget(self.lNodeType)
        self.leNodeType = QtGui.QLineEdit(wgNodeId)
        self.leNodeType.setText(_fromUtf8(""))
        self.leNodeType.setFrame(True)
        self.leNodeType.setReadOnly(True)
        self.leNodeType.setObjectName(_fromUtf8("leNodeType"))
        self.hlNodeType.addWidget(self.leNodeType)
        self.glNodeId.addLayout(self.hlNodeType, 0, 0, 1, 1)
        self.hlNodeName = QtGui.QHBoxLayout()
        self.hlNodeName.setSpacing(6)
        self.hlNodeName.setObjectName(_fromUtf8("hlNodeName"))
        self.lNodeName = QtGui.QLabel(wgNodeId)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lNodeName.sizePolicy().hasHeightForWidth())
        self.lNodeName.setSizePolicy(sizePolicy)
        self.lNodeName.setMinimumSize(QtCore.QSize(65, 0))
        self.lNodeName.setMaximumSize(QtCore.QSize(65, 16777215))
        self.lNodeName.setObjectName(_fromUtf8("lNodeName"))
        self.hlNodeName.addWidget(self.lNodeName)
        self.leNodeName = QtGui.QLineEdit(wgNodeId)
        self.leNodeName.setFrame(True)
        self.leNodeName.setReadOnly(True)
        self.leNodeName.setObjectName(_fromUtf8("leNodeName"))
        self.hlNodeName.addWidget(self.leNodeName)
        self.glNodeId.addLayout(self.hlNodeName, 1, 0, 1, 1)
        self.hlNodeId = QtGui.QHBoxLayout()
        self.hlNodeId.setSpacing(6)
        self.hlNodeId.setObjectName(_fromUtf8("hlNodeId"))
        self.lNodeId = QtGui.QLabel(wgNodeId)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lNodeId.sizePolicy().hasHeightForWidth())
        self.lNodeId.setSizePolicy(sizePolicy)
        self.lNodeId.setMinimumSize(QtCore.QSize(65, 0))
        self.lNodeId.setMaximumSize(QtCore.QSize(65, 16777215))
        self.lNodeId.setObjectName(_fromUtf8("lNodeId"))
        self.hlNodeId.addWidget(self.lNodeId)
        self.leNodeId = QtGui.QLineEdit(wgNodeId)
        self.leNodeId.setFrame(True)
        self.leNodeId.setReadOnly(True)
        self.leNodeId.setObjectName(_fromUtf8("leNodeId"))
        self.hlNodeId.addWidget(self.leNodeId)
        self.glNodeId.addLayout(self.hlNodeId, 2, 0, 1, 1)
        self.line = QtGui.QFrame(wgNodeId)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.glNodeId.addWidget(self.line, 3, 0, 1, 1)

        self.retranslateUi(wgNodeId)
        QtCore.QMetaObject.connectSlotsByName(wgNodeId)

    def retranslateUi(self, wgNodeId):
        wgNodeId.setWindowTitle(_translate("wgNodeId", "Node Id", None))
        self.lNodeType.setText(_translate("wgNodeId", "Node Type: ", None))
        self.lNodeName.setText(_translate("wgNodeId", "Node Name: ", None))
        self.lNodeId.setText(_translate("wgNodeId", "Node Id: ", None))

