# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\fondation\gui\fondation\src\toolSettings.ui'
#
# Created: Thu Dec 03 23:15:11 2015
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

class Ui_mw_toolSettings(object):
    def setupUi(self, mw_toolSettings):
        mw_toolSettings.setObjectName(_fromUtf8("mw_toolSettings"))
        mw_toolSettings.resize(800, 600)
        self.centralwidget = QtGui.QWidget(mw_toolSettings)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.vl_category = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vl_category.setSpacing(0)
        self.vl_category.setMargin(0)
        self.vl_category.setObjectName(_fromUtf8("vl_category"))
        self.tw_category = QtGui.QTreeWidget(self.verticalLayoutWidget_2)
        self.tw_category.setAlternatingRowColors(True)
        self.tw_category.setIndentation(12)
        self.tw_category.setObjectName(_fromUtf8("tw_category"))
        self.tw_category.headerItem().setText(0, _fromUtf8("1"))
        self.tw_category.header().setVisible(False)
        self.vl_category.addWidget(self.tw_category)
        self.verticalLayoutWidget = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.vl_settings = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vl_settings.setSpacing(0)
        self.vl_settings.setContentsMargins(-1, 0, -1, 0)
        self.vl_settings.setObjectName(_fromUtf8("vl_settings"))
        self.qf_settingsWidget = QtGui.QFrame(self.verticalLayoutWidget)
        self.qf_settingsWidget.setObjectName(_fromUtf8("qf_settingsWidget"))
        self.vl_settingsWidget = QtGui.QVBoxLayout(self.qf_settingsWidget)
        self.vl_settingsWidget.setSpacing(0)
        self.vl_settingsWidget.setMargin(0)
        self.vl_settingsWidget.setObjectName(_fromUtf8("vl_settingsWidget"))
        self.vl_settings.addWidget(self.qf_settingsWidget)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vl_settings.addItem(spacerItem)
        self.hl_settingsOptions = QtGui.QHBoxLayout()
        self.hl_settingsOptions.setSpacing(0)
        self.hl_settingsOptions.setContentsMargins(-1, 0, -1, -1)
        self.hl_settingsOptions.setObjectName(_fromUtf8("hl_settingsOptions"))
        self.pb_apply = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pb_apply.setMaximumSize(QtCore.QSize(50, 20))
        self.pb_apply.setObjectName(_fromUtf8("pb_apply"))
        self.hl_settingsOptions.addWidget(self.pb_apply)
        self.pb_cancel = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pb_cancel.setMaximumSize(QtCore.QSize(50, 20))
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.hl_settingsOptions.addWidget(self.pb_cancel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_settingsOptions.addItem(spacerItem1)
        self.pb_save = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pb_save.setMaximumSize(QtCore.QSize(50, 20))
        self.pb_save.setObjectName(_fromUtf8("pb_save"))
        self.hl_settingsOptions.addWidget(self.pb_save)
        self.pb_close = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pb_close.setMaximumSize(QtCore.QSize(50, 20))
        self.pb_close.setObjectName(_fromUtf8("pb_close"))
        self.hl_settingsOptions.addWidget(self.pb_close)
        self.vl_settings.addLayout(self.hl_settingsOptions)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        mw_toolSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(mw_toolSettings)
        QtCore.QMetaObject.connectSlotsByName(mw_toolSettings)

    def retranslateUi(self, mw_toolSettings):
        mw_toolSettings.setWindowTitle(_translate("mw_toolSettings", "Tool Settings", None))
        self.pb_apply.setText(_translate("mw_toolSettings", "Apply", None))
        self.pb_cancel.setText(_translate("mw_toolSettings", "Cancel", None))
        self.pb_save.setText(_translate("mw_toolSettings", "save", None))
        self.pb_close.setText(_translate("mw_toolSettings", "Close", None))

