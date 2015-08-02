# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\dynEval\ud\dynEval.ui'
#
# Created: Sat Aug 01 22:59:44 2015
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
        self.splitter_3 = QtGui.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.widget = QtGui.QWidget(self.splitter_2)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.vlSceneNodes = QtGui.QVBoxLayout(self.widget)
        self.vlSceneNodes.setSpacing(0)
        self.vlSceneNodes.setMargin(0)
        self.vlSceneNodes.setObjectName(_fromUtf8("vlSceneNodes"))
        self.widget1 = QtGui.QWidget(self.splitter_2)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.vlNodeOptions = QtGui.QVBoxLayout(self.widget1)
        self.vlNodeOptions.setSpacing(0)
        self.vlNodeOptions.setMargin(0)
        self.vlNodeOptions.setObjectName(_fromUtf8("vlNodeOptions"))
        self.splitter = QtGui.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget2 = QtGui.QWidget(self.splitter)
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.vlCaches = QtGui.QVBoxLayout(self.widget2)
        self.vlCaches.setSpacing(0)
        self.vlCaches.setMargin(0)
        self.vlCaches.setObjectName(_fromUtf8("vlCaches"))
        self.widget3 = QtGui.QWidget(self.splitter)
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.vlCacheInfo = QtGui.QVBoxLayout(self.widget3)
        self.vlCacheInfo.setSpacing(0)
        self.vlCacheInfo.setMargin(0)
        self.vlCacheInfo.setObjectName(_fromUtf8("vlCacheInfo"))
        self.gridLayout.addWidget(self.splitter_3, 0, 0, 1, 1)
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
        self.miRfDisplay = QtGui.QAction(mwDynEval)
        self.miRfDisplay.setCheckable(True)
        self.miRfDisplay.setObjectName(_fromUtf8("miRfDisplay"))
        self.mOptions.addAction(self.miToolTips)
        self.mOptions.addAction(self.miNamespace)
        self.mOptions.addAction(self.miRfDisplay)
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
        self.miRfDisplay.setText(_translate("mwDynEval", "Refresh Display", None))

