from PyQt4 import QtGui
from appli.grapher.template import toolsTab


class ToolsBar(QtGui.QTabWidget):
    """ Grapher tools tab
        :param mainUi: Grapher main window
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        super(ToolsBar, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.pWidget = self.mainUi.tbTools
        self.tabs = []
        self._setupUi()

    def _setupUi(self):
        """ Setup tools tab """
        self.log.debug("---> Setup Tools Bar ...")
        self.addTabs()
        self.tabOrientation('West')

    def tabOrientation(self, orient):
        """ Edit tools tab orientation
            :param orient: 'North', 'South', 'West', 'East'
            :type orient: str """
        if orient == 'North':
            self.setTabPosition(QtGui.QTabWidget.North)
        elif orient == 'South':
            self.setTabPosition(QtGui.QTabWidget.South)
        elif orient == 'West':
            self.setTabPosition(QtGui.QTabWidget.West)
        elif orient == 'East':
            self.setTabPosition(QtGui.QTabWidget.East)
        for tab in self.tabs:
            if orient in ['North', 'South']:
                tab.setOrientation('horizontal')
            elif orient in ['West', 'East']:
                tab.setOrientation('vertical')

    def addTabs(self):
        """ Add tools tab """
        self.clear()
        #-- Tab Mode --#
        tabMode = toolsTab.TabMode(mainUi=self.mainUi)
        self.insertTab(-1, tabMode, 'Mode')
        self.tabs.append(tabMode)
        #-- Tab Util --#
        tabUtil = toolsTab.TabUtil(mainUi=self.mainUi)
        self.insertTab(-1, tabUtil, 'Util')
        self.tabs.append(tabUtil)
