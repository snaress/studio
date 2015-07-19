import os
from appli.grapher.gui.graphWgts import GraphNode
from appli.grapher.gui import dataWgts


class AssetCastingNode(GraphNode):
    """
    GraphNode template
    :param kwargs: Graph node dict (mainUi, nodeName, nodeId)
    :type kwargs: dict
    """

    def __init__(self, **kwargs):
        self.iconFile = "gui/icon/svg/assetCastingNode.svg"
        self.nodeType = "assetCastingNode"
        self.hasInputFilePlug = False
        self.hasInputDataPlug = False
        self.hasOutputFilePlug = True
        self.hasLaunchCmd = False
        self.hasExecCmd = False
        super(AssetCastingNode, self).__init__(**kwargs)

    def dataWidgets(self):
        """
        Node specific data widgets
        :return: Node widget dicts
        :rtype: list
        """
        return [{'name': 'Node Id', 'class': dataWgts.DataNodeId(self.mainUi)},
                {'name': 'Node Output File', 'class': dataWgts.DataOutputFilePlug(self.mainUi)},
                {'name': 'Asset Casting', 'class': dataWgts.DataNodeAssetCasting(self.mainUi)}]

    @property
    def dataKeys(self):
        """
        Asset casting node data keys
        :return: data keys
        :rtype: list
        """
        return ['assetEntity', 'assetType', 'assetSpec', 'assetName', 'assetNs']

    @property
    def relativePath(self):
        return os.path.join(self.assetEntity, self.assetType, self.assetSpec, self.assetName)


class AssetNode(GraphNode):
    """
    GraphNode template
    :param kwargs: Graph node dict (mainUi, nodeName, nodeId)
    :type kwargs: dict
    """

    def __init__(self, **kwargs):
        self.iconFile = "gui/icon/svg/assetNode.svg"
        self.nodeType = "assetNode"
        self.hasInputFilePlug = False
        self.hasInputDataPlug = False
        self.hasOutputFilePlug = True
        self.hasLaunchCmd = False
        self.hasExecCmd = False
        super(AssetNode, self).__init__(**kwargs)

    def dataWidgets(self):
        """
        Node specific data widgets
        :return: Node widget dicts
        :rtype: list
        """
        return [{'name': 'Node Id', 'class': dataWgts.DataNodeId(self.mainUi)},
                {'name': 'Node Output File', 'class': dataWgts.DataOutputFilePlug(self.mainUi)},
                {'name': 'Node File', 'class': dataWgts.DataNodeFile(self.mainUi)},]

    @property
    def dataKeys(self):
        """
        Asset casting node data keys
        :return: data keys
        :rtype: list
        """
        return ['nodeFile']


class MayaNode(GraphNode):
    """
    GraphNode template
    :param kwargs: Graph node dict (mainUi, nodeName, nodeId)
    :type kwargs: dict
    """

    def __init__(self, **kwargs):
        self.iconFile = "gui/icon/svg/mayaNode.svg"
        self.nodeType = "mayaNode"
        self.hasInputFilePlug = True
        self.hasInputDataPlug = True
        self.hasOutputFilePlug = True
        self.hasLaunchCmd = True
        self.app = self.nodeType.replace('Node', '')
        self.hasExecCmd = True
        super(MayaNode, self).__init__(**kwargs)

    def dataWidgets(self):
        """
        Node specific data widgets
        :return: Node widget dicts
        :rtype: list
        """
        return [{'name': 'Node Id', 'class': dataWgts.DataNodeId(self.mainUi)},
                {'name': 'Node Input File', 'class': dataWgts.DataInputFilePlug(self.mainUi)},
                {'name': 'Node Input Data', 'class': dataWgts.DataInputDataPlug(self.mainUi)},
                {'name': 'Node Output File', 'class': dataWgts.DataOutputFilePlug(self.mainUi)},
                {'name': 'Node File', 'class': dataWgts.DataNodeFile(self.mainUi)}]

    @property
    def dataKeys(self):
        """
        Asset casting node data keys
        :return: data keys
        :rtype: list
        """
        return ['fileRootPath', 'fileRelPath', 'fileName', 'nodeFile']

    # def launchCmd(self):
    #     os.system()

    def execCmd(self):
        print "toto"


class DataNode(GraphNode):
    """
    GraphNode template
    :param kwargs: Graph node dict (mainUi, nodeName, nodeId)
    :type kwargs: dict
    """

    def __init__(self, **kwargs):
        self.iconFile = "gui/icon/svg/dataNode.svg"
        self.nodeType = "dataNode"
        self.hasInputFilePlug = False
        self.hasInputDataPlug = False
        self.hasOutputFilePlug = True
        self.hasLaunchCmd = False
        self.hasExecCmd = False
        super(DataNode, self).__init__(**kwargs)
        self.externFile = None

    def dataWidgets(self):
        """
        Node specific data widgets
        :return: Node widget dicts
        :rtype: list
        """
        return [{'name': 'Node Id', 'class': dataWgts.DataNodeId(self.mainUi)},
                {'name': 'Node Output File', 'class': dataWgts.DataOutputFilePlug(self.mainUi)},
                {'name': 'Node Script', 'class': dataWgts.DataNodeScript(self.mainUi)}]

    @property
    def dataKeys(self):
        """
        Asset casting node data keys
        :return: data keys
        :rtype: list
        """
        return ['scriptTxt']
