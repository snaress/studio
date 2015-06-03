# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothBox\ud\clothBox.ui'
#
# Created: Mon Jun 01 15:20:13 2015
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

class Ui_mwClothBox(object):
    def setupUi(self, mwClothBox):
        mwClothBox.setObjectName(_fromUtf8("mwClothBox"))
        mwClothBox.setWindowModality(QtCore.Qt.NonModal)
        mwClothBox.resize(253, 436)
        self.centralwidget = QtGui.QWidget(mwClothBox)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabClothBox = QtGui.QTabWidget(self.centralwidget)
        self.tabClothBox.setObjectName(_fromUtf8("tabClothBox"))
        self.tabMode = QtGui.QWidget()
        self.tabMode.setObjectName(_fromUtf8("tabMode"))
        self.vlMode = QtGui.QVBoxLayout(self.tabMode)
        self.vlMode.setSpacing(0)
        self.vlMode.setMargin(0)
        self.vlMode.setObjectName(_fromUtf8("vlMode"))
        self.tabClothBox.addTab(self.tabMode, _fromUtf8(""))
        self.tabRigg = QtGui.QWidget()
        self.tabRigg.setObjectName(_fromUtf8("tabRigg"))
        self.vlRigg = QtGui.QVBoxLayout(self.tabRigg)
        self.vlRigg.setSpacing(0)
        self.vlRigg.setMargin(0)
        self.vlRigg.setObjectName(_fromUtf8("vlRigg"))
        self.tabClothBox.addTab(self.tabRigg, _fromUtf8(""))
        self.tabSmu = QtGui.QWidget()
        self.tabSmu.setObjectName(_fromUtf8("tabSmu"))
        self.vlSimu = QtGui.QVBoxLayout(self.tabSmu)
        self.vlSimu.setSpacing(0)
        self.vlSimu.setMargin(0)
        self.vlSimu.setObjectName(_fromUtf8("vlSimu"))
        self.tabClothBox.addTab(self.tabSmu, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabClothBox, 0, 0, 1, 1)
        mwClothBox.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mwClothBox)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 253, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mwClothBox.setMenuBar(self.menubar)

        self.retranslateUi(mwClothBox)
        self.tabClothBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mwClothBox)

    def retranslateUi(self, mwClothBox):
        mwClothBox.setWindowTitle(_translate("mwClothBox", "Cloth Box", None))
        self.tabClothBox.setTabText(self.tabClothBox.indexOf(self.tabMode), _translate("mwClothBox", "Mode", None))
        self.tabClothBox.setTabText(self.tabClothBox.indexOf(self.tabRigg), _translate("mwClothBox", "Rigg", None))
        self.tabClothBox.setTabText(self.tabClothBox.indexOf(self.tabSmu), _translate("mwClothBox", "Simu", None))

