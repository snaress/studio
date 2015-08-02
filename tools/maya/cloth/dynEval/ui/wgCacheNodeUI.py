# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\dynEval\ud\wgCacheNode.ui'
#
# Created: Sun Aug 02 02:22:57 2015
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

class Ui_wgCacheNode(object):
    def setupUi(self, wgCacheNode):
        wgCacheNode.setObjectName(_fromUtf8("wgCacheNode"))
        wgCacheNode.resize(338, 28)
        self.gridLayout = QtGui.QGridLayout(wgCacheNode)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_6 = QtGui.QFrame(wgCacheNode)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.gridLayout.addWidget(self.line_6, 0, 0, 1, 1)
        self.hlCacheNode = QtGui.QHBoxLayout()
        self.hlCacheNode.setSpacing(2)
        self.hlCacheNode.setContentsMargins(2, 0, 2, 0)
        self.hlCacheNode.setObjectName(_fromUtf8("hlCacheNode"))
        self.line = QtGui.QFrame(wgCacheNode)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.hlCacheNode.addWidget(self.line)
        self.lCacheFile = QtGui.QLabel(wgCacheNode)
        self.lCacheFile.setObjectName(_fromUtf8("lCacheFile"))
        self.hlCacheNode.addWidget(self.lCacheFile)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlCacheNode.addItem(spacerItem)
        self.line_3 = QtGui.QFrame(wgCacheNode)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.hlCacheNode.addWidget(self.line_3)
        self.lCacheAttr = QtGui.QLabel(wgCacheNode)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lCacheAttr.setFont(font)
        self.lCacheAttr.setText(_fromUtf8(""))
        self.lCacheAttr.setObjectName(_fromUtf8("lCacheAttr"))
        self.hlCacheNode.addWidget(self.lCacheAttr)
        self.line_4 = QtGui.QFrame(wgCacheNode)
        self.line_4.setMaximumSize(QtCore.QSize(2, 16777215))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.hlCacheNode.addWidget(self.line_4)
        self.pbCacheType = QtGui.QPushButton(wgCacheNode)
        self.pbCacheType.setMaximumSize(QtCore.QSize(20, 20))
        self.pbCacheType.setText(_fromUtf8(""))
        self.pbCacheType.setIconSize(QtCore.QSize(18, 18))
        self.pbCacheType.setCheckable(False)
        self.pbCacheType.setFlat(False)
        self.pbCacheType.setObjectName(_fromUtf8("pbCacheType"))
        self.hlCacheNode.addWidget(self.pbCacheType)
        self.line_5 = QtGui.QFrame(wgCacheNode)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.hlCacheNode.addWidget(self.line_5)
        self.pbCacheOk = QtGui.QPushButton(wgCacheNode)
        self.pbCacheOk.setMaximumSize(QtCore.QSize(20, 20))
        self.pbCacheOk.setText(_fromUtf8(""))
        self.pbCacheOk.setIconSize(QtCore.QSize(18, 18))
        self.pbCacheOk.setCheckable(True)
        self.pbCacheOk.setFlat(True)
        self.pbCacheOk.setObjectName(_fromUtf8("pbCacheOk"))
        self.hlCacheNode.addWidget(self.pbCacheOk)
        self.line_2 = QtGui.QFrame(wgCacheNode)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.hlCacheNode.addWidget(self.line_2)
        self.gridLayout.addLayout(self.hlCacheNode, 1, 0, 1, 1)
        self.line_7 = QtGui.QFrame(wgCacheNode)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.gridLayout.addWidget(self.line_7, 2, 0, 1, 1)

        self.retranslateUi(wgCacheNode)
        QtCore.QMetaObject.connectSlotsByName(wgCacheNode)

    def retranslateUi(self, wgCacheNode):
        wgCacheNode.setWindowTitle(_translate("wgCacheNode", "Cache Node", None))
        self.lCacheFile.setText(_translate("wgCacheNode", "TextLabel", None))

