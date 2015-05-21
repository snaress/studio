# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothEditor\ud\wgSceneNodes.ui'
#
# Created: Thu May 21 21:37:10 2015
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
        wgSceneNodes.resize(401, 287)
        self.gridLayout = QtGui.QGridLayout(wgSceneNodes)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hlSceneNodes = QtGui.QHBoxLayout()
        self.hlSceneNodes.setSpacing(2)
        self.hlSceneNodes.setObjectName(_fromUtf8("hlSceneNodes"))
        self.twSceneNodes = QtGui.QTreeWidget(wgSceneNodes)
        self.twSceneNodes.setIndentation(20)
        self.twSceneNodes.setExpandsOnDoubleClick(False)
        self.twSceneNodes.setColumnCount(1)
        self.twSceneNodes.setObjectName(_fromUtf8("twSceneNodes"))
        self.twSceneNodes.headerItem().setText(0, _fromUtf8("1"))
        self.twSceneNodes.header().setVisible(False)
        self.hlSceneNodes.addWidget(self.twSceneNodes)
        self.line = QtGui.QFrame(wgSceneNodes)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.hlSceneNodes.addWidget(self.line)
        self.vlOptions = QtGui.QVBoxLayout()
        self.vlOptions.setSpacing(0)
        self.vlOptions.setObjectName(_fromUtf8("vlOptions"))
        self.lClothType = QtGui.QLabel(wgSceneNodes)
        self.lClothType.setMinimumSize(QtCore.QSize(0, 20))
        self.lClothType.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lClothType.setFont(font)
        self.lClothType.setObjectName(_fromUtf8("lClothType"))
        self.vlOptions.addWidget(self.lClothType)
        self.cbCloth = QtGui.QCheckBox(wgSceneNodes)
        self.cbCloth.setMinimumSize(QtCore.QSize(0, 20))
        self.cbCloth.setMaximumSize(QtCore.QSize(60, 16777215))
        self.cbCloth.setChecked(True)
        self.cbCloth.setObjectName(_fromUtf8("cbCloth"))
        self.vlOptions.addWidget(self.cbCloth)
        self.cbRigid = QtGui.QCheckBox(wgSceneNodes)
        self.cbRigid.setMinimumSize(QtCore.QSize(0, 20))
        self.cbRigid.setMaximumSize(QtCore.QSize(60, 16777215))
        self.cbRigid.setChecked(True)
        self.cbRigid.setObjectName(_fromUtf8("cbRigid"))
        self.vlOptions.addWidget(self.cbRigid)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlOptions.addItem(spacerItem)
        self.hlSceneNodes.addLayout(self.vlOptions)
        self.gridLayout.addLayout(self.hlSceneNodes, 0, 0, 1, 1)

        self.retranslateUi(wgSceneNodes)
        QtCore.QMetaObject.connectSlotsByName(wgSceneNodes)

    def retranslateUi(self, wgSceneNodes):
        wgSceneNodes.setWindowTitle(_translate("wgSceneNodes", "SceneNodes", None))
        self.lClothType.setText(_translate("wgSceneNodes", "Show: ", None))
        self.cbCloth.setText(_translate("wgSceneNodes", "nCloth", None))
        self.cbRigid.setText(_translate("wgSceneNodes", "nRigid", None))

