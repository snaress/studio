# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothEditor\ui\wgFiles.ui'
#
# Created: Mon Apr 20 00:33:23 2015
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

class Ui_wgFiles(object):
    def setupUi(self, wgFiles):
        wgFiles.setObjectName(_fromUtf8("wgFiles"))
        wgFiles.resize(480, 529)
        self.gridLayout = QtGui.QGridLayout(wgFiles)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line = QtGui.QFrame(wgFiles)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.twFiles = QtGui.QTreeWidget(wgFiles)
        self.twFiles.setObjectName(_fromUtf8("twFiles"))
        self.twFiles.headerItem().setText(0, _fromUtf8("1"))
        self.twFiles.header().setVisible(False)
        self.gridLayout.addWidget(self.twFiles, 2, 0, 1, 1)
        self.hlImpMode = QtGui.QHBoxLayout()
        self.hlImpMode.setSpacing(12)
        self.hlImpMode.setObjectName(_fromUtf8("hlImpMode"))
        self.lLoadMode = QtGui.QLabel(wgFiles)
        self.lLoadMode.setMinimumSize(QtCore.QSize(60, 0))
        self.lLoadMode.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lLoadMode.setObjectName(_fromUtf8("lLoadMode"))
        self.hlImpMode.addWidget(self.lLoadMode)
        self.cbImpAll = QtGui.QCheckBox(wgFiles)
        self.cbImpAll.setChecked(True)
        self.cbImpAll.setObjectName(_fromUtf8("cbImpAll"))
        self.hlImpMode.addWidget(self.cbImpAll)
        self.cbImpSel = QtGui.QCheckBox(wgFiles)
        self.cbImpSel.setObjectName(_fromUtf8("cbImpSel"))
        self.hlImpMode.addWidget(self.cbImpSel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlImpMode.addItem(spacerItem)
        self.gridLayout.addLayout(self.hlImpMode, 4, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pbLoad = QtGui.QPushButton(wgFiles)
        self.pbLoad.setObjectName(_fromUtf8("pbLoad"))
        self.horizontalLayout.addWidget(self.pbLoad)
        self.pbSave = QtGui.QPushButton(wgFiles)
        self.pbSave.setObjectName(_fromUtf8("pbSave"))
        self.horizontalLayout.addWidget(self.pbSave)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.hlFilesRootPath = QtGui.QHBoxLayout()
        self.hlFilesRootPath.setSpacing(2)
        self.hlFilesRootPath.setObjectName(_fromUtf8("hlFilesRootPath"))
        self.lFilesRootPath = QtGui.QLabel(wgFiles)
        self.lFilesRootPath.setMinimumSize(QtCore.QSize(80, 0))
        self.lFilesRootPath.setMaximumSize(QtCore.QSize(80, 20))
        self.lFilesRootPath.setObjectName(_fromUtf8("lFilesRootPath"))
        self.hlFilesRootPath.addWidget(self.lFilesRootPath)
        self.leFilesRootPath = QtGui.QLineEdit(wgFiles)
        self.leFilesRootPath.setReadOnly(False)
        self.leFilesRootPath.setObjectName(_fromUtf8("leFilesRootPath"))
        self.hlFilesRootPath.addWidget(self.leFilesRootPath)
        self.pbSetFilesPath = QtGui.QPushButton(wgFiles)
        self.pbSetFilesPath.setMinimumSize(QtCore.QSize(50, 0))
        self.pbSetFilesPath.setMaximumSize(QtCore.QSize(50, 20))
        self.pbSetFilesPath.setObjectName(_fromUtf8("pbSetFilesPath"))
        self.hlFilesRootPath.addWidget(self.pbSetFilesPath)
        self.gridLayout.addLayout(self.hlFilesRootPath, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(wgFiles)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.retranslateUi(wgFiles)
        QtCore.QMetaObject.connectSlotsByName(wgFiles)

    def retranslateUi(self, wgFiles):
        wgFiles.setWindowTitle(_translate("wgFiles", "Files", None))
        self.lLoadMode.setText(_translate("wgFiles", "Load Mode: ", None))
        self.cbImpAll.setText(_translate("wgFiles", "All Vtx Maps", None))
        self.cbImpSel.setText(_translate("wgFiles", "Selected Vtx Map", None))
        self.pbLoad.setText(_translate("wgFiles", "Load", None))
        self.pbSave.setText(_translate("wgFiles", "Save", None))
        self.lFilesRootPath.setText(_translate("wgFiles", "Files Root Path:", None))
        self.pbSetFilesPath.setText(_translate("wgFiles", "Set", None))

