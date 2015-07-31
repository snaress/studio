# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\dynEval\ud\dynEval.ui'
#
# Created: Fri Jul 31 20:54:09 2015
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

class Ui_mwDynEval(object):
    def setupUi(self, mwDynEval):
        mwDynEval.setObjectName(_fromUtf8("mwDynEval"))
        mwDynEval.resize(500, 500)
        self.centralwidget = QtGui.QWidget(mwDynEval)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.hlUp = QtGui.QHBoxLayout(self.layoutWidget)
        self.hlUp.setSpacing(0)
        self.hlUp.setMargin(0)
        self.hlUp.setObjectName(_fromUtf8("hlUp"))
        self.vlSceneNodes = QtGui.QVBoxLayout()
        self.vlSceneNodes.setSpacing(0)
        self.vlSceneNodes.setObjectName(_fromUtf8("vlSceneNodes"))
        self.hlUp.addLayout(self.vlSceneNodes)
        self.line_3 = QtGui.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.hlUp.addWidget(self.line_3)
        self.vlNodeOptions = QtGui.QVBoxLayout()
        self.vlNodeOptions.setSpacing(0)
        self.vlNodeOptions.setObjectName(_fromUtf8("vlNodeOptions"))
        self.hlUp.addLayout(self.vlNodeOptions)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.hlDn = QtGui.QHBoxLayout(self.layoutWidget1)
        self.hlDn.setSpacing(0)
        self.hlDn.setContentsMargins(2, -1, 2, -1)
        self.hlDn.setObjectName(_fromUtf8("hlDn"))
        self.vlCaches = QtGui.QVBoxLayout()
        self.vlCaches.setSpacing(0)
        self.vlCaches.setMargin(0)
        self.vlCaches.setObjectName(_fromUtf8("vlCaches"))
        self.hlDn.addLayout(self.vlCaches)
        self.line_2 = QtGui.QFrame(self.layoutWidget1)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.hlDn.addWidget(self.line_2)
        self.vlCacheInfo = QtGui.QVBoxLayout()
        self.vlCacheInfo.setSpacing(0)
        self.vlCacheInfo.setObjectName(_fromUtf8("vlCacheInfo"))
        self.hlDn.addLayout(self.vlCacheInfo)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        mwDynEval.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mwDynEval)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.mOptions = QtGui.QMenu(self.menubar)
        self.mOptions.setObjectName(_fromUtf8("mOptions"))
        self.mFilters = QtGui.QMenu(self.mOptions)
        self.mFilters.setTearOffEnabled(True)
        self.mFilters.setObjectName(_fromUtf8("mFilters"))
        self.mFiles = QtGui.QMenu(self.menubar)
        self.mFiles.setObjectName(_fromUtf8("mFiles"))
        self.mOpenRootPath = QtGui.QMenu(self.mFiles)
        self.mOpenRootPath.setObjectName(_fromUtf8("mOpenRootPath"))
        mwDynEval.setMenuBar(self.menubar)
        self.miToolTips = QtGui.QAction(mwDynEval)
        self.miToolTips.setCheckable(True)
        self.miToolTips.setChecked(False)
        self.miToolTips.setObjectName(_fromUtf8("miToolTips"))
        self.actionToto = QtGui.QAction(mwDynEval)
        self.actionToto.setObjectName(_fromUtf8("actionToto"))
        self.miRefreshUi = QtGui.QAction(mwDynEval)
        self.miRefreshUi.setObjectName(_fromUtf8("miRefreshUi"))
        self.miSetRootPath = QtGui.QAction(mwDynEval)
        self.miSetRootPath.setObjectName(_fromUtf8("miSetRootPath"))
        self.miXplorer = QtGui.QAction(mwDynEval)
        self.miXplorer.setObjectName(_fromUtf8("miXplorer"))
        self.miXterm = QtGui.QAction(mwDynEval)
        self.miXterm.setObjectName(_fromUtf8("miXterm"))
        self.miNamespace = QtGui.QAction(mwDynEval)
        self.miNamespace.setCheckable(True)
        self.miNamespace.setChecked(True)
        self.miNamespace.setObjectName(_fromUtf8("miNamespace"))
        self.mOptions.addAction(self.miToolTips)
        self.mOptions.addAction(self.miNamespace)
        self.mOptions.addAction(self.miRefreshUi)
        self.mOptions.addAction(self.mFilters.menuAction())
        self.mOpenRootPath.addAction(self.miXplorer)
        self.mOpenRootPath.addAction(self.miXterm)
        self.mFiles.addAction(self.miSetRootPath)
        self.mFiles.addAction(self.mOpenRootPath.menuAction())
        self.menubar.addAction(self.mFiles.menuAction())
        self.menubar.addAction(self.mOptions.menuAction())

        self.retranslateUi(mwDynEval)
        QtCore.QMetaObject.connectSlotsByName(mwDynEval)

    def retranslateUi(self, mwDynEval):
        mwDynEval.setWindowTitle(_translate("mwDynEval", "Dyn Eval", None))
        self.mOptions.setTitle(_translate("mwDynEval", "Options", None))
        self.mFilters.setTitle(_translate("mwDynEval", "Filters", None))
        self.mFiles.setTitle(_translate("mwDynEval", "Files", None))
        self.mOpenRootPath.setTitle(_translate("mwDynEval", "Open Root Path", None))
        self.miToolTips.setText(_translate("mwDynEval", "ToolTips", None))
        self.actionToto.setText(_translate("mwDynEval", "toto", None))
        self.miRefreshUi.setText(_translate("mwDynEval", "Refresh Ui", None))
        self.miSetRootPath.setText(_translate("mwDynEval", "Set Root Path", None))
        self.miXplorer.setText(_translate("mwDynEval", "Xplorer", None))
        self.miXterm.setText(_translate("mwDynEval", "Xterm", None))
        self.miNamespace.setText(_translate("mwDynEval", "Namespace", None))

