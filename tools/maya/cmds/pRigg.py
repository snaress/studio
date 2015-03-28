try:
    import maya.cmds as mc
    import maya.mel as ml
except:
    pass


def listTransforms(mesh):
    """ get transform from given mesh
        :param mesh: Mesh node name
        :type mesh: str
        :return: Transform node
        :rtype: list """
    return mc.listRelatives(mesh, p=True, pa=True)

def getPlugNode(connectionPlug):
    """ Get plug node from given connection
        :param connectionPlug: Connection plug
        :type connectionPlug: str
        :return: Plug node name
        :rtype: str """
    return connectionPlug.split('.')[0]

def getPlugAttr(connectionPlug):
    """ Get plug attribute from given connection
        :param connectionPlug: Connection plug
        :type connectionPlug: str
        :return: Plug attribute name
        :rtype: str """
    return '.'.join(connectionPlug.split('.')[1:])

def getNextFreeMultiIndex(attr, start=0):
    """ Returns the next multi index that's available for the given destination attribute
        :param attr:  Name of the multi attribute
        :type attr: str
        :param start: the first index to check from (use 0 if last index is not known)
        :type start: int
        :return: Available index
        :rtype: int """
    # assume a max of 10 million connections
    for n in range(start, 10000000, 1):
        conn = mc.connectionInfo('%s[%s]' % (attr, n), sfd=True)
        if not conn:
            return n
    return 0

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
        :return: Connected objType nodes
        :rtype: list """
    # Test with list return instead of closest connected node
    # Replace return pastObjs with return pastObjs[0] etc
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
                    if pastList[i] in pastObjs:
                        return pastObjs
                    if futureList[i] in futureObjs:
                        return futureObjs
            else:
                return pastObjs
        elif futureObjs:
            return futureObjs
    else:
        if past:
            hist = mc.listHistory(obj, f=False, bf=True, af=True)
            objs = mc.ls(hist, type=objType)
            if objs:
                return objs
        if future:
            hist = mc.listHistory(obj, f=True, bf=True, af=True)
            objs = mc.ls(hist, type=objType)
            if objs:
                return objs

def transfertWrapConns(wrapPlugs, newNode):
    """ Given a list of wrap plugs, transfer the connections from
        their current source to the given newNode.
        :param wrapPlugs: Wrap connection plugs
        :type wrapPlugs: list
        :param newNode: Destination node
        :type newNode: str """
    for wrapPlug in wrapPlugs:
        wrapAttr = getPlugAttr(wrapPlug)
        for attr in ['driverPoints', 'basePoints']:
            if wrapAttr.startswith(attr):
                meshConns = mc.listConnections(wrapPlug, s=True, p=True, sh=True, type='mesh')
                if meshConns:
                    #-- Transfert connections --#
                    meshAttr = getPlugAttr(meshConns[0])
                    mc.disconnectAttr(meshConns[0], wrapPlug)
                    mc.connectAttr('%s.%s' % (newNode, meshAttr), wrapPlug)


class FromMel(object):
    """ Rigg commands calling mel script """

    def __init__(self):
        pass

    @staticmethod
    def listTransforms(mesh):
        """ get transform from given mesh
            :param mesh: Mesh node name
            :type mesh: str
            :return: Transform node
            :rtype: list """
        return ml.eval('listTransforms("%s")' % mesh)

    @staticmethod
    def getPlugNode(connectionPlug):
        """ Get plug node from given connection
            :param connectionPlug: Connection plug
            :type connectionPlug: str
            :return: Plug node name
            :rtype: str """
        return ml.eval('plugNode("%s")' % connectionPlug)

    @staticmethod
    def getPlugAttr(connectionPlug):
        """ Get plug attribute from given connection
            :param connectionPlug: Connection plug
            :type connectionPlug: str
            :return: Plug attribute name
            :rtype: str """
        return ml.eval('plugAttr("%s")' % connectionPlug)

    @staticmethod
    def getNextFreeMultiIndex(connectionPlug, start=0):
        """ Returns the next multi index that's available for the given destination attribute
            :param connectionPlug:  Name of the multi attribute
            :type connectionPlug: str
            :param start: the first index to check from (use 0 if last index is not known)
            :type start: int
            :return: Available index
            :rtype: int """
        return ml.eval('getNextFreeMultiIndex("%s", %s)' % (connectionPlug, start))

    @staticmethod
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
        return ml.eval('findTypeInHystory("%s", "%s", %s, %s)' % (obj, objType, int(future), int(past)))

    @staticmethod
    def transfertWrapConns(wrapPlugs, newNode):
        """ Given a list of wrap plugs, transfer the connections from
            their current source to the given newNode.
            :param wrapPlugs: Wrap connection plugs
            :type wrapPlugs: list
            :param newNode: Destination node
            :type newNode: str """
        ml.eval('transfertWrapConns("%s", "%s")' % (wrapPlugs, newNode))

