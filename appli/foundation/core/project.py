import os, pprint
from lib.system import procFile as pFile


class Project(object):
    """
    Project Class: Contains project datas, child of Foundation

    :param foundationObj: Foundation object
    :type foundationObj: Foundation
    """

    __attrPrefix__ = 'project'

    def __init__(self, foundationObj):
        self.foundation = foundationObj
        self.log = self.foundation.log
        self.log.title = 'Project'
        #-- Datas --#
        self.project = None
        self.projectUsers = []
        #-- Update --#
        self._setup()

    def _setup(self):
        """
        Setup Project core object
        """
        self.log.info("#===== Setup Project Core =====#", newLinesBefore=1)

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
    def projectFile(self):
        """
        Get project file full path

        :return: Project file path
        :rtype: str
        """
        if self.project is not None:
            return pFile.conformPath(os.path.join(self.foundation.__projectsPath__,
                                                  self.project, '%s.py' % self.project))

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

    def getDatas(self, asString=False):
        """
        Get project datas

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
        Set project datas

        :param kwargs: Project datas (key must start with 'project')
        :type kwargs: dict
        """
        for k, v in kwargs.iteritems():
            if k.startswith(self.__attrPrefix__):
                if k in self.attributes:
                    setattr(self, k, v)
                else:
                    self.log.warning("!!! Unrecognized attribute: %s. Skipp !!!" % k)

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
        self.foundation.createPath([newProjectPath])
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
        projectFile = pFile.conformPath(os.path.join(self.foundation.__projectsPath__, project, '%s.py' % project))
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
        if self.foundation.userGroups._user.userName in projectDict['projectUsers']:
            self.setDatas(**projectDict)
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
            pFile.writeDictFile(self.projectFile, self.getDatas())
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
            print self.projectUsers
