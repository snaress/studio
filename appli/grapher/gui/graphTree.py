from PyQt4 import QtGui


class GraphTree(QtGui.QTreeWidget):
    """
    GraphTree widget, child of GrapherUi.GraphZone
    :param mainUi: Grapher mainUi class
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi, graphZone):
        super(GraphTree, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphTree Widget.")
        self.graphZone = graphZone
        self._setupWidget()

    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphTree Widget.")
        self.setStyleSheet("background-color: rgb(35, 35, 35)")
        self.setSelectionMode(QtGui.QTreeWidget.ExtendedSelection)
        self.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.setExpandsOnDoubleClick(False)
        self.setHeaderHidden(True)
        self.setColumnCount(12)
        self.setIndentation(0)
        self.rf_graphColumns()

    def rf_graphColumns(self):
        """
        Refresh graphTree column size
        """
        for n in range(self.columnCount()):
            self.resizeColumnToContents(n)
