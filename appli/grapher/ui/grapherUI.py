# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\ud\grapher.ui'
#
# Created: Sun Jun 14 14:25:43 2015
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
        self.verticalLayoutWidget = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.vlTree = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vlTree.setMargin(0)
        self.vlTree.setObjectName(_fromUtf8("vlTree"))
        self.twTree = QtGui.QTreeWidget(self.verticalLayoutWidget)
        self.twTree.setObjectName(_fromUtf8("twTree"))
        self.twTree.headerItem().setText(0, _fromUtf8("1"))
        self.vlTree.addWidget(self.twTree)
        self.tabGraph = QtGui.QTabWidget(self.splitter)
        self.tabGraph.setObjectName(_fromUtf8("tabGraph"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        mwGrapher.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mwGrapher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.mWindow = QtGui.QMenu(self.menubar)
        self.mWindow.setObjectName(_fromUtf8("mWindow"))
        self.mToolsBarOrientation = QtGui.QMenu(self.mWindow)
        self.mToolsBarOrientation.setObjectName(_fromUtf8("mToolsBarOrientation"))
        self.mHelp = QtGui.QMenu(self.menubar)
        self.mHelp.setObjectName(_fromUtf8("mHelp"))
        self.mEdit = QtGui.QMenu(self.menubar)
        self.mEdit.setObjectName(_fromUtf8("mEdit"))
        mwGrapher.setMenuBar(self.menubar)
        self.tbTools = QtGui.QToolBar(mwGrapher)
        self.tbTools.setObjectName(_fromUtf8("tbTools"))
        mwGrapher.addToolBar(QtCore.Qt.RightToolBarArea, self.tbTools)
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
        self.miNorth = QtGui.QAction(mwGrapher)
        self.miNorth.setObjectName(_fromUtf8("miNorth"))
        self.miSouth = QtGui.QAction(mwGrapher)
        self.miSouth.setObjectName(_fromUtf8("miSouth"))
        self.miWest = QtGui.QAction(mwGrapher)
        self.miWest.setObjectName(_fromUtf8("miWest"))
        self.miEast = QtGui.QAction(mwGrapher)
        self.miEast.setObjectName(_fromUtf8("miEast"))
        self.miAddGraphZone = QtGui.QAction(mwGrapher)
        self.miAddGraphZone.setObjectName(_fromUtf8("miAddGraphZone"))
        self.mToolsBarOrientation.addAction(self.miNorth)
        self.mToolsBarOrientation.addAction(self.miSouth)
        self.mToolsBarOrientation.addAction(self.miWest)
        self.mToolsBarOrientation.addAction(self.miEast)
        self.mWindow.addAction(self.mToolsBarOrientation.menuAction())
        self.mEdit.addAction(self.miAddGraphZone)
        self.mEdit.addAction(self.miConnectNodes)
        self.menubar.addAction(self.mEdit.menuAction())
        self.menubar.addAction(self.mWindow.menuAction())
        self.menubar.addAction(self.mHelp.menuAction())

        self.retranslateUi(mwGrapher)
        self.tabGraph.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(mwGrapher)

    def retranslateUi(self, mwGrapher):
        mwGrapher.setWindowTitle(_translate("mwGrapher", "MainWindow", None))
        self.mWindow.setTitle(_translate("mwGrapher", "Window", None))
        self.mToolsBarOrientation.setTitle(_translate("mwGrapher", "Tools Bar Orientation", None))
        self.mHelp.setTitle(_translate("mwGrapher", "Help", None))
        self.mEdit.setTitle(_translate("mwGrapher", "Edit", None))
        self.tbTools.setWindowTitle(_translate("mwGrapher", "toolBar", None))
        self.miNorth2.setText(_translate("mwGrapher", "North", None))
        self.miSouth2.setText(_translate("mwGrapher", "South", None))
        self.miWest2.setText(_translate("mwGrapher", "West", None))
        self.miEast2.setText(_translate("mwGrapher", "East", None))
        self.miConnectNodes.setText(_translate("mwGrapher", "Connect Nodes", None))
        self.miNorth.setText(_translate("mwGrapher", "North", None))
        self.miSouth.setText(_translate("mwGrapher", "South", None))
        self.miWest.setText(_translate("mwGrapher", "West", None))
        self.miEast.setText(_translate("mwGrapher", "East", None))
        self.miAddGraphZone.setText(_translate("mwGrapher", "Add GraphZone", None))

