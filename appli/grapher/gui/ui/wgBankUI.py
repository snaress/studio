# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgBank.ui'
#
# Created: Sat Oct 31 13:04:24 2015
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

class Ui_wgBank(object):
    def setupUi(self, wgBank):
        wgBank.setObjectName(_fromUtf8("wgBank"))
        wgBank.resize(656, 591)
        self.gridLayout = QtGui.QGridLayout(wgBank)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line = QtGui.QFrame(wgBank)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.line_2 = QtGui.QFrame(wgBank)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(2, -1, 2, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pbRefresh = QtGui.QPushButton(wgBank)
        self.pbRefresh.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pbRefresh.setObjectName(_fromUtf8("pbRefresh"))
        self.horizontalLayout.addWidget(self.pbRefresh)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pbEdit = QtGui.QPushButton(wgBank)
        self.pbEdit.setMaximumSize(QtCore.QSize(40, 20))
        self.pbEdit.setCheckable(True)
        self.pbEdit.setFlat(True)
        self.pbEdit.setObjectName(_fromUtf8("pbEdit"))
        self.horizontalLayout.addWidget(self.pbEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.splitter = QtGui.QSplitter(wgBank)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(3)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.hlTree = QtGui.QHBoxLayout(self.layoutWidget)
        self.hlTree.setSpacing(2)
        self.hlTree.setMargin(0)
        self.hlTree.setObjectName(_fromUtf8("hlTree"))
        self.qfEditTree = QtGui.QFrame(self.layoutWidget)
        self.qfEditTree.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qfEditTree.setObjectName(_fromUtf8("qfEditTree"))
        self.vlEditTree = QtGui.QVBoxLayout(self.qfEditTree)
        self.vlEditTree.setSpacing(0)
        self.vlEditTree.setMargin(0)
        self.vlEditTree.setObjectName(_fromUtf8("vlEditTree"))
        self.pbExplorer = QtGui.QPushButton(self.qfEditTree)
        self.pbExplorer.setObjectName(_fromUtf8("pbExplorer"))
        self.vlEditTree.addWidget(self.pbExplorer)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlEditTree.addItem(spacerItem1)
        self.pbAddFolder = QtGui.QPushButton(self.qfEditTree)
        self.pbAddFolder.setObjectName(_fromUtf8("pbAddFolder"))
        self.vlEditTree.addWidget(self.pbAddFolder)
        self.pbAddScript = QtGui.QPushButton(self.qfEditTree)
        self.pbAddScript.setObjectName(_fromUtf8("pbAddScript"))
        self.vlEditTree.addWidget(self.pbAddScript)
        self.pbAddNode = QtGui.QPushButton(self.qfEditTree)
        self.pbAddNode.setObjectName(_fromUtf8("pbAddNode"))
        self.vlEditTree.addWidget(self.pbAddNode)
        self.pbAddBranch = QtGui.QPushButton(self.qfEditTree)
        self.pbAddBranch.setObjectName(_fromUtf8("pbAddBranch"))
        self.vlEditTree.addWidget(self.pbAddBranch)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlEditTree.addItem(spacerItem2)
        self.pbDelSelFile = QtGui.QPushButton(self.qfEditTree)
        self.pbDelSelFile.setObjectName(_fromUtf8("pbDelSelFile"))
        self.vlEditTree.addWidget(self.pbDelSelFile)
        self.pbDelSelFolder = QtGui.QPushButton(self.qfEditTree)
        self.pbDelSelFolder.setObjectName(_fromUtf8("pbDelSelFolder"))
        self.vlEditTree.addWidget(self.pbDelSelFolder)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlEditTree.addItem(spacerItem3)
        self.hlTree.addWidget(self.qfEditTree)
        self.vlTree = QtGui.QVBoxLayout()
        self.vlTree.setSpacing(0)
        self.vlTree.setContentsMargins(-1, 0, -1, -1)
        self.vlTree.setObjectName(_fromUtf8("vlTree"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pbSendToGraph = QtGui.QPushButton(self.layoutWidget)
        self.pbSendToGraph.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbSendToGraph.sizePolicy().hasHeightForWidth())
        self.pbSendToGraph.setSizePolicy(sizePolicy)
        self.pbSendToGraph.setMaximumSize(QtCore.QSize(90, 20))
        self.pbSendToGraph.setObjectName(_fromUtf8("pbSendToGraph"))
        self.horizontalLayout_2.addWidget(self.pbSendToGraph)
        self.vlTree.addLayout(self.horizontalLayout_2)
        self.line_6 = QtGui.QFrame(self.layoutWidget)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.vlTree.addWidget(self.line_6)
        self.twTree = QtGui.QTreeWidget(self.layoutWidget)
        self.twTree.setObjectName(_fromUtf8("twTree"))
        self.twTree.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.twTree.header().setVisible(False)
        self.vlTree.addWidget(self.twTree)
        self.line_4 = QtGui.QFrame(self.layoutWidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.vlTree.addWidget(self.line_4)
        self.hlTreeDisp = QtGui.QHBoxLayout()
        self.hlTreeDisp.setSpacing(2)
        self.hlTreeDisp.setObjectName(_fromUtf8("hlTreeDisp"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.hlTreeDisp.addWidget(self.label)
        self.cbScript = QtGui.QCheckBox(self.layoutWidget)
        self.cbScript.setChecked(True)
        self.cbScript.setObjectName(_fromUtf8("cbScript"))
        self.hlTreeDisp.addWidget(self.cbScript)
        self.cbNode = QtGui.QCheckBox(self.layoutWidget)
        self.cbNode.setChecked(True)
        self.cbNode.setObjectName(_fromUtf8("cbNode"))
        self.hlTreeDisp.addWidget(self.cbNode)
        self.cbBranch = QtGui.QCheckBox(self.layoutWidget)
        self.cbBranch.setChecked(True)
        self.cbBranch.setObjectName(_fromUtf8("cbBranch"))
        self.hlTreeDisp.addWidget(self.cbBranch)
        self.vlTree.addLayout(self.hlTreeDisp)
        self.hlTree.addLayout(self.vlTree)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.vlInfo = QtGui.QVBoxLayout(self.layoutWidget1)
        self.vlInfo.setSpacing(0)
        self.vlInfo.setContentsMargins(0, 0, -1, 0)
        self.vlInfo.setObjectName(_fromUtf8("vlInfo"))
        self.vfSpacer = QtGui.QFrame(self.layoutWidget1)
        self.vfSpacer.setLineWidth(0)
        self.vfSpacer.setObjectName(_fromUtf8("vfSpacer"))
        self.vlSpacer = QtGui.QVBoxLayout(self.vfSpacer)
        self.vlSpacer.setSpacing(0)
        self.vlSpacer.setMargin(0)
        self.vlSpacer.setObjectName(_fromUtf8("vlSpacer"))
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vlSpacer.addItem(spacerItem5)
        self.vlInfo.addWidget(self.vfSpacer)
        self.splitScript = QtGui.QSplitter(self.layoutWidget1)
        self.splitScript.setFrameShape(QtGui.QFrame.NoFrame)
        self.splitScript.setLineWidth(0)
        self.splitScript.setOrientation(QtCore.Qt.Vertical)
        self.splitScript.setHandleWidth(3)
        self.splitScript.setObjectName(_fromUtf8("splitScript"))
        self.layoutWidget_5 = QtGui.QWidget(self.splitScript)
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.vlComment = QtGui.QVBoxLayout(self.layoutWidget_5)
        self.vlComment.setSpacing(0)
        self.vlComment.setMargin(0)
        self.vlComment.setObjectName(_fromUtf8("vlComment"))
        self.lComment = QtGui.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lComment.setFont(font)
        self.lComment.setObjectName(_fromUtf8("lComment"))
        self.vlComment.addWidget(self.lComment)
        self.teComment = QtGui.QPlainTextEdit(self.layoutWidget_5)
        self.teComment.setReadOnly(True)
        self.teComment.setObjectName(_fromUtf8("teComment"))
        self.vlComment.addWidget(self.teComment)
        self.layoutWidget_6 = QtGui.QWidget(self.splitScript)
        self.layoutWidget_6.setObjectName(_fromUtf8("layoutWidget_6"))
        self.vlRequires = QtGui.QVBoxLayout(self.layoutWidget_6)
        self.vlRequires.setSpacing(0)
        self.vlRequires.setMargin(0)
        self.vlRequires.setObjectName(_fromUtf8("vlRequires"))
        self.lRequires = QtGui.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lRequires.setFont(font)
        self.lRequires.setObjectName(_fromUtf8("lRequires"))
        self.vlRequires.addWidget(self.lRequires)
        self.teRequires = QtGui.QPlainTextEdit(self.layoutWidget_6)
        self.teRequires.setReadOnly(True)
        self.teRequires.setObjectName(_fromUtf8("teRequires"))
        self.vlRequires.addWidget(self.teRequires)
        self.layoutWidget_7 = QtGui.QWidget(self.splitScript)
        self.layoutWidget_7.setObjectName(_fromUtf8("layoutWidget_7"))
        self.vlScript = QtGui.QVBoxLayout(self.layoutWidget_7)
        self.vlScript.setSpacing(0)
        self.vlScript.setMargin(0)
        self.vlScript.setObjectName(_fromUtf8("vlScript"))
        self.lScript = QtGui.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.lScript.setFont(font)
        self.lScript.setObjectName(_fromUtf8("lScript"))
        self.vlScript.addWidget(self.lScript)
        self.teScript = QtGui.QPlainTextEdit(self.layoutWidget_7)
        self.teScript.setReadOnly(True)
        self.teScript.setObjectName(_fromUtf8("teScript"))
        self.vlScript.addWidget(self.teScript)
        self.vlInfo.addWidget(self.splitScript)
        self.line_5 = QtGui.QFrame(self.layoutWidget1)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.vlInfo.addWidget(self.line_5)
        self.qfInfoEdit = QtGui.QFrame(self.layoutWidget1)
        self.qfInfoEdit.setLineWidth(0)
        self.qfInfoEdit.setObjectName(_fromUtf8("qfInfoEdit"))
        self.hlInfoEdit = QtGui.QHBoxLayout(self.qfInfoEdit)
        self.hlInfoEdit.setSpacing(2)
        self.hlInfoEdit.setMargin(0)
        self.hlInfoEdit.setObjectName(_fromUtf8("hlInfoEdit"))
        spacerItem6 = QtGui.QSpacerItem(40, 15, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlInfoEdit.addItem(spacerItem6)
        self.pbSave = QtGui.QPushButton(self.qfInfoEdit)
        self.pbSave.setMaximumSize(QtCore.QSize(50, 18))
        self.pbSave.setObjectName(_fromUtf8("pbSave"))
        self.hlInfoEdit.addWidget(self.pbSave)
        self.pbCancel = QtGui.QPushButton(self.qfInfoEdit)
        self.pbCancel.setMaximumSize(QtCore.QSize(50, 18))
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.hlInfoEdit.addWidget(self.pbCancel)
        self.vlInfo.addWidget(self.qfInfoEdit)
        self.gridLayout.addWidget(self.splitter, 4, 0, 1, 1)
        self.line_3 = QtGui.QFrame(wgBank)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 1)

        self.retranslateUi(wgBank)
        QtCore.QMetaObject.connectSlotsByName(wgBank)

    def retranslateUi(self, wgBank):
        wgBank.setWindowTitle(_translate("wgBank", "Bank", None))
        self.pbRefresh.setText(_translate("wgBank", "Refresh", None))
        self.pbEdit.setText(_translate("wgBank", "Edit", None))
        self.pbExplorer.setText(_translate("wgBank", "Xplorer", None))
        self.pbAddFolder.setText(_translate("wgBank", "Add Folder", None))
        self.pbAddScript.setText(_translate("wgBank", "Add Script", None))
        self.pbAddNode.setText(_translate("wgBank", "Add Node", None))
        self.pbAddBranch.setText(_translate("wgBank", "Add Branch", None))
        self.pbDelSelFile.setText(_translate("wgBank", "Del Sel File", None))
        self.pbDelSelFolder.setText(_translate("wgBank", "Del Sel Folder", None))
        self.pbSendToGraph.setText(_translate("wgBank", "Send To Graph", None))
        self.twTree.headerItem().setText(0, _translate("wgBank", "Tree", None))
        self.label.setText(_translate("wgBank", "Display: ", None))
        self.cbScript.setText(_translate("wgBank", "Script", None))
        self.cbNode.setText(_translate("wgBank", "Node", None))
        self.cbBranch.setText(_translate("wgBank", "Branch", None))
        self.lComment.setText(_translate("wgBank", "Comment:", None))
        self.lRequires.setText(_translate("wgBank", "Requires:", None))
        self.lScript.setText(_translate("wgBank", "Script:", None))
        self.pbSave.setText(_translate("wgBank", "Save", None))
        self.pbCancel.setText(_translate("wgBank", "Cancel", None))

