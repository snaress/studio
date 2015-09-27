# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgVariables.ui'
#
# Created: Sat Sep 26 20:33:52 2015
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

class Ui_wgVariables(object):
    def setupUi(self, wgVariables):
        wgVariables.setObjectName(_fromUtf8("wgVariables"))
        wgVariables.resize(693, 348)
        self.gridLayout = QtGui.QGridLayout(wgVariables)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hlButtons = QtGui.QHBoxLayout()
        self.hlButtons.setSpacing(0)
        self.hlButtons.setContentsMargins(2, -1, -1, -1)
        self.hlButtons.setObjectName(_fromUtf8("hlButtons"))
        self.pbVarDn = QtGui.QPushButton(wgVariables)
        self.pbVarDn.setMinimumSize(QtCore.QSize(20, 20))
        self.pbVarDn.setMaximumSize(QtCore.QSize(20, 20))
        self.pbVarDn.setText(_fromUtf8(""))
        self.pbVarDn.setObjectName(_fromUtf8("pbVarDn"))
        self.hlButtons.addWidget(self.pbVarDn)
        self.pbVarUp = QtGui.QPushButton(wgVariables)
        self.pbVarUp.setMinimumSize(QtCore.QSize(20, 20))
        self.pbVarUp.setMaximumSize(QtCore.QSize(20, 20))
        self.pbVarUp.setText(_fromUtf8(""))
        self.pbVarUp.setObjectName(_fromUtf8("pbVarUp"))
        self.hlButtons.addWidget(self.pbVarUp)
        spacerItem = QtGui.QSpacerItem(40, 12, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlButtons.addItem(spacerItem)
        self.pbAddVar = QtGui.QPushButton(wgVariables)
        self.pbAddVar.setMinimumSize(QtCore.QSize(50, 20))
        self.pbAddVar.setMaximumSize(QtCore.QSize(50, 20))
        self.pbAddVar.setObjectName(_fromUtf8("pbAddVar"))
        self.hlButtons.addWidget(self.pbAddVar)
        self.pbDupVar = QtGui.QPushButton(wgVariables)
        self.pbDupVar.setMinimumSize(QtCore.QSize(50, 20))
        self.pbDupVar.setMaximumSize(QtCore.QSize(50, 20))
        self.pbDupVar.setObjectName(_fromUtf8("pbDupVar"))
        self.hlButtons.addWidget(self.pbDupVar)
        self.pbDelVar = QtGui.QPushButton(wgVariables)
        self.pbDelVar.setMinimumSize(QtCore.QSize(50, 20))
        self.pbDelVar.setMaximumSize(QtCore.QSize(50, 20))
        self.pbDelVar.setObjectName(_fromUtf8("pbDelVar"))
        self.hlButtons.addWidget(self.pbDelVar)
        self.gridLayout.addLayout(self.hlButtons, 0, 0, 1, 1)
        self.twVar = QtGui.QTreeWidget(wgVariables)
        self.twVar.setLineWidth(2)
        self.twVar.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.twVar.setIndentation(0)
        self.twVar.setItemsExpandable(False)
        self.twVar.setExpandsOnDoubleClick(False)
        self.twVar.setColumnCount(6)
        self.twVar.setObjectName(_fromUtf8("twVar"))
        self.twVar.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.twVar.headerItem().setTextAlignment(1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.twVar.headerItem().setTextAlignment(2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.twVar.headerItem().setTextAlignment(3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.twVar.headerItem().setTextAlignment(4, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.twVar.headerItem().setTextAlignment(5, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.twVar.header().setVisible(True)
        self.twVar.header().setStretchLastSection(True)
        self.gridLayout.addWidget(self.twVar, 1, 0, 1, 1)

        self.retranslateUi(wgVariables)
        QtCore.QMetaObject.connectSlotsByName(wgVariables)

    def retranslateUi(self, wgVariables):
        wgVariables.setWindowTitle(_translate("wgVariables", "Variables", None))
        self.pbAddVar.setText(_translate("wgVariables", "Add Var", None))
        self.pbDupVar.setText(_translate("wgVariables", "Dup Var", None))
        self.pbDelVar.setText(_translate("wgVariables", "Del Var", None))
        self.twVar.headerItem().setText(0, _translate("wgVariables", "N", None))
        self.twVar.headerItem().setText(1, _translate("wgVariables", "S", None))
        self.twVar.headerItem().setText(2, _translate("wgVariables", "Label", None))
        self.twVar.headerItem().setText(3, _translate("wgVariables", "Type", None))
        self.twVar.headerItem().setText(4, _translate("wgVariables", "Value", None))
        self.twVar.headerItem().setText(5, _translate("wgVariables", "Comment", None))

