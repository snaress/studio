# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\vtxMap\ui\wgSceneNodes.ui'
#
# Created: Sun Feb 01 05:28:13 2015
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
        wgSceneNodes.resize(256, 219)
        self.gridLayout = QtGui.QGridLayout(wgSceneNodes)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_3 = QtGui.QFrame(wgSceneNodes)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 2, 0, 1, 1)
        self.twSceneNodes = QtGui.QTreeWidget(wgSceneNodes)
        self.twSceneNodes.setIndentation(2)
        self.twSceneNodes.setObjectName(_fromUtf8("twSceneNodes"))
        self.twSceneNodes.headerItem().setText(0, _fromUtf8("1"))
        self.twSceneNodes.header().setVisible(False)
        self.gridLayout.addWidget(self.twSceneNodes, 1, 0, 1, 1)
        self.hlShowByType = QtGui.QHBoxLayout()
        self.hlShowByType.setSpacing(2)
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
        self.gridLayout.addLayout(self.hlShowByType, 3, 0, 1, 1)
        self.pbUpdate = QtGui.QPushButton(wgSceneNodes)
        self.pbUpdate.setObjectName(_fromUtf8("pbUpdate"))
        self.gridLayout.addWidget(self.pbUpdate, 0, 0, 1, 1)

        self.retranslateUi(wgSceneNodes)
        QtCore.QMetaObject.connectSlotsByName(wgSceneNodes)

    def retranslateUi(self, wgSceneNodes):
        wgSceneNodes.setWindowTitle(_translate("wgSceneNodes", "SceneNodes", None))
        self.lClothType.setText(_translate("wgSceneNodes", "Show: ", None))
        self.cbCloth.setText(_translate("wgSceneNodes", "nCloth", None))
        self.cbRigid.setText(_translate("wgSceneNodes", "nRigid", None))
        self.pbUpdate.setText(_translate("wgSceneNodes", "Update From Scene", None))

