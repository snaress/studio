# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgDataPlugItem.ui'
#
# Created: Sat Jul 18 12:56:27 2015
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

class Ui_wgDataPlugItem(object):
    def setupUi(self, wgDataPlugItem):
        wgDataPlugItem.setObjectName(_fromUtf8("wgDataPlugItem"))
        wgDataPlugItem.resize(400, 51)
        self.gridLayout = QtGui.QGridLayout(wgDataPlugItem)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.qfInputFile = QtGui.QFrame(wgDataPlugItem)
        self.qfInputFile.setObjectName(_fromUtf8("qfInputFile"))
        self.hlInputFile = QtGui.QHBoxLayout(self.qfInputFile)
        self.hlInputFile.setSpacing(2)
        self.hlInputFile.setContentsMargins(2, 0, 2, 0)
        self.hlInputFile.setObjectName(_fromUtf8("hlInputFile"))
        self.line_5 = QtGui.QFrame(self.qfInputFile)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.hlInputFile.addWidget(self.line_5)
        self.cbLoadMethod = QtGui.QComboBox(self.qfInputFile)
        self.cbLoadMethod.setObjectName(_fromUtf8("cbLoadMethod"))
        self.cbLoadMethod.addItem(_fromUtf8(""))
        self.cbLoadMethod.addItem(_fromUtf8(""))
        self.cbLoadMethod.addItem(_fromUtf8(""))
        self.hlInputFile.addWidget(self.cbLoadMethod)
        self.line_6 = QtGui.QFrame(self.qfInputFile)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.hlInputFile.addWidget(self.line_6)
        self.qfNamespace = QtGui.QFrame(self.qfInputFile)
        self.qfNamespace.setObjectName(_fromUtf8("qfNamespace"))
        self.hlNamespace = QtGui.QHBoxLayout(self.qfNamespace)
        self.hlNamespace.setSpacing(0)
        self.hlNamespace.setMargin(0)
        self.hlNamespace.setObjectName(_fromUtf8("hlNamespace"))
        self.cbNamespace = QtGui.QCheckBox(self.qfNamespace)
        self.cbNamespace.setMinimumSize(QtCore.QSize(45, 0))
        self.cbNamespace.setMaximumSize(QtCore.QSize(45, 16777215))
        self.cbNamespace.setObjectName(_fromUtf8("cbNamespace"))
        self.hlNamespace.addWidget(self.cbNamespace)
        self.leNamespace = QtGui.QLineEdit(self.qfNamespace)
        self.leNamespace.setObjectName(_fromUtf8("leNamespace"))
        self.hlNamespace.addWidget(self.leNamespace)
        self.hlInputFile.addWidget(self.qfNamespace)
        self.line_7 = QtGui.QFrame(self.qfInputFile)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.hlInputFile.addWidget(self.line_7)
        self.gridLayout.addWidget(self.qfInputFile, 2, 0, 1, 1)
        self.hlPlug = QtGui.QHBoxLayout()
        self.hlPlug.setSpacing(2)
        self.hlPlug.setContentsMargins(2, -1, 2, -1)
        self.hlPlug.setObjectName(_fromUtf8("hlPlug"))
        self.line_4 = QtGui.QFrame(wgDataPlugItem)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.hlPlug.addWidget(self.line_4)
        self.lIndex = QtGui.QLabel(wgDataPlugItem)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lIndex.sizePolicy().hasHeightForWidth())
        self.lIndex.setSizePolicy(sizePolicy)
        self.lIndex.setMinimumSize(QtCore.QSize(30, 20))
        self.lIndex.setMaximumSize(QtCore.QSize(30, 20))
        self.lIndex.setAlignment(QtCore.Qt.AlignCenter)
        self.lIndex.setObjectName(_fromUtf8("lIndex"))
        self.hlPlug.addWidget(self.lIndex)
        self.line = QtGui.QFrame(wgDataPlugItem)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.hlPlug.addWidget(self.line)
        self.lConnectedNode = QtGui.QLabel(wgDataPlugItem)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lConnectedNode.sizePolicy().hasHeightForWidth())
        self.lConnectedNode.setSizePolicy(sizePolicy)
        self.lConnectedNode.setObjectName(_fromUtf8("lConnectedNode"))
        self.hlPlug.addWidget(self.lConnectedNode)
        self.line_3 = QtGui.QFrame(wgDataPlugItem)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.hlPlug.addWidget(self.line_3)
        self.pbEnable = QtGui.QPushButton(wgDataPlugItem)
        self.pbEnable.setMinimumSize(QtCore.QSize(20, 0))
        self.pbEnable.setMaximumSize(QtCore.QSize(20, 16777215))
        self.pbEnable.setText(_fromUtf8(""))
        self.pbEnable.setCheckable(True)
        self.pbEnable.setChecked(True)
        self.pbEnable.setFlat(True)
        self.pbEnable.setObjectName(_fromUtf8("pbEnable"))
        self.hlPlug.addWidget(self.pbEnable)
        self.line_2 = QtGui.QFrame(wgDataPlugItem)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.hlPlug.addWidget(self.line_2)
        self.gridLayout.addLayout(self.hlPlug, 1, 0, 1, 1)
        self.line_8 = QtGui.QFrame(wgDataPlugItem)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout.addWidget(self.line_8, 3, 0, 1, 1)
        self.line_9 = QtGui.QFrame(wgDataPlugItem)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.gridLayout.addWidget(self.line_9, 0, 0, 1, 1)

        self.retranslateUi(wgDataPlugItem)
        QtCore.QMetaObject.connectSlotsByName(wgDataPlugItem)

    def retranslateUi(self, wgDataPlugItem):
        wgDataPlugItem.setWindowTitle(_translate("wgDataPlugItem", "Plug Item", None))
        self.cbLoadMethod.setItemText(0, _translate("wgDataPlugItem", "Load", None))
        self.cbLoadMethod.setItemText(1, _translate("wgDataPlugItem", "Import", None))
        self.cbLoadMethod.setItemText(2, _translate("wgDataPlugItem", "Ref Import", None))
        self.cbNamespace.setText(_translate("wgDataPlugItem", "NS = ", None))
        self.lIndex.setText(_translate("wgDataPlugItem", "Ind", None))
        self.lConnectedNode.setText(_translate("wgDataPlugItem", "Connected Node", None))

