
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

# from tools.maya.cmds import rigg, cloth
# from tools.maya.cmds import modeling as mode
# from tools.maya.cmds import procModeling as pMode
# from tools.maya.cmds import procCloth as pCloth
#
# #======================================================================================#
# #====================================== MODELING ======================================#
# #======================================================================================#
#
# def getBboxInfoFromMesh(mesh):
#     """ Get boundingBox info from given mesh
#         :param mesh: Mesh name
#         :type mesh: str
#         :return: Bbox info {'bbox', 'pMin', 'pMax', 'x', 'y', 'z', 'surfaceArea'}
#         :rtype: dict """
#     return mode.getBboxInfoFromMesh(mesh)
#
# def getInfoFromBbox(bbox):
#     """ Get boundingBox info from bbox values
#         :param bbox: BoundingBox values (Xmin, Ymin, Zmin, Xmax, Ymax, Zmax)
#         :type bbox: list
#         :return: Bbox info {'bbox', 'pMin', 'pMax', 'x', 'y', 'z', 'surfaceArea'}
#         :rtype: dict """
#     return mode.getInfoFromBbox(bbox)
#
# def creeBoxOnSelected(name=None, multi=False, returnShape=False):
#     """ Create boundingBox around selected objects
#         :param name: New box name
#         :type name: str
#         :param multi: If true, create a box around each mesh
#         :type multi: bool
#         :param returnShape: Enable new bbox shape name return
#         :type returnShape: bool
#         :return: New boxes info {'bbox', 'boxInfo'}
#         :rtype: dict """
#     pMode.creeBoxOnSelected(name=name, multi=multi, returnShape=returnShape)
#
# def creeBoxOnNodes(meshes, name=None, multi=False, returnShape=False):
#     """ Create boundingBox around given meshes
#         :param meshes: Mesh nodes
#         :type meshes: list
#         :param name: New box name
#         :type name: str
#         :param multi: If true, create a box around each mesh
#         :type multi: bool
#         :param returnShape: Enable new bbox shape name return
#         :type returnShape: bool
#         :return: New boxes info {'bbox', 'boxInfo'}
#         :rtype: dict """
#     pMode.creeBoxOnNodes(meshes, name=name, multi=multi, returnShape=returnShape)
#
# def creeBox(bboxDict=None, name=None, returnShape=False):
#     """ Create a boundingBox from given bounding box dict
#         :param bboxDict: Mesh bbox info
#         :type bboxDict: dict
#         :param name: Name of the new bbox
#         :type name: str
#         :param returnShape: Enable new bbox shape name return
#         :type returnShape: bool
#         :return: New bbox transform ans shape name
#         :rtype: (str, str) """
#     pMode.creeBox(bboxDict=bboxDict, name=name, returnShape=returnShape)
#
# #======================================================================================#
# #======================================== RIGG ========================================#
# #======================================================================================#
#
# def listTransforms(mesh):
#     """ get transform from given mesh
#         :param mesh: Mesh node name
#         :type mesh: str
#         :return: Transform node
#         :rtype: list """
#     return rigg.listTransforms(mesh)
#
# def getPlugNode(connectionPlug):
#     """ Get plug node from given connection
#         :param connectionPlug: Connection plug
#         :type connectionPlug: str
#         :return: Plug node name
#         :rtype: str """
#     return rigg.getPlugNode(connectionPlug)
#
# def getPlugAttr(connectionPlug):
#     """ Get plug attribute from given connection
#         :param connectionPlug: Connection plug
#         :type connectionPlug: str
#         :return: Plug attribute name
#         :rtype: str """
#     return rigg.getPlugAttr(connectionPlug)
#
# def getNextFreeMultiIndex(attr, start=0):
#     """ Returns the next multi index that's available for the given destination attribute
#         :param attr:  Name of the multi attribute
#         :type attr: str
#         :param start: the first index to check from (use 0 if last index is not known)
#         :type start: int
#         :return: Available index
#         :rtype: int """
#     return rigg.getNextFreeMultiIndex(attr, start=start)
#
# def findTypeInHistory(obj, objType, future=False, past=False):
#     """ returns the node of the specified type that is the closest traversal to the input object
#         :param obj: Object name
#         :type obj: str
#         :param objType: Object type list
#         :type objType: list
#         :param future: Future depth
#         :type future: bool
#         :param past: Past depth
#         :type past: bool
#         :return: Closest node connected
#         :rtype: str """
#     return rigg.findTypeInHistory(obj, objType, future=future, past=past)
#
# def transfertWrapConns(wrapPlugs, newNode):
#     """ Given a list of wrap plugs, transfer the connections from
#         their current source to the given newNode.
#         :param wrapPlugs: Wrap connection plugs
#         :type wrapPlugs: list
#         :param newNode: Destination node
#         :type newNode: str """
#     rigg.transfertWrapConns(wrapPlugs, newNode)
#
# #======================================================================================#
# #======================================= CLOTH ========================================#
# #======================================================================================#
#
# def hideParticleAttrs(node):
#     """ Hides the particle attributes for the given nCloth/nRigid node,
#         so they won't show up in the channel box
#         :param node: nCloth or nRigir node name
#         :type node: str """
#     cloth.hideParticleAttrs(node)
#
# def hideAllParticleAttrs():
#     """ Hide the particle attrs for all the nBase nodes in the scene """
#     cloth.hideAllParticleAttrs()
#
# def getDefaultThickness(mesh, clothFlags=False, maxRatio=0.005, thicknessCoef=0.13, minWidth=0.0001):
#     """ Try to find a reasonnable thickness for given mesh
#         :param mesh: Shape name
#         :type mesh: str
#         :param clothFlags: Enable clothFlags return
#         :type clothFlags: bool
#         :param maxRatio: Ratio of width to bounding box size
#         :type maxRatio: float
#         :param thicknessCoef: Default thickness coef
#         :type thicknessCoef: float
#         :param minWidth: Min width for precision issues
#         :type minWidth: float
#         :return: Thicknass value, ClothFlags dict
#         :rtype: float | dict """
#     return cloth.getDefaultThickness(mesh, clothFlags=clothFlags, maxRatio=maxRatio,
#                                      thicknessCoef=thicknessCoef, minWidth=minWidth)
#
# def createNucleus():
#     """ Create a new nucleus node connected to scene time
#         :return: Nucleus node name
#         :rtype: str """
#     return cloth.createNucleus()
#
# def createNSystem():
#     """ If there is a nucleus node selected, return it, else, create a new one and return it
#         :return: Nucleus node name
#         :rtype: str """
#     return cloth.createNSystem()
#
# def addActiveToNSystem(active, nucleus):
#     """ Connect nCloth or nRigid to given nucleus
#         :param active: nCloth or nRigid node
#         :type active: str
#         :param nucleus: Nucleus node
#         :type nucleus: str
#         :return: InputActive attribute index
#         :rtype: int """
#     return cloth.addActiveToNSystem(active, nucleus)
#
# def getActiveNucleus(selectExisting=False, createNew=False):
#     """ Find the currently active nucleus node, if none found, execute kargs
#         :param selectExisting: select the first existing one, if any
#         :type selectExisting: bool
#         :param createNew: force the creation of a new one
#         :type createNew: bool
#         :return: Active nucleus node
#         :rtype: str """
#     GetNuc = cloth.GetActiveNucleusNode()
#     return GetNuc.getActiveNucleus(selectExisting=selectExisting, createNew=createNew)
#
# def getClothNode(nodeName):
#     """ Try to find cloth node connected to given object
#         :param nodeName: Transform or Mesh node name
#         :type nodeName: str
#         :return: Cloth node name
#         :rtype: str """
#     return pCloth.getClothNode(nodeName)
#
# def getClothNodeFromSelected():
#     """ Try to find cloth nodes connected to selected objects
#         :return: Cloth node names
#         :rtype: list """
#     return pCloth.getClothNodeFromSelected()
#
# def getVtxMaps(clothNode):
#     """ Get vertex map list from given clothNode
#         :param clothNode: Cloth node name
#         :type clothNode: str
#         :return: Vertex map list
#         :rtype: list """
#     return pCloth.getVtxMaps(clothNode)
#
# def getVtxMapType(clothNode, mapType):
#     """ Get given clothNode vtxMap type
#         :param clothNode: Cloth node name
#         :type clothNode: str
#         :param mapType: Cloth node vtxMap name (must ends with 'MapType')
#         :type mapType: str
#         :return: VtxMap type (0 = None, 1 = Vertex, 2 = Texture)
#         :rtype: int """
#     return pCloth.getVtxMapType(clothNode, mapType)
#
# def setVtxMapType(clothNode, mapType, value):
#     """ Set given clothNode vtxMap value
#         :param clothNode: Cloth shape node name
#         :type clothNode: str
#         :param mapType: Cloth node vtxMap name (must ends with 'MapType')
#         :type mapType: str
#         :param value: VtxMap type (0 = None, 1 = Vertex, 2 = Texture)
#         :type value: int
#         :return: True if success, else False
#         :rtype: bool """
#     return pCloth.setVtxMapType(clothNode, mapType, value)
#
# def getVtxMapData(clothNode, vtxMap):
#     """ Get vertex map influence per vertex
#         :param clothNode: Cloth node name
#         :type clothNode: str
#         :param vtxMap: Vertex map name (must ends with 'PerVertex')
#         :type vtxMap: str
#         :return: Influence list per vertex
#         :rtype: list """
#     return pCloth.getVtxMapData(clothNode, vtxMap)
#
# def setVtxMapData(clothNode, vtxMap, value, refresh=False):
#     """ Set vertex map influence per vertex
#         :param clothNode: Cloth node name
#         :type clothNode: str
#         :param vtxMap: Vertex map name (must ends with 'PerVertex')
#         :type vtxMap: str
#         :param value: Influence list per vertex
#         :type value: list
#         :param refresh: Refresh maya ui
#         :type refresh: bool """
#     return pCloth.setVtxMapData(clothNode, vtxMap, value, refresh=refresh)
#
# def getModelFromClothNode(clothNode):
#     """ Get model from given clothNode
#         :param clothNode: Cloth node name
#         :type clothNode: str
#         :return: Connected model
#         :rtype: str """
#     return pCloth.getModelFromClothNode(clothNode)
#
# def getModelSelectedVtx(clothNode, indexOnly=False):
#     """ Get selected vertex on model
#         :param clothNode: Cloth node name
#         :type clothNode: str
#         :param indexOnly: If True, return index only, else fullName
#         :type indexOnly: bool
#         :return: selection list
#         :rtype: list """
#
#
# #======================================================================================#
# #====================================== FROM MEL ======================================#
# #======================================================================================#
#
# class FromMel(rigg.FromMel, cloth.FromMel):
#     """ NCloth commands calling mel script """
#
#     def __init__(self):
#         pass
#
