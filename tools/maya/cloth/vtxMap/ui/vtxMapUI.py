# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\vtxMap\ui\vtxMap.ui'
#
# Created: Sun Feb 01 16:02:37 2015
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

class Ui_mwVtxMap(object):
    def setupUi(self, mwVtxMap):
        mwVtxMap.setObjectName(_fromUtf8("mwVtxMap"))
        mwVtxMap.resize(625, 494)
        self.centralwidget = QtGui.QWidget(mwVtxMap)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setContentsMargins(1, 0, 1, 0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.hlInit = QtGui.QHBoxLayout()
        self.hlInit.setObjectName(_fromUtf8("hlInit"))
        self.pbInit = QtGui.QPushButton(self.centralwidget)
        self.pbInit.setObjectName(_fromUtf8("pbInit"))
        self.hlInit.addWidget(self.pbInit)
        self.leInit = QtGui.QLineEdit(self.centralwidget)
        self.leInit.setReadOnly(True)
        self.leInit.setObjectName(_fromUtf8("leInit"))
        self.hlInit.addWidget(self.leInit)
        self.pbSelect = QtGui.QPushButton(self.centralwidget)
        self.pbSelect.setObjectName(_fromUtf8("pbSelect"))
        self.hlInit.addWidget(self.pbSelect)
        self.gridLayout_3.addLayout(self.hlInit, 0, 0, 1, 1)
        self.hlNodetype = QtGui.QHBoxLayout()
        self.hlNodetype.setSpacing(2)
        self.hlNodetype.setObjectName(_fromUtf8("hlNodetype"))
        self.cbSceneNodes = QtGui.QCheckBox(self.centralwidget)
        self.cbSceneNodes.setChecked(True)
        self.cbSceneNodes.setObjectName(_fromUtf8("cbSceneNodes"))
        self.hlNodetype.addWidget(self.cbSceneNodes)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlNodetype.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.hlNodetype, 1, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 2, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.vfSceneNodes = QtGui.QFrame(self.splitter)
        self.vfSceneNodes.setLineWidth(0)
        self.vfSceneNodes.setObjectName(_fromUtf8("vfSceneNodes"))
        self.vlSceneNodes = QtGui.QVBoxLayout(self.vfSceneNodes)
        self.vlSceneNodes.setSpacing(2)
        self.vlSceneNodes.setMargin(0)
        self.vlSceneNodes.setObjectName(_fromUtf8("vlSceneNodes"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.vlMapType = QtGui.QVBoxLayout(self.layoutWidget)
        self.vlMapType.setSpacing(2)
        self.vlMapType.setContentsMargins(-1, 0, -1, 0)
        self.vlMapType.setObjectName(_fromUtf8("vlMapType"))
        self.tabVertex = QtGui.QTabWidget(self.splitter)
        self.tabVertex.setObjectName(_fromUtf8("tabVertex"))
        self.tabVtxTools = QtGui.QWidget()
        self.tabVtxTools.setObjectName(_fromUtf8("tabVtxTools"))
        self.gridLayout = QtGui.QGridLayout(self.tabVtxTools)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(1, 0, 1, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vlVtxEdition = QtGui.QVBoxLayout()
        self.vlVtxEdition.setSpacing(2)
        self.vlVtxEdition.setContentsMargins(-1, -1, -1, 0)
        self.vlVtxEdition.setObjectName(_fromUtf8("vlVtxEdition"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlVtxEdition.addItem(spacerItem1)
        self.gridLayout.addLayout(self.vlVtxEdition, 0, 0, 1, 1)
        self.tabVertex.addTab(self.tabVtxTools, _fromUtf8(""))
        self.tabVtxValues = QtGui.QWidget()
        self.tabVtxValues.setObjectName(_fromUtf8("tabVtxValues"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabVtxValues)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.vlVtxValues = QtGui.QVBoxLayout()
        self.vlVtxValues.setSpacing(2)
        self.vlVtxValues.setContentsMargins(-1, 0, -1, 0)
        self.vlVtxValues.setObjectName(_fromUtf8("vlVtxValues"))
        self.gridLayout_2.addLayout(self.vlVtxValues, 0, 0, 1, 1)
        self.tabVertex.addTab(self.tabVtxValues, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.splitter, 3, 0, 1, 1)
        mwVtxMap.setCentralWidget(self.centralwidget)

        self.retranslateUi(mwVtxMap)
        self.tabVertex.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mwVtxMap)

    def retranslateUi(self, mwVtxMap):
        mwVtxMap.setWindowTitle(_translate("mwVtxMap", "VtxMap", None))
        self.pbInit.setText(_translate("mwVtxMap", "Init", None))
        self.pbSelect.setText(_translate("mwVtxMap", "Select", None))
        self.cbSceneNodes.setText(_translate("mwVtxMap", "Scene Cloth Nodes", None))
        self.tabVertex.setTabText(self.tabVertex.indexOf(self.tabVtxTools), _translate("mwVtxMap", "Vtx Tools", None))
        self.tabVertex.setTabText(self.tabVertex.indexOf(self.tabVtxValues), _translate("mwVtxMap", "Vtx Values", None))

