# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothEditor\ui\wgVtxMapNode.ui'
#
# Created: Sun Mar 29 04:44:49 2015
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

class Ui_wgVtxMapNode(object):
    def setupUi(self, wgVtxMapNode):
        wgVtxMapNode.setObjectName(_fromUtf8("wgVtxMapNode"))
        wgVtxMapNode.resize(477, 28)
        self.gridLayout = QtGui.QGridLayout(wgVtxMapNode)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line = QtGui.QFrame(wgVtxMapNode)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 0, 1, 1)
        self.hlVtxMapNode = QtGui.QHBoxLayout()
        self.hlVtxMapNode.setSpacing(0)
        self.hlVtxMapNode.setContentsMargins(2, 0, 2, 0)
        self.hlVtxMapNode.setObjectName(_fromUtf8("hlVtxMapNode"))
        self.lVtxMap = QtGui.QLabel(wgVtxMapNode)
        self.lVtxMap.setObjectName(_fromUtf8("lVtxMap"))
        self.hlVtxMapNode.addWidget(self.lVtxMap)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlVtxMapNode.addItem(spacerItem)
        self.cbState = QtGui.QComboBox(wgVtxMapNode)
        self.cbState.setObjectName(_fromUtf8("cbState"))
        self.cbState.addItem(_fromUtf8(""))
        self.cbState.addItem(_fromUtf8(""))
        self.cbState.addItem(_fromUtf8(""))
        self.hlVtxMapNode.addWidget(self.cbState)
        self.gridLayout.addLayout(self.hlVtxMapNode, 1, 0, 1, 1)
        self.line_2 = QtGui.QFrame(wgVtxMapNode)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 1)

        self.retranslateUi(wgVtxMapNode)
        QtCore.QMetaObject.connectSlotsByName(wgVtxMapNode)

    def retranslateUi(self, wgVtxMapNode):
        wgVtxMapNode.setWindowTitle(_translate("wgVtxMapNode", "VtxMapNode", None))
        self.lVtxMap.setText(_translate("wgVtxMapNode", "TextLabel", None))
        self.cbState.setItemText(0, _translate("wgVtxMapNode", "None", None))
        self.cbState.setItemText(1, _translate("wgVtxMapNode", "Vertex", None))
        self.cbState.setItemText(2, _translate("wgVtxMapNode", "Texture", None))

