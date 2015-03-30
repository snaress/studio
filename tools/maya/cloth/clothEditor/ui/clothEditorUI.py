# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothEditor\ui\clothEditor.ui'
#
# Created: Mon Mar 30 00:58:04 2015
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

class Ui_mwClothEditor(object):
    def setupUi(self, mwClothEditor):
        mwClothEditor.setObjectName(_fromUtf8("mwClothEditor"))
        mwClothEditor.resize(711, 470)
        self.centralwidget = QtGui.QWidget(mwClothEditor)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.qfSceneNodes = QtGui.QFrame(self.splitter_2)
        self.qfSceneNodes.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qfSceneNodes.setObjectName(_fromUtf8("qfSceneNodes"))
        self.vlSceneNodes = QtGui.QVBoxLayout(self.qfSceneNodes)
        self.vlSceneNodes.setSpacing(0)
        self.vlSceneNodes.setMargin(0)
        self.vlSceneNodes.setObjectName(_fromUtf8("vlSceneNodes"))
        self.tabClothEditor = QtGui.QTabWidget(self.splitter_2)
        self.tabClothEditor.setObjectName(_fromUtf8("tabClothEditor"))
        self.tiPreset = QtGui.QWidget()
        self.tiPreset.setObjectName(_fromUtf8("tiPreset"))
        self.tabClothEditor.addTab(self.tiPreset, _fromUtf8(""))
        self.tiVtxMap = QtGui.QWidget()
        self.tiVtxMap.setObjectName(_fromUtf8("tiVtxMap"))
        self.glVtxMap = QtGui.QGridLayout(self.tiVtxMap)
        self.glVtxMap.setMargin(0)
        self.glVtxMap.setSpacing(0)
        self.glVtxMap.setObjectName(_fromUtf8("glVtxMap"))
        self.vlVtxMap = QtGui.QVBoxLayout()
        self.vlVtxMap.setSpacing(0)
        self.vlVtxMap.setObjectName(_fromUtf8("vlVtxMap"))
        self.glVtxMap.addLayout(self.vlVtxMap, 0, 0, 1, 1)
        self.tabClothEditor.addTab(self.tiVtxMap, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.splitter_2, 0, 0, 1, 1)
        mwClothEditor.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(mwClothEditor)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 711, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.mHelp = QtGui.QMenu(self.menuBar)
        self.mHelp.setObjectName(_fromUtf8("mHelp"))
        mwClothEditor.setMenuBar(self.menuBar)
        self.miNCloth = QtGui.QAction(mwClothEditor)
        self.miNCloth.setCheckable(True)
        self.miNCloth.setChecked(True)
        self.miNCloth.setObjectName(_fromUtf8("miNCloth"))
        self.miNRigid = QtGui.QAction(mwClothEditor)
        self.miNRigid.setCheckable(True)
        self.miNRigid.setChecked(True)
        self.miNRigid.setObjectName(_fromUtf8("miNRigid"))
        self.miRfSceneNodes = QtGui.QAction(mwClothEditor)
        self.miRfSceneNodes.setObjectName(_fromUtf8("miRfSceneNodes"))
        self.actionRefresh = QtGui.QAction(mwClothEditor)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.miToolTips = QtGui.QAction(mwClothEditor)
        self.miToolTips.setCheckable(True)
        self.miToolTips.setChecked(False)
        self.miToolTips.setObjectName(_fromUtf8("miToolTips"))
        self.mHelp.addAction(self.miToolTips)
        self.menuBar.addAction(self.mHelp.menuAction())

        self.retranslateUi(mwClothEditor)
        self.tabClothEditor.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(mwClothEditor)

    def retranslateUi(self, mwClothEditor):
        mwClothEditor.setWindowTitle(_translate("mwClothEditor", "Cloth Editor", None))
        self.tabClothEditor.setTabText(self.tabClothEditor.indexOf(self.tiPreset), _translate("mwClothEditor", "Preset", None))
        self.tabClothEditor.setTabText(self.tabClothEditor.indexOf(self.tiVtxMap), _translate("mwClothEditor", "VtxMap", None))
        self.mHelp.setTitle(_translate("mwClothEditor", "Help", None))
        self.miNCloth.setText(_translate("mwClothEditor", "nCloth", None))
        self.miNRigid.setText(_translate("mwClothEditor", "nRigid", None))
        self.miRfSceneNodes.setText(_translate("mwClothEditor", "Scene Nodes", None))
        self.actionRefresh.setText(_translate("mwClothEditor", "Refresh", None))
        self.miToolTips.setText(_translate("mwClothEditor", "ToolTips", None))

