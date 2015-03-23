import os
from PyQt4 import QtGui
from lib.qt import procQt as pQt
from lib.system import procFile as pFile
from appli.prodManager import prodManager
from appli.prodManager.ui import mainTreeUI, mainTreeNodeUI


class MainTree(QtGui.QWidget, mainTreeUI.Ui_mainTree):
    """ QWidget class used by 'ProdManager' QMainWindow.
        :param mainUi: ProdManager window
        :type mainUi: QtGui.QMainWindow
        :param logLvl: Print log level
        :type logLvl: str """

    def __init__(self, mainUi, logLvl='info'):
        self.log = pFile.Logger(title="MainTree", level=logLvl)
        self.log.info("#-- Main Tree Ui --#")
        self.mainUi = mainUi
        self.pm = self.mainUi.pm
        super(MainTree, self).__init__()
        self._setupUi()
        self.refresh()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup main tree ui """
        self.setupUi(self)
        self.twTree.setStyleSheet("background-color: rgb(200, 200, 200)")

    def getItem(self, nodeName):
        """ Get QTreeWidgetItem from given nodeName
            :param nodeName: Item name or node name
            :type nodeName: str
            :return: Tree item
            :rtype: QtGui.QTreeWidgetItem """
        allItems = pQt.getAllItems(self.twTree)
        for item in allItems:
            if item.name == nodeName:
                return item

    def refresh(self):
        """ Refresh main tree """
        self.twTree.clear()
        #-- Add Trees --#
        for treeName in self.pm.treeNames:
            tree = self.pm.getTree(treeName)
            if tree is not None:
                icon = pFile.conformPath(os.path.join(self.mainUi.iconPath, 'tree.png'))
                newTreeItem = self.newItem(tree, icon)
                self.twTree.addTopLevelItem(newTreeItem)
                self.twTree.setItemWidget(newTreeItem, 0, newTreeItem._widget)
                #-- Add Tree Nodes --#
                treeParams = tree.getParams()
                for n in sorted(treeParams.keys()):
                    treeDict = treeParams[n]
                    if treeDict['type'] == 'container':
                        icon = pFile.conformPath(os.path.join(self.mainUi.iconPath, '%s.png' % treeDict['type']))
                    else:
                        icon = pFile.conformPath(os.path.join(self.mainUi.iconPath, '%s.png' % tree.type))
                    _object = tree.getTreeNode(treeDict['name'])
                    newNodeItem = self.newItem(_object, icon)
                    if treeDict['_parent'] is None:
                        newTreeItem.addChild(newNodeItem)
                    else:
                        parentItem = self.getItem(treeDict['_parent'])
                        parentItem.addChild(newNodeItem)
                    self.twTree.setItemWidget(newNodeItem, 0, newNodeItem._widget)

    def newItem(self, nodeObject, icon):
        """ Create new tree item
            :param nodeObject: Linked node object from ProdManager
            :type nodeObject: prodManager.Tree | prodManager.TreeNode
            :param icon: New item icon path
            :type icon: str
            :return: New tree item
            :rtype: QtGui.QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem.name = nodeObject.name
        newItem.label = nodeObject.label
        newItem.type = nodeObject.type
        newItem._object = nodeObject
        newItem._widget = MainTreeNode(self, newItem, icon)
        return newItem


class MainTreeNode(QtGui.QWidget, mainTreeNodeUI.Ui_wgTreeNode):

    def __init__(self, pWidget, item, icon):
        self.pWidget = pWidget
        self.item = item
        self.name = self.item._object.name
        self.label = self.item._object.label
        self.type = self.item._object.type
        self.iconPath = icon
        super(MainTreeNode, self).__init__()
        self._setupUi()

    def _setupUi(self):
        """ Setup widget """
        self.setupUi(self)
        btnIcon = QtGui.QIcon(self.iconPath)
        self.pbIcon.setIcon(btnIcon)
        newFont = QtGui.QFont()
        newFont.setBold(True)
        if self.type in ['asset', 'shot', 'container']:
            self.lName.setText(self.label.upper())
        else:
            self.lName.setText(self.label.capitalize())
            self.lName.setStyleSheet("color: rgb(50, 100, 255)")
        self.lName.setFont(newFont)
        self.lName.setFixedHeight(10)
