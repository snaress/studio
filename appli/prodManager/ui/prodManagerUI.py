# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\prodManager\ui\prodManager.ui'
#
# Created: Tue Feb 17 23:51:19 2015
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

class Ui_mwProdManager(object):
    def setupUi(self, mwProdManager):
        mwProdManager.setObjectName(_fromUtf8("mwProdManager"))
        mwProdManager.resize(800, 600)
        self.centralwidget = QtGui.QWidget(mwProdManager)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(300, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        mwProdManager.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mwProdManager)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuProject = QtGui.QMenu(self.menubar)
        self.menuProject.setObjectName(_fromUtf8("menuProject"))
        mwProdManager.setMenuBar(self.menubar)
        self.miNewProject = QtGui.QAction(mwProdManager)
        self.miNewProject.setObjectName(_fromUtf8("miNewProject"))
        self.miLoadProject = QtGui.QAction(mwProdManager)
        self.miLoadProject.setObjectName(_fromUtf8("miLoadProject"))
        self.miEditProject = QtGui.QAction(mwProdManager)
        self.miEditProject.setObjectName(_fromUtf8("miEditProject"))
        self.miUserPref = QtGui.QAction(mwProdManager)
        self.miUserPref.setObjectName(_fromUtf8("miUserPref"))
        self.miToolSettings = QtGui.QAction(mwProdManager)
        self.miToolSettings.setObjectName(_fromUtf8("miToolSettings"))
        self.miProjectSettings = QtGui.QAction(mwProdManager)
        self.miProjectSettings.setObjectName(_fromUtf8("miProjectSettings"))
        self.menuProject.addAction(self.miProjectSettings)
        self.menubar.addAction(self.menuProject.menuAction())

        self.retranslateUi(mwProdManager)
        QtCore.QMetaObject.connectSlotsByName(mwProdManager)

    def retranslateUi(self, mwProdManager):
        mwProdManager.setWindowTitle(_translate("mwProdManager", "ProdManager", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mwProdManager", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mwProdManager", "Tab 2", None))
        self.menuProject.setTitle(_translate("mwProdManager", "Project", None))
        self.miNewProject.setText(_translate("mwProdManager", "New Project", None))
        self.miLoadProject.setText(_translate("mwProdManager", "Load Project", None))
        self.miEditProject.setText(_translate("mwProdManager", "Edit Project", None))
        self.miUserPref.setText(_translate("mwProdManager", "User Pref", None))
        self.miToolSettings.setText(_translate("mwProdManager", "Tool Settings", None))
        self.miProjectSettings.setText(_translate("mwProdManager", "Project Settings", None))

