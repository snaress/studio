# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\fondation\gui\fondation\_src\tsUgUsersDial.ui'
#
# Created: Sun Dec 13 19:17:38 2015
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

class Ui_dial_users(object):
    def setupUi(self, dial_users):
        dial_users.setObjectName(_fromUtf8("dial_users"))
        dial_users.resize(455, 207)
        self.gridLayout = QtGui.QGridLayout(dial_users)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line = QtGui.QFrame(dial_users)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 7, 0, 1, 1)
        self.l_message = QtGui.QLabel(dial_users)
        self.l_message.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l_message.setFont(font)
        self.l_message.setAlignment(QtCore.Qt.AlignCenter)
        self.l_message.setObjectName(_fromUtf8("l_message"))
        self.gridLayout.addWidget(self.l_message, 1, 0, 1, 1)
        self.line_3 = QtGui.QFrame(dial_users)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(dial_users)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 1)
        self.hl_useName = QtGui.QHBoxLayout()
        self.hl_useName.setObjectName(_fromUtf8("hl_useName"))
        self.l_userName = QtGui.QLabel(dial_users)
        self.l_userName.setMinimumSize(QtCore.QSize(92, 0))
        self.l_userName.setMaximumSize(QtCore.QSize(92, 16777215))
        self.l_userName.setObjectName(_fromUtf8("l_userName"))
        self.hl_useName.addWidget(self.l_userName)
        self.le_userName = QtGui.QLineEdit(dial_users)
        self.le_userName.setMinimumSize(QtCore.QSize(100, 0))
        self.le_userName.setMaximumSize(QtCore.QSize(100, 16777215))
        self.le_userName.setObjectName(_fromUtf8("le_userName"))
        self.hl_useName.addWidget(self.le_userName)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_useName.addItem(spacerItem)
        self.gridLayout.addLayout(self.hl_useName, 3, 0, 1, 1)
        self.hl_useFirstName = QtGui.QHBoxLayout()
        self.hl_useFirstName.setObjectName(_fromUtf8("hl_useFirstName"))
        self.l_userFirstName = QtGui.QLabel(dial_users)
        self.l_userFirstName.setMinimumSize(QtCore.QSize(92, 0))
        self.l_userFirstName.setMaximumSize(QtCore.QSize(92, 16777215))
        self.l_userFirstName.setObjectName(_fromUtf8("l_userFirstName"))
        self.hl_useFirstName.addWidget(self.l_userFirstName)
        self.le_userFirstName = QtGui.QLineEdit(dial_users)
        self.le_userFirstName.setMinimumSize(QtCore.QSize(100, 0))
        self.le_userFirstName.setMaximumSize(QtCore.QSize(100, 16777215))
        self.le_userFirstName.setObjectName(_fromUtf8("le_userFirstName"))
        self.hl_useFirstName.addWidget(self.le_userFirstName)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_useFirstName.addItem(spacerItem1)
        self.gridLayout.addLayout(self.hl_useFirstName, 5, 0, 1, 1)
        self.hl_useGroup = QtGui.QHBoxLayout()
        self.hl_useGroup.setObjectName(_fromUtf8("hl_useGroup"))
        self.l_userGroup = QtGui.QLabel(dial_users)
        self.l_userGroup.setMinimumSize(QtCore.QSize(92, 0))
        self.l_userGroup.setMaximumSize(QtCore.QSize(92, 16777215))
        self.l_userGroup.setObjectName(_fromUtf8("l_userGroup"))
        self.hl_useGroup.addWidget(self.l_userGroup)
        self.cb_userGroup = QtGui.QComboBox(dial_users)
        self.cb_userGroup.setObjectName(_fromUtf8("cb_userGroup"))
        self.hl_useGroup.addWidget(self.cb_userGroup)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_useGroup.addItem(spacerItem2)
        self.gridLayout.addLayout(self.hl_useGroup, 4, 0, 1, 1)
        self.hl_useLastName = QtGui.QHBoxLayout()
        self.hl_useLastName.setObjectName(_fromUtf8("hl_useLastName"))
        self.l_userLastName = QtGui.QLabel(dial_users)
        self.l_userLastName.setMinimumSize(QtCore.QSize(92, 0))
        self.l_userLastName.setMaximumSize(QtCore.QSize(92, 16777215))
        self.l_userLastName.setObjectName(_fromUtf8("l_userLastName"))
        self.hl_useLastName.addWidget(self.l_userLastName)
        self.le_userLastName = QtGui.QLineEdit(dial_users)
        self.le_userLastName.setMinimumSize(QtCore.QSize(100, 0))
        self.le_userLastName.setMaximumSize(QtCore.QSize(100, 16777215))
        self.le_userLastName.setObjectName(_fromUtf8("le_userLastName"))
        self.hl_useLastName.addWidget(self.le_userLastName)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_useLastName.addItem(spacerItem3)
        self.gridLayout.addLayout(self.hl_useLastName, 6, 0, 1, 1)
        self.hl_buttons = QtGui.QHBoxLayout()
        self.hl_buttons.setSpacing(0)
        self.hl_buttons.setObjectName(_fromUtf8("hl_buttons"))
        spacerItem4 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_buttons.addItem(spacerItem4)
        self.pb_save = QtGui.QPushButton(dial_users)
        self.pb_save.setMaximumSize(QtCore.QSize(60, 20))
        self.pb_save.setObjectName(_fromUtf8("pb_save"))
        self.hl_buttons.addWidget(self.pb_save)
        self.pb_cancel = QtGui.QPushButton(dial_users)
        self.pb_cancel.setMaximumSize(QtCore.QSize(60, 20))
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.hl_buttons.addWidget(self.pb_cancel)
        self.gridLayout.addLayout(self.hl_buttons, 9, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 8, 0, 1, 1)

        self.retranslateUi(dial_users)
        QtCore.QMetaObject.connectSlotsByName(dial_users)
        dial_users.setTabOrder(self.le_userName, self.cb_userGroup)
        dial_users.setTabOrder(self.cb_userGroup, self.le_userFirstName)
        dial_users.setTabOrder(self.le_userFirstName, self.le_userLastName)
        dial_users.setTabOrder(self.le_userLastName, self.pb_save)
        dial_users.setTabOrder(self.pb_save, self.pb_cancel)

    def retranslateUi(self, dial_users):
        dial_users.setWindowTitle(_translate("dial_users", "Users Dialog", None))
        self.l_message.setText(_translate("dial_users", "Edit User", None))
        self.l_userName.setText(_translate("dial_users", "User Name: ", None))
        self.l_userFirstName.setText(_translate("dial_users", "User First Name: ", None))
        self.l_userGroup.setText(_translate("dial_users", "User Group: ", None))
        self.l_userLastName.setText(_translate("dial_users", "User Last Name: ", None))
        self.pb_save.setText(_translate("dial_users", "Save", None))
        self.pb_cancel.setText(_translate("dial_users", "cancel", None))

