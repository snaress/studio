# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgDataGroup.ui'
#
# Created: Sat Jun 20 19:41:37 2015
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

class Ui_wgDataGroup(object):
    def setupUi(self, wgDataGroup):
        wgDataGroup.setObjectName(_fromUtf8("wgDataGroup"))
        wgDataGroup.resize(324, 20)
        self.glDataGroup = QtGui.QGridLayout(wgDataGroup)
        self.glDataGroup.setMargin(0)
        self.glDataGroup.setHorizontalSpacing(2)
        self.glDataGroup.setVerticalSpacing(0)
        self.glDataGroup.setObjectName(_fromUtf8("glDataGroup"))
        self.pbGrpName = QtGui.QPushButton(wgDataGroup)
        self.pbGrpName.setMinimumSize(QtCore.QSize(20, 20))
        self.pbGrpName.setMaximumSize(QtCore.QSize(20, 20))
        self.pbGrpName.setText(_fromUtf8(""))
        self.pbGrpName.setIconSize(QtCore.QSize(20, 20))
        self.pbGrpName.setCheckable(True)
        self.pbGrpName.setFlat(True)
        self.pbGrpName.setObjectName(_fromUtf8("pbGrpName"))
        self.glDataGroup.addWidget(self.pbGrpName, 0, 0, 1, 1)
        self.line = QtGui.QFrame(wgDataGroup)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.glDataGroup.addWidget(self.line, 0, 1, 1, 1)
        self.lGrpName = QtGui.QLabel(wgDataGroup)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lGrpName.setFont(font)
        self.lGrpName.setObjectName(_fromUtf8("lGrpName"))
        self.glDataGroup.addWidget(self.lGrpName, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.glDataGroup.addItem(spacerItem, 0, 3, 1, 1)

        self.retranslateUi(wgDataGroup)
        QtCore.QMetaObject.connectSlotsByName(wgDataGroup)

    def retranslateUi(self, wgDataGroup):
        wgDataGroup.setWindowTitle(_translate("wgDataGroup", "Data Group", None))
        self.lGrpName.setText(_translate("wgDataGroup", "TextLabel", None))

