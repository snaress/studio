# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgDataAssetCasting.ui'
#
# Created: Sun Jun 28 18:07:32 2015
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

class Ui_wgDataAssetCasting(object):
    def setupUi(self, wgDataAssetCasting):
        wgDataAssetCasting.setObjectName(_fromUtf8("wgDataAssetCasting"))
        wgDataAssetCasting.resize(220, 110)
        self.gridLayout = QtGui.QGridLayout(wgDataAssetCasting)
        self.gridLayout.setMargin(0)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hlAssetEntity = QtGui.QHBoxLayout()
        self.hlAssetEntity.setSpacing(2)
        self.hlAssetEntity.setObjectName(_fromUtf8("hlAssetEntity"))
        self.lAssetEntity = QtGui.QLabel(wgDataAssetCasting)
        self.lAssetEntity.setMinimumSize(QtCore.QSize(65, 0))
        self.lAssetEntity.setMaximumSize(QtCore.QSize(65, 16777215))
        self.lAssetEntity.setObjectName(_fromUtf8("lAssetEntity"))
        self.hlAssetEntity.addWidget(self.lAssetEntity)
        self.leAssetEntity = QtGui.QLineEdit(wgDataAssetCasting)
        self.leAssetEntity.setText(_fromUtf8(""))
        self.leAssetEntity.setFrame(False)
        self.leAssetEntity.setReadOnly(True)
        self.leAssetEntity.setObjectName(_fromUtf8("leAssetEntity"))
        self.hlAssetEntity.addWidget(self.leAssetEntity)
        self.gridLayout.addLayout(self.hlAssetEntity, 0, 0, 1, 1)
        self.hlAssetType = QtGui.QHBoxLayout()
        self.hlAssetType.setSpacing(2)
        self.hlAssetType.setObjectName(_fromUtf8("hlAssetType"))
        self.lAssetType = QtGui.QLabel(wgDataAssetCasting)
        self.lAssetType.setMinimumSize(QtCore.QSize(65, 0))
        self.lAssetType.setMaximumSize(QtCore.QSize(65, 16777215))
        self.lAssetType.setObjectName(_fromUtf8("lAssetType"))
        self.hlAssetType.addWidget(self.lAssetType)
        self.leAssetType = QtGui.QLineEdit(wgDataAssetCasting)
        self.leAssetType.setText(_fromUtf8(""))
        self.leAssetType.setFrame(False)
        self.leAssetType.setReadOnly(True)
        self.leAssetType.setObjectName(_fromUtf8("leAssetType"))
        self.hlAssetType.addWidget(self.leAssetType)
        self.gridLayout.addLayout(self.hlAssetType, 1, 0, 1, 1)
        self.hlAssetSpec = QtGui.QHBoxLayout()
        self.hlAssetSpec.setSpacing(2)
        self.hlAssetSpec.setObjectName(_fromUtf8("hlAssetSpec"))
        self.lAssetSpec = QtGui.QLabel(wgDataAssetCasting)
        self.lAssetSpec.setMinimumSize(QtCore.QSize(65, 0))
        self.lAssetSpec.setMaximumSize(QtCore.QSize(65, 16777215))
        self.lAssetSpec.setObjectName(_fromUtf8("lAssetSpec"))
        self.hlAssetSpec.addWidget(self.lAssetSpec)
        self.leAssetSpec = QtGui.QLineEdit(wgDataAssetCasting)
        self.leAssetSpec.setText(_fromUtf8(""))
        self.leAssetSpec.setFrame(False)
        self.leAssetSpec.setReadOnly(True)
        self.leAssetSpec.setObjectName(_fromUtf8("leAssetSpec"))
        self.hlAssetSpec.addWidget(self.leAssetSpec)
        self.gridLayout.addLayout(self.hlAssetSpec, 2, 0, 1, 1)
        self.hlAssetName = QtGui.QHBoxLayout()
        self.hlAssetName.setSpacing(2)
        self.hlAssetName.setObjectName(_fromUtf8("hlAssetName"))
        self.lAssetName = QtGui.QLabel(wgDataAssetCasting)
        self.lAssetName.setMinimumSize(QtCore.QSize(65, 0))
        self.lAssetName.setMaximumSize(QtCore.QSize(65, 16777215))
        self.lAssetName.setObjectName(_fromUtf8("lAssetName"))
        self.hlAssetName.addWidget(self.lAssetName)
        self.leAssetName = QtGui.QLineEdit(wgDataAssetCasting)
        self.leAssetName.setText(_fromUtf8(""))
        self.leAssetName.setFrame(False)
        self.leAssetName.setReadOnly(True)
        self.leAssetName.setObjectName(_fromUtf8("leAssetName"))
        self.hlAssetName.addWidget(self.leAssetName)
        self.gridLayout.addLayout(self.hlAssetName, 3, 0, 1, 1)
        self.hlNamespace = QtGui.QHBoxLayout()
        self.hlNamespace.setSpacing(2)
        self.hlNamespace.setObjectName(_fromUtf8("hlNamespace"))
        self.lNamespace = QtGui.QLabel(wgDataAssetCasting)
        self.lNamespace.setMinimumSize(QtCore.QSize(65, 0))
        self.lNamespace.setMaximumSize(QtCore.QSize(65, 16777215))
        self.lNamespace.setObjectName(_fromUtf8("lNamespace"))
        self.hlNamespace.addWidget(self.lNamespace)
        self.leNamespace = QtGui.QLineEdit(wgDataAssetCasting)
        self.leNamespace.setText(_fromUtf8(""))
        self.leNamespace.setFrame(False)
        self.leNamespace.setReadOnly(True)
        self.leNamespace.setObjectName(_fromUtf8("leNamespace"))
        self.hlNamespace.addWidget(self.leNamespace)
        self.gridLayout.addLayout(self.hlNamespace, 4, 0, 1, 1)

        self.retranslateUi(wgDataAssetCasting)
        QtCore.QMetaObject.connectSlotsByName(wgDataAssetCasting)

    def retranslateUi(self, wgDataAssetCasting):
        wgDataAssetCasting.setWindowTitle(_translate("wgDataAssetCasting", "Asset Casting", None))
        self.lAssetEntity.setText(_translate("wgDataAssetCasting", "Asset Entity :", None))
        self.lAssetType.setText(_translate("wgDataAssetCasting", "Asset Type :", None))
        self.lAssetSpec.setText(_translate("wgDataAssetCasting", "Asset Spec :", None))
        self.lAssetName.setText(_translate("wgDataAssetCasting", "Asset Name :", None))
        self.lNamespace.setText(_translate("wgDataAssetCasting", "Asset Ns :", None))

