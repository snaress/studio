# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgScript.ui'
#
# Created: Sun Sep 27 03:26:11 2015
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

class Ui_wgScript(object):
    def setupUi(self, wgScript):
        wgScript.setObjectName(_fromUtf8("wgScript"))
        wgScript.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(wgScript)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hlButtons = QtGui.QHBoxLayout()
        self.hlButtons.setSpacing(0)
        self.hlButtons.setContentsMargins(2, -1, -1, -1)
        self.hlButtons.setObjectName(_fromUtf8("hlButtons"))
        self.label = QtGui.QLabel(wgScript)
        self.label.setObjectName(_fromUtf8("label"))
        self.hlButtons.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 12, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlButtons.addItem(spacerItem)
        self.pbPush = QtGui.QPushButton(wgScript)
        self.pbPush.setMinimumSize(QtCore.QSize(20, 20))
        self.pbPush.setMaximumSize(QtCore.QSize(20, 20))
        self.pbPush.setText(_fromUtf8(""))
        self.pbPush.setObjectName(_fromUtf8("pbPush"))
        self.hlButtons.addWidget(self.pbPush)
        self.pbPull = QtGui.QPushButton(wgScript)
        self.pbPull.setMinimumSize(QtCore.QSize(20, 20))
        self.pbPull.setMaximumSize(QtCore.QSize(20, 20))
        self.pbPull.setText(_fromUtf8(""))
        self.pbPull.setObjectName(_fromUtf8("pbPull"))
        self.hlButtons.addWidget(self.pbPull)
        self.gridLayout.addLayout(self.hlButtons, 0, 0, 1, 1)
        self.line = QtGui.QFrame(wgScript)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.vfScript = QtGui.QFrame(wgScript)
        self.vfScript.setFrameShape(QtGui.QFrame.StyledPanel)
        self.vfScript.setObjectName(_fromUtf8("vfScript"))
        self.vlScript = QtGui.QVBoxLayout(self.vfScript)
        self.vlScript.setSpacing(0)
        self.vlScript.setMargin(0)
        self.vlScript.setObjectName(_fromUtf8("vlScript"))
        self.gridLayout.addWidget(self.vfScript, 2, 0, 1, 1)

        self.retranslateUi(wgScript)
        QtCore.QMetaObject.connectSlotsByName(wgScript)

    def retranslateUi(self, wgScript):
        wgScript.setWindowTitle(_translate("wgScript", "ScriptEditor", None))
        self.label.setText(_translate("wgScript", "Script", None))

