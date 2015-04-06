# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothEditor\ui\wgAttrNode.ui'
#
# Created: Fri Apr 03 01:38:26 2015
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

class Ui_wgPresetNode(object):
    def setupUi(self, wgPresetNode):
        wgPresetNode.setObjectName(_fromUtf8("wgPresetNode"))
        wgPresetNode.resize(440, 24)
        self.gridLayout = QtGui.QGridLayout(wgPresetNode)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lGroup = QtGui.QLabel(wgPresetNode)
        self.lGroup.setObjectName(_fromUtf8("lGroup"))
        self.gridLayout.addWidget(self.lGroup, 0, 0, 1, 1)
        self.qfValue = QtGui.QFrame(wgPresetNode)
        self.qfValue.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qfValue.setObjectName(_fromUtf8("qfValue"))
        self.vlValue = QtGui.QVBoxLayout(self.qfValue)
        self.vlValue.setSpacing(0)
        self.vlValue.setMargin(0)
        self.vlValue.setObjectName(_fromUtf8("vlValue"))
        self.hlLayout = QtGui.QHBoxLayout()
        self.hlLayout.setObjectName(_fromUtf8("hlLayout"))
        self.lPreset = QtGui.QLabel(self.qfValue)
        self.lPreset.setObjectName(_fromUtf8("lPreset"))
        self.hlLayout.addWidget(self.lPreset)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlLayout.addItem(spacerItem)
        self.line_5 = QtGui.QFrame(self.qfValue)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.hlLayout.addWidget(self.line_5)
        self.hfValue = QtGui.QFrame(self.qfValue)
        self.hfValue.setMinimumSize(QtCore.QSize(20, 0))
        self.hfValue.setObjectName(_fromUtf8("hfValue"))
        self.hlValue = QtGui.QHBoxLayout(self.hfValue)
        self.hlValue.setSpacing(0)
        self.hlValue.setMargin(0)
        self.hlValue.setObjectName(_fromUtf8("hlValue"))
        self.hlLayout.addWidget(self.hfValue)
        self.line_3 = QtGui.QFrame(self.qfValue)
        self.line_3.setMaximumSize(QtCore.QSize(2, 16777215))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.hlLayout.addWidget(self.line_3)
        self.pbLock = QtGui.QPushButton(self.qfValue)
        self.pbLock.setMaximumSize(QtCore.QSize(20, 20))
        self.pbLock.setText(_fromUtf8(""))
        self.pbLock.setIconSize(QtCore.QSize(20, 20))
        self.pbLock.setCheckable(True)
        self.pbLock.setFlat(True)
        self.pbLock.setObjectName(_fromUtf8("pbLock"))
        self.hlLayout.addWidget(self.pbLock)
        self.line_4 = QtGui.QFrame(self.qfValue)
        self.line_4.setMaximumSize(QtCore.QSize(2, 16777215))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.hlLayout.addWidget(self.line_4)
        self.vlValue.addLayout(self.hlLayout)
        self.gridLayout.addWidget(self.qfValue, 0, 1, 1, 1)

        self.retranslateUi(wgPresetNode)
        QtCore.QMetaObject.connectSlotsByName(wgPresetNode)

    def retranslateUi(self, wgPresetNode):
        wgPresetNode.setWindowTitle(_translate("wgPresetNode", "Preset Node", None))
        self.lGroup.setText(_translate("wgPresetNode", "TextLabel", None))
        self.lPreset.setText(_translate("wgPresetNode", "TextLabel", None))

