# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\fondation\gui\fondation\settings\_src\userGroups.ui'
#
# Created: Tue Dec 08 00:24:29 2015
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

class Ui_wg_tsUserGroups(object):
    def setupUi(self, wg_tsUserGroups):
        wg_tsUserGroups.setObjectName(_fromUtf8("wg_tsUserGroups"))
        wg_tsUserGroups.resize(356, 248)
        self.gridLayout = QtGui.QGridLayout(wg_tsUserGroups)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.qf_userGroups = QtGui.QFrame(wg_tsUserGroups)
        self.qf_userGroups.setMinimumSize(QtCore.QSize(0, 0))
        self.qf_userGroups.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qf_userGroups.setObjectName(_fromUtf8("qf_userGroups"))
        self.vl_userGroups = QtGui.QVBoxLayout(self.qf_userGroups)
        self.vl_userGroups.setSpacing(0)
        self.vl_userGroups.setMargin(0)
        self.vl_userGroups.setObjectName(_fromUtf8("vl_userGroups"))
        self.gridLayout.addWidget(self.qf_userGroups, 0, 0, 1, 1)
        self.qf_users = QtGui.QFrame(wg_tsUserGroups)
        self.qf_users.setMinimumSize(QtCore.QSize(0, 0))
        self.qf_users.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qf_users.setObjectName(_fromUtf8("qf_users"))
        self.vl_users = QtGui.QVBoxLayout(self.qf_users)
        self.vl_users.setSpacing(0)
        self.vl_users.setMargin(0)
        self.vl_users.setObjectName(_fromUtf8("vl_users"))
        self.gridLayout.addWidget(self.qf_users, 1, 0, 1, 1)

        self.retranslateUi(wg_tsUserGroups)
        QtCore.QMetaObject.connectSlotsByName(wg_tsUserGroups)

    def retranslateUi(self, wg_tsUserGroups):
        wg_tsUserGroups.setWindowTitle(_translate("wg_tsUserGroups", "User Groups", None))

