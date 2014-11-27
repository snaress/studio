import pymel.core as pm
from tools.maya.util.proc import procUi as pUi


def launch():
    """ Launch ToolManager
        :return: (object) : Launched window """
    toolName = 'factory'
    from appli.factory import factoryUi
    reload(factoryUi)
    if pm.window(toolName, q=True, ex=True):
        pm.deleteUI(toolName, wnd=True)
    window = factoryUi.FactoryUi(parent=pUi.getMayaMainWindow())
    window.show()
    return window

launch()