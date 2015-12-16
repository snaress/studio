# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\foundation\gui\foundation\_src\foundation.ui'
#
# Created: Tue Dec 15 20:53:07 2015
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

class Ui_mw_foundation(object):
    def setupUi(self, mw_foundation):
        mw_foundation.setObjectName(_fromUtf8("mw_foundation"))
        mw_foundation.setWindowModality(QtCore.Qt.NonModal)
        mw_foundation.resize(800, 600)
        self.centralwidget = QtGui.QWidget(mw_foundation)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        mw_foundation.setCentralWidget(self.centralwidget)

        self.retranslateUi(mw_foundation)
        QtCore.QMetaObject.connectSlotsByName(mw_foundation)

    def retranslateUi(self, mw_foundation):
        mw_foundation.setWindowTitle(_translate("mw_foundation", "Foundation", None))

