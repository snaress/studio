# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\prodManager\ui\settings.ui'
#
# Created: Sun Feb 22 01:31:05 2015
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

class Ui_mwSettings(object):
    def setupUi(self, mwSettings):
        mwSettings.setObjectName(_fromUtf8("mwSettings"))
        mwSettings.resize(500, 500)
        self.centralwidget = QtGui.QWidget(mwSettings)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(2, 0, 2, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.qfSettings = QtGui.QFrame(self.centralwidget)
        self.qfSettings.setFrameShape(QtGui.QFrame.Box)
        self.qfSettings.setObjectName(_fromUtf8("qfSettings"))
        self.hlSettings = QtGui.QHBoxLayout(self.qfSettings)
        self.hlSettings.setSpacing(1)
        self.hlSettings.setMargin(0)
        self.hlSettings.setObjectName(_fromUtf8("hlSettings"))
        self.twSettings = QtGui.QTreeWidget(self.qfSettings)
        self.twSettings.setMaximumSize(QtCore.QSize(150, 16777215))
        self.twSettings.setIndentation(2)
        self.twSettings.setItemsExpandable(False)
        self.twSettings.setExpandsOnDoubleClick(False)
        self.twSettings.setObjectName(_fromUtf8("twSettings"))
        self.twSettings.headerItem().setText(0, _fromUtf8("1"))
        self.twSettings.header().setVisible(False)
        self.hlSettings.addWidget(self.twSettings)
        self.vlSettings = QtGui.QVBoxLayout()
        self.vlSettings.setSpacing(0)
        self.vlSettings.setObjectName(_fromUtf8("vlSettings"))
        self.teInfo = QtGui.QPlainTextEdit(self.qfSettings)
        self.teInfo.setMinimumSize(QtCore.QSize(0, 60))
        self.teInfo.setMaximumSize(QtCore.QSize(16777215, 60))
        self.teInfo.setReadOnly(True)
        self.teInfo.setObjectName(_fromUtf8("teInfo"))
        self.vlSettings.addWidget(self.teInfo)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlSettings.addItem(spacerItem)
        self.hlSettings.addLayout(self.vlSettings)
        self.gridLayout.addWidget(self.qfSettings, 3, 0, 1, 1)
        self.qfProject_1 = QtGui.QFrame(self.centralwidget)
        self.qfProject_1.setLineWidth(0)
        self.qfProject_1.setObjectName(_fromUtf8("qfProject_1"))
        self.hlProject_1 = QtGui.QHBoxLayout(self.qfProject_1)
        self.hlProject_1.setSpacing(2)
        self.hlProject_1.setMargin(0)
        self.hlProject_1.setObjectName(_fromUtf8("hlProject_1"))
        self.lName = QtGui.QLabel(self.qfProject_1)
        self.lName.setMinimumSize(QtCore.QSize(85, 0))
        self.lName.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lName.setFont(font)
        self.lName.setObjectName(_fromUtf8("lName"))
        self.hlProject_1.addWidget(self.lName)
        self.lNameValue = QtGui.QLabel(self.qfProject_1)
        self.lNameValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lNameValue.setObjectName(_fromUtf8("lNameValue"))
        self.hlProject_1.addWidget(self.lNameValue)
        spacerItem1 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hlProject_1.addItem(spacerItem1)
        self.lAlias = QtGui.QLabel(self.qfProject_1)
        self.lAlias.setMinimumSize(QtCore.QSize(70, 0))
        self.lAlias.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lAlias.setFont(font)
        self.lAlias.setObjectName(_fromUtf8("lAlias"))
        self.hlProject_1.addWidget(self.lAlias)
        self.lAliasValue = QtGui.QLabel(self.qfProject_1)
        self.lAliasValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lAliasValue.setObjectName(_fromUtf8("lAliasValue"))
        self.hlProject_1.addWidget(self.lAliasValue)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlProject_1.addItem(spacerItem2)
        self.lType = QtGui.QLabel(self.qfProject_1)
        self.lType.setMinimumSize(QtCore.QSize(70, 0))
        self.lType.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lType.setFont(font)
        self.lType.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.lType.setObjectName(_fromUtf8("lType"))
        self.hlProject_1.addWidget(self.lType)
        self.lTypeValue = QtGui.QLabel(self.qfProject_1)
        self.lTypeValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lTypeValue.setObjectName(_fromUtf8("lTypeValue"))
        self.hlProject_1.addWidget(self.lTypeValue)
        self.gridLayout.addWidget(self.qfProject_1, 0, 0, 1, 1)
        self.qfProject_2 = QtGui.QFrame(self.centralwidget)
        self.qfProject_2.setLineWidth(0)
        self.qfProject_2.setObjectName(_fromUtf8("qfProject_2"))
        self.hlProject_2 = QtGui.QHBoxLayout(self.qfProject_2)
        self.hlProject_2.setSpacing(2)
        self.hlProject_2.setMargin(0)
        self.hlProject_2.setObjectName(_fromUtf8("hlProject_2"))
        self.lSeason = QtGui.QLabel(self.qfProject_2)
        self.lSeason.setMinimumSize(QtCore.QSize(85, 0))
        self.lSeason.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lSeason.setFont(font)
        self.lSeason.setObjectName(_fromUtf8("lSeason"))
        self.hlProject_2.addWidget(self.lSeason)
        self.lSeasonValue = QtGui.QLabel(self.qfProject_2)
        self.lSeasonValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lSeasonValue.setObjectName(_fromUtf8("lSeasonValue"))
        self.hlProject_2.addWidget(self.lSeasonValue)
        spacerItem3 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlProject_2.addItem(spacerItem3)
        self.lEpisode = QtGui.QLabel(self.qfProject_2)
        self.lEpisode.setMinimumSize(QtCore.QSize(85, 0))
        self.lEpisode.setMaximumSize(QtCore.QSize(85, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lEpisode.setFont(font)
        self.lEpisode.setObjectName(_fromUtf8("lEpisode"))
        self.hlProject_2.addWidget(self.lEpisode)
        self.lEpisodeValue = QtGui.QLabel(self.qfProject_2)
        self.lEpisodeValue.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lEpisodeValue.setObjectName(_fromUtf8("lEpisodeValue"))
        self.hlProject_2.addWidget(self.lEpisodeValue)
        self.gridLayout.addWidget(self.qfProject_2, 1, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pbReset = QtGui.QPushButton(self.centralwidget)
        self.pbReset.setObjectName(_fromUtf8("pbReset"))
        self.horizontalLayout.addWidget(self.pbReset)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pbSave = QtGui.QPushButton(self.centralwidget)
        self.pbSave.setObjectName(_fromUtf8("pbSave"))
        self.horizontalLayout.addWidget(self.pbSave)
        self.pbClose = QtGui.QPushButton(self.centralwidget)
        self.pbClose.setObjectName(_fromUtf8("pbClose"))
        self.horizontalLayout.addWidget(self.pbClose)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        mwSettings.setCentralWidget(self.centralwidget)

        self.retranslateUi(mwSettings)
        QtCore.QMetaObject.connectSlotsByName(mwSettings)

    def retranslateUi(self, mwSettings):
        mwSettings.setWindowTitle(_translate("mwSettings", "Settings", None))
        self.lName.setText(_translate("mwSettings", "Project Name :", None))
        self.lNameValue.setText(_translate("mwSettings", "TextLabel", None))
        self.lAlias.setText(_translate("mwSettings", "Project Alias :", None))
        self.lAliasValue.setText(_translate("mwSettings", "TextLabel", None))
        self.lType.setText(_translate("mwSettings", "Project Type:", None))
        self.lTypeValue.setText(_translate("mwSettings", "TextLabel", None))
        self.lSeason.setText(_translate("mwSettings", "Project Season :", None))
        self.lSeasonValue.setText(_translate("mwSettings", "TextLabel", None))
        self.lEpisode.setText(_translate("mwSettings", "Project Episode :", None))
        self.lEpisodeValue.setText(_translate("mwSettings", "TextLabel", None))
        self.pbReset.setText(_translate("mwSettings", "Reset", None))
        self.pbSave.setText(_translate("mwSettings", "Save", None))
        self.pbClose.setText(_translate("mwSettings", "Close", None))

