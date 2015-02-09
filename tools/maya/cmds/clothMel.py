try:
    import maya.mel as ml
except:
    pass


class FromMel(object):
    """ NCloth commands calling mel script """

    def __init__(self):
        pass

    @staticmethod
    def createNSystem():
        """ If there is an nucleus node selected, return it, else, create a new one and return it
            :return: Nucleus node name
            :rtype: str """
        return ml.eval("createNSystem:")

    @staticmethod
    def addActiveToNSystem(active, nucleus):
        """ Connect nCloth to given nucleus
            :param active: nCloth node
            :type active: str
            :param nucleus: Nucleus node
            :type nucleus: str
            :return: Nucleus inputActive attribute index
            :rtype: int """
        return ml.eval('addActiveToNSystem("%s", "%s");' % (active, nucleus))

    @staticmethod
    def addPassiveToNSystem(passive, nucleus):
        """ Connect nCloth or nRigid to given nucleus
            :param passive: nRigid node
            :type passive: str
            :param nucleus: Nucleus node
            :type nucleus: str
            :return: Nucleus inputPassive attribute index
            :rtype: int """
        return ml.eval('addPassiveToNSystem("%s", "%s");' % (passive, nucleus))

    @staticmethod
    def getActiveNucleusNode(selectExisting=True, createNew=False):
        """ Find the currently active nucleus node, if none found, create one
            :param selectExisting: Select exisitng nucleus node
            :type selectExisting: bool
            :param createNew: Force new nucleus node creation
            :type createNew: bool
            :return: Active nucleus node
            :rtype: str """
        return ml.eval("getActiveNucleusNode(%s, %s);" % (int(selectExisting), int(createNew)))

    @staticmethod
    def createNCloth(worldSpace=False):
        """ Create nCloth node on selection
            :param worldSpace: If true, use worldSpace, else use localSpace
            :type worldSpace: bool
            :return: New nCloth nodes
            :rtype: list """
        return ml.eval("createNCloth %s;" % int(worldSpace))

    @staticmethod
    def createNRigid():
        """ Create nRigid node on selection
            :return: New nRigid nodes
            :rtype: list """
        return ml.eval("makeCollideNCloth;")

    @staticmethod
    def removeNCloth(delMode='selected'):
        """ Remove nCloth or nRigid nodes
            :param delMode: 'selected', 'allNCloths', 'allNRigids'
            :type delMode: str """
        ml.eval('removeNCloth "%s";' % delMode)
