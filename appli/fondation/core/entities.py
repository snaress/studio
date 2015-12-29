import pprint
from lib.system import procFile as pFile


class Entity(object):
    """
    Entity Class: Contains entities datas, child of Entity

    :param parent: Parent object
    :type parent: UserGroups
    """

    __attrPrefix__ = 'entity'

    def __init__(self, parent=None):
        self._parent = parent
        self.log = self._parent.log
        #-- Datas --#
        self.entityType = None
        self.entityName = None
        self.entityLabel = None
        self.entityFolder = None
        self._entities = []

    @property
    def attributes(self):
        """
        List all attributes

        :return: Attributes
        :rtype: list
        """
        attrs = []
        for attr in self.__dict__.keys():
            if attr.startswith(self.__attrPrefix__):
                attrs.append(attr)
        return attrs

    def getDatas(self, asString=False):
        """
        Get entity datas

        :param asString: Return string instead of dict
        :type asString: bool
        :return: Group datas
        :rtype: dict | str
        """
        datas = dict()
        for attr in self.attributes:
            datas[attr] = getattr(self, attr)
        #-- Result --#
        if asString:
            return pprint.pformat(datas)
        return datas

    def setDatas(self, **kwargs):
        """
        Set entity datas

        :param kwargs: Entity datas
        :type kwargs: dict
        """
        for k, v in kwargs.iteritems():
            if k.startswith(self.__attrPrefix__):
                setattr(self, k, v)


class Entities(object):
    """
    Entities Class: Contains entities and tasks datas, child of Fondation

    :param fdtObj: Fondation object
    :type fdtObj: Fondation
    :param logLvl : Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """

    log = pFile.Logger(title="Entities")

    def __init__(self, fdtObj, logLvl='info'):
        self.log.level = logLvl
        self.fondation = fdtObj
        #-- Datas --#
        self._entities = []

    def buildGroupsFromSettings(self):
        """
        Populate _entities from settings
        """
        if 'entities' in self.fondation.settings.keys():
            if 'entity' in self.fondation.settings['entities'].keys():
                self.buildEntitiesFromDict(self.fondation.settings['entities']['entity'])

    def buildEntitiesFromDict(self, entityDict):
        """
        Populate _entities from given dict

        :param entityDict: Entities dict
        :type entityDict: dict
        """
        self._entities = []

    def newEntity(self, entityName, entityType, entityParent, **kwargs):
        entityObj = Entity(parent=self)
        entityObj.setDatas(entityName=entityName, entityType=entityType, **kwargs)
        return entityObj