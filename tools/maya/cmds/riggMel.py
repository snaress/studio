try:
    import maya.mel as ml
except:
    pass


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
