# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\ui\grapher.ui'
#
# Created: Mon Nov 24 16:27:55 2014
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
        mwGrapher.resize(800, 600)
        self.centralwidget = QtGui.QWidget(mwGrapher)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setFrameShape(QtGui.QFrame.NoFrame)
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.vfComment = QtGui.QFrame(self.splitter)
        self.vfComment.setFrameShape(QtGui.QFrame.StyledPanel)
        self.vfComment.setObjectName(_fromUtf8("vfComment"))
        self.vlComment = QtGui.QVBoxLayout(self.vfComment)
        self.vlComment.setSpacing(0)
        self.vlComment.setMargin(0)
        self.vlComment.setObjectName(_fromUtf8("vlComment"))
        self.cbComment = QtGui.QCheckBox(self.vfComment)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.cbComment.setFont(font)
        self.cbComment.setObjectName(_fromUtf8("cbComment"))
        self.vlComment.addWidget(self.cbComment)
        self.vfVariables = QtGui.QFrame(self.splitter)
        self.vfVariables.setFrameShape(QtGui.QFrame.StyledPanel)
        self.vfVariables.setObjectName(_fromUtf8("vfVariables"))
        self.vlVariables = QtGui.QVBoxLayout(self.vfVariables)
        self.vlVariables.setSpacing(0)
        self.vlVariables.setMargin(0)
        self.vlVariables.setObjectName(_fromUtf8("vlVariables"))
        self.cbVariables = QtGui.QCheckBox(self.vfVariables)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.cbVariables.setFont(font)
        self.cbVariables.setObjectName(_fromUtf8("cbVariables"))
        self.vlVariables.addWidget(self.cbVariables)
        self.vfGraph = QtGui.QFrame(self.splitter)
        self.vfGraph.setFrameShape(QtGui.QFrame.StyledPanel)
        self.vfGraph.setObjectName(_fromUtf8("vfGraph"))
        self.vlGraph = QtGui.QVBoxLayout(self.vfGraph)
        self.vlGraph.setSpacing(0)
        self.vlGraph.setMargin(0)
        self.vlGraph.setObjectName(_fromUtf8("vlGraph"))
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.mFile = QtGui.QMenu(self.menubar)
        self.mFile.setObjectName(_fromUtf8("mFile"))
        self.mGraph = QtGui.QMenu(self.menubar)
        self.mGraph.setObjectName(_fromUtf8("mGraph"))
        self.mLib = QtGui.QMenu(self.menubar)
        self.mLib.setObjectName(_fromUtf8("mLib"))
        self.mPref = QtGui.QMenu(self.menubar)
        self.mPref.setObjectName(_fromUtf8("mPref"))
        self.mExec = QtGui.QMenu(self.menubar)
        self.mExec.setObjectName(_fromUtf8("mExec"))
        mwGrapher.setMenuBar(self.menubar)
        self.miNewNode = QtGui.QAction(mwGrapher)
        self.miNewNode.setObjectName(_fromUtf8("miNewNode"))
        self.miRenameNode = QtGui.QAction(mwGrapher)
        self.miRenameNode.setObjectName(_fromUtf8("miRenameNode"))
        self.miDeleteNode = QtGui.QAction(mwGrapher)
        self.miDeleteNode.setObjectName(_fromUtf8("miDeleteNode"))
        self.miCopyNodes = QtGui.QAction(mwGrapher)
        self.miCopyNodes.setObjectName(_fromUtf8("miCopyNodes"))
        self.miCopyBranch = QtGui.QAction(mwGrapher)
        self.miCopyBranch.setObjectName(_fromUtf8("miCopyBranch"))
        self.miCutNodes = QtGui.QAction(mwGrapher)
        self.miCutNodes.setObjectName(_fromUtf8("miCutNodes"))
        self.miCutBranch = QtGui.QAction(mwGrapher)
        self.miCutBranch.setObjectName(_fromUtf8("miCutBranch"))
        self.miPasteNodes = QtGui.QAction(mwGrapher)
        self.miPasteNodes.setObjectName(_fromUtf8("miPasteNodes"))
        self.miMoveUp = QtGui.QAction(mwGrapher)
        self.miMoveUp.setObjectName(_fromUtf8("miMoveUp"))
        self.miMoveDown = QtGui.QAction(mwGrapher)
        self.miMoveDown.setObjectName(_fromUtf8("miMoveDown"))
        self.miSaveAs = QtGui.QAction(mwGrapher)
        self.miSaveAs.setObjectName(_fromUtf8("miSaveAs"))
        self.miSave = QtGui.QAction(mwGrapher)
        self.miSave.setObjectName(_fromUtf8("miSave"))
        self.miLoad = QtGui.QAction(mwGrapher)
        self.miLoad.setObjectName(_fromUtf8("miLoad"))
        self.miXterm = QtGui.QAction(mwGrapher)
        self.miXterm.setObjectName(_fromUtf8("miXterm"))
        self.miXplorer = QtGui.QAction(mwGrapher)
        self.miXplorer.setObjectName(_fromUtf8("miXplorer"))
        self.miQuit = QtGui.QAction(mwGrapher)
        self.miQuit.setObjectName(_fromUtf8("miQuit"))
        self.miNodeEditor = QtGui.QAction(mwGrapher)
        self.miNodeEditor.setCheckable(True)
        self.miNodeEditor.setObjectName(_fromUtf8("miNodeEditor"))
        self.mFile.addAction(self.miLoad)
        self.mFile.addSeparator()
        self.mFile.addAction(self.miSave)
        self.mFile.addAction(self.miSaveAs)
        self.mFile.addSeparator()
        self.mFile.addAction(self.miQuit)
        self.mGraph.addAction(self.miNewNode)
        self.mGraph.addAction(self.miRenameNode)
        self.mGraph.addAction(self.miDeleteNode)
        self.mGraph.addSeparator()
        self.mGraph.addAction(self.miCopyNodes)
        self.mGraph.addAction(self.miCopyBranch)
        self.mGraph.addAction(self.miCutNodes)
        self.mGraph.addAction(self.miCutBranch)
        self.mGraph.addAction(self.miPasteNodes)
        self.mGraph.addSeparator()
        self.mGraph.addAction(self.miMoveUp)
        self.mGraph.addAction(self.miMoveDown)
        self.mPref.addAction(self.miNodeEditor)
        self.mExec.addAction(self.miXterm)
        self.mExec.addAction(self.miXplorer)
        self.menubar.addAction(self.mFile.menuAction())
        self.menubar.addAction(self.mGraph.menuAction())
        self.menubar.addAction(self.mExec.menuAction())
        self.menubar.addAction(self.mLib.menuAction())
        self.menubar.addAction(self.mPref.menuAction())

        self.retranslateUi(mwGrapher)
        QtCore.QMetaObject.connectSlotsByName(mwGrapher)

    def retranslateUi(self, mwGrapher):
        mwGrapher.setWindowTitle(_translate("mwGrapher", "Grapher", None))
        self.cbComment.setText(_translate("mwGrapher", "Comments", None))
        self.cbVariables.setText(_translate("mwGrapher", "Variables", None))
        self.mFile.setTitle(_translate("mwGrapher", "File", None))
        self.mGraph.setTitle(_translate("mwGrapher", "Graph", None))
        self.mLib.setTitle(_translate("mwGrapher", "Lib", None))
        self.mPref.setTitle(_translate("mwGrapher", "Pref", None))
        self.mExec.setTitle(_translate("mwGrapher", "Exec", None))
        self.miNewNode.setText(_translate("mwGrapher", "New Node", None))
        self.miRenameNode.setText(_translate("mwGrapher", "Rename Node", None))
        self.miDeleteNode.setText(_translate("mwGrapher", "Delete Nodes", None))
        self.miCopyNodes.setText(_translate("mwGrapher", "Copy Nodes", None))
        self.miCopyBranch.setText(_translate("mwGrapher", "Copy Branch", None))
        self.miCutNodes.setText(_translate("mwGrapher", "Cut Nodes", None))
        self.miCutBranch.setText(_translate("mwGrapher", "Cut Branch", None))
        self.miPasteNodes.setText(_translate("mwGrapher", "Paste Nodes", None))
        self.miMoveUp.setText(_translate("mwGrapher", "Move Up", None))
        self.miMoveDown.setText(_translate("mwGrapher", "Move Down", None))
        self.miSaveAs.setText(_translate("mwGrapher", "Save As", None))
        self.miSave.setText(_translate("mwGrapher", "Save", None))
        self.miLoad.setText(_translate("mwGrapher", "Load", None))
        self.miXterm.setText(_translate("mwGrapher", "Xterm", None))
        self.miXplorer.setText(_translate("mwGrapher", "Xplorer", None))
        self.miQuit.setText(_translate("mwGrapher", "Quit", None))
        self.miNodeEditor.setText(_translate("mwGrapher", "Node Editor", None))
