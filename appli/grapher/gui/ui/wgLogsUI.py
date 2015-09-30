# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgLogs.ui'
#
# Created: Wed Sep 30 01:35:39 2015
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

class Ui_wgLogs(object):
    def setupUi(self, wgLogs):
        wgLogs.setObjectName(_fromUtf8("wgLogs"))
        wgLogs.resize(557, 300)
        self.gridLayout = QtGui.QGridLayout(wgLogs)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(wgLogs)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.twJobs = QtGui.QTreeWidget(self.splitter)
        self.twJobs.setObjectName(_fromUtf8("twJobs"))
        self.twJobs.headerItem().setText(0, _fromUtf8("1"))
        self.teLogs = QtGui.QPlainTextEdit(self.splitter)
        self.teLogs.setReadOnly(True)
        self.teLogs.setObjectName(_fromUtf8("teLogs"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(wgLogs)
        QtCore.QMetaObject.connectSlotsByName(wgLogs)

    def retranslateUi(self, wgLogs):
        wgLogs.setWindowTitle(_translate("wgLogs", "Logs", None))

