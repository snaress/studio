# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\foundation\gui\foundation\_src\foundation.ui'
#
# Created: Sat Jan 02 18:19:55 2016
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

class Ui_mw_foundation(object):
    def setupUi(self, mw_foundation):
        mw_foundation.setObjectName(_fromUtf8("mw_foundation"))
        mw_foundation.resize(502, 398)
        self.centralwidget = QtGui.QWidget(mw_foundation)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.qf_left = QtGui.QFrame(self.centralwidget)
        self.qf_left.setMinimumSize(QtCore.QSize(300, 0))
        self.qf_left.setMaximumSize(QtCore.QSize(300, 16777215))
        self.qf_left.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qf_left.setObjectName(_fromUtf8("qf_left"))
        self.vl_left = QtGui.QVBoxLayout(self.qf_left)
        self.vl_left.setSpacing(0)
        self.vl_left.setMargin(0)
        self.vl_left.setObjectName(_fromUtf8("vl_left"))
        self.qf_treeUp = QtGui.QFrame(self.qf_left)
        self.qf_treeUp.setMinimumSize(QtCore.QSize(0, 250))
        self.qf_treeUp.setMaximumSize(QtCore.QSize(16777215, 250))
        self.qf_treeUp.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qf_treeUp.setObjectName(_fromUtf8("qf_treeUp"))
        self.vl_treeUp = QtGui.QVBoxLayout(self.qf_treeUp)
        self.vl_treeUp.setSpacing(0)
        self.vl_treeUp.setMargin(0)
        self.vl_treeUp.setObjectName(_fromUtf8("vl_treeUp"))
        self.vl_left.addWidget(self.qf_treeUp)
        self.qf_treeDn = QtGui.QFrame(self.qf_left)
        self.qf_treeDn.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qf_treeDn.setObjectName(_fromUtf8("qf_treeDn"))
        self.vl_treeDn = QtGui.QVBoxLayout(self.qf_treeDn)
        self.vl_treeDn.setSpacing(0)
        self.vl_treeDn.setMargin(0)
        self.vl_treeDn.setObjectName(_fromUtf8("vl_treeDn"))
        self.vl_left.addWidget(self.qf_treeDn)
        self.gridLayout.addWidget(self.qf_left, 0, 0, 1, 1)
        self.qf_right = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qf_right.sizePolicy().hasHeightForWidth())
        self.qf_right.setSizePolicy(sizePolicy)
        self.qf_right.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qf_right.setObjectName(_fromUtf8("qf_right"))
        self.vl_right = QtGui.QVBoxLayout(self.qf_right)
        self.vl_right.setSpacing(0)
        self.vl_right.setMargin(0)
        self.vl_right.setObjectName(_fromUtf8("vl_right"))
        self.qf_datasUp = QtGui.QFrame(self.qf_right)
        self.qf_datasUp.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qf_datasUp.setObjectName(_fromUtf8("qf_datasUp"))
        self.vl_datas = QtGui.QVBoxLayout(self.qf_datasUp)
        self.vl_datas.setSpacing(0)
        self.vl_datas.setMargin(0)
        self.vl_datas.setObjectName(_fromUtf8("vl_datas"))
        self.vl_right.addWidget(self.qf_datasUp)
        self.qf_datasDn = QtGui.QFrame(self.qf_right)
        self.qf_datasDn.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qf_datasDn.setObjectName(_fromUtf8("qf_datasDn"))
        self.vl_log = QtGui.QVBoxLayout(self.qf_datasDn)
        self.vl_log.setSpacing(0)
        self.vl_log.setMargin(0)
        self.vl_log.setObjectName(_fromUtf8("vl_log"))
        self.vl_right.addWidget(self.qf_datasDn)
        self.gridLayout.addWidget(self.qf_right, 0, 1, 1, 1)
        mw_foundation.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(mw_foundation)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 502, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.m_project = QtGui.QMenu(self.menuBar)
        self.m_project.setObjectName(_fromUtf8("m_project"))
        self.m_help = QtGui.QMenu(self.menuBar)
        self.m_help.setObjectName(_fromUtf8("m_help"))
        self.m_logLevel = QtGui.QMenu(self.m_help)
        self.m_logLevel.setObjectName(_fromUtf8("m_logLevel"))
        mw_foundation.setMenuBar(self.menuBar)
        self.mi_log = QtGui.QAction(mw_foundation)
        self.mi_log.setCheckable(True)
        self.mi_log.setObjectName(_fromUtf8("mi_log"))
        self.mi_userGroups = QtGui.QAction(mw_foundation)
        self.mi_userGroups.setObjectName(_fromUtf8("mi_userGroups"))
        self.mi_newProject = QtGui.QAction(mw_foundation)
        self.mi_newProject.setObjectName(_fromUtf8("mi_newProject"))
        self.mi_loadProject = QtGui.QAction(mw_foundation)
        self.mi_loadProject.setObjectName(_fromUtf8("mi_loadProject"))
        self.mi_projectSettings = QtGui.QAction(mw_foundation)
        self.mi_projectSettings.setObjectName(_fromUtf8("mi_projectSettings"))
        self.actionTmp1 = QtGui.QAction(mw_foundation)
        self.actionTmp1.setObjectName(_fromUtf8("actionTmp1"))
        self.mi_toolTips = QtGui.QAction(mw_foundation)
        self.mi_toolTips.setCheckable(True)
        self.mi_toolTips.setChecked(True)
        self.mi_toolTips.setObjectName(_fromUtf8("mi_toolTips"))
        self.m_project.addAction(self.mi_newProject)
        self.m_project.addAction(self.mi_loadProject)
        self.m_project.addSeparator()
        self.m_project.addAction(self.mi_projectSettings)
        self.m_help.addAction(self.m_logLevel.menuAction())
        self.m_help.addAction(self.mi_toolTips)
        self.menuBar.addAction(self.m_project.menuAction())
        self.menuBar.addAction(self.m_help.menuAction())

        self.retranslateUi(mw_foundation)
        QtCore.QMetaObject.connectSlotsByName(mw_foundation)

    def retranslateUi(self, mw_foundation):
        mw_foundation.setWindowTitle(_translate("mw_foundation", "Foundation", None))
        self.m_project.setTitle(_translate("mw_foundation", "Project", None))
        self.m_help.setTitle(_translate("mw_foundation", "Help", None))
        self.m_logLevel.setTitle(_translate("mw_foundation", "Log Level", None))
        self.mi_log.setText(_translate("mw_foundation", "Log", None))
        self.mi_userGroups.setText(_translate("mw_foundation", "UserGroups", None))
        self.mi_newProject.setText(_translate("mw_foundation", "New Project", None))
        self.mi_loadProject.setText(_translate("mw_foundation", "Load Project", None))
        self.mi_projectSettings.setText(_translate("mw_foundation", "Project Settings", None))
        self.actionTmp1.setText(_translate("mw_foundation", "tmp1", None))
        self.mi_toolTips.setText(_translate("mw_foundation", "Tool Tips", None))

