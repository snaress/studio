from appli.grapher.gui import graphTree


class GraphZone(object):

    def __init__(self, mainUi):
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphZone Widget.")
        self.graphTree = graphTree.GraphTree(self.mainUi)
