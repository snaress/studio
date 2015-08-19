import pprint


class Node(object):

    def __init__(self, nodeName=None):
        self.nodeName = nodeName
        self.nodeVersion  = 0
        self.nodeVersions = {0: "Default Version"}

    def __repr__(self):
        """
        GraphNode representation as dict
        :return: Node contents
        :rtype: dict
        """
        nodeDict = dict()
        for k, v in sorted(self.__dict__.iteritems()):
            if k.startswith('node'):
                nodeDict[k] = v
        return nodeDict

    def __str__(self):
        """
        GraphNode representation as string
        :return: Node contents
        :rtype: str
        """
        return pprint.pformat(self.__repr__())

    def listAttrs(self):
        """
        List all attributes
        :return: Attributes
        :rtype: list
        """
        attrs = []
        for attr in self.__repr__().keys():
            attrs.append(attr)
        return sorted(attrs)


class Modul(Node):

    def __init__(self, nodeName=None):
        super(Modul, self).__init__(nodeName)
        self.nodeType = 'modul'
        self._nodeColor = (200, 200, 200, 255)
        self._nodeIcon = "%s.svg" % self.nodeType


class SysData(Node):

    def __init__(self, nodeName=None):
        super(SysData, self).__init__(nodeName)
        self.nodeType = 'sysData'
        self._nodeColor = (100, 255, 255, 255)
        self._nodeIcon = "%s.svg" % self.nodeType
        self.nodeScript = ""


class CmdData(Node):

    def __init__(self, nodeName=None):
        super(CmdData, self).__init__(nodeName)
        self.nodeType = 'cmdData'
        self._nodeColor = (60, 135, 255, 255)
        self._nodeIcon = "%s.svg" % self.nodeType
        self.nodeScript = ""


class PyData(Node):

    def __init__(self, nodeName=None):
        super(PyData, self).__init__(nodeName)
        self.nodeType = 'pyData'
        self._nodeColor = (0, 125, 0, 255)
        self._nodeIcon = "%s.svg" % self.nodeType
        self.nodeScript = ""



if __name__ == '__main__':

    tt = PyData('test')
    print tt.__repr__()
    print tt.listAttrs()