# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\fondation\gui\fondation\src\tsUserGroups.ui'
#
# Created: Fri Dec 04 03:14:59 2015
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
        wg_tsUserGroups.resize(574, 623)
        self.gridLayout = QtGui.QGridLayout(wg_tsUserGroups)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.qf_userGroups = QtGui.QFrame(wg_tsUserGroups)
        self.qf_userGroups.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qf_userGroups.setObjectName(_fromUtf8("qf_userGroups"))
        self.vl_userGroups = QtGui.QVBoxLayout(self.qf_userGroups)
        self.vl_userGroups.setSpacing(0)
        self.vl_userGroups.setMargin(0)
        self.vl_userGroups.setObjectName(_fromUtf8("vl_userGroups"))
        self.label = QtGui.QLabel(self.qf_userGroups)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.vl_userGroups.addWidget(self.label)
        self.hl_groups = QtGui.QHBoxLayout()
        self.hl_groups.setSpacing(0)
        self.hl_groups.setObjectName(_fromUtf8("hl_groups"))
        self.vl_groupsEdit = QtGui.QVBoxLayout()
        self.vl_groupsEdit.setSpacing(6)
        self.vl_groupsEdit.setContentsMargins(-1, 0, -1, -1)
        self.vl_groupsEdit.setObjectName(_fromUtf8("vl_groupsEdit"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vl_groupsEdit.addItem(spacerItem)
        self.pb_addGrp = QtGui.QPushButton(self.qf_userGroups)
        self.pb_addGrp.setMaximumSize(QtCore.QSize(55, 20))
        self.pb_addGrp.setObjectName(_fromUtf8("pb_addGrp"))
        self.vl_groupsEdit.addWidget(self.pb_addGrp)
        self.pb_delGrp = QtGui.QPushButton(self.qf_userGroups)
        self.pb_delGrp.setMaximumSize(QtCore.QSize(55, 20))
        self.pb_delGrp.setObjectName(_fromUtf8("pb_delGrp"))
        self.vl_groupsEdit.addWidget(self.pb_delGrp)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vl_groupsEdit.addItem(spacerItem1)
        self.pb_editGrp = QtGui.QPushButton(self.qf_userGroups)
        self.pb_editGrp.setMaximumSize(QtCore.QSize(55, 20))
        self.pb_editGrp.setObjectName(_fromUtf8("pb_editGrp"))
        self.vl_groupsEdit.addWidget(self.pb_editGrp)
        self.pb_styleGrp = QtGui.QPushButton(self.qf_userGroups)
        self.pb_styleGrp.setMaximumSize(QtCore.QSize(55, 20))
        self.pb_styleGrp.setObjectName(_fromUtf8("pb_styleGrp"))
        self.vl_groupsEdit.addWidget(self.pb_styleGrp)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vl_groupsEdit.addItem(spacerItem2)
        self.hl_groups.addLayout(self.vl_groupsEdit)
        self.line = QtGui.QFrame(self.qf_userGroups)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.hl_groups.addWidget(self.line)
        self.tw_groups = QtGui.QTreeWidget(self.qf_userGroups)
        self.tw_groups.setAlternatingRowColors(True)
        self.tw_groups.setIndentation(0)
        self.tw_groups.setItemsExpandable(False)
        self.tw_groups.setExpandsOnDoubleClick(False)
        self.tw_groups.setObjectName(_fromUtf8("tw_groups"))
        self.tw_groups.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tw_groups.headerItem().setText(1, _fromUtf8("Code"))
        self.tw_groups.headerItem().setTextAlignment(1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tw_groups.headerItem().setTextAlignment(2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tw_groups.headerItem().setTextAlignment(3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tw_groups.header().setStretchLastSection(False)
        self.hl_groups.addWidget(self.tw_groups)
        self.vl_userGroups.addLayout(self.hl_groups)
        self.gridLayout.addWidget(self.qf_userGroups, 0, 0, 1, 1)
        self.qf_users = QtGui.QFrame(wg_tsUserGroups)
        self.qf_users.setObjectName(_fromUtf8("qf_users"))
        self.vl_users = QtGui.QVBoxLayout(self.qf_users)
        self.vl_users.setSpacing(0)
        self.vl_users.setMargin(0)
        self.vl_users.setObjectName(_fromUtf8("vl_users"))
        self.tw_users = QtGui.QTreeWidget(self.qf_users)
        self.tw_users.setObjectName(_fromUtf8("tw_users"))
        self.tw_users.headerItem().setText(0, _fromUtf8("2"))
        self.vl_users.addWidget(self.tw_users)
        self.gridLayout.addWidget(self.qf_users, 1, 0, 1, 1)

        self.retranslateUi(wg_tsUserGroups)
        QtCore.QMetaObject.connectSlotsByName(wg_tsUserGroups)

    def retranslateUi(self, wg_tsUserGroups):
        wg_tsUserGroups.setWindowTitle(_translate("wg_tsUserGroups", "User Groups", None))
        self.label.setText(_translate("wg_tsUserGroups", "User Groups:", None))
        self.pb_addGrp.setToolTip(_translate("wg_tsUserGroups", "Create new user group", None))
        self.pb_addGrp.setText(_translate("wg_tsUserGroups", "Add", None))
        self.pb_delGrp.setToolTip(_translate("wg_tsUserGroups", "Delete selected group", None))
        self.pb_delGrp.setText(_translate("wg_tsUserGroups", "Del", None))
        self.pb_editGrp.setToolTip(_translate("wg_tsUserGroups", "Edit selected group", None))
        self.pb_editGrp.setText(_translate("wg_tsUserGroups", "Edit", None))
        self.pb_styleGrp.setToolTip(_translate("wg_tsUserGroups", "Update style auto", None))
        self.pb_styleGrp.setText(_translate("wg_tsUserGroups", "Style", None))
        self.tw_groups.headerItem().setText(0, _translate("wg_tsUserGroups", "Id", None))
        self.tw_groups.headerItem().setText(2, _translate("wg_tsUserGroups", "Name", None))
        self.tw_groups.headerItem().setText(3, _translate("wg_tsUserGroups", "Style", None))

