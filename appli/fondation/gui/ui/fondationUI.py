# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\fondation\gui\src\fondation.ui'
#
# Created: Thu Aug 13 21:57:24 2015
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

class Ui_mwFondation(object):
    def setupUi(self, mwFondation):
        mwFondation.setObjectName(_fromUtf8("mwFondation"))
        mwFondation.resize(714, 600)
        self.centralwidget = QtGui.QWidget(mwFondation)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vfGraphScene = QtGui.QFrame(self.centralwidget)
        self.vfGraphScene.setFrameShape(QtGui.QFrame.StyledPanel)
        self.vfGraphScene.setObjectName(_fromUtf8("vfGraphScene"))
        self.vlGraphScene = QtGui.QVBoxLayout(self.vfGraphScene)
        self.vlGraphScene.setSpacing(0)
        self.vlGraphScene.setMargin(0)
        self.vlGraphScene.setObjectName(_fromUtf8("vlGraphScene"))
        self.gridLayout.addWidget(self.vfGraphScene, 0, 0, 1, 1)
        mwFondation.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mwFondation)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 714, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.mGraph = QtGui.QMenu(self.menubar)
        self.mGraph.setObjectName(_fromUtf8("mGraph"))
        self.mCreateNode = QtGui.QMenu(self.mGraph)
        self.mCreateNode.setTearOffEnabled(True)
        self.mCreateNode.setObjectName(_fromUtf8("mCreateNode"))
        self.mFoldUnfold = QtGui.QMenu(self.mGraph)
        self.mFoldUnfold.setObjectName(_fromUtf8("mFoldUnfold"))
        self.mHideUnhide = QtGui.QMenu(self.mGraph)
        self.mHideUnhide.setObjectName(_fromUtf8("mHideUnhide"))
        self.mFiles = QtGui.QMenu(self.menubar)
        self.mFiles.setObjectName(_fromUtf8("mFiles"))
        self.mDisplay = QtGui.QMenu(self.menubar)
        self.mDisplay.setObjectName(_fromUtf8("mDisplay"))
        self.mToolsBarOrient = QtGui.QMenu(self.mDisplay)
        self.mToolsBarOrient.setObjectName(_fromUtf8("mToolsBarOrient"))
        self.mToolsTabOrient = QtGui.QMenu(self.mDisplay)
        self.mToolsTabOrient.setObjectName(_fromUtf8("mToolsTabOrient"))
        self.mPref = QtGui.QMenu(self.menubar)
        self.mPref.setObjectName(_fromUtf8("mPref"))
        mwFondation.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mwFondation)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mwFondation.setStatusBar(self.statusbar)
        self.tbTools = QtGui.QToolBar(mwFondation)
        self.tbTools.setMovable(True)
        self.tbTools.setFloatable(False)
        self.tbTools.setObjectName(_fromUtf8("tbTools"))
        mwFondation.addToolBar(QtCore.Qt.LeftToolBarArea, self.tbTools)
        self.miNewNode = QtGui.QAction(mwFondation)
        self.miNewNode.setObjectName(_fromUtf8("miNewNode"))
        self.miModul = QtGui.QAction(mwFondation)
        self.miModul.setObjectName(_fromUtf8("miModul"))
        self.miLoop = QtGui.QAction(mwFondation)
        self.miLoop.setObjectName(_fromUtf8("miLoop"))
        self.miSysData = QtGui.QAction(mwFondation)
        self.miSysData.setObjectName(_fromUtf8("miSysData"))
        self.miCmdData = QtGui.QAction(mwFondation)
        self.miCmdData.setObjectName(_fromUtf8("miCmdData"))
        self.miPyData = QtGui.QAction(mwFondation)
        self.miPyData.setObjectName(_fromUtf8("miPyData"))
        self.miWait = QtGui.QAction(mwFondation)
        self.miWait.setObjectName(_fromUtf8("miWait"))
        self.miUnselectAll = QtGui.QAction(mwFondation)
        self.miUnselectAll.setObjectName(_fromUtf8("miUnselectAll"))
        self.miToolsIconOnly = QtGui.QAction(mwFondation)
        self.miToolsIconOnly.setCheckable(True)
        self.miToolsIconOnly.setChecked(True)
        self.miToolsIconOnly.setObjectName(_fromUtf8("miToolsIconOnly"))
        self.miBarHorizontal = QtGui.QAction(mwFondation)
        self.miBarHorizontal.setObjectName(_fromUtf8("miBarHorizontal"))
        self.miBarVertical = QtGui.QAction(mwFondation)
        self.miBarVertical.setObjectName(_fromUtf8("miBarVertical"))
        self.miTabNorth = QtGui.QAction(mwFondation)
        self.miTabNorth.setObjectName(_fromUtf8("miTabNorth"))
        self.miTabSouth = QtGui.QAction(mwFondation)
        self.miTabSouth.setObjectName(_fromUtf8("miTabSouth"))
        self.miTabWest = QtGui.QAction(mwFondation)
        self.miTabWest.setObjectName(_fromUtf8("miTabWest"))
        self.miTabEast = QtGui.QAction(mwFondation)
        self.miTabEast.setObjectName(_fromUtf8("miTabEast"))
        self.miToolsVisibility = QtGui.QAction(mwFondation)
        self.miToolsVisibility.setCheckable(True)
        self.miToolsVisibility.setChecked(True)
        self.miToolsVisibility.setObjectName(_fromUtf8("miToolsVisibility"))
        self.miExpandAll = QtGui.QAction(mwFondation)
        self.miExpandAll.setObjectName(_fromUtf8("miExpandAll"))
        self.miCollapseAll = QtGui.QAction(mwFondation)
        self.miCollapseAll.setObjectName(_fromUtf8("miCollapseAll"))
        self.miExpandSel = QtGui.QAction(mwFondation)
        self.miExpandSel.setObjectName(_fromUtf8("miExpandSel"))
        self.miCollapseSel = QtGui.QAction(mwFondation)
        self.miCollapseSel.setObjectName(_fromUtf8("miCollapseSel"))
        self.miHideSel = QtGui.QAction(mwFondation)
        self.miHideSel.setObjectName(_fromUtf8("miHideSel"))
        self.miHideAll = QtGui.QAction(mwFondation)
        self.miHideAll.setObjectName(_fromUtf8("miHideAll"))
        self.miUnhideSel = QtGui.QAction(mwFondation)
        self.miUnhideSel.setObjectName(_fromUtf8("miUnhideSel"))
        self.miUnhideAll = QtGui.QAction(mwFondation)
        self.miUnhideAll.setObjectName(_fromUtf8("miUnhideAll"))
        self.mCreateNode.addAction(self.miNewNode)
        self.mCreateNode.addSeparator()
        self.mCreateNode.addAction(self.miModul)
        self.mCreateNode.addAction(self.miSysData)
        self.mCreateNode.addAction(self.miCmdData)
        self.mCreateNode.addAction(self.miPyData)
        self.mCreateNode.addSeparator()
        self.mCreateNode.addAction(self.miLoop)
        self.mCreateNode.addAction(self.miWait)
        self.mFoldUnfold.addAction(self.miExpandSel)
        self.mFoldUnfold.addAction(self.miExpandAll)
        self.mFoldUnfold.addAction(self.miCollapseSel)
        self.mFoldUnfold.addAction(self.miCollapseAll)
        self.mHideUnhide.addAction(self.miHideSel)
        self.mHideUnhide.addAction(self.miHideAll)
        self.mHideUnhide.addAction(self.miUnhideSel)
        self.mHideUnhide.addAction(self.miUnhideAll)
        self.mGraph.addAction(self.mCreateNode.menuAction())
        self.mGraph.addSeparator()
        self.mGraph.addAction(self.mFoldUnfold.menuAction())
        self.mGraph.addAction(self.mHideUnhide.menuAction())
        self.mGraph.addSeparator()
        self.mGraph.addAction(self.miUnselectAll)
        self.mToolsBarOrient.addAction(self.miBarHorizontal)
        self.mToolsBarOrient.addAction(self.miBarVertical)
        self.mToolsTabOrient.addAction(self.miTabNorth)
        self.mToolsTabOrient.addAction(self.miTabSouth)
        self.mToolsTabOrient.addAction(self.miTabWest)
        self.mToolsTabOrient.addAction(self.miTabEast)
        self.mDisplay.addAction(self.miToolsVisibility)
        self.mDisplay.addAction(self.mToolsBarOrient.menuAction())
        self.mDisplay.addAction(self.mToolsTabOrient.menuAction())
        self.mDisplay.addAction(self.miToolsIconOnly)
        self.menubar.addAction(self.mFiles.menuAction())
        self.menubar.addAction(self.mGraph.menuAction())
        self.menubar.addAction(self.mDisplay.menuAction())
        self.menubar.addAction(self.mPref.menuAction())

        self.retranslateUi(mwFondation)
        QtCore.QMetaObject.connectSlotsByName(mwFondation)

    def retranslateUi(self, mwFondation):
        mwFondation.setWindowTitle(_translate("mwFondation", "Fondation", None))
        self.mGraph.setTitle(_translate("mwFondation", "Graph", None))
        self.mCreateNode.setTitle(_translate("mwFondation", "Create Node", None))
        self.mFoldUnfold.setTitle(_translate("mwFondation", "Fold / Unfold", None))
        self.mHideUnhide.setTitle(_translate("mwFondation", "Hide / Unhide", None))
        self.mFiles.setTitle(_translate("mwFondation", "Files", None))
        self.mDisplay.setTitle(_translate("mwFondation", "Display", None))
        self.mToolsBarOrient.setTitle(_translate("mwFondation", "Tools Bar Orient", None))
        self.mToolsTabOrient.setTitle(_translate("mwFondation", "Tools Tab Orient", None))
        self.mPref.setTitle(_translate("mwFondation", "Pref", None))
        self.tbTools.setWindowTitle(_translate("mwFondation", "toolBar", None))
        self.miNewNode.setText(_translate("mwFondation", "New Node", None))
        self.miModul.setText(_translate("mwFondation", "Modul", None))
        self.miLoop.setText(_translate("mwFondation", "Loop", None))
        self.miSysData.setText(_translate("mwFondation", "SysData", None))
        self.miCmdData.setText(_translate("mwFondation", "CmdData", None))
        self.miPyData.setText(_translate("mwFondation", "PyData", None))
        self.miWait.setText(_translate("mwFondation", "Confition", None))
        self.miUnselectAll.setText(_translate("mwFondation", "Unselect All", None))
        self.miToolsIconOnly.setText(_translate("mwFondation", "Tools Icon Only", None))
        self.miBarHorizontal.setText(_translate("mwFondation", "Horizontal", None))
        self.miBarVertical.setText(_translate("mwFondation", "Vertical", None))
        self.miTabNorth.setText(_translate("mwFondation", "North", None))
        self.miTabSouth.setText(_translate("mwFondation", "South", None))
        self.miTabWest.setText(_translate("mwFondation", "West", None))
        self.miTabEast.setText(_translate("mwFondation", "East", None))
        self.miToolsVisibility.setText(_translate("mwFondation", "Tools Visibility", None))
        self.miExpandAll.setText(_translate("mwFondation", "Expand All", None))
        self.miCollapseAll.setText(_translate("mwFondation", "Collapse All", None))
        self.miExpandSel.setText(_translate("mwFondation", "Expand Sel", None))
        self.miCollapseSel.setText(_translate("mwFondation", "Collapse Sel", None))
        self.miHideSel.setText(_translate("mwFondation", "Hide Sel", None))
        self.miHideAll.setText(_translate("mwFondation", "Hide All", None))
        self.miUnhideSel.setText(_translate("mwFondation", "Unhide Sel", None))
        self.miUnhideAll.setText(_translate("mwFondation", "Unhide All", None))

