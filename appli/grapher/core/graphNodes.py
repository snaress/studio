import os, pprint, collections
from lib.env import studio
from lib.system import procFile as pFile


class Node(object):
    """
    Node common datas contents.

    :param nodeName: Node Name
    :type nodeName: str
    :param graphObj: Grapher parent
    :type graphObj: grapher.Grapher
    """

    def __init__(self, nodeName=None, graphObj=None):
        self.gp = graphObj
        self.nodeName = nodeName
        self.nodeIsEnabled = True
        self.nodeIsActive = True
        self.nodeIsExpanded = False
        self.nodeVersion = 0
        self.nodeVersions = {0: "Default Version"}
        self.nodeComments = {0: ""}
        self.nodeVariables = {0: dict()}
        self.nodeTrash = {0: ""}

    def getDatas(self, asString=False):
        """
        Get GraphNode datas as dict or string

        :param asString: Return string instead of dict
        :type asString: bool
        :return: Node contents
        :rtype: dict | str
        """
        nodeDict = dict()
        #-- Parse Datas --#
        for k, v in sorted(self.__dict__.iteritems()):
            if k.startswith('node'):
                nodeDict[k] = v
        #-- Return Datas --#
        if asString:
            return pprint.pformat(nodeDict)
        return nodeDict

    def setDatas(self, **kwargs):
        """
        Set GraphNode datas

        :param kwargs: Node datas
        :type kwargs: dict
        """
        for k, v in kwargs.iteritems():
            if not k in ['nodeName', 'nodeType']:
                if hasattr(self, k):
                    setattr(self, k, v)

    def setVersionnedDatas(self, **kwargs):
        """
        Set GraphNode versionned datas

        :param kwargs: Datas (node.attrName: node.attrValue)
        :type kwargs: dict
        """
        for k, v in kwargs.iteritems():
            if hasattr(self, k):
                val = getattr(self, k)
                val[self.nodeVersion] = v
                setattr(self, k, val)

    def listAttrs(self):
        """
        List all attributes

        :return: Attributes
        :rtype: list
        """
        attrs = []
        for attr in self.getDatas().keys():
            attrs.append(attr)
        return sorted(attrs)

    def addVersion(self):
        """
        Add new node version

        :return: New version
        :rtype: int
        """
        curIndex = self.nodeVersion
        newIndex = int(sorted(self.nodeVersions.keys())[-1] + 1)
        self.nodeVersions[newIndex] = "New Version"
        self.nodeComments[newIndex] = self.nodeComments[curIndex]
        self.nodeVariables[newIndex] = self.nodeVariables[curIndex]
        self.nodeTrash[newIndex] = self.nodeTrash[curIndex]
        if hasattr(self, 'nodeScript'):
            self.nodeScript[newIndex] = self.nodeScript[curIndex]
            if hasattr(self, 'nodeLauncher'):
                self.nodeLauncher[newIndex] = self.nodeLauncher[curIndex]
            if hasattr(self, 'nodeLaunchArgs'):
                self.nodeLaunchArgs[newIndex] = self.nodeLaunchArgs[curIndex]
            if hasattr(self, 'nodeExecMode'):
                self.nodeExecMode[newIndex] = self.nodeExecMode[curIndex]
        if hasattr(self, 'nodeLoopParams'):
            self.nodeLoopParams[newIndex] = self.nodeLoopParams[curIndex]
        self.nodeVersion = newIndex
        return self.nodeVersion

    def delVersion(self):
        """
        Delete current node version

        :return: Current version
        :rtype: int
        """
        curIndex = self.nodeVersion
        if not len(self.nodeVersions.keys()) == 1:
            #-- Get new Index --#
            if curIndex == sorted(self.nodeVersions.keys())[0]:
                newIndex = sorted(self.nodeVersions.keys())[1]
            else:
                n = sorted(self.nodeVersions.keys()).index(curIndex)
                newIndex = sorted(self.nodeVersions.keys())[n-1]
            self.nodeVersion = newIndex
            #-- Delete Version --#
            self.nodeVersions.pop(curIndex)
            self.nodeComments.pop(curIndex)
            self.nodeVariables.pop(curIndex)
            self.nodeTrash.pop(curIndex)
            if hasattr(self, 'nodeScript'):
                self.nodeScript.pop(curIndex)
                if hasattr(self, 'nodeLauncher'):
                    self.nodeLauncher.pop(curIndex)
                if hasattr(self, 'nodeLaunchArgs'):
                    self.nodeLaunchArgs.pop(curIndex)
                if hasattr(self, 'nodeExecMode'):
                    self.nodeExecMode.pop(curIndex)
            if hasattr(self, 'nodeLoopParams'):
                self.nodeLoopParams.pop(curIndex)
            return newIndex

    @staticmethod
    def conformVarDict(varDict):
        """
        Conform variables to string

        :param varDict: Variables to conform
        :type varDict: dict
        :return: Conformed variables
        :rtype: str
        """
        var = []
        stored = dict()
        for n, varDict in sorted(varDict.iteritems()):
            if varDict['state']:
                #-- Store Current Var Type --#
                if not varDict['label'] in stored.keys():
                    stored[varDict['label']] = type(varDict['value'])
                #-- Type Init --#
                if varDict['type'] == 0:
                    if isinstance(varDict['value'], str):
                        if '+' in varDict['value'] or '%' in varDict['value']:
                            var.append("%s = eval(%r)" % (varDict['label'], varDict['value']))
                        else:
                            var.append("%s = %r" % (varDict['label'], varDict['value']))
                    else:
                        var.append("%s = %s" % (varDict['label'], varDict['value']))
                #-- Type Add --#
                elif varDict['type'] == 1:
                    #-- Add List --#
                    if stored[varDict['label']] is list:
                        if isinstance(varDict['value'], list):
                            var.append("%s.extend(%s)" % (varDict['label'], varDict['value']))
                        else:
                            if isinstance(varDict['value'], basestring):
                                if '+' in varDict['value'] or '%' in varDict['value']:
                                    var.append("%s.append(eval(%r))" % (varDict['label'], varDict['value']))
                                else:
                                    var.append("%s.append(%r)" % (varDict['label'], varDict['value']))
                            else:
                                var.append("%s.append(%s)" % (varDict['label'], varDict['value']))
                    #-- Add Dict --#
                    elif stored[varDict['label']] is dict:
                        if isinstance(varDict['value'], dict):
                            for k, v in varDict['value'].iteritems():
                                if isinstance(v, basestring):
                                    if isinstance(k, basestring):
                                        var.append("%s[%r] = %r" % (varDict['label'], k, v))
                                    else:
                                        var.append("%s[%s] = %r" % (varDict['label'], k, v))
                                else:
                                    if isinstance(k, basestring):
                                        var.append("%s[%r] = %s" % (varDict['label'], k, v))
                                    else:
                                        var.append("%s[%s] = %s" % (varDict['label'], k, v))
                        else:
                            raise ValueError("!!! ERROR: %s value should be 'dict', got %s" % (varDict['label'],
                                                                                               varDict['value']))
                    #-- Add Str --#
                    elif stored[varDict['label']] in [str, basestring]:
                        var.append("%s += %r" % (varDict['label'], varDict['value']))
                    #-- Add Num --#
                    elif stored[varDict['label']] in [int, float, long, complex]:
                        var.append("%s += %s" % (varDict['label'], varDict['value']))
                    #-- Error --#
                    else:
                        raise ValueError("!!! ERROR: %s value type not supported: %s" % (varDict['label'],
                                                                                         stored[varDict['label']]))
        #-- Result --#
        return '\n'.join(var)

    def writeScript(self, scriptFile, graphVars, parents):
        """
        Write current script to file

        :param scriptFile: Script file full path
        :type scriptFile: str
        :param graphVars: Grapher variables
        :type graphVars: dict
        :param parents: Parent items
        :type parents: list
        """
        if hasattr(self, 'nodeScript'):
            script = []
            if not self.nodeType == 'purData':
                #-- Get Graph Var --#
                script.append("\n#----- Internal Vars -----#")
                for k, v in self.gp.internalVar.iteritems():
                    script.append("%s = %r" % (k, v))
                #-- Get Graph Var --#
                script.append("\n#----- Grapher Vars -----#")
                varStr = self.conformVarDict(graphVars)
                if varStr is not None:
                    script.append(varStr)
                #-- Get Parents Var --#
                script.append("\n#----- Parents Vars -----#")
                parents.reverse()
                for parent in parents:
                    script.append("#-- Node: %s --#" % parent._node.nodeName)
                    varStr = self.conformVarDict(parent._node.nodeVariables[parent._node.nodeVersion])
                    if varStr is not None:
                        script.append(varStr)
            #-- Get Node Var --#
            script.append("\n#----- Node Vars -----#")
            varStr = self.conformVarDict(self.nodeVariables[self.nodeVersion])
            if varStr is not None:
                script.append(varStr)
            #-- Get Script --#
            script.append("\n#----- Node Script -----#")
            script.append(self.nodeScript[self.nodeVersion])
            try:
                pFile.writeFile(os.path.normpath(scriptFile), '\n'.join(script))
            except:
                raise IOError("!!! Can not write script: %s" % self.nodeName)


class Modul(Node):
    """
    Modul datas contents.

    :param nodeName: Node Name
    :type nodeName: str
    :param graphObj: Grapher parent
    :type graphObj: grapher.Grapher
    """

    _nodeColor = (200, 200, 200, 255)
    _nodeIcon = 'modul.svg'

    def __init__(self, nodeName=None, graphObj=None):
        super(Modul, self).__init__(nodeName, graphObj)
        self.nodeType = 'modul'


class SysData(Node):
    """
    SysData datas contents.

    :param nodeName: Node Name
    :type nodeName: str
    :param graphObj: Grapher parent
    :type graphObj: grapher.Grapher
    """

    _nodeColor = (100, 255, 255, 255)
    _nodeIcon = 'sysData.svg'

    def __init__(self, nodeName=None, graphObj=None):
        super(SysData, self).__init__(nodeName, graphObj)
        self.nodeType = 'sysData'
        self.nodeExecMode = {0: False}
        self.nodeScript = {0: ''}

    @staticmethod
    def execCommand(scriptFile, remote=False):
        """
        Get node exec command

        :param scriptFile: Node script file full path
        :type scriptFile: str
        :param remote: Remote state
        :type remote: bool
        :return: Node exec cmd, melFileNeeded
        :rtype: str, bool
        """
        if remote:
            return "os.system('%s" % studio.python27, False
        return "os.system('%s %s')" % (studio.python27, pFile.conformPath(scriptFile)), False


class CmdData(Node):
    """
    CmdData datas contents.

    :param nodeName: Node Name
    :type nodeName: str
    :param graphObj: Grapher parent
    :type graphObj: grapher.Grapher
    """

    _nodeColor = (60, 135, 255, 255)
    _nodeIcon = 'cmdData.svg'
    _launchers = collections.OrderedDict([('maya2014', pFile.conformPath(studio.maya)),
                                          ('mayaBatch2014', pFile.conformPath(studio.mayaBatch)),
                                          ('mayaPy2014', pFile.conformPath(studio.mayaPy)),
                                          ('mayaRender2014', pFile.conformPath(studio.mayaRender)),
                                          ('nuke5', pFile.conformPath(studio.nuke5)),
                                          ('nuke9', pFile.conformPath(studio.nuke9))])

    def __init__(self, nodeName=None, graphObj=None):
        super(CmdData, self).__init__(nodeName, graphObj)
        self.nodeType = 'cmdData'
        self.nodeExecMode = {0: False}
        self.nodeLauncher = {0: 'mayaBatch2014'}
        self.nodeLaunchArgs = {0: ''}
        self.nodeScript = {0: ''}

    def execCommand(self, scriptFile):
        """
        Get node exec command

        :param scriptFile: Node script file full path
        :type scriptFile: str
        :return: Node exec cmd, melFileNeeded
        :rtype: str, bool
        """
        launcher = self.nodeLauncher[self.nodeVersion]
        launcherCmd = self._launchers[launcher]
        #-- Init Command --#
        cmd = ""
        cmd += "os.system('"
        cmd += "%s" % launcherCmd
        #-- Add Launcher Arguments --#
        if self.nodeLaunchArgs[self.nodeVersion]:
            cmd += " ' + %s + '" % self.nodeLaunchArgs[self.nodeVersion]
        #-- Mel Launcher --#
        if launcher in ['maya2014', 'mayaBatch2014']:
            return cmd, True
        #-- Py Launcher --#
        cmd += " %s" % pFile.conformPath(scriptFile)
        cmd += "')"
        return cmd, False


class PurData(Node):
    """
    PurData datas contents.

    :param nodeName: Node Name
    :type nodeName: str
    :param graphObj: Grapher parent
    :type graphObj: grapher.Grapher
    """

    _nodeColor = (0, 125, 0, 255)
    _nodeIcon = 'purData.svg'

    def __init__(self, nodeName=None, graphObj=None):
        super(PurData, self).__init__(nodeName, graphObj)
        self.nodeType = 'purData'
        self.nodeScript = {0: ''}


class Loop(Node):
    """
    Loop datas contents.

    :param nodeName: Node Name
    :type nodeName: str
    :param graphObj: Grapher parent
    :type graphObj: grapher.Grapher
    """

    _nodeColor = (100, 255, 150, 255)
    _nodeIcon = 'loop.svg'

    def __init__(self, nodeName=None, graphObj=None):
        super(Loop, self).__init__(nodeName, graphObj)
        self.nodeType = 'loop'
        self.nodeLoopParams = {0: {'remote': False, 'packet': 5, 'pool': 'default', 'mode': 'Incremental',
                                   'type': 'Range', 'iterator': 'i', 'checkFiles': 'tmpCheck',
                                   'loopStart': 1, 'loopStop': 100, 'loopStep': 1,
                                   'loopList': [], 'loopSingle': 1}}

    # noinspection PyTypeChecker
    def loopCommand(self):
        """
        Get node loop command

        :return: Node loop cmd
        :rtype: str
        """
        #-- Mode Range --#
        if self.nodeLoopParams[self.nodeVersion]['type'] == 'Range':
            loop = "for %s in range(%s, (%s + 1), %s):" % (self.nodeLoopParams[self.nodeVersion]['iterator'],
                                                           self.nodeLoopParams[self.nodeVersion]['loopStart'],
                                                           self.nodeLoopParams[self.nodeVersion]['loopStop'],
                                                           self.nodeLoopParams[self.nodeVersion]['loopStep'])
        #-- Mode List --#
        elif self.nodeLoopParams[self.nodeVersion]['type'] == 'List':
            loop = "for %s in %s:" % (self.nodeLoopParams[self.nodeVersion]['iterator'],
                                      self.nodeLoopParams[self.nodeVersion]['loopList'])
        #-- Mode Single --#
        else:
            loop = "for %s in [%s]:" % (self.nodeLoopParams[self.nodeVersion]['iterator'],
                                        self.nodeLoopParams[self.nodeVersion]['loopSingle'])
        #++ Result --#
        return loop
