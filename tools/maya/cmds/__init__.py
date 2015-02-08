
class SanityCheck(object):

    def __init__(self):
        self._initResult()
        self.cmdDict = self._getCmdsDict()

    @staticmethod
    def _getCmdsDict():
        """ Convert package parsing into dict
            :return: Package module and functions
            :rtype: dict """
        #-- Import Local --#
        import os
        from lib.system import procFile as pFile
        #-- Parse Package --#
        print "Parsing package ..."
        toolPath = os.path.normpath(os.path.dirname(__file__))
        cmdFiles = os.listdir(toolPath) or []
        cmdDict = {}
        for cmdFile in cmdFiles:
            #-- Parse File --#
            if not cmdFile.startswith('_') and not cmdFile.startswith('.') and cmdFile.endswith('.py'):
                cmdDict[cmdFile] = {'_functions': []}
                cmdLines = pFile.readFile(os.path.join(toolPath, cmdFile))
                className = None
                for line in cmdLines:
                    if line.startswith('def '):
                        cmdDict[cmdFile]['_functions'].append(line.strip())
                    if line.startswith('class '):
                        className = line.strip('\n')
                        cmdDict[cmdFile][className] = []
                    if line.startswith('    def '):
                        cmdDict[cmdFile][className].append(line.strip())
        return cmdDict

    def checkAuto(self, printCmds=False):
        """ Launch check and give result
            :param printCmds: Enable functions listing
            :type printCmds: bool
            :return: True if success, False if failed
            :rtype: bool """
        if printCmds:
            self.printCmds()
        errors = self.check()
        return self.result(errors)

    def check(self):
        """ Check non duplicity of commands
            :return: Errors info
            :rtype: dict """
        print "Checking Modules ..."
        errors = {}
        for f in self.cmdDict.keys():
            print "\t Module: %s" % f
            #-- Check Functions --#
            functions = self.cmdDict[f]['_functions']
            for func in functions:
                funcError = self._compareFunctions(f, func)
                if funcError.keys():
                    for k, v in funcError.iteritems():
                        errors[k] = v
            #-- Check Class --#
            if not 'Mel.py' in f:
                for cl in self.cmdDict[f].keys():
                    if not cl == '_functions':
                        classError = self._compareClass(f, cl)
                        if classError.keys():
                            for k, v in classError.iteritems():
                                errors[k] = v
            #-- Check Mel Class --#
            else:
                for k in self.cmdDict[f].keys():
                    if k.startswith('class FromMel(object):'):
                        melFunctions = self.cmdDict[f][k]
                        melError = self._compareMel(f, melFunctions)
                        if melError.keys():
                            for k, v in melError.iteritems():
                                errors[k] = v
        return errors

    @staticmethod
    def result(errors):
        """ Print result from errors dict
            :param errors: Errors found
            :type errors: dict
            :return: True if success, False if failed
            :rtype: bool """
        print "\n#========== SANITY CHECK ==========#"
        if not errors.keys():
            print "Success !"
            return True
        else:
            print "Failed !!!"
            for k in errors.keys():
                print k
                for f in errors[k]:
                    print "\t %s" % f
            return False

    def printCmds(self, cmdFile=None):
        """ List and print functions and class
            :param cmdFile: Specific cmdFile to print
            :type cmdFile: str """
        print "\n#========== COMMANDS LIST ==========#"
        #-- Parse dict function --#
        def parseDict(fileName):
            """ print dict with given key
                :param fileName: Python file
                :type fileName: str """
            print "\nCmd File: %s" % fileName
            for func in self.cmdDict[fileName]['_functions']:
                print "\t %s" % func
            for k in self.cmdDict[fileName].keys():
                if not k == '_functions':
                    print "\n\t %s" % k
                    for v in self.cmdDict[fileName][k]:
                        print "\t\t %s" % v
        #-- Launch dict parsing
        if cmdFile is None:
            for f in self.cmdDict.keys():
                parseDict(f)
        else:
            parseDict(cmdFile)

    def _compareFunctions(self, fileName, function):
        """ Compare given function to all cmds and proc modules to find doublon
            :param fileName: Python file module ('cloth.py')
            :type fileName: str
            :param function: Function name to compare
            :type function: str
            :return: Errors if duplicate function found
            :rtype: dict """
        errors = {}
        funcName = function.split('(')[0]
        for f in self.cmdDict.keys():
            dupli = False
            if not f == fileName:
                for dFunction in self.cmdDict[f]['_functions']:
                    if funcName == dFunction.split('(')[0]:
                        if not funcName in errors.keys():
                            errors[funcName] = []
                        errors[funcName].append(f)
                        dupli = True
            if dupli:
                errors[funcName].append(fileName)
        return errors

    def _compareClass(self, fileName, className):
        """ Compare given class to all cmds and proc modules to find doublon
            :param fileName: Python file module ('cloth.py')
            :type fileName: str
            :param className: Class name to compare
            :type className: str
            :return: Errors if duplicate class found
            :rtype: dict """
        errors = {}
        className = className.split('(')[0]
        for f in self.cmdDict.keys():
            dupli = False
            if not f == fileName and not f.endswith('Mel.py'):
                for dClass in self.cmdDict[f].keys():
                    if not dClass == '_functions':
                        if className == dClass.split('(')[0]:
                            if not className in errors.keys():
                                errors[className] = []
                            errors[className].append(f)
                            dupli = True
            if dupli:
                errors[className].append(fileName)
        return errors

    def _compareMel(self, fileName, melFunctions):
        """ Compare given melFunctions to all mel modules to find doublon
            :param fileName: Python file module ('cloth.py')
            :type fileName: str
            :param melFunctions: Mel functions
            :type melFunctions: list
            :return: Errors if duplicate class found
            :rtype: dict """
        errors = {}
        for f in self.cmdDict.keys():
            if not f == fileName and f.endswith('Mel.py'):
                for melFunc in melFunctions:
                    melFuncName = melFunc.split('(')[0]
                    label = "class FromMel().%s" % melFuncName
                    for k in self.cmdDict[f].keys():
                        if k.startswith('class FromMel(object):'):
                            dFunctions = self.cmdDict[f][k]
                            for dFunc in dFunctions:
                                dfuncName = dFunc.split('(')[0]
                                if not dfuncName in ['def __init__']:
                                    if dfuncName == melFuncName:
                                        if not label in errors.keys():
                                            errors[label] = []
                                        errors[label].append(f)
        if errors.keys():
            for k in errors.keys():
                errors[k].append(fileName)
        return errors

    @staticmethod
    def _initResult():
        """ Initialize result """
        #-- Import Local --#
        import os
        #-- Init Print --#
        print '\n', '#' * 80
        print "#" * 26, "STUDIO MAYA COMMANDS CHECK", "#" * 26
        print '#' * 80
        print "Path:", os.path.normpath(os.path.dirname(__file__))



if not SanityCheck().checkAuto():
    raise IOError, "Sanity Check failed !!!"


print "\n#========== IMPORT MODULES ==========#"
#-- MODELING --#
print "Importing modeling.py ..."
from tools.maya.cmds.modeling import *
print "Importing procModeling.py ..."
from tools.maya.cmds.procModeling import *
#-- RIGG --#
print "Importing rigg.py ..."
from tools.maya.cmds.rigg import *
#-- CLOTH --#
print "Importing cloth.py ..."
from tools.maya.cmds.cloth import *
print "Importing procCloth.py ..."
from tools.maya.cmds.procCloth import *


print  "\n#========== CREATE CLASS 'FROM MEL' ==========#"
from tools.maya.cmds import riggMel, clothMel

class FromMel(riggMel.FromMel, clothMel.FromMel):

    def __init__(self):
        pass
