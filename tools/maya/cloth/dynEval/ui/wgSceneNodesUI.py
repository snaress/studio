# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\dynEval\ud\wgSceneNodes.ui'
#
# Created: Sun Aug 09 05:43:17 2015
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
        self.hlOptions = QtGui.QHBoxLayout()
        self.hlOptions.setSpacing(2)
        self.hlOptions.setObjectName(_fromUtf8("hlOptions"))
        self.lClothType = QtGui.QLabel(wgSceneNodes)
        self.lClothType.setMinimumSize(QtCore.QSize(0, 20))
        self.lClothType.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lClothType.setFont(font)
        self.lClothType.setObjectName(_fromUtf8("lClothType"))
        self.hlOptions.addWidget(self.lClothType)
        self.cbCloth = QtGui.QCheckBox(wgSceneNodes)
        self.cbCloth.setMinimumSize(QtCore.QSize(0, 20))
        self.cbCloth.setMaximumSize(QtCore.QSize(60, 16777215))
        self.cbCloth.setChecked(True)
        self.cbCloth.setObjectName(_fromUtf8("cbCloth"))
        self.hlOptions.addWidget(self.cbCloth)
        self.cbRigid = QtGui.QCheckBox(wgSceneNodes)
        self.cbRigid.setMinimumSize(QtCore.QSize(0, 20))
        self.cbRigid.setMaximumSize(QtCore.QSize(60, 16777215))
        self.cbRigid.setChecked(True)
        self.cbRigid.setObjectName(_fromUtf8("cbRigid"))
        self.hlOptions.addWidget(self.cbRigid)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlOptions.addItem(spacerItem)
        self.pbAllOn = QtGui.QPushButton(wgSceneNodes)
        self.pbAllOn.setMaximumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pbAllOn.setFont(font)
        self.pbAllOn.setFlat(False)
        self.pbAllOn.setObjectName(_fromUtf8("pbAllOn"))
        self.hlOptions.addWidget(self.pbAllOn)
        self.pbAllOff = QtGui.QPushButton(wgSceneNodes)
        self.pbAllOff.setMaximumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pbAllOff.setFont(font)
        self.pbAllOff.setFlat(False)
        self.pbAllOff.setObjectName(_fromUtf8("pbAllOff"))
        self.hlOptions.addWidget(self.pbAllOff)
        self.gridLayout.addLayout(self.hlOptions, 2, 0, 1, 1)
        self.twSceneNodes = QtGui.QTreeWidget(wgSceneNodes)
        self.twSceneNodes.setIndentation(20)
        self.twSceneNodes.setExpandsOnDoubleClick(False)
        self.twSceneNodes.setColumnCount(1)
        self.twSceneNodes.setObjectName(_fromUtf8("twSceneNodes"))
        self.twSceneNodes.headerItem().setText(0, _fromUtf8("1"))
        self.twSceneNodes.header().setVisible(False)
        self.gridLayout.addWidget(self.twSceneNodes, 0, 0, 1, 1)
        self.line = QtGui.QFrame(wgSceneNodes)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.retranslateUi(wgSceneNodes)
        QtCore.QMetaObject.connectSlotsByName(wgSceneNodes)

    def retranslateUi(self, wgSceneNodes):
        wgSceneNodes.setWindowTitle(_translate("wgSceneNodes", "SceneNodes", None))
        self.lClothType.setText(_translate("wgSceneNodes", "Show: ", None))
        self.cbCloth.setText(_translate("wgSceneNodes", "nCloth", None))
        self.cbRigid.setText(_translate("wgSceneNodes", "nRigid", None))
        self.pbAllOn.setText(_translate("wgSceneNodes", "All ON", None))
        self.pbAllOff.setText(_translate("wgSceneNodes", "All OFF", None))

