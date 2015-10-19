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
from appli.grapher.core import grapherCmds, graphTree, graphNodes


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
        self.nodeCompiler = NodeCompiler(self.grapher)

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
        execTxt = self.nodeCompiler.collecteDatas(execTxt, item)
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
        self.grapher.createFolders(os.path.normpath(os.path.join(self.grapher.graphTmpPath, 'launcher')))
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
            if hasattr(item._node, 'nodeScript'):
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
                          impFrom={'lib.system': 'procFile',
                                   'appli.grapher.core': 'grapherCmds'})
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
                       "gpCmds = grapherCmds",
                       graphNodes.Node.conformVarDict(self.grapher.variables),
                       "print '---> Graph variables setted'"])
        #-- Start Duration --#
        header.append("GP_START_TIME = time.time()")
        #-- Result --#
        self.log.detail("\t >>> Init exec script done.")
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


class NodeCompiler(object):
    """
    Grapher node compiler functions, child of GrapherExec

    :param grapher: Main parent grapher
    :type grapher: Grapher
    """

    def __init__(self, grapher):
        self.grapher = grapher
        self.log = self.grapher.log

    @staticmethod
    def getParentLoops(item):
        """
        Get parent loop nodes

        :param item: GraphItem to execute
        :type item: graphTree.GraphItem
        :return: Parent loop nodes
        :rtype: list
        """
        loopNodes = []
        for pItem in item.allParents():
            if pItem._node.nodeType == 'loop':
                loopNodes.append(pItem)
        loopNodes.reverse()
        return loopNodes

    @staticmethod
    def getVarsStr(item, tab):
        """
        Get readable variable string text

        :param item: GraphItem to execute
        :type item: graphTree.GraphItem
        :param tab: Tab text
        :type tab: str
        :return: Variable string
        :rtype: str
        """
        varDict = graphNodes.Node.conformVarDict(item._node.nodeVariables[item._node.nodeVersion])
        if not tab:
            return varDict
        else:
            lines = varDict.split('\n')
            if not lines:
                return varDict
            else:
                varLines = []
                for line in lines:
                    varLines.append("%s%s" % (tab, line))
                return '\n'.join(varLines)

    def getTab(self, item):
        """
        Get tab text to insert

        :param item: GraphItem to execute
        :type item: graphTree.GraphItem
        :return: Tab text
        :rtype: str
        """
        tab = ''
        for n in range(len(self.getParentLoops(item))):
            tab += '    '
        return tab

    def collecteDatas(self, execTxt, item=None):
        """
        Collecte node datas to store in exec script

        :param execTxt: Exec script
        :type execTxt: str
        :param item: GraphItem to execute
        :type item: graphTree.GraphItem
        :return: Updated Exec script
        :rtype: str
        """
        self.log.info("#--- Collecte Datas ---#", newLinesBefor=1)
        nodeTxt = execTxt
        #-- Get Graph Items --#
        if item is None:
            self.log.detail("\t Mode Graph")
            graphItems = self.grapher.tree.allItems()
            force = False
        else:
            self.log.detail("\t Mode Node")
            graphItems = item.allParents()
            graphItems.reverse()
            graphItems.append(item)
            force =True
        #-- Parse Graph Items --#
        for item in graphItems:
            if item._node.nodeIsActive:
                if not hasattr(item._node, 'nodeExecMode') or not item._node.nodeExecMode[item._node.nodeVersion] or force:
                    if not item._node.nodeType == 'purData':
                        nodeTxt += self.nodeHeader(item)
                        if hasattr(item._node, 'nodeLoopParams'):
                            nodeTxt += self.loopDatas(item)
                        if hasattr(item._node, 'execCommand'):
                            nodeTxt += self.execFileDatas(item)
        #-- Result --#
        self.log.detail("\t >>> Collecte datas done.")
        return nodeTxt

    def nodeHeader(self, item):
        """
        Get node header

        :param item: GraphItem to execute
        :type item: graphTree.GraphItem
        :return: Node header
        :rtype: str
        """
        tab = self.getTab(item)
        dateLine = "print 'Date: %s -- Time: %s' % (procFile.getDate(), procFile.getTime())"
        varStr = self.getVarsStr(item, tab)
        header = ["\n%sprint ''" % tab, "%sprint ''" % tab, "%sprint ''" % tab, "%sprint ''" % tab,
                  "%sprint '%s%s%s'" % (tab, '#' * 10, '#' * (len(item._node.nodeName) + 2), '#' * 10),
                  "%sprint '%s %s %s'" % (tab, '#' * 10, item._node.nodeName, '#' * 10),
                  "%sprint '%s%s%s'" % (tab, '#' * 10, '#' * (len(item._node.nodeName) + 2), '#' * 10),
                  "%s%s" % (tab, dateLine),
                  "%sprint ''" % tab, "%sprint '#--- Set Node Var ---#'" % tab,
                  varStr,
                  "%sprint '---> Node variables setted'" % tab, "%sprint ''" %tab,
                  "%sGP_NODE_START_TIME = time.time()" % tab]
        return '\n'.join(header)

    def loopDatas(self, item):
        """
        Store loop params

        :param item: GraphItem to execute
        :type item: graphItem.GraphItem
        :return: loop string
        :rtype: str
        """
        tab = self.getTab(item)
        iterator = item._node.nodeLoopParams[item._node.nodeVersion]['iterator']
        checkFile = item._node.nodeLoopParams[item._node.nodeVersion]['checkFiles']
        tmpPath = pFile.conformPath(os.path.join(self.grapher.graphTmpPath, 'tmpFiles'))
        tmpFile = "procFile.conformPath(os.path.join('%s', '%s.' + str(%s) + '.py'))" % (tmpPath, checkFile, iterator)
        loopTxt = ["\n%sprint '#--- Set Loop Params ---#'" % tab,
                   "%s%s" % (tab, item._node.loopCommand()),
                   "%s    print ''" % tab, "%s    print ''" % tab,
                   "%s    print '%s'" % (tab, '-' * 80),
                   "%s    print 'LoopNode: %s'" % (tab, item._node.nodeName),
                   "%s    print 'Iterator: %s'" % (tab, iterator),
                   "%s    print 'Iter:', %s" % (tab, iterator),
                   "%s    print '%s'" % (tab, '-' * 80),
                   "%s    %s_tmpFile = %s" % (tab, item._node.nodeName, tmpFile),
                   "%s    result = gpCmds.makeCheckFile(%s_tmpFile, %r, %r, %s)" % (tab, item._node.nodeName,
                                                                                    item._node.nodeName,
                                                                                    iterator, iterator),
                   "%s    if result == 'exists':" % tab,
                   "%s        continue" % tab]
        return '\n'.join(loopTxt)

    def execFileDatas(self, item):
        """
        Store exec script datas

        :param item: GraphItem to execute
        :type item: graphItem.GraphItem
        :return: Exec string
        :rtype: str
        """
        #-- Get Node Exec Info --#
        tab = self.getTab(item)
        nodeScriptFile = os.path.join(os.path.realpath(self.grapher.graphScriptPath), '%s.py' % item._node.nodeName)
        nodeCmd, melFileNeeded = item._node.execCommand(pFile.conformPath(nodeScriptFile))
        nodeTxt = ["\n%sprint ''" % tab, "%sprint '#--- Make Launcher ---#'" % tab]
        loopNodes = self.getParentLoops(item)
        #-- Mode No Loop --#
        if not loopNodes:
            if melFileNeeded:
                #-- Create Unique Mel Launcher --#
                melFile = os.path.join(self.grapher.graphTmpPath, 'launcher', '%s.mel' % item._node.nodeName)
                nodeCmd = "%s -script %s')" % (nodeCmd, pFile.conformPath(os.path.realpath(melFile)))
                nodeTxt.extend(["%sprint 'Create launcher file %s'" % (tab, pFile.conformPath(melFile)),
                                "%sgpCmds.makeLauncher(%r, %r)" % (tab, pFile.conformPath(melFile),
                                                                   pFile.conformPath(nodeScriptFile))])
        #-- Mode Loop --#
        else:
            #-- Get Loop File Info --#
            loopChecks = "["
            launchFile = '"%s' % os.path.join(os.path.realpath(self.grapher.graphTmpPath), 'launcher')
            launchFile += '/%s' % item._node.nodeName
            for loop in loopNodes:
                loopChecks += " %s_tmpFile," % loop._node.nodeName
                launchFile += '." + str(%s) + "' % loop._node.nodeLoopParams[loop._node.nodeVersion]['iterator']
            loopChecks += " ]"
            #-- Create Launcher --#
            if melFileNeeded:
                #-- Create Sequential Mel Launcher --#
                launchFile += '.mel"'
                nodeCmd, melFileNeeded = item._node.execCommand(pFile.conformPath(launchFile))
                nodeCmd = "%s -script" % nodeCmd
            else:
                #-- Create Sequential Py Launcher --#
                launchFile += '.py"'
                nodeCmd, melFileNeeded = item._node.execCommand(pFile.conformPath(launchFile), remote=True)
            nodeCmd += " %s' % launchFile)"
            #-- Edit Node Exec Launcher --#
            nodeTxt.extend(["%slaunchFile = %s" % (tab, pFile.conformPath(launchFile)),
                            "%sprint 'Create launcher file %s'" % (tab, pFile.conformPath(launchFile)),
                            "%sgpCmds.makeLauncher(launchFile, %r, loopChecks=%s)" % (tab,
                                                                                pFile.conformPath(nodeScriptFile),
                                                                                loopChecks)])
        #-- Edit Node Exec Command --#
        nodeTxt.extend(["\n%sprint ''" % tab, "%sprint '#--- Exec Cmd ---#'" % tab,
                        "%sprint %r" % (tab, pFile.conformPath(nodeCmd)),
                        "%sprint ''" % tab, "%s%s" % (tab, nodeCmd)])
        #-- Node Exec Timer --#
        nodeTxt.append(self.nodeEnder(item))
        #-- Result --#
        return '\n'.join(nodeTxt)

    def nodeEnder(self, item):
        """
        Get node ender

        :param item: GraphItem to execute
        :type item: graphItem.GraphItem
        :return: Node end process header
        :rtype: str
        """
        tab = self.getTab(item)
        dateLine = "print 'Date: %s -- Time: %s' % (procFile.getDate(), procFile.getTime())"
        timeLine = "print 'Duration: %s' % procFile.secondsToStr(time.time() - GP_NODE_START_TIME)"
        header = ["\n%sprint ''" % tab, "%sprint ''" % tab,
                  "%sprint '%s Node End: %s %s'" % (tab, '=' * 20, item._node.nodeName, '=' * 20),
                  "%s%s" % (tab, dateLine), "%s%s" % (tab, timeLine)]
        return '\n'.join(header)
