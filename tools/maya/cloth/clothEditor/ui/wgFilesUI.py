# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothEditor\ui\wgFiles.ui'
#
# Created: Sat May 16 03:49:39 2015
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
        wgFiles.resize(377, 247)
        self.gridLayout = QtGui.QGridLayout(wgFiles)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line = QtGui.QFrame(wgFiles)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 6, 0, 1, 1)
        self.line_4 = QtGui.QFrame(wgFiles)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 4, 0, 1, 1)
        self.line_3 = QtGui.QFrame(wgFiles)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(wgFiles)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 1)
        self.hlEditRoot = QtGui.QHBoxLayout()
        self.hlEditRoot.setSpacing(2)
        self.hlEditRoot.setContentsMargins(0, 0, -1, 0)
        self.hlEditRoot.setObjectName(_fromUtf8("hlEditRoot"))
        self.pbNewProject = QtGui.QPushButton(wgFiles)
        self.pbNewProject.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbNewProject.setObjectName(_fromUtf8("pbNewProject"))
        self.hlEditRoot.addWidget(self.pbNewProject)
        self.pbNewFolder = QtGui.QPushButton(wgFiles)
        self.pbNewFolder.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbNewFolder.setObjectName(_fromUtf8("pbNewFolder"))
        self.hlEditRoot.addWidget(self.pbNewFolder)
        self.pbRefresh = QtGui.QPushButton(wgFiles)
        self.pbRefresh.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbRefresh.setObjectName(_fromUtf8("pbRefresh"))
        self.hlEditRoot.addWidget(self.pbRefresh)
        self.gridLayout.addLayout(self.hlEditRoot, 3, 0, 1, 1)
        self.hlEditBtns = QtGui.QHBoxLayout()
        self.hlEditBtns.setObjectName(_fromUtf8("hlEditBtns"))
        self.pbSave = QtGui.QPushButton(wgFiles)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pbSave.setFont(font)
        self.pbSave.setObjectName(_fromUtf8("pbSave"))
        self.hlEditBtns.addWidget(self.pbSave)
        self.pbLoad = QtGui.QPushButton(wgFiles)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pbLoad.setFont(font)
        self.pbLoad.setObjectName(_fromUtf8("pbLoad"))
        self.hlEditBtns.addWidget(self.pbLoad)
        self.gridLayout.addLayout(self.hlEditBtns, 7, 0, 1, 1)
        self.splitter = QtGui.QSplitter(wgFiles)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.twDir = QtGui.QTreeWidget(self.splitter)
        self.twDir.setIndentation(15)
        self.twDir.setObjectName(_fromUtf8("twDir"))
        self.twDir.headerItem().setText(0, _fromUtf8("1"))
        self.twDir.header().setVisible(False)
        self.twFiles = QtGui.QTreeWidget(self.splitter)
        self.twFiles.setIndentation(2)
        self.twFiles.setItemsExpandable(False)
        self.twFiles.setExpandsOnDoubleClick(False)
        self.twFiles.setObjectName(_fromUtf8("twFiles"))
        self.twFiles.headerItem().setText(0, _fromUtf8("1"))
        self.twFiles.header().setVisible(False)
        self.gridLayout.addWidget(self.splitter, 5, 0, 1, 1)
        self.qfRootPath = QtGui.QFrame(wgFiles)
        self.qfRootPath.setMaximumSize(QtCore.QSize(16777215, 20))
        self.qfRootPath.setObjectName(_fromUtf8("qfRootPath"))
        self.hlFilesRootPath = QtGui.QHBoxLayout(self.qfRootPath)
        self.hlFilesRootPath.setSpacing(2)
        self.hlFilesRootPath.setContentsMargins(2, 0, 2, 0)
        self.hlFilesRootPath.setObjectName(_fromUtf8("hlFilesRootPath"))
        self.lRootPath = QtGui.QLabel(self.qfRootPath)
        self.lRootPath.setMinimumSize(QtCore.QSize(80, 0))
        self.lRootPath.setMaximumSize(QtCore.QSize(80, 20))
        self.lRootPath.setObjectName(_fromUtf8("lRootPath"))
        self.hlFilesRootPath.addWidget(self.lRootPath)
        self.lRootPathVal = QtGui.QLabel(self.qfRootPath)
        self.lRootPathVal.setObjectName(_fromUtf8("lRootPathVal"))
        self.hlFilesRootPath.addWidget(self.lRootPathVal)
        self.gridLayout.addWidget(self.qfRootPath, 1, 0, 1, 1)

        self.retranslateUi(wgFiles)
        QtCore.QMetaObject.connectSlotsByName(wgFiles)

    def retranslateUi(self, wgFiles):
        wgFiles.setWindowTitle(_translate("wgFiles", "Files", None))
        self.pbNewProject.setText(_translate("wgFiles", "New Project", None))
        self.pbNewFolder.setText(_translate("wgFiles", "New Folder", None))
        self.pbRefresh.setText(_translate("wgFiles", "Refresh", None))
        self.pbSave.setText(_translate("wgFiles", "Save", None))
        self.pbLoad.setText(_translate("wgFiles", "Load", None))
        self.lRootPath.setText(_translate("wgFiles", "Files Root Path:", None))
        self.lRootPathVal.setText(_translate("wgFiles", "Root Path Not Set", None))

