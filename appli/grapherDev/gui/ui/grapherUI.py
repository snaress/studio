# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\grapher.ui'
#
# Created: Sat Jul 18 12:53:57 2015
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

class Ui_mwGrapher(object):
    def setupUi(self, mwGrapher):
        mwGrapher.setObjectName(_fromUtf8("mwGrapher"))
        mwGrapher.resize(1000, 600)
        self.centralwidget = QtGui.QWidget(mwGrapher)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.qfProjectTree = QtGui.QFrame(self.splitter)
        self.qfProjectTree.setLineWidth(0)
        self.qfProjectTree.setObjectName(_fromUtf8("qfProjectTree"))
        self.vlProjectTree = QtGui.QVBoxLayout(self.qfProjectTree)
        self.vlProjectTree.setSpacing(0)
        self.vlProjectTree.setMargin(0)
        self.vlProjectTree.setObjectName(_fromUtf8("vlProjectTree"))
        self.tabGraph = QtGui.QTabWidget(self.splitter)
        self.tabGraph.setAcceptDrops(True)
        self.tabGraph.setTabsClosable(False)
        self.tabGraph.setMovable(True)
        self.tabGraph.setObjectName(_fromUtf8("tabGraph"))
        self.vfNodeData = QtGui.QFrame(self.splitter)
        self.vfNodeData.setObjectName(_fromUtf8("vfNodeData"))
        self.vlNodeData = QtGui.QVBoxLayout(self.vfNodeData)
        self.vlNodeData.setSpacing(0)
        self.vlNodeData.setMargin(0)
        self.vlNodeData.setObjectName(_fromUtf8("vlNodeData"))
        self.twNodeData = QtGui.QTreeWidget(self.vfNodeData)
        self.twNodeData.setMinimumSize(QtCore.QSize(300, 0))
        self.twNodeData.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.twNodeData.setIndentation(0)
        self.twNodeData.setExpandsOnDoubleClick(False)
        self.twNodeData.setObjectName(_fromUtf8("twNodeData"))
        self.twNodeData.headerItem().setText(0, _fromUtf8("1"))
        self.twNodeData.header().setVisible(False)
        self.vlNodeData.addWidget(self.twNodeData)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        mwGrapher.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mwGrapher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.mPref = QtGui.QMenu(self.menubar)
        self.mPref.setObjectName(_fromUtf8("mPref"))
        self.mToolsBar = QtGui.QMenu(self.mPref)
        self.mToolsBar.setTearOffEnabled(True)
        self.mToolsBar.setObjectName(_fromUtf8("mToolsBar"))
        self.mBarOrientation = QtGui.QMenu(self.mToolsBar)
        self.mBarOrientation.setObjectName(_fromUtf8("mBarOrientation"))
        self.mTabOrientation = QtGui.QMenu(self.mToolsBar)
        self.mTabOrientation.setObjectName(_fromUtf8("mTabOrientation"))
        self.mStyle = QtGui.QMenu(self.mPref)
        self.mStyle.setObjectName(_fromUtf8("mStyle"))
        self.mHelp = QtGui.QMenu(self.menubar)
        self.mHelp.setObjectName(_fromUtf8("mHelp"))
        self.mEdit = QtGui.QMenu(self.menubar)
        self.mEdit.setObjectName(_fromUtf8("mEdit"))
        self.mGrapher = QtGui.QMenu(self.menubar)
        self.mGrapher.setObjectName(_fromUtf8("mGrapher"))
        self.menuDisplay = QtGui.QMenu(self.menubar)
        self.menuDisplay.setObjectName(_fromUtf8("menuDisplay"))
        mwGrapher.setMenuBar(self.menubar)
        self.tbTools = QtGui.QToolBar(mwGrapher)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbTools.sizePolicy().hasHeightForWidth())
        self.tbTools.setSizePolicy(sizePolicy)
        self.tbTools.setObjectName(_fromUtf8("tbTools"))
        mwGrapher.addToolBar(QtCore.Qt.BottomToolBarArea, self.tbTools)
        self.miNorth2 = QtGui.QAction(mwGrapher)
        self.miNorth2.setObjectName(_fromUtf8("miNorth2"))
        self.miSouth2 = QtGui.QAction(mwGrapher)
        self.miSouth2.setObjectName(_fromUtf8("miSouth2"))
        self.miWest2 = QtGui.QAction(mwGrapher)
        self.miWest2.setObjectName(_fromUtf8("miWest2"))
        self.miEast2 = QtGui.QAction(mwGrapher)
        self.miEast2.setObjectName(_fromUtf8("miEast2"))
        self.miConnectNodes = QtGui.QAction(mwGrapher)
        self.miConnectNodes.setObjectName(_fromUtf8("miConnectNodes"))
        self.miTabNorth = QtGui.QAction(mwGrapher)
        self.miTabNorth.setObjectName(_fromUtf8("miTabNorth"))
        self.miTabSouth = QtGui.QAction(mwGrapher)
        self.miTabSouth.setObjectName(_fromUtf8("miTabSouth"))
        self.miTabWest = QtGui.QAction(mwGrapher)
        self.miTabWest.setObjectName(_fromUtf8("miTabWest"))
        self.miTabEast = QtGui.QAction(mwGrapher)
        self.miTabEast.setObjectName(_fromUtf8("miTabEast"))
        self.miAddGraphZone = QtGui.QAction(mwGrapher)
        self.miAddGraphZone.setObjectName(_fromUtf8("miAddGraphZone"))
        self.miBarHorizontal = QtGui.QAction(mwGrapher)
        self.miBarHorizontal.setObjectName(_fromUtf8("miBarHorizontal"))
        self.miBarVertical = QtGui.QAction(mwGrapher)
        self.miBarVertical.setObjectName(_fromUtf8("miBarVertical"))
        self.miDefaultStyle = QtGui.QAction(mwGrapher)
        self.miDefaultStyle.setObjectName(_fromUtf8("miDefaultStyle"))
        self.miDarkOrange = QtGui.QAction(mwGrapher)
        self.miDarkOrange.setObjectName(_fromUtf8("miDarkOrange"))
        self.miDarkGrey = QtGui.QAction(mwGrapher)
        self.miDarkGrey.setObjectName(_fromUtf8("miDarkGrey"))
        self.miRedGrey = QtGui.QAction(mwGrapher)
        self.miRedGrey.setObjectName(_fromUtf8("miRedGrey"))
        self.miShowToolBar = QtGui.QAction(mwGrapher)
        self.miShowToolBar.setObjectName(_fromUtf8("miShowToolBar"))
        self.miHideToolBar = QtGui.QAction(mwGrapher)
        self.miHideToolBar.setObjectName(_fromUtf8("miHideToolBar"))
        self.miToolBarVisibility = QtGui.QAction(mwGrapher)
        self.miToolBarVisibility.setCheckable(True)
        self.miToolBarVisibility.setChecked(True)
        self.miToolBarVisibility.setObjectName(_fromUtf8("miToolBarVisibility"))
        self.miDataVisibility = QtGui.QAction(mwGrapher)
        self.miDataVisibility.setCheckable(True)
        self.miDataVisibility.setChecked(True)
        self.miDataVisibility.setObjectName(_fromUtf8("miDataVisibility"))
        self.miPrintConnections = QtGui.QAction(mwGrapher)
        self.miPrintConnections.setObjectName(_fromUtf8("miPrintConnections"))
        self.miEditMode = QtGui.QAction(mwGrapher)
        self.miEditMode.setCheckable(True)
        self.miEditMode.setChecked(True)
        self.miEditMode.setObjectName(_fromUtf8("miEditMode"))
        self.miFitInSelection = QtGui.QAction(mwGrapher)
        self.miFitInSelection.setObjectName(_fromUtf8("miFitInSelection"))
        self.miNewProject = QtGui.QAction(mwGrapher)
        self.miNewProject.setObjectName(_fromUtf8("miNewProject"))
        self.miLoadProject = QtGui.QAction(mwGrapher)
        self.miLoadProject.setObjectName(_fromUtf8("miLoadProject"))
        self.miEditProject = QtGui.QAction(mwGrapher)
        self.miEditProject.setObjectName(_fromUtf8("miEditProject"))
        self.miFitInScene = QtGui.QAction(mwGrapher)
        self.miFitInScene.setObjectName(_fromUtf8("miFitInScene"))
        self.miTreeVisibility = QtGui.QAction(mwGrapher)
        self.miTreeVisibility.setCheckable(True)
        self.miTreeVisibility.setChecked(True)
        self.miTreeVisibility.setObjectName(_fromUtf8("miTreeVisibility"))
        self.miButtonIconOnly = QtGui.QAction(mwGrapher)
        self.miButtonIconOnly.setCheckable(True)
        self.miButtonIconOnly.setObjectName(_fromUtf8("miButtonIconOnly"))
        self.miSaveGraphAs = QtGui.QAction(mwGrapher)
        self.miSaveGraphAs.setObjectName(_fromUtf8("miSaveGraphAs"))
        self.miDelGraphZone = QtGui.QAction(mwGrapher)
        self.miDelGraphZone.setObjectName(_fromUtf8("miDelGraphZone"))
        self.mBarOrientation.addAction(self.miBarHorizontal)
        self.mBarOrientation.addAction(self.miBarVertical)
        self.mTabOrientation.addAction(self.miTabNorth)
        self.mTabOrientation.addAction(self.miTabSouth)
        self.mTabOrientation.addAction(self.miTabWest)
        self.mTabOrientation.addAction(self.miTabEast)
        self.mToolsBar.addAction(self.mBarOrientation.menuAction())
        self.mToolsBar.addAction(self.mTabOrientation.menuAction())
        self.mToolsBar.addAction(self.miButtonIconOnly)
        self.mStyle.addAction(self.miDefaultStyle)
        self.mStyle.addAction(self.miDarkOrange)
        self.mStyle.addAction(self.miDarkGrey)
        self.mStyle.addAction(self.miRedGrey)
        self.mPref.addAction(self.mStyle.menuAction())
        self.mPref.addSeparator()
        self.mPref.addAction(self.mToolsBar.menuAction())
        self.mHelp.addAction(self.miPrintConnections)
        self.mEdit.addAction(self.miAddGraphZone)
        self.mEdit.addAction(self.miDelGraphZone)
        self.mEdit.addAction(self.miEditMode)
        self.mEdit.addSeparator()
        self.mEdit.addAction(self.miConnectNodes)
        self.mGrapher.addAction(self.miLoadProject)
        self.mGrapher.addAction(self.miEditProject)
        self.mGrapher.addSeparator()
        self.mGrapher.addAction(self.miSaveGraphAs)
        self.menuDisplay.addAction(self.miTreeVisibility)
        self.menuDisplay.addAction(self.miDataVisibility)
        self.menuDisplay.addAction(self.miToolBarVisibility)
        self.menuDisplay.addAction(self.miFitInScene)
        self.menuDisplay.addAction(self.miFitInSelection)
        self.menubar.addAction(self.mGrapher.menuAction())
        self.menubar.addAction(self.mEdit.menuAction())
        self.menubar.addAction(self.menuDisplay.menuAction())
        self.menubar.addAction(self.mPref.menuAction())
        self.menubar.addAction(self.mHelp.menuAction())

        self.retranslateUi(mwGrapher)
        self.tabGraph.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(mwGrapher)

    def retranslateUi(self, mwGrapher):
        mwGrapher.setWindowTitle(_translate("mwGrapher", "Grapher", None))
        self.mPref.setTitle(_translate("mwGrapher", "Pref", None))
        self.mToolsBar.setTitle(_translate("mwGrapher", "Tools Bar", None))
        self.mBarOrientation.setTitle(_translate("mwGrapher", "Bar Orientation", None))
        self.mTabOrientation.setTitle(_translate("mwGrapher", "Tab Orientation", None))
        self.mStyle.setTitle(_translate("mwGrapher", "Style", None))
        self.mHelp.setTitle(_translate("mwGrapher", "Help", None))
        self.mEdit.setTitle(_translate("mwGrapher", "Edit", None))
        self.mGrapher.setTitle(_translate("mwGrapher", "Grapher", None))
        self.menuDisplay.setTitle(_translate("mwGrapher", "Display", None))
        self.tbTools.setWindowTitle(_translate("mwGrapher", "toolBar", None))
        self.miNorth2.setText(_translate("mwGrapher", "North", None))
        self.miSouth2.setText(_translate("mwGrapher", "South", None))
        self.miWest2.setText(_translate("mwGrapher", "West", None))
        self.miEast2.setText(_translate("mwGrapher", "East", None))
        self.miConnectNodes.setText(_translate("mwGrapher", "Connect Nodes", None))
        self.miTabNorth.setText(_translate("mwGrapher", "North", None))
        self.miTabSouth.setText(_translate("mwGrapher", "South", None))
        self.miTabWest.setText(_translate("mwGrapher", "West", None))
        self.miTabEast.setText(_translate("mwGrapher", "East", None))
        self.miAddGraphZone.setText(_translate("mwGrapher", "Add GraphZone", None))
        self.miBarHorizontal.setText(_translate("mwGrapher", "Horizontal", None))
        self.miBarVertical.setText(_translate("mwGrapher", "Vertical", None))
        self.miDefaultStyle.setText(_translate("mwGrapher", "Default", None))
        self.miDarkOrange.setText(_translate("mwGrapher", "Dark Orange", None))
        self.miDarkGrey.setText(_translate("mwGrapher", "Dark Grey", None))
        self.miRedGrey.setText(_translate("mwGrapher", "Red Grey", None))
        self.miShowToolBar.setText(_translate("mwGrapher", "Show", None))
        self.miHideToolBar.setText(_translate("mwGrapher", "Hide", None))
        self.miToolBarVisibility.setText(_translate("mwGrapher", "ToolBar Visibility", None))
        self.miDataVisibility.setText(_translate("mwGrapher", "Data Visibility", None))
        self.miPrintConnections.setText(_translate("mwGrapher", "Print Sel Connections", None))
        self.miEditMode.setText(_translate("mwGrapher", "Edit Mode", None))
        self.miFitInSelection.setText(_translate("mwGrapher", "Fit In Selection", None))
        self.miNewProject.setText(_translate("mwGrapher", "New Project", None))
        self.miLoadProject.setText(_translate("mwGrapher", "Load Project", None))
        self.miEditProject.setText(_translate("mwGrapher", "Edit Project", None))
        self.miFitInScene.setText(_translate("mwGrapher", "Fit In Scene", None))
        self.miTreeVisibility.setText(_translate("mwGrapher", "Tree Visibility", None))
        self.miButtonIconOnly.setText(_translate("mwGrapher", "Button Icon Only", None))
        self.miSaveGraphAs.setText(_translate("mwGrapher", "Save Graph As", None))
        self.miDelGraphZone.setText(_translate("mwGrapher", "Delete GraphZone", None))
