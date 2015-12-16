import os, pprint
from lib.system import procFile as pFile


class Group(object):
    """
    Group Class: Contains user group datas, child of UserGroups

    :param parent: Parent object
    :type parent: UserGroups
    """

    __attrPrefix__ = 'grp'

    def __init__(self, parent=None):
        self._parent = parent
        self.log = self._parent.log
        #-- Datas --#
        self.grpCode = None
        self.grpName = None
        self.grpGrade = 9
        self.grpColor = None

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
        Get group datas

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
        Set group datas

        :param kwargs: Group datas (key must start with 'grp')
        :type kwargs: dict
        """
        for k, v in kwargs.iteritems():
            if k.startswith(self.__attrPrefix__):
                setattr(self, k, v)


class User(object):
    """
    User Class: Contains user datas, child of UserGroups

    :param userName: User name
    :type userName: str
    :param parent: Parent object
    :type parent: UserGroups
    """

    __attrPrefix__ = 'user'

    def __init__(self, userName, parent=None):
        self._parent = parent
        self.fondation = self._parent.fondation
        self.log = self._parent.log
        #-- Datas --#
        self.userName = userName
        self.userGroup = None
        self.userFirstName = None
        self.userLastName = None

    @property
    def userPrefixFolder(self):
        """
        Get user prefixe folder

        :return: User prefixe folder
        :rtype: str
        """
        return self.userName[0].lower()

    @property
    def userPath(self):
        """
        Get user path

        :return: User path
        :rtype: str
        """
        return pFile.conformPath(os.path.join(self._parent.usersPath, self.userPrefixFolder, self.userName))

    @property
    def userFile(self):
        """
        Get user file full path

        :return: User file full path
        :rtype: str
        """
        return pFile.conformPath(os.path.join(self.userPath, '%s.py' % self.userName))

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
        Get user datas

        :param asString: Return string instead of dict
        :type asString: bool
        :return: User datas
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
        Set user datas

        :param kwargs: User datas (key must start with 'user')
        :type kwargs: dict
        """
        for k, v in kwargs.iteritems():
            if k.startswith(self.__attrPrefix__):
                setattr(self, k, v)

    def setDatasFromUserFile(self):
        """
        Set user datas from userFile
        """
        datas = pFile.readDictFile(self.userFile)
        self.setDatas(**datas)

    def writeFile(self):
        """
        Write user file
        """
        self.log.debug("#--- Write User File: %s ---#" % self.userName)
        #-- Check Path --#
        self.log.detail("Check user path ...")
        self.fondation.createPath(self.userPath, recursive=True, root=self._parent.usersPath)
        #-- Write File --#
        self.log.detail("Write user file ...")
        try:
            pFile.writeDictFile(self.userFile, self.getDatas())
            self.log.debug("---> User file successfully written: %s" % self.userFile)
        except:
            mess = "!!! Can not write userFile: %s !!!" % self.userName
            self.log.error(mess)
            raise IOError(mess)


class UserGroups(object):
    """
    UserGroups Class: Contains groups and users datas, child of Project

    :param fdtObj: Fondation object
    :type fdtObj: Fondation
    :param logLvl : Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """

    log = pFile.Logger(title="UserGrp")
    __usersDir__ = 'users'
    __install__ = False

    def __init__(self, fdtObj, logLvl='info'):
        self.log.level = logLvl
        self.fondation = fdtObj
        #-- Datas --#
        self._user = None
        self._users = []
        self._groups = []
        #-- Update --#
        self._setup()

    def _setup(self):
        """
        Setup UserGroups core object
        """
        self.log.detail("#===== Setup UserGroups Core =====#", newLinesBefore=1)
        #-- Create Tool Paths --#
        self.log.debug("#--- Check Paths ---#")
        if not os.path.exists(self.usersPath):
            self.__install__ = True
            self.fondation.createPath([self.usersPath])
        #-- Check User --#
        self.log.debug("#--- Check User ---#")
        self.collecteUsers(userName=self.fondation.__user__)
        if not self.fondation.__user__ in self.users:
            self.newUser()
        #-- Store User Data --#
        self.log.debug("#--- Store User Datas ---#")
        self._user = self.getUserObjFromName(self.fondation.__user__)

    @property
    def usersPath(self):
        """
        Get users bank path

        :return: Users bank path
        :rtype: str
        """
        return pFile.conformPath(os.path.join(self.fondation.__rootPath__, self.__usersDir__))

    @property
    def users(self):
        """
        Get users name list

        :return: Users name list
        :rtype: list
        """
        userList = []
        for user in self._users:
            userList.append(user.userName)
        return sorted(userList)

    @property
    def groups(self):
        """
        Get groups code list

        :return: Groups code list
        :rtype: list
        """
        grpList = []
        for grp in self._groups:
            grpList.append(grp.grpCode)
        return grpList

    def getGroupsDatas(self, asString=False):
        """
        Get groups datas

        :param asString: Return string instead of dict
        :type asString: bool
        :return: Group datas
        :rtype: dict | str
        """
        grpDict = dict()
        for n, grpObj in enumerate(self._groups):
            grpDict[n] = grpObj.getDatas(asString=asString)
        #-- Result --#
        if asString:
            return pprint.pformat(grpDict)
        return grpDict

    def getUserObjFromName(self, userName):
        """
        Get user object from given userName

        :param userName: User name
        :type userName: str
        :return: User object
        :rtype: User
        """
        for userObj in self._users:
            if userObj.userName == userName:
                return userObj

    def collecteUsers(self, index=None, userName=None, clearUsers=False):
        """
        Collecte Users from disk

        :param index: Letter index
        :type index: str
        :param userName: User name
        :type userName: str
        :param clearUsers: Clear '_users' attribut
        :type clearUsers: bool
        :return: Collected user objects
        :rtype: list
        """
        self.log.debug("Collecting users ...")
        if clearUsers:
            self.log.debug("Clean users list")
            self._users = []
        #-- Collecte Users --#
        userObjects = []
        userList, indexPath = self.parseUsers(index, userName)
        for user in userList:
            userPath = pFile.conformPath(os.path.join(indexPath, user))
            if not user.startswith('_') and os.path.isdir(userPath):
                #-- Remove Existing object --#
                userCheck = self.getUserObjFromName(user)
                if userCheck is not None:
                    self.log.debug("Remove user object: %s" % user)
                    self._users.remove(userCheck)
                #-- Add User Object --#
                userObj = User(user, parent=self)
                userObj.setDatasFromUserFile()
                if user == self.fondation.__user__:
                    self._user = userObj
                self._users.append(userObj)
                userObjects.append(userObj)
                self.log.detail("---> User Object %r added" % user)
        #-- Result --#
        return userObjects

    def parseUsers(self, index, userName):
        """
        Parse disk users directory

        :param index: Letter index
        :type index: str
        :param userName: User name
        :type userName: str
        :return: Users list, index path
        :rtype: list, str
        """
        #-- Get Index List --#
        if index is not None:
            indexList = [index]
        else:
            if userName is not None:
                indexList = userName[0].lower()
            else:
                indexList = os.listdir(self.usersPath) or []
        #-- Collecte Index --#
        userList = []
        indexPath = None
        for index in indexList:
            indexPath = pFile.conformPath(os.path.join(self.usersPath, index))
            if len(index) == 1 and os.path.isdir(indexPath):
                #-- Get User List --#
                if userName is not None:
                    userList = [userName]
                else:
                    userList = os.listdir(indexPath) or []
        #-- Result --#
        return userList, indexPath

    def newUser(self, userName=None, forceUpdate=False):
        """
        Create new user

        :param userName: New user name
        :type userName: str
        :param forceUpdate: Force users or given userName collect
        :type forceUpdate: bool
        :return: User object
        :rtype: User
        """
        #-- Get UserName --#
        if userName is None:
            userName = self.fondation.__user__
        self.log.info("Create New User %r ..." % userName)
        #-- Check UserName --#
        if forceUpdate:
            self.collecteUsers(userName=userName)
        if userName in self.users:
            mess = "!!! UserName %r already exists !!!"
            self.log.error(mess)
            raise AttributeError(mess)
        #-- Add User Object --#
        userObj = User(userName, parent=self)
        if self.__install__:
            self.log.detail("Install mode, %s ---> 'ADMIN'" % userName)
            userObj.userGroup = 'ADMIN'
        userObj.writeFile()
        self._users.append(userObj)
        return userObj

    def newGroup(self, grpCode, **kwargs):
        """
        Create new group
        :param grpCode: Group code
        :type grpCode: str
        :param kwargs: Group datas (key must ends with '_grp')
        :type kwargs: dict
        :return: Group object
        :rtype: Group
        """
        #-- Check GrpName --#
        if grpCode in self.groups:
            mess = "!!! Group code %r already exists !!!" % grpCode
            self.log.error(mess)
            raise AttributeError(mess)
        #-- Create Group --#
        grpObj = Group(parent=self)
        grpObj.setDatas(grpCode=grpCode, **kwargs)
        return grpObj

    def buildGroupsFromSettings(self):
        """
        Populate _groups from settings
        """
        if 'userGroups' in self.fondation.settings.keys():
            if 'groups' in self.fondation.settings['userGroups'].keys():
                self.buildGroupsFromDict(self.fondation.settings['userGroups']['groups'])

    def buildGroupsFromDict(self, grpDict):
        """
        Populate _groups from fiven dict

        :param grpDict: Groups dict
        :type grpDict: dict
        """
        self._groups = []
        for n in sorted(grpDict.keys()):
            newGroup = Group(parent=self)
            newGroup.setDatas(**grpDict[n])
            self._groups.append(newGroup)

    def pushGroupsToSettings(self):
        self.log.debug("Push groups datas to settings ...")
        #-- Refresh Settings --#
        self.log.detail("---> Refresh settings ...")
        self.fondation.storeSettings()
        #-- Check Keys --#
        if not 'userGroups' in self.fondation.settings:
            self.log.detail("---> Add 'userGroups' ...")
            self.fondation.settings['userGroups'] = dict()
        if not 'groups' in self.fondation.settings['userGroups']:
            self.log.detail("---> Add 'groups' to 'userGroups' ...")
            self.fondation.settings['userGroups']['groups'] = dict()
        self.fondation.settings['userGroups']['groups'] = self.getGroupsDatas()
