import os
from lib import qt
from PyQt4 import QtGui, QtCore
from lib.system import procFile as pFile

#========================================== Compile Ui ===========================================#

class CompileUi(object):
    """ Convert uiFile to pyFile
        :param uiFile: uiFile absolut path
        :type uiFile: str
        :param pyFile: pyFile absolut path
        :type pyFile: str
        :param uiDir: Path to list
        :type uiDir: str
        :param pyUic: pyuic.bat absolut path
        :type pyUic: str """

    def __init__(self, uiFile=None, pyFile=None, uiDir=None, pyUic=None):
        print "#----- Compile UI -----#"
        self.pyUic = pyUic
        if self.pyUic is None:
            self.pyUic = "C:/Python27/Lib/site-packages/PyQt4/pyuic4.bat"
        self.uiFile = uiFile
        self.pyFile = pyFile
        self.uiDir = uiDir
        self.uiToPy()

    def uiToPy(self):
        """ Check kwargs
            :return: uiFiles ansolut path, pyFiles absolut path
            :rtype: (list, list) """
        if self.uiFile is None and self.pyFile is None and self.uiDir is None:
            raise KeyError, "Error: All kwargs are empty !!!"
        if self.uiFile is not None and self.pyFile is not None:
            if self.checkDate(self.uiFile, self.pyFile) in ['create', 'update']:
                self.convert(self.uiFile, self.pyFile)
        elif self.uiFile is not None and self.pyFile is None:
            if self.checkDate(self.uiFile, self.uiFile.replace('.ui', 'UI.py')) in ['create', 'update']:
                self.convert(self.uiFile, self.uiFile.replace('.ui', 'UI.py'))
        elif self.uiDir is not None:
            print "uiDir = %s" % self.uiDir
            files = os.listdir(self.uiDir) or []
            for f in files:
                if f.endswith('.ui'):
                    uiFile = os.path.join(self.uiDir, f)
                    pyFile = os.path.join(self.uiDir, f.replace('.ui', 'UI.py'))
                    if self.checkDate(uiFile, pyFile) in ['create', 'update']:
                        self.convert(uiFile, pyFile)
        else:
            raise KeyError, "uiFile=%s, pyFile=%s, uiDir=%s" % (self.uiFile, self.pyFile, self.uiDir)

    @staticmethod
    def checkDate(uiFile, pyFile):
        """ Compare uiFile and pyFile modif date
            :param uiFile: uiFile absolut path
            :type uiFile: str
            :param pyFile: pyFile absolut path
            :type pyFile: str
            :return: 'create', 'update', 'ok'
            :rtype: str """
        if pyFile is None:
            print "%s \t ---> \t CREATE" % os.path.basename(pyFile)
            return 'create'
        else:
            if not os.path.exists(pyFile):
                print "%s \t ---> \t CREATE" % os.path.basename(pyFile)
                return 'create'
            else:
                uiDate = os.path.getmtime(uiFile)
                pyDate = os.path.getmtime(pyFile)
                if uiDate > pyDate:
                    print "%s \t ---> \t UPDATE" % os.path.basename(pyFile)
                    return 'update'
                else:
                    print "%s \t ---> \t OK" % os.path.basename(pyFile)
                    return 'ok'

    def convert(self, uiFile, pyFile):
        """ Convert uiFile into pyFile
            :param uiFile: uiFile absolut path
            :type uiFile: str
            :param pyFile: pyFile absolut path
            :type pyFile: str """
        try:
            os.system("%s %s > %s" % (self.pyUic, uiFile, pyFile))
        except:
            raise IOError, "Error: Can not convert %s" % pyFile

#============================================ Action =============================================#

def popupMenu(menuDict):
    """ Create a popup menu with given dict
        :param menuDict: {0: ['label', 'cmd']}
        :type menuDict: dict
        :return: QMenu
        :rtype: QtGui.QMenu """
    pmMenu = QtGui.QMenu()
    pmMenu.items = []
    pmMenu.popup(QtGui.QCursor.pos())
    for ind in sorted(menuDict.keys()):
        qAction = pmMenu.addAction(menuDict[ind][0])
        qAction.triggered.connect(menuDict[ind][1])
        pmMenu.items.append(qAction)
    return pmMenu

class ClickHandler(object):
    """ Activate double click for QPushButton
        :param dcTimer: Time in milliSec
        :type dcTimer: int
        :param singleClickCmd: Command launch when single click is detected
        :type singleClickCmd: function
        :param doubleClickCmd: Command launch when double click is detected
        :type doubleClickCmd: function """

    def __init__(self, dcTimer=200, singleClickCmd=None, doubleClickCmd=None):
        self.singleCmd = singleClickCmd
        self.doubleCmd = doubleClickCmd
        self.timer = QtCore.QTimer()
        self.timer.setInterval(dcTimer)
        self.timer.setSingleShot(True)
        # noinspection PyUnresolvedReferences
        self.timer.timeout.connect(self.timeout)
        self.click_count = 0

    def timeout(self):
        if self.click_count == 1:
            if self.singleCmd is not None:
                self.singleCmd()
        elif self.click_count > 1:
            if self.doubleCmd is not None:
                self.doubleCmd()
        self.click_count = 0

    def __call__(self):
        self.click_count += 1
        if not self.timer.isActive():
            self.timer.start()

#========================================== QTreeWidget ==========================================#

def getAllItems(QTreeWidget):
    """ Get all QTreeWidgetItem of given QTreeWidget
        :param QTreeWidget: QTreeWidget object
        :type QTreeWidget: QtGui.QTreeWidget
        :return: All QTreeWidgetItem list
        :rtype: list """
    items = []
    allItems = QtGui.QTreeWidgetItemIterator(QTreeWidget, QtGui.QTreeWidgetItemIterator.All) or None
    if allItems is not None:
        while allItems.value():
            item = allItems.value()
            items.append(item)
            allItems += 1
    return items

def getTopItems(QTreeWidget):
    """ Get all topLevelItems of given QTreeWidget
        :param QTreeWidget: QTreeWidget object
        :type QTreeWidget: QtGui.QTreeWidget
        :return: All topLevelItem list
        :rtype: list """
    items = []
    nTop = QTreeWidget.topLevelItemCount()
    for n in range(nTop):
        items.append(QTreeWidget.topLevelItem(n))
    return items

def getAllChildren(QTreeWidgetItem, depth=-1):
    """ Get all children of given QTreeWidgetItem
        :param QTreeWidgetItem: Recusion start QTreeWidgetItem
        :type QTreeWidgetItem: QTreeWidgetItem
        :param depth: Number of recursion (-1 = infinite)
        :type depth: int
        :return: QTreeWigdetItem list
        :rtype: list """
    items = []

    def recurse(currentItem, depth):
        items.append(currentItem)
        if depth != 0:
            for n in range(currentItem.childCount()):
                recurse(currentItem.child(n), depth-1)

    recurse(QTreeWidgetItem, depth)
    return items

def getAllParent(QTreeWidgetItem, depth=-1):
    """ Get all parent of given QTreeWidgetItem
        :param QTreeWidgetItem: Recusion start QTreeWidgetItem
        :type QTreeWidgetItem: QtGui.QTreeWidgetItem
        :param depth: Number of recursion (-1 = infinite)
        :type depth: int
        :return: QTreeWigdetItem list
        :rtype: list """
    items = []

    def recurse(currentItem, depth):
        items.append(currentItem)
        if depth != 0:
            if currentItem.parent() is not None:
                recurse(currentItem.parent(), depth-1)

    recurse(QTreeWidgetItem, depth)
    return items

def moveSelItems(twTree, item, side):
    """ Move Selected items
        :param twTree: (object) : QTreeWidget
        :type twTree: QtGui.QTreeWidget
        :param side: (str) : 'up' or 'down'
        :type side: str
        :return: Moved QTreeWidgetItems
        :rtype: list """
    movedItem = None
    #-- Move Child Item --#
    if item.parent() is not None:
        ind = item.parent().indexOfChild(item)
        if side == 'up':
            if ind > 0:
                movedItem = item.parent().takeChild(ind)
                item.parent().insertChild(ind-1, movedItem)
        elif side == 'down':
            N = item.parent().childCount()
            if ind < N-1:
                movedItem = item.parent().takeChild(ind)
                item.parent().insertChild(ind+1, movedItem)
    #-- Move Top Items --#
    else:
        ind = twTree.indexOfTopLevelItem(item)
        if side == 'up':
            if ind > 0:
                movedItem = twTree.takeTopLevelItem(ind)
                twTree.insertTopLevelItem(ind-1, movedItem)
        elif side == 'down':
            N = twTree.topLevelItemCount()
            if ind < N-1:
                movedItem = twTree.takeTopLevelItem(ind)
                twTree.insertTopLevelItem(ind+1, movedItem)
    return movedItem

def delSelItems(twTree):
    """ Remove selected QTreeWidgetItems from given QTreeWidget
        :param twTree: QTreeWidget
        :type twTree: QtGui.QTreeWidget"""
    selItems = twTree.selectedItems()
    for item in selItems:
        if item.parent() is None:
            ind = twTree.indexOfTopLevelItem(item)
            twTree.takeTopLevelItem(ind)
        else:
            ind = item.parent().indexOfChild(item)
            item.parent().takeChild(ind)

def deselectAllItems(twTree):
    """ Deselected QTreeWidgetItems from given QTreeWidget
        :param twTree: QTreeWidget
        :type twTree: QtGui.QTreeWidget"""
    selItems = twTree.selectedItems()
    for item in selItems:
        twTree.setItemSelected(item, False)

#=========================================== QComboBox ===========================================#

def getComboBoxItems(QComboBox):
    """ Get all given conboBox items
        :param QComboBox: QComboBox
        :type QComboBox: QtGui.QComboBox
        :return: Items text list
        :rtype: list """
    items = []
    for n in range(QComboBox.count()):
        items.append(str(QComboBox.itemText(n)))
    return items

#============================================ QDialog ============================================#

def fileDialog(fdMode='open', fdFileMode='AnyFile', fdRoot=None, fdRoots=None,
               fdFilters=None, fdCmd=None):
    """ FileDialog popup
        :param fdMode: setAcceptMode 'open' or 'save'
        :type fdMode: str
        :param fdFileMode: setFileMode 'AnyFile', 'ExistingFile', 'Directory', 'DirectoryOnly'
        :type fdFileMode: str
        :param fdRoot: Start root path
        :type fdRoot: str
        :param fdRoots: List of recent files (list[str(QUrl)])
        :type fdRoots: list
        :param fdFilters: List of extensions
        :type fdFilters: list
        :param fdCmd: Command for accepted execution
        :type fdCmd: function
        :return: (object) : QFileDialog widget object
        :rtype: QtGui.QFileDialog """
    fd = QtGui.QFileDialog()
    #-- FileDialog AcceptedMode --#
    if fdMode == 'open':
        fd.setAcceptMode(QtGui.QFileDialog.AcceptOpen)
    elif fdMode == 'save':
        fd.setAcceptMode(QtGui.QFileDialog.AcceptSave)
    #-- FileDialog FileMode --#
    if fdFileMode == 'AnyFile':
        fd.setFileMode(QtGui.QFileDialog.AnyFile)
    elif fdFileMode == 'ExistingFile':
        fd.setFileMode(QtGui.QFileDialog.ExistingFile)
    elif fdFileMode == 'Directory':
        fd.setFileMode(QtGui.QFileDialog.Directory)
    elif fdFileMode == 'DirectoryOnly':
        fd.setFileMode(QtGui.QFileDialog.DirectoryOnly)
    #-- FileDialog Params --#
    if fdRoot is not None:
        fd.setDirectory(fdRoot)
    if fdRoots is not None:
        fd.setSidebarUrls(fdRoots)
    if fdFilters is not None:
        fd.setFilters(fdFilters)
    if fdCmd is not None:
        # noinspection PyUnresolvedReferences
        fd.accepted.connect(fdCmd)
    return fd

def errorDialog(message, parent):
    """ Launch default error dialog
        :param message: (str or list): Message to print
        :type message: str | list
        :param parent: (object) : Parent ui
        :type parent: QtGui.QMainWindow | QtGui.QWidget """
    errorDial = QtGui.QErrorMessage(parent)
    if isinstance(message, list):
        errorDial.showMessage('\n'.join(message))
    else:
        errorDial.showMessage(message)


if __name__ == '__main__':
    CompileUi(uiFile=qt.uiList['confirmDialog'])
from lib.qt.ui import confirmDialogUI
class ConfirmDialog(QtGui.QDialog, confirmDialogUI.Ui_Dialog):
    """ Confirm dialog popup
        :param message: Dialog texte
        :type message: str
        :param buttons: Buttons list
        :type buttons: list
        :param btnCmds: Commands list
        :type btnCmds: list
        :param cancelBtn: Add cacnel button
        :type cancelBtn: bool """

    def __init__(self, message, buttons, btnCmds, cancelBtn=True):
        if not len(buttons) == len(btnCmds):
            raise KeyError, "!!! Error: Buttons list and cmds lists should have same length !!!"
        else:
            self.mess = message
            buttons.reverse()
            self.btns = buttons
            btnCmds.reverse()
            self.btnCmds = btnCmds
            self.cancelBtn = cancelBtn
            super(ConfirmDialog, self).__init__()
            self.setupUi(self)
            self.initDialog()

    def initDialog(self):
        """ Init dialog window """
        self.lMessage.setText(self.mess)
        if self.cancelBtn:
            newButton = self.newButton('Cancel', self.close)
            self.hlButtons.insertWidget(1, newButton)
        for n, btn in enumerate(self.btns):
            newButton = self.newButton(btn, self.btnCmds[n])
            self.hlButtons.insertWidget(1, newButton)

    @staticmethod
    def newButton(label, btnCmd):
        """ Create new button
            :param label: Button label
            :type label: str
            :param btnCmd: Button command
            :type btnCmd: function
            :return: New QPushButton
            :rtype: QtGui.QPushButton """
        newButton = QtGui.QPushButton()
        newButton.setText(label)
        # noinspection PyUnresolvedReferences
        newButton.clicked.connect(btnCmd)
        return newButton


if __name__ == '__main__':
    CompileUi(uiFile=qt.uiList['promptDialog'])
from lib.qt.ui import promptDialogUI
class PromptDialog(QtGui.QDialog, promptDialogUI.Ui_Dialog):
    """ Prompt dialog popup
        :param message: Dialog texte
        :type message: str
        :param acceptCmd: Accept command
        :type acceptCmd: function
        :param cancelCmd: Cancel command
        :type cancelCmd: function
        :param Nlines: Prompt line count
        :type Nlines: int """

    def __init__(self, message, acceptCmd, cancelCmd=None, Nlines=1):
        self.message = message
        self.acceptCmd = acceptCmd
        self.cancelCmd = cancelCmd
        self.Nlines = Nlines
        super(PromptDialog, self).__init__()
        self.setupUi(self)
        self.initDialog()

    def initDialog(self):
        """ Init dialog window """
        self.lMessage.setText(self.message)
        for n in range(self.Nlines):
            newWidget = QtGui.QLineEdit()
            newItem = QtGui.QTreeWidgetItem()
            newItem._widget = newWidget
            self.twPrompt.addTopLevelItem(newItem)
            self.twPrompt.setItemWidget(newItem, 0, newWidget)
        self.bAccept.clicked.connect(self.acceptCmd)
        if self.cancelCmd is None:
            self.bCancel.clicked.connect(self.close)
        else:
            self.bCancel.clicked.connect(self.cancelCmd)

    def result(self):
        """ Get QLineEdit value
            :return: Prompt result
            :rtype: dict """
        results = {}
        allItems = getTopItems(self.twPrompt)
        for n, item in enumerate(allItems):
            results['result_%s' % (n+1)] = str(item._widget.text())
        return results

#============================================ QStyle =============================================#

class Style(object):

    _styleDir = os.path.join(qt.toolPath, '_lib', 'style')
    _qssDarkOrange = os.path.join(_styleDir, 'darkOrange.qss')
    _qssDarkGrey = os.path.join(_styleDir, 'darkGrey.qss')
    _qssRedGrey = os.path.join(_styleDir, 'redGrey.qss')

    def __init__(self):
        pass

    def applyStyle(self, styleName='darkOrange'):
        """ Apply given styleSheet
            :param styleName: ['darkOrange', 'darkGrey']
            :type styleName: str
            :return: Style sheet
            :rtype: str """
        styleList = ['darkOrange', 'darkGrey', 'redGrey']
        if not styleName in styleList:
            raise KeyError, "Error: StyleName not found: %s. Should be in %s" % (styleName, styleList)
        else:
            qssFile = "_qss%s%s" % (styleName[0].upper(), styleName[1:])
            return ''.join(pFile.readFile(getattr(self, qssFile)))

    @staticmethod
    def _hexToRgb(value):
        """ Convert hex color value to rgb value
            :param value: Hex color value
            :type value: str
            :return: Rgb color
            :rtype: tuple """
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

    @staticmethod
    def _rgbToHex(rgb):
        """ Convert rgb value to hex color value
            :param rgb: Rgb color
            :type rgb: tuple
            :return: Hex color value
            :rtype: str """
        return '%02x%02x%02x' % rgb
