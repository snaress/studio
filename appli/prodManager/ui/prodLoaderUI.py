# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\prodManager\ui\prodLoader.ui'
#
# Created: Tue Feb 17 01:12:59 2015
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

class Ui_mwProdLoader(object):
    def setupUi(self, mwProdLoader):
        mwProdLoader.setObjectName(_fromUtf8("mwProdLoader"))
        mwProdLoader.resize(333, 300)
        self.centralwidget = QtGui.QWidget(mwProdLoader)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(2)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pbCreate = QtGui.QPushButton(self.centralwidget)
        self.pbCreate.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pbCreate.setObjectName(_fromUtf8("pbCreate"))
        self.gridLayout.addWidget(self.pbCreate, 0, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.hlProjects = QtGui.QHBoxLayout()
        self.hlProjects.setObjectName(_fromUtf8("hlProjects"))
        self.cbAllProjects = QtGui.QCheckBox(self.centralwidget)
        self.cbAllProjects.setChecked(True)
        self.cbAllProjects.setObjectName(_fromUtf8("cbAllProjects"))
        self.bgProjects = QtGui.QButtonGroup(mwProdLoader)
        self.bgProjects.setObjectName(_fromUtf8("bgProjects"))
        self.bgProjects.addButton(self.cbAllProjects)
        self.hlProjects.addWidget(self.cbAllProjects)
        self.cbMyProjects = QtGui.QCheckBox(self.centralwidget)
        self.cbMyProjects.setObjectName(_fromUtf8("cbMyProjects"))
        self.bgProjects.addButton(self.cbMyProjects)
        self.hlProjects.addWidget(self.cbMyProjects)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlProjects.addItem(spacerItem)
        self.gridLayout.addLayout(self.hlProjects, 2, 0, 1, 1)
        self.twProjects = QtGui.QTreeWidget(self.centralwidget)
        self.twProjects.setAlternatingRowColors(False)
        self.twProjects.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.twProjects.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.twProjects.setIndentation(2)
        self.twProjects.setItemsExpandable(False)
        self.twProjects.setExpandsOnDoubleClick(False)
        self.twProjects.setObjectName(_fromUtf8("twProjects"))
        self.twProjects.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.twProjects.headerItem().setFont(0, font)
        self.twProjects.headerItem().setTextAlignment(1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.twProjects.headerItem().setFont(1, font)
        self.twProjects.headerItem().setTextAlignment(2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.twProjects.headerItem().setTextAlignment(3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.twProjects.header().setVisible(True)
        self.twProjects.header().setHighlightSections(False)
        self.twProjects.header().setSortIndicatorShown(True)
        self.twProjects.header().setStretchLastSection(False)
        self.gridLayout.addWidget(self.twProjects, 3, 0, 1, 1)
        self.hlProjectType = QtGui.QHBoxLayout()
        self.hlProjectType.setObjectName(_fromUtf8("hlProjectType"))
        self.cbMovie = QtGui.QCheckBox(self.centralwidget)
        self.cbMovie.setChecked(True)
        self.cbMovie.setObjectName(_fromUtf8("cbMovie"))
        self.hlProjectType.addWidget(self.cbMovie)
        self.cbMarketing = QtGui.QCheckBox(self.centralwidget)
        self.cbMarketing.setChecked(True)
        self.cbMarketing.setObjectName(_fromUtf8("cbMarketing"))
        self.hlProjectType.addWidget(self.cbMarketing)
        self.cbSerie = QtGui.QCheckBox(self.centralwidget)
        self.cbSerie.setChecked(True)
        self.cbSerie.setObjectName(_fromUtf8("cbSerie"))
        self.hlProjectType.addWidget(self.cbSerie)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlProjectType.addItem(spacerItem1)
        self.gridLayout.addLayout(self.hlProjectType, 4, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 1)
        self.hlBtns = QtGui.QHBoxLayout()
        self.hlBtns.setObjectName(_fromUtf8("hlBtns"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlBtns.addItem(spacerItem2)
        self.pbLoad = QtGui.QPushButton(self.centralwidget)
        self.pbLoad.setObjectName(_fromUtf8("pbLoad"))
        self.hlBtns.addWidget(self.pbLoad)
        self.pbClose = QtGui.QPushButton(self.centralwidget)
        self.pbClose.setObjectName(_fromUtf8("pbClose"))
        self.hlBtns.addWidget(self.pbClose)
        self.gridLayout.addLayout(self.hlBtns, 6, 0, 1, 1)
        mwProdLoader.setCentralWidget(self.centralwidget)

        self.retranslateUi(mwProdLoader)
        QtCore.QMetaObject.connectSlotsByName(mwProdLoader)

    def retranslateUi(self, mwProdLoader):
        mwProdLoader.setWindowTitle(_translate("mwProdLoader", "ProdLoader", None))
        self.pbCreate.setText(_translate("mwProdLoader", "Create New Project", None))
        self.cbAllProjects.setText(_translate("mwProdLoader", "All Projects", None))
        self.cbMyProjects.setText(_translate("mwProdLoader", "My Projects", None))
        self.twProjects.setSortingEnabled(True)
        self.twProjects.headerItem().setText(0, _translate("mwProdLoader", "Alias", None))
        self.twProjects.headerItem().setText(1, _translate("mwProdLoader", "Name", None))
        self.twProjects.headerItem().setText(2, _translate("mwProdLoader", "Season", None))
        self.twProjects.headerItem().setText(3, _translate("mwProdLoader", "Episode", None))
        self.cbMovie.setText(_translate("mwProdLoader", "Movie", None))
        self.cbMarketing.setText(_translate("mwProdLoader", "Marketing", None))
        self.cbSerie.setText(_translate("mwProdLoader", "Serie", None))
        self.pbLoad.setText(_translate("mwProdLoader", "Load", None))
        self.pbClose.setText(_translate("mwProdLoader", "Close", None))

