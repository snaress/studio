# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\fondation\gui\src\nodeEditor.ui'
#
# Created: Fri Aug 14 23:25:05 2015
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

class Ui_wgNodeEditor(object):
    def setupUi(self, wgNodeEditor):
        wgNodeEditor.setObjectName(_fromUtf8("wgNodeEditor"))
        wgNodeEditor.resize(444, 800)
        self.gridLayout = QtGui.QGridLayout(wgNodeEditor)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hlNodeName = QtGui.QHBoxLayout()
        self.hlNodeName.setSpacing(4)
        self.hlNodeName.setContentsMargins(4, -1, 4, -1)
        self.hlNodeName.setObjectName(_fromUtf8("hlNodeName"))
        self.lName = QtGui.QLabel(wgNodeEditor)
        self.lName.setMinimumSize(QtCore.QSize(30, 0))
        self.lName.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lName.setObjectName(_fromUtf8("lName"))
        self.hlNodeName.addWidget(self.lName)
        self.leNodeName = QtGui.QLineEdit(wgNodeEditor)
        self.leNodeName.setMinimumSize(QtCore.QSize(150, 0))
        self.leNodeName.setReadOnly(True)
        self.leNodeName.setObjectName(_fromUtf8("leNodeName"))
        self.hlNodeName.addWidget(self.leNodeName)
        self.lType = QtGui.QLabel(wgNodeEditor)
        self.lType.setMinimumSize(QtCore.QSize(30, 0))
        self.lType.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lType.setObjectName(_fromUtf8("lType"))
        self.hlNodeName.addWidget(self.lType)
        self.lTypeValue = QtGui.QLabel(wgNodeEditor)
        self.lTypeValue.setObjectName(_fromUtf8("lTypeValue"))
        self.hlNodeName.addWidget(self.lTypeValue)
        self.gridLayout.addLayout(self.hlNodeName, 0, 0, 1, 1)
        self.hlNodeVersion = QtGui.QHBoxLayout()
        self.hlNodeVersion.setSpacing(4)
        self.hlNodeVersion.setContentsMargins(4, -1, 4, -1)
        self.hlNodeVersion.setObjectName(_fromUtf8("hlNodeVersion"))
        self.lVTitle = QtGui.QLabel(wgNodeEditor)
        self.lVTitle.setMinimumSize(QtCore.QSize(30, 0))
        self.lVTitle.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lVTitle.setObjectName(_fromUtf8("lVTitle"))
        self.hlNodeVersion.addWidget(self.lVTitle)
        self.leVersionTitle = QtGui.QLineEdit(wgNodeEditor)
        self.leVersionTitle.setMinimumSize(QtCore.QSize(0, 18))
        self.leVersionTitle.setMaximumSize(QtCore.QSize(16777215, 18))
        self.leVersionTitle.setObjectName(_fromUtf8("leVersionTitle"))
        self.hlNodeVersion.addWidget(self.leVersionTitle)
        self.lVersion = QtGui.QLabel(wgNodeEditor)
        self.lVersion.setMinimumSize(QtCore.QSize(40, 0))
        self.lVersion.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lVersion.setObjectName(_fromUtf8("lVersion"))
        self.hlNodeVersion.addWidget(self.lVersion)
        self.cbNodeVersion = QtGui.QComboBox(wgNodeEditor)
        self.cbNodeVersion.setMinimumSize(QtCore.QSize(60, 18))
        self.cbNodeVersion.setMaximumSize(QtCore.QSize(60, 18))
        self.cbNodeVersion.setSizeIncrement(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cbNodeVersion.setFont(font)
        self.cbNodeVersion.setObjectName(_fromUtf8("cbNodeVersion"))
        self.hlNodeVersion.addWidget(self.cbNodeVersion)
        self.pbNewVersion = QtGui.QPushButton(wgNodeEditor)
        self.pbNewVersion.setMinimumSize(QtCore.QSize(35, 18))
        self.pbNewVersion.setMaximumSize(QtCore.QSize(35, 18))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pbNewVersion.setFont(font)
        self.pbNewVersion.setObjectName(_fromUtf8("pbNewVersion"))
        self.hlNodeVersion.addWidget(self.pbNewVersion)
        self.pbDelVersion = QtGui.QPushButton(wgNodeEditor)
        self.pbDelVersion.setMinimumSize(QtCore.QSize(35, 18))
        self.pbDelVersion.setMaximumSize(QtCore.QSize(35, 18))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pbDelVersion.setFont(font)
        self.pbDelVersion.setObjectName(_fromUtf8("pbDelVersion"))
        self.hlNodeVersion.addWidget(self.pbDelVersion)
        self.gridLayout.addLayout(self.hlNodeVersion, 1, 0, 1, 1)
        self.line = QtGui.QFrame(wgNodeEditor)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 676, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.line_5 = QtGui.QFrame(wgNodeEditor)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout.addWidget(self.line_5, 4, 0, 1, 1)
        self.hlNodeBtns = QtGui.QHBoxLayout()
        self.hlNodeBtns.setSpacing(1)
        self.hlNodeBtns.setObjectName(_fromUtf8("hlNodeBtns"))
        self.pbClose = QtGui.QPushButton(wgNodeEditor)
        self.pbClose.setMinimumSize(QtCore.QSize(60, 20))
        self.pbClose.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbClose.setObjectName(_fromUtf8("pbClose"))
        self.hlNodeBtns.addWidget(self.pbClose)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlNodeBtns.addItem(spacerItem1)
        self.pbSave = QtGui.QPushButton(wgNodeEditor)
        self.pbSave.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbSave.setObjectName(_fromUtf8("pbSave"))
        self.hlNodeBtns.addWidget(self.pbSave)
        self.pbCancel = QtGui.QPushButton(wgNodeEditor)
        self.pbCancel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.hlNodeBtns.addWidget(self.pbCancel)
        self.gridLayout.addLayout(self.hlNodeBtns, 5, 0, 1, 1)

        self.retranslateUi(wgNodeEditor)
        QtCore.QMetaObject.connectSlotsByName(wgNodeEditor)

    def retranslateUi(self, wgNodeEditor):
        wgNodeEditor.setWindowTitle(_translate("wgNodeEditor", "Node Editor", None))
        self.lName.setText(_translate("wgNodeEditor", "Name: ", None))
        self.lType.setText(_translate("wgNodeEditor", "Type:", None))
        self.lTypeValue.setText(_translate("wgNodeEditor", "Modul", None))
        self.lVTitle.setText(_translate("wgNodeEditor", "Title: ", None))
        self.lVersion.setText(_translate("wgNodeEditor", "Version:", None))
        self.pbNewVersion.setText(_translate("wgNodeEditor", "New", None))
        self.pbDelVersion.setText(_translate("wgNodeEditor", "Del", None))
        self.pbClose.setText(_translate("wgNodeEditor", "Close", None))
        self.pbSave.setText(_translate("wgNodeEditor", "Save", None))
        self.pbCancel.setText(_translate("wgNodeEditor", "Cancel", None))

