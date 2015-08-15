# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgDataNodeConn.ui'
#
# Created: Sun Jun 21 20:33:00 2015
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

class Ui_wgNodeConnections(object):
    def setupUi(self, wgNodeConnections):
        wgNodeConnections.setObjectName(_fromUtf8("wgNodeConnections"))
        wgNodeConnections.resize(342, 300)
        self.gridLayout = QtGui.QGridLayout(wgNodeConnections)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hlNodeConnections = QtGui.QHBoxLayout()
        self.hlNodeConnections.setSpacing(0)
        self.hlNodeConnections.setObjectName(_fromUtf8("hlNodeConnections"))
        self.pbUp = QtGui.QPushButton(wgNodeConnections)
        self.pbUp.setMinimumSize(QtCore.QSize(20, 20))
        self.pbUp.setMaximumSize(QtCore.QSize(20, 20))
        self.pbUp.setText(_fromUtf8(""))
        self.pbUp.setObjectName(_fromUtf8("pbUp"))
        self.hlNodeConnections.addWidget(self.pbUp)
        self.pbDn = QtGui.QPushButton(wgNodeConnections)
        self.pbDn.setMinimumSize(QtCore.QSize(20, 20))
        self.pbDn.setMaximumSize(QtCore.QSize(20, 20))
        self.pbDn.setText(_fromUtf8(""))
        self.pbDn.setObjectName(_fromUtf8("pbDn"))
        self.hlNodeConnections.addWidget(self.pbDn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlNodeConnections.addItem(spacerItem)
        self.pbDel = QtGui.QPushButton(wgNodeConnections)
        self.pbDel.setMinimumSize(QtCore.QSize(20, 20))
        self.pbDel.setMaximumSize(QtCore.QSize(20, 20))
        self.pbDel.setText(_fromUtf8(""))
        self.pbDel.setObjectName(_fromUtf8("pbDel"))
        self.hlNodeConnections.addWidget(self.pbDel)
        self.gridLayout.addLayout(self.hlNodeConnections, 0, 0, 1, 1)
        self.twNodeConnections = QtGui.QTreeWidget(wgNodeConnections)
        self.twNodeConnections.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.twNodeConnections.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.twNodeConnections.setIndentation(0)
        self.twNodeConnections.setExpandsOnDoubleClick(False)
        self.twNodeConnections.setObjectName(_fromUtf8("twNodeConnections"))
        self.twNodeConnections.headerItem().setText(0, _fromUtf8("1"))
        self.twNodeConnections.header().setVisible(False)
        self.gridLayout.addWidget(self.twNodeConnections, 1, 0, 1, 1)

        self.retranslateUi(wgNodeConnections)
        QtCore.QMetaObject.connectSlotsByName(wgNodeConnections)

    def retranslateUi(self, wgNodeConnections):
        wgNodeConnections.setWindowTitle(_translate("wgNodeConnections", "Node Connections", None))

