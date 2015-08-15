# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\fondation\gui\src\wgToolsTab.ui'
#
# Created: Wed Aug 12 20:55:09 2015
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

class Ui_wgToolsTab(object):
    def setupUi(self, wgToolsTab):
        wgToolsTab.setObjectName(_fromUtf8("wgToolsTab"))
        wgToolsTab.resize(952, 255)
        self.gridLayout = QtGui.QGridLayout(wgToolsTab)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.saHorizontal = QtGui.QScrollArea(wgToolsTab)
        self.saHorizontal.setMinimumSize(QtCore.QSize(0, 40))
        self.saHorizontal.setMaximumSize(QtCore.QSize(16777215, 40))
        self.saHorizontal.setWidgetResizable(True)
        self.saHorizontal.setObjectName(_fromUtf8("saHorizontal"))
        self.saWidgetHorizontal = QtGui.QWidget()
        self.saWidgetHorizontal.setGeometry(QtCore.QRect(0, 0, 800, 38))
        self.saWidgetHorizontal.setObjectName(_fromUtf8("saWidgetHorizontal"))
        self.gridLayout_2 = QtGui.QGridLayout(self.saWidgetHorizontal)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.qfHlTools = QtGui.QFrame(self.saWidgetHorizontal)
        self.qfHlTools.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qfHlTools.setObjectName(_fromUtf8("qfHlTools"))
        self.hlTools = QtGui.QHBoxLayout(self.qfHlTools)
        self.hlTools.setSpacing(0)
        self.hlTools.setMargin(0)
        self.hlTools.setObjectName(_fromUtf8("hlTools"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlTools.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.qfHlTools, 0, 0, 1, 1)
        self.saHorizontal.setWidget(self.saWidgetHorizontal)
        self.gridLayout.addWidget(self.saHorizontal, 0, 0, 1, 1)
        self.saVertical = QtGui.QScrollArea(wgToolsTab)
        self.saVertical.setMinimumSize(QtCore.QSize(150, 0))
        self.saVertical.setMaximumSize(QtCore.QSize(150, 16777215))
        self.saVertical.setWidgetResizable(True)
        self.saVertical.setObjectName(_fromUtf8("saVertical"))
        self.saWidgetVertical = QtGui.QWidget()
        self.saWidgetVertical.setGeometry(QtCore.QRect(0, 0, 148, 253))
        self.saWidgetVertical.setObjectName(_fromUtf8("saWidgetVertical"))
        self.gridLayout_3 = QtGui.QGridLayout(self.saWidgetVertical)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.qfVlTools = QtGui.QFrame(self.saWidgetVertical)
        self.qfVlTools.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qfVlTools.setObjectName(_fromUtf8("qfVlTools"))
        self.vlTools = QtGui.QVBoxLayout(self.qfVlTools)
        self.vlTools.setSpacing(0)
        self.vlTools.setMargin(0)
        self.vlTools.setObjectName(_fromUtf8("vlTools"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlTools.addItem(spacerItem1)
        self.gridLayout_3.addWidget(self.qfVlTools, 0, 0, 1, 1)
        self.saVertical.setWidget(self.saWidgetVertical)
        self.gridLayout.addWidget(self.saVertical, 0, 1, 1, 1)

        self.retranslateUi(wgToolsTab)
        QtCore.QMetaObject.connectSlotsByName(wgToolsTab)

    def retranslateUi(self, wgToolsTab):
        wgToolsTab.setWindowTitle(_translate("wgToolsTab", "Tools Tab", None))

