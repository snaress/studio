"""
Usage:

Init Grapher:
-------------
gp = Grapher(logLvl='debug')

Load GraphFile:
---------------
gp.load(graphFile)

Create Node:
------------
newItem = gp.tree.createItem(nodeType='modul', nodeName='myNodeName_1', nodeParent='nodeParentName_#')

Get Node:
---------
myItem = gp.tree.getItemFromNodeName('myNodeName_1')

Parent Node:
------------
myItem.setParent(GraphItem)

Enable / Disable Node:
----------------------
myItem.setEnabled(True)
myItem.setEnabled(False)

delete Node:
------------
myItem.delete()

Get Tree Datas:
---------------
treeDict = gp.tree.getDatas()
print gp.tree.getDatas(asString=True)

Get Node Datas:
---------------
nodeDict = myNodeName_1.getDatas()
print myNodeName_1.getDatas(asString=True)

Loop On Nodes:
--------------
for item in gp.tree.allItems():
    print item._node.nodeName
"""

import os, pprint
from appli import grapher
from lib.env import studio
from lib.system import procFile as pFile
from appli.grapher.core import graphTree, graphNodes


class Grapher(object):
    """
    Grapher core

    :param logLvl: Verbose ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type logLvl: str
    """

    _isReadOnly = False
    _graphFile = None

    def __init__(self, logLvl='info'):
        self.log = pFile.Logger(title="Grapher", level=logLvl)
        self.log.info("#-- Init Grapher Core --#", newLinesBefor=1)
        self.user = grapher.user
        self.userPath = os.path.join(grapher.binPath, 'users', self.user)
        self.studio = studio
        self.comment = ""
        self.variables = dict()
        self.tree = graphTree.GraphTree(self)
        self.gpExec = GrapherExec(self)

    @property
    def graphPath(self):
        """
        Get Grapher root path

        :return: Grapher root path
        :rtype: str
        """
        return os.path.dirname(self._graphFile)

    @property
    def graphName(self):
        """
        Get Grapher name

        :return: Grapher name (graphFile without extension)
        :rtype: str
        """
        return self.graphFile.split('.')[0]

    @property
    def graphFile(self):
        """
        Get Grapher file name

        :return: Grapher file name (with extension)
        :rtype: str
        """
        return os.path.basename(self._graphFile)

    @graphFile.setter
    def graphFile(self, gpFile):
        """
        Set graphFile with given value

        :param gpFile: Grapher file full path
        :type gpFile: str
        """
        self._graphFile = gpFile

    @property
    def graphFullPath(self):
        """
        Get Grapher file full path

        :return: Grapher file full path
        :rtype: str
        """
        return self._graphFile

    @property
    def graphTmpPath(self):
        """
        Get Grapher tmp path

        :return: Grapher relative tmp path
        :rtype: str
        """
        return os.path.join('tmp', 'GP_%s' % self.graphName)

    @property
    def graphScriptPath(self):
        """
        Get Grapher scripts path

        :return: Grapher relative scripts path
        :rtype: str
        """
        return os.path.join('scripts', 'GP_%s' % self.graphName)

    def getDatas(self, asString=False):
        """
        Grapher datas as dict or string

        :param asString: Return string instead of dict
        :type asString: bool
        :return: Grapher contents
        :rtype: dict | str
        """
        graphDict = dict(graphDatas={'comment': self.comment,
                                     'variables': self.variables},
                         treeDatas=self.tree.getDatas())
        if asString:
            graphTxt = []
            for k, v in sorted(graphDict.iteritems()):
                if isinstance(v, basestring):
                    graphTxt.append("%s = %r" % (k, v))
                else:
                    graphTxt.append("%s = %s" % (k, pprint.pformat(v)))
            return '\n'.join(graphTxt)
        return graphDict

    def readDatas(self):
        """
        Read graph datas from graphFile

        :return: Grapher datas
        :rtype: dict
        """
        if self._graphFile is None:
            raise AttributeError("!!! 'graphFile' attribute not setted !!!")
        return pFile.readPyFile(self.graphFullPath)

    def setComment(self, comment):
        """
        Set grapher comment

        :param comment: Grapher comment
        :type comment: str
        """
        self.comment = comment

    def conformNewNodeName(self, nodeName):
        """
        Check new nodeName and return a unique name

        :param nodeName: New nodeName
        :type nodeName: str
        :return: New valide node name
        :rtype: str
        """
        rejected = [' ', '-', ',', ';', ':', '.', '/', '!', '?',
                    '*', '$', '=', '+', '\'', '\\', '"', '&']
        #-- Check Rejected --#
        for r in rejected:
            if r in nodeName:
                nodeName.replace(r, '')
        #-- Check CamelCase --#
        if '_' in nodeName:
            if not nodeName.split('_')[-1].isdigit():
                nodeName.replace('_', '')
        #-- Check Index --#
        if not '_' in nodeName:
            nodeName = '%s_1' % nodeName
        #-- Find Same Base Name --#
        founds = []
        for _nodeName in self.tree.allItems(asString=True):
            if nodeName == _nodeName:
                if not _nodeName in founds:
                    founds.append(_nodeName)
            elif _nodeName.startswith(nodeName.split('_')[0]):
                if not _nodeName in founds:
                    founds.append(_nodeName)
        #-- Result: Name Is Unique --#
        if not founds or not nodeName in founds:
            return nodeName
        #-- Result: Generate Unique Name --#
        iList = []
        for f in founds:
            iList.append(int(f.split('_')[-1]))
        return '%s_%s' % (nodeName.split('_')[0], (max(iList) + 1))

    def createFolders(self, path, relative=True):
        """
        Create Grapher folders

        :param path: Directory to create
        :type path: str
        :param relative: Path is relative to grapher root path
        :type relative: bool
        :return: Full path
        :rtype: str
        """
        #-- Get Root Path --#
        if relative:
            fullPath = os.path.normpath(self.graphPath)
        else:
            fullPath = ''
        #-- Create Path --#
        for fld in os.path.normpath(path).split(os.sep):
            fullPath = os.path.join(fullPath, fld)
            if not os.path.exists(fullPath):
                try:
                    os.mkdir(fullPath)
                    self.log.debug("Create path: %s" % pFile.conformPath(fullPath))
                except:
                    raise IOError("!!! Can not create path: %s !!!" % pFile.conformPath(fullPath))
        #-- Result --#
        return fullPath

    def load(self, graphFile):
        """
        Load given graph file

        :param graphFile: Grapher file full path
        :type graphFile: str
        """
        if not os.path.exists(graphFile):
            raise IOError("!!! GraphFile not found: %s !!!" % graphFile)
        self.log.info("#-- Load Graph File --#")
        self.log.info("Set graphFile: %s" % graphFile)
        self.graphFile = graphFile
        os.chdir(self.graphPath)
        #-- Set Graph Datas --#
        graphDatas = self.readDatas()
        self.setComment(graphDatas['graphDatas']['comment'])
        self.variables = graphDatas['graphDatas']['variables']
        #-- Build Tree --#
        self.tree._topItems = []
        self.tree.buildTree(graphDatas['treeDatas'])
        self.log.info("Parsing Done")

    def saveAs(self, graphFile):
        """
        Save graph as given file name

        :param graphFile: Graph file full path
        :type graphFile: str
        :return: Result
        :rtype: bool
        """
        if not os.path.exists(os.path.dirname(graphFile)):
            raise IOError("!!! Given path not found: %s !!!" % os.path.dirname(graphFile))
        self.log.info("#-- Save Graph File --#")
        self.log.info("Set graphFile: %s" % graphFile)
        self.graphFile = graphFile
        result = self.save()
        if result:
            os.chdir(self.graphPath)
        return result

    def save(self):
        """
        Save graph

        :return: Result, True if success, else False
        :rtype: bool
        """
        #-- Check GraphFile Attr --#
        if self._graphFile is None:
            raise AttributeError("!!! 'graphFile' attribute is None !!!")
        if not os.path.exists(self.graphPath):
            raise IOError("!!! GraphFile path not found: %s !!!" % self.graphPath)
        #-- Try To Save --#
        try:
            pFile.writeFile(self.graphFullPath, self.getDatas(asString=True))
            self.log.info("Graph saved: %s" % self.graphFullPath)
            return True
        except:
            raise IOError("!!! Can not write file %s !!!" % self.graphFullPath)


class GrapherExec(object):
    """
    Grapher exec functions, child of Grapher

    :param grapher: Main parent grapher
    :type grapher: Grapher
    """

    def __init__(self, grapher):
        self.grapher = grapher
        self.log = self.grapher.log

    def execGraph(self, item=None, xTerm=True, wait=True):
        """
        Execute graph tree. If item is None, execute all active nodes.

        :param item: GraphItem to execute
        :type item: GraphItem
        :param xTerm: Enable xTerm
        :type xTerm: bool
        :param wait: Wait at end
        :type wait: bool
        :return: Log file full path
        :rtype: str
        """
        _date = pFile.getDate()
        _time = pFile.getTime()
        #-- Init --#
        if item is None:
            self.log.info("########## EXEC GRAPH ##########", newLinesBefor=1)
        else:
            self.log.info("########## EXEC NODE ##########", newLinesBefor=1)
        self.log.info("Date: %s -- Time: %s" % (_date, _time))
        self.log.info("xTerm: %s" % xTerm)
        self.log.info("wait: %s" % wait)
        #-- Compile --#
        self.createProcessPaths()
        self.createScriptFiles()
        execFile, logFile = self.createProcessFiles(_date, _time)
        execTxt = self.execFileHeader(execFile, _date, _time)
        execTxt = self.collecteDatas(execTxt, item)
        execTxt += self.execFileEnder()
        self.writeExecFile(execFile, execTxt)
        self.executeFile(execFile, logFile, xTerm, wait)
        return logFile

    def createProcessPaths(self):
        """
        Create process directories
        """
        self.log.info("#--- Create Process Path ---#", newLinesBefor=1)
        self.grapher.createFolders(os.path.normpath(os.path.join(self.grapher.graphTmpPath, 'exec')))
        self.grapher.createFolders(os.path.normpath(os.path.join(self.grapher.graphTmpPath, 'logs')))
        self.grapher.createFolders(os.path.normpath(os.path.join(self.grapher.graphTmpPath, 'tmpFiles')))
        self.grapher.createFolders(os.path.normpath(self.grapher.graphScriptPath))
        self.log.detail("\t >>> Create process path done.")

    def createScriptFiles(self):
        """
        Create script files
        """
        self.log.info("#--- create Script Files ---#", newLinesBefor=1)
        for item in self.grapher.tree.allItems():
            self.log.detail("\t ---> %s" % item._node.nodeName)
            nodeScriptFile = os.path.join(self.grapher.graphScriptPath, '%s.py' % item._node.nodeName)
            parents = item.allParents()
            item._node.writeScript(nodeScriptFile, self.grapher.variables, parents)
        self.log.detail("\t >>> Create script files done.")

    def createProcessFiles(self, _date, _time):
        """
        Create process files

        :param _date: Exec date (Y_M_D)
        :type _date: str
        :param _time: Exec time (H_M_S)
        :type _time: str
        :return: ExecFile full path, LogFile full path
        :rtype: str && str
        """
        self.log.info("#--- Create Process Files ---#", newLinesBefor=1)
        execFile = os.path.join(self.grapher.graphTmpPath, 'exec',
                                '%s--%s--%s.py' % (self.grapher.user, _date, _time))
        logFile = os.path.join(self.grapher.graphTmpPath, 'logs',
                               '%s--%s--%s.txt' % (self.grapher.user, _date, _time))
        self.log.detail("\t >>> Create process files done.")
        return execFile, logFile

    def execFileHeader(self, execFile, _date, _time):
        """
        Store exec script header

        :param execFile: ExecFile full path
        :type execFile: str
        :param _date: Exec date (Y_M_D)
        :type _date: str
        :param _time: Exec time (H_M_S)
        :type _time: str
        :return: Script header
        :rtype: str
        """
        self.log.info("#--- Init Exec Script ---#", newLinesBefor=1)
        #-- Init --#
        header = ["print '%s%s%s'" % ("#" * 20, "#" * 9, "#" * 20),
                  "print '%s GRAPHER %s'" % ("#" * 20, "#" * 20),
                  "print '%s%s%s'" % ("#" * 20, "#" * 9, "#" * 20),
                  "print 'Date: %s -- Time: %s'" % (_date, _time),
                  "print 'GraphFile: %s'" % pFile.conformPath(self.grapher.graphFullPath),
                  "print 'ExecFile: %s'" % pFile.conformPath(execFile),
                  "print ''", "print '#--- Import ---#'"]
        #-- Import --#
        importDict = dict(imp=['os', 'sys', 'time'],
                          impFrom={'lib.system': 'procFile'})
        for m in importDict['imp']:
            header.append("print '---> %s'" % m)
            header.append("import %s" % m)
        for k, v in importDict['impFrom'].iteritems():
            header.append("print '---> %s'" % v)
            header.append("from %s import %s" % (k, v))
        #-- Set Path --#
        header.extend(["print ''", "print '#--- Set Path ---#'",
                       "os.chdir('%s')" % self.grapher.graphPath,
                       "print '--->', os.getcwd()"])
        #-- Graph Var --#
        header.extend(["print ''", "print '#--- Set Graph Var ---#'",
                       graphNodes.Node.conformVarDict(self.grapher.variables),
                       "print '---> Graph variables setted'"])
        #-- Start Duration --#
        header.append("GP_START_TIME = time.time()")
        #-- Result --#
        self.log.detail("\t >>> Init exec script done.")
        return '\n'.join(header)

    def collecteDatas(self, execTxt, item=None):
        """
        Collecte node datas to store in exec script

        :param execTxt: Exec script
        :type execTxt: str
        :param item: GraphItem to execute
        :type item: graphItem.GraphItem
        :return: Updated Exec script
        :rtype: str
        """
        self.log.info("#--- Collecte Datas ---#", newLinesBefor=1)
        nodeTxt = execTxt
        #-- Mode Graph --#
        if item is None:
            self.log.detail("\t Mode Graph")
            for item in self.grapher.tree.allItems():
                if item._node.nodeIsActive:
                    if not hasattr(item._node, 'nodeExecMode') or not item._node.nodeExecMode[item._node.nodeVersion]:
                        if not item._node.nodeType == 'purData':
                            nodeTxt = self.execFileDatas(nodeTxt, item)
        #-- Mode Node --#
        else:
            self.log.detail("\t Mode Node")
            parents = item.allParents()
            parents.reverse()
            for parent in parents:
                nodeTxt = self.execFileDatas(nodeTxt, parent)
            nodeTxt = self.execFileDatas(nodeTxt, item)
        #-- Result --#
        self.log.detail("\t >>> Collecte datas done.")
        return nodeTxt

    def execFileDatas(self, execTxt, item):
        """
        Store exec script datas

        :param execTxt: Exec script
        :type execTxt: str
        :param item: GraphItem to execute
        :type item: graphItem.GraphItem
        :return: Node datas
        :rtype: str
        """
        execTxt += self.nodeHeader(item._node)
        if hasattr(item._node, 'execCommand'):
            nodeScriptFile = os.path.join(self.grapher.graphScriptPath, '%s.py' % item._node.nodeName)
            nodeCmd = item._node.execCommand(pFile.conformPath(os.path.realpath(nodeScriptFile)))
            execTxt += self.nodeCommand(nodeCmd)
            execTxt += self.nodeEnder(item._node)
        return execTxt

    @staticmethod
    def nodeHeader(node):
        """
        Get node header

        :param node: Graph node
        :type node: graphNodes.Modul | graphNodes.SysData | graphNodes.CmdData |
                    graphNodes.PurData | graphNodes.Loop
        :return: Node header
        :rtype: str
        """
        header = ["\nprint ''", "print ''", "print ''", "print ''", "print ''",
                  "print '%s%s%s'" % ('#' * 10, '#' * (len(node.nodeName) + 2), '#' * 10),
                  "print '%s %s %s'" % ('#' * 10, node.nodeName, '#' * 10),
                  "print '%s%s%s'" % ('#' * 10, '#' * (len(node.nodeName) + 2), '#' * 10),
                  "print 'Date: %s -- Time: %s'" % (pFile.getDate(), pFile.getTime()),
                  "print ''", "print '#--- Set Node Var ---#'",
                  graphNodes.Node.conformVarDict(node.nodeVariables[node.nodeVersion]),
                  "print '---> Node variables setted'", "print ''",
                  "GP_NODE_START_TIME = time.time()"]
        return '\n'.join(header)

    @staticmethod
    def nodeCommand(cmd):
        """
        Get node command

        :param cmd: Node exec command
        :type cmd: str
        :return: Node exec header
        :rtype: str
        """
        header = ["\nprint '#--- Exec Cmd ---#'",
                  'print %r' % pFile.conformPath(cmd),
                  "print ''", cmd]
        return '\n'.join(header)

    @staticmethod
    def nodeEnder(node):
        """
        Get node ender

        :param node: Graph node
        :type node: graphNodes.Modul | graphNodes.SysData | graphNodes.CmdData |
                    graphNodes.PurData | graphNodes.Loop
        :return: Node end process header
        :rtype: str
        """
        header = ["\nprint ''", "print ''",
                  "print '%s Node End: %s %s'" % ('=' * 20, node.nodeName, '=' * 20),
                  "print 'Date: %s -- Time: %s' % (procFile.getDate(), procFile.getTime())",
                  "print 'Duration: %s' % procFile.secondsToStr(time.time() - GP_NODE_START_TIME)"]
        return '\n'.join(header)

    def execFileEnder(self):
        """
        Store exec script last lines

        :return: Script end header
        :rtype: str
        """
        header = ["\nprint ''", "print ''", "print ''", "print ''", "print ''",
                  "if os.path.exists(%r):" % pFile.conformPath(os.path.join(self.grapher.graphPath, 'Keyboard')),
                  "    print '>>> Clean unknown folders: Keyboard ...'",
                  "    os.rmdir(%r)" % pFile.conformPath(os.path.join(self.grapher.graphPath, 'Keyboard')),
                  "print '%s%s%s'" % ('=' * 20, '=' * 13, '=' * 20),
                  "print '%s GRAPHER END %s'" % ('=' * 20, '=' * 20),
                  "print '%s%s%s'" % ('=' * 20, '=' * 13, '=' * 20),
                  "print 'Date: %s -- Time: %s' % (procFile.getDate(), procFile.getTime())",
                  "print 'Duration: %s' % procFile.secondsToStr(time.time() - GP_START_TIME)"]
        return '\n'.join(header)

    def writeExecFile(self, execFile, execTxt):
        """
        Write exec file

        :param execFile: ExecFile full path
        :type execFile: str
        :param execTxt: Exec script
        :type execTxt: str
        """
        self.log.info("#--- Write Exec File ---#", newLinesBefor=1)
        try:
            pFile.writeFile(execFile, execTxt)
            self.log.info("execFile saved: %s" % pFile.conformPath(execFile))
        except:
            raise IOError("!!! Can not write execFile: %s !!!" % pFile.conformPath(execFile))
        self.log.detail("\t >>> Write exec file done.")

    def executeFile(self, execFile, logFile, xTerm, wait):
        """
        Execute script file

        :param execFile: ExecFile full path
        :type execFile: str
        :param logFile: LogFile full path
        :type logFile: str
        :param xTerm: Enable 'Show XTerm'
        :type xTerm: bool
        :param wait: Enable 'Wait At End'
        :type wait: bool
        """
        self.log.info("#--- Launch Exec File ---#", newLinesBefor=1)
        cmd = self.execCommand(execFile, logFile, xTerm=xTerm, wait=wait)
        self.log.info("cmd: %s" % cmd)
        os.system(cmd)
        self.log.detail("\t >>> Exec file launched.")

    def execCommand(self, execFile, logFile, xTerm=True, wait=True):
        """
        Get exec command

        :param execFile: Exec file full path
        :type execFile: str
        :param logFile: Log file full path
        :type logFile: str
        :param xTerm: Enable xTerm
        :type xTerm: bool
        :param wait: Wait at end
        :type wait: bool
        :return: Exec commmand
        :rtype: str
        """
        cmd = ''
        #-- Start Options --#
        cmd += 'start "%s" ' % self.grapher.graphFile
        if not xTerm:
            cmd += '/B '
        #-- Batch Options --#
        cmd += '"%s" ' % os.path.normpath(self.grapher.studio.cmdExe)
        if wait:
            if xTerm:
                cmd += '/K '
            else:
                cmd += '/C '
        else:
            cmd += '/C '
        #-- Command Options --#
        cmd += '"%s ' % os.path.normpath(self.grapher.studio.python27)
        cmd += '%s" ' % os.path.normpath(os.path.join(self.grapher.graphPath, pFile.conformPath(execFile)))
        #-- Log File --#
        if not xTerm:
            cmd += '>>%s 2>&1' % logFile
        #-- Result --#
        return cmd
