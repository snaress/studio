# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\camera\camPrez\ui\camPrez.ui'
#
# Created: Sat Dec 13 17:04:55 2014
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
        mwCamPrez.resize(472, 259)
        self.centralwidget = QtGui.QWidget(mwCamPrez)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.vlRender = QtGui.QVBoxLayout()
        self.vlRender.setSpacing(0)
        self.vlRender.setContentsMargins(2, 0, 2, 0)
        self.vlRender.setObjectName(_fromUtf8("vlRender"))
        self.hlParams = QtGui.QHBoxLayout()
        self.hlParams.setSpacing(2)
        self.hlParams.setContentsMargins(-1, 0, -1, -1)
        self.hlParams.setObjectName(_fromUtf8("hlParams"))
        self.bRefreshInfo = QtGui.QPushButton(self.centralwidget)
        self.bRefreshInfo.setObjectName(_fromUtf8("bRefreshInfo"))
        self.hlParams.addWidget(self.bRefreshInfo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlParams.addItem(spacerItem)
        self.lRenderer = QtGui.QLabel(self.centralwidget)
        self.lRenderer.setObjectName(_fromUtf8("lRenderer"))
        self.hlParams.addWidget(self.lRenderer)
        self.cbMentalRay = QtGui.QCheckBox(self.centralwidget)
        self.cbMentalRay.setChecked(True)
        self.cbMentalRay.setObjectName(_fromUtf8("cbMentalRay"))
        self.bgRenderer = QtGui.QButtonGroup(mwCamPrez)
        self.bgRenderer.setObjectName(_fromUtf8("bgRenderer"))
        self.bgRenderer.addButton(self.cbMentalRay)
        self.hlParams.addWidget(self.cbMentalRay)
        self.cbTurtle = QtGui.QCheckBox(self.centralwidget)
        self.cbTurtle.setObjectName(_fromUtf8("cbTurtle"))
        self.bgRenderer.addButton(self.cbTurtle)
        self.hlParams.addWidget(self.cbTurtle)
        self.bParamRender = QtGui.QPushButton(self.centralwidget)
        self.bParamRender.setObjectName(_fromUtf8("bParamRender"))
        self.hlParams.addWidget(self.bParamRender)
        self.vlRender.addLayout(self.hlParams)
        self.hlRenderPath = QtGui.QHBoxLayout()
        self.hlRenderPath.setSpacing(2)
        self.hlRenderPath.setObjectName(_fromUtf8("hlRenderPath"))
        self.lRenderPath = QtGui.QLabel(self.centralwidget)
        self.lRenderPath.setMinimumSize(QtCore.QSize(75, 0))
        self.lRenderPath.setMaximumSize(QtCore.QSize(75, 20))
        self.lRenderPath.setObjectName(_fromUtf8("lRenderPath"))
        self.hlRenderPath.addWidget(self.lRenderPath)
        self.leRenderPath = QtGui.QLineEdit(self.centralwidget)
        self.leRenderPath.setReadOnly(True)
        self.leRenderPath.setObjectName(_fromUtf8("leRenderPath"))
        self.hlRenderPath.addWidget(self.leRenderPath)
        self.vlRender.addLayout(self.hlRenderPath)
        self.hlImagePath = QtGui.QHBoxLayout()
        self.hlImagePath.setSpacing(2)
        self.hlImagePath.setObjectName(_fromUtf8("hlImagePath"))
        self.lImagePath = QtGui.QLabel(self.centralwidget)
        self.lImagePath.setMinimumSize(QtCore.QSize(75, 0))
        self.lImagePath.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lImagePath.setObjectName(_fromUtf8("lImagePath"))
        self.hlImagePath.addWidget(self.lImagePath)
        self.leImagePath = QtGui.QLineEdit(self.centralwidget)
        self.leImagePath.setReadOnly(False)
        self.leImagePath.setObjectName(_fromUtf8("leImagePath"))
        self.hlImagePath.addWidget(self.leImagePath)
        self.bOpen = QtGui.QPushButton(self.centralwidget)
        self.bOpen.setMinimumSize(QtCore.QSize(60, 0))
        self.bOpen.setMaximumSize(QtCore.QSize(60, 16777215))
        self.bOpen.setObjectName(_fromUtf8("bOpen"))
        self.hlImagePath.addWidget(self.bOpen)
        self.vlRender.addLayout(self.hlImagePath)
        self.hlImageName = QtGui.QHBoxLayout()
        self.hlImageName.setSpacing(2)
        self.hlImageName.setContentsMargins(0, 0, -1, -1)
        self.hlImageName.setObjectName(_fromUtf8("hlImageName"))
        self.lImageName = QtGui.QLabel(self.centralwidget)
        self.lImageName.setMinimumSize(QtCore.QSize(75, 0))
        self.lImageName.setMaximumSize(QtCore.QSize(75, 20))
        self.lImageName.setObjectName(_fromUtf8("lImageName"))
        self.hlImageName.addWidget(self.lImageName)
        self.leImageName = QtGui.QLineEdit(self.centralwidget)
        self.leImageName.setObjectName(_fromUtf8("leImageName"))
        self.hlImageName.addWidget(self.leImageName)
        self.sbPadding = QtGui.QSpinBox(self.centralwidget)
        self.sbPadding.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.sbPadding.setMaximum(12)
        self.sbPadding.setProperty("value", 4)
        self.sbPadding.setObjectName(_fromUtf8("sbPadding"))
        self.hlImageName.addWidget(self.sbPadding)
        self.cbImageExt = QtGui.QComboBox(self.centralwidget)
        self.cbImageExt.setMinimumSize(QtCore.QSize(60, 0))
        self.cbImageExt.setMaximumSize(QtCore.QSize(60, 16777215))
        self.cbImageExt.setObjectName(_fromUtf8("cbImageExt"))
        self.hlImageName.addWidget(self.cbImageExt)
        self.vlRender.addLayout(self.hlImageName)
        self.hlImageSize = QtGui.QHBoxLayout()
        self.hlImageSize.setSpacing(2)
        self.hlImageSize.setContentsMargins(-1, -1, -1, 0)
        self.hlImageSize.setObjectName(_fromUtf8("hlImageSize"))
        self.lImageSize = QtGui.QLabel(self.centralwidget)
        self.lImageSize.setMinimumSize(QtCore.QSize(75, 0))
        self.lImageSize.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lImageSize.setObjectName(_fromUtf8("lImageSize"))
        self.hlImageSize.addWidget(self.lImageSize)
        self.lWidth = QtGui.QLabel(self.centralwidget)
        self.lWidth.setObjectName(_fromUtf8("lWidth"))
        self.hlImageSize.addWidget(self.lWidth)
        self.sbWidth = QtGui.QSpinBox(self.centralwidget)
        self.sbWidth.setMinimumSize(QtCore.QSize(60, 0))
        self.sbWidth.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sbWidth.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.sbWidth.setPrefix(_fromUtf8(""))
        self.sbWidth.setMaximum(12000)
        self.sbWidth.setProperty("value", 2000)
        self.sbWidth.setObjectName(_fromUtf8("sbWidth"))
        self.hlImageSize.addWidget(self.sbWidth)
        self.lHeight = QtGui.QLabel(self.centralwidget)
        self.lHeight.setObjectName(_fromUtf8("lHeight"))
        self.hlImageSize.addWidget(self.lHeight)
        self.sbHeight = QtGui.QSpinBox(self.centralwidget)
        self.sbHeight.setMinimumSize(QtCore.QSize(60, 0))
        self.sbHeight.setMaximumSize(QtCore.QSize(60, 16777215))
        self.sbHeight.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.sbHeight.setPrefix(_fromUtf8(""))
        self.sbHeight.setMaximum(12000)
        self.sbHeight.setProperty("value", 2000)
        self.sbHeight.setObjectName(_fromUtf8("sbHeight"))
        self.hlImageSize.addWidget(self.sbHeight)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlImageSize.addItem(spacerItem1)
        self.lByFrame = QtGui.QLabel(self.centralwidget)
        self.lByFrame.setObjectName(_fromUtf8("lByFrame"))
        self.hlImageSize.addWidget(self.lByFrame)
        self.sbByFrame = QtGui.QSpinBox(self.centralwidget)
        self.sbByFrame.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.sbByFrame.setProperty("value", 1)
        self.sbByFrame.setObjectName(_fromUtf8("sbByFrame"))
        self.hlImageSize.addWidget(self.sbByFrame)
        self.vlRender.addLayout(self.hlImageSize)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.vlRender.addWidget(self.line_4)
        self.hlResult = QtGui.QHBoxLayout()
        self.hlResult.setSpacing(2)
        self.hlResult.setContentsMargins(-1, 0, -1, -1)
        self.hlResult.setObjectName(_fromUtf8("hlResult"))
        self.lResult = QtGui.QLabel(self.centralwidget)
        self.lResult.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lResult.setObjectName(_fromUtf8("lResult"))
        self.hlResult.addWidget(self.lResult)
        self.lResultVal = QtGui.QLabel(self.centralwidget)
        self.lResultVal.setText(_fromUtf8(""))
        self.lResultVal.setWordWrap(True)
        self.lResultVal.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lResultVal.setObjectName(_fromUtf8("lResultVal"))
        self.hlResult.addWidget(self.lResultVal)
        self.vlRender.addLayout(self.hlResult)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.vlRender.addWidget(self.line_5)
        self.gridLayout.addLayout(self.vlRender, 2, 0, 1, 1)
        self.bRender = QtGui.QPushButton(self.centralwidget)
        self.bRender.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bRender.setObjectName(_fromUtf8("bRender"))
        self.gridLayout.addWidget(self.bRender, 3, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabTurn = QtGui.QWidget()
        self.tabTurn.setObjectName(_fromUtf8("tabTurn"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabTurn)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.bCreateCamTurn = QtGui.QPushButton(self.tabTurn)
        self.bCreateCamTurn.setMaximumSize(QtCore.QSize(16777215, 20))
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
        spacerItem2 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlTurnAxe.addItem(spacerItem2)
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
        spacerItem3 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlTurnDuration.addItem(spacerItem3)
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
        self.bRefreshInfo.setText(_translate("mwCamPrez", "Refresh Info", None))
        self.lRenderer.setText(_translate("mwCamPrez", "Renderer: ", None))
        self.cbMentalRay.setText(_translate("mwCamPrez", "MentalRay", None))
        self.cbTurtle.setText(_translate("mwCamPrez", "Turtle", None))
        self.bParamRender.setText(_translate("mwCamPrez", "Param Render", None))
        self.lRenderPath.setText(_translate("mwCamPrez", "Render Path: ", None))
        self.lImagePath.setText(_translate("mwCamPrez", "Image Path: ", None))
        self.bOpen.setText(_translate("mwCamPrez", "Open", None))
        self.lImageName.setText(_translate("mwCamPrez", "Image Name:", None))
        self.sbPadding.setPrefix(_translate("mwCamPrez", "Padding: ", None))
        self.lImageSize.setText(_translate("mwCamPrez", "Image Size: ", None))
        self.lWidth.setText(_translate("mwCamPrez", "Width: ", None))
        self.lHeight.setText(_translate("mwCamPrez", "Height: ", None))
        self.lByFrame.setText(_translate("mwCamPrez", "By Frame: ", None))
        self.lResult.setText(_translate("mwCamPrez", "Result: ", None))
        self.bRender.setText(_translate("mwCamPrez", "Render Previz", None))
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

