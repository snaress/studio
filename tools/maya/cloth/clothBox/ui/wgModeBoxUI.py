# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothBox\ud\wgModeBox.ui'
#
# Created: Mon Jun 01 02:21:00 2015
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

class Ui_wgModeBox(object):
    def setupUi(self, wgModeBox):
        wgModeBox.setObjectName(_fromUtf8("wgModeBox"))
        wgModeBox.resize(273, 196)
        self.gridLayout_2 = QtGui.QGridLayout(wgModeBox)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.line = QtGui.QFrame(wgModeBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pbDuplicateSelected = QtGui.QPushButton(wgModeBox)
        self.pbDuplicateSelected.setIconSize(QtCore.QSize(24, 24))
        self.pbDuplicateSelected.setFlat(False)
        self.pbDuplicateSelected.setObjectName(_fromUtf8("pbDuplicateSelected"))
        self.gridLayout.addWidget(self.pbDuplicateSelected, 0, 0, 1, 1)
        self.pbCreateOutMesh = QtGui.QPushButton(wgModeBox)
        self.pbCreateOutMesh.setEnabled(True)
        self.pbCreateOutMesh.setIconSize(QtCore.QSize(24, 24))
        self.pbCreateOutMesh.setFlat(False)
        self.pbCreateOutMesh.setObjectName(_fromUtf8("pbCreateOutMesh"))
        self.gridLayout.addWidget(self.pbCreateOutMesh, 0, 1, 1, 1)
        self.pbConnectOutMesh = QtGui.QPushButton(wgModeBox)
        self.pbConnectOutMesh.setIconSize(QtCore.QSize(24, 24))
        self.pbConnectOutMesh.setFlat(False)
        self.pbConnectOutMesh.setObjectName(_fromUtf8("pbConnectOutMesh"))
        self.gridLayout.addWidget(self.pbConnectOutMesh, 1, 0, 1, 1)
        self.pbUpdateOutMesh = QtGui.QPushButton(wgModeBox)
        self.pbUpdateOutMesh.setIconSize(QtCore.QSize(24, 24))
        self.pbUpdateOutMesh.setFlat(False)
        self.pbUpdateOutMesh.setObjectName(_fromUtf8("pbUpdateOutMesh"))
        self.gridLayout.addWidget(self.pbUpdateOutMesh, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.line_2 = QtGui.QFrame(wgModeBox)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 0, 0, 1, 1)

        self.retranslateUi(wgModeBox)
        QtCore.QMetaObject.connectSlotsByName(wgModeBox)

    def retranslateUi(self, wgModeBox):
        wgModeBox.setWindowTitle(_translate("wgModeBox", "Modeling Box", None))
        self.pbDuplicateSelected.setText(_translate("wgModeBox", "Duplicate Selected", None))
        self.pbCreateOutMesh.setText(_translate("wgModeBox", "Create OutMesh", None))
        self.pbConnectOutMesh.setText(_translate("wgModeBox", "Connect OutMesh", None))
        self.pbUpdateOutMesh.setText(_translate("wgModeBox", "Update OutMesh", None))

