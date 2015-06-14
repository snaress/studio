# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher2\ud\grapher.ui'
#
# Created: Sun Jun 14 01:33:25 2015
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
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gvGraphZone = QtGui.QGraphicsView(self.centralwidget)
        self.gvGraphZone.setObjectName(_fromUtf8("gvGraphZone"))
        self.horizontalLayout.addWidget(self.gvGraphZone)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        mwGrapher.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mwGrapher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.mWindow = QtGui.QMenu(self.menubar)
        self.mWindow.setObjectName(_fromUtf8("mWindow"))
        self.mToolBarOptions = QtGui.QMenu(self.mWindow)
        self.mToolBarOptions.setObjectName(_fromUtf8("mToolBarOptions"))
        self.mTools = QtGui.QMenu(self.mToolBarOptions)
        self.mTools.setObjectName(_fromUtf8("mTools"))
        self.mOrientation = QtGui.QMenu(self.mTools)
        self.mOrientation.setObjectName(_fromUtf8("mOrientation"))
        self.mHelp = QtGui.QMenu(self.menubar)
        self.mHelp.setObjectName(_fromUtf8("mHelp"))
        self.mEdit = QtGui.QMenu(self.menubar)
        self.mEdit.setObjectName(_fromUtf8("mEdit"))
        mwGrapher.setMenuBar(self.menubar)
        self.tbTools = QtGui.QToolBar(mwGrapher)
        self.tbTools.setObjectName(_fromUtf8("tbTools"))
        mwGrapher.addToolBar(QtCore.Qt.RightToolBarArea, self.tbTools)
        mwGrapher.insertToolBarBreak(self.tbTools)
        self.miNorth = QtGui.QAction(mwGrapher)
        self.miNorth.setObjectName(_fromUtf8("miNorth"))
        self.miSouth = QtGui.QAction(mwGrapher)
        self.miSouth.setObjectName(_fromUtf8("miSouth"))
        self.miWest = QtGui.QAction(mwGrapher)
        self.miWest.setObjectName(_fromUtf8("miWest"))
        self.miEast = QtGui.QAction(mwGrapher)
        self.miEast.setObjectName(_fromUtf8("miEast"))
        self.miConnectNodes = QtGui.QAction(mwGrapher)
        self.miConnectNodes.setObjectName(_fromUtf8("miConnectNodes"))
        self.mOrientation.addAction(self.miNorth)
        self.mOrientation.addAction(self.miSouth)
        self.mOrientation.addAction(self.miWest)
        self.mOrientation.addAction(self.miEast)
        self.mTools.addAction(self.mOrientation.menuAction())
        self.mToolBarOptions.addAction(self.mTools.menuAction())
        self.mWindow.addAction(self.mToolBarOptions.menuAction())
        self.mEdit.addAction(self.miConnectNodes)
        self.menubar.addAction(self.mEdit.menuAction())
        self.menubar.addAction(self.mWindow.menuAction())
        self.menubar.addAction(self.mHelp.menuAction())

        self.retranslateUi(mwGrapher)
        QtCore.QMetaObject.connectSlotsByName(mwGrapher)

    def retranslateUi(self, mwGrapher):
        mwGrapher.setWindowTitle(_translate("mwGrapher", "MainWindow", None))
        self.mWindow.setTitle(_translate("mwGrapher", "Window", None))
        self.mToolBarOptions.setTitle(_translate("mwGrapher", "ToolBar Options", None))
        self.mTools.setTitle(_translate("mwGrapher", "Tools", None))
        self.mOrientation.setTitle(_translate("mwGrapher", "Orientation", None))
        self.mHelp.setTitle(_translate("mwGrapher", "Help", None))
        self.mEdit.setTitle(_translate("mwGrapher", "Edit", None))
        self.tbTools.setWindowTitle(_translate("mwGrapher", "toolBar", None))
        self.miNorth.setText(_translate("mwGrapher", "North", None))
        self.miSouth.setText(_translate("mwGrapher", "South", None))
        self.miWest.setText(_translate("mwGrapher", "West", None))
        self.miEast.setText(_translate("mwGrapher", "East", None))
        self.miConnectNodes.setText(_translate("mwGrapher", "Connect Nodes", None))

