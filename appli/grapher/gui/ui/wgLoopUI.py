# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\rnd\workspace\studio\appli\grapher\gui\src\wgLoop.ui'
#
# Created: Sat Oct 17 15:28:03 2015
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

class Ui_wgLoop(object):
    def setupUi(self, wgLoop):
        wgLoop.setObjectName(_fromUtf8("wgLoop"))
        wgLoop.resize(509, 122)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wgLoop.sizePolicy().hasHeightForWidth())
        wgLoop.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(wgLoop)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.qfLoopSingle = QtGui.QFrame(wgLoop)
        self.qfLoopSingle.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qfLoopSingle.setObjectName(_fromUtf8("qfLoopSingle"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.qfLoopSingle)
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.lLoopSingle = QtGui.QLabel(self.qfLoopSingle)
        self.lLoopSingle.setMinimumSize(QtCore.QSize(50, 0))
        self.lLoopSingle.setObjectName(_fromUtf8("lLoopSingle"))
        self.horizontalLayout_9.addWidget(self.lLoopSingle)
        self.leLoopSingle = QtGui.QLineEdit(self.qfLoopSingle)
        self.leLoopSingle.setMaximumSize(QtCore.QSize(125, 16777215))
        self.leLoopSingle.setObjectName(_fromUtf8("leLoopSingle"))
        self.horizontalLayout_9.addWidget(self.leLoopSingle)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.gridLayout.addWidget(self.qfLoopSingle, 7, 0, 1, 1)
        self.qfLoopRange = QtGui.QFrame(wgLoop)
        self.qfLoopRange.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qfLoopRange.setObjectName(_fromUtf8("qfLoopRange"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.qfLoopRange)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.lLoopRange = QtGui.QLabel(self.qfLoopRange)
        self.lLoopRange.setMinimumSize(QtCore.QSize(50, 0))
        self.lLoopRange.setObjectName(_fromUtf8("lLoopRange"))
        self.horizontalLayout_7.addWidget(self.lLoopRange)
        self.lRangeStart = QtGui.QLabel(self.qfLoopRange)
        self.lRangeStart.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lRangeStart.setObjectName(_fromUtf8("lRangeStart"))
        self.horizontalLayout_7.addWidget(self.lRangeStart)
        self.leRangeStart = QtGui.QLineEdit(self.qfLoopRange)
        self.leRangeStart.setMaximumSize(QtCore.QSize(60, 16777215))
        self.leRangeStart.setObjectName(_fromUtf8("leRangeStart"))
        self.horizontalLayout_7.addWidget(self.leRangeStart)
        spacerItem1 = QtGui.QSpacerItem(25, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.lRangeStop = QtGui.QLabel(self.qfLoopRange)
        self.lRangeStop.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lRangeStop.setObjectName(_fromUtf8("lRangeStop"))
        self.horizontalLayout_7.addWidget(self.lRangeStop)
        self.leRangeStop = QtGui.QLineEdit(self.qfLoopRange)
        self.leRangeStop.setMaximumSize(QtCore.QSize(60, 16777215))
        self.leRangeStop.setObjectName(_fromUtf8("leRangeStop"))
        self.horizontalLayout_7.addWidget(self.leRangeStop)
        spacerItem2 = QtGui.QSpacerItem(25, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.lRangeStep = QtGui.QLabel(self.qfLoopRange)
        self.lRangeStep.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lRangeStep.setObjectName(_fromUtf8("lRangeStep"))
        self.horizontalLayout_7.addWidget(self.lRangeStep)
        self.leRangeStep = QtGui.QLineEdit(self.qfLoopRange)
        self.leRangeStep.setMaximumSize(QtCore.QSize(60, 16777215))
        self.leRangeStep.setObjectName(_fromUtf8("leRangeStep"))
        self.horizontalLayout_7.addWidget(self.leRangeStep)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.gridLayout.addWidget(self.qfLoopRange, 5, 0, 1, 1)
        self.qfLoopList = QtGui.QFrame(wgLoop)
        self.qfLoopList.setFrameShape(QtGui.QFrame.StyledPanel)
        self.qfLoopList.setObjectName(_fromUtf8("qfLoopList"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.qfLoopList)
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.lLoopList = QtGui.QLabel(self.qfLoopList)
        self.lLoopList.setMinimumSize(QtCore.QSize(50, 0))
        self.lLoopList.setObjectName(_fromUtf8("lLoopList"))
        self.horizontalLayout_8.addWidget(self.lLoopList)
        self.leLoopList = QtGui.QLineEdit(self.qfLoopList)
        self.leLoopList.setObjectName(_fromUtf8("leLoopList"))
        self.horizontalLayout_8.addWidget(self.leLoopList)
        self.gridLayout.addWidget(self.qfLoopList, 6, 0, 1, 1)
        self.hlLoopMode = QtGui.QHBoxLayout()
        self.hlLoopMode.setSpacing(2)
        self.hlLoopMode.setContentsMargins(4, -1, 4, -1)
        self.hlLoopMode.setObjectName(_fromUtf8("hlLoopMode"))
        self.cbRemote = QtGui.QCheckBox(wgLoop)
        self.cbRemote.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cbRemote.setObjectName(_fromUtf8("cbRemote"))
        self.hlLoopMode.addWidget(self.cbRemote)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlLoopMode.addItem(spacerItem4)
        self.lMode = QtGui.QLabel(wgLoop)
        self.lMode.setObjectName(_fromUtf8("lMode"))
        self.hlLoopMode.addWidget(self.lMode)
        self.rbIncremental = QtGui.QRadioButton(wgLoop)
        self.rbIncremental.setChecked(True)
        self.rbIncremental.setObjectName(_fromUtf8("rbIncremental"))
        self.bgLoopMode = QtGui.QButtonGroup(wgLoop)
        self.bgLoopMode.setObjectName(_fromUtf8("bgLoopMode"))
        self.bgLoopMode.addButton(self.rbIncremental)
        self.hlLoopMode.addWidget(self.rbIncremental)
        self.rbSequential = QtGui.QRadioButton(wgLoop)
        self.rbSequential.setObjectName(_fromUtf8("rbSequential"))
        self.bgLoopMode.addButton(self.rbSequential)
        self.hlLoopMode.addWidget(self.rbSequential)
        self.gridLayout.addLayout(self.hlLoopMode, 1, 0, 1, 1)
        self.line_2 = QtGui.QFrame(wgLoop)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 1)
        self.line_3 = QtGui.QFrame(wgLoop)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 8, 0, 1, 1)
        self.line = QtGui.QFrame(wgLoop)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 0, 1, 1)
        self.hlLoopOption = QtGui.QHBoxLayout()
        self.hlLoopOption.setSpacing(2)
        self.hlLoopOption.setContentsMargins(4, -1, 4, -1)
        self.hlLoopOption.setObjectName(_fromUtf8("hlLoopOption"))
        self.lType = QtGui.QLabel(wgLoop)
        self.lType.setMinimumSize(QtCore.QSize(50, 0))
        self.lType.setObjectName(_fromUtf8("lType"))
        self.hlLoopOption.addWidget(self.lType)
        self.rbLoopRange = QtGui.QRadioButton(wgLoop)
        self.rbLoopRange.setChecked(True)
        self.rbLoopRange.setObjectName(_fromUtf8("rbLoopRange"))
        self.bgLoopType = QtGui.QButtonGroup(wgLoop)
        self.bgLoopType.setObjectName(_fromUtf8("bgLoopType"))
        self.bgLoopType.addButton(self.rbLoopRange)
        self.hlLoopOption.addWidget(self.rbLoopRange)
        self.rbLoopList = QtGui.QRadioButton(wgLoop)
        self.rbLoopList.setObjectName(_fromUtf8("rbLoopList"))
        self.bgLoopType.addButton(self.rbLoopList)
        self.hlLoopOption.addWidget(self.rbLoopList)
        self.rbLoopSingle = QtGui.QRadioButton(wgLoop)
        self.rbLoopSingle.setObjectName(_fromUtf8("rbLoopSingle"))
        self.bgLoopType.addButton(self.rbLoopSingle)
        self.hlLoopOption.addWidget(self.rbLoopSingle)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlLoopOption.addItem(spacerItem5)
        self.lLoopIter = QtGui.QLabel(wgLoop)
        self.lLoopIter.setObjectName(_fromUtf8("lLoopIter"))
        self.hlLoopOption.addWidget(self.lLoopIter)
        self.leLoopIter = QtGui.QLineEdit(wgLoop)
        self.leLoopIter.setMinimumSize(QtCore.QSize(60, 0))
        self.leLoopIter.setMaximumSize(QtCore.QSize(60, 16777215))
        self.leLoopIter.setAlignment(QtCore.Qt.AlignCenter)
        self.leLoopIter.setObjectName(_fromUtf8("leLoopIter"))
        self.hlLoopOption.addWidget(self.leLoopIter)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hlLoopOption.addItem(spacerItem6)
        self.lLoopCheckFile = QtGui.QLabel(wgLoop)
        self.lLoopCheckFile.setObjectName(_fromUtf8("lLoopCheckFile"))
        self.hlLoopOption.addWidget(self.lLoopCheckFile)
        self.leLoopCheckFile = QtGui.QLineEdit(wgLoop)
        self.leLoopCheckFile.setMinimumSize(QtCore.QSize(100, 0))
        self.leLoopCheckFile.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leLoopCheckFile.setObjectName(_fromUtf8("leLoopCheckFile"))
        self.hlLoopOption.addWidget(self.leLoopCheckFile)
        self.gridLayout.addLayout(self.hlLoopOption, 3, 0, 1, 1)
        self.line_4 = QtGui.QFrame(wgLoop)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 4, 0, 1, 1)

        self.retranslateUi(wgLoop)
        QtCore.QMetaObject.connectSlotsByName(wgLoop)

    def retranslateUi(self, wgLoop):
        wgLoop.setWindowTitle(_translate("wgLoop", "Loop", None))
        self.lLoopSingle.setText(_translate("wgLoop", "Single : ", None))
        self.lLoopRange.setText(_translate("wgLoop", "Range : ", None))
        self.lRangeStart.setText(_translate("wgLoop", "Start = ", None))
        self.leRangeStart.setText(_translate("wgLoop", "1", None))
        self.lRangeStop.setText(_translate("wgLoop", "Stop = ", None))
        self.leRangeStop.setText(_translate("wgLoop", "100", None))
        self.lRangeStep.setText(_translate("wgLoop", "Step = ", None))
        self.leRangeStep.setText(_translate("wgLoop", "1", None))
        self.lLoopList.setText(_translate("wgLoop", "List : ", None))
        self.cbRemote.setText(_translate("wgLoop", "Remote: ", None))
        self.lMode.setText(_translate("wgLoop", "Mode: ", None))
        self.rbIncremental.setText(_translate("wgLoop", "Incremental", None))
        self.rbSequential.setText(_translate("wgLoop", "Sequential", None))
        self.lType.setText(_translate("wgLoop", "Type: ", None))
        self.rbLoopRange.setText(_translate("wgLoop", "Range", None))
        self.rbLoopList.setText(_translate("wgLoop", "List", None))
        self.rbLoopSingle.setText(_translate("wgLoop", "Single", None))
        self.lLoopIter.setText(_translate("wgLoop", "Iterator: ", None))
        self.leLoopIter.setText(_translate("wgLoop", "i", None))
        self.lLoopCheckFile.setText(_translate("wgLoop", "CheckFile: ", None))
        self.leLoopCheckFile.setText(_translate("wgLoop", "tmpCheck", None))

