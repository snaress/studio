import os
import appli.prodManager as pm
from lib.system import procFile as pFile


class ProdManager(object):
    """ ProdManager main class
        :param prodId: Project alias
        :type prodId: str
        :param logLvl: Print log level
        :type logLvl: str """

    def __init__(self, prodId=None, logLvl='info'):
        self._log = pFile.Logger(title="ProdManager", level=logLvl)
        self._log.info("########## ProdManager ##########", newLinesBefor=1)
        self._prodId = prodId
        self.binPath = pm.binPath
        self.project = Project(self)
        self.trees = Trees(self)
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
        self.project.setParam('alias', self._prodId)
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
        self.project.updateParams(prodDict)
        self.trees._initParams()

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
    """ ProdManager subClass: Project params
        :param prodManager: PrdManager main class
        :type prodManager: ProdManager """

    def __init__(self, prodManager):
        self._pm = prodManager
        self._log = self._pm._log
        self._log.info("#-- Project Class --#")
        self._projectKeys = ['type', 'name', 'alias', 'season', 'episode']
        self.type = None
        self.name = None
        self.alias = None
        self.season = None
        self.episode = None
        self.rootPath = None
        self.tasks = None
        self.trees = None
        self.steps = None
        self._log.debug("--> Done")

    @property
    def projectPath(self):
        """ Get project Path
            :return: Project path
            :rtype: str """
        if self.alias is not None:
            return pFile.conformPath(os.path.join(self._pm.binPath, 'prods', self.alias))

    @property
    def dataPath(self):
        """ Get project data path
            :return: Project data path
            :rtype: str """
        if self.projectPath is not None:
            return pFile.conformPath(os.path.join(self.projectPath, 'data'))

    @property
    def treePath(self):
        """ Get project tree path
            :return: Project tree path
            :rtype: str """
        if self.projectPath is not None:
            return pFile.conformPath(os.path.join(self.projectPath, 'tree'))

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

    def paramsToTxt(self):
        """ Convert params dict to text lines
            :return: Params text lines
            :rtype: list """
        txt = []
        for k, v in sorted(self.getParams().iteritems()):
            if isinstance(v, str):
                txt.append("%s = %r" % (k, v))
            else:
                txt.append("%s = %s" % (k, v))
        return txt

    def updateParams(self, projectDict):
        """ Update class params with given projectDict
            :param projectDict: Project params
            :type projectDict: dict """
        self._log.info("#-- Update project params --#")
        for k in projectDict.keys():
            self._log.debug("\t Updating %s" % k)
            setattr(self, k, projectDict[k])

    def setParam(self, param, value):
        """ Set given class params with given value
            :param param: Param name to set
            :type param: str
            :param value: Param value
            :type value: str | list """
        if param in self.getParams().keys():
            self._log.debug("Set project param '%s'" % param)
            setattr(self, param, value)
        else:
            log = "Param '%s' not found !!!" % param
            self._log.error(log)
            raise KeyError, log

    def printParams(self):
        """ Print current project params """
        self._log.info("########## PROJECT PARAMS ##########", newLinesBefor=1)
        txt = self.paramsToTxt()
        print '\n'.join(txt)

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
                    projectDict[fileDict['alias']] = {}
                    for k in self._projectKeys:
                        projectDict[fileDict['alias']][k] = fileDict[k]
        #-- Result --#
        if projectDict.keys():
            return projectDict

    def printAllProject(self):
        """ Print all projects in data base """
        self._log.info("########## PRODMANAGER PROJECT LIST ##########", newLinesBefor=1)
        projectsDict = self.getAllProjects()
        for project in sorted(projectsDict.keys()):
            txt = ["#-- %s --#" % project]
            for k in self._projectKeys:
                txt.append("%s = %r" % (k, projectsDict[project][k]))
            txt.append("")
            print '\n'.join(txt)

    def createNewProject(self, projectDict):
        """ Create new project in data base
            :param projectDict: Project info {'type', 'name', 'alias', 'season', 'episode'}
            :type projectDict: dict
            :return: Project file absolute path
            :rtype: str """
        if self._checkProjectDict(projectDict):
            projectPath = self._createProjectFolder(projectDict['alias'])
            self.updateParams(projectDict)
            projectFile = self._createProjectFile(projectPath, projectDict)
            self._log.info("Project succesfully created: %s" % projectFile)
            return projectFile

    def _checkProjectDict(self, projectDict):
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

    def _createProjectFolder(self, alias):
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
                for fld in ['data', 'tree']:
                    flpPath = pFile.conformPath(os.path.join(projectPath, fld))
                    os.mkdir(flpPath)
                    self._log.debug("Create project folder: %s/%s" % (alias, fld))
                return projectPath
            except:
                log = "Can not create folder !!! (%s) !!!" % projectPath
                self._log.error(log)
                raise IOError, log
        else:
            log = "Path already exists !!! (%s) !!!" % projectPath
            self._log.error(log)
            raise IOError, log

    def _createProjectFile(self, projectPath, projectDict):
        """ Create project file
            :param projectPath: Projet path in data base
            :type projectPath: str
            :param projectDict: Project info
            :type projectDict: dict
            :return: Project file if success
            :rtype: str """
        self._log.debug("Create project file ...")
        txt = self.paramsToTxt()
        projectFile = pFile.conformPath(os.path.join(projectPath, "%s.py" % projectDict['alias']))
        if not os.path.exists(projectFile):
            return self.writeProjectFile(projectFile, txt)
        else:
            log = "Project file already exists !!! (%s) !!!" % projectFile
            self._log.error(log)
            raise IOError, log

    def saveSettings(self):
        """ Save project settings to file
            :return: Project file if success
            :rtype: str """
        self._log.debug("Save project settings ...")
        txt = self.paramsToTxt()
        projectFile = self.projectFilePath
        if projectFile is not None:
            if os.path.exists(projectFile):
                return self.writeProjectFile(projectFile, txt)
            else:
                log = "Can not save settings, project file not found !!! (%s) !!!" % projectFile
                self._log.error(log)
                raise IOError, log

    def writeProjectFile(self, projectFile, txt):
        """ Write project setings in data base
            :param projectFile: Project file absolute path
            :type projectFile: str
            :param txt: Text lines to write
            :type txt: list
            :return: Project file if success
            :rtype: str """
        try:
            pFile.writeFile(projectFile, '\n'.join(txt))
            self._log.debug("Write project file %s" % projectFile)
            return projectFile
        except:
            log = "Can not write project file !!! (%s) !!!" % projectFile
            self._log.error(log)
            raise IOError, log


class Trees(object):
    """ ProdManager subClass: Trees params
        :param prodManager: PrdManager main class
        :type prodManager: ProdManager """

    def __init__(self, prodManager):
        self._pm = prodManager
        self._log = self._pm._log
        self._log.info("#-- Trees Class --#")
        self._project = self._pm.project
        self._treeNames = []
        self._log.debug("--> Done")

    def _initParams(self):
        """ Update class params with given treeDict """
        self._log.info("#-- Init trees params --#")
        if self._project.trees is not None:
            for n in self._project.trees.keys():
                treeName = self._project.trees[n].keys()[0]
                treeType = self._project.trees[n][treeName]
                self._log.debug("\t Init %s tree" % treeName)
                self._treeNames.append(treeName)
                if not os.path.exists(self.getTreeFile(treeName)):
                    setattr(self, treeName, Tree(self, treeName, treeType))

    def getParams(self):
        """ Get class params
            :return: Trees params
            :rtype: dict """
        treesDict = {}
        for tree in self._treeNames:
            treeObj = getattr(self, tree)
            treesDict[tree] = treeObj.getParams()
        return treesDict

    def getTreeFile(self, treeName):
        """ Get tree file path
            :param treeName: Tree name
            :type treeName: str
            :return: Tree file path
            :rtype: str """
        if self._project.dataPath is not None:
            return pFile.conformPath(os.path.join(self._project.dataPath, '%s.py' % treeName))


class Tree(object):
    """ Trees subClass: Tree params
        :param parent: Trees class
        :type parent: Trees
        :param treeName: Tree name
        :type treeName: str
        :param treeType: Tree type ('asset', 'shot', 'shooting', 'other')
        :type treeType: str
        :param treeContents: Tree hierarchy
        :type treeContents: dict """

    def __init__(self, parent, treeName, treeType, treeContents=None):
        self._parent = parent
        self._pm = self._parent._pm
        self._log = self._pm._log
        self._project = self._pm.project
        self.name = treeName
        self.type = treeType
        self.tree = treeContents

    @property
    def treeFile(self):
        """ Get tree file path
            :return: Tree file path
            :rtype: str """
        return self._parent.getTreeFile(self.name)

    def getParams(self):
        """ Get class params
            :return: Tree params
            :rtype: dict """
        treeDict = {}
        for k, v in self.__dict__.iteritems():
            if not k.startswith('_') and not k.startswith('__'):
                treeDict[k] = v
        return treeDict
