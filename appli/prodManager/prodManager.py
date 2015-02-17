import os
import appli.prodManager as pm
from lib.system import procFile as pFile


class ProdManager(object):

    def __init__(self, prodId=None, logLvl='info'):
        self._log = pFile.Logger(title="ProdManager", level=logLvl)
        self._log.info("########## ProdManager ##########", newLinesBefor=1)
        self._prodId = prodId
        self.binPath = pm.binPath
        self.project = Project(self)
        if self._prodId is not None:
            self.loadProject()

    def loadProject(self, prodId=None):
        """ Load given project
            :param prodId: Project alias
            :type prodId: str """
        #-- Check ProdId --#
        if prodId is None and self._prodId is None:
            log = "'prodId' and '_prodId' can't be None !!!"
            self._log.error(log)
            raise KeyError, log
        if prodId is None:
            prodId = self._prodId
        self._log.info("Loading project %r ..." % prodId)
        #-- Update Project Alias --#
        self._prodId = prodId
        self.project.alias = self._prodId
        projectFile = self.project.projectFilePath
        #-- Check Project File Attribute --#
        if projectFile is  None:
            log = "Project file attribute failed !!! (%s) !!!" % self._prodId
            self._log.error(log)
            raise KeyError, log
        #-- Check Project File --#
        if not os.path.exists(projectFile):
            log = "Project file not found !!! (%s) !!!" % projectFile
            self._log.error(log)
            raise IOError, log
        #-- Parse Project File --#
        self._log.debug("\t Parse project file ...")
        prodDict = pFile.readPyFile(projectFile)
        self._log.debug("\t Update project params ...")
        self.project.updateParams(prodDict['project'])

    @staticmethod
    def isCleanPath(rootPath, item, checkMode='folder'):
        """ Check type and name of given file or folder path
            :param rootPath: Root path of file or folder to check
            :type rootPath: str
            :param item: File or folder to check
            :type item: str
            :param checkMode: Check mode 'folder' or 'file'
            :type checkMode: str
            :return: Clean path if valid, None if failed
            :rtype: str """
        cleanPath = pFile.conformPath(os.path.join(rootPath, item))
        if checkMode == 'folder':
            if os.path.isdir(cleanPath) and not item.startswith('.') and not item.startswith('_'):
                return cleanPath
        elif checkMode == 'file':
            if os.path.isfile(cleanPath) and not item.startswith('.') and not item.startswith('_'):
                return cleanPath


class Project(object):

    def __init__(self, prodManager):
        self._pm = prodManager
        self._log = self._pm._log
        self.type = None
        self.name = None
        self.alias = None
        self.season = None
        self.episode = None

    @property
    def projectPath(self):
        """ Get project Path
            :return: Project path
            :rtype: str """
        if self.alias is not None:
            return pFile.conformPath(os.path.join(self._pm.binPath, 'prods', self.alias))

    @property
    def projectFile(self):
        """ Get project File
            :return: Project file
            :rtype: str """
        if self.alias is not None:
            return "%s.py" % self.alias

    @property
    def projectFilePath(self):
        """ Get project File absolute path
            :return: Project file absolute path
            :rtype: str """
        if self.projectPath is not None and self.projectFile is not None:
            return pFile.conformPath(os.path.join(self.projectPath, self.projectFile))

    def getParams(self):
        """ Get class params
            :return: Project params
            :rtype: dict """
        classDict = {}
        currentDict = self.__dict__
        for k in currentDict.keys():
            if not k.startswith('_') and not k.startswith('__'):
                classDict[k] = currentDict[k]
        return classDict

    def updateParams(self, projectDict):
        """ Update class params with given projectDict
            :param projectDict: Project params
            :type projectDict: dict """
        for k in projectDict.keys():
            setattr(self, k, projectDict[k])

    def printParams(self):
        """ Print current project params """
        self._log.info("#-- Project params --#")
        params = self.getParams()
        if params is not None:
            for k, v in params.iteritems():
                self._log.info("%s = %s" % (k, v))

    def getAllProjects(self):
        """ Get all projects in data base
            :return: Projects info {'type', 'name', 'alias', 'season', 'episode'}
            :rtype: dict """
        prodsPath = os.path.join(self._pm.binPath, 'prods')
        projectDict = {}
        #-- Parse projects path --#
        for project in os.listdir(prodsPath):
            projectPath = self._pm.isCleanPath(prodsPath, project)
            if projectPath is not None:
                projectFile = pFile.conformPath(os.path.join(projectPath, "%s.py" % project))
                if os.path.exists(projectFile):
                    fileDict = pFile.readPyFile(projectFile)
                    projectDict[fileDict['project']['alias']] = fileDict['project']
        #-- Result --#
        if projectDict.keys():
            return projectDict

    def createNewProject(self, projectDict):
        """ Create new project in data base
            :param projectDict: Project info {'type', 'name', 'alias', 'season', 'episode'}
            :type projectDict: dict """
        if self.checkProjectDict(projectDict):
            projectPath = self.createProjectFolder(projectDict['alias'])
            self.createProjectFile(projectPath, projectDict)
            self.updateParams(projectDict)

    def checkProjectDict(self, projectDict):
        """ Check project Dict values
            :param projectDict: Project params
            :type projectDict: dict
            :return: Check result (True if success)
            :rtype: bool """
        self._log.debug("Check project params ...")
        log = "Attribute is missing in projectDict !!!"
        if projectDict['type'] == 'Movie':
            if projectDict['name'] is None or projectDict['alias'] is None:
                self._log.error(log)
                raise AttributeError, log
            return True
        elif projectDict['type'] == 'Marketing':
            if projectDict['name'] is None or projectDict['alias'] is None or projectDict['season'] is None:
                self._log.error(log)
                raise AttributeError, log
            return True
        elif projectDict['type'] == 'Serie':
            if (projectDict['name'] is None or projectDict['alias'] is None
                or projectDict['season'] is None or projectDict['episode'] is None):
                self._log.error(log)
                raise AttributeError, log
            return True

    def createProjectFolder(self, alias):
        """ Create project folder in data base
            :param alias: Project alias
            :type alias: str
            :return: Project path
            :rtype: str """
        self._log.debug("Create project folder ...")
        projectPath = pFile.conformPath(os.path.join(self._pm.binPath, 'prods', alias))
        if not os.path.exists(projectPath):
            try:
                os.mkdir(projectPath)
                self._log.debug("Create project folder: %s" % alias)
                return projectPath
            except:
                log = "Can not create folder !!! (%s) !!!" % projectPath
                self._log.error(log)
                raise IOError, log
        else:
            log = "Path already exists !!! (%s) !!!" % projectPath
            self._log.error(log)
            raise IOError, log

    def createProjectFile(self, projectPath, projectDict):
        """ Create project file in data base
            :param projectPath: Projet path in data base
            :type projectPath: str
            :param projectDict: Project info
            :type projectDict: dict
            :return: Project file
            :rtype: str """
        self._log.debug("Create project file ...")
        txt = "project = %s" % projectDict
        projectFile = pFile.conformPath(os.path.join(projectPath, "%s.py" % projectDict['alias']))
        if not os.path.exists(projectFile):
            try:
                pFile.writeFile(projectFile, txt)
                self._log.debug("Write project file %s" % projectFile)
                return projectFile
            except:
                log = "Can not write project file !!! (%s) !!!" % projectFile
                self._log.error(log)
                raise IOError, log
        log = "Project file already exists !!! (%s) !!!" % projectFile
        self._log.error(log)
        raise IOError, log
