import pprint


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
        if self._parent is not None:
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

    def getDatas(self, recursive=False, asString=False):
        """
        Get Entity datas

        :param recursive: Recursive state
        :type recursive: bool
        :param asString: Return string instead of dict
        :type asString: bool
        :return: Entity datas
        :rtype: dict | str
        """
        datas = dict()
        for attr in self.attributes:
            datas[attr] = getattr(self, attr)
            if recursive:
                if self._childs is not None:
                    datas['childs'] = dict()
                    for c , childObj in enumerate(self._childs):
                        datas['childs'][c] = childObj.getDatas(recursive=False)
        if asString:
            return pprint.pformat(datas)
        return datas

    # noinspection PyUnresolvedReferences
    def setDatas(self, **kwargs):
        """
        Set entity datas

        :param kwargs: Entity datas (key must start with 'entity')
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
    Entity Class: Class Contains entity datas, child of Entities

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
        #-- Datas --#
        self.entityContext = None
        self.entityType = None
        self.entityCode = None
        self.entityName = None
        self.entityLabel = None
        self.entityFolder = None

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


class Asset(EntityNode):

    __attrPrefix__ = 'asset'

    def __init__(self, entitiesObj, parent=None):
        super(Asset, self).__init__(entitiesObj, parent=parent)
        self.nodeType = 'asset'
        #-- Datas --#
        self.assetType = None
        self.assetSubType = None
        self.assetName = None


class Shot(EntityNode):

    __attrPrefix__ = 'shot'

    def __init__(self, entitiesObj, parent=None):
        super(Shot, self).__init__(entitiesObj, parent=parent)
        self.nodeType = 'shot'


class Entities(object):
    """
    Entities Class: Contains entities datas, child of Foundation

    :param foundationObj: Foundation object
    :type foundationObj: Foundation
    :param projectObj: Foundation Project object
    :type projectObj: Project
    """

    __assetsDir__ = "assets"
    __shotsDir__ = "shots"

    def __init__(self, foundationObj, projectObj):
        self.foundation = foundationObj
        self.project = projectObj
        self.log = self.foundation.log
        self.log.title = 'Entities'
        #-- Datas --#
        self._assets = []
        self._shots = []
        #-- Update --#
        self._setup()

    def _setup(self):
        """
        Setup Entities core object
        """
        self.log.info("#===== Setup Entities Core =====#", newLinesBefore=1)

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

    def getDatas(self, context, recursive=False):
        """
        Get entities datas considering given context

        :param context: 'asset' or shot'
        :type context:str
        :param recursive: Recursive state
        :type recursive: bool
        :return: Entities datas
        :rtype: dict
        """
        datas = dict()
        for n, entityObj in enumerate(self.contextTree(context)):
            datas[n] = entityObj.getDatas(recursive=recursive)
        return datas

    def newEntity(self, parent=None, **kwargs):
        """
        Create new entity

        :param parent: Parent entity
        :type parent: Entity
        :param kwargs: Entity datas
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
        entityObj.setDatas(**kwargs)
        #-- Result --#
        return entityObj

    def updateEntitiesFromDict(self, context, entityDict):
        """
        Populate entities from given dict considering given context

        :param context: 'asset' or 'shot'
        :type context: str
        :param entityDict: Entity dict
        :type entityDict: dict
        """
        self.log.detail("Build %s entities from entityDict ..." % context)
        #-- Add MainTypes --#
        for n, datas in sorted(entityDict.iteritems()):
            if not datas['entityCode'] in self.mainTypes(context):
                entityObj = self.newEntity(**datas)
                self.contextTree(context).insert(n, entityObj)
            else:
                entityObj = self.getMainTypeFromCode(context, datas['entityCode'])
                if entityObj is not None:
                    entityObj.setDatas(**datas)
                else:
                    self.log.warning("!!! Entity not found: %r. skip update !!!" % datas['entityCode'])
            #-- Add SubTypes --#
            for c, childDatas in sorted(datas['childs'].iteritems()):
                if not childDatas['entityCode'] in entityObj.subTypes:
                    subEntityObj = self.newEntity(**childDatas)
                    entityObj._childs.insert(c, subEntityObj)
                else:
                    subEntityObj = entityObj.getSubTypeFromCode(datas['childs'][c]['entityCode'])
                    if subEntityObj is not None:
                        subEntityObj.setDatas(**childDatas)
                    else:
                        self.log.warning("!!! Entity not found: %r. skip update !!!" % datas['childs'][c]['entityCode'])

    def updateProject(self, context):
        """
        Update project with current entities

        :param context: 'asset' or shot'
        :type context:str
        """
        if context == 'asset':
            self.project.projectAssets = self.getDatas(context, recursive=True)
        elif context == 'shot':
            self.project.projectShots = self.getDatas(context, recursive=True)

    #======================================= ASSETS =========================================#
