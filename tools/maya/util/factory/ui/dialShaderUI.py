# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\tools\maya\util\factory\ui\dialShader.ui'
#
# Created: Sat Nov 29 04:30:36 2014
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
        Shader.resize(524, 134)
        self.centralwidget = QtGui.QWidget(Shader)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(1)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)
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
        self.bInit.setObjectName(_fromUtf8("bInit"))
        self.hlShader.addWidget(self.bInit)
        self.gridLayout.addLayout(self.hlShader, 2, 0, 1, 1)
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
        self.bOpen.setObjectName(_fromUtf8("bOpen"))
        self.hlPreview.addWidget(self.bOpen)
        self.gridLayout.addLayout(self.hlPreview, 3, 0, 1, 1)
        self.hlCategory = QtGui.QHBoxLayout()
        self.hlCategory.setObjectName(_fromUtf8("hlCategory"))
        self.lCategory = QtGui.QLabel(self.centralwidget)
        self.lCategory.setObjectName(_fromUtf8("lCategory"))
        self.hlCategory.addWidget(self.lCategory)
        self.cbCategory = QtGui.QComboBox(self.centralwidget)
        self.cbCategory.setModelColumn(0)
        self.cbCategory.setObjectName(_fromUtf8("cbCategory"))
        self.hlCategory.addWidget(self.cbCategory)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.hlCategory.addItem(spacerItem)
        self.lSubCategory = QtGui.QLabel(self.centralwidget)
        self.lSubCategory.setObjectName(_fromUtf8("lSubCategory"))
        self.hlCategory.addWidget(self.lSubCategory)
        self.cbSubCategory = QtGui.QComboBox(self.centralwidget)
        self.cbSubCategory.setModelColumn(0)
        self.cbSubCategory.setObjectName(_fromUtf8("cbSubCategory"))
        self.hlCategory.addWidget(self.cbSubCategory)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlCategory.addItem(spacerItem1)
        self.gridLayout.addLayout(self.hlCategory, 4, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 5, 0, 1, 1)
        self.hlEdit = QtGui.QHBoxLayout()
        self.hlEdit.setObjectName(_fromUtf8("hlEdit"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlEdit.addItem(spacerItem2)
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
        self.gridLayout.addLayout(self.hlEdit, 6, 0, 1, 1)
        Shader.setCentralWidget(self.centralwidget)

        self.retranslateUi(Shader)
        QtCore.QMetaObject.connectSlotsByName(Shader)

    def retranslateUi(self, Shader):
        Shader.setWindowTitle(_translate("Shader", "Shader", None))
        self.pushButton.setText(_translate("Shader", "Import Presentoir", None))
        self.lShader.setText(_translate("Shader", "Selected Shader: ", None))
        self.bInit.setText(_translate("Shader", "Init", None))
        self.lPreview.setText(_translate("Shader", "Preview Image: ", None))
        self.bOpen.setText(_translate("Shader", "Open", None))
        self.lCategory.setText(_translate("Shader", "Category: ", None))
        self.lSubCategory.setText(_translate("Shader", "Sub Category: ", None))
        self.bSave.setText(_translate("Shader", "Save", None))
        self.bCancel.setText(_translate("Shader", "Cancel", None))

