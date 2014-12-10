# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\camera\camPrez\ui\camPrez.ui'
#
# Created: Wed Dec 10 09:29:08 2014
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

class Ui_mwCamPrez(object):
    def setupUi(self, mwCamPrez):
        mwCamPrez.setObjectName(_fromUtf8("mwCamPrez"))
        mwCamPrez.resize(333, 97)
        self.centralwidget = QtGui.QWidget(mwCamPrez)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(1, 0, 1, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabTurn = QtGui.QWidget()
        self.tabTurn.setObjectName(_fromUtf8("tabTurn"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabTurn)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.bCreateCamTurn = QtGui.QPushButton(self.tabTurn)
        self.bCreateCamTurn.setObjectName(_fromUtf8("bCreateCamTurn"))
        self.gridLayout_2.addWidget(self.bCreateCamTurn, 4, 0, 1, 1)
        self.line = QtGui.QFrame(self.tabTurn)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        self.hlTurnAxe = QtGui.QHBoxLayout()
        self.hlTurnAxe.setSpacing(12)
        self.hlTurnAxe.setObjectName(_fromUtf8("hlTurnAxe"))
        self.lTurnFrontAxe = QtGui.QLabel(self.tabTurn)
        self.lTurnFrontAxe.setObjectName(_fromUtf8("lTurnFrontAxe"))
        self.hlTurnAxe.addWidget(self.lTurnFrontAxe)
        self.cbTurnX = QtGui.QCheckBox(self.tabTurn)
        self.cbTurnX.setObjectName(_fromUtf8("cbTurnX"))
        self.bgTurnFrontAxe = QtGui.QButtonGroup(mwCamPrez)
        self.bgTurnFrontAxe.setObjectName(_fromUtf8("bgTurnFrontAxe"))
        self.bgTurnFrontAxe.addButton(self.cbTurnX)
        self.hlTurnAxe.addWidget(self.cbTurnX)
        self.cbTurnY = QtGui.QCheckBox(self.tabTurn)
        self.cbTurnY.setChecked(False)
        self.cbTurnY.setObjectName(_fromUtf8("cbTurnY"))
        self.bgTurnFrontAxe.addButton(self.cbTurnY)
        self.hlTurnAxe.addWidget(self.cbTurnY)
        self.cbTurnZ = QtGui.QCheckBox(self.tabTurn)
        self.cbTurnZ.setChecked(True)
        self.cbTurnZ.setObjectName(_fromUtf8("cbTurnZ"))
        self.bgTurnFrontAxe.addButton(self.cbTurnZ)
        self.hlTurnAxe.addWidget(self.cbTurnZ)
        spacerItem = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlTurnAxe.addItem(spacerItem)
        self.cbTurnInvert = QtGui.QCheckBox(self.tabTurn)
        self.cbTurnInvert.setMinimumSize(QtCore.QSize(80, 0))
        self.cbTurnInvert.setObjectName(_fromUtf8("cbTurnInvert"))
        self.hlTurnAxe.addWidget(self.cbTurnInvert)
        self.gridLayout_2.addLayout(self.hlTurnAxe, 0, 0, 1, 1)
        self.hlTurnDuration = QtGui.QHBoxLayout()
        self.hlTurnDuration.setSpacing(12)
        self.hlTurnDuration.setObjectName(_fromUtf8("hlTurnDuration"))
        self.lTurnDuration = QtGui.QLabel(self.tabTurn)
        self.lTurnDuration.setObjectName(_fromUtf8("lTurnDuration"))
        self.hlTurnDuration.addWidget(self.lTurnDuration)
        self.sbTurnDuration = QtGui.QSpinBox(self.tabTurn)
        self.sbTurnDuration.setMinimumSize(QtCore.QSize(60, 0))
        self.sbTurnDuration.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.sbTurnDuration.setMaximum(10000)
        self.sbTurnDuration.setProperty("value", 120)
        self.sbTurnDuration.setObjectName(_fromUtf8("sbTurnDuration"))
        self.hlTurnDuration.addWidget(self.sbTurnDuration)
        self.lTurnFrames = QtGui.QLabel(self.tabTurn)
        self.lTurnFrames.setObjectName(_fromUtf8("lTurnFrames"))
        self.hlTurnDuration.addWidget(self.lTurnFrames)
        spacerItem1 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlTurnDuration.addItem(spacerItem1)
        self.cbInvertRotate = QtGui.QCheckBox(self.tabTurn)
        self.cbInvertRotate.setMinimumSize(QtCore.QSize(80, 0))
        self.cbInvertRotate.setObjectName(_fromUtf8("cbInvertRotate"))
        self.hlTurnDuration.addWidget(self.cbInvertRotate)
        self.gridLayout_2.addLayout(self.hlTurnDuration, 2, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.tabTurn)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tabTurn, _fromUtf8(""))
        self.tabQuadra = QtGui.QWidget()
        self.tabQuadra.setObjectName(_fromUtf8("tabQuadra"))
        self.tabWidget.addTab(self.tabQuadra, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        mwCamPrez.setCentralWidget(self.centralwidget)

        self.retranslateUi(mwCamPrez)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mwCamPrez)

    def retranslateUi(self, mwCamPrez):
        mwCamPrez.setWindowTitle(_translate("mwCamPrez", "CamPrez", None))
        self.bCreateCamTurn.setText(_translate("mwCamPrez", "Create Camera Turn", None))
        self.lTurnFrontAxe.setText(_translate("mwCamPrez", "Front Axe:", None))
        self.cbTurnX.setText(_translate("mwCamPrez", "X", None))
        self.cbTurnY.setText(_translate("mwCamPrez", "Y", None))
        self.cbTurnZ.setText(_translate("mwCamPrez", "Z", None))
        self.cbTurnInvert.setText(_translate("mwCamPrez", "Invert Axe", None))
        self.lTurnDuration.setText(_translate("mwCamPrez", "Duration = ", None))
        self.lTurnFrames.setText(_translate("mwCamPrez", "(Frame)", None))
        self.cbInvertRotate.setText(_translate("mwCamPrez", "Invert Turn", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTurn), _translate("mwCamPrez", "Turn", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabQuadra), _translate("mwCamPrez", "Quadra", None))

