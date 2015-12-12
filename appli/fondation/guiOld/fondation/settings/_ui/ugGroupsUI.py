# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\fondation\gui\fondation\settings\_src\ugGroups.ui'
#
# Created: Mon Dec 07 22:31:48 2015
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

class Ui_wg_groups(object):
    def setupUi(self, wg_groups):
        wg_groups.setObjectName(_fromUtf8("wg_groups"))
        wg_groups.resize(443, 299)
        self.gridLayout = QtGui.QGridLayout(wg_groups)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.l_groups = QtGui.QLabel(wg_groups)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l_groups.setFont(font)
        self.l_groups.setObjectName(_fromUtf8("l_groups"))
        self.gridLayout.addWidget(self.l_groups, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(wg_groups)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 1)
        self.hl_groups = QtGui.QHBoxLayout()
        self.hl_groups.setSpacing(0)
        self.hl_groups.setObjectName(_fromUtf8("hl_groups"))
        self.vl_groupsEdit = QtGui.QVBoxLayout()
        self.vl_groupsEdit.setSpacing(6)
        self.vl_groupsEdit.setContentsMargins(-1, 26, -1, -1)
        self.vl_groupsEdit.setObjectName(_fromUtf8("vl_groupsEdit"))
        self.hl_moveGrp = QtGui.QHBoxLayout()
        self.hl_moveGrp.setSpacing(0)
        self.hl_moveGrp.setObjectName(_fromUtf8("hl_moveGrp"))
        self.pb_upGrp = QtGui.QPushButton(wg_groups)
        self.pb_upGrp.setMinimumSize(QtCore.QSize(22, 22))
        self.pb_upGrp.setMaximumSize(QtCore.QSize(22, 22))
        self.pb_upGrp.setText(_fromUtf8(""))
        self.pb_upGrp.setObjectName(_fromUtf8("pb_upGrp"))
        self.hl_moveGrp.addWidget(self.pb_upGrp)
        self.pb_dnGrp = QtGui.QPushButton(wg_groups)
        self.pb_dnGrp.setMinimumSize(QtCore.QSize(22, 22))
        self.pb_dnGrp.setMaximumSize(QtCore.QSize(22, 22))
        self.pb_dnGrp.setText(_fromUtf8(""))
        self.pb_dnGrp.setObjectName(_fromUtf8("pb_dnGrp"))
        self.hl_moveGrp.addWidget(self.pb_dnGrp)
        self.vl_groupsEdit.addLayout(self.hl_moveGrp)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vl_groupsEdit.addItem(spacerItem)
        self.pb_addGrp = QtGui.QPushButton(wg_groups)
        self.pb_addGrp.setMaximumSize(QtCore.QSize(55, 20))
        self.pb_addGrp.setToolTip(_fromUtf8(""))
        self.pb_addGrp.setObjectName(_fromUtf8("pb_addGrp"))
        self.vl_groupsEdit.addWidget(self.pb_addGrp)
        self.pb_delGrp = QtGui.QPushButton(wg_groups)
        self.pb_delGrp.setMaximumSize(QtCore.QSize(55, 20))
        self.pb_delGrp.setToolTip(_fromUtf8(""))
        self.pb_delGrp.setObjectName(_fromUtf8("pb_delGrp"))
        self.vl_groupsEdit.addWidget(self.pb_delGrp)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vl_groupsEdit.addItem(spacerItem1)
        self.pb_editGrp = QtGui.QPushButton(wg_groups)
        self.pb_editGrp.setMaximumSize(QtCore.QSize(55, 20))
        self.pb_editGrp.setToolTip(_fromUtf8(""))
        self.pb_editGrp.setObjectName(_fromUtf8("pb_editGrp"))
        self.vl_groupsEdit.addWidget(self.pb_editGrp)
        self.pb_styleGrp = QtGui.QPushButton(wg_groups)
        self.pb_styleGrp.setMaximumSize(QtCore.QSize(55, 20))
        self.pb_styleGrp.setToolTip(_fromUtf8(""))
        self.pb_styleGrp.setObjectName(_fromUtf8("pb_styleGrp"))
        self.vl_groupsEdit.addWidget(self.pb_styleGrp)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vl_groupsEdit.addItem(spacerItem2)
        self.hl_groups.addLayout(self.vl_groupsEdit)
        self.line = QtGui.QFrame(wg_groups)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.hl_groups.addWidget(self.line)
        self.tw_groups = QtGui.QTreeWidget(wg_groups)
        self.tw_groups.setAlternatingRowColors(True)
        self.tw_groups.setIndentation(0)
        self.tw_groups.setItemsExpandable(False)
        self.tw_groups.setExpandsOnDoubleClick(False)
        self.tw_groups.setObjectName(_fromUtf8("tw_groups"))
        self.tw_groups.headerItem().setText(0, _fromUtf8("Code"))
        self.tw_groups.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tw_groups.headerItem().setTextAlignment(1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tw_groups.headerItem().setTextAlignment(2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tw_groups.header().setStretchLastSection(False)
        self.hl_groups.addWidget(self.tw_groups)
        self.gridLayout.addLayout(self.hl_groups, 2, 0, 1, 1)
        self.hl_grpApply = QtGui.QHBoxLayout()
        self.hl_grpApply.setSpacing(0)
        self.hl_grpApply.setObjectName(_fromUtf8("hl_grpApply"))
        self.pb_grpApply = QtGui.QPushButton(wg_groups)
        self.pb_grpApply.setMaximumSize(QtCore.QSize(60, 20))
        self.pb_grpApply.setObjectName(_fromUtf8("pb_grpApply"))
        self.hl_grpApply.addWidget(self.pb_grpApply)
        self.pb_grpCancel = QtGui.QPushButton(wg_groups)
        self.pb_grpCancel.setMaximumSize(QtCore.QSize(60, 20))
        self.pb_grpCancel.setObjectName(_fromUtf8("pb_grpCancel"))
        self.hl_grpApply.addWidget(self.pb_grpCancel)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_grpApply.addItem(spacerItem3)
        self.gridLayout.addLayout(self.hl_grpApply, 4, 0, 1, 1)
        self.line_3 = QtGui.QFrame(wg_groups)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 1)

        self.retranslateUi(wg_groups)
        QtCore.QMetaObject.connectSlotsByName(wg_groups)

    def retranslateUi(self, wg_groups):
        wg_groups.setWindowTitle(_translate("wg_groups", "Groups", None))
        self.l_groups.setText(_translate("wg_groups", "Groups:", None))
        self.pb_addGrp.setText(_translate("wg_groups", "Add", None))
        self.pb_delGrp.setText(_translate("wg_groups", "Del", None))
        self.pb_editGrp.setText(_translate("wg_groups", "Edit", None))
        self.pb_styleGrp.setText(_translate("wg_groups", "Style", None))
        self.tw_groups.headerItem().setText(1, _translate("wg_groups", "Name", None))
        self.tw_groups.headerItem().setText(2, _translate("wg_groups", "Style", None))
        self.pb_grpApply.setText(_translate("wg_groups", "Apply", None))
        self.pb_grpCancel.setText(_translate("wg_groups", "Cancel", None))

