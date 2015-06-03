# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothCache\ud\wgCacheList.ui'
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

class Ui_wgCacheList(object):
    def setupUi(self, wgCacheList):
        wgCacheList.setObjectName(_fromUtf8("wgCacheList"))
        wgCacheList.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(wgCacheList)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.twCaches = QtGui.QTreeWidget(wgCacheList)
        self.twCaches.setIndentation(2)
        self.twCaches.setObjectName(_fromUtf8("twCaches"))
        self.twCaches.headerItem().setText(0, _fromUtf8("1"))
        self.twCaches.header().setVisible(False)
        self.gridLayout.addWidget(self.twCaches, 0, 0, 1, 1)

        self.retranslateUi(wgCacheList)
        QtCore.QMetaObject.connectSlotsByName(wgCacheList)

    def retranslateUi(self, wgCacheList):
        wgCacheList.setWindowTitle(_translate("wgCacheList", "Cache List", None))

