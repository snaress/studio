# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\vtxMap\ui\vtxMap.ui'
#
# Created: Sun Jan 25 18:48:47 2015
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
        mwVtxMap.resize(608, 494)
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
        self.cbSceneNodes.setObjectName(_fromUtf8("cbSceneNodes"))
        self.hlNodetype.addWidget(self.cbSceneNodes)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlNodetype.addItem(spacerItem)
        self.lNodeType = QtGui.QLabel(self.centralwidget)
        self.lNodeType.setMinimumSize(QtCore.QSize(0, 15))
        self.lNodeType.setMaximumSize(QtCore.QSize(16777215, 15))
        self.lNodeType.setObjectName(_fromUtf8("lNodeType"))
        self.hlNodetype.addWidget(self.lNodeType)
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
        self.twSceneNodes = QtGui.QTreeWidget(self.vfSceneNodes)
        self.twSceneNodes.setIndentation(2)
        self.twSceneNodes.setObjectName(_fromUtf8("twSceneNodes"))
        self.twSceneNodes.headerItem().setText(0, _fromUtf8("1"))
        self.twSceneNodes.header().setVisible(False)
        self.vlSceneNodes.addWidget(self.twSceneNodes)
        self.line_3 = QtGui.QFrame(self.vfSceneNodes)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.vlSceneNodes.addWidget(self.line_3)
        self.hlShowByType = QtGui.QHBoxLayout()
        self.hlShowByType.setSpacing(2)
        self.hlShowByType.setContentsMargins(-1, -1, -1, 0)
        self.hlShowByType.setObjectName(_fromUtf8("hlShowByType"))
        self.lClothType = QtGui.QLabel(self.vfSceneNodes)
        self.lClothType.setMinimumSize(QtCore.QSize(0, 20))
        self.lClothType.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lClothType.setObjectName(_fromUtf8("lClothType"))
        self.hlShowByType.addWidget(self.lClothType)
        self.cbCloth = QtGui.QCheckBox(self.vfSceneNodes)
        self.cbCloth.setMinimumSize(QtCore.QSize(0, 20))
        self.cbCloth.setMaximumSize(QtCore.QSize(60, 16777215))
        self.cbCloth.setChecked(True)
        self.cbCloth.setObjectName(_fromUtf8("cbCloth"))
        self.hlShowByType.addWidget(self.cbCloth)
        self.cbRigid = QtGui.QCheckBox(self.vfSceneNodes)
        self.cbRigid.setMinimumSize(QtCore.QSize(0, 20))
        self.cbRigid.setMaximumSize(QtCore.QSize(60, 16777215))
        self.cbRigid.setChecked(True)
        self.cbRigid.setObjectName(_fromUtf8("cbRigid"))
        self.hlShowByType.addWidget(self.cbRigid)
        self.vlSceneNodes.addLayout(self.hlShowByType)
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.vlMapType = QtGui.QVBoxLayout(self.layoutWidget)
        self.vlMapType.setSpacing(2)
        self.vlMapType.setContentsMargins(-1, 0, -1, 0)
        self.vlMapType.setObjectName(_fromUtf8("vlMapType"))
        self.twMapType = QtGui.QTreeWidget(self.layoutWidget)
        self.twMapType.setMinimumSize(QtCore.QSize(0, 0))
        self.twMapType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.twMapType.setIndentation(0)
        self.twMapType.setItemsExpandable(False)
        self.twMapType.setExpandsOnDoubleClick(False)
        self.twMapType.setColumnCount(1)
        self.twMapType.setObjectName(_fromUtf8("twMapType"))
        self.twMapType.header().setVisible(False)
        self.vlMapType.addWidget(self.twMapType)
        self.line_2 = QtGui.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.vlMapType.addWidget(self.line_2)
        self.hlEditType = QtGui.QHBoxLayout()
        self.hlEditType.setSpacing(2)
        self.hlEditType.setContentsMargins(-1, -1, -1, 0)
        self.hlEditType.setObjectName(_fromUtf8("hlEditType"))
        self.lEditType = QtGui.QLabel(self.layoutWidget)
        self.lEditType.setObjectName(_fromUtf8("lEditType"))
        self.hlEditType.addWidget(self.lEditType)
        self.pbNone = QtGui.QPushButton(self.layoutWidget)
        self.pbNone.setMaximumSize(QtCore.QSize(50, 20))
        self.pbNone.setObjectName(_fromUtf8("pbNone"))
        self.hlEditType.addWidget(self.pbNone)
        self.pbVertex = QtGui.QPushButton(self.layoutWidget)
        self.pbVertex.setMaximumSize(QtCore.QSize(50, 20))
        self.pbVertex.setObjectName(_fromUtf8("pbVertex"))
        self.hlEditType.addWidget(self.pbVertex)
        self.pbTexture = QtGui.QPushButton(self.layoutWidget)
        self.pbTexture.setMaximumSize(QtCore.QSize(50, 20))
        self.pbTexture.setObjectName(_fromUtf8("pbTexture"))
        self.hlEditType.addWidget(self.pbTexture)
        self.vlMapType.addLayout(self.hlEditType)
        self.tabVertex = QtGui.QTabWidget(self.splitter)
        self.tabVertex.setObjectName(_fromUtf8("tabVertex"))
        self.tabVtxTools = QtGui.QWidget()
        self.tabVtxTools.setObjectName(_fromUtf8("tabVtxTools"))
        self.gridLayout = QtGui.QGridLayout(self.tabVtxTools)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vlVtxEdition = QtGui.QVBoxLayout()
        self.vlVtxEdition.setSpacing(2)
        self.vlVtxEdition.setContentsMargins(-1, -1, -1, 0)
        self.vlVtxEdition.setObjectName(_fromUtf8("vlVtxEdition"))
        self.lSelRange = QtGui.QLabel(self.tabVtxTools)
        self.lSelRange.setMinimumSize(QtCore.QSize(120, 0))
        self.lSelRange.setMaximumSize(QtCore.QSize(120, 16777215))
        self.lSelRange.setObjectName(_fromUtf8("lSelRange"))
        self.vlVtxEdition.addWidget(self.lSelRange)
        self.hlVtxSelRange = QtGui.QHBoxLayout()
        self.hlVtxSelRange.setObjectName(_fromUtf8("hlVtxSelRange"))
        self.sbRangeMin = QtGui.QDoubleSpinBox(self.tabVtxTools)
        self.sbRangeMin.setMinimumSize(QtCore.QSize(70, 0))
        self.sbRangeMin.setDecimals(3)
        self.sbRangeMin.setObjectName(_fromUtf8("sbRangeMin"))
        self.hlVtxSelRange.addWidget(self.sbRangeMin)
        self.sbRangeMax = QtGui.QDoubleSpinBox(self.tabVtxTools)
        self.sbRangeMax.setMinimumSize(QtCore.QSize(70, 0))
        self.sbRangeMax.setDecimals(3)
        self.sbRangeMax.setObjectName(_fromUtf8("sbRangeMax"))
        self.hlVtxSelRange.addWidget(self.sbRangeMax)
        self.pbVtxSelect = QtGui.QPushButton(self.tabVtxTools)
        self.pbVtxSelect.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbVtxSelect.setObjectName(_fromUtf8("pbVtxSelect"))
        self.hlVtxSelRange.addWidget(self.pbVtxSelect)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlVtxSelRange.addItem(spacerItem1)
        self.vlVtxEdition.addLayout(self.hlVtxSelRange)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlVtxEdition.addItem(spacerItem2)
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
        self.pbUpdateInf = QtGui.QPushButton(self.tabVtxValues)
        self.pbUpdateInf.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbUpdateInf.setObjectName(_fromUtf8("pbUpdateInf"))
        self.vlVtxValues.addWidget(self.pbUpdateInf)
        self.twVtxValues = QtGui.QTreeWidget(self.tabVtxValues)
        self.twVtxValues.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.twVtxValues.setIndentation(0)
        self.twVtxValues.setObjectName(_fromUtf8("twVtxValues"))
        self.twVtxValues.header().setVisible(False)
        self.vlVtxValues.addWidget(self.twVtxValues)
        self.line_4 = QtGui.QFrame(self.tabVtxValues)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.vlVtxValues.addWidget(self.line_4)
        self.gridLayout_2.addLayout(self.vlVtxValues, 0, 0, 1, 1)
        self.tabVertex.addTab(self.tabVtxValues, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.splitter, 3, 0, 1, 1)
        mwVtxMap.setCentralWidget(self.centralwidget)

        self.retranslateUi(mwVtxMap)
        self.tabVertex.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(mwVtxMap)

    def retranslateUi(self, mwVtxMap):
        mwVtxMap.setWindowTitle(_translate("mwVtxMap", "VtxMap", None))
        self.pbInit.setText(_translate("mwVtxMap", "Init", None))
        self.pbSelect.setText(_translate("mwVtxMap", "Select", None))
        self.cbSceneNodes.setText(_translate("mwVtxMap", "Scene Cloth Nodes", None))
        self.lNodeType.setText(_translate("mwVtxMap", "Node Type: ", None))
        self.lClothType.setText(_translate("mwVtxMap", "Show: ", None))
        self.cbCloth.setText(_translate("mwVtxMap", "nCloth", None))
        self.cbRigid.setText(_translate("mwVtxMap", "nRigid", None))
        self.twMapType.headerItem().setText(0, _translate("mwVtxMap", "Vertex Map Type", None))
        self.lEditType.setText(_translate("mwVtxMap", "Set All To:", None))
        self.pbNone.setText(_translate("mwVtxMap", "None", None))
        self.pbVertex.setText(_translate("mwVtxMap", "Vertex", None))
        self.pbTexture.setText(_translate("mwVtxMap", "Texture", None))
        self.lSelRange.setText(_translate("mwVtxMap", "Vertex Selection Range: ", None))
        self.pbVtxSelect.setText(_translate("mwVtxMap", "Select", None))
        self.tabVertex.setTabText(self.tabVertex.indexOf(self.tabVtxTools), _translate("mwVtxMap", "Vtx Tools", None))
        self.pbUpdateInf.setText(_translate("mwVtxMap", "Update From Scene", None))
        self.twVtxValues.headerItem().setText(0, _translate("mwVtxMap", "Index", None))
        self.twVtxValues.headerItem().setText(1, _translate("mwVtxMap", "Influence", None))
        self.tabVertex.setTabText(self.tabVertex.indexOf(self.tabVtxValues), _translate("mwVtxMap", "Vtx Values", None))

