# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\prodManager\ui\settings.ui'
#
# Created: Sun Feb 15 02:53:58 2015
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

class Ui_mwSettings(object):
    def setupUi(self, mwSettings):
        mwSettings.setObjectName(_fromUtf8("mwSettings"))
        mwSettings.resize(506, 288)
        self.centralwidget = QtGui.QWidget(mwSettings)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setMargin(1)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.qfNewProject = QtGui.QFrame(self.centralwidget)
        self.qfNewProject.setFrameShape(QtGui.QFrame.Box)
        self.qfNewProject.setObjectName(_fromUtf8("qfNewProject"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.qfNewProject)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.leProjectName = QtGui.QLineEdit(self.qfNewProject)
        self.leProjectName.setMinimumSize(QtCore.QSize(250, 0))
        self.leProjectName.setObjectName(_fromUtf8("leProjectName"))
        self.gridLayout.addWidget(self.leProjectName, 0, 1, 1, 1)
        self.lProjectName = QtGui.QLabel(self.qfNewProject)
        self.lProjectName.setMaximumSize(QtCore.QSize(95, 16777215))
        self.lProjectName.setObjectName(_fromUtf8("lProjectName"))
        self.gridLayout.addWidget(self.lProjectName, 0, 0, 1, 1)
        self.lProjectAlias = QtGui.QLabel(self.qfNewProject)
        self.lProjectAlias.setMaximumSize(QtCore.QSize(95, 16777215))
        self.lProjectAlias.setObjectName(_fromUtf8("lProjectAlias"))
        self.gridLayout.addWidget(self.lProjectAlias, 1, 0, 1, 1)
        self.leProjectAlias = QtGui.QLineEdit(self.qfNewProject)
        self.leProjectAlias.setMinimumSize(QtCore.QSize(250, 0))
        self.leProjectAlias.setObjectName(_fromUtf8("leProjectAlias"))
        self.gridLayout.addWidget(self.leProjectAlias, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.pbCreate = QtGui.QPushButton(self.qfNewProject)
        self.pbCreate.setMinimumSize(QtCore.QSize(0, 44))
        self.pbCreate.setObjectName(_fromUtf8("pbCreate"))
        self.horizontalLayout.addWidget(self.pbCreate)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.qfNewProject, 0, 0, 1, 1)
        self.qfSettings = QtGui.QFrame(self.centralwidget)
        self.qfSettings.setFrameShape(QtGui.QFrame.Box)
        self.qfSettings.setObjectName(_fromUtf8("qfSettings"))
        self.hlSettings = QtGui.QHBoxLayout(self.qfSettings)
        self.hlSettings.setSpacing(1)
        self.hlSettings.setMargin(0)
        self.hlSettings.setObjectName(_fromUtf8("hlSettings"))
        self.twSettings = QtGui.QTreeWidget(self.qfSettings)
        self.twSettings.setMaximumSize(QtCore.QSize(200, 16777215))
        self.twSettings.setIndentation(2)
        self.twSettings.setItemsExpandable(False)
        self.twSettings.setExpandsOnDoubleClick(False)
        self.twSettings.setObjectName(_fromUtf8("twSettings"))
        self.twSettings.headerItem().setText(0, _fromUtf8("1"))
        self.twSettings.header().setVisible(False)
        self.hlSettings.addWidget(self.twSettings)
        self.vlSettings = QtGui.QVBoxLayout()
        self.vlSettings.setSpacing(0)
        self.vlSettings.setObjectName(_fromUtf8("vlSettings"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlSettings.addItem(spacerItem1)
        self.hlSettings.addLayout(self.vlSettings)
        self.gridLayout_2.addWidget(self.qfSettings, 1, 0, 1, 1)
        mwSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(mwSettings)
        QtCore.QMetaObject.connectSlotsByName(mwSettings)

    def retranslateUi(self, mwSettings):
        mwSettings.setWindowTitle(_translate("mwSettings", "Settings", None))
        self.lProjectName.setText(_translate("mwSettings", "Project Name :", None))
        self.lProjectAlias.setText(_translate("mwSettings", "Project Alias :", None))
        self.pbCreate.setText(_translate("mwSettings", "Create", None))

