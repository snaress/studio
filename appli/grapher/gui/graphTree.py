from PyQt4 import QtGui


class GraphTree(QtGui.QTreeWidget):

    def __init__(self, mainUi):
        super(GraphTree, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphTree Widget.")

