try:
    import maya.cmds as mc
except:
    pass


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

def listTransforms(mesh):
    """ get transform from given mesh
        :param mesh: (str) : Mesh node name
        :return: (str): Transform node """
    return mc.listRelatives(mesh, p=True, pa=True)
