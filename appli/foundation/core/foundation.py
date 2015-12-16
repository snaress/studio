import os
from lib.system import procFile as pFile


class Foundation(object):

    log = pFile.Logger(title="Foundation")
    __user__ = os.environ['USERNAME']
    __rootPath__ = "E:/fondation"
    __prodsPath__ = pFile.conformPath(os.path.join(__rootPath__, 'prods'))
    __settingsPath__ = pFile.conformPath(os.path.join(__rootPath__, 'settings'))

    def __init__(self, logLvl='info'):
        self.log.level = logLvl
        self.log.info("########## Launching Foundation ##########", newLinesBefore=1)

    def _setup(self):
        """
        Setup Foundation core object
        """
        self.log.debug("#===== Setup Foundation =====#", newLinesBefore=1)

    def _checkFoundationMainDir(self):
        self.log.debug("#--- Check Paths ---#")

    def createPath(self, paths, recursive=False, root=None):
        """
        Create given path list

        :param paths: Paths to create
        :type paths: str | list
        :param recursive: Create paths recursively considering 'root'
        :type recursive: bool
        :param root: Root path for recursive methode
        :type root: str
        :return: Created path
        :rtype: list
        """
        #-- Check Args --#
        if isinstance(paths, basestring):
            paths = [paths]
        #-- Function --#
        dirs = []
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
                    dirs.append(path)
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
        #-- Result --#
        return dirs
