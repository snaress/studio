try:
    import maya.cmds as mc
except:
    pass


def findTypeInHistory(obj, objType, future=False, past=False):
    """ returns the node of the specified type that is the closest traversal to the input object
        :param obj: Object name
        :type obj: str
        :param objType: Object type list
        :type objType: list
        :param future: Future depth
        :type future: bool
        :param past: Past depth
        :type past: bool
        :return: Closest node connected
        :rtype: str """
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

def listTransforms(mesh):
    """ get transform from given mesh
        :param mesh: Mesh node name
        :type mesh: str
        :return: Transform node
        :rtype: str """
    return mc.listRelatives(mesh, p=True, pa=True)

def getNextFreeMultiIndex(attr, start=0):
    """ Returns the next multi index that's available for the given destination attribute
        :param attr:  Name of the multi attribute
        :type attr: str
        :param start: the first index to check from (use zero if last index is not known)
        :type start: int
        :return: Available index
        :rtype: int """
    for n in range(start, 10000000, 1):
        conn = mc.connectionInfo('%s[%s]' % (attr, n), sfd=True)
        if not conn:
            return n
    return 0

def plugNode(connectionPlug):
    """ Get plug node from given connection
        :param connectionPlug: Connection plug
        :type connectionPlug: str
        :return: Plug node name
        :rtype: str """
    return connectionPlug.split('.')[0]

def plugAttr(connectionPlug):
    """ Get plug attribute from given connection
        :param connectionPlug: Connection plug
        :type connectionPlug: str
        :return: Plug attribute name
        :rtype: str """
    return '.'.join(connectionPlug.split('.')[1:])

def transfertWrapConns(wrapPlugs, newNode):
    """ Given a list of wrap plugs, transfer the connections from
        their current source to the given newNode.
        :param wrapPlugs: Wrap connection plugs
        :type wrapPlugs: list
        :param newNode: Destination node
        :type newNode: str """
    for wrapPlug in wrapPlugs:
        wrapAttr = plugAttr(wrapPlug)
        for attr in ['driverPoints', 'basePoints']:
            if wrapAttr.startswith(attr):
                meshConns = mc.listConnections(wrapPlug, s=True, p=True, sh=True, type='mesh')
                if meshConns:
                    #-- Transfert connections --#
                    meshAttr = plugAttr(meshConns[0])
                    mc.disconnectAttr(meshConns[0], wrapPlug)
                    mc.connectAttr('%s.%s' % (newNode, meshAttr), wrapPlug)
