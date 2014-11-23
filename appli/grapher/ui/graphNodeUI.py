# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\ui\graphNode.ui'
#
# Created: Wed Nov 19 18:38:42 2014
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

class Ui_graphNode(object):
    def setupUi(self, graphNode):
        graphNode.setObjectName(_fromUtf8("graphNode"))
        graphNode.resize(387, 20)
        self.gridLayout = QtGui.QGridLayout(graphNode)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pbExecNode = QtGui.QPushButton(graphNode)
        self.pbExecNode.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pbExecNode.setFont(font)
        self.pbExecNode.setObjectName(_fromUtf8("pbExecNode"))
        self.gridLayout.addWidget(self.pbExecNode, 0, 3, 1, 1)
        self.lChildIndicator = QtGui.QLabel(graphNode)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lChildIndicator.sizePolicy().hasHeightForWidth())
        self.lChildIndicator.setSizePolicy(sizePolicy)
        self.lChildIndicator.setText(_fromUtf8(""))
        self.lChildIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.lChildIndicator.setObjectName(_fromUtf8("lChildIndicator"))
        self.gridLayout.addWidget(self.lChildIndicator, 0, 5, 1, 1)
        self.cbNode = QtGui.QCheckBox(graphNode)
        self.cbNode.setMaximumSize(QtCore.QSize(18, 20))
        self.cbNode.setAutoFillBackground(True)
        self.cbNode.setText(_fromUtf8(""))
        self.cbNode.setChecked(True)
        self.cbNode.setObjectName(_fromUtf8("cbNode"))
        self.gridLayout.addWidget(self.cbNode, 0, 1, 1, 1)
        self.pbExpand = QtGui.QPushButton(graphNode)
        self.pbExpand.setMaximumSize(QtCore.QSize(20, 20))
        self.pbExpand.setObjectName(_fromUtf8("pbExpand"))
        self.gridLayout.addWidget(self.pbExpand, 0, 0, 1, 1)
        self.pbNode = QtGui.QPushButton(graphNode)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbNode.sizePolicy().hasHeightForWidth())
        self.pbNode.setSizePolicy(sizePolicy)
        self.pbNode.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbNode.setObjectName(_fromUtf8("pbNode"))
        self.gridLayout.addWidget(self.pbNode, 0, 2, 1, 1)

        self.retranslateUi(graphNode)
        QtCore.QMetaObject.connectSlotsByName(graphNode)

    def retranslateUi(self, graphNode):
        graphNode.setWindowTitle(_translate("graphNode", "graphNode", None))
        self.pbExecNode.setText(_translate("graphNode", "Exec", None))
        self.pbExpand.setText(_translate("graphNode", "+", None))
        self.pbNode.setText(_translate("graphNode", "PushButton", None))

