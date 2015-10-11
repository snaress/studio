# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgLauncher.ui'
#
# Created: Sat Oct 10 13:51:41 2015
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
        wgLauncher.resize(691, 49)
        self.gridLayout = QtGui.QGridLayout(wgLauncher)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_4 = QtGui.QFrame(wgLauncher)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 8, 0, 1, 1)
        self.line = QtGui.QFrame(wgLauncher)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 0, 1, 1)
        self.vfLauncher = QtGui.QFrame(wgLauncher)
        self.vfLauncher.setFrameShape(QtGui.QFrame.StyledPanel)
        self.vfLauncher.setObjectName(_fromUtf8("vfLauncher"))
        self.vlLauncher = QtGui.QVBoxLayout(self.vfLauncher)
        self.vlLauncher.setSpacing(0)
        self.vlLauncher.setContentsMargins(0, 1, 0, 1)
        self.vlLauncher.setObjectName(_fromUtf8("vlLauncher"))
        self.hlLauncher = QtGui.QHBoxLayout()
        self.hlLauncher.setSpacing(0)
        self.hlLauncher.setContentsMargins(4, 0, 2, 0)
        self.hlLauncher.setObjectName(_fromUtf8("hlLauncher"))
        self.lLauncher = QtGui.QLabel(self.vfLauncher)
        self.lLauncher.setMinimumSize(QtCore.QSize(55, 0))
        self.lLauncher.setMaximumSize(QtCore.QSize(55, 16777215))
        self.lLauncher.setObjectName(_fromUtf8("lLauncher"))
        self.hlLauncher.addWidget(self.lLauncher)
        self.cbLauncher = QtGui.QComboBox(self.vfLauncher)
        self.cbLauncher.setMinimumSize(QtCore.QSize(150, 0))
        self.cbLauncher.setObjectName(_fromUtf8("cbLauncher"))
        self.hlLauncher.addWidget(self.cbLauncher)
        spacerItem = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hlLauncher.addItem(spacerItem)
        self.lLauncherArgs = QtGui.QLabel(self.vfLauncher)
        self.lLauncherArgs.setMinimumSize(QtCore.QSize(30, 0))
        self.lLauncherArgs.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lLauncherArgs.setObjectName(_fromUtf8("lLauncherArgs"))
        self.hlLauncher.addWidget(self.lLauncherArgs)
        self.leArgs = QtGui.QLineEdit(self.vfLauncher)
        self.leArgs.setEnabled(True)
        self.leArgs.setObjectName(_fromUtf8("leArgs"))
        self.hlLauncher.addWidget(self.leArgs)
        self.vlLauncher.addLayout(self.hlLauncher)
        self.gridLayout.addWidget(self.vfLauncher, 2, 0, 1, 1)
        self.vfExecMode = QtGui.QFrame(wgLauncher)
        self.vfExecMode.setObjectName(_fromUtf8("vfExecMode"))
        self.vlExecMode = QtGui.QVBoxLayout(self.vfExecMode)
        self.vlExecMode.setSpacing(0)
        self.vlExecMode.setMargin(0)
        self.vlExecMode.setObjectName(_fromUtf8("vlExecMode"))
        self.cbExecMode = QtGui.QCheckBox(self.vfExecMode)
        self.cbExecMode.setObjectName(_fromUtf8("cbExecMode"))
        self.vlExecMode.addWidget(self.cbExecMode)
        self.gridLayout.addWidget(self.vfExecMode, 1, 0, 1, 1)

        self.retranslateUi(wgLauncher)
        QtCore.QMetaObject.connectSlotsByName(wgLauncher)

    def retranslateUi(self, wgLauncher):
        wgLauncher.setWindowTitle(_translate("wgLauncher", "Launcher", None))
        self.lLauncher.setText(_translate("wgLauncher", "Launcher: ", None))
        self.lLauncherArgs.setText(_translate("wgLauncher", "Args: ", None))
        self.cbExecMode.setText(_translate("wgLauncher", "Exec Mode", None))

