import os
try:
    import maya.cmds as mc
except:
    pass


def loadScene(sceneName, force=True):
    """ Open given maya scene
        :param sceneName: (str) : Scene absolut path
        :param force: (bool) : Force opening """
    print "Opening Maya Scene: %s" % sceneName
    mc.file(sceneName, o=True, f=force)

def importScene(sceneName, force=True):
    """ Import given scene
        :param sceneName: (str) : Scene absolut path
        :param force: (bool) : Force opening """
    ext = os.path.splitext(sceneName)[-1]
    if ext == '.ma':
        print "Importing Maya Scene from ascii file: %s" % sceneName
        mc.file(sceneName, i=True, type="mayaAscii", pr=True, lrd="all", f=force)
    elif ext == '.mb':
        print "Importing Maya Scene from binary file: %s" % sceneName
        mc.file(sceneName, i=True, type="mayaBinary", pr=True, lrd="all", f=force)
    else:
        print "Error: Unrecognize extention: %s" % ext

def saveSceneAs(sceneName, force=False, keepCurrentName=False):
    """ Save scene with given name
        :param sceneName: (str) : Scene absolut path
        :param force: (bool) : Force opening
        :param keepCurrentName: (bool) : Keep original scene name """
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
        print "Error: Unrecognize extention: %s" % ext
    if keepCurrentName:
        print "Keep Scene Name: %s" % currentSceneName
        mc.file(rn=currentSceneName)

def exportSel(sceneName, force=True):
    """ Save selection with given name
        :param sceneName: (str) : Scene absolut path
        :param force: (bool) : Force opening """
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
        :return: (dict) : Workspace info """
    wsDict = {'projectName': mc.workspace(q=True, fn=True).split('/')[-1],
              'projectPath': mc.workspace(q=True, fn=True), 'fileRules': {}}
    fr = mc.workspace(q=True, fr=True)
    for n in range(0, len(fr), 2):
        wsDict['fileRules'][fr[n]] = fr[n+1]
    return wsDict

def wsDictToStr(wsDict=None):
    """ Convert workspace dict to string
        :param wsDict: (dict) : Workspace info (If None, use current workspace)
        :return: (str) : Workspace info """
    if wsDict is None:
        wsDict = wsToDict
    txt = ["#-- Workspace Info --#",
           "Project Name = %s" % wsDict['projectName'], "Project Path = %s" % wsDict['projectPath'],
           "#-- File Rules --#"]
    for k, v in wsDict['fileRules'].iteritems():
        txt.append("%s = %s" % (k, v))
    return '\n'.join(txt)

def findTypeInHistory(obj, objType, future=False, past=False):
    """ returns the node of the specified type that is the closest traversal to the input object
        :param obj: (str) : Object name
        :param objType: (str) : Object type
        :param future: (int) : Future depth
        :param past: (int) : Past depth
        :return: (str) : Closest node connected """
    if past and future:
        # In the case that the object type exists in both past and future,
        # find the one that is fewer connections away.
        pastList = mc.listHistory(obj, f=False, bf=True, af=True)
        futureList = mc.listHistory(obj, f=True, bf=True, af=True)
        pastObjs = mc.ls(pastList, type=objType)
        futureObjs = mc.ls(futureList, type=objType)
        if pastObjs:
            if futureObjs:
                mini = len(futureList)
                if len(pastList) < mini:
                    mini = len(pastList)
                for i in range(mini):
                    if pastList[i] == pastObjs[0]:
                        return pastObjs[0]
                    if futureList[i] == futureObjs[0]:
                        return futureObjs[0]
            else:
                return pastObjs[0]
        elif futureObjs:
            return futureObjs[0]
    else:
        if past:
            hist = mc.listHistory(obj, f=False, bf=True, af=True)
            objs = mc.ls(hist, type=objType)
            if objs:
                return objs[0]
        if future:
            hist = mc.listHistory(obj, f=True, bf=True, af=True)
            objs = mc.ls(hist, type=objType)
            if objs:
                return objs[0]
    print "!!! Error: No depth given !!!"
    return None
