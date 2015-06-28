# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgTreeItem.ui'
#
# Created: Sun Jun 28 20:34:56 2015
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

class Ui_wgTreeItem(object):
    def setupUi(self, wgTreeItem):
        wgTreeItem.setObjectName(_fromUtf8("wgTreeItem"))
        wgTreeItem.resize(324, 20)
        self.glDataGroup = QtGui.QGridLayout(wgTreeItem)
        self.glDataGroup.setMargin(0)
        self.glDataGroup.setHorizontalSpacing(2)
        self.glDataGroup.setVerticalSpacing(0)
        self.glDataGroup.setObjectName(_fromUtf8("glDataGroup"))
        self.lItemName = QtGui.QLabel(wgTreeItem)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lItemName.setFont(font)
        self.lItemName.setObjectName(_fromUtf8("lItemName"))
        self.glDataGroup.addWidget(self.lItemName, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.glDataGroup.addItem(spacerItem, 0, 2, 1, 1)
        self.pbItemIcon = QtGui.QPushButton(wgTreeItem)
        self.pbItemIcon.setMinimumSize(QtCore.QSize(20, 20))
        self.pbItemIcon.setMaximumSize(QtCore.QSize(20, 20))
        self.pbItemIcon.setText(_fromUtf8(""))
        self.pbItemIcon.setAutoRepeat(False)
        self.pbItemIcon.setFlat(True)
        self.pbItemIcon.setObjectName(_fromUtf8("pbItemIcon"))
        self.glDataGroup.addWidget(self.pbItemIcon, 0, 0, 1, 1)

        self.retranslateUi(wgTreeItem)
        QtCore.QMetaObject.connectSlotsByName(wgTreeItem)

    def retranslateUi(self, wgTreeItem):
        wgTreeItem.setWindowTitle(_translate("wgTreeItem", "Tree Item", None))
        self.lItemName.setText(_translate("wgTreeItem", "TextLabel", None))

