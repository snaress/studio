# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgLogs.ui'
#
# Created: Sat Oct 03 01:46:09 2015
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
        self.vlButtons.setSpacing(2)
        self.vlButtons.setObjectName(_fromUtf8("vlButtons"))
        self.pbGetJobs = QtGui.QPushButton(wgLogs)
        self.pbGetJobs.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbGetJobs.setCheckable(False)
        self.pbGetJobs.setAutoRepeat(False)
        self.pbGetJobs.setObjectName(_fromUtf8("pbGetJobs"))
        self.vlButtons.addWidget(self.pbGetJobs)
        self.pbDelJobs = QtGui.QPushButton(wgLogs)
        self.pbDelJobs.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbDelJobs.setObjectName(_fromUtf8("pbDelJobs"))
        self.vlButtons.addWidget(self.pbDelJobs)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlButtons.addItem(spacerItem)
        self.cbShowXterm = QtGui.QCheckBox(wgLogs)
        self.cbShowXterm.setObjectName(_fromUtf8("cbShowXterm"))
        self.vlButtons.addWidget(self.cbShowXterm)
        self.cbWaitAtEnd = QtGui.QCheckBox(wgLogs)
        self.cbWaitAtEnd.setObjectName(_fromUtf8("cbWaitAtEnd"))
        self.vlButtons.addWidget(self.cbWaitAtEnd)
        self.gridLayout.addLayout(self.vlButtons, 0, 0, 1, 1)
        self.splitter = QtGui.QSplitter(wgLogs)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.twJobs = QtGui.QTreeWidget(self.splitter)
        self.twJobs.setAlternatingRowColors(True)
        self.twJobs.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.twJobs.setIndentation(2)
        self.twJobs.setItemsExpandable(False)
        self.twJobs.setExpandsOnDoubleClick(False)
        self.twJobs.setObjectName(_fromUtf8("twJobs"))
        self.twJobs.headerItem().setText(0, _fromUtf8("Jobs"))
        self.twJobs.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.teLogs = QtGui.QPlainTextEdit(self.splitter)
        self.teLogs.setReadOnly(True)
        self.teLogs.setObjectName(_fromUtf8("teLogs"))
        self.gridLayout.addWidget(self.splitter, 0, 1, 1, 1)

        self.retranslateUi(wgLogs)
        QtCore.QMetaObject.connectSlotsByName(wgLogs)

    def retranslateUi(self, wgLogs):
        wgLogs.setWindowTitle(_translate("wgLogs", "Logs", None))
        self.pbGetJobs.setText(_translate("wgLogs", "Get Jobs", None))
        self.pbDelJobs.setText(_translate("wgLogs", "Del Jobs", None))
        self.cbShowXterm.setText(_translate("wgLogs", "Show Xterm", None))
        self.cbWaitAtEnd.setText(_translate("wgLogs", "Wait At End", None))

