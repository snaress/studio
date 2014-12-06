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

def saveSceneAs(sceneName, force=True, keepCurrentName=False):
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