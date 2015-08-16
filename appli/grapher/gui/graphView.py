from PyQt4 import QtGui, QtSvg, QtCore


class GraphView(QtGui.QGraphicsView):
    """
    GraphView widget, child of Fondation
    :param _mainUi: Fondation main window
    :type _mainUi: QtGui.QMainWindow
    :param graphScene: Graph scene
    :type graphScene: QtGui.QGraphicsScene
    """

    def __init__(self, _mainUi, graphScene):
        super(GraphView, self).__init__()
        self._mainUi = _mainUi
        self.log = self._mainUi.log
        self.log.debug("\t Init GraphView Widget.")
        self.setScene(graphScene)
        self._setupWidget()

    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphView Widget.")
        self.setSceneRect(0, 0, 10000, 10000)
        self.scale(0.5, 0.5)
        self.setRubberBandSelectionMode(QtCore.Qt.IntersectsItemShape)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(35, 35, 35, 255), QtCore.Qt.SolidPattern))
        self.setVisible(False)

    # noinspection PyArgumentList,PyCallByClass,PyTypeChecker
    def mouseMoveEvent(self, event):
        """
        Add mouse move options: 'Left': If ctrlKey is True, enable scene drag movement
        """
        if event.y() < 0 or event.y() > self.height() or event.x() < 0 or event.x() > self.width():
            globalPos = self.mapToGlobal(event.pos())
            if event.y() < 0 or event.y() > self.height():
                if event.y() < 0:
                    globalPos.setY(globalPos.y() + self.height())
                else:
                    globalPos.setY(globalPos.y() - self.height())
            else:
                if event.x() < 0:
                    globalPos.setX(globalPos.x() + self.width())
                else:
                    globalPos.setX(globalPos.x() - self.width())
            r_event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonRelease, self.mapFromGlobal(QtGui.QCursor.pos()),
                                        QtCore.Qt.LeftButton, QtCore.Qt.NoButton, QtCore.Qt.NoModifier)
            self.mouseReleaseEvent(r_event)
            QtGui.QCursor.setPos(globalPos)
            p_event = QtGui.QMouseEvent(QtCore.QEvent.MouseButtonPress, self.mapFromGlobal(QtGui.QCursor.pos()),
                                        QtCore.Qt.LeftButton, QtCore.Qt.LeftButton, QtCore.Qt.NoModifier)
            QtCore.QTimer.singleShot(0, lambda: self.mousePressEvent(p_event))
        else:
            super(GraphView, self).mouseMoveEvent(event)

    def wheelEvent(self, event):
        """
        Scale graph view (zoom fit)
        """
        factor = 1.41 ** ((event.delta()*.5) / 240.0)
        self.scale(factor, factor)

    def resizeEvent(self, event):
        """
        Resize graph view (widget size)
        """
        self.scene().setSceneRect(0, 0, self.width(), self.height())


class GraphScene(QtGui.QGraphicsScene):
    """
    GraphScene widget, child of Fondation.GraphView
    :param _mainUi: Grapher main window
    :type _mainUi: QtGui.QMainWindow
    """

    def __init__(self, _mainUi):
        super(GraphScene, self).__init__()
        self._mainUi = _mainUi
        self.log = self._mainUi.log
        self.log.debug("\t Init GraphScene Widget.")
        self._setupWidget()

    def _setupWidget(self):
        self.log.debug("\t ---> Setup GraphScene Widget.")
        self.buffer = None
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
            self._mainUi.graphView.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        elif item is None and self.ctrlKey:
            self._mainUi.graphView.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
        super(GraphScene, self).mousePressEvent(event)
