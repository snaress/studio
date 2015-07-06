# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgDataNodeScript.ui'
#
# Created: Mon Jul 06 00:07:54 2015
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

class Ui_wgDataScript(object):
    def setupUi(self, wgDataScript):
        wgDataScript.setObjectName(_fromUtf8("wgDataScript"))
        wgDataScript.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(wgDataScript)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.qfScriptZone = QtGui.QFrame(wgDataScript)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qfScriptZone.sizePolicy().hasHeightForWidth())
        self.qfScriptZone.setSizePolicy(sizePolicy)
        self.qfScriptZone.setObjectName(_fromUtf8("qfScriptZone"))
        self.vlScriptZone = QtGui.QVBoxLayout(self.qfScriptZone)
        self.vlScriptZone.setSpacing(0)
        self.vlScriptZone.setMargin(0)
        self.vlScriptZone.setObjectName(_fromUtf8("vlScriptZone"))
        self.gridLayout.addWidget(self.qfScriptZone, 0, 0, 1, 1)
        self.hlButtons = QtGui.QHBoxLayout()
        self.hlButtons.setSpacing(0)
        self.hlButtons.setObjectName(_fromUtf8("hlButtons"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlButtons.addItem(spacerItem)
        self.pbSave = QtGui.QPushButton(wgDataScript)
        self.pbSave.setMinimumSize(QtCore.QSize(50, 20))
        self.pbSave.setMaximumSize(QtCore.QSize(50, 20))
        self.pbSave.setObjectName(_fromUtf8("pbSave"))
        self.hlButtons.addWidget(self.pbSave)
        self.pbCancel = QtGui.QPushButton(wgDataScript)
        self.pbCancel.setMinimumSize(QtCore.QSize(50, 20))
        self.pbCancel.setMaximumSize(QtCore.QSize(50, 20))
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.hlButtons.addWidget(self.pbCancel)
        self.gridLayout.addLayout(self.hlButtons, 1, 0, 1, 1)

        self.retranslateUi(wgDataScript)
        QtCore.QMetaObject.connectSlotsByName(wgDataScript)

    def retranslateUi(self, wgDataScript):
        wgDataScript.setWindowTitle(_translate("wgDataScript", "Script", None))
        self.pbSave.setText(_translate("wgDataScript", "Save", None))
        self.pbCancel.setText(_translate("wgDataScript", "Cancel", None))

