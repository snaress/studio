# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\foundation\gui\foundation\_src\wg_projectTree.ui'
#
# Created: Sat Jan 02 16:22:58 2016
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

class Ui_wg_projectTree(object):
    def setupUi(self, wg_projectTree):
        wg_projectTree.setObjectName(_fromUtf8("wg_projectTree"))
        wg_projectTree.resize(222, 300)
        self.gridLayout = QtGui.QGridLayout(wg_projectTree)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_2 = QtGui.QFrame(wg_projectTree)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 0, 0, 1, 1)
        self.hl_entityOptions = QtGui.QHBoxLayout()
        self.hl_entityOptions.setSpacing(12)
        self.hl_entityOptions.setContentsMargins(6, -1, 6, -1)
        self.hl_entityOptions.setObjectName(_fromUtf8("hl_entityOptions"))
        self.l_entity = QtGui.QLabel(wg_projectTree)
        self.l_entity.setObjectName(_fromUtf8("l_entity"))
        self.hl_entityOptions.addWidget(self.l_entity)
        self.rb_asset = QtGui.QRadioButton(wg_projectTree)
        self.rb_asset.setChecked(True)
        self.rb_asset.setObjectName(_fromUtf8("rb_asset"))
        self.bg_entity = QtGui.QButtonGroup(wg_projectTree)
        self.bg_entity.setObjectName(_fromUtf8("bg_entity"))
        self.bg_entity.addButton(self.rb_asset)
        self.hl_entityOptions.addWidget(self.rb_asset)
        self.rb_shot = QtGui.QRadioButton(wg_projectTree)
        self.rb_shot.setObjectName(_fromUtf8("rb_shot"))
        self.bg_entity.addButton(self.rb_shot)
        self.hl_entityOptions.addWidget(self.rb_shot)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hl_entityOptions.addItem(spacerItem)
        self.gridLayout.addLayout(self.hl_entityOptions, 1, 0, 1, 1)
        self.line = QtGui.QFrame(wg_projectTree)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.tw_project = QtGui.QTreeWidget(wg_projectTree)
        self.tw_project.setObjectName(_fromUtf8("tw_project"))
        self.tw_project.headerItem().setText(0, _fromUtf8("1"))
        self.tw_project.header().setVisible(False)
        self.gridLayout.addWidget(self.tw_project, 3, 0, 1, 1)

        self.retranslateUi(wg_projectTree)
        QtCore.QMetaObject.connectSlotsByName(wg_projectTree)

    def retranslateUi(self, wg_projectTree):
        wg_projectTree.setWindowTitle(_translate("wg_projectTree", "Project Tree", None))
        self.l_entity.setText(_translate("wg_projectTree", "Entity: ", None))
        self.rb_asset.setText(_translate("wg_projectTree", "Asset", None))
        self.rb_shot.setText(_translate("wg_projectTree", "Shot", None))

