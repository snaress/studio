# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\dynEval\ud\wgCacheInfo.ui'
#
# Created: Sun Aug 02 21:23:12 2015
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

class Ui_wgCacheInfo(object):
    def setupUi(self, wgCacheInfo):
        wgCacheInfo.setObjectName(_fromUtf8("wgCacheInfo"))
        wgCacheInfo.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(wgCacheInfo)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabInfo = QtGui.QTabWidget(wgCacheInfo)
        self.tabInfo.setObjectName(_fromUtf8("tabInfo"))
        self.tabNotes = QtGui.QWidget()
        self.tabNotes.setObjectName(_fromUtf8("tabNotes"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabNotes)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pbEditNotes = QtGui.QPushButton(self.tabNotes)
        self.pbEditNotes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pbEditNotes.setFont(font)
        self.pbEditNotes.setIconSize(QtCore.QSize(24, 24))
        self.pbEditNotes.setObjectName(_fromUtf8("pbEditNotes"))
        self.gridLayout_2.addWidget(self.pbEditNotes, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(316, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.teNotes = QtGui.QTextEdit(self.tabNotes)
        self.teNotes.setObjectName(_fromUtf8("teNotes"))
        self.gridLayout_2.addWidget(self.teNotes, 0, 0, 1, 3)
        self.tabInfo.addTab(self.tabNotes, _fromUtf8(""))
        self.tabInfos = QtGui.QWidget()
        self.tabInfos.setObjectName(_fromUtf8("tabInfos"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tabInfos)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.teInfos = QtGui.QTextEdit(self.tabInfos)
        self.teInfos.setReadOnly(True)
        self.teInfos.setObjectName(_fromUtf8("teInfos"))
        self.gridLayout_3.addWidget(self.teInfos, 0, 0, 1, 1)
        self.tabInfo.addTab(self.tabInfos, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabInfo, 0, 0, 1, 1)

        self.retranslateUi(wgCacheInfo)
        self.tabInfo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wgCacheInfo)

    def retranslateUi(self, wgCacheInfo):
        wgCacheInfo.setWindowTitle(_translate("wgCacheInfo", "Cache Info", None))
        self.pbEditNotes.setText(_translate("wgCacheInfo", "Edit Notes", None))
        self.tabInfo.setTabText(self.tabInfo.indexOf(self.tabNotes), _translate("wgCacheInfo", "Notes", None))
        self.tabInfo.setTabText(self.tabInfo.indexOf(self.tabInfos), _translate("wgCacheInfo", "Infos", None))

