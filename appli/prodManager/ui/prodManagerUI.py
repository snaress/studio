# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\prodManager\ui\prodManager.ui'
#
# Created: Wed Mar 18 22:14:16 2015
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
        self.hlProdManager = QtGui.QHBoxLayout()
        self.hlProdManager.setObjectName(_fromUtf8("hlProdManager"))
        self.qfLeftUi = QtGui.QFrame(self.centralwidget)
        self.qfLeftUi.setMinimumSize(QtCore.QSize(300, 0))
        self.qfLeftUi.setMaximumSize(QtCore.QSize(300, 16777215))
        self.qfLeftUi.setFrameShape(QtGui.QFrame.Box)
        self.qfLeftUi.setObjectName(_fromUtf8("qfLeftUi"))
        self.vlLeftUi = QtGui.QVBoxLayout(self.qfLeftUi)
        self.vlLeftUi.setSpacing(0)
        self.vlLeftUi.setMargin(0)
        self.vlLeftUi.setObjectName(_fromUtf8("vlLeftUi"))
        self.hlProdManager.addWidget(self.qfLeftUi)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.hlProdManager.addWidget(self.line)
        self.tabProdManager = QtGui.QTabWidget(self.centralwidget)
        self.tabProdManager.setObjectName(_fromUtf8("tabProdManager"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabProdManager.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabProdManager.addTab(self.tab_2, _fromUtf8(""))
        self.hlProdManager.addWidget(self.tabProdManager)
        self.gridLayout.addLayout(self.hlProdManager, 0, 0, 1, 1)
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
        self.tabProdManager.setTabText(self.tabProdManager.indexOf(self.tab), _translate("mwProdManager", "Tab 1", None))
        self.tabProdManager.setTabText(self.tabProdManager.indexOf(self.tab_2), _translate("mwProdManager", "Tab 2", None))
        self.menuProject.setTitle(_translate("mwProdManager", "Project", None))
        self.miNewProject.setText(_translate("mwProdManager", "New Project", None))
        self.miLoadProject.setText(_translate("mwProdManager", "Load Project", None))
        self.miEditProject.setText(_translate("mwProdManager", "Edit Project", None))
        self.miUserPref.setText(_translate("mwProdManager", "User Pref", None))
        self.miToolSettings.setText(_translate("mwProdManager", "Tool Settings", None))
        self.miProjectSettings.setText(_translate("mwProdManager", "Project Settings", None))

