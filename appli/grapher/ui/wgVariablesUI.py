# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\ui\wgVariables.ui'
#
# Created: Wed Nov 19 07:31:11 2014
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

class Ui_mwVariables(object):
    def setupUi(self, mwVariables):
        mwVariables.setObjectName(_fromUtf8("mwVariables"))
        mwVariables.resize(528, 263)
        self.centralwidget = QtGui.QWidget(mwVariables)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.twVariables = QtGui.QTreeWidget(self.centralwidget)
        self.twVariables.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.twVariables.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.twVariables.setIndentation(0)
        self.twVariables.setItemsExpandable(False)
        self.twVariables.setColumnCount(6)
        self.twVariables.setObjectName(_fromUtf8("twVariables"))
        self.twVariables.headerItem().setText(0, _fromUtf8("Ind"))
        self.gridLayout.addWidget(self.twVariables, 0, 0, 1, 1)
        mwVariables.setCentralWidget(self.centralwidget)
        self.mbVariables = QtGui.QMenuBar(mwVariables)
        self.mbVariables.setGeometry(QtCore.QRect(0, 0, 528, 21))
        self.mbVariables.setObjectName(_fromUtf8("mbVariables"))
        self.mEdit = QtGui.QMenu(self.mbVariables)
        self.mEdit.setObjectName(_fromUtf8("mEdit"))
        mwVariables.setMenuBar(self.mbVariables)
        self.miCopy = QtGui.QAction(mwVariables)
        self.miCopy.setObjectName(_fromUtf8("miCopy"))
        self.miCut = QtGui.QAction(mwVariables)
        self.miCut.setObjectName(_fromUtf8("miCut"))
        self.miPaste = QtGui.QAction(mwVariables)
        self.miPaste.setObjectName(_fromUtf8("miPaste"))
        self.miMoveUp = QtGui.QAction(mwVariables)
        self.miMoveUp.setObjectName(_fromUtf8("miMoveUp"))
        self.miMoveDn = QtGui.QAction(mwVariables)
        self.miMoveDn.setObjectName(_fromUtf8("miMoveDn"))
        self.miPush = QtGui.QAction(mwVariables)
        self.miPush.setObjectName(_fromUtf8("miPush"))
        self.miPull = QtGui.QAction(mwVariables)
        self.miPull.setObjectName(_fromUtf8("miPull"))
        self.miAdd = QtGui.QAction(mwVariables)
        self.miAdd.setObjectName(_fromUtf8("miAdd"))
        self.miDel = QtGui.QAction(mwVariables)
        self.miDel.setObjectName(_fromUtf8("miDel"))
        self.mEdit.addAction(self.miAdd)
        self.mEdit.addAction(self.miDel)
        self.mEdit.addSeparator()
        self.mEdit.addAction(self.miCopy)
        self.mEdit.addAction(self.miCut)
        self.mEdit.addAction(self.miPaste)
        self.mEdit.addSeparator()
        self.mEdit.addAction(self.miMoveUp)
        self.mEdit.addAction(self.miMoveDn)
        self.mEdit.addSeparator()
        self.mEdit.addAction(self.miPush)
        self.mEdit.addAction(self.miPull)
        self.mbVariables.addAction(self.mEdit.menuAction())

        self.retranslateUi(mwVariables)
        QtCore.QMetaObject.connectSlotsByName(mwVariables)

    def retranslateUi(self, mwVariables):
        mwVariables.setWindowTitle(_translate("mwVariables", "MainWindow", None))
        self.twVariables.headerItem().setText(1, _translate("mwVariables", "On", None))
        self.twVariables.headerItem().setText(2, _translate("mwVariables", "Label", None))
        self.twVariables.headerItem().setText(3, _translate("mwVariables", "Type", None))
        self.twVariables.headerItem().setText(4, _translate("mwVariables", "Value", None))
        self.twVariables.headerItem().setText(5, _translate("mwVariables", "Comment", None))
        self.mEdit.setTitle(_translate("mwVariables", "Edit", None))
        self.miCopy.setText(_translate("mwVariables", "Copy", None))
        self.miCut.setText(_translate("mwVariables", "Cut", None))
        self.miPaste.setText(_translate("mwVariables", "Paste", None))
        self.miMoveUp.setText(_translate("mwVariables", "Move Up", None))
        self.miMoveDn.setText(_translate("mwVariables", "Move Down", None))
        self.miPush.setText(_translate("mwVariables", "Push", None))
        self.miPull.setText(_translate("mwVariables", "Pull", None))
        self.miAdd.setText(_translate("mwVariables", "Add", None))
        self.miDel.setText(_translate("mwVariables", "Delete", None))

