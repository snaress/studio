import os
from lib.system import procFile as pFile
from appli.foundation.core import users, userGroups, project


class Foundation(object):
    """
    Foundation Class: Contains foundation datas, main core object

    :param logLvl : Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """

    log = pFile.Logger(title="Foundation")
    __user__ = os.environ['USERNAME']
    # __user__ = 'Daneel'
    __rootPath__ = "E:/foundation"
    __tmpPath__ = pFile.conformPath(os.path.join(__rootPath__, "tmp"))
    __projectsPath__ = pFile.conformPath(os.path.join(__rootPath__, "projects"))
    __settingsPath__ = pFile.conformPath(os.path.join(__rootPath__, "settings"))

    def __init__(self, logLvl='info'):
        self.log.level = logLvl
        self.log.info("########## Launching Foundation ##########", newLinesBefore=1)
        self._setup()
        self.userGrps = userGroups.UserGroups(self)
        self.users = users.Users(self)
        self.project = project.Project(self)

    def _setup(self):
        """
        Setup Foundation core object
        """
        self.log.info("#===== Setup Foundation Core =====#", newLinesBefore=1)
        #-- Create Tool Paths --#
        self.log.debug("#--- Check Paths ---#")
        paths = [self.__rootPath__, self.__tmpPath__, self.__projectsPath__, self.__settingsPath__]
        pFile.createPath(paths, log=self.log)
