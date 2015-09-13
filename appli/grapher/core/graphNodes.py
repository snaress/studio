import pprint


class Node(object):
    """
    Node common datas contents.

    :param nodeName: Node Name
    :type nodeName: str
    """

    def __init__(self, nodeName=None):
        self.nodeName = nodeName
        self.nodeIsEnabled = True
        self.nodeIsActive = True
        self.nodeIsExpanded = False
        self.nodeVersion  = 0
        self.nodeVersions = {0: "Default Version"}

    def getDatas(self, asString=False):
        """
        get GraphNode datas as dict or string

        :param asString: Return string instead of dict
        :type asString: bool
        :return: Node contents
        :rtype: dict | str
        """
        nodeDict = dict()
        #-- Parse Datas --#
        for k, v in sorted(self.__dict__.iteritems()):
            if k.startswith('node'):
                nodeDict[k] = v
        #-- Return Datas --#
        if asString:
            return pprint.pformat(nodeDict)
        return nodeDict

    def listAttrs(self):
        """
        List all attributes

        :return: Attributes
        :rtype: list
        """
        attrs = []
        for attr in self.getDatas().keys():
            attrs.append(attr)
        return sorted(attrs)


class Modul(Node):
    """
    Modul datas contents.

    :param nodeName: Node Name
    :type nodeName: str
    """

    _nodeColor = (200, 200, 200, 255)
    _nodeIcon = 'modul.svg'

    def __init__(self, nodeName=None):
        super(Modul, self).__init__(nodeName)
        self.nodeType = 'modul'


class SysData(Node):
    """
    SysData datas contents.

    :param nodeName: Node Name
    :type nodeName: str
    """

    _nodeColor = (100, 255, 255, 255)
    _nodeIcon = 'sysData.svg'

    def __init__(self, nodeName=None):
        super(SysData, self).__init__(nodeName)
        self.nodeType = 'sysData'
        self.nodeScript = {0: ''}


class CmdData(Node):
    """
    CmdData datas contents.

    :param nodeName: Node Name
    :type nodeName: str
    """

    _nodeColor = (60, 135, 255, 255)
    _nodeIcon = 'cmdData.svg'

    def __init__(self, nodeName=None):
        super(CmdData, self).__init__(nodeName)
        self.nodeType = 'cmdData'
        self.nodeScript = {0: ''}


class PyData(Node):
    """
    PyData datas contents.

    :param nodeName: Node Name
    :type nodeName: str
    """

    _nodeColor = (0, 125, 0, 255)
    _nodeIcon = 'pyData.svg'

    def __init__(self, nodeName=None):
        super(PyData, self).__init__(nodeName)
        self.nodeType = 'pyData'
        self.nodeScript = {0: ''}
