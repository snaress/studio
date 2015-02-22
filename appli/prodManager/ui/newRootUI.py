# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\prodManager\ui\newRoot.ui'
#
# Created: Sun Feb 22 05:22:54 2015
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

class Ui_newRoot(object):
    def setupUi(self, newRoot):
        newRoot.setObjectName(_fromUtf8("newRoot"))
        newRoot.resize(400, 57)
        self.gridLayout = QtGui.QGridLayout(newRoot)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 2, 0, 2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lPath = QtGui.QLabel(newRoot)
        self.lPath.setObjectName(_fromUtf8("lPath"))
        self.horizontalLayout.addWidget(self.lPath)
        self.lePath = QtGui.QLineEdit(newRoot)
        self.lePath.setObjectName(_fromUtf8("lePath"))
        self.horizontalLayout.addWidget(self.lePath)
        self.pbOpen = QtGui.QPushButton(newRoot)
        self.pbOpen.setObjectName(_fromUtf8("pbOpen"))
        self.horizontalLayout.addWidget(self.pbOpen)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.line = QtGui.QFrame(newRoot)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pbAdd = QtGui.QPushButton(newRoot)
        self.pbAdd.setObjectName(_fromUtf8("pbAdd"))
        self.horizontalLayout_2.addWidget(self.pbAdd)
        self.pbCancel = QtGui.QPushButton(newRoot)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.horizontalLayout_2.addWidget(self.pbCancel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(newRoot)
        QtCore.QMetaObject.connectSlotsByName(newRoot)

    def retranslateUi(self, newRoot):
        newRoot.setWindowTitle(_translate("newRoot", "New Root Path", None))
        self.lPath.setText(_translate("newRoot", "New Root Path: ", None))
        self.pbOpen.setText(_translate("newRoot", "Open", None))
        self.pbAdd.setText(_translate("newRoot", "Add", None))
        self.pbCancel.setText(_translate("newRoot", "Cancel", None))

