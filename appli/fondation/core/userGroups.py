import os, pprint
from lib.system import procFile as pFile


class User(object):
    """
    User Class: Contains user datas, child of UserGroups

    :param userName: User name
    :type userName: str
    :param parent: Parent object
    :type parent: UserGroups
    """

    def __init__(self, userName, parent=None):
        self.parent = parent
        self.log = self.parent.log
        self.userName = userName
        self.userGroup = None
        self.userFirstName = None
        self.userLastName = None

    @property
    def userPath(self):
        """
        Get user path

        :return: User path
        :rtype: str
        """
        return pFile.conformPath(os.path.join(self.parent.bankPath, self.userName[0].lower(), self.userName))

    @property
    def userFile(self):
        return pFile.conformPath(os.path.join(self.userPath, '%s.py' % self.userName))

    def getDatas(self, asString=False):
        """
        Get user datas

        :param asString: Return string instead of dict
        :type asString: bool
        :return: User datas
        :rtype: dict | str
        """
        datas = dict()
        for k, v in self.__dict__.iteritems():
            if k.startswith('user'):
                datas[k] = v
        if asString:
            return pprint.pformat(datas)
        return datas

    def setDatas(self, datas=None, fromUserFile=False):
        """
        Set user datas

        :param datas: Datas dict to use if not using userFile
        :type datas: dict
        :param fromUserFile: Use userFile instead of given datas
        :type fromUserFile: bool
        """
        #-- Get Datas From File --#
        if fromUserFile:
            datas = pFile.readPyFile(self.userFile)
        #-- Set Datas --#
        if datas is not None:
            for k, v in datas.iteritems():
                setattr(self, k, v)
        else:
            self.log.warning("!!! Datas can not be None, setDatas command skipped: %s !!!" % self.userName)

    def writeFile(self):
        """
        Write user file
        """
        self.log.debug("#--- Write User File: %s ---#" % self.userName)
        #-- Translate Datas --#
        self.log.detail("Translate datas ...")
        txt = []
        for k, v in self.getDatas().iteritems():
            if isinstance(v, str):
                txt.append("%s = %r" % (k, v))
            else:
                txt.append("%s = %s" % (k, v))
        #-- Check Path --#
        self.log.detail("Check user path ...")
        self.parent.fondation.createPath(self.userPath, recursive=True, root=self.parent.bankPath)
        #-- Write File --#
        self.log.detail("Write user file ...")
        try:
            pFile.writeFile(self.userFile, '\n'.join(txt))
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
    __bankDir__ = 'users'

    def __init__(self, fdtObj, logLvl='info'):
        self.log.level = logLvl
        self.fondation = fdtObj
        self._users = []
        self._user = None
        self.groups = dict()
        self._setup()

    def _setup(self):
        """
        Setup UserGroups core object
        """
        self.log.detail("#===== Setup UserGroups Core =====#", newLinesBefor=1)
        #-- Create Tool Paths --#
        self.log.debug("#--- Check Paths ---#")
        instal = False
        if not os.path.exists(self.bankPath):
            instal = True
            self.fondation.createPath([self.bankPath])
        #-- Check User --#
        self.log.debug("#--- Check User ---#")
        self.collecteUsers(userName=self.fondation.__user__)
        if not self.fondation.__user__ in self.users:
            self.createNewUser(instal=instal)
        #-- Store User Data --#
        self.log.debug("#--- Store User Datas ---#")
        self._user = self.getUserObjFromName(self.fondation.__user__)

    @property
    def bankPath(self):
        """
        Get users bank path

        :return: Users bank path
        :rtype: str
        """
        return pFile.conformPath(os.path.join(self.fondation.__bankPath__, self.__bankDir__))

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
        :param clearUsers: Clear '_users' attribut
        :type clearUsers: bool
        :return: Collected user objects
        :rtype: list
        """
        self.log.debug("Collecting users ...")
        if clearUsers:
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
                userObj.setDatas(fromUserFile=True)
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
                indexList = os.listdir(self.bankPath) or []
        #-- Collecte Index --#
        userList = []
        indexPath = None
        for index in indexList:
            indexPath = pFile.conformPath(os.path.join(self.bankPath, index))
            if len(index) == 1 and os.path.isdir(indexPath):
                #-- Get User List --#
                if userName is not None:
                    userList = [userName]
                else:
                    userList = os.listdir(indexPath) or []
        #-- Result --#
        return userList, indexPath

    def createNewUser(self, userName=None, forceUpdate=False, instal=False):
        """
        Create new user

        :param userName: New user name
        :type userName: str
        :param forceUpdate: Force users or given userName collect
        :type forceUpdate: bool
        :param instal: Fondation first instal, user will be in 'admin' group
        :type instal: bool
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
        if instal:
            self.log.detail("Install mode, %s ---> 'ADMIN'" % userName)
            userObj.userGroup = 'ADMIN'
        userObj.writeFile()
        self._users.append(userObj)
        return userObj

