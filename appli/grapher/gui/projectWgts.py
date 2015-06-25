import os
from PyQt4 import QtGui
from appli.grapher.gui.ui import wgProjectLoadUI


class LoadProject(QtGui.QDialog, wgProjectLoadUI.Ui_wgLoadProject):
    """
    Load project dialog
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.projectRootPath = os.path.join(self.mainUi.rootPath, 'project')
        super(LoadProject, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """
        Setup dialog ui
        """
        self.setupUi(self)
        self.cbNewProject.clicked.connect(self.rf_newProjectVisibility)
        self.pbCreate.clicked.connect(self.on_create)
        self.pbCancel.clicked.connect(self.close)
        self.rf_newProjectVisibility()

    def rf_newProjectVisibility(self):
        """
        Refresh new project widget visibility
        """
        self.qfNewProject.setVisible(self.cbNewProject.isChecked())

    def on_create(self):
        """
        Command launched when 'Create' QPushButton is clicked
        Will create new project
        """
        pName = str(self.leProjectName.text())
        pAlias = str(self.leProjectAlias.text())
        pFolder = "%s--%s" % (pAlias, pName)
        pPath = os.path.join(self.projectRootPath, pFolder)
        if os.path.exists(pPath):
            raise IOError, "!!! Project %s already exists !!!"
        try:
            self.log.info("Creating new project: %s" % pFolder)
            os.mkdir(pPath)
            self.log.info("---> Project %s successfully created." % pFolder)
            self.close()
        except:
            raise IOError, "Can not create project %s" % pFolder

