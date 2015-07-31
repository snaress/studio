# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothCache\ud\wgSceneNode.ui'
#
# Created: Fri May 22 00:06:31 2015
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

class Ui_wgSceneNode(object):
    def setupUi(self, wgSceneNode):
        wgSceneNode.setObjectName(_fromUtf8("wgSceneNode"))
        wgSceneNode.resize(477, 22)
        self.gridLayout = QtGui.QGridLayout(wgSceneNode)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hlSceneNode = QtGui.QHBoxLayout()
        self.hlSceneNode.setSpacing(2)
        self.hlSceneNode.setContentsMargins(2, 0, 2, 0)
        self.hlSceneNode.setObjectName(_fromUtf8("hlSceneNode"))
        self.line_2 = QtGui.QFrame(wgSceneNode)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.hlSceneNode.addWidget(self.line_2)
        self.pbIcon = QtGui.QPushButton(wgSceneNode)
        self.pbIcon.setMaximumSize(QtCore.QSize(20, 20))
        self.pbIcon.setText(_fromUtf8(""))
        self.pbIcon.setIconSize(QtCore.QSize(16, 16))
        self.pbIcon.setFlat(True)
        self.pbIcon.setObjectName(_fromUtf8("pbIcon"))
        self.hlSceneNode.addWidget(self.pbIcon)
        self.line = QtGui.QFrame(wgSceneNode)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.hlSceneNode.addWidget(self.line)
        self.lSceneNode = QtGui.QLabel(wgSceneNode)
        self.lSceneNode.setObjectName(_fromUtf8("lSceneNode"))
        self.hlSceneNode.addWidget(self.lSceneNode)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlSceneNode.addItem(spacerItem)
        self.line_4 = QtGui.QFrame(wgSceneNode)
        self.line_4.setMaximumSize(QtCore.QSize(2, 16777215))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.hlSceneNode.addWidget(self.line_4)
        self.pbEnable = QtGui.QPushButton(wgSceneNode)
        self.pbEnable.setMaximumSize(QtCore.QSize(20, 20))
        self.pbEnable.setText(_fromUtf8(""))
        self.pbEnable.setIconSize(QtCore.QSize(18, 18))
        self.pbEnable.setCheckable(True)
        self.pbEnable.setFlat(True)
        self.pbEnable.setObjectName(_fromUtf8("pbEnable"))
        self.hlSceneNode.addWidget(self.pbEnable)
        self.line_5 = QtGui.QFrame(wgSceneNode)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.hlSceneNode.addWidget(self.line_5)
        self.gridLayout.addLayout(self.hlSceneNode, 0, 0, 1, 1)

        self.retranslateUi(wgSceneNode)
        QtCore.QMetaObject.connectSlotsByName(wgSceneNode)

    def retranslateUi(self, wgSceneNode):
        wgSceneNode.setWindowTitle(_translate("wgSceneNode", "SceneNode", None))
        self.lSceneNode.setText(_translate("wgSceneNode", "TextLabel", None))

