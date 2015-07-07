from appli.grapher.gui.graphWgts import GraphNode
from appli.grapher.gui import dataWgts


class AssetCastingNode(GraphNode):
    """
    GraphNode template
    :param kwargs: Graph node dict (mainUi, nodeName, nodeLabel)
    :type kwargs: dict
    """

    def __init__(self, **kwargs):
        self.iconFile = "gui/icon/svg/assetCastingNode.svg"
        self.nodeType = "assetCastingNode"
        self.hasInputFilePlug = False
        self.hasInputDataPlug = False
        self.hasOutputFilePlug = True
        super(AssetCastingNode, self).__init__(**kwargs)

    def dataWidgets(self):
        """
        Node specific data widgets
        :return: Node widget dicts
        :rtype: list
        """
        return [{'name': 'Node Id', 'class': dataWgts.DataNodeId(self.mainUi)},
                {'name': 'Node Connections', 'class': dataWgts.DataNodeConnections(self.mainUi)},
                {'name': 'Asset Casting', 'class': dataWgts.DataNodeAssetCasting(self.mainUi)}]

    @property
    def dataKeys(self):
        """
        Asset casting node data keys
        :return: data keys
        :rtype: list
        """
        return ['assetEntity', 'assetType', 'assetSpec', 'assetName', 'assetNs']


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

    def dataWidgets(self):
        """
        Node specific data widgets
        :return: Node widget dicts
        :rtype: list
        """
        return [{'name': 'Node Id', 'class': dataWgts.DataNodeId(self.mainUi)},
                {'name': 'Node Connections', 'class': dataWgts.DataNodeConnections(self.mainUi)}]

    @property
    def dataKeys(self):
        """
        Asset casting node data keys
        :return: data keys
        :rtype: list
        """
        return []


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

    def dataWidgets(self):
        """
        Node specific data widgets
        :return: Node widget dicts
        :rtype: list
        """
        return [{'name': 'Node Id', 'class': dataWgts.DataNodeId(self.mainUi)},
                {'name': 'Node Connections', 'class': dataWgts.DataNodeConnections(self.mainUi)}]

    @property
    def dataKeys(self):
        """
        Asset casting node data keys
        :return: data keys
        :rtype: list
        """
        return []


class DataNode(GraphNode):
    """
    GraphNode template
    :param kwargs: Graph node dict (mainUi, nodeName, nodeLabel)
    :type kwargs: dict
    """

    def __init__(self, **kwargs):
        self.iconFile = "gui/icon/svg/dataNode.svg"
        self.nodeType = "dataNode"
        self.hasInputFilePlug = False
        self.hasInputDataPlug = False
        self.hasOutputFilePlug = True
        super(DataNode, self).__init__(**kwargs)
        self.externFile = None

    def dataWidgets(self):
        """
        Node specific data widgets
        :return: Node widget dicts
        :rtype: list
        """
        return [{'name': 'Node Id', 'class': dataWgts.DataNodeId(self.mainUi)},
                {'name': 'Node Connections', 'class': dataWgts.DataNodeConnections(self.mainUi)},
                {'name': 'Node Script', 'class': dataWgts.DataNodeScript(self.mainUi)}]

    @property
    def dataKeys(self):
        """
        Asset casting node data keys
        :return: data keys
        :rtype: list
        """
        return ['scriptTxt']
