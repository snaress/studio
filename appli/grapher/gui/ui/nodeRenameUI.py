# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\nodeRename.ui'
#
# Created: Fri Sep 18 00:47:12 2015
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

class Ui_dialNodeRename(object):
    def setupUi(self, dialNodeRename):
        dialNodeRename.setObjectName(_fromUtf8("dialNodeRename"))
        dialNodeRename.resize(506, 94)
        self.gridLayout = QtGui.QGridLayout(dialNodeRename)
        self.gridLayout.setMargin(2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line = QtGui.QFrame(dialNodeRename)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 4, 0, 1, 1)
        self.hlNewName = QtGui.QHBoxLayout()
        self.hlNewName.setObjectName(_fromUtf8("hlNewName"))
        self.lNewName = QtGui.QLabel(dialNodeRename)
        self.lNewName.setMinimumSize(QtCore.QSize(70, 0))
        self.lNewName.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lNewName.setObjectName(_fromUtf8("lNewName"))
        self.hlNewName.addWidget(self.lNewName)
        self.leNewName = QtGui.QLineEdit(dialNodeRename)
        self.leNewName.setObjectName(_fromUtf8("leNewName"))
        self.hlNewName.addWidget(self.leNewName)
        self.gridLayout.addLayout(self.hlNewName, 2, 0, 1, 1)
        self.hlResult = QtGui.QHBoxLayout()
        self.hlResult.setObjectName(_fromUtf8("hlResult"))
        self.lResult = QtGui.QLabel(dialNodeRename)
        self.lResult.setMinimumSize(QtCore.QSize(70, 0))
        self.lResult.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lResult.setObjectName(_fromUtf8("lResult"))
        self.hlResult.addWidget(self.lResult)
        self.lResultVal = QtGui.QLabel(dialNodeRename)
        self.lResultVal.setText(_fromUtf8(""))
        self.lResultVal.setObjectName(_fromUtf8("lResultVal"))
        self.hlResult.addWidget(self.lResultVal)
        self.gridLayout.addLayout(self.hlResult, 3, 0, 1, 1)
        self.hlButtons = QtGui.QHBoxLayout()
        self.hlButtons.setSpacing(2)
        self.hlButtons.setObjectName(_fromUtf8("hlButtons"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlButtons.addItem(spacerItem)
        self.pbOk = QtGui.QPushButton(dialNodeRename)
        self.pbOk.setMinimumSize(QtCore.QSize(50, 20))
        self.pbOk.setMaximumSize(QtCore.QSize(50, 20))
        self.pbOk.setObjectName(_fromUtf8("pbOk"))
        self.hlButtons.addWidget(self.pbOk)
        self.pbCancel = QtGui.QPushButton(dialNodeRename)
        self.pbCancel.setMinimumSize(QtCore.QSize(50, 20))
        self.pbCancel.setMaximumSize(QtCore.QSize(50, 20))
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.hlButtons.addWidget(self.pbCancel)
        self.gridLayout.addLayout(self.hlButtons, 5, 0, 1, 1)
        self.hlCurrentNode = QtGui.QHBoxLayout()
        self.hlCurrentNode.setObjectName(_fromUtf8("hlCurrentNode"))
        self.lCurrentNode = QtGui.QLabel(dialNodeRename)
        self.lCurrentNode.setMinimumSize(QtCore.QSize(70, 0))
        self.lCurrentNode.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lCurrentNode.setObjectName(_fromUtf8("lCurrentNode"))
        self.hlCurrentNode.addWidget(self.lCurrentNode)
        self.lCurrentNodeVal = QtGui.QLabel(dialNodeRename)
        self.lCurrentNodeVal.setObjectName(_fromUtf8("lCurrentNodeVal"))
        self.hlCurrentNode.addWidget(self.lCurrentNodeVal)
        self.gridLayout.addLayout(self.hlCurrentNode, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(dialNodeRename)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.retranslateUi(dialNodeRename)
        QtCore.QMetaObject.connectSlotsByName(dialNodeRename)

    def retranslateUi(self, dialNodeRename):
        dialNodeRename.setWindowTitle(_translate("dialNodeRename", "Rename Node", None))
        self.lNewName.setText(_translate("dialNodeRename", "New Name:", None))
        self.lResult.setText(_translate("dialNodeRename", "Result: ", None))
        self.pbOk.setText(_translate("dialNodeRename", "Ok", None))
        self.pbCancel.setText(_translate("dialNodeRename", "Cancel", None))
        self.lCurrentNode.setText(_translate("dialNodeRename", "Current Node: ", None))
        self.lCurrentNodeVal.setText(_translate("dialNodeRename", "TextLabel", None))

