import pprint
from appli.grapher.core import graphNodes


class GraphTree(object):
    """
    Grapher tree, child of Grapher

    :param grapher: Grapher core
    :type grapher: grapher.Grapher
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

    def topItemIndex(self, topItem):
        """
        Get given topItem index

        :param topItem: Top GraphItem
        :type topItem: GraphItem
        :return: Top item index
        :rtype: int
        """
        for n, tItem in enumerate(self.topItems()):
            if tItem == topItem:
                return n

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

    def buildTree(self, treeDict):
        """
        Build tree from given tree datas

        :param treeDict: Tree datas
        :type treeDict: dict
        """
        for n in sorted(treeDict.keys()):
            newItem = self.createItem(nodeType=treeDict[n]['nodeType'],
                                      nodeName=treeDict[n]['nodeName'],
                                      nodeParent=treeDict[n]['parent'])
            # noinspection PyUnresolvedReferences
            newItem._node.setDatas(**treeDict[n])

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
        :rtype: Modul | SysData | CmdData | PurData | Loop
        """
        if nodeType == 'modul':
            return GraphItem(self, graphNodes.Modul(nodeName, self.gp))
        elif nodeType == 'sysData':
            return GraphItem(self, graphNodes.SysData(nodeName, self.gp))
        elif nodeType == 'cmdData':
            return  GraphItem(self, graphNodes.CmdData(nodeName, self.gp))
        elif nodeType == 'purData':
            return GraphItem(self, graphNodes.PurData(nodeName, self.gp))
        elif nodeType == 'loop':
            return GraphItem(self, graphNodes.Loop(nodeName, self.gp))

    # noinspection PyUnresolvedReferences
    def _addItem(self, item, parent=None):
        """
        Add given item to tree

        :param item: Tree item
        :rtype: Modul | SysData | CmdData | PyData | Loop
        :param parent: New node parent
        :type parent: str | Modul | SysData | CmdData | PyData | Loop
        :return: New tree item
        :rtype: Modul | SysData | CmdData | PyData | Loop
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
            children.append(child._node.nodeName)
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

    def allParents(self, depth=-1):
        """
        Get node all parents

        :param depth: Number of recursion (-1 = infinite)
        :type depth: int
        :return: Node parents
        :rtype: list
        """
        parents = []
        def recurse(currentItem, depth):
            parents.append(currentItem)
            if depth != 0:
                if currentItem._parent is not None:
                    recurse(currentItem._parent, depth-1)
        if self._parent is not None:
            recurse(self._parent, depth)
        return parents

    def childItemIndex(self, childItem):
        """
        Get given chilItem index

        :param childItem: Child GraphItem
        :type childItem: GraphItem
        :return: Child item index
        :rtype: int
        """
        for n, cItem in enumerate(self._children):
            if cItem == childItem:
                return n

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

    def setEnabled(self, state):
        """
        Enable item with given state

        :param state: Enable state
        :type state: bool
        """
        self._node.nodeIsEnabled = state
        self._node.nodeIsActive = state
        for child in self.allChildren():
            if child._node.nodeIsEnabled:
                if child._parent is not None:
                    if not child._parent._node.nodeIsActive:
                        child._node.nodeIsActive = False
                    else:
                        child._node.nodeIsActive = state
                else:
                    child._node.nodeIsActive = state
            else:
                child._node.nodeIsActive = False

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

    def move(self, side):
        newIndex = self._getNewIndex(side)
        if newIndex is not None:
            if self._parent is None:
                self._tree._topItems.pop(self._tree.topItemIndex(self))
                self._tree._topItems.insert(newIndex, self)
            else:
                self._parent._children.pop(self._parent.childItemIndex(self))
                self._parent._children.insert(newIndex, self)

    def _getNewIndex(self, side):
        """
        Get new insertion index

        :param side: 'up', 'down'
        :type side: str
        :return: New index
        :rtype: int
        """
        #-- Get Current Index --#
        if self._parent is None:
            index = self._tree.topItemIndex(self)
            iCount = len(self._tree._topItems)
        else:
            index = self._parent.childItemIndex(self)
            iCount = len(self._parent._children)
        #- Side Up New Index --#
        if side == 'up':
            if index > 0:
                newIndex = index - 1
            else:
                newIndex = None
        #-- Side Down New Index --#
        else:
            if index < (iCount - 1):
                newIndex = index + 1
            else:
                newIndex = None
        return newIndex

    def delete(self):
        """
        Delete GraphItem
        """
        if self._parent is None:
            self._tree._topItems.remove(self)
        else:
            self._parent._children.remove(self)
