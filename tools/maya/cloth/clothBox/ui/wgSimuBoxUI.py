# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothBox\ud\wgSimuBox.ui'
#
# Created: Sat Jun 06 21:08:19 2015
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

class Ui_wgSimuBox(object):
    def setupUi(self, wgSimuBox):
        wgSimuBox.setObjectName(_fromUtf8("wgSimuBox"))
        wgSimuBox.resize(271, 304)
        self.gridLayout_4 = QtGui.QGridLayout(wgSimuBox)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem = QtGui.QSpacerItem(20, 76, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 7, 0, 1, 1)
        self.line_2 = QtGui.QFrame(wgSimuBox)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_4.addWidget(self.line_2, 0, 0, 1, 1)
        self.line = QtGui.QFrame(wgSimuBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_4.addWidget(self.line, 2, 0, 1, 1)
        self.line_3 = QtGui.QFrame(wgSimuBox)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_4.addWidget(self.line_3, 4, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pbClothEditor = QtGui.QPushButton(wgSimuBox)
        self.pbClothEditor.setIconSize(QtCore.QSize(24, 24))
        self.pbClothEditor.setFlat(False)
        self.pbClothEditor.setObjectName(_fromUtf8("pbClothEditor"))
        self.gridLayout.addWidget(self.pbClothEditor, 0, 0, 1, 1)
        self.pbClothCache = QtGui.QPushButton(wgSimuBox)
        self.pbClothCache.setEnabled(True)
        self.pbClothCache.setIconSize(QtCore.QSize(24, 24))
        self.pbClothCache.setFlat(False)
        self.pbClothCache.setObjectName(_fromUtf8("pbClothCache"))
        self.gridLayout.addWidget(self.pbClothCache, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setMargin(2)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pbExportHi = QtGui.QPushButton(wgSimuBox)
        self.pbExportHi.setEnabled(True)
        self.pbExportHi.setIconSize(QtCore.QSize(24, 24))
        self.pbExportHi.setFlat(False)
        self.pbExportHi.setObjectName(_fromUtf8("pbExportHi"))
        self.gridLayout_3.addWidget(self.pbExportHi, 0, 1, 1, 1)
        self.pbConnectHi = QtGui.QPushButton(wgSimuBox)
        self.pbConnectHi.setIconSize(QtCore.QSize(24, 24))
        self.pbConnectHi.setFlat(False)
        self.pbConnectHi.setObjectName(_fromUtf8("pbConnectHi"))
        self.gridLayout_3.addWidget(self.pbConnectHi, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 5, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setMargin(2)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pbBakeSel = QtGui.QPushButton(wgSimuBox)
        self.pbBakeSel.setIconSize(QtCore.QSize(24, 24))
        self.pbBakeSel.setFlat(False)
        self.pbBakeSel.setObjectName(_fromUtf8("pbBakeSel"))
        self.gridLayout_2.addWidget(self.pbBakeSel, 0, 0, 1, 1)
        self.pbUnused1 = QtGui.QPushButton(wgSimuBox)
        self.pbUnused1.setEnabled(False)
        self.pbUnused1.setText(_fromUtf8(""))
        self.pbUnused1.setIconSize(QtCore.QSize(24, 24))
        self.pbUnused1.setFlat(True)
        self.pbUnused1.setObjectName(_fromUtf8("pbUnused1"))
        self.gridLayout_2.addWidget(self.pbUnused1, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.line_4 = QtGui.QFrame(wgSimuBox)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout_4.addWidget(self.line_4, 6, 0, 1, 1)

        self.retranslateUi(wgSimuBox)
        QtCore.QMetaObject.connectSlotsByName(wgSimuBox)

    def retranslateUi(self, wgSimuBox):
        wgSimuBox.setWindowTitle(_translate("wgSimuBox", "Simulation Box", None))
        self.pbClothEditor.setText(_translate("wgSimuBox", "Cloth Editor Ui", None))
        self.pbClothCache.setText(_translate("wgSimuBox", "Cloth Cache Ui", None))
        self.pbExportHi.setText(_translate("wgSimuBox", "Export Hi", None))
        self.pbConnectHi.setText(_translate("wgSimuBox", "Connect Hi", None))
        self.pbBakeSel.setText(_translate("wgSimuBox", "Bake Selected", None))

