# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\cloth\clothEditor\ui\wgSceneNodes.ui'
#
# Created: Sat Mar 28 22:43:09 2015
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
        wgSceneNodes.resize(314, 626)
        self.gridLayout = QtGui.QGridLayout(wgSceneNodes)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(wgSceneNodes)
        self.splitter.setFrameShape(QtGui.QFrame.StyledPanel)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lSceneNodes = QtGui.QLabel(self.layoutWidget)
        self.lSceneNodes.setMinimumSize(QtCore.QSize(0, 0))
        self.lSceneNodes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lSceneNodes.setFont(font)
        self.lSceneNodes.setAlignment(QtCore.Qt.AlignCenter)
        self.lSceneNodes.setObjectName(_fromUtf8("lSceneNodes"))
        self.horizontalLayout.addWidget(self.lSceneNodes)
        self.pbRefresh = QtGui.QPushButton(self.layoutWidget)
        self.pbRefresh.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pbRefresh.setObjectName(_fromUtf8("pbRefresh"))
        self.horizontalLayout.addWidget(self.pbRefresh)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.line_4 = QtGui.QFrame(self.layoutWidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)
        self.twSceneNodes = QtGui.QTreeWidget(self.layoutWidget)
        self.twSceneNodes.setIndentation(20)
        self.twSceneNodes.setColumnCount(1)
        self.twSceneNodes.setObjectName(_fromUtf8("twSceneNodes"))
        self.twSceneNodes.headerItem().setText(0, _fromUtf8("1"))
        self.twSceneNodes.header().setVisible(False)
        self.verticalLayout.addWidget(self.twSceneNodes)
        self.hlShowByType = QtGui.QHBoxLayout()
        self.hlShowByType.setSpacing(2)
        self.hlShowByType.setContentsMargins(-1, -1, -1, 0)
        self.hlShowByType.setObjectName(_fromUtf8("hlShowByType"))
        self.lClothType = QtGui.QLabel(self.layoutWidget)
        self.lClothType.setMinimumSize(QtCore.QSize(0, 20))
        self.lClothType.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lClothType.setObjectName(_fromUtf8("lClothType"))
        self.hlShowByType.addWidget(self.lClothType)
        self.cbCloth = QtGui.QCheckBox(self.layoutWidget)
        self.cbCloth.setMinimumSize(QtCore.QSize(0, 20))
        self.cbCloth.setMaximumSize(QtCore.QSize(60, 16777215))
        self.cbCloth.setChecked(True)
        self.cbCloth.setObjectName(_fromUtf8("cbCloth"))
        self.hlShowByType.addWidget(self.cbCloth)
        self.cbRigid = QtGui.QCheckBox(self.layoutWidget)
        self.cbRigid.setMinimumSize(QtCore.QSize(0, 20))
        self.cbRigid.setMaximumSize(QtCore.QSize(60, 16777215))
        self.cbRigid.setChecked(True)
        self.cbRigid.setObjectName(_fromUtf8("cbRigid"))
        self.hlShowByType.addWidget(self.cbRigid)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlShowByType.addItem(spacerItem)
        self.cbFilters = QtGui.QCheckBox(self.layoutWidget)
        self.cbFilters.setMinimumSize(QtCore.QSize(0, 20))
        self.cbFilters.setMaximumSize(QtCore.QSize(60, 16777215))
        self.cbFilters.setObjectName(_fromUtf8("cbFilters"))
        self.hlShowByType.addWidget(self.cbFilters)
        self.verticalLayout.addLayout(self.hlShowByType)
        self.twFilters = QtGui.QTreeWidget(self.splitter)
        self.twFilters.setIndentation(0)
        self.twFilters.setColumnCount(2)
        self.twFilters.setObjectName(_fromUtf8("twFilters"))
        self.twFilters.headerItem().setText(0, _fromUtf8("1"))
        self.twFilters.headerItem().setText(1, _fromUtf8("2"))
        self.twFilters.header().setVisible(False)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(wgSceneNodes)
        QtCore.QMetaObject.connectSlotsByName(wgSceneNodes)

    def retranslateUi(self, wgSceneNodes):
        wgSceneNodes.setWindowTitle(_translate("wgSceneNodes", "SceneNodes", None))
        self.lSceneNodes.setText(_translate("wgSceneNodes", "Scene Nodes", None))
        self.pbRefresh.setText(_translate("wgSceneNodes", "Refresh", None))
        self.lClothType.setText(_translate("wgSceneNodes", "Show: ", None))
        self.cbCloth.setText(_translate("wgSceneNodes", "nCloth", None))
        self.cbRigid.setText(_translate("wgSceneNodes", "nRigid", None))
        self.cbFilters.setText(_translate("wgSceneNodes", "Filters", None))
