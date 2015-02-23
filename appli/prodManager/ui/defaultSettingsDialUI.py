# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\prodManager\ui\defaultSettingsDial.ui'
#
# Created: Mon Feb 23 01:56:37 2015
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

class Ui_settingsItem(object):
    def setupUi(self, settingsItem):
        settingsItem.setObjectName(_fromUtf8("settingsItem"))
        settingsItem.resize(400, 123)
        self.gridLayout = QtGui.QGridLayout(settingsItem)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 2, 0, 2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.qfRootPath = QtGui.QFrame(settingsItem)
        self.qfRootPath.setObjectName(_fromUtf8("qfRootPath"))
        self.hlRootPath = QtGui.QHBoxLayout(self.qfRootPath)
        self.hlRootPath.setSpacing(2)
        self.hlRootPath.setObjectName(_fromUtf8("hlRootPath"))
        self.lPath = QtGui.QLabel(self.qfRootPath)
        self.lPath.setMinimumSize(QtCore.QSize(60, 0))
        self.lPath.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lPath.setObjectName(_fromUtf8("lPath"))
        self.hlRootPath.addWidget(self.lPath)
        self.lePath = QtGui.QLineEdit(self.qfRootPath)
        self.lePath.setObjectName(_fromUtf8("lePath"))
        self.hlRootPath.addWidget(self.lePath)
        self.pbOpen = QtGui.QPushButton(self.qfRootPath)
        self.pbOpen.setObjectName(_fromUtf8("pbOpen"))
        self.hlRootPath.addWidget(self.pbOpen)
        self.gridLayout.addWidget(self.qfRootPath, 0, 0, 1, 1)
        self.qfTask = QtGui.QFrame(settingsItem)
        self.qfTask.setObjectName(_fromUtf8("qfTask"))
        self.flTask = QtGui.QFormLayout(self.qfTask)
        self.flTask.setSpacing(2)
        self.flTask.setObjectName(_fromUtf8("flTask"))
        self.lName = QtGui.QLabel(self.qfTask)
        self.lName.setMinimumSize(QtCore.QSize(60, 0))
        self.lName.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lName.setObjectName(_fromUtf8("lName"))
        self.flTask.setWidget(0, QtGui.QFormLayout.LabelRole, self.lName)
        self.leName = QtGui.QLineEdit(self.qfTask)
        self.leName.setObjectName(_fromUtf8("leName"))
        self.flTask.setWidget(0, QtGui.QFormLayout.FieldRole, self.leName)
        self.lLabel = QtGui.QLabel(self.qfTask)
        self.lLabel.setMinimumSize(QtCore.QSize(60, 0))
        self.lLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lLabel.setObjectName(_fromUtf8("lLabel"))
        self.flTask.setWidget(1, QtGui.QFormLayout.LabelRole, self.lLabel)
        self.leLabel = QtGui.QLineEdit(self.qfTask)
        self.leLabel.setObjectName(_fromUtf8("leLabel"))
        self.flTask.setWidget(1, QtGui.QFormLayout.FieldRole, self.leLabel)
        self.gridLayout.addWidget(self.qfTask, 1, 0, 1, 1)
        self.qfTreeName = QtGui.QFrame(settingsItem)
        self.qfTreeName.setObjectName(_fromUtf8("qfTreeName"))
        self.hlTreeName = QtGui.QHBoxLayout(self.qfTreeName)
        self.hlTreeName.setSpacing(2)
        self.hlTreeName.setObjectName(_fromUtf8("hlTreeName"))
        self.lTreeName = QtGui.QLabel(self.qfTreeName)
        self.lTreeName.setMinimumSize(QtCore.QSize(60, 0))
        self.lTreeName.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lTreeName.setObjectName(_fromUtf8("lTreeName"))
        self.hlTreeName.addWidget(self.lTreeName)
        self.leTreeName = QtGui.QLineEdit(self.qfTreeName)
        self.leTreeName.setObjectName(_fromUtf8("leTreeName"))
        self.hlTreeName.addWidget(self.leTreeName)
        self.cbTreeType = QtGui.QComboBox(self.qfTreeName)
        self.cbTreeType.setObjectName(_fromUtf8("cbTreeType"))
        self.hlTreeName.addWidget(self.cbTreeType)
        self.gridLayout.addWidget(self.qfTreeName, 2, 0, 1, 1)
        self.line = QtGui.QFrame(settingsItem)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.hlConfirm = QtGui.QHBoxLayout()
        self.hlConfirm.setSpacing(2)
        self.hlConfirm.setObjectName(_fromUtf8("hlConfirm"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlConfirm.addItem(spacerItem)
        self.pbAdd = QtGui.QPushButton(settingsItem)
        self.pbAdd.setObjectName(_fromUtf8("pbAdd"))
        self.hlConfirm.addWidget(self.pbAdd)
        self.pbCancel = QtGui.QPushButton(settingsItem)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.hlConfirm.addWidget(self.pbCancel)
        self.gridLayout.addLayout(self.hlConfirm, 4, 0, 1, 1)

        self.retranslateUi(settingsItem)
        QtCore.QMetaObject.connectSlotsByName(settingsItem)

    def retranslateUi(self, settingsItem):
        settingsItem.setWindowTitle(_translate("settingsItem", "SettingsItem", None))
        self.lPath.setText(_translate("settingsItem", "Root Path: ", None))
        self.pbOpen.setText(_translate("settingsItem", "Open", None))
        self.lName.setText(_translate("settingsItem", "Task Name: ", None))
        self.lLabel.setText(_translate("settingsItem", "Task Label: ", None))
        self.lTreeName.setText(_translate("settingsItem", "Tree Name: ", None))
        self.pbAdd.setText(_translate("settingsItem", "Add", None))
        self.pbCancel.setText(_translate("settingsItem", "Cancel", None))

