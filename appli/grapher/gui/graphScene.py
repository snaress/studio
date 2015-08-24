from PyQt4 import QtGui, QtCore


class GraphScene(QtGui.QGraphicsScene):
    """
    GraphScene widget, child of Grapher.GraphView
    :param mainUi: Grapher main window
    :type mainUi: QtGui.QMainWindow
    """

    def __init__(self, mainUi, graphZone):
        super(GraphScene, self).__init__()
        self.mainUi = mainUi
        self.log = self.mainUi.log
        self.log.debug("\t Init GraphScene Widget.")
        self.graphZone = graphZone
        self._setupWidget()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphScene Widget.")
        self.ctrlKey = False

    def keyPressEvent(self, event):
        """
        Add key press options: 'Control' = store State for move options
        """
        #-- Store State For Move Options --#
        if event.key() == QtCore.Qt.Key_Control:
            self.ctrlKey = True

    def keyReleaseEvent(self, event):
        """
        Add key release options: 'Control' = Clear state for move options
        """
        #-- Clear State For Move Options --#
        if event.key() == QtCore.Qt.Key_Control:
            self.ctrlKey = False

    def mousePressEvent(self, event):
        """
        Add mouse press options: 'Left' = - If empty and ctrlKey is False: Enable area selection
                                          - If empty and ctrlKey is True: Enable move by drag
        """
        item = self.itemAt(event.scenePos())
        #-- Enable Area Selection Or Moving Scene --#
        if item is None and not self.ctrlKey:
            self.graphZone.sceneView.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        elif item is None and self.ctrlKey:
            self.graphZone.sceneView.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
        super(GraphScene, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """
        Add mouse release options: 'left' = - Disable GraphView 'move by drag' mode.
        """
        self.graphZone.sceneView.setDragMode(QtGui.QGraphicsView.NoDrag)
        super(GraphScene, self).mouseReleaseEvent(event)
