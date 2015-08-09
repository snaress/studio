# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\dynEval\ud\wgInfoNode.ui'
#
# Created: Sun Aug 09 01:54:43 2015
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

class Ui_wgInfoNode(object):
    def setupUi(self, wgInfoNode):
        wgInfoNode.setObjectName(_fromUtf8("wgInfoNode"))
        wgInfoNode.resize(400, 21)
        self.gridLayout = QtGui.QGridLayout(wgInfoNode)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line = QtGui.QFrame(wgInfoNode)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(2, -1, 2, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.line_3 = QtGui.QFrame(wgInfoNode)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.label = QtGui.QLabel(wgInfoNode)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.line_4 = QtGui.QFrame(wgInfoNode)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout.addWidget(self.line_4)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.line_2 = QtGui.QFrame(wgInfoNode)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 1)

        self.retranslateUi(wgInfoNode)
        QtCore.QMetaObject.connectSlotsByName(wgInfoNode)

    def retranslateUi(self, wgInfoNode):
        wgInfoNode.setWindowTitle(_translate("wgInfoNode", "Info Node", None))
        self.label.setText(_translate("wgInfoNode", "TextLabel", None))

