import os
import pymel.core as pm
from PyQt4 import QtGui
from tools.maya.cmds import pScene
from lib.system import procFile as pFile
from tools.maya.util import toolManager as tm
from tools.maya.util.toolManager.ui import toolManagerUI
try:
    import maya.cmds as mc
except:
    pass


class ToolManagerUi(QtGui.QMainWindow, toolManagerUI.Ui_mwToolManager):

    def __init__(self, parent=None):
        self.log = pFile.Logger(title="toolManager")
        self.log.info("#-- Launching ToolManager Ui --#")
        self.toolsPath = pFile.conformPath(os.sep.join(tm.toolPath.split(os.sep)[:-2]))
        super(ToolManagerUi, self).__init__(parent)
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup main ui """
        self.setupUi(self)
        self.twTools.itemDoubleClicked.connect(self.on_tool)
        self._refresh()

    def _refresh(self):
        """ Refresh main ui """
        steps = os.listdir(self.toolsPath) or []
        #-- Add Steps --#
        for step in steps:
            if not step.startswith('_') and not step.startswith('.') and not step == 'cmds':
                stepPath = pFile.conformPath(os.path.join(self.toolsPath, step))
                if os.path.isdir(stepPath):
                    stepItem = self._newItem(step, 'step')
                    stepItem.path = stepPath
                    self.twTools.addTopLevelItem(stepItem)
                    #-- Add Tools --#
                    tools = os.listdir(stepPath) or []
                    for tool in tools:
                        if not tool.startswith('_') and not tool.startswith('.'):
                            toolPath = pFile.conformPath(os.path.join(stepPath, tool))
                            if os.path.isdir(toolPath):
                                launcher = pFile.conformPath(os.path.join(toolPath, "__tm__.py"))
                                if os.path.exists(launcher):
                                    toolItem = self._newItem(tool, 'tool')
                                    toolItem.path = toolPath
                                    toolItem.launcher = launcher
                                    stepItem.addChild(toolItem)

    def on_tool(self):
        """ Command launched when tool QTreeWidgetItem is doubleClicked """
        selItems = self.twTools.selectedItems() or []
        if selItems:
            if hasattr(selItems[0], 'launcher'):
                self.log.info("Launching %s ..." % selItems[0].nodeName)
                execfile(selItems[0].launcher)

    @staticmethod
    def _newItem(nodeName, nodeType):
        """ Create new item
            :param nodeName: (str) : Node Name
            :param nodeType: (str) : 'step' or 'tool'
            :return: (object) : QTreeWidgetItem """
        newItem = QtGui.QTreeWidgetItem()
        newItem.nodeName = nodeName
        if nodeType == 'step':
            newItem.setText(0, nodeName.upper())
        else:
            newItem.setText(0, nodeName)
        return newItem

    def close(self):
        self.log.info("#-- Closing ToolManager Ui --#")
        super(ToolManagerUi, self).close()



def launch():
    """ Launch ToolManager
        :return: (object) : Launched window """
    toolName = 'mwToolManager'
    if 'tmDock' in mc.lsUI(type='dockControl'):
        print "Delete ToolManager DockControl"
        mc.deleteUI('tmDock')
    if mc.window(toolName, q=True, ex=True):
        print "Delete ToolManager Window"
        pm.deleteUI(toolName, wnd=True)
    window = ToolManagerUi(parent=pScene.getMayaMainWindow())
    mc.dockControl('tmDock', aa=['right', 'left'], a='right', content=str(window.objectName()), label='ToolManager')
    return window
