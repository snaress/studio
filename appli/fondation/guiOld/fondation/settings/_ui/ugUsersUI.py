# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\fondation\gui\fondation\settings\_src\ugUsers.ui'
#
# Created: Mon Dec 07 22:31:49 2015
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

class Ui_wg_users(object):
    def setupUi(self, wg_users):
        wg_users.setObjectName(_fromUtf8("wg_users"))
        wg_users.resize(400, 382)
        self.gridLayout = QtGui.QGridLayout(wg_users)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.l_users = QtGui.QLabel(wg_users)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l_users.setFont(font)
        self.l_users.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l_users.setObjectName(_fromUtf8("l_users"))
        self.gridLayout.addWidget(self.l_users, 0, 0, 1, 1)
        self.line = QtGui.QFrame(wg_users)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.vl_usersEdit = QtGui.QVBoxLayout()
        self.vl_usersEdit.setSpacing(6)
        self.vl_usersEdit.setContentsMargins(-1, 26, -1, -1)
        self.vl_usersEdit.setObjectName(_fromUtf8("vl_usersEdit"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vl_usersEdit.addItem(spacerItem)
        self.pb_addUser = QtGui.QPushButton(wg_users)
        self.pb_addUser.setMaximumSize(QtCore.QSize(55, 20))
        self.pb_addUser.setToolTip(_fromUtf8(""))
        self.pb_addUser.setObjectName(_fromUtf8("pb_addUser"))
        self.vl_usersEdit.addWidget(self.pb_addUser)
        self.pb_delUser = QtGui.QPushButton(wg_users)
        self.pb_delUser.setMaximumSize(QtCore.QSize(55, 20))
        self.pb_delUser.setToolTip(_fromUtf8(""))
        self.pb_delUser.setObjectName(_fromUtf8("pb_delUser"))
        self.vl_usersEdit.addWidget(self.pb_delUser)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vl_usersEdit.addItem(spacerItem1)
        self.pb_editUser = QtGui.QPushButton(wg_users)
        self.pb_editUser.setMaximumSize(QtCore.QSize(55, 20))
        self.pb_editUser.setToolTip(_fromUtf8(""))
        self.pb_editUser.setObjectName(_fromUtf8("pb_editUser"))
        self.vl_usersEdit.addWidget(self.pb_editUser)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vl_usersEdit.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.vl_usersEdit)
        self.line_3 = QtGui.QFrame(wg_users)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.tw_users = QtGui.QTreeWidget(wg_users)
        self.tw_users.setObjectName(_fromUtf8("tw_users"))
        self.tw_users.headerItem().setText(0, _fromUtf8("Icone"))
        self.tw_users.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tw_users.headerItem().setTextAlignment(1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tw_users.headerItem().setTextAlignment(2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tw_users.headerItem().setTextAlignment(3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.tw_users)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.line_2 = QtGui.QFrame(wg_users)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 1)
        self.hl_userApply = QtGui.QHBoxLayout()
        self.hl_userApply.setSpacing(0)
        self.hl_userApply.setObjectName(_fromUtf8("hl_userApply"))
        self.pb_userApply = QtGui.QPushButton(wg_users)
        self.pb_userApply.setMaximumSize(QtCore.QSize(60, 20))
        self.pb_userApply.setObjectName(_fromUtf8("pb_userApply"))
        self.hl_userApply.addWidget(self.pb_userApply)
        self.pb_userCancel = QtGui.QPushButton(wg_users)
        self.pb_userCancel.setMaximumSize(QtCore.QSize(60, 20))
        self.pb_userCancel.setObjectName(_fromUtf8("pb_userCancel"))
        self.hl_userApply.addWidget(self.pb_userCancel)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_userApply.addItem(spacerItem3)
        self.gridLayout.addLayout(self.hl_userApply, 4, 0, 1, 1)

        self.retranslateUi(wg_users)
        QtCore.QMetaObject.connectSlotsByName(wg_users)

    def retranslateUi(self, wg_users):
        wg_users.setWindowTitle(_translate("wg_users", "Users", None))
        self.l_users.setText(_translate("wg_users", "Users:", None))
        self.pb_addUser.setText(_translate("wg_users", "Add", None))
        self.pb_delUser.setText(_translate("wg_users", "Del", None))
        self.pb_editUser.setText(_translate("wg_users", "Edit", None))
        self.tw_users.headerItem().setText(1, _translate("wg_users", "User Name", None))
        self.tw_users.headerItem().setText(2, _translate("wg_users", "First Name", None))
        self.tw_users.headerItem().setText(3, _translate("wg_users", "Last Name", None))
        self.pb_userApply.setText(_translate("wg_users", "Apply", None))
        self.pb_userCancel.setText(_translate("wg_users", "Cancel", None))

