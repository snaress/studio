# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\dynEval\ud\wgCacheEval.ui'
#
# Created: Fri Jul 31 20:45:38 2015
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

class Ui_wgCacheEval(object):
    def setupUi(self, wgCacheEval):
        wgCacheEval.setObjectName(_fromUtf8("wgCacheEval"))
        wgCacheEval.resize(250, 150)
        wgCacheEval.setMinimumSize(QtCore.QSize(0, 0))
        wgCacheEval.setMaximumSize(QtCore.QSize(250, 16777215))
        self.gridLayout = QtGui.QGridLayout(wgCacheEval)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vlEval = QtGui.QVBoxLayout()
        self.vlEval.setSpacing(0)
        self.vlEval.setContentsMargins(-1, 2, -1, 2)
        self.vlEval.setObjectName(_fromUtf8("vlEval"))
        self.pbClothCache = QtGui.QToolButton(wgCacheEval)
        self.pbClothCache.setMinimumSize(QtCore.QSize(0, 0))
        self.pbClothCache.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pbClothCache.setFont(font)
        self.pbClothCache.setIconSize(QtCore.QSize(36, 36))
        self.pbClothCache.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.pbClothCache.setObjectName(_fromUtf8("pbClothCache"))
        self.vlEval.addWidget(self.pbClothCache)
        self.pbAppendCache = QtGui.QToolButton(wgCacheEval)
        self.pbAppendCache.setMinimumSize(QtCore.QSize(0, 0))
        self.pbAppendCache.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pbAppendCache.setFont(font)
        self.pbAppendCache.setIconSize(QtCore.QSize(36, 36))
        self.pbAppendCache.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.pbAppendCache.setObjectName(_fromUtf8("pbAppendCache"))
        self.vlEval.addWidget(self.pbAppendCache)
        self.pbGeoCache = QtGui.QToolButton(wgCacheEval)
        self.pbGeoCache.setMinimumSize(QtCore.QSize(0, 0))
        self.pbGeoCache.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pbGeoCache.setFont(font)
        self.pbGeoCache.setIconSize(QtCore.QSize(36, 36))
        self.pbGeoCache.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.pbGeoCache.setObjectName(_fromUtf8("pbGeoCache"))
        self.vlEval.addWidget(self.pbGeoCache)
        self.pbClearCache = QtGui.QToolButton(wgCacheEval)
        self.pbClearCache.setMinimumSize(QtCore.QSize(0, 0))
        self.pbClearCache.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pbClearCache.setFont(font)
        self.pbClearCache.setIconSize(QtCore.QSize(36, 36))
        self.pbClearCache.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.pbClearCache.setObjectName(_fromUtf8("pbClearCache"))
        self.vlEval.addWidget(self.pbClearCache)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlEval.addItem(spacerItem)
        self.gridLayout.addLayout(self.vlEval, 0, 2, 3, 1)
        self.twCommonAttr = QtGui.QTreeWidget(wgCacheEval)
        self.twCommonAttr.setMinimumSize(QtCore.QSize(0, 0))
        self.twCommonAttr.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.twCommonAttr.setObjectName(_fromUtf8("twCommonAttr"))
        self.gridLayout.addWidget(self.twCommonAttr, 0, 0, 1, 1)
        self.line = QtGui.QFrame(wgCacheEval)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 1, 3, 1)
        self.twCustomAttr = QtGui.QTreeWidget(wgCacheEval)
        self.twCustomAttr.setMinimumSize(QtCore.QSize(0, 0))
        self.twCustomAttr.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.twCustomAttr.setObjectName(_fromUtf8("twCustomAttr"))
        self.gridLayout.addWidget(self.twCustomAttr, 2, 0, 1, 1)
        self.line_2 = QtGui.QFrame(wgCacheEval)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.retranslateUi(wgCacheEval)
        QtCore.QMetaObject.connectSlotsByName(wgCacheEval)

    def retranslateUi(self, wgCacheEval):
        wgCacheEval.setWindowTitle(_translate("wgCacheEval", "Cache Eval", None))
        self.pbClothCache.setText(_translate("wgCacheEval", "Create nCloth Cache", None))
        self.pbAppendCache.setText(_translate("wgCacheEval", "Append To Cache", None))
        self.pbGeoCache.setText(_translate("wgCacheEval", "Create Geo Cache", None))
        self.pbClearCache.setText(_translate("wgCacheEval", "Delete Cache Node", None))
        self.twCommonAttr.headerItem().setText(0, _translate("wgCacheEval", "Common Attributes", None))
        self.twCustomAttr.headerItem().setText(0, _translate("wgCacheEval", "Custom Attributes", None))

