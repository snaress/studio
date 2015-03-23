# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\prodManager\ui\mainTreeNode.ui'
#
# Created: Sun Mar 22 17:20:23 2015
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

class Ui_wgTreeNode(object):
    def setupUi(self, wgTreeNode):
        wgTreeNode.setObjectName(_fromUtf8("wgTreeNode"))
        wgTreeNode.resize(247, 24)
        self.gridLayout = QtGui.QGridLayout(wgTreeNode)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pbIcon = QtGui.QPushButton(wgTreeNode)
        self.pbIcon.setMinimumSize(QtCore.QSize(24, 24))
        self.pbIcon.setMaximumSize(QtCore.QSize(24, 24))
        self.pbIcon.setText(_fromUtf8(""))
        self.pbIcon.setIconSize(QtCore.QSize(24, 24))
        self.pbIcon.setObjectName(_fromUtf8("pbIcon"))
        self.gridLayout.addWidget(self.pbIcon, 0, 0, 1, 1)
        self.lName = QtGui.QLabel(wgTreeNode)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lName.setFont(font)
        self.lName.setFrameShape(QtGui.QFrame.NoFrame)
        self.lName.setObjectName(_fromUtf8("lName"))
        self.gridLayout.addWidget(self.lName, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(8, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)

        self.retranslateUi(wgTreeNode)
        QtCore.QMetaObject.connectSlotsByName(wgTreeNode)

    def retranslateUi(self, wgTreeNode):
        wgTreeNode.setWindowTitle(_translate("wgTreeNode", "Form", None))
        self.lName.setText(_translate("wgTreeNode", "TextLabel", None))

