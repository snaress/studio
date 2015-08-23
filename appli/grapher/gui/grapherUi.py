import sys
from appli import grapher
from functools import partial
from PyQt4 import QtGui, QtCore
from lib.system import procFile as pFile
from appli.grapher.gui.ui import grapherUI
from appli.grapher.core.grapher import Grapher
from appli.grapher.gui import graphZone, toolsWgts, nodeEditor


class GrapherUi(QtGui.QMainWindow, grapherUI.Ui_mwGrapher):

    def __init__(self, logLvl='info'):
        self.log = pFile.Logger(title="GrapherUi", level=logLvl)
        self.log.info("########## Launching Grapher Ui ##########")
        self.grapher = Grapher()
        self.iconPath = grapher.iconPath
        super(GrapherUi, self).__init__()
        self._setupUi()

    def _setupUi(self):
        self.log.info("#-- Setup Main Ui --#", newLinesBefor=1)
        self.setupUi(self)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self._initWidgets()
        self._initMenu()

    # noinspection PyUnresolvedReferences
    def _initWidgets(self):
        self.log.info("#-- Init Widgets --#", newLinesBefor=1)
        #-- GraphZone --#
        self.graphZone = graphZone.GraphZone(self)
        #-- GraphTools --#
        self.graphTools = toolsWgts.GraphTools(self)
        self.tbTools.addWidget(self.graphTools)
        self.tbTools.orientationChanged.connect(partial(self.on_miToolsOrientChanged, orient=False, force=False))
        #-- Node Editor --#
        self.nodeEditor = nodeEditor.NodeEditor(self)
        self.vlNodeEditor.insertWidget(0, self.nodeEditor)

    def _initMenu(self):
        self.log.info("#-- Init Menus --#", newLinesBefor=1)
        self._menuDisplay()
        self.on_miNodeEditor()

    # noinspection PyUnresolvedReferences
    def _menuDisplay(self):
        self.log.debug("\t ---> Menu Display ...")
        #-- Widgets Visibility --#
        self.miToolsVisibility.triggered.connect(self.on_miToolsVisibility)
        self.miToolsVisibility.setShortcut("T")
        self.miNodeEditor.triggered.connect(self.on_miNodeEditor)
        self.miNodeEditor.setShortcut("E")
        # self.miGraphView.triggered.connect(self.on_miGraphView)
        # self.miGraphView.setShortcut("Tab")
        #-- SubMenu 'Tools Bar Orient' --#
        self.miBarHorizontal.triggered.connect(partial(self.on_miToolsOrientChanged, orient='horizontal', force=True))
        self.miBarVertical.triggered.connect(partial(self.on_miToolsOrientChanged, orient='vertical', force=True))
        #-- SubMenu 'Tools Tab Orient' --#
        self.miTabNorth.triggered.connect(partial(self.on_miTabOrientChanged, 'North'))
        self.miTabSouth.triggered.connect(partial(self.on_miTabOrientChanged, 'South'))
        self.miTabWest.triggered.connect(partial(self.on_miTabOrientChanged, 'West'))
        self.miTabEast.triggered.connect(partial(self.on_miTabOrientChanged, 'East'))
        #-- Tools Options --#
        self.miToolsIconOnly.triggered.connect(self.on_miToolsIconOnly)
        self.miToolsIconOnly.setShortcut("Ctrl+T")

    @property
    def toolsIconOnly(self):
        """
        Get tools icon only state
        :return: Tools icon only state
        :rtype: bool
        """
        return self.miToolsIconOnly.isChecked()

    def on_miToolsOrientChanged(self, orient=False, force=False):
        """
        Orient toolsTab and their contents
        :param orient: 'horizontal' or 'vertical'
        :type orient: str
        :param force: Force orientation
        :type force: bool
        """
        self.log.detail(">>> Launch menuItem 'Tools Orient' ...")
        #-- Force Orient --#
        if force:
            if orient == 'horizontal':
                self.tbTools.setOrientation(QtCore.Qt.Horizontal)
            elif orient == 'vertical':
                self.tbTools.setOrientation(QtCore.Qt.Vertical)
        #-- Refresh ToolBar Display --#
        if self.tbTools.orientation() == 1:
            self.graphTools.tabOrientation('North')
            self.miToolsIconOnly.setChecked(True)
        else:
            self.graphTools.tabOrientation('West')
            self.miToolsIconOnly.setChecked(False)
        self.graphTools.toolsAspect()

    def on_miTabOrientChanged(self, orient):
        """
        Command launched when 'Tab Orient' QMenuItem is triggered
        Orient tab contents
        :param orient: 'North', 'South', 'West' or 'East'
        :type orient: str
        """
        self.log.detail(">>> Launch menuItem 'Tab Orient' ...")
        self.graphTools.tabOrientation(orient)

    def on_miToolsVisibility(self):
        """
        Command launched when 'Tools Visibility' QMenuItem is triggered
        Turn on or off tools bar visibility
        """
        self.log.detail(">>> Launch menuItem 'Tools Visibility' ...")
        self.tbTools.setVisible(self.miToolsVisibility.isChecked())

    def on_miNodeEditor(self):
        """
        Command launched when 'Node Editor' QMenuItem is triggered
        Show / Hide node editor
        """
        self.log.detail(">>> Launch menuItem 'Node Editor' ...")
        self.vfNodeEditor.setVisible(self.miNodeEditor.isChecked())

    def on_miToolsIconOnly(self):
        """
        Command launched when 'Tools Icon Only' QMenuItem is triggered
        Switch toolsTab aspect
        """
        self.log.detail(">>> Launch menuItem 'Tools Icon Only' ...")
        self.graphTools.toolsAspect()


def launch(logLvl='info'):
    """
    Grapher launcher
    :param logLvl: Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """
    app = QtGui.QApplication(sys.argv)
    window = GrapherUi(logLvl=logLvl)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    launch(logLvl='detail')