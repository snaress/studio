# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\nodeEditor.ui'
#
# Created: Sun Oct 18 02:46:03 2015
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

class Ui_wgNodeEditor(object):
    def setupUi(self, wgNodeEditor):
        wgNodeEditor.setObjectName(_fromUtf8("wgNodeEditor"))
        wgNodeEditor.resize(650, 833)
        self.gridLayout = QtGui.QGridLayout(wgNodeEditor)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.hlNodeName = QtGui.QHBoxLayout()
        self.hlNodeName.setSpacing(4)
        self.hlNodeName.setContentsMargins(4, -1, 4, -1)
        self.hlNodeName.setObjectName(_fromUtf8("hlNodeName"))
        self.lName = QtGui.QLabel(wgNodeEditor)
        self.lName.setMinimumSize(QtCore.QSize(30, 0))
        self.lName.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lName.setObjectName(_fromUtf8("lName"))
        self.hlNodeName.addWidget(self.lName)
        self.leNodeName = QtGui.QLineEdit(wgNodeEditor)
        self.leNodeName.setMinimumSize(QtCore.QSize(150, 0))
        self.leNodeName.setReadOnly(True)
        self.leNodeName.setObjectName(_fromUtf8("leNodeName"))
        self.hlNodeName.addWidget(self.leNodeName)
        self.lType = QtGui.QLabel(wgNodeEditor)
        self.lType.setMinimumSize(QtCore.QSize(30, 0))
        self.lType.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lType.setObjectName(_fromUtf8("lType"))
        self.hlNodeName.addWidget(self.lType)
        self.lTypeValue = QtGui.QLabel(wgNodeEditor)
        self.lTypeValue.setObjectName(_fromUtf8("lTypeValue"))
        self.hlNodeName.addWidget(self.lTypeValue)
        self.gridLayout.addLayout(self.hlNodeName, 0, 0, 1, 1)
        self.hlNodeVersion = QtGui.QHBoxLayout()
        self.hlNodeVersion.setSpacing(4)
        self.hlNodeVersion.setContentsMargins(4, -1, 4, -1)
        self.hlNodeVersion.setObjectName(_fromUtf8("hlNodeVersion"))
        self.lVTitle = QtGui.QLabel(wgNodeEditor)
        self.lVTitle.setMinimumSize(QtCore.QSize(30, 0))
        self.lVTitle.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lVTitle.setObjectName(_fromUtf8("lVTitle"))
        self.hlNodeVersion.addWidget(self.lVTitle)
        self.leVersionTitle = QtGui.QLineEdit(wgNodeEditor)
        self.leVersionTitle.setMinimumSize(QtCore.QSize(0, 18))
        self.leVersionTitle.setMaximumSize(QtCore.QSize(16777215, 18))
        self.leVersionTitle.setObjectName(_fromUtf8("leVersionTitle"))
        self.hlNodeVersion.addWidget(self.leVersionTitle)
        self.line_3 = QtGui.QFrame(wgNodeEditor)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.hlNodeVersion.addWidget(self.line_3)
        self.lVersion = QtGui.QLabel(wgNodeEditor)
        self.lVersion.setMinimumSize(QtCore.QSize(40, 0))
        self.lVersion.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lVersion.setObjectName(_fromUtf8("lVersion"))
        self.hlNodeVersion.addWidget(self.lVersion)
        self.cbNodeVersion = QtGui.QComboBox(wgNodeEditor)
        self.cbNodeVersion.setMinimumSize(QtCore.QSize(60, 18))
        self.cbNodeVersion.setMaximumSize(QtCore.QSize(60, 18))
        self.cbNodeVersion.setSizeIncrement(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cbNodeVersion.setFont(font)
        self.cbNodeVersion.setObjectName(_fromUtf8("cbNodeVersion"))
        self.hlNodeVersion.addWidget(self.cbNodeVersion)
        self.pbSwitch = QtGui.QPushButton(wgNodeEditor)
        self.pbSwitch.setMinimumSize(QtCore.QSize(45, 18))
        self.pbSwitch.setMaximumSize(QtCore.QSize(45, 18))
        self.pbSwitch.setObjectName(_fromUtf8("pbSwitch"))
        self.hlNodeVersion.addWidget(self.pbSwitch)
        self.line_2 = QtGui.QFrame(wgNodeEditor)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.hlNodeVersion.addWidget(self.line_2)
        self.pbNewVersion = QtGui.QPushButton(wgNodeEditor)
        self.pbNewVersion.setMinimumSize(QtCore.QSize(35, 18))
        self.pbNewVersion.setMaximumSize(QtCore.QSize(35, 18))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pbNewVersion.setFont(font)
        self.pbNewVersion.setObjectName(_fromUtf8("pbNewVersion"))
        self.hlNodeVersion.addWidget(self.pbNewVersion)
        self.pbDelVersion = QtGui.QPushButton(wgNodeEditor)
        self.pbDelVersion.setMinimumSize(QtCore.QSize(35, 18))
        self.pbDelVersion.setMaximumSize(QtCore.QSize(35, 18))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pbDelVersion.setFont(font)
        self.pbDelVersion.setObjectName(_fromUtf8("pbDelVersion"))
        self.hlNodeVersion.addWidget(self.pbDelVersion)
        self.gridLayout.addLayout(self.hlNodeVersion, 1, 0, 1, 1)
        self.line = QtGui.QFrame(wgNodeEditor)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.splitter = QtGui.QSplitter(wgNodeEditor)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.gbComment = QtGui.QGroupBox(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbComment.sizePolicy().hasHeightForWidth())
        self.gbComment.setSizePolicy(sizePolicy)
        self.gbComment.setFlat(False)
        self.gbComment.setCheckable(True)
        self.gbComment.setChecked(False)
        self.gbComment.setObjectName(_fromUtf8("gbComment"))
        self.glComment = QtGui.QGridLayout(self.gbComment)
        self.glComment.setMargin(0)
        self.glComment.setSpacing(0)
        self.glComment.setObjectName(_fromUtf8("glComment"))
        self.gbVariables = QtGui.QGroupBox(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbVariables.sizePolicy().hasHeightForWidth())
        self.gbVariables.setSizePolicy(sizePolicy)
        self.gbVariables.setFlat(False)
        self.gbVariables.setCheckable(True)
        self.gbVariables.setChecked(False)
        self.gbVariables.setObjectName(_fromUtf8("gbVariables"))
        self.glVariables = QtGui.QGridLayout(self.gbVariables)
        self.glVariables.setMargin(0)
        self.glVariables.setSpacing(0)
        self.glVariables.setObjectName(_fromUtf8("glVariables"))
        self.vfLoop = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vfLoop.sizePolicy().hasHeightForWidth())
        self.vfLoop.setSizePolicy(sizePolicy)
        self.vfLoop.setFrameShape(QtGui.QFrame.StyledPanel)
        self.vfLoop.setObjectName(_fromUtf8("vfLoop"))
        self.vlLoop = QtGui.QVBoxLayout(self.vfLoop)
        self.vlLoop.setSpacing(0)
        self.vlLoop.setMargin(0)
        self.vlLoop.setObjectName(_fromUtf8("vlLoop"))
        self.vfScript = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vfScript.sizePolicy().hasHeightForWidth())
        self.vfScript.setSizePolicy(sizePolicy)
        self.vfScript.setFrameShape(QtGui.QFrame.StyledPanel)
        self.vfScript.setObjectName(_fromUtf8("vfScript"))
        self.vlScript = QtGui.QVBoxLayout(self.vfScript)
        self.vlScript.setSpacing(0)
        self.vlScript.setMargin(0)
        self.vlScript.setObjectName(_fromUtf8("vlScript"))
        self.vfSpacer = QtGui.QFrame(self.splitter)
        self.vfSpacer.setObjectName(_fromUtf8("vfSpacer"))
        self.vlSpacer = QtGui.QVBoxLayout(self.vfSpacer)
        self.vlSpacer.setSpacing(0)
        self.vlSpacer.setObjectName(_fromUtf8("vlSpacer"))
        spacerItem = QtGui.QSpacerItem(18, 500, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlSpacer.addItem(spacerItem)
        self.gbTrash = QtGui.QGroupBox(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbTrash.sizePolicy().hasHeightForWidth())
        self.gbTrash.setSizePolicy(sizePolicy)
        self.gbTrash.setFlat(False)
        self.gbTrash.setCheckable(True)
        self.gbTrash.setChecked(False)
        self.gbTrash.setObjectName(_fromUtf8("gbTrash"))
        self.glNotes = QtGui.QGridLayout(self.gbTrash)
        self.glNotes.setMargin(0)
        self.glNotes.setSpacing(0)
        self.glNotes.setObjectName(_fromUtf8("glNotes"))
        self.teTrash = QtGui.QPlainTextEdit(self.gbTrash)
        self.teTrash.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.teTrash.setTabStopWidth(4)
        self.teTrash.setBackgroundVisible(False)
        self.teTrash.setObjectName(_fromUtf8("teTrash"))
        self.glNotes.addWidget(self.teTrash, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.splitter, 3, 0, 1, 1)
        self.line_5 = QtGui.QFrame(wgNodeEditor)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout.addWidget(self.line_5, 4, 0, 1, 1)
        self.hlNodeBtns = QtGui.QHBoxLayout()
        self.hlNodeBtns.setSpacing(1)
        self.hlNodeBtns.setObjectName(_fromUtf8("hlNodeBtns"))
        self.pbExec = QtGui.QPushButton(wgNodeEditor)
        self.pbExec.setObjectName(_fromUtf8("pbExec"))
        self.hlNodeBtns.addWidget(self.pbExec)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlNodeBtns.addItem(spacerItem1)
        self.pbSave = QtGui.QPushButton(wgNodeEditor)
        self.pbSave.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbSave.setObjectName(_fromUtf8("pbSave"))
        self.hlNodeBtns.addWidget(self.pbSave)
        self.pbCancel = QtGui.QPushButton(wgNodeEditor)
        self.pbCancel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.hlNodeBtns.addWidget(self.pbCancel)
        self.pbClose = QtGui.QPushButton(wgNodeEditor)
        self.pbClose.setMinimumSize(QtCore.QSize(60, 20))
        self.pbClose.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbClose.setObjectName(_fromUtf8("pbClose"))
        self.hlNodeBtns.addWidget(self.pbClose)
        self.gridLayout.addLayout(self.hlNodeBtns, 5, 0, 1, 1)

        self.retranslateUi(wgNodeEditor)
        QtCore.QMetaObject.connectSlotsByName(wgNodeEditor)

    def retranslateUi(self, wgNodeEditor):
        wgNodeEditor.setWindowTitle(_translate("wgNodeEditor", "Node Editor", None))
        self.lName.setText(_translate("wgNodeEditor", "Name: ", None))
        self.lType.setText(_translate("wgNodeEditor", "Type:", None))
        self.lTypeValue.setText(_translate("wgNodeEditor", "Modul", None))
        self.lVTitle.setText(_translate("wgNodeEditor", "Title: ", None))
        self.lVersion.setText(_translate("wgNodeEditor", "Version:", None))
        self.pbSwitch.setText(_translate("wgNodeEditor", "Switch", None))
        self.pbNewVersion.setText(_translate("wgNodeEditor", "New", None))
        self.pbDelVersion.setText(_translate("wgNodeEditor", "Del", None))
        self.gbComment.setTitle(_translate("wgNodeEditor", "Comment", None))
        self.gbVariables.setTitle(_translate("wgNodeEditor", "Variables", None))
        self.gbTrash.setTitle(_translate("wgNodeEditor", "Trash", None))
        self.pbExec.setText(_translate("wgNodeEditor", "Exec", None))
        self.pbSave.setText(_translate("wgNodeEditor", "Save", None))
        self.pbCancel.setText(_translate("wgNodeEditor", "Cancel", None))
        self.pbClose.setText(_translate("wgNodeEditor", "Close", None))

