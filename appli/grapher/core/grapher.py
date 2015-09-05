"""
Usage:

Init Grapher:
-------------
gp = Grapher(logLvl='debug')

Create Node:
------------
newItem = gp.tree.createItem(nodeType='modul', nodeName='myNodeName_1', nodeParent='nodeParentName_#')

Get Node:
---------
myItem = gp.tree.getItemFromNodeName('myNodeName_1')

Parent Node:
------------
myItem.setParent(GraphItem)

delete Node:
------------
myItem.delete()

Get Tree Datas:
---------------
treeDict = gp.tree.getDatas()
print gp.tree.getDatas(asString=True)

get Node Datas:
---------------
nodeDict = myNodeName_1.getDatas()
print myNodeName_1.getDatas(asString=True)
"""


import os, pprint
from lib.system import procFile as pFile
from appli.grapher.core import graphNodes


class Grapher(object):
    """
    Grapher core

    :param logLvl: Verbose ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """

    _isReadOnly = False
    _graphFile = None

    def __init__(self, logLvl='info'):
        self.log = pFile.Logger(title="Grapher", level=logLvl)
        self.log.info("#-- Init Grapher Core --#", newLinesBefor=1)
        self.tree = GraphTree(self)

    @property
    def graphPath(self):
        """
        Get Grapher root path

        :return: Grapher root path
        :rtype: str
        """
        return os.path.dirname(self._graphFile)

    @property
    def GraphName(self):
        """
        Get Grapher name

        :return: Grapher name (graphFile without extension)
        :rtype: str
        """
        return self.graphFile.split('.')[0]

    @property
    def graphFile(self):
        """
        Get Grapher file name

        :return: Grapher file name (with extension)
        :rtype: str
        """
        return os.path.basename(self._graphFile)

    @graphFile.setter
    def graphFile(self, gpFile):
        """
        Set graphFile with given value

        :param gpFile: Grapher file full path
        :type gpFile: str
        """
        if not os.path.exists(gpFile):
            raise IOError ('!!! Graph file not found !!!')
        if not gpFile.endswith('.gp.py'):
            raise IOError ('!!! Wrong Extension, should be ".gp.py"')
        self._graphFile = gpFile

    def conformNewNodeName(self, nodeName):
        """
        Check new nodeName and return a unique name

        :param nodeName: New nodeName
        :type nodeName: str
        :return: New valide node name
        :rtype: str
        """
        rejected = [' ', '-', ',', ';', ':', '.', '/', '!', '?',
                    '*', '$', '=', '+', '\'', '\\', '"', '&']
        #-- Check Rejected --#
        for r in rejected:
            if r in nodeName:
                nodeName.replace(r, '')
        #-- Check CamelCase --#
        if '_' in nodeName:
            if not nodeName.split('_')[-1].isdigit():
                nodeName.replace('_', '')
        #-- Check Index --#
        if not '_' in nodeName:
            nodeName = '%s_1' % nodeName
        #-- Find Same Base Name --#
        founds = []
        for _nodeName in self.tree.allItems(asString=True):
            if nodeName == _nodeName:
                if not _nodeName in founds:
                    founds.append(_nodeName)
            elif _nodeName.startswith(nodeName.split('_')[0]):
                if not _nodeName in founds:
                    founds.append(_nodeName)
        #-- Result: Name Is Unique --#
        if not founds or not nodeName in founds:
            return nodeName
        #-- Result: Generate Unique Name --#
        iList = []
        for f in founds:
            iList.append(int(f.split('_')[-1]))
        return '%s_%s' % (nodeName.split('_')[0], (max(iList) + 1))


class GraphTree(object):
    """
    Grapher tree, child of Grapher

    :param grapher: Grapher core
    :type grapher: Grapher
    """

    def __init__(self, grapher=None):
        self.gp = grapher
        self.log = self.gp.log
        self.log.info("#-- Init Graph Tree --#", newLinesBefor=1)
        self._topItems = []

    def getDatas(self, asString=False):
        """
        GraphTree datas as dict or string

        :param asString: Return string instead of dict
        :type asString: bool
        :return: Tree contents
        :rtype: dict | str
        """
        treeDict = dict()
        #-- Parse Datas --#
        for n, item in enumerate(self.allItems()):
            treeDict[n] = item.getDatas()
        #-- Return Datas --#
        if asString:
            return pprint.pformat(treeDict)
        return treeDict

    def topItems(self, asString=False):
        """
        Get tree top items

        :param asString: Return list of strings instead of objects
        :type asString: bool
        :return: Tree top nodes
        :rtype: list
        """
        #-- Return String List --#
        if asString:
            topItems = []
            for item in self._topItems:
                topItems.append(item._node.nodeName)
            return topItems
        #-- Return Object List --#
        return self._topItems

    def allItems(self, asString=False):
        """
        Get tree all items

        :param asString: Return list of strings instead of objects
        :type asString: bool
        :return: Tree top nodes
        :rtype: list
        """
        items = []
        #-- Get Items --#
        for topItem in self.topItems():
            items.append(topItem)
            items.extend(topItem.allChildren())
        #-- Return String List --#
        if asString:
            allItems = []
            for item in items:
                allItems.append(item._node.nodeName)
            return allItems
        #-- Return Object List --#
        return items

    def getItemFromNodeName(self, nodeName):
        """
        Get item from given node name

        :param nodeName: Node name
        :type nodeName: str
        :return: Tree item
        :rtype: GraphItem
        """
        for item in self.allItems():
            if item._node.nodeName == nodeName:
                return item

    def createItem(self, nodeType='modul', nodeName=None, nodeParent=None):
        """
        Create and add new tree item

        :param nodeType: 'modul', 'sysData', 'cmdData', 'pyData'
        :type nodeType: str
        :param nodeName: New node name
        :type nodeName: str
        :param nodeParent: New node parent
        :type nodeParent: str | Modul | SysData | CmdData | PyData
        :return: New tree item
        :rtype: Modul | SysData | CmdData | PyData
        """
        if nodeName is None:
            nodeName = '%s_1' % nodeType
        newNodeName = self.gp.conformNewNodeName(nodeName)
        newItem = self._addItem(self._newItem(nodeType, newNodeName), parent=nodeParent)
        return newItem

    def _newItem(self, nodeType, nodeName):
        """
        Create new tree item

        :param nodeType: 'modul', 'sysData', 'cmdData', 'pyData'
        :type nodeType: str
        :param nodeName: New node name
        :type nodeName: str
        :return: New tree item
        :rtype: Modul | SysData | CmdData | PyData
        """
        if nodeType == 'modul':
            return GraphItem(self, graphNodes.Modul(nodeName))
        elif nodeType == 'sysData':
            return GraphItem(self, graphNodes.SysData(nodeName))
        elif nodeType == 'cmdData':
            return  GraphItem(self, graphNodes.CmdData(nodeName))
        elif nodeType == 'pyData':
            return GraphItem(self, graphNodes.PyData(nodeName))

    # noinspection PyUnresolvedReferences
    def _addItem(self, item, parent=None):
        """
        Add given item to tree

        :param item: Tree item
        :rtype: Modul | SysData | CmdData | PyData
        :param parent: New node parent
        :type parent: str | Modul | SysData | CmdData | PyData
        :return: New tree item
        :rtype: Modul | SysData | CmdData | PyData
        """
        if parent is None:
            self.log.detail("\t ---> Parent %s to world" % item._node.nodeName)
            self._topItems.append(item)
        else:
            if isinstance(parent, str):
                parent = self.getItemFromNodeName(parent)
            self.log.detail("\t ---> Parent %s to %s" % (item._node.nodeName, parent._node.nodeName))
            parent._children.append(item)
            item._parent = parent
        return item

    def printData(self):
        """
        Print tree datas
        """
        print self.getDatas(asString=True)


class GraphItem(object):
    """
    Grapher tree item, child of Grapher.GraphTree

    :param treeObject: Grapher tree
    :type treeObject: GraphTree
    :param nodeObject: Grapher node
    :type nodeObject: graphNodes.Modul | graphNodes.SysData | graphNodes.CmdData | graphNodes.PyData
    """

    def __init__(self, treeObject, nodeObject):
        self._tree = treeObject
        self.log = self._tree.log
        self.log.debug("#-- Init Graph Item: %s (%s) --#" % (nodeObject.nodeName,
                                                             nodeObject.nodeType), newLinesBefor=1)
        self._node = nodeObject
        self._parent = None
        self._children = []

    def getDatas(self, asString=False):
        """
        Get graphItem datas as dict or string

        :param asString: Return string instead of dict
        :type asString: bool
        :return: Item contents
        :rtype: dict | str
        """
        #-- Parse Datas --#
        nodeDatas = self._node.getDatas()
        nodeDatas['parent'] = self.parent
        #-- Return Datas --#
        if asString:
            return pprint.pformat(nodeDatas)
        return nodeDatas

    @property
    def parent(self):
        """
        Get parent node name

        :return: Node parent
        :rtype: str
        """
        if self._parent is None:
            nodeParent = None
        else:
            nodeParent = self._parent._node.nodeName
        return nodeParent

    @property
    def children(self):
        """
        Get node children

        :return: Node Children
        :rtype: list
        """
        children = []
        for child in self._children:
            children.append(child.nodeName)
        return children

    def allChildren(self, depth=-1):
        """
        Get node all children

        :param depth: Number of recursion (-1 = infinite)
        :type depth: int
        :return: Node children
        :rtype: list
        """
        children = []
        #-- Recurse Function --#
        def recurse(currentItem, depth):
            children.append(currentItem)
            if depth != 0:
                for child in currentItem._children:
                    recurse(child, depth-1)
        #-- Get Top Child --#
        for childItem in self._children:
            recurse(childItem, depth)
        #-- Result --#
        return children

    def setParent(self, graphItem):
        """
        Parent item to given GraphItem

        :param graphItem: Parent item
        :type graphItem: GraphItem
        """
        #-- Remove From Parent Children list --#
        if self._parent is not None:
            if self._parent._children:
                self._parent._children.remove(self)
        #-- Parent To Given GraphItem --#
        self._parent = graphItem
        self._parent._children.append(self)

    def setExpanded(self, state):
        """
        Expand item with given state

        :param state: Expand state
        :type state: bool
        """
        self._node.nodeIsExpanded = state
        if not state:
            for child in self.allChildren():
                child._node.nodeIsExpanded = state

    def delete(self):
        """
        Delete GraphItem
        """
        if self._parent is None:
            self._tree._topItems.remove(self)
        else:
            self._parent._children.remove(self)



if __name__ == '__main__':
    gp = Grapher(logLvl='debug')
    gp.tree.createItem(nodeName='toto_1')
    print '#' * 120
    print gp.tree.getDatas(asString=True)
