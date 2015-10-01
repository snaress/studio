# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgLogs.ui'
#
# Created: Thu Oct 01 02:30:26 2015
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
        self.vlButtons = QtGui.QVBoxLayout()
        self.vlButtons.setSpacing(20)
        self.vlButtons.setObjectName(_fromUtf8("vlButtons"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlButtons.addItem(spacerItem)
        self.pbAutoRefresh = QtGui.QPushButton(wgLogs)
        self.pbAutoRefresh.setCheckable(True)
        self.pbAutoRefresh.setChecked(False)
        self.pbAutoRefresh.setAutoRepeat(True)
        self.pbAutoRefresh.setDefault(False)
        self.pbAutoRefresh.setFlat(False)
        self.pbAutoRefresh.setObjectName(_fromUtf8("pbAutoRefresh"))
        self.vlButtons.addWidget(self.pbAutoRefresh)
        self.pbDelJobs = QtGui.QPushButton(wgLogs)
        self.pbDelJobs.setObjectName(_fromUtf8("pbDelJobs"))
        self.vlButtons.addWidget(self.pbDelJobs)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlButtons.addItem(spacerItem1)
        self.gridLayout.addLayout(self.vlButtons, 0, 0, 1, 1)
        self.splitter = QtGui.QSplitter(wgLogs)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.twJobs = QtGui.QTreeWidget(self.splitter)
        self.twJobs.setObjectName(_fromUtf8("twJobs"))
        self.twJobs.headerItem().setText(0, _fromUtf8("1"))
        self.teLogs = QtGui.QPlainTextEdit(self.splitter)
        self.teLogs.setReadOnly(True)
        self.teLogs.setObjectName(_fromUtf8("teLogs"))
        self.gridLayout.addWidget(self.splitter, 0, 1, 1, 1)

        self.retranslateUi(wgLogs)
        QtCore.QMetaObject.connectSlotsByName(wgLogs)

    def retranslateUi(self, wgLogs):
        wgLogs.setWindowTitle(_translate("wgLogs", "Logs", None))
        self.pbAutoRefresh.setText(_translate("wgLogs", "Auto Refresh", None))
        self.pbDelJobs.setText(_translate("wgLogs", "Del Jobs", None))

