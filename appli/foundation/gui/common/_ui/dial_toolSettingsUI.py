# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\foundation\gui\common\_src\dial_toolSettings.ui'
#
# Created: Sun Jan 03 02:48:04 2016
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

class Ui_dial_projectSettings(object):
    def setupUi(self, dial_projectSettings):
        dial_projectSettings.setObjectName(_fromUtf8("dial_projectSettings"))
        dial_projectSettings.resize(599, 400)
        self.gridLayout = QtGui.QGridLayout(dial_projectSettings)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hl_toolSettings = QtGui.QHBoxLayout()
        self.hl_toolSettings.setSpacing(0)
        self.hl_toolSettings.setContentsMargins(-1, 0, -1, -1)
        self.hl_toolSettings.setObjectName(_fromUtf8("hl_toolSettings"))
        self.qf_category = QtGui.QFrame(dial_projectSettings)
        self.qf_category.setMinimumSize(QtCore.QSize(0, 0))
        self.qf_category.setMaximumSize(QtCore.QSize(200, 16777215))
        self.qf_category.setObjectName(_fromUtf8("qf_category"))
        self.vl_category = QtGui.QVBoxLayout(self.qf_category)
        self.vl_category.setSpacing(0)
        self.vl_category.setMargin(0)
        self.vl_category.setObjectName(_fromUtf8("vl_category"))
        self.tw_category = QtGui.QTreeWidget(self.qf_category)
        self.tw_category.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tw_category.setAlternatingRowColors(True)
        self.tw_category.setIndentation(20)
        self.tw_category.setObjectName(_fromUtf8("tw_category"))
        self.tw_category.headerItem().setText(0, _fromUtf8("1"))
        self.tw_category.header().setVisible(False)
        self.vl_category.addWidget(self.tw_category)
        self.hl_toolSettings.addWidget(self.qf_category)
        self.line = QtGui.QFrame(dial_projectSettings)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.hl_toolSettings.addWidget(self.line)
        self.vl_settings = QtGui.QVBoxLayout()
        self.vl_settings.setSpacing(0)
        self.vl_settings.setContentsMargins(-1, 0, -1, 0)
        self.vl_settings.setObjectName(_fromUtf8("vl_settings"))
        self.qf_settingsWidget = QtGui.QFrame(dial_projectSettings)
        self.qf_settingsWidget.setObjectName(_fromUtf8("qf_settingsWidget"))
        self.vl_settingsWidget = QtGui.QVBoxLayout(self.qf_settingsWidget)
        self.vl_settingsWidget.setSpacing(0)
        self.vl_settingsWidget.setMargin(0)
        self.vl_settingsWidget.setObjectName(_fromUtf8("vl_settingsWidget"))
        self.vl_settings.addWidget(self.qf_settingsWidget)
        spacerItem = QtGui.QSpacerItem(20, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vl_settings.addItem(spacerItem)
        self.line_2 = QtGui.QFrame(dial_projectSettings)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.vl_settings.addWidget(self.line_2)
        self.hl_settingsOptions = QtGui.QHBoxLayout()
        self.hl_settingsOptions.setSpacing(0)
        self.hl_settingsOptions.setContentsMargins(-1, 0, -1, -1)
        self.hl_settingsOptions.setObjectName(_fromUtf8("hl_settingsOptions"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_settingsOptions.addItem(spacerItem1)
        self.pb_save = QtGui.QPushButton(dial_projectSettings)
        self.pb_save.setMaximumSize(QtCore.QSize(60, 20))
        self.pb_save.setFlat(False)
        self.pb_save.setObjectName(_fromUtf8("pb_save"))
        self.hl_settingsOptions.addWidget(self.pb_save)
        self.pb_close = QtGui.QPushButton(dial_projectSettings)
        self.pb_close.setMaximumSize(QtCore.QSize(60, 20))
        self.pb_close.setFlat(False)
        self.pb_close.setObjectName(_fromUtf8("pb_close"))
        self.hl_settingsOptions.addWidget(self.pb_close)
        self.vl_settings.addLayout(self.hl_settingsOptions)
        self.hl_toolSettings.addLayout(self.vl_settings)
        self.gridLayout.addLayout(self.hl_toolSettings, 0, 0, 1, 1)

        self.retranslateUi(dial_projectSettings)
        QtCore.QMetaObject.connectSlotsByName(dial_projectSettings)

    def retranslateUi(self, dial_projectSettings):
        dial_projectSettings.setWindowTitle(_translate("dial_projectSettings", "Project Settings", None))
        self.pb_save.setText(_translate("dial_projectSettings", "save", None))
        self.pb_close.setText(_translate("dial_projectSettings", "Close", None))

