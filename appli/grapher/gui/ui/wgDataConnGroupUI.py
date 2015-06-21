# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgDataConnGroup.ui'
#
# Created: Sat Jun 20 21:21:45 2015
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

class Ui_wgConnGroup(object):
    def setupUi(self, wgConnGroup):
        wgConnGroup.setObjectName(_fromUtf8("wgConnGroup"))
        wgConnGroup.resize(324, 20)
        self.glDataGroup = QtGui.QGridLayout(wgConnGroup)
        self.glDataGroup.setMargin(0)
        self.glDataGroup.setHorizontalSpacing(2)
        self.glDataGroup.setVerticalSpacing(0)
        self.glDataGroup.setObjectName(_fromUtf8("glDataGroup"))
        self.line_2 = QtGui.QFrame(wgConnGroup)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.glDataGroup.addWidget(self.line_2, 0, 6, 1, 1)
        self.lGrpName = QtGui.QLabel(wgConnGroup)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lGrpName.setFont(font)
        self.lGrpName.setObjectName(_fromUtf8("lGrpName"))
        self.glDataGroup.addWidget(self.lGrpName, 0, 2, 1, 1)
        self.line = QtGui.QFrame(wgConnGroup)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.glDataGroup.addWidget(self.line, 0, 1, 1, 1)
        self.pbGrpName = QtGui.QPushButton(wgConnGroup)
        self.pbGrpName.setMinimumSize(QtCore.QSize(20, 20))
        self.pbGrpName.setMaximumSize(QtCore.QSize(20, 20))
        self.pbGrpName.setText(_fromUtf8(""))
        self.pbGrpName.setIconSize(QtCore.QSize(20, 20))
        self.pbGrpName.setCheckable(True)
        self.pbGrpName.setChecked(False)
        self.pbGrpName.setFlat(True)
        self.pbGrpName.setObjectName(_fromUtf8("pbGrpName"))
        self.glDataGroup.addWidget(self.pbGrpName, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.glDataGroup.addItem(spacerItem, 0, 3, 1, 1)
        self.lCount = QtGui.QLabel(wgConnGroup)
        self.lCount.setObjectName(_fromUtf8("lCount"))
        self.glDataGroup.addWidget(self.lCount, 0, 5, 1, 1)
        self.pbGrpSelect = QtGui.QPushButton(wgConnGroup)
        self.pbGrpSelect.setMinimumSize(QtCore.QSize(45, 20))
        self.pbGrpSelect.setMaximumSize(QtCore.QSize(45, 20))
        self.pbGrpSelect.setObjectName(_fromUtf8("pbGrpSelect"))
        self.glDataGroup.addWidget(self.pbGrpSelect, 0, 7, 1, 1)
        self.line_3 = QtGui.QFrame(wgConnGroup)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.glDataGroup.addWidget(self.line_3, 0, 4, 1, 1)

        self.retranslateUi(wgConnGroup)
        QtCore.QMetaObject.connectSlotsByName(wgConnGroup)

    def retranslateUi(self, wgConnGroup):
        wgConnGroup.setWindowTitle(_translate("wgConnGroup", "Connection Group", None))
        self.lGrpName.setText(_translate("wgConnGroup", "TextLabel", None))
        self.lCount.setText(_translate("wgConnGroup", "0", None))
        self.pbGrpSelect.setText(_translate("wgConnGroup", "select", None))

