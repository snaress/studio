import pprint



class Common(object):

    def __init__(self):
        self.nodeVersion  = 0
        self.nodeVersions = {0: "Default Version"}


class Modul(Common):

    def __init__(self):
        super(Modul, self).__init__()
        self._nodeColor = (200, 200, 200, 255)
        self._nodeIcon = "modul.svg"

    def __repr__(self):
        """
        GraphNode representation as dict
        :return: Node contents
        :rtype: dict
        """
        nodeDict = dict()
        for k, v in self.__dict__.iteritems():
            if k.startswith('node'):
                nodeDict[k] = v
        return nodeDict

    def __str__(self):
        """
        GraphNode representation as str
        :return: Node contents
        :rtype: str
        """
        return pprint.pformat(self.__repr__())


class SysData(Common):

    def __init__(self):
        super(SysData, self).__init__()
        self._nodeColor = (100, 255, 255, 255)
        self._nodeIcon = "sysData.svg"

    def __repr__(self):
        """
        GraphNode representation as dict
        :return: Node contents
        :rtype: dict
        """
        nodeDict = dict()
        for k, v in self.__dict__.iteritems():
            if k.startswith('node'):
                nodeDict[k] = v
        return nodeDict

    def __str__(self):
        """
        GraphNode representation as str
        :return: Node contents
        :rtype: str
        """
        return pprint.pformat(self.__repr__())


class CmdData(Common):

    def __init__(self):
        super(CmdData, self).__init__()
        self._nodeColor = (60, 135, 255, 255)
        self._nodeIcon = "cmdData.svg"

    def __repr__(self):
        """
        GraphNode representation as dict
        :return: Node contents
        :rtype: dict
        """
        nodeDict = dict()
        for k, v in self.__dict__.iteritems():
            if k.startswith('node'):
                nodeDict[k] = v
        return nodeDict

    def __str__(self):
        """
        GraphNode representation as str
        :return: Node contents
        :rtype: str
        """
        return pprint.pformat(self.__repr__())


class PyData(Common):

    def __init__(self):
        super(PyData, self).__init__()
        self._nodeColor = (0, 125, 0, 255)
        self._nodeIcon = "pyData.svg"

    def __repr__(self):
        """
        GraphNode representation as dict
        :return: Node contents
        :rtype: dict
        """
        nodeDict = dict()
        for k, v in self.__dict__.iteritems():
            if k.startswith('node'):
                nodeDict[k] = v
        return nodeDict

    def __str__(self):
        """
        GraphNode representation as str
        :return: Node contents
        :rtype: str
        """
        return pprint.pformat(self.__repr__())
