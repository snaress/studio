# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\prodManager\ui\defaultSettingsWgt.ui'
#
# Created: Sun Mar 01 14:36:01 2015
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

class Ui_wgSettings(object):
    def setupUi(self, wgSettings):
        wgSettings.setObjectName(_fromUtf8("wgSettings"))
        wgSettings.resize(428, 191)
        self.gridLayout = QtGui.QGridLayout(wgSettings)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setContentsMargins(1, 0, 1, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vlSettings = QtGui.QVBoxLayout()
        self.vlSettings.setSpacing(2)
        self.vlSettings.setObjectName(_fromUtf8("vlSettings"))
        self.hlSettings = QtGui.QHBoxLayout()
        self.hlSettings.setSpacing(2)
        self.hlSettings.setObjectName(_fromUtf8("hlSettings"))
        self.qfButtons = QtGui.QFrame(wgSettings)
        self.qfButtons.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qfButtons.setObjectName(_fromUtf8("qfButtons"))
        self.vlTreeBtns = QtGui.QVBoxLayout(self.qfButtons)
        self.vlTreeBtns.setSpacing(0)
        self.vlTreeBtns.setMargin(0)
        self.vlTreeBtns.setObjectName(_fromUtf8("vlTreeBtns"))
        self.cbCurrentTree = QtGui.QComboBox(self.qfButtons)
        self.cbCurrentTree.setObjectName(_fromUtf8("cbCurrentTree"))
        self.vlTreeBtns.addWidget(self.cbCurrentTree)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlTreeBtns.addItem(spacerItem)
        self.pbAddItem = QtGui.QPushButton(self.qfButtons)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbAddItem.sizePolicy().hasHeightForWidth())
        self.pbAddItem.setSizePolicy(sizePolicy)
        self.pbAddItem.setMinimumSize(QtCore.QSize(0, 0))
        self.pbAddItem.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbAddItem.setObjectName(_fromUtf8("pbAddItem"))
        self.vlTreeBtns.addWidget(self.pbAddItem)
        self.pbDelItem = QtGui.QPushButton(self.qfButtons)
        self.pbDelItem.setEnabled(True)
        self.pbDelItem.setObjectName(_fromUtf8("pbDelItem"))
        self.vlTreeBtns.addWidget(self.pbDelItem)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlTreeBtns.addItem(spacerItem1)
        self.pbItemUp = QtGui.QPushButton(self.qfButtons)
        self.pbItemUp.setMinimumSize(QtCore.QSize(50, 20))
        self.pbItemUp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbItemUp.setObjectName(_fromUtf8("pbItemUp"))
        self.vlTreeBtns.addWidget(self.pbItemUp)
        self.pbItemDn = QtGui.QPushButton(self.qfButtons)
        self.pbItemDn.setMinimumSize(QtCore.QSize(50, 20))
        self.pbItemDn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbItemDn.setObjectName(_fromUtf8("pbItemDn"))
        self.vlTreeBtns.addWidget(self.pbItemDn)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlTreeBtns.addItem(spacerItem2)
        self.hlSettings.addWidget(self.qfButtons)
        self.twTree = QtGui.QTreeWidget(wgSettings)
        self.twTree.setMinimumSize(QtCore.QSize(0, 0))
        self.twTree.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.twTree.setAlternatingRowColors(False)
        self.twTree.setIndentation(2)
        self.twTree.setObjectName(_fromUtf8("twTree"))
        self.twTree.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.twTree.headerItem().setTextAlignment(1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.twTree.headerItem().setTextAlignment(2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.twTree.header().setStretchLastSection(False)
        self.hlSettings.addWidget(self.twTree)
        self.vlSettings.addLayout(self.hlSettings)
        self.gridLayout.addLayout(self.vlSettings, 0, 0, 1, 1)

        self.retranslateUi(wgSettings)
        QtCore.QMetaObject.connectSlotsByName(wgSettings)

    def retranslateUi(self, wgSettings):
        wgSettings.setWindowTitle(_translate("wgSettings", "ProdTree", None))
        self.cbCurrentTree.setToolTip(_translate("wgSettings", "Current Tree", None))
        self.pbAddItem.setText(_translate("wgSettings", "Add Item", None))
        self.pbDelItem.setText(_translate("wgSettings", "Del Item", None))
        self.pbItemUp.setText(_translate("wgSettings", "Up", None))
        self.pbItemDn.setText(_translate("wgSettings", "Down", None))
        self.twTree.headerItem().setText(0, _translate("wgSettings", "Header1", None))
        self.twTree.headerItem().setText(1, _translate("wgSettings", "Header2", None))
        self.twTree.headerItem().setText(2, _translate("wgSettings", "Header3", None))

