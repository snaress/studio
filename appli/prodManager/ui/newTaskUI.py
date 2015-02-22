# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\prodManager\ui\newTask.ui'
#
# Created: Sun Feb 22 05:22:54 2015
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

class Ui_newTask(object):
    def setupUi(self, newTask):
        newTask.setObjectName(_fromUtf8("newTask"))
        newTask.resize(328, 72)
        self.gridLayout = QtGui.QGridLayout(newTask)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(2, 0, 2, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lName = QtGui.QLabel(newTask)
        self.lName.setMinimumSize(QtCore.QSize(60, 0))
        self.lName.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lName.setObjectName(_fromUtf8("lName"))
        self.horizontalLayout.addWidget(self.lName)
        self.leName = QtGui.QLineEdit(newTask)
        self.leName.setObjectName(_fromUtf8("leName"))
        self.horizontalLayout.addWidget(self.leName)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lLabel = QtGui.QLabel(newTask)
        self.lLabel.setMinimumSize(QtCore.QSize(60, 0))
        self.lLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lLabel.setObjectName(_fromUtf8("lLabel"))
        self.horizontalLayout_2.addWidget(self.lLabel)
        self.leLabel = QtGui.QLineEdit(newTask)
        self.leLabel.setObjectName(_fromUtf8("leLabel"))
        self.horizontalLayout_2.addWidget(self.leLabel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.line = QtGui.QFrame(newTask)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pbAdd = QtGui.QPushButton(newTask)
        self.pbAdd.setObjectName(_fromUtf8("pbAdd"))
        self.horizontalLayout_3.addWidget(self.pbAdd)
        self.pbCancel = QtGui.QPushButton(newTask)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.horizontalLayout_3.addWidget(self.pbCancel)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.retranslateUi(newTask)
        QtCore.QMetaObject.connectSlotsByName(newTask)

    def retranslateUi(self, newTask):
        newTask.setWindowTitle(_translate("newTask", "New Task", None))
        self.lName.setText(_translate("newTask", "Task Name: ", None))
        self.lLabel.setText(_translate("newTask", "Task Label: ", None))
        self.pbAdd.setText(_translate("newTask", "Add", None))
        self.pbCancel.setText(_translate("newTask", "Cancel", None))

