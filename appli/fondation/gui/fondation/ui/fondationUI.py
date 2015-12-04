# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\fondation\gui\fondation\src\fondation.ui'
#
# Created: Fri Dec 04 04:04:26 2015
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

class Ui_mw_fondation(object):
    def setupUi(self, mw_fondation):
        mw_fondation.setObjectName(_fromUtf8("mw_fondation"))
        mw_fondation.resize(800, 600)
        self.centralwidget = QtGui.QWidget(mw_fondation)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 774, 487))
        self.page.setObjectName(_fromUtf8("page"))
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 774, 487))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.toolBox, 0, 1, 1, 1)
        mw_fondation.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mw_fondation)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.m_settings = QtGui.QMenu(self.menubar)
        self.m_settings.setObjectName(_fromUtf8("m_settings"))
        self.m_help = QtGui.QMenu(self.menubar)
        self.m_help.setObjectName(_fromUtf8("m_help"))
        self.m_project = QtGui.QMenu(self.menubar)
        self.m_project.setObjectName(_fromUtf8("m_project"))
        mw_fondation.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mw_fondation)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mw_fondation.setStatusBar(self.statusbar)
        self.mi_newProject = QtGui.QAction(mw_fondation)
        self.mi_newProject.setObjectName(_fromUtf8("mi_newProject"))
        self.mi_loadProject = QtGui.QAction(mw_fondation)
        self.mi_loadProject.setObjectName(_fromUtf8("mi_loadProject"))
        self.actionClose_Project = QtGui.QAction(mw_fondation)
        self.actionClose_Project.setObjectName(_fromUtf8("actionClose_Project"))
        self.actionQuit = QtGui.QAction(mw_fondation)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.mi_projectSettings = QtGui.QAction(mw_fondation)
        self.mi_projectSettings.setObjectName(_fromUtf8("mi_projectSettings"))
        self.mi_fondationSettings = QtGui.QAction(mw_fondation)
        self.mi_fondationSettings.setObjectName(_fromUtf8("mi_fondationSettings"))
        self.m_settings.addAction(self.mi_fondationSettings)
        self.m_settings.addAction(self.mi_projectSettings)
        self.m_project.addAction(self.mi_newProject)
        self.m_project.addAction(self.mi_loadProject)
        self.menubar.addAction(self.m_project.menuAction())
        self.menubar.addAction(self.m_settings.menuAction())
        self.menubar.addAction(self.m_help.menuAction())

        self.retranslateUi(mw_fondation)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mw_fondation)

    def retranslateUi(self, mw_fondation):
        mw_fondation.setWindowTitle(_translate("mw_fondation", "Fondation", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("mw_fondation", "Page 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("mw_fondation", "Page 2", None))
        self.m_settings.setTitle(_translate("mw_fondation", "Settings", None))
        self.m_help.setTitle(_translate("mw_fondation", "Help", None))
        self.m_project.setTitle(_translate("mw_fondation", "Project", None))
        self.mi_newProject.setText(_translate("mw_fondation", "New Project", None))
        self.mi_loadProject.setText(_translate("mw_fondation", "Load Project", None))
        self.actionClose_Project.setText(_translate("mw_fondation", "Close Project", None))
        self.actionQuit.setText(_translate("mw_fondation", "Quit", None))
        self.mi_projectSettings.setText(_translate("mw_fondation", "Project Settings", None))
        self.mi_fondationSettings.setText(_translate("mw_fondation", "Fondation Settings", None))

