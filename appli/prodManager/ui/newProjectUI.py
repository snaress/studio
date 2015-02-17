# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\prodManager\ui\newProject.ui'
#
# Created: Sun Feb 15 03:33:19 2015
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

class Ui_newProject(object):
    def setupUi(self, newProject):
        newProject.setObjectName(_fromUtf8("newProject"))
        newProject.resize(465, 136)
        self.gridLayout_2 = QtGui.QGridLayout(newProject)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(1)
        self.gridLayout.setContentsMargins(2, -1, 2, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lProjectType = QtGui.QLabel(newProject)
        self.lProjectType.setMaximumSize(QtCore.QSize(95, 16777215))
        self.lProjectType.setObjectName(_fromUtf8("lProjectType"))
        self.gridLayout.addWidget(self.lProjectType, 0, 0, 1, 1)
        self.cbProjectType = QtGui.QComboBox(newProject)
        self.cbProjectType.setMaximumSize(QtCore.QSize(80, 16777215))
        self.cbProjectType.setObjectName(_fromUtf8("cbProjectType"))
        self.cbProjectType.addItem(_fromUtf8(""))
        self.cbProjectType.addItem(_fromUtf8(""))
        self.cbProjectType.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cbProjectType, 0, 1, 1, 1)
        self.lProjectName = QtGui.QLabel(newProject)
        self.lProjectName.setMaximumSize(QtCore.QSize(95, 16777215))
        self.lProjectName.setObjectName(_fromUtf8("lProjectName"))
        self.gridLayout.addWidget(self.lProjectName, 1, 0, 1, 1)
        self.leProjectName = QtGui.QLineEdit(newProject)
        self.leProjectName.setMinimumSize(QtCore.QSize(250, 0))
        self.leProjectName.setObjectName(_fromUtf8("leProjectName"))
        self.gridLayout.addWidget(self.leProjectName, 1, 1, 1, 1)
        self.lProjectAlias = QtGui.QLabel(newProject)
        self.lProjectAlias.setMaximumSize(QtCore.QSize(95, 16777215))
        self.lProjectAlias.setObjectName(_fromUtf8("lProjectAlias"))
        self.gridLayout.addWidget(self.lProjectAlias, 2, 0, 1, 1)
        self.leProjectAlias = QtGui.QLineEdit(newProject)
        self.leProjectAlias.setMinimumSize(QtCore.QSize(250, 0))
        self.leProjectAlias.setObjectName(_fromUtf8("leProjectAlias"))
        self.gridLayout.addWidget(self.leProjectAlias, 2, 1, 1, 1)
        self.lProjectSeason = QtGui.QLabel(newProject)
        self.lProjectSeason.setMaximumSize(QtCore.QSize(95, 16777215))
        self.lProjectSeason.setObjectName(_fromUtf8("lProjectSeason"))
        self.gridLayout.addWidget(self.lProjectSeason, 3, 0, 1, 1)
        self.leProjectSeason = QtGui.QLineEdit(newProject)
        self.leProjectSeason.setMinimumSize(QtCore.QSize(250, 0))
        self.leProjectSeason.setObjectName(_fromUtf8("leProjectSeason"))
        self.gridLayout.addWidget(self.leProjectSeason, 3, 1, 1, 1)
        self.lProjectEpisode = QtGui.QLabel(newProject)
        self.lProjectEpisode.setMaximumSize(QtCore.QSize(95, 16777215))
        self.lProjectEpisode.setObjectName(_fromUtf8("lProjectEpisode"))
        self.gridLayout.addWidget(self.lProjectEpisode, 4, 0, 1, 1)
        self.leProjectEpisode = QtGui.QLineEdit(newProject)
        self.leProjectEpisode.setMinimumSize(QtCore.QSize(250, 0))
        self.leProjectEpisode.setObjectName(_fromUtf8("leProjectEpisode"))
        self.gridLayout.addWidget(self.leProjectEpisode, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.line = QtGui.QFrame(newProject)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(2, -1, 2, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbAccept = QtGui.QPushButton(newProject)
        self.pbAccept.setObjectName(_fromUtf8("pbAccept"))
        self.horizontalLayout.addWidget(self.pbAccept)
        self.pbCancel = QtGui.QPushButton(newProject)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.horizontalLayout.addWidget(self.pbCancel)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(newProject)
        QtCore.QMetaObject.connectSlotsByName(newProject)

    def retranslateUi(self, newProject):
        newProject.setWindowTitle(_translate("newProject", "New Project", None))
        self.lProjectType.setText(_translate("newProject", "Project Type :", None))
        self.cbProjectType.setItemText(0, _translate("newProject", "Movie", None))
        self.cbProjectType.setItemText(1, _translate("newProject", "Marketing", None))
        self.cbProjectType.setItemText(2, _translate("newProject", "Serie", None))
        self.lProjectName.setText(_translate("newProject", "Project Name :", None))
        self.lProjectAlias.setText(_translate("newProject", "Project Alias :", None))
        self.lProjectSeason.setText(_translate("newProject", "Project Season :", None))
        self.lProjectEpisode.setText(_translate("newProject", "Project Episode :", None))
        self.pbAccept.setText(_translate("newProject", "Accept", None))
        self.pbCancel.setText(_translate("newProject", "Cancel", None))

