# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgProjectLoad.ui'
#
# Created: Fri Jun 26 01:04:28 2015
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

class Ui_wgLoadProject(object):
    def setupUi(self, wgLoadProject):
        wgLoadProject.setObjectName(_fromUtf8("wgLoadProject"))
        wgLoadProject.resize(250, 249)
        self.gridLayout = QtGui.QGridLayout(wgLoadProject)
        self.gridLayout.setContentsMargins(2, 1, 1, 1)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cbNewProject = QtGui.QCheckBox(wgLoadProject)
        self.cbNewProject.setObjectName(_fromUtf8("cbNewProject"))
        self.gridLayout.addWidget(self.cbNewProject, 0, 0, 1, 1)
        self.qfNewProject = QtGui.QFrame(wgLoadProject)
        self.qfNewProject.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qfNewProject.setLineWidth(1)
        self.qfNewProject.setObjectName(_fromUtf8("qfNewProject"))
        self.glNewProject = QtGui.QGridLayout(self.qfNewProject)
        self.glNewProject.setContentsMargins(2, 1, 2, 1)
        self.glNewProject.setHorizontalSpacing(2)
        self.glNewProject.setVerticalSpacing(1)
        self.glNewProject.setObjectName(_fromUtf8("glNewProject"))
        self.leProjectName = QtGui.QLineEdit(self.qfNewProject)
        self.leProjectName.setObjectName(_fromUtf8("leProjectName"))
        self.glNewProject.addWidget(self.leProjectName, 0, 1, 1, 1)
        self.lProjectAlias = QtGui.QLabel(self.qfNewProject)
        self.lProjectAlias.setObjectName(_fromUtf8("lProjectAlias"))
        self.glNewProject.addWidget(self.lProjectAlias, 1, 0, 1, 1)
        self.lProjectName = QtGui.QLabel(self.qfNewProject)
        self.lProjectName.setObjectName(_fromUtf8("lProjectName"))
        self.glNewProject.addWidget(self.lProjectName, 0, 0, 1, 1)
        self.leProjectAlias = QtGui.QLineEdit(self.qfNewProject)
        self.leProjectAlias.setObjectName(_fromUtf8("leProjectAlias"))
        self.glNewProject.addWidget(self.leProjectAlias, 1, 1, 1, 1)
        self.line = QtGui.QFrame(self.qfNewProject)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.glNewProject.addWidget(self.line, 2, 0, 1, 2)
        self.hlButtons = QtGui.QHBoxLayout()
        self.hlButtons.setSpacing(0)
        self.hlButtons.setObjectName(_fromUtf8("hlButtons"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlButtons.addItem(spacerItem)
        self.pbCreate = QtGui.QPushButton(self.qfNewProject)
        self.pbCreate.setObjectName(_fromUtf8("pbCreate"))
        self.hlButtons.addWidget(self.pbCreate)
        self.pbCancel = QtGui.QPushButton(self.qfNewProject)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.hlButtons.addWidget(self.pbCancel)
        self.glNewProject.addLayout(self.hlButtons, 3, 0, 1, 2)
        self.gridLayout.addWidget(self.qfNewProject, 1, 0, 1, 1)
        self.twProjects = QtGui.QTreeWidget(wgLoadProject)
        self.twProjects.setIndentation(2)
        self.twProjects.setItemsExpandable(False)
        self.twProjects.setExpandsOnDoubleClick(False)
        self.twProjects.setObjectName(_fromUtf8("twProjects"))
        self.twProjects.headerItem().setText(0, _fromUtf8("1"))
        self.twProjects.header().setVisible(False)
        self.gridLayout.addWidget(self.twProjects, 2, 0, 1, 1)

        self.retranslateUi(wgLoadProject)
        QtCore.QMetaObject.connectSlotsByName(wgLoadProject)

    def retranslateUi(self, wgLoadProject):
        wgLoadProject.setWindowTitle(_translate("wgLoadProject", "Load Project", None))
        self.cbNewProject.setText(_translate("wgLoadProject", "New Project", None))
        self.lProjectAlias.setText(_translate("wgLoadProject", "Project Alias :", None))
        self.lProjectName.setText(_translate("wgLoadProject", "Project Name :", None))
        self.pbCreate.setText(_translate("wgLoadProject", "Create", None))
        self.pbCancel.setText(_translate("wgLoadProject", "Cancel", None))

