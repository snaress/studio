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
        self.entityParent = None
        self.entityName = None
        self.entityLabel = None
        self.entityFolder = None

    @property
    def _entityParent(self):
        """
        Get parent entity object

        :return: Parent entity
        :rtype: Entity
        """
        if self.entityParent is not None:
            return self._parent.getEntityObjFromName(self.entityParent)

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

    def _setup(self):
        """
        Setup Entities core object
        """
        self.log.detail("#===== Setup Entities Core =====#", newLinesBefore=1)
        #-- Store Entities Data --#
        self.log.debug("#--- Store Entities Datas ---#")


    def getEntitiesDatas(self, asString=False):
        """
        Get entities datas

        :param asString: Return string instead of dict
        :type asString: bool
        :return: Entities datas
        :rtype: dict | str
        """
        entitiesDict = dict()
        for n, entityObj in enumerate(self._entities):
            entitiesDict[n] = entityObj.getDatas(asString=asString)
        #-- Result --#
        if asString:
            return pprint.pformat(entitiesDict)
        return entitiesDict

    def getEntityObjFromName(self, entityName):
        """
        Get group object from given groupName

        :param entityName: Entity name
        :type entityName: str
        :return: Entity object
        :rtype: Entity
        """
        for entity in self._entities:
            if entity.entityName == entityName:
                return entity

    def buildEntitiesFromSettings(self):
        """
        Populate _entities from settings
        """
        if 'entities' in self.fondation.settings.keys():
            if 'structure' in self.fondation.settings['entities'].keys():
                self.buildEntitiesFromDict(self.fondation.settings['entities']['structure'])

    def buildEntitiesFromDict(self, entityDict):
        """
        Populate _entities from given dict

        :param entityDict: Entities dict
        :type entityDict: dict
        """
        self._entities = []
        for n in sorted(entityDict.keys()):
            newEntity = self.newEntity(**entityDict[n])
            self._entities.append(newEntity)

    def pushEntitiesToSettings(self):
        """
        Push Groups to settings file
        """
        self.log.debug("Push entities datas to settings ...")
        #-- Refresh Settings --#
        self.log.detail("---> Refresh settings ...")
        self.fondation.storeSettings()
        #-- Check Keys --#
        if not 'entities' in self.fondation.settings:
            self.log.detail("---> Add 'entities' ...")
            self.fondation.settings['entities'] = dict()
        if not 'structure' in self.fondation.settings['entities']:
            self.log.detail("---> Add 'structure' to 'entities' ...")
            self.fondation.settings['entities']['structure'] = dict()
        #-- Push Settings --#
        self.fondation.settings['entities']['structure'] = self.getEntitiesDatas()

    def newEntity(self, **kwargs):
        """
        Create new Entity object

        :param kwargs: Entity datas (key must starts with 'entity')
        :type kwargs: dict
        :return: Entity object
        :rtype: Entity
        """
        entityObj = Entity(parent=self)
        entityObj.setDatas(**kwargs)
        return entityObj
