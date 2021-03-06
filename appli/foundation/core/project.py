import os, pprint
from lib.system import procFile as pFile
from appli.foundation.core import entities


class Project(object):
    """
    Project Class: Contains project datas, child of Foundation

    :param fdnObj: Foundation object
    :type fdnObj: Foundation
    """

    __attrPrefix__ = 'project'

    def __init__(self, fdnObj):
        self.foundation = self.fdn = fdnObj
        self.entities = entities.Entities(self.fdn, self)
        self.log = self.fdn.log
        self.log.title = "Users"
        #-- Datas --#
        self.project = None
        self.projectUsers = []
        self.projectAssets = dict()
        self.projectShots = dict()
        #-- Update --#
        self._setup()

    def _setup(self):
        """
        Setup Project core object
        """
        self.log.info("#===== Setup Project Core =====#", newLinesBefore=1)

    @property
    def projectName(self):
        """
        Get project name

        :return: Project name
        :rtype: str
        """
        if self.project is not None:
            return self.project.split('--')[0]

    @property
    def projectCode(self):
        """
        Get project code

        :return: Project code
        :rtype: str
        """
        if self.project is not None:
            return self.project.split('--')[1]

    @property
    def projectPath(self):
        """
        Get project path

        :return: Project path
        :rtype: str
        """
        if self.project is not None:
            return pFile.conformPath(os.path.join(self.foundation.__projectsPath__, self.project))

    @property
    def projectFile(self):
        """
        Get project file full path

        :return: Project file path
        :rtype: str
        """
        if self.project is not None:
            return pFile.conformPath(os.path.join(self.projectPath, '%s.py' % self.project))

    @property
    def projects(self):
        """
        Get all projects

        :return: Project list
        :rtype: list
        """
        projectList = []
        for fld in os.listdir(self.foundation.__projectsPath__):
            if '--' in fld:
                fldPath = pFile.conformPath(os.path.join(self.foundation.__projectsPath__, fld))
                if os.path.isdir(fldPath):
                    if os.path.exists(pFile.conformPath(os.path.join(fldPath, '%s.py' % fld))):
                        projectList.append(fld)
        return projectList

    @property
    def attributes(self):
        """
        List all attributes

        :return: Attributes
        :rtype: list
        """
        attrs = []
        for key in self.__dict__.keys():
            if key.startswith(self.__attrPrefix__):
                attrs.append(key)
        return attrs

    def getData(self, asString=False):
        """
        Get project datas

        :param asString: Return string instead of dict
        :type asString: bool
        :return: User data
        :rtype: dict | str
        """
        data = dict()
        for attr in self.attributes:
            data[attr] = getattr(self, attr)
        #-- Result --#
        if asString:
            return pprint.pformat(data)
        return data

    def setData(self, **kwargs):
        """
        Set project data

        :param kwargs: Project data (key must start with 'project')
        :type kwargs: dict
        """
        for k, v in kwargs.iteritems():
            if k.startswith(self.__attrPrefix__):
                if k in self.attributes:
                    setattr(self, k, v)
                else:
                    self.log.warning("!!! Unrecognized attribute: %s. Skip !!!" % k)

    def createNewProject(self, projectName, projectCode):
        """
        Create new project

        :param projectName: Project name
        :type projectName: str
        :param projectCode: Project code
        :type projectCode: str
        """
        self.log.info("#--- Create New Project ---#")
        self.log.info("Project Name: %s" % projectName)
        self.log.info("Project Code: %s" % projectCode)
        #-- Check New Project --#
        if '%s--%s' % (projectName, projectCode) in self.projects:
            mess = "Project already exists: %s--%s" % (projectName, projectCode)
            self.log.error(mess)
            raise AttributeError(mess)
        #-- Create Project Folder --#
        newProjectPath = pFile.conformPath(os.path.join(self.foundation.__projectsPath__,
                                                        '%s--%s' % (projectName, projectCode)))
        pFile.createPath([newProjectPath])
        #-- Create Project File --#
        projFile = pFile.conformPath(os.path.join(newProjectPath, '%s--%s.py' % (projectName, projectCode)))
        projDict = {'project': "%s--%s" % (projectName, projectCode), 'projectUsers': [self.foundation.__user__]}
        try:
            pFile.writeDictFile(projFile, projDict)
            self.log.debug("---> Project file successfully written: %s" % projFile)
        except:
            mess = "!!! Can not write project file: %s !!!" % projFile
            self.log.error(mess)
            raise IOError(mess)

    def loadProject(self, project):
        """
        Load given project

        :param project: Project (name--code)
        :type project: str
        """
        self.log.info("#--- Load Project: %r ---#" % project)
        #-- Check Project --#
        projectFile = pFile.conformPath(os.path.join(self.fdn.__projectsPath__, project, '%s.py' % project))
        if not os.path.exists(projectFile):
            mess = "!!! Project %r not found !!!" % project
            self.log.error(mess)
            raise ValueError(mess)
        #-- Get Project --#
        try:
            projectDict = pFile.readDictFile(projectFile)
        except:
            mess = "!!! Can not load project %r !!!" % project
            self.log.error(mess)
            raise IOError(mess)
        #-- Load Project --#
        if self.fdn.users._user.userName in projectDict['projectUsers']:
            self.setData(**projectDict)
            # self.entities.resetContextTree('asset')
            # self.entities.updateEntitiesFromDict('asset', self.projectAssets)
            # self.entities.resetContextTree('shot')
            # self.entities.updateEntitiesFromDict('shot', self.projectShots)
            self.log.info("---> Project %r successfully loaded" % project)
        else:
            mess = "User %r is not set as projectUser in %s !" % (self.foundation.userGroups._user.userName, project)
            self.log.warning(mess)
            raise ValueError(mess)

    def writeProject(self):
        """
        Write project file
        """
        self.log.debug("#--- Write Project File: %s ---#" % self.project)
        try:
            pFile.writeDictFile(self.projectFile, self.getData())
            self.log.debug("---> Project file successfully written: %s" % self.projectFile)
        except:
            mess = "!!! Can not write projectFile: %s !!!" % self.projectFile
            self.log.error(mess)
            raise IOError(mess)

    def addProjectUser(self, userName):
        """
        Add project user (watcher)

        :param userName: User name
        :type userName: str
        """
        if not userName in self.projectUsers:
            self.projectUsers.append(userName)
            self.log.detail("User %r added to project %r" % (userName, self.project))

    def removeProjectUser(self, userName):
        """
        Remove project user (watcher)

        :param userName: User name
        :type userName: str
        """
        if userName in self.projectUsers:
            self.projectUsers.remove(userName)
            self.log.detail("User %r removed from project %r" % (userName, self.project))
