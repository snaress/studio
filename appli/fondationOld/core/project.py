import os
from lib.system import procFile as pFile


class Project(object):
    """
    Project Class: Contains project datas, child of Fondation

    :param fdtObj: Fondation object
    :type fdtObj: Fondation
    :param logLvl : Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """

    log = pFile.Logger(title="Project")
    __bankDir__ = 'project'

    def __init__(self, fdtObj, logLvl='info'):
        self.log.level = logLvl
        self.fondation = fdtObj
        self._setup()

    def _setup(self):
        """
        Setup Project core object
        """
        self.log.detail("#===== Setup Project Core =====#", newLinesBefor=1)
        #-- Create Tool Paths --#
        self.log.debug("#--- Check Paths ---#")
        self.fondation.createPath([self.bankPath])

    @property
    def bankPath(self):
        """
        Get project bank path

        :return: Project bank path
        :rtype: str
        """
        return pFile.conformPath(os.path.join(self.fondation.__bankPath__, self.__bankDir__))
