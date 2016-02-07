import os, pprint
from lib.system import procFile as pFile


class EntityNode(object):
    """
    EntityNode Class: Common class used by Entity, Asset and Shot

    :param entitiesObj: Entities object
    :type entitiesObj: Entities
    :param parent: Parent Entity
    :type parent: Entity
    """

    def __init__(self, entitiesObj, parent=None):
        self.entities = entitiesObj
        self.foundation = self.entities.foundation
        self.log = self.entities.log
        self._parent = parent
        self._childs = None

    @property
    def parent(self):
        """
        Get parent entity

        :return: Parent entity
        :rtype: str
        """
        return self._parent.entityCode

    # noinspection PyUnresolvedReferences
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

    def getData(self, recursive=False, asString=False):
        """
        Get Entity data

        :param recursive: Recursive state
        :type recursive: bool
        :param asString: Return string instead of dict
        :type asString: bool
        :return: Entity data
        :rtype: dict | str
        """
        data = dict()
        for attr in self.attributes:
            data[attr] = getattr(self, attr)
            if recursive:
                if self._childs is not None:
                    data['childs'] = dict()
                    for c , childObj in enumerate(self._childs):
                        data['childs'][c] = childObj.getData(recursive=False)
        if asString:
            return pprint.pformat(data)
        return data

    # noinspection PyUnresolvedReferences
    def setData(self, **kwargs):
        """
        Set entity data

        :param kwargs: Entity data (key must start with 'entity')
        :type kwargs: dict
        """
        for k, v in kwargs.iteritems():
            if k.startswith(self.__attrPrefix__):
                if k in self.attributes:
                    setattr(self, k, v)
                else:
                    self.log.warning("!!! Unrecognized attribute: %s. Skip !!!" % k)


class Entity(EntityNode):
    """
    Entity Class: Class Contains entity data, child of Entities

    :param entitiesObj: Entities object
    :type entitiesObj: Entities
    :param parent: Parent Entity
    :type parent: Entity
    """

    __attrPrefix__ = 'entity'

    def __init__(self, entitiesObj, parent=None):
        super(Entity, self).__init__(entitiesObj, parent=parent)
        self.nodeType = 'entity'
        self._childs = []
        #-- data --#
        self.entityContext = None
        self.entityType = None
        self.entityCode = None
        self.entityName = None

    @property
    def entityLabel(self):
        """
        Get entity label

        :return: Entity label
        :rtype: str
        """
        if self.entityName is not None:
            return self.entityName.capitalize()

    @property
    def subTypes(self):
        """
        Get entities subTypes

        :return: Entities subTypes
        :rtype: list
        """
        entities = []
        for entityObj in self._childs:
            entities.append(entityObj.entityCode)
        return entities

    def getSubTypeFromCode(self, entityCode):
        """
        Get entity object (subType) considering given code

        :param entityCode: Entity code
        :type entityCode: str
        :return: Entity object (subType)
        :rtype: Entity
        """
        for entityObj in self._childs:
            if entityObj.entityCode == entityCode:
                return entityObj


class Entities(object):
    """
    Entities Class: Contains entities data, child of Foundation

    :param foundationObj: Foundation object
    :type foundationObj: Foundation
    :param projectObj: Foundation Project object
    :type projectObj: Project
    """

    __assetsDir__ = "assets"
    __shotsDir__ = "shots"

    def __init__(self, foundationObj, projectObj):
        self.foundation = self.fdn = foundationObj
        self.project = projectObj
        self.log = self.fdn.log
        self.log.title = 'Entities'
        #-- data --#
        self._assets = []
        self._shots = []
        #-- Update --#
        self._setup()

    def _setup(self):
        """
        Setup Entities core object
        """
        self.log.info("#===== Setup Entities Core =====#", newLinesBefore=1)
        #-- Check UserGroups File --#
        self.log.debug("#--- Check Entities File ---#")
        if not os.path.exists(self.settingsFile):
            self.createSettingsFile()

    @property
    def settingsFile(self):
        """
        Get entities file full path

        :return: Entities file full path
        :rtype: str
        """
        return pFile.conformPath(os.path.join(self.fdn.__settingsPath__, 'entities.py'))

    def contextTree(self, context):
        """
        Get entities tree considering given context

        :param context: 'asset' or 'shot'
        :type: str
        :return: Entities tree
        :rtype: list
        """
        return getattr(self, '_%ss' % context)

    def resetContextTree(self, context):
        """
        Reset given context tree

        :param context: 'asset' or 'shot'
        :type: str
        """
        setattr(self, '_%ss' % context, [])

    def mainTypes(self, context):
        """
        Get entities mainTypes considering given context

        :param context: 'asset' or 'shot'
        :type context: str
        :return: Entities mainTypes
        :rtype: list
        """
        entities = []
        for entityObj in self.contextTree(context):
            entities.append(entityObj.entityCode)
        return entities

    def getMainTypeFromCode(self, context, entityCode):
        """
        Get entity object (mainType) considering given context and code

        :param context: 'asset' or 'shot'
        :type: str
        :param entityCode: Entity code
        :type entityCode: str
        :return: Entity object (mainType)
        :rtype: Entity
        """
        for entityObj in self.contextTree(context):
            if entityObj.entityCode == entityCode:
                return entityObj

    def getData(self, context, recursive=False):
        """
        Get entities data considering given context

        :param context: 'asset' or shot'
        :type context:str
        :param recursive: Recursive state
        :type recursive: bool
        :return: Entities data
        :rtype: dict
        """
        data = dict()
        for n, entityObj in enumerate(self.contextTree(context)):
            data[n] = entityObj.getData(recursive=recursive)
        return data

    def newEntity(self, parent=None, **kwargs):
        """
        Create new entity

        :param parent: Parent entity
        :type parent: Entity
        :param kwargs: Entity data
        :type kwargs: dict
        :return: New entity object
        :rtype: Entity
        """
        #-- Get Entity Objects --#
        if parent is None:
            entityList = self.contextTree(kwargs['entityContext'])
        else:
            if parent.entityType == 'mainType':
                entityList = parent._childs
            else:
                mess = "!!! Entity can not be child of 'subType' entity !!!"
                self.log.error(mess)
                raise AttributeError(mess)
        #-- Check New Entity --#
        for entityObj in entityList:
            #-- Check Entity objects --#
            for attr in ['entityCode', 'entityName']:
                if kwargs[attr] == getattr(entityObj, attr):
                    mess = "!!! Entity %r already exists: %r !!!" % (kwargs['entityCode'], kwargs['entityName'])
                    self.log.error(mess)
                    raise AttributeError(mess)
        #-- Create New Entity --#
        entityObj = Entity(self, parent=parent)
        entityObj.setData(**kwargs)
        #-- Result --#
        return entityObj

    def buildFromSettings(self):
        """
        Populate _groups from settings
        """
        self.log.detail("Build userGroups from settings ...")
        entityDict = pFile.readDictFile(self.settingsFile)
        # self.buildFromDict(grpDict)

    def createSettingsFile(self):
        """
        Create default settings file
        """
        try:
            pFile.writeDictFile(self.settingsFile, {})
            self.log.debug("---> Entities file successfully written: %s" % self.settingsFile)
        except:
            mess = "!!! Can not write entities file: %s !!!" % os.path.basename(self.settingsFile)
            self.log.error(mess)
            raise IOError(mess)
