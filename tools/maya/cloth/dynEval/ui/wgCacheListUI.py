# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\dynEval\ud\wgCacheList.ui'
#
# Created: Sun Aug 02 21:24:54 2015
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
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.twCaches = QtGui.QTreeWidget(wgCacheList)
        self.twCaches.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.twCaches.setIndentation(2)
        self.twCaches.setObjectName(_fromUtf8("twCaches"))
        self.twCaches.headerItem().setText(0, _fromUtf8("1"))
        self.twCaches.header().setVisible(False)
        self.gridLayout.addWidget(self.twCaches, 1, 0, 1, 1)
        self.hlCachePath = QtGui.QHBoxLayout()
        self.hlCachePath.setSpacing(2)
        self.hlCachePath.setContentsMargins(2, 0, 2, -1)
        self.hlCachePath.setObjectName(_fromUtf8("hlCachePath"))
        self.lCachePath = QtGui.QLabel(wgCacheList)
        self.lCachePath.setObjectName(_fromUtf8("lCachePath"))
        self.hlCachePath.addWidget(self.lCachePath)
        self.leCachePath = QtGui.QLineEdit(wgCacheList)
        self.leCachePath.setEnabled(False)
        self.leCachePath.setObjectName(_fromUtf8("leCachePath"))
        self.hlCachePath.addWidget(self.leCachePath)
        self.gridLayout.addLayout(self.hlCachePath, 0, 0, 1, 1)
        self.hlVersionOnly = QtGui.QHBoxLayout()
        self.hlVersionOnly.setContentsMargins(2, -1, 2, 0)
        self.hlVersionOnly.setObjectName(_fromUtf8("hlVersionOnly"))
        self.lVersion = QtGui.QLabel(wgCacheList)
        self.lVersion.setMinimumSize(QtCore.QSize(0, 20))
        self.lVersion.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lVersion.setFont(font)
        self.lVersion.setObjectName(_fromUtf8("lVersion"))
        self.hlVersionOnly.addWidget(self.lVersion)
        self.cbVersionOnly = QtGui.QCheckBox(wgCacheList)
        self.cbVersionOnly.setChecked(True)
        self.cbVersionOnly.setObjectName(_fromUtf8("cbVersionOnly"))
        self.hlVersionOnly.addWidget(self.cbVersionOnly)
        self.gridLayout.addLayout(self.hlVersionOnly, 2, 0, 1, 1)

        self.retranslateUi(wgCacheList)
        QtCore.QMetaObject.connectSlotsByName(wgCacheList)

    def retranslateUi(self, wgCacheList):
        wgCacheList.setWindowTitle(_translate("wgCacheList", "Cache List", None))
        self.lCachePath.setText(_translate("wgCacheList", "Cache Path: ", None))
        self.lVersion.setText(_translate("wgCacheList", "Show: ", None))
        self.cbVersionOnly.setText(_translate("wgCacheList", "Version Only", None))

