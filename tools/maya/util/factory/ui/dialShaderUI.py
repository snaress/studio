# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\util\factory\ui\dialShader.ui'
#
# Created: Mon Dec 01 17:53:31 2014
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

class Ui_Shader(object):
    def setupUi(self, Shader):
        Shader.setObjectName(_fromUtf8("Shader"))
        Shader.resize(617, 247)
        self.centralwidget = QtGui.QWidget(Shader)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(2, -1, 2, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.bImport = QtGui.QPushButton(self.centralwidget)
        self.bImport.setObjectName(_fromUtf8("bImport"))
        self.verticalLayout.addWidget(self.bImport)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.hlShader = QtGui.QHBoxLayout()
        self.hlShader.setSpacing(0)
        self.hlShader.setObjectName(_fromUtf8("hlShader"))
        self.lShader = QtGui.QLabel(self.centralwidget)
        self.lShader.setMinimumSize(QtCore.QSize(85, 0))
        self.lShader.setMaximumSize(QtCore.QSize(85, 16777215))
        self.lShader.setObjectName(_fromUtf8("lShader"))
        self.hlShader.addWidget(self.lShader)
        self.leShader = QtGui.QLineEdit(self.centralwidget)
        self.leShader.setObjectName(_fromUtf8("leShader"))
        self.hlShader.addWidget(self.leShader)
        self.bInit = QtGui.QPushButton(self.centralwidget)
        self.bInit.setMinimumSize(QtCore.QSize(75, 0))
        self.bInit.setMaximumSize(QtCore.QSize(75, 16777215))
        self.bInit.setObjectName(_fromUtf8("bInit"))
        self.hlShader.addWidget(self.bInit)
        self.verticalLayout.addLayout(self.hlShader)
        self.hlSurfaceShader = QtGui.QHBoxLayout()
        self.hlSurfaceShader.setObjectName(_fromUtf8("hlSurfaceShader"))
        self.lSurfaceShader = QtGui.QLabel(self.centralwidget)
        self.lSurfaceShader.setMinimumSize(QtCore.QSize(90, 0))
        self.lSurfaceShader.setMaximumSize(QtCore.QSize(90, 16777215))
        self.lSurfaceShader.setObjectName(_fromUtf8("lSurfaceShader"))
        self.hlSurfaceShader.addWidget(self.lSurfaceShader)
        self.lSSValue = QtGui.QLabel(self.centralwidget)
        self.lSSValue.setObjectName(_fromUtf8("lSSValue"))
        self.hlSurfaceShader.addWidget(self.lSSValue)
        spacerItem = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlSurfaceShader.addItem(spacerItem)
        self.verticalLayout.addLayout(self.hlSurfaceShader)
        self.hlDisplaceShader = QtGui.QHBoxLayout()
        self.hlDisplaceShader.setObjectName(_fromUtf8("hlDisplaceShader"))
        self.lDisplaceShader = QtGui.QLabel(self.centralwidget)
        self.lDisplaceShader.setMinimumSize(QtCore.QSize(90, 0))
        self.lDisplaceShader.setMaximumSize(QtCore.QSize(90, 16777215))
        self.lDisplaceShader.setObjectName(_fromUtf8("lDisplaceShader"))
        self.hlDisplaceShader.addWidget(self.lDisplaceShader)
        self.lDSValue = QtGui.QLabel(self.centralwidget)
        self.lDSValue.setObjectName(_fromUtf8("lDSValue"))
        self.hlDisplaceShader.addWidget(self.lDSValue)
        spacerItem1 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlDisplaceShader.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.hlDisplaceShader)
        self.hlVolumeShader = QtGui.QHBoxLayout()
        self.hlVolumeShader.setObjectName(_fromUtf8("hlVolumeShader"))
        self.lVolumeShader = QtGui.QLabel(self.centralwidget)
        self.lVolumeShader.setMinimumSize(QtCore.QSize(90, 0))
        self.lVolumeShader.setMaximumSize(QtCore.QSize(90, 16777215))
        self.lVolumeShader.setObjectName(_fromUtf8("lVolumeShader"))
        self.hlVolumeShader.addWidget(self.lVolumeShader)
        self.lVSValue = QtGui.QLabel(self.centralwidget)
        self.lVSValue.setObjectName(_fromUtf8("lVSValue"))
        self.hlVolumeShader.addWidget(self.lVSValue)
        spacerItem2 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlVolumeShader.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.hlVolumeShader)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.rbDraft = QtGui.QRadioButton(self.centralwidget)
        self.rbDraft.setChecked(True)
        self.rbDraft.setObjectName(_fromUtf8("rbDraft"))
        self.bgQuality = QtGui.QButtonGroup(Shader)
        self.bgQuality.setObjectName(_fromUtf8("bgQuality"))
        self.bgQuality.addButton(self.rbDraft)
        self.horizontalLayout.addWidget(self.rbDraft)
        self.rbPreview = QtGui.QRadioButton(self.centralwidget)
        self.rbPreview.setObjectName(_fromUtf8("rbPreview"))
        self.bgQuality.addButton(self.rbPreview)
        self.horizontalLayout.addWidget(self.rbPreview)
        self.bParamRender = QtGui.QPushButton(self.centralwidget)
        self.bParamRender.setMinimumSize(QtCore.QSize(0, 0))
        self.bParamRender.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bParamRender.setObjectName(_fromUtf8("bParamRender"))
        self.horizontalLayout.addWidget(self.bParamRender)
        spacerItem3 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.bRender = QtGui.QPushButton(self.centralwidget)
        self.bRender.setMinimumSize(QtCore.QSize(75, 0))
        self.bRender.setMaximumSize(QtCore.QSize(75, 16777215))
        self.bRender.setObjectName(_fromUtf8("bRender"))
        self.horizontalLayout.addWidget(self.bRender)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.hlPreview = QtGui.QHBoxLayout()
        self.hlPreview.setSpacing(0)
        self.hlPreview.setObjectName(_fromUtf8("hlPreview"))
        self.lPreview = QtGui.QLabel(self.centralwidget)
        self.lPreview.setMinimumSize(QtCore.QSize(85, 0))
        self.lPreview.setMaximumSize(QtCore.QSize(85, 16777215))
        self.lPreview.setObjectName(_fromUtf8("lPreview"))
        self.hlPreview.addWidget(self.lPreview)
        self.lePreview = QtGui.QLineEdit(self.centralwidget)
        self.lePreview.setObjectName(_fromUtf8("lePreview"))
        self.hlPreview.addWidget(self.lePreview)
        self.bOpen = QtGui.QPushButton(self.centralwidget)
        self.bOpen.setMinimumSize(QtCore.QSize(75, 0))
        self.bOpen.setMaximumSize(QtCore.QSize(75, 16777215))
        self.bOpen.setObjectName(_fromUtf8("bOpen"))
        self.hlPreview.addWidget(self.bOpen)
        self.verticalLayout.addLayout(self.hlPreview)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)
        self.hlCategory = QtGui.QHBoxLayout()
        self.hlCategory.setObjectName(_fromUtf8("hlCategory"))
        self.lCategory = QtGui.QLabel(self.centralwidget)
        self.lCategory.setObjectName(_fromUtf8("lCategory"))
        self.hlCategory.addWidget(self.lCategory)
        self.cbCategory = QtGui.QComboBox(self.centralwidget)
        self.cbCategory.setModelColumn(0)
        self.cbCategory.setObjectName(_fromUtf8("cbCategory"))
        self.hlCategory.addWidget(self.cbCategory)
        spacerItem4 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hlCategory.addItem(spacerItem4)
        self.lSubCategory = QtGui.QLabel(self.centralwidget)
        self.lSubCategory.setObjectName(_fromUtf8("lSubCategory"))
        self.hlCategory.addWidget(self.lSubCategory)
        self.cbSubCategory = QtGui.QComboBox(self.centralwidget)
        self.cbSubCategory.setModelColumn(0)
        self.cbSubCategory.setObjectName(_fromUtf8("cbSubCategory"))
        self.hlCategory.addWidget(self.cbSubCategory)
        spacerItem5 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlCategory.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.hlCategory)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.hlShaderName = QtGui.QHBoxLayout()
        self.hlShaderName.setObjectName(_fromUtf8("hlShaderName"))
        self.lShaderName = QtGui.QLabel(self.centralwidget)
        self.lShaderName.setObjectName(_fromUtf8("lShaderName"))
        self.hlShaderName.addWidget(self.lShaderName)
        self.leShaderName = QtGui.QLineEdit(self.centralwidget)
        self.leShaderName.setObjectName(_fromUtf8("leShaderName"))
        self.hlShaderName.addWidget(self.leShaderName)
        self.bCheck = QtGui.QPushButton(self.centralwidget)
        self.bCheck.setMinimumSize(QtCore.QSize(75, 0))
        self.bCheck.setMaximumSize(QtCore.QSize(75, 16777215))
        self.bCheck.setObjectName(_fromUtf8("bCheck"))
        self.hlShaderName.addWidget(self.bCheck)
        self.verticalLayout.addLayout(self.hlShaderName)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lCheckResult = QtGui.QLabel(self.centralwidget)
        self.lCheckResult.setObjectName(_fromUtf8("lCheckResult"))
        self.horizontalLayout_2.addWidget(self.lCheckResult)
        self.lCheckValue = QtGui.QLabel(self.centralwidget)
        self.lCheckValue.setText(_fromUtf8(""))
        self.lCheckValue.setObjectName(_fromUtf8("lCheckValue"))
        self.horizontalLayout_2.addWidget(self.lCheckValue)
        spacerItem6 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout.addWidget(self.line_5)
        self.hlEdit = QtGui.QHBoxLayout()
        self.hlEdit.setObjectName(_fromUtf8("hlEdit"))
        spacerItem7 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlEdit.addItem(spacerItem7)
        self.bSave = QtGui.QPushButton(self.centralwidget)
        self.bSave.setMinimumSize(QtCore.QSize(75, 0))
        self.bSave.setMaximumSize(QtCore.QSize(75, 16777215))
        self.bSave.setObjectName(_fromUtf8("bSave"))
        self.hlEdit.addWidget(self.bSave)
        self.bCancel = QtGui.QPushButton(self.centralwidget)
        self.bCancel.setMinimumSize(QtCore.QSize(75, 0))
        self.bCancel.setMaximumSize(QtCore.QSize(75, 16777215))
        self.bCancel.setObjectName(_fromUtf8("bCancel"))
        self.hlEdit.addWidget(self.bCancel)
        self.verticalLayout.addLayout(self.hlEdit)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Shader.setCentralWidget(self.centralwidget)

        self.retranslateUi(Shader)
        QtCore.QMetaObject.connectSlotsByName(Shader)

    def retranslateUi(self, Shader):
        Shader.setWindowTitle(_translate("Shader", "Shader", None))
        self.bImport.setText(_translate("Shader", "Import Presentoir", None))
        self.lShader.setText(_translate("Shader", "Selected Shader: ", None))
        self.bInit.setText(_translate("Shader", "Init", None))
        self.lSurfaceShader.setText(_translate("Shader", "Surface Shader:", None))
        self.lSSValue.setText(_translate("Shader", "None", None))
        self.lDisplaceShader.setText(_translate("Shader", "Displace Shader:", None))
        self.lDSValue.setText(_translate("Shader", "None", None))
        self.lVolumeShader.setText(_translate("Shader", "Volume Shader:", None))
        self.lVSValue.setText(_translate("Shader", "None", None))
        self.rbDraft.setText(_translate("Shader", "Draft", None))
        self.rbPreview.setText(_translate("Shader", "Preview", None))
        self.bParamRender.setText(_translate("Shader", "Param Render", None))
        self.bRender.setText(_translate("Shader", "Render", None))
        self.lPreview.setText(_translate("Shader", "Preview Image: ", None))
        self.bOpen.setText(_translate("Shader", "Open", None))
        self.lCategory.setText(_translate("Shader", "Category: ", None))
        self.lSubCategory.setText(_translate("Shader", "Sub Category: ", None))
        self.lShaderName.setText(_translate("Shader", "Shader Name: ", None))
        self.bCheck.setText(_translate("Shader", "Check", None))
        self.lCheckResult.setText(_translate("Shader", "Check Result: ", None))
        self.bSave.setText(_translate("Shader", "Save", None))
        self.bCancel.setText(_translate("Shader", "Cancel", None))

