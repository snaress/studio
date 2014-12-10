from PyQt4 import QtGui
from lib.system import procFile as pFile
from tools.maya.util.proc import procUi as pUi
from tools.maya.camera.camPrez.ui import camPrezUI
from tools.maya.camera.camPrez import camPrezCmds as cpCmds
try:
    import maya.cmds as mc
except:
    pass


class CamPrez(QtGui.QMainWindow, camPrezUI.Ui_mwCamPrez):

    def __init__(self, parent=None):
        self.log = pFile.Logger(title="camPrez")
        self.log.info("#-- Launching CamPrez Ui --#")
        super(CamPrez, self).__init__(parent)
        self._setupUi()
        self.rf_ui()
        print 'launch 1'

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup main ui """
        self.setupUi(self)
        print 'connect'
        self.bCreateCamTurn.clicked.connect(self.on_createCamTurn)

    def rf_ui(self):
        print 'toto'

    def on_createCamTurn(self):
        """ Command launched when 'Create Camera Turn' is clicked """
        print 'launch 2'
        cpCmds.createCamTurn(self.getFrontAxe('turn'), self.getDuration('turn'))

    def getFrontAxe(self, mode):
        """ Get front axe from given mode
            :param mode: (str) : 'turn' or 'quadra'
            :return: (str) : Front axe """
        print self.tabWidget.currentIndex()
        if mode == 'turn':
            if self.cbTurnX.isChecked():
                if self.cbTurnInvert.isChecked():
                    return '-x'
                return 'x'
            elif self.cbTurnY.isChecked():
                if self.cbTurnInvert.isChecked():
                    return '-y'
                return 'y'
            elif self.cbTurnZ.isChecked():
                if self.cbTurnInvert.isChecked():
                    return '-z'
                return 'z'

    def getDuration(self, mode):
        """ Get duration from given mode
            :param mode: (str) : 'turn' or 'quadra'
            :return: (int) : Duration """
        if mode == 'turn':
            if self.cbInvertRotate.isChecked():
                return int(self.sbTurnDuration.value())*-1
            return int(self.sbTurnDuration.value())


def launch():
    """ Launch CamPrez
        :return: (object) : Launched window """
    toolName = 'mwCamPrez'
    if mc.window(toolName, q=True, ex=True):
        print "Delete CamPrez Window"
        mc.deleteUI(toolName, wnd=True)
    global window
    window = CamPrez(parent=pUi.getMayaMainWindow())
    window.show()
    return window
