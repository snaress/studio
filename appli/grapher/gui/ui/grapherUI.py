# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\grapher.ui'
#
# Created: Mon Aug 24 01:17:13 2015
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
        mwGrapher.resize(800, 600)
        self.centralwidget = QtGui.QWidget(mwGrapher)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.vfGraphZone = QtGui.QFrame(self.splitter)
        self.vfGraphZone.setFrameShape(QtGui.QFrame.StyledPanel)
        self.vfGraphZone.setObjectName(_fromUtf8("vfGraphZone"))
        self.vlGraphZone = QtGui.QVBoxLayout(self.vfGraphZone)
        self.vlGraphZone.setSpacing(0)
        self.vlGraphZone.setMargin(0)
        self.vlGraphZone.setObjectName(_fromUtf8("vlGraphZone"))
        self.vfNodeEditor = QtGui.QFrame(self.splitter)
        self.vfNodeEditor.setFrameShape(QtGui.QFrame.StyledPanel)
        self.vfNodeEditor.setObjectName(_fromUtf8("vfNodeEditor"))
        self.vlNodeEditor = QtGui.QVBoxLayout(self.vfNodeEditor)
        self.vlNodeEditor.setSpacing(0)
        self.vlNodeEditor.setMargin(0)
        self.vlNodeEditor.setObjectName(_fromUtf8("vlNodeEditor"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        mwGrapher.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mwGrapher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuDisplay = QtGui.QMenu(self.menubar)
        self.menuDisplay.setObjectName(_fromUtf8("menuDisplay"))
        self.menuToolBarOptions = QtGui.QMenu(self.menuDisplay)
        self.menuToolBarOptions.setObjectName(_fromUtf8("menuToolBarOptions"))
        self.menuToolBarOrient = QtGui.QMenu(self.menuToolBarOptions)
        self.menuToolBarOrient.setObjectName(_fromUtf8("menuToolBarOrient"))
        self.menuToolTabOrient = QtGui.QMenu(self.menuToolBarOptions)
        self.menuToolTabOrient.setObjectName(_fromUtf8("menuToolTabOrient"))
        self.menuGraph = QtGui.QMenu(self.menubar)
        self.menuGraph.setObjectName(_fromUtf8("menuGraph"))
        mwGrapher.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mwGrapher)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mwGrapher.setStatusBar(self.statusbar)
        self.tbTools = QtGui.QToolBar(mwGrapher)
        self.tbTools.setFloatable(False)
        self.tbTools.setObjectName(_fromUtf8("tbTools"))
        mwGrapher.addToolBar(QtCore.Qt.LeftToolBarArea, self.tbTools)
        self.miToolsVisibility = QtGui.QAction(mwGrapher)
        self.miToolsVisibility.setCheckable(True)
        self.miToolsVisibility.setChecked(True)
        self.miToolsVisibility.setObjectName(_fromUtf8("miToolsVisibility"))
        self.miGraphScene = QtGui.QAction(mwGrapher)
        self.miGraphScene.setCheckable(True)
        self.miGraphScene.setObjectName(_fromUtf8("miGraphScene"))
        self.miNodeEditor = QtGui.QAction(mwGrapher)
        self.miNodeEditor.setCheckable(True)
        self.miNodeEditor.setObjectName(_fromUtf8("miNodeEditor"))
        self.miToolsIconOnly = QtGui.QAction(mwGrapher)
        self.miToolsIconOnly.setCheckable(True)
        self.miToolsIconOnly.setChecked(True)
        self.miToolsIconOnly.setObjectName(_fromUtf8("miToolsIconOnly"))
        self.miBarHorizontal = QtGui.QAction(mwGrapher)
        self.miBarHorizontal.setObjectName(_fromUtf8("miBarHorizontal"))
        self.miBarVertical = QtGui.QAction(mwGrapher)
        self.miBarVertical.setObjectName(_fromUtf8("miBarVertical"))
        self.miTabNorth = QtGui.QAction(mwGrapher)
        self.miTabNorth.setObjectName(_fromUtf8("miTabNorth"))
        self.miTabSouth = QtGui.QAction(mwGrapher)
        self.miTabSouth.setObjectName(_fromUtf8("miTabSouth"))
        self.miTabWest = QtGui.QAction(mwGrapher)
        self.miTabWest.setObjectName(_fromUtf8("miTabWest"))
        self.miTabEast = QtGui.QAction(mwGrapher)
        self.miTabEast.setObjectName(_fromUtf8("miTabEast"))
        self.menuToolBarOrient.addAction(self.miBarHorizontal)
        self.menuToolBarOrient.addAction(self.miBarVertical)
        self.menuToolTabOrient.addAction(self.miTabNorth)
        self.menuToolTabOrient.addAction(self.miTabSouth)
        self.menuToolTabOrient.addAction(self.miTabWest)
        self.menuToolTabOrient.addAction(self.miTabEast)
        self.menuToolBarOptions.addAction(self.menuToolBarOrient.menuAction())
        self.menuToolBarOptions.addAction(self.menuToolTabOrient.menuAction())
        self.menuToolBarOptions.addSeparator()
        self.menuToolBarOptions.addAction(self.miToolsIconOnly)
        self.menuDisplay.addAction(self.miToolsVisibility)
        self.menuDisplay.addAction(self.miNodeEditor)
        self.menuDisplay.addAction(self.miGraphScene)
        self.menuDisplay.addSeparator()
        self.menuDisplay.addAction(self.menuToolBarOptions.menuAction())
        self.menubar.addAction(self.menuGraph.menuAction())
        self.menubar.addAction(self.menuDisplay.menuAction())

        self.retranslateUi(mwGrapher)
        QtCore.QMetaObject.connectSlotsByName(mwGrapher)

    def retranslateUi(self, mwGrapher):
        mwGrapher.setWindowTitle(_translate("mwGrapher", "Grapher", None))
        self.menuDisplay.setTitle(_translate("mwGrapher", "Display", None))
        self.menuToolBarOptions.setTitle(_translate("mwGrapher", "Tool Bar Options", None))
        self.menuToolBarOrient.setTitle(_translate("mwGrapher", "Tool Bar Orient", None))
        self.menuToolTabOrient.setTitle(_translate("mwGrapher", "Tool Tab Orient", None))
        self.menuGraph.setTitle(_translate("mwGrapher", "Graph", None))
        self.tbTools.setWindowTitle(_translate("mwGrapher", "toolBar", None))
        self.miToolsVisibility.setText(_translate("mwGrapher", "Tools Bar", None))
        self.miGraphScene.setText(_translate("mwGrapher", "Graph Scene", None))
        self.miNodeEditor.setText(_translate("mwGrapher", "Node Editor", None))
        self.miToolsIconOnly.setText(_translate("mwGrapher", "Tools Icon Only", None))
        self.miBarHorizontal.setText(_translate("mwGrapher", "Horizontal", None))
        self.miBarVertical.setText(_translate("mwGrapher", "Vertical", None))
        self.miTabNorth.setText(_translate("mwGrapher", "North", None))
        self.miTabSouth.setText(_translate("mwGrapher", "South", None))
        self.miTabWest.setText(_translate("mwGrapher", "West", None))
        self.miTabEast.setText(_translate("mwGrapher", "East", None))

