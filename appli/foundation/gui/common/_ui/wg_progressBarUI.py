# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\foundation\gui\common\_src\wg_progressBar.ui'
#
# Created: Sat Jan 02 14:36:14 2016
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(185, 16)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vl_progress = QtGui.QVBoxLayout()
        self.vl_progress.setSpacing(0)
        self.vl_progress.setObjectName(_fromUtf8("vl_progress"))
        self.pgb_1 = QtGui.QProgressBar(Form)
        self.pgb_1.setMaximumSize(QtCore.QSize(16777215, 5))
        self.pgb_1.setStyleSheet(_fromUtf8(""))
        self.pgb_1.setProperty("value", 24)
        self.pgb_1.setTextVisible(False)
        self.pgb_1.setObjectName(_fromUtf8("pgb_1"))
        self.vl_progress.addWidget(self.pgb_1)
        self.line_6 = QtGui.QFrame(Form)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.vl_progress.addWidget(self.line_6)
        self.pgb_2 = QtGui.QProgressBar(Form)
        self.pgb_2.setMaximumSize(QtCore.QSize(16777215, 5))
        self.pgb_2.setStyleSheet(_fromUtf8(""))
        self.pgb_2.setProperty("value", 0)
        self.pgb_2.setTextVisible(False)
        self.pgb_2.setObjectName(_fromUtf8("pgb_2"))
        self.vl_progress.addWidget(self.pgb_2)
        self.gridLayout.addLayout(self.vl_progress, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Progress", None))

