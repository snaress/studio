# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\grapher.ui'
#
# Created: Wed Nov 04 02:56:46 2015
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

class Ui_mwGrapher(object):
    def setupUi(self, mwGrapher):
        mwGrapher.setObjectName(_fromUtf8("mwGrapher"))
        mwGrapher.resize(1006, 670)
        self.centralwidget = QtGui.QWidget(mwGrapher)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
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
        self.vfGraphZone = QtGui.QFrame(self.splitter)
        self.vfGraphZone.setFrameShape(QtGui.QFrame.StyledPanel)
        self.vfGraphZone.setObjectName(_fromUtf8("vfGraphZone"))
        self.vlGraphZone = QtGui.QVBoxLayout(self.vfGraphZone)
        self.vlGraphZone.setSpacing(0)
        self.vlGraphZone.setMargin(0)
        self.vlGraphZone.setObjectName(_fromUtf8("vlGraphZone"))
        self.vfLogs = QtGui.QFrame(self.splitter)
        self.vfLogs.setFrameShape(QtGui.QFrame.StyledPanel)
        self.vfLogs.setObjectName(_fromUtf8("vfLogs"))
        self.vlLogs = QtGui.QVBoxLayout(self.vfLogs)
        self.vlLogs.setSpacing(0)
        self.vlLogs.setMargin(0)
        self.vlLogs.setObjectName(_fromUtf8("vlLogs"))
        self.vfNodeEditor = QtGui.QFrame(self.splitter_2)
        self.vfNodeEditor.setFrameShape(QtGui.QFrame.StyledPanel)
        self.vfNodeEditor.setObjectName(_fromUtf8("vfNodeEditor"))
        self.vlNodeEditor = QtGui.QVBoxLayout(self.vfNodeEditor)
        self.vlNodeEditor.setSpacing(0)
        self.vlNodeEditor.setMargin(0)
        self.vlNodeEditor.setObjectName(_fromUtf8("vlNodeEditor"))
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        mwGrapher.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mwGrapher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1006, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuDisplay = QtGui.QMenu(self.menubar)
        self.menuDisplay.setObjectName(_fromUtf8("menuDisplay"))
        self.menuToolBarOptions = QtGui.QMenu(self.menuDisplay)
        self.menuToolBarOptions.setObjectName(_fromUtf8("menuToolBarOptions"))
        self.menuToolBarOrient = QtGui.QMenu(self.menuToolBarOptions)
        self.menuToolBarOrient.setObjectName(_fromUtf8("menuToolBarOrient"))
        self.menuToolTabOrient = QtGui.QMenu(self.menuToolBarOptions)
        self.menuToolTabOrient.setObjectName(_fromUtf8("menuToolTabOrient"))
        self.menuGraph = QtGui.QMenu(self.menubar)
        self.menuGraph.setObjectName(_fromUtf8("menuGraph"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuPrintDatas = QtGui.QMenu(self.menuHelp)
        self.menuPrintDatas.setTearOffEnabled(True)
        self.menuPrintDatas.setObjectName(_fromUtf8("menuPrintDatas"))
        self.menuVerbose = QtGui.QMenu(self.menuHelp)
        self.menuVerbose.setTearOffEnabled(True)
        self.menuVerbose.setObjectName(_fromUtf8("menuVerbose"))
        self.menuFiles = QtGui.QMenu(self.menubar)
        self.menuFiles.setObjectName(_fromUtf8("menuFiles"))
        self.menuRecentFiles = QtGui.QMenu(self.menuFiles)
        self.menuRecentFiles.setObjectName(_fromUtf8("menuRecentFiles"))
        self.menuExec = QtGui.QMenu(self.menubar)
        self.menuExec.setObjectName(_fromUtf8("menuExec"))
        mwGrapher.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mwGrapher)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mwGrapher.setStatusBar(self.statusbar)
        self.tbTools = QtGui.QToolBar(mwGrapher)
        self.tbTools.setFloatable(False)
        self.tbTools.setObjectName(_fromUtf8("tbTools"))
        mwGrapher.addToolBar(QtCore.Qt.LeftToolBarArea, self.tbTools)
        self.miToolsVisibility = QtGui.QAction(mwGrapher)
        self.miToolsVisibility.setCheckable(True)
        self.miToolsVisibility.setChecked(True)
        self.miToolsVisibility.setObjectName(_fromUtf8("miToolsVisibility"))
        self.miGraphScene = QtGui.QAction(mwGrapher)
        self.miGraphScene.setCheckable(True)
        self.miGraphScene.setObjectName(_fromUtf8("miGraphScene"))
        self.miNodeEditor = QtGui.QAction(mwGrapher)
        self.miNodeEditor.setCheckable(True)
        self.miNodeEditor.setObjectName(_fromUtf8("miNodeEditor"))
        self.miToolsIconOnly = QtGui.QAction(mwGrapher)
        self.miToolsIconOnly.setCheckable(True)
        self.miToolsIconOnly.setChecked(True)
        self.miToolsIconOnly.setObjectName(_fromUtf8("miToolsIconOnly"))
        self.miBarHorizontal = QtGui.QAction(mwGrapher)
        self.miBarHorizontal.setObjectName(_fromUtf8("miBarHorizontal"))
        self.miBarVertical = QtGui.QAction(mwGrapher)
        self.miBarVertical.setObjectName(_fromUtf8("miBarVertical"))
        self.miTabNorth = QtGui.QAction(mwGrapher)
        self.miTabNorth.setObjectName(_fromUtf8("miTabNorth"))
        self.miTabSouth = QtGui.QAction(mwGrapher)
        self.miTabSouth.setObjectName(_fromUtf8("miTabSouth"))
        self.miTabWest = QtGui.QAction(mwGrapher)
        self.miTabWest.setObjectName(_fromUtf8("miTabWest"))
        self.miTabEast = QtGui.QAction(mwGrapher)
        self.miTabEast.setObjectName(_fromUtf8("miTabEast"))
        self.miTreeDatas = QtGui.QAction(mwGrapher)
        self.miTreeDatas.setObjectName(_fromUtf8("miTreeDatas"))
        self.miFromUi = QtGui.QAction(mwGrapher)
        self.miFromUi.setObjectName(_fromUtf8("miFromUi"))
        self.miSaveAs = QtGui.QAction(mwGrapher)
        self.miSaveAs.setObjectName(_fromUtf8("miSaveAs"))
        self.miSave = QtGui.QAction(mwGrapher)
        self.miSave.setObjectName(_fromUtf8("miSave"))
        self.miLoad = QtGui.QAction(mwGrapher)
        self.miLoad.setObjectName(_fromUtf8("miLoad"))
        self.miBreakLock = QtGui.QAction(mwGrapher)
        self.miBreakLock.setObjectName(_fromUtf8("miBreakLock"))
        self.miClose = QtGui.QAction(mwGrapher)
        self.miClose.setObjectName(_fromUtf8("miClose"))
        self.miQuit = QtGui.QAction(mwGrapher)
        self.miQuit.setObjectName(_fromUtf8("miQuit"))
        self.miNodeDatas = QtGui.QAction(mwGrapher)
        self.miNodeDatas.setObjectName(_fromUtf8("miNodeDatas"))
        self.miXplorer = QtGui.QAction(mwGrapher)
        self.miXplorer.setObjectName(_fromUtf8("miXplorer"))
        self.miXterm = QtGui.QAction(mwGrapher)
        self.miXterm.setObjectName(_fromUtf8("miXterm"))
        self.actionRecent = QtGui.QAction(mwGrapher)
        self.actionRecent.setObjectName(_fromUtf8("actionRecent"))
        self.miGrapherDatas = QtGui.QAction(mwGrapher)
        self.miGrapherDatas.setObjectName(_fromUtf8("miGrapherDatas"))
        self.miExecGraph = QtGui.QAction(mwGrapher)
        self.miExecGraph.setObjectName(_fromUtf8("miExecGraph"))
        self.miShowXterm = QtGui.QAction(mwGrapher)
        self.miShowXterm.setCheckable(True)
        self.miShowXterm.setChecked(False)
        self.miShowXterm.setObjectName(_fromUtf8("miShowXterm"))
        self.miWaitAtEnd = QtGui.QAction(mwGrapher)
        self.miWaitAtEnd.setCheckable(True)
        self.miWaitAtEnd.setChecked(False)
        self.miWaitAtEnd.setObjectName(_fromUtf8("miWaitAtEnd"))
        self.actionDe = QtGui.QAction(mwGrapher)
        self.actionDe.setObjectName(_fromUtf8("actionDe"))
        self.miCriticalLvl = QtGui.QAction(mwGrapher)
        self.miCriticalLvl.setCheckable(True)
        self.miCriticalLvl.setChecked(False)
        self.miCriticalLvl.setObjectName(_fromUtf8("miCriticalLvl"))
        self.miErrorLvl = QtGui.QAction(mwGrapher)
        self.miErrorLvl.setCheckable(True)
        self.miErrorLvl.setChecked(False)
        self.miErrorLvl.setObjectName(_fromUtf8("miErrorLvl"))
        self.miWarningLvl = QtGui.QAction(mwGrapher)
        self.miWarningLvl.setCheckable(True)
        self.miWarningLvl.setChecked(False)
        self.miWarningLvl.setObjectName(_fromUtf8("miWarningLvl"))
        self.miInfoLvl = QtGui.QAction(mwGrapher)
        self.miInfoLvl.setCheckable(True)
        self.miInfoLvl.setChecked(False)
        self.miInfoLvl.setObjectName(_fromUtf8("miInfoLvl"))
        self.miDebugLvl = QtGui.QAction(mwGrapher)
        self.miDebugLvl.setCheckable(True)
        self.miDebugLvl.setChecked(False)
        self.miDebugLvl.setObjectName(_fromUtf8("miDebugLvl"))
        self.miDetailLvl = QtGui.QAction(mwGrapher)
        self.miDetailLvl.setCheckable(True)
        self.miDetailLvl.setChecked(False)
        self.miDetailLvl.setObjectName(_fromUtf8("miDetailLvl"))
        self.miLogs = QtGui.QAction(mwGrapher)
        self.miLogs.setCheckable(True)
        self.miLogs.setObjectName(_fromUtf8("miLogs"))
        self.miExecNode = QtGui.QAction(mwGrapher)
        self.miExecNode.setObjectName(_fromUtf8("miExecNode"))
        self.miBank = QtGui.QAction(mwGrapher)
        self.miBank.setObjectName(_fromUtf8("miBank"))
        self.miInternalVar = QtGui.QAction(mwGrapher)
        self.miInternalVar.setObjectName(_fromUtf8("miInternalVar"))
        self.menuToolBarOrient.addAction(self.miBarHorizontal)
        self.menuToolBarOrient.addAction(self.miBarVertical)
        self.menuToolTabOrient.addAction(self.miTabNorth)
        self.menuToolTabOrient.addAction(self.miTabSouth)
        self.menuToolTabOrient.addAction(self.miTabWest)
        self.menuToolTabOrient.addAction(self.miTabEast)
        self.menuToolBarOptions.addAction(self.menuToolBarOrient.menuAction())
        self.menuToolBarOptions.addAction(self.menuToolTabOrient.menuAction())
        self.menuToolBarOptions.addSeparator()
        self.menuToolBarOptions.addAction(self.miToolsIconOnly)
        self.menuDisplay.addAction(self.miToolsVisibility)
        self.menuDisplay.addAction(self.miNodeEditor)
        self.menuDisplay.addAction(self.miGraphScene)
        self.menuDisplay.addAction(self.miLogs)
        self.menuDisplay.addAction(self.miBank)
        self.menuDisplay.addSeparator()
        self.menuDisplay.addAction(self.menuToolBarOptions.menuAction())
        self.menuPrintDatas.addAction(self.miGrapherDatas)
        self.menuPrintDatas.addAction(self.miTreeDatas)
        self.menuPrintDatas.addAction(self.miNodeDatas)
        self.menuHelp.addAction(self.miInternalVar)
        self.menuHelp.addAction(self.menuPrintDatas.menuAction())
        self.menuHelp.addAction(self.menuVerbose.menuAction())
        self.menuFiles.addAction(self.miLoad)
        self.menuFiles.addAction(self.menuRecentFiles.menuAction())
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.miSave)
        self.menuFiles.addAction(self.miSaveAs)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.miBreakLock)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.miClose)
        self.menuFiles.addAction(self.miQuit)
        self.menuExec.addAction(self.miXplorer)
        self.menuExec.addAction(self.miXterm)
        self.menuExec.addSeparator()
        self.menuExec.addAction(self.miExecGraph)
        self.menuExec.addAction(self.miExecNode)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuGraph.menuAction())
        self.menubar.addAction(self.menuExec.menuAction())
        self.menubar.addAction(self.menuDisplay.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mwGrapher)
        QtCore.QMetaObject.connectSlotsByName(mwGrapher)

    def retranslateUi(self, mwGrapher):
        mwGrapher.setWindowTitle(_translate("mwGrapher", "Grapher", None))
        self.gbComment.setTitle(_translate("mwGrapher", "Comment", None))
        self.gbVariables.setTitle(_translate("mwGrapher", "Variables", None))
        self.menuDisplay.setTitle(_translate("mwGrapher", "Display", None))
        self.menuToolBarOptions.setTitle(_translate("mwGrapher", "Tool Bar Options", None))
        self.menuToolBarOrient.setTitle(_translate("mwGrapher", "Tool Bar Orient", None))
        self.menuToolTabOrient.setTitle(_translate("mwGrapher", "Tool Tab Orient", None))
        self.menuGraph.setTitle(_translate("mwGrapher", "Graph", None))
        self.menuHelp.setTitle(_translate("mwGrapher", "Help", None))
        self.menuPrintDatas.setTitle(_translate("mwGrapher", "Print Datas", None))
        self.menuVerbose.setTitle(_translate("mwGrapher", "Verbose", None))
        self.menuFiles.setTitle(_translate("mwGrapher", "Files", None))
        self.menuRecentFiles.setTitle(_translate("mwGrapher", "Recent Files", None))
        self.menuExec.setTitle(_translate("mwGrapher", "Exec", None))
        self.tbTools.setWindowTitle(_translate("mwGrapher", "toolBar", None))
        self.miToolsVisibility.setText(_translate("mwGrapher", "Tools Bar", None))
        self.miGraphScene.setText(_translate("mwGrapher", "Graph Scene", None))
        self.miNodeEditor.setText(_translate("mwGrapher", "Node Editor", None))
        self.miToolsIconOnly.setText(_translate("mwGrapher", "Tools Icon Only", None))
        self.miBarHorizontal.setText(_translate("mwGrapher", "Horizontal", None))
        self.miBarVertical.setText(_translate("mwGrapher", "Vertical", None))
        self.miTabNorth.setText(_translate("mwGrapher", "North", None))
        self.miTabSouth.setText(_translate("mwGrapher", "South", None))
        self.miTabWest.setText(_translate("mwGrapher", "West", None))
        self.miTabEast.setText(_translate("mwGrapher", "East", None))
        self.miTreeDatas.setText(_translate("mwGrapher", "Tree Datas", None))
        self.miFromUi.setText(_translate("mwGrapher", "From Ui", None))
        self.miSaveAs.setText(_translate("mwGrapher", "Save As", None))
        self.miSave.setText(_translate("mwGrapher", "Save", None))
        self.miLoad.setText(_translate("mwGrapher", "Load", None))
        self.miBreakLock.setText(_translate("mwGrapher", "Break Lock", None))
        self.miClose.setText(_translate("mwGrapher", "Close", None))
        self.miQuit.setText(_translate("mwGrapher", "Quit", None))
        self.miNodeDatas.setText(_translate("mwGrapher", "Node Datas", None))
        self.miXplorer.setText(_translate("mwGrapher", "Xplorer", None))
        self.miXterm.setText(_translate("mwGrapher", "Xterm", None))
        self.actionRecent.setText(_translate("mwGrapher", "recent", None))
        self.miGrapherDatas.setText(_translate("mwGrapher", "Grapher Datas", None))
        self.miExecGraph.setText(_translate("mwGrapher", "Exec Graph", None))
        self.miShowXterm.setText(_translate("mwGrapher", "Show Xterm", None))
        self.miWaitAtEnd.setText(_translate("mwGrapher", "Wait At End", None))
        self.actionDe.setText(_translate("mwGrapher", "de", None))
        self.miCriticalLvl.setText(_translate("mwGrapher", "critical", None))
        self.miErrorLvl.setText(_translate("mwGrapher", "error", None))
        self.miWarningLvl.setText(_translate("mwGrapher", "warning", None))
        self.miInfoLvl.setText(_translate("mwGrapher", "info", None))
        self.miDebugLvl.setText(_translate("mwGrapher", "debug", None))
        self.miDetailLvl.setText(_translate("mwGrapher", "detail", None))
        self.miLogs.setText(_translate("mwGrapher", "Logs", None))
        self.miExecNode.setText(_translate("mwGrapher", "Exec Node", None))
        self.miBank.setText(_translate("mwGrapher", "Bank", None))
        self.miInternalVar.setText(_translate("mwGrapher", "Internal Var", None))

