# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\prodManager\ui\tabInfo.ui'
#
# Created: Tue Mar 24 01:58:25 2015
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

class Ui_wgInfo(object):
    def setupUi(self, wgInfo):
        wgInfo.setObjectName(_fromUtf8("wgInfo"))
        wgInfo.resize(538, 391)
        self.gridLayout = QtGui.QGridLayout(wgInfo)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.treeWidget = QtGui.QTreeWidget(wgInfo)
        self.treeWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.horizontalLayout.addWidget(self.treeWidget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(wgInfo)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.hlWorkDir = QtGui.QHBoxLayout()
        self.hlWorkDir.setSpacing(2)
        self.hlWorkDir.setObjectName(_fromUtf8("hlWorkDir"))
        self.lWorkDir = QtGui.QLabel(wgInfo)
        self.lWorkDir.setMinimumSize(QtCore.QSize(0, 0))
        self.lWorkDir.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lWorkDir.setFont(font)
        self.lWorkDir.setObjectName(_fromUtf8("lWorkDir"))
        self.hlWorkDir.addWidget(self.lWorkDir)
        self.leWorkDir = QtGui.QLineEdit(wgInfo)
        self.leWorkDir.setMinimumSize(QtCore.QSize(0, 0))
        self.leWorkDir.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.leWorkDir.setObjectName(_fromUtf8("leWorkDir"))
        self.hlWorkDir.addWidget(self.leWorkDir)
        self.bOpenWorkDir = QtGui.QPushButton(wgInfo)
        self.bOpenWorkDir.setMaximumSize(QtCore.QSize(40, 20))
        self.bOpenWorkDir.setObjectName(_fromUtf8("bOpenWorkDir"))
        self.hlWorkDir.addWidget(self.bOpenWorkDir)
        self.verticalLayout.addLayout(self.hlWorkDir)
        self.hlImaDir = QtGui.QHBoxLayout()
        self.hlImaDir.setSpacing(2)
        self.hlImaDir.setObjectName(_fromUtf8("hlImaDir"))
        self.lImaDir = QtGui.QLabel(wgInfo)
        self.lImaDir.setMinimumSize(QtCore.QSize(45, 0))
        self.lImaDir.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lImaDir.setFont(font)
        self.lImaDir.setObjectName(_fromUtf8("lImaDir"))
        self.hlImaDir.addWidget(self.lImaDir)
        self.leImaDir = QtGui.QLineEdit(wgInfo)
        self.leImaDir.setMinimumSize(QtCore.QSize(0, 0))
        self.leImaDir.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.leImaDir.setObjectName(_fromUtf8("leImaDir"))
        self.hlImaDir.addWidget(self.leImaDir)
        self.bOpenImaDir = QtGui.QPushButton(wgInfo)
        self.bOpenImaDir.setMaximumSize(QtCore.QSize(40, 20))
        self.bOpenImaDir.setObjectName(_fromUtf8("bOpenImaDir"))
        self.hlImaDir.addWidget(self.bOpenImaDir)
        self.verticalLayout.addLayout(self.hlImaDir)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(wgInfo)
        QtCore.QMetaObject.connectSlotsByName(wgInfo)

    def retranslateUi(self, wgInfo):
        wgInfo.setWindowTitle(_translate("wgInfo", "Form", None))
        self.label.setText(_translate("wgInfo", "TextLabel", None))
        self.lWorkDir.setText(_translate("wgInfo", "Work Dir:", None))
        self.bOpenWorkDir.setText(_translate("wgInfo", "Open", None))
        self.lImaDir.setText(_translate("wgInfo", "Ima Dir:", None))
        self.bOpenImaDir.setText(_translate("wgInfo", "Open", None))

