# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\vtxMap\ui\wgVtxMap.ui'
#
# Created: Sat Jan 24 16:18:14 2015
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

class Ui_wgVtxMap(object):
    def setupUi(self, wgVtxMap):
        wgVtxMap.setObjectName(_fromUtf8("wgVtxMap"))
        wgVtxMap.resize(477, 28)
        self.gridLayout = QtGui.QGridLayout(wgVtxMap)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line = QtGui.QFrame(wgVtxMap)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 0, 1, 1)
        self.hlVtxMap = QtGui.QHBoxLayout()
        self.hlVtxMap.setSpacing(0)
        self.hlVtxMap.setContentsMargins(2, 0, 2, 0)
        self.hlVtxMap.setObjectName(_fromUtf8("hlVtxMap"))
        self.lVtxMap = QtGui.QLabel(wgVtxMap)
        self.lVtxMap.setObjectName(_fromUtf8("lVtxMap"))
        self.hlVtxMap.addWidget(self.lVtxMap)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlVtxMap.addItem(spacerItem)
        self.cbState = QtGui.QComboBox(wgVtxMap)
        self.cbState.setObjectName(_fromUtf8("cbState"))
        self.cbState.addItem(_fromUtf8(""))
        self.cbState.addItem(_fromUtf8(""))
        self.cbState.addItem(_fromUtf8(""))
        self.hlVtxMap.addWidget(self.cbState)
        self.gridLayout.addLayout(self.hlVtxMap, 1, 0, 1, 1)
        self.line_2 = QtGui.QFrame(wgVtxMap)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 1)

        self.retranslateUi(wgVtxMap)
        QtCore.QMetaObject.connectSlotsByName(wgVtxMap)

    def retranslateUi(self, wgVtxMap):
        wgVtxMap.setWindowTitle(_translate("wgVtxMap", "VtxMapNode", None))
        self.lVtxMap.setText(_translate("wgVtxMap", "TextLabel", None))
        self.cbState.setItemText(0, _translate("wgVtxMap", "None", None))
        self.cbState.setItemText(1, _translate("wgVtxMap", "Vertex", None))
        self.cbState.setItemText(2, _translate("wgVtxMap", "Texture", None))

