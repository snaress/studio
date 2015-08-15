from appli.fondation.gui.graphTree import GraphNode


class Modul(GraphNode):

    _nodeColor = (200, 200, 200, 255)

    def __init__(self, **kwargs):
        super(Modul, self).__init__(**kwargs)


class SysData(GraphNode):

    _nodeColor = (100, 255, 255, 255)

    def __init__(self, **kwargs):
        super(SysData, self).__init__(**kwargs)


class CmdData(GraphNode):

    _nodeColor = (60, 135, 255, 255)

    def __init__(self, **kwargs):
        super(CmdData, self).__init__(**kwargs)


class PyData(GraphNode):

    _nodeColor = (0, 125, 0, 255)

    def __init__(self, **kwargs):
        super(PyData, self).__init__(**kwargs)
