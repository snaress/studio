# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgDataNodeFile.ui'
#
# Created: Sun Jul 19 09:32:21 2015
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

class Ui_wgDataNodeFile(object):
    def setupUi(self, wgDataNodeFile):
        wgDataNodeFile.setObjectName(_fromUtf8("wgDataNodeFile"))
        wgDataNodeFile.resize(491, 47)
        self.gridLayout = QtGui.QGridLayout(wgDataNodeFile)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(2, 0, 2, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hlOptions = QtGui.QHBoxLayout()
        self.hlOptions.setSpacing(2)
        self.hlOptions.setObjectName(_fromUtf8("hlOptions"))
        self.line_3 = QtGui.QFrame(wgDataNodeFile)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.hlOptions.addWidget(self.line_3)
        self.rbFullPath = QtGui.QRadioButton(wgDataNodeFile)
        self.rbFullPath.setObjectName(_fromUtf8("rbFullPath"))
        self.bgOptions = QtGui.QButtonGroup(wgDataNodeFile)
        self.bgOptions.setObjectName(_fromUtf8("bgOptions"))
        self.bgOptions.addButton(self.rbFullPath)
        self.hlOptions.addWidget(self.rbFullPath)
        self.rbRelPath = QtGui.QRadioButton(wgDataNodeFile)
        self.rbRelPath.setChecked(False)
        self.rbRelPath.setObjectName(_fromUtf8("rbRelPath"))
        self.bgOptions.addButton(self.rbRelPath)
        self.hlOptions.addWidget(self.rbRelPath)
        self.rbFileName = QtGui.QRadioButton(wgDataNodeFile)
        self.rbFileName.setChecked(True)
        self.rbFileName.setObjectName(_fromUtf8("rbFileName"))
        self.bgOptions.addButton(self.rbFileName)
        self.hlOptions.addWidget(self.rbFileName)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlOptions.addItem(spacerItem)
        self.line_5 = QtGui.QFrame(wgDataNodeFile)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.hlOptions.addWidget(self.line_5)
        self.pbEnable = QtGui.QPushButton(wgDataNodeFile)
        self.pbEnable.setMinimumSize(QtCore.QSize(20, 0))
        self.pbEnable.setMaximumSize(QtCore.QSize(20, 16777215))
        self.pbEnable.setText(_fromUtf8(""))
        self.pbEnable.setCheckable(True)
        self.pbEnable.setChecked(True)
        self.pbEnable.setFlat(True)
        self.pbEnable.setObjectName(_fromUtf8("pbEnable"))
        self.hlOptions.addWidget(self.pbEnable)
        self.line_4 = QtGui.QFrame(wgDataNodeFile)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.hlOptions.addWidget(self.line_4)
        self.gridLayout.addLayout(self.hlOptions, 0, 0, 1, 1)
        self.hlNodeFile = QtGui.QHBoxLayout()
        self.hlNodeFile.setSpacing(2)
        self.hlNodeFile.setObjectName(_fromUtf8("hlNodeFile"))
        self.line = QtGui.QFrame(wgDataNodeFile)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.hlNodeFile.addWidget(self.line)
        self.leNodeFile = QtGui.QLineEdit(wgDataNodeFile)
        self.leNodeFile.setMinimumSize(QtCore.QSize(0, 20))
        self.leNodeFile.setMaximumSize(QtCore.QSize(16777215, 20))
        self.leNodeFile.setObjectName(_fromUtf8("leNodeFile"))
        self.hlNodeFile.addWidget(self.leNodeFile)
        self.pbFromCasting = QtGui.QPushButton(wgDataNodeFile)
        self.pbFromCasting.setMinimumSize(QtCore.QSize(0, 20))
        self.pbFromCasting.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbFromCasting.setObjectName(_fromUtf8("pbFromCasting"))
        self.hlNodeFile.addWidget(self.pbFromCasting)
        self.pbOpen = QtGui.QPushButton(wgDataNodeFile)
        self.pbOpen.setMinimumSize(QtCore.QSize(50, 20))
        self.pbOpen.setMaximumSize(QtCore.QSize(50, 20))
        self.pbOpen.setObjectName(_fromUtf8("pbOpen"))
        self.hlNodeFile.addWidget(self.pbOpen)
        self.line_2 = QtGui.QFrame(wgDataNodeFile)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.hlNodeFile.addWidget(self.line_2)
        self.gridLayout.addLayout(self.hlNodeFile, 1, 0, 1, 1)

        self.retranslateUi(wgDataNodeFile)
        QtCore.QMetaObject.connectSlotsByName(wgDataNodeFile)

    def retranslateUi(self, wgDataNodeFile):
        wgDataNodeFile.setWindowTitle(_translate("wgDataNodeFile", "Data Node File", None))
        self.rbFullPath.setText(_translate("wgDataNodeFile", "FullPath", None))
        self.rbRelPath.setText(_translate("wgDataNodeFile", "RelativePath", None))
        self.rbFileName.setText(_translate("wgDataNodeFile", "FileName", None))
        self.pbFromCasting.setText(_translate("wgDataNodeFile", "Set From Casting", None))
        self.pbOpen.setText(_translate("wgDataNodeFile", "Open", None))

