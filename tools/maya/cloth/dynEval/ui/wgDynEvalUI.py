# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\dynEval\ud\wgDynEval.ui'
#
# Created: Sat Aug 01 06:00:50 2015
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

class Ui_wgDynEval(object):
    def setupUi(self, wgDynEval):
        wgDynEval.setObjectName(_fromUtf8("wgDynEval"))
        wgDynEval.resize(250, 276)
        wgDynEval.setMinimumSize(QtCore.QSize(0, 0))
        wgDynEval.setMaximumSize(QtCore.QSize(250, 16777215))
        self.gridLayout = QtGui.QGridLayout(wgDynEval)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.twCommonAttr = QtGui.QTreeWidget(wgDynEval)
        self.twCommonAttr.setMinimumSize(QtCore.QSize(0, 0))
        self.twCommonAttr.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.twCommonAttr.setObjectName(_fromUtf8("twCommonAttr"))
        self.gridLayout.addWidget(self.twCommonAttr, 3, 0, 1, 1)
        self.twCustomAttr = QtGui.QTreeWidget(wgDynEval)
        self.twCustomAttr.setMinimumSize(QtCore.QSize(0, 0))
        self.twCustomAttr.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.twCustomAttr.setObjectName(_fromUtf8("twCustomAttr"))
        self.gridLayout.addWidget(self.twCustomAttr, 5, 0, 1, 1)
        self.line_2 = QtGui.QFrame(wgDynEval)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 1)
        self.line = QtGui.QFrame(wgDynEval)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 3, 1, 3, 1)
        self.vlEval = QtGui.QVBoxLayout()
        self.vlEval.setSpacing(0)
        self.vlEval.setContentsMargins(-1, 2, -1, 2)
        self.vlEval.setObjectName(_fromUtf8("vlEval"))
        self.pbClothCache = QtGui.QToolButton(wgDynEval)
        self.pbClothCache.setMinimumSize(QtCore.QSize(0, 0))
        self.pbClothCache.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pbClothCache.setFont(font)
        self.pbClothCache.setIconSize(QtCore.QSize(36, 36))
        self.pbClothCache.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.pbClothCache.setObjectName(_fromUtf8("pbClothCache"))
        self.vlEval.addWidget(self.pbClothCache)
        self.pbAppendCache = QtGui.QToolButton(wgDynEval)
        self.pbAppendCache.setMinimumSize(QtCore.QSize(0, 0))
        self.pbAppendCache.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pbAppendCache.setFont(font)
        self.pbAppendCache.setIconSize(QtCore.QSize(36, 36))
        self.pbAppendCache.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.pbAppendCache.setObjectName(_fromUtf8("pbAppendCache"))
        self.vlEval.addWidget(self.pbAppendCache)
        self.pbGeoCache = QtGui.QToolButton(wgDynEval)
        self.pbGeoCache.setMinimumSize(QtCore.QSize(0, 0))
        self.pbGeoCache.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pbGeoCache.setFont(font)
        self.pbGeoCache.setIconSize(QtCore.QSize(36, 36))
        self.pbGeoCache.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.pbGeoCache.setObjectName(_fromUtf8("pbGeoCache"))
        self.vlEval.addWidget(self.pbGeoCache)
        self.pbClearCache = QtGui.QToolButton(wgDynEval)
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
        self.gridLayout.addLayout(self.vlEval, 2, 2, 4, 1)
        self.hlCacheMode = QtGui.QHBoxLayout()
        self.hlCacheMode.setContentsMargins(-1, 0, -1, -1)
        self.hlCacheMode.setObjectName(_fromUtf8("hlCacheMode"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlCacheMode.addItem(spacerItem1)
        self.lCacheAttr = QtGui.QLabel(wgDynEval)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lCacheAttr.sizePolicy().hasHeightForWidth())
        self.lCacheAttr.setSizePolicy(sizePolicy)
        self.lCacheAttr.setObjectName(_fromUtf8("lCacheAttr"))
        self.hlCacheMode.addWidget(self.lCacheAttr)
        self.cbCacheAttr = QtGui.QComboBox(wgDynEval)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbCacheAttr.sizePolicy().hasHeightForWidth())
        self.cbCacheAttr.setSizePolicy(sizePolicy)
        self.cbCacheAttr.setObjectName(_fromUtf8("cbCacheAttr"))
        self.cbCacheAttr.addItem(_fromUtf8(""))
        self.cbCacheAttr.addItem(_fromUtf8(""))
        self.cbCacheAttr.addItem(_fromUtf8(""))
        self.hlCacheMode.addWidget(self.cbCacheAttr)
        self.gridLayout.addLayout(self.hlCacheMode, 0, 0, 1, 3)

        self.retranslateUi(wgDynEval)
        QtCore.QMetaObject.connectSlotsByName(wgDynEval)

    def retranslateUi(self, wgDynEval):
        wgDynEval.setWindowTitle(_translate("wgDynEval", "Dyn Eval Control", None))
        self.twCommonAttr.headerItem().setText(0, _translate("wgDynEval", "Common Attributes", None))
        self.twCustomAttr.headerItem().setText(0, _translate("wgDynEval", "Custom Attributes", None))
        self.pbClothCache.setText(_translate("wgDynEval", "Create nCloth Cache", None))
        self.pbAppendCache.setText(_translate("wgDynEval", "Append To Cache", None))
        self.pbGeoCache.setText(_translate("wgDynEval", "Create Geo Cache", None))
        self.pbClearCache.setText(_translate("wgDynEval", "Delete Cache Node", None))
        self.lCacheAttr.setText(_translate("wgDynEval", "Cacheable Attr:", None))
        self.cbCacheAttr.setItemText(0, _translate("wgDynEval", "Positions", None))
        self.cbCacheAttr.setItemText(1, _translate("wgDynEval", "Velocities", None))
        self.cbCacheAttr.setItemText(2, _translate("wgDynEval", "Internal State", None))

