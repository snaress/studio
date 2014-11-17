# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\factory\ui\dialTransfert.ui'
#
# Created: Mon Nov 17 15:32:57 2014
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

class Ui_transfert(object):
    def setupUi(self, transfert):
        transfert.setObjectName(_fromUtf8("transfert"))
        transfert.resize(561, 100)
        self.gridLayout = QtGui.QGridLayout(transfert)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hlTmpFolder = QtGui.QHBoxLayout()
        self.hlTmpFolder.setSpacing(2)
        self.hlTmpFolder.setObjectName(_fromUtf8("hlTmpFolder"))
        self.cbTmpFolder = QtGui.QCheckBox(transfert)
        self.cbTmpFolder.setChecked(True)
        self.cbTmpFolder.setObjectName(_fromUtf8("cbTmpFolder"))
        self.hlTmpFolder.addWidget(self.cbTmpFolder)
        self.leTmpFolder = QtGui.QLineEdit(transfert)
        self.leTmpFolder.setObjectName(_fromUtf8("leTmpFolder"))
        self.hlTmpFolder.addWidget(self.leTmpFolder)
        self.gridLayout.addLayout(self.hlTmpFolder, 4, 0, 1, 1)
        self.line = QtGui.QFrame(transfert)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 5, 0, 1, 1)
        self.lTransfert = QtGui.QLabel(transfert)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lTransfert.setFont(font)
        self.lTransfert.setAlignment(QtCore.Qt.AlignCenter)
        self.lTransfert.setObjectName(_fromUtf8("lTransfert"))
        self.gridLayout.addWidget(self.lTransfert, 0, 0, 1, 1)
        self.hlDestination = QtGui.QHBoxLayout()
        self.hlDestination.setSpacing(2)
        self.hlDestination.setContentsMargins(2, -1, 2, -1)
        self.hlDestination.setObjectName(_fromUtf8("hlDestination"))
        self.lDestination = QtGui.QLabel(transfert)
        self.lDestination.setObjectName(_fromUtf8("lDestination"))
        self.hlDestination.addWidget(self.lDestination)
        self.leDestination = QtGui.QLineEdit(transfert)
        self.leDestination.setObjectName(_fromUtf8("leDestination"))
        self.hlDestination.addWidget(self.leDestination)
        self.bOpen = QtGui.QPushButton(transfert)
        self.bOpen.setObjectName(_fromUtf8("bOpen"))
        self.hlDestination.addWidget(self.bOpen)
        self.gridLayout.addLayout(self.hlDestination, 2, 0, 1, 1)
        self.hlBtns = QtGui.QHBoxLayout()
        self.hlBtns.setSpacing(2)
        self.hlBtns.setContentsMargins(2, -1, 2, -1)
        self.hlBtns.setObjectName(_fromUtf8("hlBtns"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlBtns.addItem(spacerItem)
        self.bTransfert = QtGui.QPushButton(transfert)
        self.bTransfert.setObjectName(_fromUtf8("bTransfert"))
        self.hlBtns.addWidget(self.bTransfert)
        self.bCancel = QtGui.QPushButton(transfert)
        self.bCancel.setObjectName(_fromUtf8("bCancel"))
        self.hlBtns.addWidget(self.bCancel)
        self.gridLayout.addLayout(self.hlBtns, 6, 0, 1, 1)
        self.line_2 = QtGui.QFrame(transfert)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 1)
        self.line_3 = QtGui.QFrame(transfert)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 1)

        self.retranslateUi(transfert)
        QtCore.QMetaObject.connectSlotsByName(transfert)

    def retranslateUi(self, transfert):
        transfert.setWindowTitle(_translate("transfert", "Transfert", None))
        self.cbTmpFolder.setText(_translate("transfert", "Tmp Folder :", None))
        self.leTmpFolder.setText(_translate("transfert", "_fromFactory", None))
        self.lTransfert.setText(_translate("transfert", "TextLabel", None))
        self.lDestination.setText(_translate("transfert", "Destination: ", None))
        self.bOpen.setText(_translate("transfert", "Open", None))
        self.bTransfert.setText(_translate("transfert", "Transfert", None))
        self.bCancel.setText(_translate("transfert", "Cancel", None))

