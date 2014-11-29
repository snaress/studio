# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\factory\ui\wgtThumbnail.ui'
#
# Created: Thu Nov 27 17:27:00 2014
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

class Ui_thumbnail(object):
    def setupUi(self, thumbnail):
        thumbnail.setObjectName(_fromUtf8("thumbnail"))
        thumbnail.resize(116, 142)
        thumbnail.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout = QtGui.QGridLayout(thumbnail)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cbPreview = QtGui.QCheckBox(thumbnail)
        self.cbPreview.setMinimumSize(QtCore.QSize(0, 0))
        self.cbPreview.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbPreview.setText(_fromUtf8(""))
        self.cbPreview.setObjectName(_fromUtf8("cbPreview"))
        self.gridLayout.addWidget(self.cbPreview, 3, 1, 1, 1)
        self.bPreview = QtGui.QPushButton(thumbnail)
        self.bPreview.setMinimumSize(QtCore.QSize(110, 110))
        self.bPreview.setMaximumSize(QtCore.QSize(110, 110))
        self.bPreview.setText(_fromUtf8(""))
        self.bPreview.setIconSize(QtCore.QSize(100, 100))
        self.bPreview.setCheckable(True)
        self.bPreview.setFlat(False)
        self.bPreview.setObjectName(_fromUtf8("bPreview"))
        self.gridLayout.addWidget(self.bPreview, 1, 1, 1, 1)
        self.line_3 = QtGui.QFrame(thumbnail)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 1, 0, 3, 1)
        self.line_2 = QtGui.QFrame(thumbnail)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 0, 1, 1, 1)
        self.lName = QtGui.QLabel(thumbnail)
        self.lName.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lName.setAlignment(QtCore.Qt.AlignCenter)
        self.lName.setObjectName(_fromUtf8("lName"))
        self.gridLayout.addWidget(self.lName, 2, 1, 1, 1)
        self.line = QtGui.QFrame(thumbnail)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 4, 1, 1, 1)
        self.line_4 = QtGui.QFrame(thumbnail)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 1, 2, 3, 1)

        self.retranslateUi(thumbnail)
        QtCore.QMetaObject.connectSlotsByName(thumbnail)

    def retranslateUi(self, thumbnail):
        thumbnail.setWindowTitle(_translate("thumbnail", "Thumbnail", None))
        self.lName.setText(_translate("thumbnail", "Name", None))

