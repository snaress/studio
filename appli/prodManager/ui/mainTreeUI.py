# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\prodManager\ui\mainTree.ui'
#
# Created: Sun Mar 22 23:46:12 2015
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

class Ui_mainTree(object):
    def setupUi(self, mainTree):
        mainTree.setObjectName(_fromUtf8("mainTree"))
        mainTree.resize(258, 313)
        self.gridLayout = QtGui.QGridLayout(mainTree)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.twTree = QtGui.QTreeWidget(mainTree)
        self.twTree.setIndentation(24)
        self.twTree.setObjectName(_fromUtf8("twTree"))
        self.twTree.headerItem().setText(0, _fromUtf8("1"))
        self.twTree.header().setVisible(False)
        self.gridLayout.addWidget(self.twTree, 1, 0, 1, 1)
        self.line = QtGui.QFrame(mainTree)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 0, 1, 1)

        self.retranslateUi(mainTree)
        QtCore.QMetaObject.connectSlotsByName(mainTree)

    def retranslateUi(self, mainTree):
        mainTree.setWindowTitle(_translate("mainTree", "MainTree", None))

