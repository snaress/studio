# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\ui\grapher.ui'
#
# Created: Tue Nov 18 04:24:08 2014
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
        self.glGrapher = QtGui.QGridLayout(self.centralwidget)
        self.glGrapher.setMargin(2)
        self.glGrapher.setSpacing(2)
        self.glGrapher.setObjectName(_fromUtf8("glGrapher"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
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
        self.glGrapher.addWidget(self.splitter, 0, 0, 1, 1)
        mwGrapher.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mwGrapher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mwGrapher.setMenuBar(self.menubar)

        self.retranslateUi(mwGrapher)
        QtCore.QMetaObject.connectSlotsByName(mwGrapher)

    def retranslateUi(self, mwGrapher):
        mwGrapher.setWindowTitle(_translate("mwGrapher", "Grapher", None))
        self.cbComment.setText(_translate("mwGrapher", "Comments", None))
        self.cbVariables.setText(_translate("mwGrapher", "Variables", None))

