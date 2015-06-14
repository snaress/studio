import os
from appli import grapherOld
from lib.system import procFile as pFile


class Grapher(object):

    def __init__(self, logLvl='info'):
        self.log = pFile.Logger(title="Grapher", level=logLvl)
        self.log.info("#-- Launching Grapher --#")
        self._file = None
        self._lock = False
        self.gpComment = {'html': "", 'text': ""}
        self.gpVariables = {}
        self.gpGraph = {'_order': []}

    @property
    def fileName(self):
        """ Get graph fileName
            :return: (str) : Graph fileName """
        if self._file is not None:
            return pFile.conformPath(os.path.basename(self._file))

    @property
    def filePath(self):
        """ Get graph filePath
            :return: (str) : Graph filePath """
        if self._file is not None:
            return pFile.conformPath(os.path.dirname(self._file))

    @property
    def graphFile(self):
        """ Get graph absolute path
            :return: (str) : Graph file absolute path """
        if self._file is not None:
            return pFile.conformPath(self._file)

    @graphFile.setter
    def graphFile(self, value):
        """ Set graphFile absolute path
            :param value: (str) : GraphFile absolute path """
        self._file = value

    @property
    def graphData(self):
        """ Get graph data
            :return: (dict) : Graph data """
        data = {}
        for k, v in self.__dict__.iteritems():
            if k.startswith("gp"):
                data[k] = v
        return data

    @property
    def lock(self):
        """ Get lock state
            :return: (bool) : True if graph is locked """
        return self._lock

    @lock.setter
    def lock(self, value):
        """ Set lock state
            :param value: (bool) : Lock state """
        self._lock = value

    @property
    def lockFile(self):
        """ Get lockFile
            :return: (str) : LockFile absolute path """
        if self.graphFile is not None:
            lockFile = self.fileName.replace("gp_", "gpLock_")
            return pFile.conformPath(os.path.join(self.filePath, lockFile))

    @property
    def defaultNodeDict(self):
        """ Get default nodeData dict
            :return: (dict) : Node data """
        return {'nodeName': "NewNode", 'nodeInstance': None, 'nodeEnabled': True, 'nodeExpanded': True,
                'nodeType': "modul", 'nodeVersion': "001", 'nodeVTitle': {'001': "New Version"}, 'nodeExec': False}

    def loadGraphFile(self, graphFile):
        """ Load given graph file
            :param graphFile: (str) : GraphFile absolut path
            :return: (bool, str) : Result, log """
        self.log.info("Loading graphFile: %s" % graphFile)
        #-- Check Graph File --#
        if not os.path.exists(graphFile):
            warn = "GraphFile not found"
            self.log.error(warn)
            return False, warn
        #-- Check FileName --#
        fileName = os.path.basename(os.path.normpath(graphFile))
        if not fileName.startswith("gp_") or not fileName.endswith(".py"):
            warn = "FileName Not Valide, Should have path/gp_fileName.py, got %s" % graphFile
            self.log.error(warn)
            return False, warn
        #-- Load Graph --#
        self.graphFile = graphFile
        self._checkLockFile()
        self.update()
        return True, "GraphFile successfully loaded"

    def writeGraphFile(self, graphFile=None, force=False, forceLock=False):
        """ Write Graph with grapher fileName
            :param graphFile: (str) : GraphFile absolute path
            :param force: (bool) : Overwrite existing file
            :return: (bool, str) : Result, log """
        #-- Check FileName --#
        if graphFile is not None:
            if self._checkGraphFileName(graphFile):
                self.graphFile = graphFile
            else:
                warn = "FileName Not Valide, Should have path/gp_fileName.py, got %s" % graphFile
                self.log.error(warn)
                return False, warn
        #-- Check GraphFile --#
        if self.graphFile is None:
            warn = "Grapher param graphFile is None"
            self.log.error(warn)
            return False, warn
        #-- Check FilePath --#
        if os.path.exists(self.filePath):
            if not force:
                warn = "GraphFile already exists, use 'force=True' to enable overwriting"
                self.log.error(warn)
                return False, warn
        #-- Check LockFile --#
        if self.lock:
            if not forceLock:
                warn = "Destination Graph Locked, use 'forceLock=True' to enable overwriting"
                self.log.error(warn)
                return False, warn
        #-- Write File --#
        data = self._dataToString(self.graphData)
        try:
            self.log.debug("Writing graphFile: %s" % self.graphFile)
            pFile.writeFile(self.graphFile, data)
            return True, "Graph successfully written"
        except:
            return False, "Can not write file %s" % self.graphFile

    def update(self):
        """ Update graph data from graphFile """
        params = pFile.readPyFile(self.graphFile)
        for k in params.keys():
            if k.startswith("gp"):
                self.log.debug("Updating %s ..." % k)
                setattr(self, k, params[k])

    @staticmethod
    def _checkGraphFileName(graphFile):
        """ Check if graph fileName is valid
            :param graphFile: (str) : GraphFile absolute path
            :return: (bool) : True if valid """
        fileName = os.path.basename(graphFile)
        if not fileName.startswith('gp_') or not fileName.endswith('.py'):
            return False
        return True

    def _checkLockFile(self):
        """ Check if lockFile exists and set 'lock' property """
        if self.lockFile is None:
            self.lock = False
        else:
            if not os.path.exists(self.lockFile):
                self.lock = False
            else:
                self.lock = True

    def _createLockFile(self, lockFile):
        """ Create lockFile
            :param lockFile: (str) : LockFile absolute path """
        lockTxt = ["user = %r" % grapherOld.user,
                   "station = %r" % grapherOld.station,
                   "date = %r" % pFile.getDate(),
                   "time = %r" % pFile.getTime()]
        try:
            pFile.writeFile(lockFile, '\n'.join(lockTxt))
            self.log.debug("LockFile successfully create: %s" % lockFile)
        except:
            raise IOError, "Can not create lockFile: %s" % lockFile

    def _removeLockFile(self, lockFile):
        """ Remove lockFile
            :param lockFile: (str) : LockFile absolute path
            :return: (bool) : True if success, False if failed """
        if os.path.exists(lockFile):
            try:
                os.remove(lockFile)
                self.log.debug("LockFile removed: %s" % os.path.basename(lockFile))
                return True
            except:
                raise IOError, "Can not remove lockFile: %s" % lockFile
        else:
            raise IOError, "LockFile not found: %s" % lockFile

    @staticmethod
    def _dataToString(data):
        """ Convert dataDict to string
            :param data: (dict) : grapher.graphData
            :return: (str) : Data string format """
        txt = []
        for k, v in data.iteritems():
            if isinstance(v, str):
                txt.append("%s = %r" % (k, v))
            else:
                txt.append("%s = %s" % (k, v))
        return '\n'.join(txt)
