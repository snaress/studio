import os
import pprint
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
                if k in self.attributes:
                    setattr(self, k, v)
                else:
                    self.log.warning("!!! Unrecognized attribute: %s. Skipp !!!" % k)


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
        self.foundation = self._parent.foundation
        self.log = self._parent.log
        #-- Datas --#
        self.userName = userName
        self.userGroup = None
        self.userFirstName = None
        self.userLastName = None
        self.userRecentProjects = []
        self.userPinedProjects = []

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

    @property
    def grade(self):
        """
        Get user grade

        :return: User grade
        :rtype: int
        """
        if self.userGroup is not None:
            grpObj = self._parent.getGroupObjFromCode(self.userGroup)
            if grpObj is not None:
                return grpObj.grpGrade

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
                if k in self.attributes:
                    setattr(self, k, v)
                else:
                    self.log.warning("!!! Unrecognized attribute: %s. Skipp !!!" % k)

    def setDatasFromUserFile(self):
        """
        Set user datas from userFile
        """
        datas = pFile.readDictFile(self.userFile)
        self.setDatas(**datas)

    def addPinedProject(self, project):
        """
        Add given project to pinedProjects

        :param project: Project (name--code)
        :type project: str
        """
        if not project in self.userPinedProjects:
            self.userPinedProjects.append(project)
            self.log.info("%r added to pinProjects" % project)
        else:
            mess = "!!! Project %r already in pinedProjects, Skipp !!!" % project
            self.log.warning(mess)
            raise ValueError(mess)

    def delPinedProject(self, project):
        """
        Remove given project from pinedProjects

        :param project: Project (name--code)
        :type project: str
        """
        if project in self.userPinedProjects:
            self.userPinedProjects.remove(project)
            self.log.info("%r removed from pinedProjects" % project)
        else:
            mess = "!!! %r not found, Skipp !!!" % project
            self.log.warning(mess)
            raise ValueError(mess)

    def writeFile(self):
        """
        Write user file
        """
        self.log.debug("#--- Write User File: %s ---#" % self.userName)
        #-- Check Path --#
        self.log.detail("Check user path ...")
        self.foundation.createPath(self.userPath, recursive=True, root=self._parent.usersPath)
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
    UserGroups Class: Contains groups and users datas, child of Foundation

    :param foundationObj: Foundation object
    :type foundationObj: Foundation
    """

    __usersDir__ = 'users'
    __archiveDir__ = '_archive'
    __install__ = False

    def __init__(self, foundationObj):
        self.foundation = foundationObj
        self.log = self.foundation.log
        self.log.title = 'UserGroups'
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
        self.log.info("#===== Setup UserGroups Core =====#", newLinesBefore=1)
        #-- Create Tool Paths --#
        self.log.debug("#--- Check Paths ---#")
        if not os.path.exists(self.usersPath):
            self.__install__ = True
            self.foundation.createPath([self.usersPath, self.archivePath])
        #-- Check UserGroups File --#
        self.log.debug("#--- Check UserGroups File ---#")
        if not os.path.exists(self.userGroupsFile):
            self.createUserGroupFile()
        self.buildGroupsFromSettings()
        #-- Check User --#
        self.log.debug("#--- Check User ---#")
        self.collecteUsers(userName=self.foundation.__user__)
        if not self.foundation.__user__ in self.users:
            self.newUser()
            #-- Store User Data --#
            self.log.debug("#--- Store User Datas ---#")
            self._user = self.getUserObjFromName(self.foundation.__user__)

    @property
    def usersPath(self):
        """
        Get users path

        :return: Users path
        :rtype: str
        """
        return pFile.conformPath(os.path.join(self.foundation.__settingsPath__, self.__usersDir__))

    @property
    def archivePath(self):
        """
        Get archive path

        :return: Archive path
        :rtype: str
        """
        return pFile.conformPath(os.path.join(self.usersPath, self.__archiveDir__))

    #======================================= GROUPS ========================================#

    @property
    def userGroupsFile(self):
        """
        Get userGroups file full path

        :return: userGroups file full path
        :rtype: str
        """
        return pFile.conformPath(os.path.join(self.usersPath, 'userGroups.py'))

    @property
    def defaultGroups(self):
        """
        Get default user groups

        :return: User groups param
        :rtype: dict
        """
        return {0: {'grpCode': 'ADMIN', 'grpName': 'Administrator', 'grpGrade': 0, 'grpColor': (255, 0, 0)},
                1: {'grpCode': 'VST', 'grpName': 'Visitor', 'grpGrade': 9, 'grpColor': (0, 0, 255)}}

    @property
    def groupsCode(self):
        """
        Get groups code list

        :return: Groups code list
        :rtype: list
        """
        grpList = []
        for grp in self._groups:
            grpList.append(grp.grpCode)
        return grpList

    @property
    def groupsName(self):
        """
        Get groups name list

        :return: Groups name list
        :rtype: list
        """
        grpList = []
        for grp in self._groups:
            grpList.append(grp.grpName)
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

    def getGroupObjFromCode(self, groupCode):
        """
        Get group object from given groupCode

        :param groupCode: Group code
        :type groupCode: str
        :return: Group object
        :rtype: Group
        """
        for grpObj in self._groups:
            if grpObj.grpCode == groupCode:
                return grpObj

    def getGroupObjFromName(self, groupName):
        """
        Get group object from given groupName

        :param groupName: Group name
        :type groupName: str
        :return: Group object
        :rtype: Group
        """
        for grpObj in self._groups:
            if grpObj.grpName == groupName:
                return grpObj

    def createUserGroupFile(self):
        """
        Create default user group file
        """
        try:
            pFile.writeDictFile(self.userGroupsFile, self.defaultGroups)
            self.log.debug("---> User groups file successfully written: %s" % self.userGroupsFile)
        except:
            mess = "!!! Can not write user groups file: %s !!!" % os.path.basename(self.userGroupsFile)
            self.log.error(mess)
            raise IOError(mess)

    def newGroup(self, grpCode, **kwargs):
        """
        Create new group

        :param grpCode: Group code
        :type grpCode: str
        :param kwargs: Group datas (key must starts with 'grp')
        :type kwargs: dict
        :return: Group object
        :rtype: Group
        """
        #-- Check GrpName --#
        if grpCode in self.groupsCode:
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
        self.log.detail("Build user groups from settings ...")
        grpDict = pFile.readDictFile(self.userGroupsFile)
        self.buildGroupsFromDict(grpDict)

    def buildGroupsFromDict(self, grpDict):
        """
        Populate _groups from given dict

        :param grpDict: Groups dict
        :type grpDict: dict
        """
        self.log.detail("Build user groups from grpDict ...")
        self._groups = []
        for n in sorted(grpDict.keys()):
            newGroup = Group(parent=self)
            newGroup.setDatas(**grpDict[n])
            self._groups.append(newGroup)

    def writeGroupsToSettings(self):
        """
        Write userGroups to settings file
        """
        self.log.debug("#--- Write UserGroups File ---#")
        try:
            pFile.writeDictFile(self.userGroupsFile, self.getGroupsDatas())
            self.log.debug("---> UserGroup file successfully written: %s" % self.userGroupsFile)
        except:
            mess = "!!! Can not write userGroups file: %s !!!" % self.userGroupsFile
            self.log.error(mess)
            raise IOError(mess)

    #======================================= USERS =========================================#

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
        :param clearUsers: Clear '_users' attribute
        :type clearUsers: bool
        :return: Collected user objects
        :rtype: list
        """
        self.log.debug("Collecting users ...")
        #-- Clear Users --#
        if clearUsers:
            self.log.detail("Clear users list")
            self._users = []
        #-- Collecte Users --#
        userObjects = []
        userList = self.parseUsers(index, userName)
        for user in userList:
            userPath = pFile.conformPath(os.path.join(self.usersPath, user[0].lower(), user))
            if not user.startswith('_') and os.path.isdir(userPath):
                #-- Remove Existing object --#
                userCheck = self.getUserObjFromName(user)
                if userCheck is not None:
                    self.log.debug("Remove user object: %s" % user)
                    self._users.remove(userCheck)
                #-- Add User Object --#
                userObj = User(user, parent=self)
                userObj.setDatasFromUserFile()
                if user == self.foundation.__user__:
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
        :return: Users list
        :rtype: list
        """
        self.log.detail("Parse disk ...")
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
        for index in indexList:
            indexPath = pFile.conformPath(os.path.join(self.usersPath, index))
            if len(index) == 1 and os.path.isdir(indexPath):
                #-- Get User List --#
                if userName is not None:
                    userList = [userName]
                else:
                    userList.extend(os.listdir(indexPath) or [])
        #-- Result --#
        return userList

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
            userName = self.foundation.__user__
        self.log.info("Create New User %r ..." % userName)
        #-- Check UserName --#
        if forceUpdate:
            self.collecteUsers(userName=userName)
        if userName in self.users:
            mess = "!!! UserName %r already exists !!!" % userName
            self.log.error(mess)
            raise AttributeError(mess)
        #-- Add User Object --#
        userObj = User(userName, parent=self)
        if self.__install__:
            self.log.detail("Install mode, %s ---> 'ADMIN'" % userName)
            userObj.setDatas(userGroup='ADMIN')
            userObj.writeFile()
        self._users.append(userObj)
        return userObj

    def deleteUser(self, userName):
        """
        Delete given user

        :param userName: User name
        :type userName: str
        """
        userObj = self.getUserObjFromName(userName)
        #-- Check User Object --#
        if userObj is None:
            mess = "!!! User not found: %s !!!" % userName
            self.log.error(mess)
            raise AttributeError(mess)
        #-- Delete User --#
        self.log.info("Deleting User %s ..." % userName)
        self._users.remove(userObj)
        #ToDo: Move user folder to archive
        self.log.info("---> %s deleted." % userName)
