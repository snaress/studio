# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgLauncher.ui'
#
# Created: Wed Oct 07 02:10:59 2015
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

class Ui_wgLauncher(object):
    def setupUi(self, wgLauncher):
        wgLauncher.setObjectName(_fromUtf8("wgLauncher"))
        wgLauncher.resize(691, 52)
        self.gridLayout = QtGui.QGridLayout(wgLauncher)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_2 = QtGui.QFrame(wgLauncher)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 1)
        self.line_4 = QtGui.QFrame(wgLauncher)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 6, 0, 1, 1)
        self.line_3 = QtGui.QFrame(wgLauncher)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 1)
        self.line = QtGui.QFrame(wgLauncher)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 0, 1, 1)
        self.hlResult = QtGui.QHBoxLayout()
        self.hlResult.setSpacing(0)
        self.hlResult.setContentsMargins(4, -1, 2, -1)
        self.hlResult.setObjectName(_fromUtf8("hlResult"))
        self.lResult = QtGui.QLabel(wgLauncher)
        self.lResult.setMinimumSize(QtCore.QSize(55, 0))
        self.lResult.setMaximumSize(QtCore.QSize(55, 16777215))
        self.lResult.setObjectName(_fromUtf8("lResult"))
        self.hlResult.addWidget(self.lResult)
        self.lResultVal = QtGui.QLabel(wgLauncher)
        self.lResultVal.setEnabled(True)
        self.lResultVal.setAlignment(QtCore.Qt.AlignCenter)
        self.lResultVal.setObjectName(_fromUtf8("lResultVal"))
        self.hlResult.addWidget(self.lResultVal)
        self.gridLayout.addLayout(self.hlResult, 4, 0, 1, 1)
        self.hlLauncher = QtGui.QHBoxLayout()
        self.hlLauncher.setSpacing(0)
        self.hlLauncher.setContentsMargins(4, 0, 2, 0)
        self.hlLauncher.setObjectName(_fromUtf8("hlLauncher"))
        self.lLauncher = QtGui.QLabel(wgLauncher)
        self.lLauncher.setMinimumSize(QtCore.QSize(55, 0))
        self.lLauncher.setMaximumSize(QtCore.QSize(55, 16777215))
        self.lLauncher.setObjectName(_fromUtf8("lLauncher"))
        self.hlLauncher.addWidget(self.lLauncher)
        self.cbLauncher = QtGui.QComboBox(wgLauncher)
        self.cbLauncher.setMinimumSize(QtCore.QSize(150, 0))
        self.cbLauncher.setObjectName(_fromUtf8("cbLauncher"))
        self.hlLauncher.addWidget(self.cbLauncher)
        spacerItem = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hlLauncher.addItem(spacerItem)
        self.lLauncherArgs = QtGui.QLabel(wgLauncher)
        self.lLauncherArgs.setMinimumSize(QtCore.QSize(30, 0))
        self.lLauncherArgs.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lLauncherArgs.setObjectName(_fromUtf8("lLauncherArgs"))
        self.hlLauncher.addWidget(self.lLauncherArgs)
        self.leArgs = QtGui.QLineEdit(wgLauncher)
        self.leArgs.setEnabled(True)
        self.leArgs.setObjectName(_fromUtf8("leArgs"))
        self.hlLauncher.addWidget(self.leArgs)
        self.gridLayout.addLayout(self.hlLauncher, 2, 0, 1, 1)
        self.line_5 = QtGui.QFrame(wgLauncher)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout.addWidget(self.line_5, 3, 0, 1, 1)

        self.retranslateUi(wgLauncher)
        QtCore.QMetaObject.connectSlotsByName(wgLauncher)

    def retranslateUi(self, wgLauncher):
        wgLauncher.setWindowTitle(_translate("wgLauncher", "Launcher", None))
        self.lResult.setText(_translate("wgLauncher", "Result: ", None))
        self.lResultVal.setText(_translate("wgLauncher", "TextLabel", None))
        self.lLauncher.setText(_translate("wgLauncher", "Launcher: ", None))
        self.lLauncherArgs.setText(_translate("wgLauncher", "Args: ", None))

