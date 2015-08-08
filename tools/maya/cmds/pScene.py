import os, sip
from PyQt4 import QtCore
try:
    import maya.cmds as mc
    import maya.OpenMayaUI as mOpen
except:
    pass


def getMayaMainWindow():
    """ Get maya main window
        :return: Maya main window
        :rtype: QtCore.QObject """
    return sip.wrapinstance(long(mOpen.MQtUtil.mainWindow()), QtCore.QObject)

def loadScene(sceneName, force=True):
    """ Open given maya scene
        :param sceneName: Scene absolut path
        :type sceneName: str
        :param force: Force opening
        :type force: bool """
    print "Opening Maya Scene: %s" % sceneName
    mc.file(sceneName, o=True, f=force)

def importScene(sceneName, force=True):
    """ Import given scene
        :param sceneName: Scene absolut path
        :type sceneName: str
        :param force: Force opening
        :type force: bool """
    ext = os.path.splitext(sceneName)[-1]
    if ext == '.ma':
        print "Importing Maya Scene from ascii file: %s" % sceneName
        mc.file(sceneName, i=True, type="mayaAscii", pr=True, lrd="all", f=force)
    elif ext == '.mb':
        print "Importing Maya Scene from binary file: %s" % sceneName
        mc.file(sceneName, i=True, type="mayaBinary", pr=True, lrd="all", f=force)
    else:
        raise IOError, "Error: Unrecognize extention: %s" % ext

def saveSceneAs(sceneName, force=False, keepCurrentName=False):
    """ Save scene with given name
        :param sceneName: Scene absolut path
        :type sceneName: str
        :param force: Force opening
        :type force: bool
        :param keepCurrentName: Keep original scene name
        :type keepCurrentName: bool """
    currentSceneName = mc.file(q=True, sn=True)
    mc.file(rn=sceneName)
    ext = os.path.splitext(sceneName)[-1]
    if ext == '.ma':
        print "Saving Maya Scene from ascii file: %s" % sceneName
        mc.file(s=True, type="mayaAscii", f=force)
    elif ext == '.mb':
        print "Saving Maya Scene from binary file: %s" % sceneName
        mc.file(s=True, type="mayaBinary", f=force)
    else:
        raise IOError, "Error: Unrecognize extention: %s" % ext
    if keepCurrentName:
        print "Keep Scene Name: %s" % currentSceneName
        mc.file(rn=currentSceneName)

def exportSel(sceneName, force=True):
    """ Save selection with given name
        :param sceneName: Scene absolut path
        :type sceneName: str
        :param force: (bool) : Force opening
        :type force: bool """
    ext = os.path.splitext(sceneName)[-1]
    if ext == '.ma':
        print "Saving Maya Scene from ascii file: %s" % sceneName
        mc.file(sceneName, es=True, f=force, op="v=0", typ="mayaAscii", pr=True)
    elif ext == '.mb':
        print "Saving Maya Scene from binary file: %s" % sceneName
        mc.file(sceneName, es=True, f=force, op="v=0", typ="mayaBinary", pr=True)
    else:
        print "Error: Unrecognize extention: %s" % ext

def wsToDict():
    """ Store workspace info to dict
        :return: Workspace info
        :rtype: dict """
    wsDict = {'projectName': mc.workspace(q=True, fn=True).split('/')[-1],
              'projectPath': mc.workspace(q=True, fn=True), 'fileRules': {}}
    fr = mc.workspace(q=True, fr=True)
    for n in range(0, len(fr), 2):
        wsDict['fileRules'][fr[n]] = fr[n+1]
    return wsDict

def wsDictToStr(wsDict=None):
    """ Convert workspace dict to string
        :param wsDict: Workspace info (If None, use current workspace)
        :type wsDict: dict
        :return: Workspace info
        :rtype: str """
    if wsDict is None:
        wsDict = wsToDict
    txt = ["#-- Workspace Info --#",
           "Project Name = %s" % wsDict['projectName'], "Project Path = %s" % wsDict['projectPath'],
           "#-- File Rules --#"]
    for k, v in wsDict['fileRules'].iteritems():
        txt.append("%s = %s" % (k, v))
    return '\n'.join(txt)

def getNamespace(nodeName, returnList=False):
    """ Get given node namespace
        :param nodeName: Node full name
        :type nodeName: str
        :param returnList: Return result as list instead of str
        :return: Node namespace, Node name
        :rtype: (str | list, str) """
    if ':' in nodeName:
        if returnList:
            return nodeName.split(':')[:-1], nodeName.split(':')[-1]
        else:
            return ':'.join(nodeName.split(':')[:-1]) , nodeName.split(':')[-1]
    return None, nodeName

def getTimeRange():
    """
    Get scene time range
    :return: time range info
    :rtype: dict
    """
    return {'timeSliderStart': mc.playbackOptions(q=True, min=True),
            'timeSliderStop': mc.playbackOptions(q=True, max=True),
            'timeRangeStart': mc.playbackOptions(q=True, ast=True),
            'timeRangeStop': mc.playbackOptions(q=True, aet=True)}

def attrIsLocked(nodeFullName):
    """ Check if given node attribute is locked
        :param nodeFullName: 'nodeName.nodeAttr'
        :type nodeFullName: str
        :return: Attribute lock state
        :rtype: bool """
    if mc.objExists(nodeFullName):
        return mc.getAttr(nodeFullName, l=True)
    print "!!! WARNING: Node not found: %s !!!" % nodeFullName

def setAttrLock(nodeFullName, state):
    """ Set given nodeAttr lock on or off
        :param nodeFullName: 'nodeName.nodeAttr'
        :type nodeFullName: str
        :param state: Attribute lock state
        :type state: bool
        :return: True if success, else False
        :rtype: bool """
    if mc.objExists(nodeFullName):
        try:
            mc.setAttr(nodeFullName, l=state)
            return True
        except:
            return False
    print "!!! WARNING: Node not found: %s !!!" % nodeFullName
    return False

def mayaWarning(message):
    """
    Display maya warning
    :param message: Warning to print
    :type message: str
    """
    mc.warning(message)

def mayaError(message):
    """
    Display maya error
    :param message: Error to print
    :type message: str
    """
    mc.error(message)
