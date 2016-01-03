from PyQt4 import QtGui
from appli.foundation.gui.foundation._ui import wg_projectTreeUI


class ProjectTree(QtGui.QWidget, wg_projectTreeUI.Ui_wg_projectTree):

    def __init__(self, parent=None):
        self.log = parent.log
        super(ProjectTree, self).__init__(parent)
        self._setupWidget()

    def _setupWidget(self):
        """
        Setup widget ui
        """
        self.log.info("#----- Setup Project Tree -----#")
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
