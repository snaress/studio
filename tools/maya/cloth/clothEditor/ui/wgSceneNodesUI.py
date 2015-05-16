# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothEditor\ui\wgSceneNodes.ui'
#
# Created: Sat May 16 16:07:09 2015
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

class Ui_wgSceneNodes(object):
    def setupUi(self, wgSceneNodes):
        wgSceneNodes.setObjectName(_fromUtf8("wgSceneNodes"))
        wgSceneNodes.resize(314, 558)
        self.gridLayout = QtGui.QGridLayout(wgSceneNodes)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.twSceneNodes = QtGui.QTreeWidget(wgSceneNodes)
        self.twSceneNodes.setIndentation(20)
        self.twSceneNodes.setExpandsOnDoubleClick(False)
        self.twSceneNodes.setColumnCount(1)
        self.twSceneNodes.setObjectName(_fromUtf8("twSceneNodes"))
        self.twSceneNodes.headerItem().setText(0, _fromUtf8("1"))
        self.twSceneNodes.header().setVisible(False)
        self.verticalLayout.addWidget(self.twSceneNodes)
        self.line_2 = QtGui.QFrame(wgSceneNodes)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.hlShowByType = QtGui.QHBoxLayout()
        self.hlShowByType.setSpacing(6)
        self.hlShowByType.setContentsMargins(-1, -1, -1, 0)
        self.hlShowByType.setObjectName(_fromUtf8("hlShowByType"))
        self.lClothType = QtGui.QLabel(wgSceneNodes)
        self.lClothType.setMinimumSize(QtCore.QSize(0, 20))
        self.lClothType.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lClothType.setObjectName(_fromUtf8("lClothType"))
        self.hlShowByType.addWidget(self.lClothType)
        self.cbCloth = QtGui.QCheckBox(wgSceneNodes)
        self.cbCloth.setMinimumSize(QtCore.QSize(0, 20))
        self.cbCloth.setMaximumSize(QtCore.QSize(60, 16777215))
        self.cbCloth.setChecked(True)
        self.cbCloth.setObjectName(_fromUtf8("cbCloth"))
        self.hlShowByType.addWidget(self.cbCloth)
        self.cbRigid = QtGui.QCheckBox(wgSceneNodes)
        self.cbRigid.setMinimumSize(QtCore.QSize(0, 20))
        self.cbRigid.setMaximumSize(QtCore.QSize(60, 16777215))
        self.cbRigid.setChecked(True)
        self.cbRigid.setObjectName(_fromUtf8("cbRigid"))
        self.hlShowByType.addWidget(self.cbRigid)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlShowByType.addItem(spacerItem)
        self.verticalLayout.addLayout(self.hlShowByType)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.vfFilters = QtGui.QFrame(wgSceneNodes)
        self.vfFilters.setObjectName(_fromUtf8("vfFilters"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.vfFilters)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout.addWidget(self.vfFilters, 1, 0, 1, 1)

        self.retranslateUi(wgSceneNodes)
        QtCore.QMetaObject.connectSlotsByName(wgSceneNodes)

    def retranslateUi(self, wgSceneNodes):
        wgSceneNodes.setWindowTitle(_translate("wgSceneNodes", "SceneNodes", None))
        self.lClothType.setText(_translate("wgSceneNodes", "Show: ", None))
        self.cbCloth.setText(_translate("wgSceneNodes", "nCloth", None))
        self.cbRigid.setText(_translate("wgSceneNodes", "nRigid", None))

