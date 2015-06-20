from appli.grapher.gui.graphWgts import GraphNode


class AssetNode(GraphNode):

    def __init__(self, **kwargs):
        self.iconFile = "gui/icon/assetNode.svg"
        self.nodeType = "assetNode"
        self.hasInputFileConnection = False
        self.hasInputDataConnection = False
        self.hasOutputFileConnection = True
        super(AssetNode, self).__init__(**kwargs)


class MayaNode(GraphNode):

    def __init__(self, **kwargs):
        self.iconFile = "gui/icon/mayaNode.svg"
        self.nodeType = "mayaNode"
        self.hasInputFileConnection = True
        self.hasInputDataConnection = True
        self.hasOutputFileConnection = True
        super(MayaNode, self).__init__(**kwargs)


class SvgNode(GraphNode):

    def __init__(self, **kwargs):
        self.iconFile = "gui/icon/baseNode.svg"
        self.nodeType = "svgNode"
        self.hasInputFileConnection = True
        self.hasInputDataConnection = False
        self.hasOutputFileConnection = True
        super(SvgNode, self).__init__(**kwargs)
