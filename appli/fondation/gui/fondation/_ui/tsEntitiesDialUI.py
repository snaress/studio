# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\fondation\gui\fondation\_src\tsEntitiesDial.ui'
#
# Created: Wed Dec 23 05:54:11 2015
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

class Ui_dial_entity(object):
    def setupUi(self, dial_entity):
        dial_entity.setObjectName(_fromUtf8("dial_entity"))
        dial_entity.resize(426, 201)
        self.gridLayout = QtGui.QGridLayout(dial_entity)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_3 = QtGui.QFrame(dial_entity)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 0, 0, 1, 1)
        self.l_message = QtGui.QLabel(dial_entity)
        self.l_message.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l_message.setFont(font)
        self.l_message.setAlignment(QtCore.Qt.AlignCenter)
        self.l_message.setObjectName(_fromUtf8("l_message"))
        self.gridLayout.addWidget(self.l_message, 1, 0, 1, 1)
        self.line_2 = QtGui.QFrame(dial_entity)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 1)
        self.hl_entityType = QtGui.QHBoxLayout()
        self.hl_entityType.setObjectName(_fromUtf8("hl_entityType"))
        self.l_entityType = QtGui.QLabel(dial_entity)
        self.l_entityType.setMinimumSize(QtCore.QSize(92, 0))
        self.l_entityType.setMaximumSize(QtCore.QSize(92, 16777215))
        self.l_entityType.setObjectName(_fromUtf8("l_entityType"))
        self.hl_entityType.addWidget(self.l_entityType)
        self.le_entityType = QtGui.QLineEdit(dial_entity)
        self.le_entityType.setMinimumSize(QtCore.QSize(200, 0))
        self.le_entityType.setMaximumSize(QtCore.QSize(100, 16777215))
        self.le_entityType.setReadOnly(True)
        self.le_entityType.setObjectName(_fromUtf8("le_entityType"))
        self.hl_entityType.addWidget(self.le_entityType)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_entityType.addItem(spacerItem)
        self.gridLayout.addLayout(self.hl_entityType, 3, 0, 1, 1)
        self.hl_entityName = QtGui.QHBoxLayout()
        self.hl_entityName.setObjectName(_fromUtf8("hl_entityName"))
        self.l_entityName = QtGui.QLabel(dial_entity)
        self.l_entityName.setMinimumSize(QtCore.QSize(92, 0))
        self.l_entityName.setMaximumSize(QtCore.QSize(92, 16777215))
        self.l_entityName.setObjectName(_fromUtf8("l_entityName"))
        self.hl_entityName.addWidget(self.l_entityName)
        self.le_entityName = QtGui.QLineEdit(dial_entity)
        self.le_entityName.setMinimumSize(QtCore.QSize(200, 0))
        self.le_entityName.setMaximumSize(QtCore.QSize(100, 16777215))
        self.le_entityName.setObjectName(_fromUtf8("le_entityName"))
        self.hl_entityName.addWidget(self.le_entityName)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_entityName.addItem(spacerItem1)
        self.gridLayout.addLayout(self.hl_entityName, 4, 0, 1, 1)
        self.hl_entityLabel = QtGui.QHBoxLayout()
        self.hl_entityLabel.setObjectName(_fromUtf8("hl_entityLabel"))
        self.l_entityLabel = QtGui.QLabel(dial_entity)
        self.l_entityLabel.setMinimumSize(QtCore.QSize(92, 0))
        self.l_entityLabel.setMaximumSize(QtCore.QSize(92, 16777215))
        self.l_entityLabel.setObjectName(_fromUtf8("l_entityLabel"))
        self.hl_entityLabel.addWidget(self.l_entityLabel)
        self.le_entityLabel = QtGui.QLineEdit(dial_entity)
        self.le_entityLabel.setMinimumSize(QtCore.QSize(200, 0))
        self.le_entityLabel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.le_entityLabel.setObjectName(_fromUtf8("le_entityLabel"))
        self.hl_entityLabel.addWidget(self.le_entityLabel)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_entityLabel.addItem(spacerItem2)
        self.gridLayout.addLayout(self.hl_entityLabel, 5, 0, 1, 1)
        self.hl_entityFolder = QtGui.QHBoxLayout()
        self.hl_entityFolder.setObjectName(_fromUtf8("hl_entityFolder"))
        self.l_entityFolder = QtGui.QLabel(dial_entity)
        self.l_entityFolder.setMinimumSize(QtCore.QSize(92, 0))
        self.l_entityFolder.setMaximumSize(QtCore.QSize(92, 16777215))
        self.l_entityFolder.setObjectName(_fromUtf8("l_entityFolder"))
        self.hl_entityFolder.addWidget(self.l_entityFolder)
        self.le_entityFolder = QtGui.QLineEdit(dial_entity)
        self.le_entityFolder.setMinimumSize(QtCore.QSize(200, 0))
        self.le_entityFolder.setMaximumSize(QtCore.QSize(100, 16777215))
        self.le_entityFolder.setObjectName(_fromUtf8("le_entityFolder"))
        self.hl_entityFolder.addWidget(self.le_entityFolder)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_entityFolder.addItem(spacerItem3)
        self.gridLayout.addLayout(self.hl_entityFolder, 6, 0, 1, 1)
        self.line = QtGui.QFrame(dial_entity)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 7, 0, 1, 1)
        self.hl_buttons = QtGui.QHBoxLayout()
        self.hl_buttons.setSpacing(0)
        self.hl_buttons.setObjectName(_fromUtf8("hl_buttons"))
        spacerItem4 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_buttons.addItem(spacerItem4)
        self.pb_save = QtGui.QPushButton(dial_entity)
        self.pb_save.setMaximumSize(QtCore.QSize(60, 20))
        self.pb_save.setObjectName(_fromUtf8("pb_save"))
        self.hl_buttons.addWidget(self.pb_save)
        self.pb_cancel = QtGui.QPushButton(dial_entity)
        self.pb_cancel.setMaximumSize(QtCore.QSize(60, 20))
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.hl_buttons.addWidget(self.pb_cancel)
        self.gridLayout.addLayout(self.hl_buttons, 8, 0, 1, 1)

        self.retranslateUi(dial_entity)
        QtCore.QMetaObject.connectSlotsByName(dial_entity)

    def retranslateUi(self, dial_entity):
        dial_entity.setWindowTitle(_translate("dial_entity", "Entity Dialog", None))
        self.l_message.setText(_translate("dial_entity", "Edit Entity", None))
        self.l_entityType.setText(_translate("dial_entity", "Entity Type: ", None))
        self.l_entityName.setText(_translate("dial_entity", "Entity Name: ", None))
        self.l_entityLabel.setText(_translate("dial_entity", "Entity Label: ", None))
        self.l_entityFolder.setText(_translate("dial_entity", "Entity Folder: ", None))
        self.pb_save.setText(_translate("dial_entity", "Save", None))
        self.pb_cancel.setText(_translate("dial_entity", "cancel", None))

