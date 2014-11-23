import sys
from PyQt4 import QtGui
from lib.env import studio
from lib.qt import procQt as pQt
from appli.grapher.ui import grapherUI
from lib.system import procFile as pFile
from appli.grapher import grapher, gpWidget, graphTree


class GrapherUi(QtGui.QMainWindow, grapherUI.Ui_mwGrapher, pQt.Style):

    def __init__(self, logLvl='info'):
        self.log = pFile.Logger(title="Grapher-UI", level=logLvl)
        self.log.info("#-- Launching Grapher Ui --#")
        self.gp = grapher.Grapher(logLvl=logLvl)
        super(GrapherUi, self).__init__()
        self._setupUi()
        self._initUi()

    def _setupUi(self):
        """ Setup main ui """
        self.log.debug("#-- Setup Grapher Ui --#")
        self.setupUi(self)
        self.setStyleSheet(self.applyStyle(styleName='darkOrange'))
        self.wgComment = gpWidget.Comment(self)
        self.vlComment.addWidget(self.wgComment)
        self.wgVariables = gpWidget.Variables(self)
        self.vlVariables.addWidget(self.wgVariables)
        self.wgGraph = graphTree.GraphTree(self)
        self.vlGraph.addWidget(self.wgGraph)
        self._menuFile()
        self._menuGraph()

    def _initUi(self):
        """ Init main ui """
        self.log.debug("#-- Init Grapher Ui --#")
        self.setWindowTitle("Grapher: Untitled")
        self.wgComment.rf_widgetVis()
        self.wgComment.rf_menuVis()
        self.wgVariables.rf_widgetVis()

    def _updateUi(self):
        """ Update Ui """
        self.log.debug("#-- Update Grapher Ui --#")
        self.setWindowTitle("Grapher: %s" % self.gp.graphFile)
        self.wgComment.rf_comment(self.gp.gpComment['html'])

    # noinspection PyUnresolvedReferences
    def _menuFile(self):
        """ Init menu File """
        self.miLoad.triggered.connect(self.on_loadGraph)
        self.miLoad.setShortcut("Ctrl+O")
        self.miSave.triggered.connect(self.on_saveGraph)
        self.miSave.setShortcut("Ctrl+S")
        self.miSaveAs.triggered.connect(self.on_saveGraphAs)
        self.miSaveAs.setShortcut("Ctrl+Shift+S")

    # noinspection PyUnresolvedReferences
    def _menuGraph(self):
        """ Init menu Graph """
        self.miNewNode.triggered.connect(self.wgGraph.on_newNode)
        self.miNewNode.setShortcut("N")
        self.miRenameNode.setShortcut("F2")
        self.miDeleteNode.setShortcut("Del")

    def on_loadGraph(self):
        """ Command launched when miLoad is clicked """
        self.log.debug("#-- Load Graph --#")
        if self.gp.filePath is None or self.gp.fileName is None:
            rootDir = studio.prodPath
        else:
            rootDir = self.gp.filePath
        self.fdOpen = pQt.fileDialog(fdMode='open', fdFileMode='ExistingFile', fdRoot=rootDir,
                                     fdFilters=['gp_*.py'], fdCmd=self.loadGraph)
        self.fdOpen.exec_()

    def on_saveGraph(self):
        """ Command launched when miSave is clicked """
        self.log.debug("#-- Save Graph --#")
        if not self.gp.lock:
            if self.gp.graphFile is None:
                self.on_saveGraphAs()
            else:
                result, log = self.gp.writeGraphFile(graphFile=None, force=True)
                if not result:
                    self._errorDialog(log, self)
                else:
                    self.log.info(log)
        else:
            self._errorDialog("!!! Warning: Destination Graph Locked !!!\nCan't overwrite locked graph", self)

    def on_saveGraphAs(self):
        """ Command launched when miSaveAs is clicked """
        if self.gp.filePath is None or self.gp.fileName is None:
            rootDir = studio.prodPath
        else:
            rootDir = self.gp.filePath
        self.fdSaveAs = pQt.fileDialog(fdMode='save', fdFileMode='AnyFile', fdRoot=rootDir,
                                       fdFilters=['gp_*.py'], fdCmd=self.saveGraphAs)
        self.fdSaveAs.exec_()

    def loadGraph(self, graphFile=None):
        """ Open selected graph
            :param graphFile: (str) : Graph absolut path """
        #-- Get Graph Path --#
        if graphFile is None:
            selPath = self.fdOpen.selectedFiles()
            self.fdOpen.close()
        else:
            selPath = [graphFile]
        #-- Open Graph --#
        if selPath:
            result, log = self.gp.loadGraphFile(str(selPath[0]))
            if not result:
                self._errorDialog(log, self)
            else:
                self.log.info(log)
                if not self.gp.lock:
                    self.gp._createLockFile(self.gp.lockFile)
                    self.gp.lock = False
                    self._updateUi()
                else:
                    lockParams = pFile.readPyFile(self.gp.lockFile)
                    mess = ["!!! WARNING !!!",
                            "Graph %s is already open:" % self.gp.graphFile,
                            "Locked by %s on %s" % (lockParams['user'], lockParams['station']),
                            "Date: %s" % lockParams['date'], "Time: %s" % lockParams['time']]
                    self.lockDialog = pQt.ConfirmDialog('\n'.join(mess), ["Read Only", "Break Lock"],
                                                        [self.openReadOnly, self.breakLock])
                    self.lockDialog.exec_()

    def openReadOnly(self):
        """ Load graphFile in read only """
        self.lockDialog.close()
        self.gp.lock = True
        self.setStyleSheet(self.applyStyle(styleName='redGrey'))
        self._updateUi()

    def breakLock(self):
        """ Break lockFile and load graphFile """
        self.lockDialog.close()
        self.gp._removeLockFile(self.gp.lockFile)
        self.gp.lock = False
        self.gp._createLockFile(self.gp.lockFile)
        self.setStyleSheet(self.applyStyle(styleName='darkOrange'))
        self._updateUi()

    def saveGraphAs(self):
        """ Save graph as selected fileName """
        self.log.debug("#-- Save Graph As --#")
        selPath = self.fdSaveAs.selectedFiles()
        if selPath:
            graphFile = str(selPath[0])
            result, log = self.gp.writeGraphFile(graphFile=graphFile, force=True)
            if not result:
                self._errorDialog(log, self)
            else:
                self.log.info(log)
                self.fdSaveAs.close()

    @staticmethod
    def _errorDialog(message, parent):
        """ Launch default error dialog
            :param message: (str or list): Message to print
            :param parent: (object) : Parent ui """
        errorDial = QtGui.QErrorMessage(parent)
        if isinstance(message, list):
            errorDial.showMessage('\n'.join(message))
        else:
            errorDial.showMessage(message)



def launch(logLvl='info'):
    """ Grapher launcher
        :param logLvl: (str) : Log level ('critical', 'error', 'warning', 'info', 'debug') """
    app = QtGui.QApplication(sys.argv)
    window = GrapherUi(logLvl=logLvl)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch(logLvl='debug')