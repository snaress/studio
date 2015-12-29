import os
from lib.system import procFile as pFile
from appli.fondation.core import userGroups, entities


class Fondation(object):
    """
    Fondation Class: Contains fondation datas, main core object

    :param logLvl : Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """

    log = pFile.Logger(title="Fondation")
    __user__ = os.environ['USERNAME']
    __rootPath__ = "E:/fondation"
    __prodsPath__ = pFile.conformPath(os.path.join(__rootPath__, 'prods'))
    __settingsPath__ = pFile.conformPath(os.path.join(__rootPath__, 'settings'))

    def __init__(self, logLvl='info'):
        self.log.level = logLvl
        self.log.info("########## Launching Fondation ##########", newLinesBefore=1)
        self.settings = dict()
        self._setup()
        self.userGrps = userGroups.UserGroups(self, logLvl=self.log.level)
        self.entities = entities.Entities(self, logLvl=self.log.level)

    def _setup(self):
        """
        Setup Fondation core object
        """
        self.log.detail("#===== Setup Fondation Core =====#", newLinesBefore=1)
        #-- Create Tool Paths --#
        self.log.debug("#--- Check Paths ---#")
        self.createPath([self.__rootPath__, self.__prodsPath__, self.__settingsPath__])
        #-- Check Settings File --#
        if not os.path.exists(self.settingsFile):
            self.createDefaultSettingsFile()
        self.storeSettings()

    @property
    def settingsFile(self):
        """
        Get Fondation settings file

        :return: Fondation settings file
        :rtype: str
        """
        return pFile.conformPath(os.path.join(self.__settingsPath__, 'fondationSettings.py'))

    def storeSettings(self):
        """
        Store Fondation settings from file

        :return: Fondation settings
        :rtype: dict
        """
        self.settings = pFile.readDictFile(self.settingsFile)

    def writeSettings(self):
        """
        Write settings file
        """
        self.log.debug("Writing settings file ...")
        #-- Write File --#
        try:
            pFile.writeDictFile(self.settingsFile, self.settings)
            self.log.debug("---> Settings file successfully written: %s" % self.settingsFile)
        except:
            mess = "!!! Can not write settingsFile: %s !!!" % self.settingsFile
            self.log.error(mess)
            raise IOError(mess)

    def createDefaultSettingsFile(self):
        """
        Create Fondation settings file
        """
        self.log.detail("Write settings file ...")
        datasDict = {'userGroups': {'groups': {0: {'grpCode': 'ADMIN',
                                                   'grpName': 'Administrator',
                                                   'grpGrade': 0,
                                                   'grpColor': (255, 0, 0)}}}}
        try:
            pFile.writeDictFile(self.settingsFile, datasDict)
            self.log.debug("---> Tool settings file successfully written: %s" % self.settingsFile)
        except:
            mess = "!!! Can not write tool settings file: %s !!!" % os.path.basename(self.settingsFile)
            self.log.error(mess)
            raise IOError(mess)

    def createPath(self, paths, recursive=False, root=None):
        """
        Create given path list

        :param paths: Paths to create
        :type paths: str | list
        :param recursive: Create paths recursively considering 'root'
        :type recursive: bool
        :param root: Root path for recursive methode
        :type root: str
        """
        #-- Check Args --#
        if isinstance(paths, basestring):
            paths = [paths]
        #-- Function --#
        def makeDir(path):
            """
            Create Given Path

            :param path: Directory full path
            :type path: str
            """
            if not os.path.exists(path):
                try:
                    os.mkdir(path)
                    self.log.debug("Path Created: %s" % path)
                except:
                    mess = "!!! Can not create path: %s !!!" % path
                    self.log.critical(mess)
                    raise IOError(mess)
        #-- Create Paths --#
        for path in paths:
            if recursive:
                if root is None:
                    mess = "!!! In recursive mode, root can not be None !!!"
                    self.log.critical(mess)
                    raise AttributeError(mess)
                #-- Decompose Folders --#
                folders = path.replace('%s/' % root, '').split('/')
                recPath = root
                for fld in folders:
                    recPath = pFile.conformPath(os.path.join(recPath, fld))
                    makeDir(recPath)
            else:
                makeDir(path)
