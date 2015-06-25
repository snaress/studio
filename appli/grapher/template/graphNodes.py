from appli.grapher.gui.graphWgts import GraphNode


class AssetNode(GraphNode):
    """
    GraphNode template
    :param kwargs: Graph node dict (mainUi, nodeName, nodeLabel)
    :type kwargs: dict
    """

    def __init__(self, **kwargs):
        self.iconFile = "gui/icon/svg/assetNode.svg"
        self.nodeType = "assetNode"
        self.hasInputFilePlug = False
        self.hasInputDataPlug = False
        self.hasOutputFilePlug = True
        super(AssetNode, self).__init__(**kwargs)


class MayaNode(GraphNode):
    """
    GraphNode template
    :param kwargs: Graph node dict (mainUi, nodeName, nodeLabel)
    :type kwargs: dict
    """

    def __init__(self, **kwargs):
        self.iconFile = "gui/icon/svg/mayaNode.svg"
        self.nodeType = "mayaNode"
        self.hasInputFilePlug = True
        self.hasInputDataPlug = True
        self.hasOutputFilePlug = True
        super(MayaNode, self).__init__(**kwargs)


class SvgNode(GraphNode):
    """
    GraphNode template
    :param kwargs: Graph node dict (mainUi, nodeName, nodeLabel)
    :type kwargs: dict
"""

    def __init__(self, **kwargs):
        self.iconFile = "gui/icon/svg/baseNode.svg"
        self.nodeType = "svgNode"
        self.hasInputFilePlug = True
        self.hasInputDataPlug = False
        self.hasOutputFilePlug = True
        super(SvgNode, self).__init__(**kwargs)
