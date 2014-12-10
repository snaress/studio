# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\util\toolManager\ui\toolManager.ui'
#
# Created: Wed Dec 10 01:25:25 2014
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

class Ui_mwToolManager(object):
    def setupUi(self, mwToolManager):
        mwToolManager.setObjectName(_fromUtf8("mwToolManager"))
        mwToolManager.resize(268, 435)
        self.centralwidget = QtGui.QWidget(mwToolManager)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.twTools = QtGui.QTreeWidget(self.splitter)
        self.twTools.setObjectName(_fromUtf8("twTools"))
        self.twTools.headerItem().setText(0, _fromUtf8("1"))
        self.twTools.header().setVisible(False)
        self.vfToolBox = QtGui.QFrame(self.splitter)
        self.vfToolBox.setObjectName(_fromUtf8("vfToolBox"))
        self.vlToolBox = QtGui.QVBoxLayout(self.vfToolBox)
        self.vlToolBox.setSpacing(1)
        self.vlToolBox.setObjectName(_fromUtf8("vlToolBox"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        mwToolManager.setCentralWidget(self.centralwidget)

        self.retranslateUi(mwToolManager)
        QtCore.QMetaObject.connectSlotsByName(mwToolManager)

    def retranslateUi(self, mwToolManager):
        mwToolManager.setWindowTitle(_translate("mwToolManager", "ToolManager", None))

