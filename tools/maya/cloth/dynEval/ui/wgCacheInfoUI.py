# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothCache\ud\wgCacheInfo.ui'
#
# Created: Sat May 23 15:54:49 2015
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
        self.tabInfo.addTab(self.tabNotes, _fromUtf8(""))
        self.tabInfos = QtGui.QWidget()
        self.tabInfos.setObjectName(_fromUtf8("tabInfos"))
        self.tabInfo.addTab(self.tabInfos, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabInfo, 0, 0, 1, 1)

        self.retranslateUi(wgCacheInfo)
        self.tabInfo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wgCacheInfo)

    def retranslateUi(self, wgCacheInfo):
        wgCacheInfo.setWindowTitle(_translate("wgCacheInfo", "Cache Info", None))
        self.tabInfo.setTabText(self.tabInfo.indexOf(self.tabNotes), _translate("wgCacheInfo", "Notes", None))
        self.tabInfo.setTabText(self.tabInfo.indexOf(self.tabInfos), _translate("wgCacheInfo", "Infos", None))

