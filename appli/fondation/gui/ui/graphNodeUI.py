# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\fondation\gui\src\graphNode.ui'
#
# Created: Thu Aug 13 02:46:45 2015
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

class Ui_wgGraphNode(object):
    def setupUi(self, wgGraphNode):
        wgGraphNode.setObjectName(_fromUtf8("wgGraphNode"))
        wgGraphNode.resize(212, 28)
        self.gridLayout = QtGui.QGridLayout(wgGraphNode)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_5 = QtGui.QFrame(wgGraphNode)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout.addWidget(self.line_5, 0, 0, 1, 1)
        self.line_6 = QtGui.QFrame(wgGraphNode)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout.addWidget(self.line_6, 2, 0, 1, 1)
        self.hlNode = QtGui.QHBoxLayout()
        self.hlNode.setSpacing(0)
        self.hlNode.setObjectName(_fromUtf8("hlNode"))
        self.line = QtGui.QFrame(wgGraphNode)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.hlNode.addWidget(self.line)
        self.pbEnable = QtGui.QPushButton(wgGraphNode)
        self.pbEnable.setMinimumSize(QtCore.QSize(16, 16))
        self.pbEnable.setMaximumSize(QtCore.QSize(16, 16))
        self.pbEnable.setText(_fromUtf8(""))
        self.pbEnable.setCheckable(True)
        self.pbEnable.setChecked(True)
        self.pbEnable.setFlat(True)
        self.pbEnable.setObjectName(_fromUtf8("pbEnable"))
        self.hlNode.addWidget(self.pbEnable)
        self.line_7 = QtGui.QFrame(wgGraphNode)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.hlNode.addWidget(self.line_7)
        self.label = QtGui.QLabel(wgGraphNode)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.hlNode.addWidget(self.label)
        self.lNodeName = QtGui.QLabel(wgGraphNode)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lNodeName.sizePolicy().hasHeightForWidth())
        self.lNodeName.setSizePolicy(sizePolicy)
        self.lNodeName.setMinimumSize(QtCore.QSize(0, 20))
        self.lNodeName.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lNodeName.setFont(font)
        self.lNodeName.setAlignment(QtCore.Qt.AlignCenter)
        self.lNodeName.setMargin(0)
        self.lNodeName.setIndent(-1)
        self.lNodeName.setObjectName(_fromUtf8("lNodeName"))
        self.hlNode.addWidget(self.lNodeName)
        self.label_2 = QtGui.QLabel(wgGraphNode)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.hlNode.addWidget(self.label_2)
        self.line_4 = QtGui.QFrame(wgGraphNode)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.hlNode.addWidget(self.line_4)
        self.pbExpand = QtGui.QPushButton(wgGraphNode)
        self.pbExpand.setMinimumSize(QtCore.QSize(16, 16))
        self.pbExpand.setMaximumSize(QtCore.QSize(16, 16))
        self.pbExpand.setText(_fromUtf8(""))
        self.pbExpand.setCheckable(True)
        self.pbExpand.setChecked(False)
        self.pbExpand.setFlat(False)
        self.pbExpand.setObjectName(_fromUtf8("pbExpand"))
        self.hlNode.addWidget(self.pbExpand)
        self.line_2 = QtGui.QFrame(wgGraphNode)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.hlNode.addWidget(self.line_2)
        self.gridLayout.addLayout(self.hlNode, 1, 0, 1, 1)

        self.retranslateUi(wgGraphNode)
        QtCore.QMetaObject.connectSlotsByName(wgGraphNode)

    def retranslateUi(self, wgGraphNode):
        wgGraphNode.setWindowTitle(_translate("wgGraphNode", "Graph Node", None))
        self.lNodeName.setText(_translate("wgGraphNode", "None", None))

