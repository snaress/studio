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
        self.nodeVersion = 0
        self.nodeVersions = {0: "Default Version"}
        self.nodeComments = {0: ""}
        self.nodeVariables = {0: dict()}
        self.nodeTrash = {0: ""}

    def getDatas(self, asString=False):
        """
        Get GraphNode datas as dict or string

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

    def setDatas(self, **kwargs):
        """
        Set GraphNode datas

        :param kwargs: Node datas
        :type kwargs: dict
        """
        for k, v in kwargs.iteritems():
            if not k in ['nodeName', 'nodeType']:
                if hasattr(self, k):
                    setattr(self, k, v)

    def setVersionnedDatas(self, **kwargs):
        """
        Set GraphNode versionned datas

        :param kwargs: Datas (node.attrName: node.attrValue)
        :type kwargs: dict
        """
        for k, v in kwargs.iteritems():
            if hasattr(self, k):
                val = getattr(self, k)
                val[self.nodeVersion] = v
                setattr(self, k, val)

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

    def addVersion(self):
        """
        Add new node version

        :return: New version
        :rtype: int
        """
        curIndex = self.nodeVersion
        newIndex = int(sorted(self.nodeVersions.keys())[-1] + 1)
        self.nodeVersions[newIndex] = "New version"
        self.nodeComments[newIndex] = self.nodeComments[curIndex]
        self.nodeVariables[newIndex] = self.nodeVariables[curIndex]
        self.nodeTrash[newIndex] = self.nodeTrash[curIndex]
        if hasattr(self, 'nodeScript'):
            self.nodeScript[newIndex] = self.nodeScript[curIndex]
        self.nodeVersion = newIndex
        return self.nodeVersion

    def delVersion(self):
        """
        Delete current node version

        :return: Current version
        :rtype: int
        """
        curIndex = self.nodeVersion
        if not len(self.nodeVersions.keys()) == 1:
            #-- Get new Index --#
            if curIndex == sorted(self.nodeVersions.keys())[0]:
                newIndex = sorted(self.nodeVersions.keys())[1]
            else:
                n = sorted(self.nodeVersions.keys()).index(curIndex)
                newIndex = sorted(self.nodeVersions.keys())[n-1]
            self.nodeVersion = newIndex
            #-- Delete Version --#
            self.nodeVersions.pop(curIndex)
            self.nodeComments.pop(curIndex)
            self.nodeVariables.pop(curIndex)
            self.nodeTrash.pop(curIndex)
            if hasattr(self, 'nodeScript'):
                self.nodeScript.pop(curIndex)
            return newIndex


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
