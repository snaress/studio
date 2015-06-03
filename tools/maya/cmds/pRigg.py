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
        :type objType: str | list
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

def createWrap(driver, mesh, **kwargs):
    """ Create wrap deformer
        :param driver: Wrap driver mesh
        :type driver: str
        :param mesh: Wrap driven mesh
        :type mesh: str
        :param kwargs: Wrap options:
                       :keyword weightThreshold: Weight Treshold
                       :type weightThreshold: float
                       :keyword maxDistance: Max Distance
                       :type maxDistance: float
                       :keyword exclusiveBind: Exclusive Bind
                       :type exclusiveBind: bool
                       :keyword autoWeightThreshold: Auto Weight Treshold
                       :type autoWeightThreshold: bool
                       :keyword falloffMode: Falloff Mode
                       :type falloffMode: int
        :return: BaseMesh name, wrapNode name
        :rtype: (str, str) """
    #-- Get Wrap Options --#
    influenceShape = mc.listRelatives(driver, shapes=True)[0]
    weightThreshold = kwargs.get('weightThreshold', 0.0)
    maxDistance = kwargs.get('maxDistance', 1.0)
    exclusiveBind = kwargs.get('exclusiveBind', False)
    autoWeightThreshold = kwargs.get('autoWeightThreshold', True)
    falloffMode = kwargs.get('falloffMode', 0)

    #-- Create Wrap Deformer --#
    wrapNode = mc.deformer(mesh, type='wrap')[0]
    mc.setAttr("%s.weightThreshold" % wrapNode, weightThreshold)
    mc.setAttr("%s.maxDistance" % wrapNode, maxDistance)
    mc.setAttr("%s.exclusiveBind" % wrapNode, exclusiveBind)
    mc.setAttr("%s.autoWeightThreshold" % wrapNode, autoWeightThreshold)
    mc.setAttr("%s.falloffMode" % wrapNode, falloffMode)
    mc.connectAttr("%s.worldMatrix[0]" % mesh, "%s.geomMatrix" % wrapNode)

    #-- Add Influence --#
    base = mc.duplicate(driver, name="%sBase" % driver)[0]
    baseShape = mc.listRelatives(base, shapes=True)[0]
    mc.hide(base)

    #-- Create Dropoff --#
    if not mc.attributeQuery('dropoff', n=driver, exists=True):
        mc.addAttr(driver, sn='dr', ln='dropoff', dv=4.0, min=0.0, max=20.0)
        mc.setAttr("%s.dr" % driver, k=True)

    #-- Type Mesh --#
    if mc.nodeType(influenceShape) == 'mesh':
        # Create smoothness attr if it doesn't exist
        if not mc.attributeQuery('smoothness', n=driver, exists=True):
            mc.addAttr(driver, sn='smt', ln='smoothness', dv=0.0, min=0.0)
            mc.setAttr("%s.smt" % driver, k=True)
        # Create the inflType attr if it doesn't exist
        if not mc.attributeQuery('inflType', n=driver, exists=True):
            mc.addAttr(driver, at='short', sn='ift', ln='inflType', dv=2, min=1, max=2)
        mc.connectAttr("%s.worldMesh" % influenceShape, "%s.driverPoints[0]" % wrapNode)
        mc.connectAttr("%s.worldMesh" % baseShape, "%s.basePoints[0]" % wrapNode)
        mc.connectAttr("%s.inflType" % driver, "%s.inflType[0]" % wrapNode)
        mc.connectAttr("%s.smoothness" % driver, "%s.smoothness[0]" % wrapNode)

    #-- Type NurbsCurve or NurbsSurface --#
    if mc.nodeType(influenceShape) == 'nurbsCurve' or mc.nodeType(influenceShape) == 'nurbsSurface':
        # Create the wrapSamples attr if it doesn't exist
        if not mc.attributeQuery('wrapSamples', n=driver, exists=True):
            mc.addAttr(driver, at='short', sn='wsm', ln='wrapSamples', dv=10, min=1)
            mc.setAttr("%s.wsm" % driver, k=True)
        mc.connectAttr("%s.ws" % influenceShape, "%s.driverPoints[0]" % wrapNode)
        mc.connectAttr("%s.ws" % baseShape, "%s.basePoints[0]" % wrapNode)
        mc.connectAttr("%s.wsm" % driver, "%s.nurbsSamples[0]" % wrapNode)

    #-- Connect Dropoff --#
    mc.connectAttr("%s.dropoff" % driver, "%s.dropoff[0]" % wrapNode)
    return base, wrapNode

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
