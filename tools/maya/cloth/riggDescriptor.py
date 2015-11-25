import pprint
from tools.maya.cmds import pCloth
from tools.maya.cloth.clothBox import clothBoxCmds
try:
    import maya.cmds as mc
    import pymel.core as pm
except:
    pass


class Node(object):
    """
    RiggDescriptor common child object:

    :param nodeName: New node name
    :type nodeName: str
    :param nodeType: New node type ('nCloth', 'nRigid', 'dynamicConstraint')
    :type nodeType: str
    :param shapeName: New shape name
    :type shapeName: str
    :param parent: Parent object
    :type parent: Nucleus
    """

    _baseIndex0EnumFilter = ['inputAttractMethod', 'scalingRelation', 'evaluationOrder', 'bendSolver',
                             'timingOutput', 'pressureMethod']

    def __init__(self, nodeName, nodeType, shapeName, parent=None):
        print "---> %s ..." % nodeName
        self._parent = parent
        self.nodeName = nodeName
        self.nodeType = nodeType
        self.shapeName = shapeName
        self.presets = dict()
        self.vtxMaps = dict()

    def listAttrs(self):
        """
        List object attributes

        :return: Object attributes
        :rtype: list
        """
        return self.__dict__.keys()

    def getDatas(self, asString=False):
        """
        Get object datas

        :param asString: Translate object to string
        :type asString: bool
        :return: Object datas
        :rtype: dict
        """
        datas = dict()
        for k, v in self.__dict__.iteritems():
            if k == '_parent':
                if asString:
                    datas[k] = v.nodeName
                else:
                    datas[k] = v
            else:
                datas[k] = v
        return datas

    def buildFromScene(self, buildPresets=False, buildVtxMaps=False):
        """
        Build node from current scene

        :param buildPresets: Enable default attributes parsing
        :type buildPresets: bool
        :param buildVtxMaps: Enable vtxMaps parsing
        :type buildVtxMaps bool
        """
        self._buildInitMesh()
        self._buildInputMesh()
        self._buildDriverMesh()
        if buildPresets:
            self._buildPresets()
        if buildVtxMaps:
            self._buildVtxMaps()

    def _buildInitMesh(self):
        """
        Build node initMesh attribute from scene
        """
        if hasattr(self, 'initMesh'):
            print "\t ---> Init Mesh ..."
            initMesh = mc.listConnections('%s.restShapeMesh' % self.shapeName, s=True, d=False, shapes=True)
            if initMesh:
                self.initMesh = str(initMesh[0])
            else:
                self.initMesh = None

    def _buildInputMesh(self):
        """
        Build node inputMesh attribute from scene
        """
        if hasattr(self, 'inputMesh'):
            print "\t ---> Input Mesh ..."
            inputMesh = mc.listConnections('%s.inputMesh' % self.shapeName, s=True, d=False, shapes=True)
            if inputMesh:
                self.inputMesh = str(inputMesh[0])
            else:
                self.inputMesh = None

    def _buildDriverMesh(self):
        """
        Build node driverMesh attribute from scene
        """
        if hasattr(self, 'driverMesh'):
            print "\t ---> Driver Mesh ..."
            driverMesh = mc.listConnections('%s.inMesh' % self.inputMesh, s=True, d=False, shapes=True)
            driverName = mc.listRelatives(driverMesh, p=True)
            if driverMesh:
                self.driverName = str(driverName[0])
                self.driverMesh = str(driverMesh[0])
            else:
                self.driverName = None
                self.driverMesh = None

    def _buildPresets(self):
        """
        Build node presets attribute from scene
        """
        print "\t ---> Presets ..."
        self.presets = dict()
        for n in sorted(self.defaultAttrs.keys()):
            grp = self.defaultAttrs[n].keys()[0]
            for attr in self.defaultAttrs[n][grp]:
                self.presets[attr] = mc.getAttr("%s.%s" % (self.shapeName, attr))

    def _buildVtxMaps(self):
        """
        Build node vtxMaps attribute from scene
        """
        print "\t ---> Vertex Maps ..."
        self.vtxMaps = dict()
        for mapName in pCloth.getVtxMaps(self.shapeName):
            if pCloth.getVtxMapType(self.shapeName, '%sMapType' % mapName) == 1:
                self.vtxMaps['%sPerVertex' % mapName] = pCloth.getVtxMapData(self.shapeName, '%sPerVertex' % mapName)


class ClothNode(Node):

    def __init__(self, nodeName, nodeType, shapeName, parent=None):
        super(ClothNode, self).__init__(nodeName, nodeType, shapeName, parent=parent)
        self.initMesh = None
        self.inputMesh = None
        self.driverName = None
        self.driverMesh = None

    @property
    def defaultAttrs(self):
        """
        Get default cloth node attributes list

        :return: Cloth node attributes
        :rtype: dict
        """
        return {0: {'Collisions': ["collide", "selfCollide", "collisionFlag", "selfCollisionFlag",
                                   "collideStrength",  "collisionLayer", "thickness", "selfCollideWidthScale",
                                   "bounce", "friction", "stickiness"]},
                1: {'Dynamic': ["stretchResistance", "compressionResistance", "bendResistance", "bendAngleDropoff",
                                "shearResistance", "restitutionAngle", "restitutionTension", "rigidity",
                                "deformResistance", "usePolygonShells", "inputMeshAttract", "inputAttractMethod",
                                "inputAttractDamp", "inputMotionDrag", "restLengthScale", "bendAngleScale",
                                "pointMass", "lift", "drag", "tangentialDrag", "damp", "stretchDamp",
                                "scalingRelation", "ignoreSolverGravity", "ignoreSolverWind",
                                "localForce", "localWind"]},
                2: {'Pressure': ["pressureMethod", "pressure", "pressureDamping", "startPressure", "pumpRate",
                                 "airTightness", "incompressibility", "sealHoles"]},
                3: {'Quality': ["maxIterations", "maxSelfCollisionIterations", "collideLastThreshold",
                                "addCrossLinks", "evaluationOrder", "bendSolver", "sortLinks", "trappedCheck",
                                "selfTrappedCheck", "pushOut", "pushOutRadius", "crossoverPush",
                                "selfCrossoverPush"]}}

    def riggApply(self):
        mesh = mc.listRelatives(self.inputMesh, p=True)[0]
        # clothBoxCmds.createCloth(self.driverName, mesh, )


class RigidNode(Node):

    def __init__(self, nodeName, nodeType, shapeName, parent=None):
        super(RigidNode, self).__init__(nodeName, nodeType, shapeName, parent=parent)
        self.inputMesh = None

    @property
    def defaultAttrs(self):
        """
        Get default rigid node attributes list

        :return: Rigid node attributes
        :rtype: dict
        """
        return {0: {'Collisions': ["collide", "collisionFlag", "collideStrength", "collisionLayer",
                                   "thickness", "bounce", "friction", "stickiness"]},
                1: {'Quality': ["trappedCheck", "pushOut", "pushOutRadius", "crossoverPush"]}}


class ConstNode(Node):

    def __init__(self, nodeName, nodeType, shapeName, parent=None):
        super(ConstNode, self).__init__(nodeName, nodeType, shapeName, parent=parent)

    @property
    def defaultAttrs(self):
        """
        Get default dynConstraint node attributes list

        :return: DynConstraint node attributes
        :rtype: dict
        """
        return {}


class Nucleus(object):
    """
    RiggDescriptor root object:

    :param nodeName: New node name
    :type nodeName: str
    :param nodeType: New node type ('nucleus')
    :type nodeType: str
    :param parent: Parent object
    :type parent: RiggDescriptor
    """

    def __init__(self, nodeName, nodeType, parent=None):
        print "#--- %s ---#" % nodeName
        self._parent = parent
        self._children = []
        self.nodeName = nodeName
        self.nodeType = nodeType
        self.presets = dict()

    @property
    def defaultAttrs(self):
        """
        Get default nucleus node attributes list

        :return: Nucleus node attributes
        :rtype: dict
        """
        return {0: {'Gravity': ["gravity", "gravityDirection", "airDensity","windSpeed", "windDirection",
                                "windNoise"]},
                1: {'Solver': ["subSteps", "maxCollisionIterations", "collisionLayerRange", "timingOutput",
                               "useTransform"]},
                2: {'Scale': ["timeScale", "spaceScale"]}}

    @property
    def children(self):
        """
        Get children name string list

        :return: stored node names
        :rtype: list
        """
        childs = []
        for child in self._children:
            childs.append(child.nodeName)
        return childs

    def listAttrs(self):
        """
        List object attributes

        :return: Object attributes
        :rtype: list
        """
        return self.__dict__.keys()

    def getNode(self, nodeName, nodeType=None):
        """
        Get node object considering given nodeName and nodeType

        :param nodeName: Node name
        :type nodeName: str
        :param nodeType: Node type ('nCloth', 'nRigid', 'dynamicConstraint')
        :type nodeType: str
        :return: Matching nodes:
        :rtype: list
        """
        nodes = []
        for child in self._children:
            if child.nodeName == nodeName:
                if nodeType is None:
                    nodes.append(child)
                else:
                    if child.nodeType == nodeType:
                        nodes.append(child)
        return nodes

    def getNodesByType(self, nodeType):
        """
        Get child object considering given nodeType

        :param nodeType: Node type ('nCloth', 'nRigid', 'dynamicConstraint')
        :type nodeType: str
        :return: Child objects
        :rtype: list
        """
        nodes = []
        for child in self._children:
            if child.nodeType == nodeType:
                nodes.append(child)
        return nodes

    def getDatas(self, asString=False, recursive=False):
        """
        Get object datas

        :param asString: Translate object to string
        :type asString: bool
        :param recursive: Enable recursive parsing
        :type recursive: bool
        :return: Object datas
        :rtype: dict
        """
        datas = dict()
        for k, v in self.__dict__.iteritems():
            #-- Parent Object --#
            if k == '_parent':
                if hasattr(v, '_nucleus'):
                    datas[k] = None
                else:
                    if asString:
                        datas[k] = v.nodeName
                    else:
                        datas[k] = v
            #-- Child Object --#
            elif k == '_children':
                if not recursive:
                    if asString:
                        datas[k] = self.children
                    else:
                        datas[k] = self._children
                else:
                    datas[k] = dict()
                    for child in self._children:
                        datas[k][child.nodeName] = child.getDatas(asString=asString)
            #-- Other Object --#
            else:
                datas[k] = v
        return datas

    def addChild(self, nodeName, nodeType, shapeName):
        """
        Add child object to RiggRoot

        :param nodeName: New node name
        :type nodeName: str
        :param nodeType: New node type ('nCloth', 'nRigid', 'dynamicConstraint')
        :type nodeType: str
        :param shapeName: New shape name
        :type shapeName: str
        :return: New child object
        :rtype Node
        """
        if nodeType == 'nCloth':
            newChild = ClothNode(nodeName, nodeType, shapeName, parent=self)
        elif nodeType == 'nRigid':
            newChild = RigidNode(nodeName, nodeType, shapeName, parent=self)
        elif nodeType == 'dynamicConstraint':
            newChild = ConstNode(nodeName, nodeType, shapeName, parent=self)
        else:
            newChild = None
        if newChild is not None:
            self._children.append(newChild)
            return newChild
        log = "!!! Unrecognise nodeType: %s (should be 'nCloth', 'nRigid' or 'dynamicConstraint')" % nodeType
        raise TypeError(log)

    def buildFromScene(self, buildPresets=False, buildVtxMaps=False):
        """
        Build root from current scene

        :param buildPresets: Enable default attributes parsing
        :type buildPresets: bool
        :param buildVtxMaps: Enable vtxMaps parsing
        :type buildVtxMaps bool
        """
        #-- Nucleus Presets --#
        self.presets = dict()
        if buildPresets:
            self._buildPresets()
        #-- Nucleus Children --#
        nodes = []
        self._children = []
        links = pm.listConnections(self.nodeName, s=True, d=False, p=True, c=True)
        for link in links:
            #-- Dst Info --#
            dst = link[1]
            dstShape = dst.split('.')[0]
            nodeType = mc.nodeType(dstShape)
            #-- Parse nBase nodes --#
            if nodeType in ['nCloth', 'nRigid', 'dynamicConstraint']:
                dstNode = mc.listRelatives(dstShape, p=True)[0]
                if not dstNode in nodes:
                    nodes.append(dstNode)
                    newChild = self.addChild(str(dstNode), str(nodeType), str(dstShape))
                    newChild.buildFromScene(buildPresets=buildPresets, buildVtxMaps=buildVtxMaps)

    def _buildPresets(self):
        """
        Build node presets from scene
        """
        for n in sorted(self.defaultAttrs.keys()):
            grp = self.defaultAttrs[n].keys()[0]
            for attr in self.defaultAttrs[n][grp]:
                self.presets[attr] = mc.getAttr("%s.%s" % (self.nodeName, attr))

    def riggApply(self):
        print "#----- Rigg Apply: %s -----#" % self.nodeName
        for child in self.getNodesByType('nCloth'):
            print child.nodeName


class RiggDescriptor(object):
    """
    RiggDescriptor main class:

    Decompose, read, edit, write cloth datas
    """

    def __init__(self):
        print "\n########## RIGG DESCRIPTOR ##########"
        self._nucleus = []

    def getFileRepr(self, asString=False, recursive=False):
        """
        Translate to writable string

        :return: Writable string
        :rtype: str
        """
        rdDict = {}
        for n, nucleus in enumerate(self._nucleus):
            rdDict[n] = {nucleus.nodeName: nucleus.getDatas(asString=asString, recursive=recursive)}
        return pprint.pformat(rdDict)

    @property
    def nucleus(self):
        """
        get nucleus name string list

        :return: Stored nucleus name
        :rtype: list
        """
        nucleusList = []
        for node in self._nucleus:
            nucleusList.append(node.nodeName)
        return  nucleusList

    @property
    def allNucleus(self):
        """
        Get all nucleus in scene

        :return: Nucleus nodes
        :rtype: list
        """
        return pCloth.getAllNucleus()

    def getNucleus(self, nucleusName):
        """
        Get nucleus object matching with given nucleusName

        :param nucleusName: Nucleus name
        :type nucleusName: str
        :return: Nucleus object
        :rtype: Nucleus
        """
        for nucleus in self._nucleus:
            if nucleus.nodeName == nucleusName:
                return nucleus

    def getNode(self, nodeName, nodeType=None, nucleusName=None):
        """
        Get node matching nodeName, nodeType and nucleus

        :param nodeName: Node name
        :type nodeName: str
        :param nodeType: Node type ('nCloth', 'nRigid', 'dynamicConstraint')
        :type nodeType: str
        :param nucleusName: Nucleus name
        :type nucleusName: str
        :return: Matching nodes
        :rtype: list
        """
        #-- Get Nucleus List --#
        if nucleusName is not None:
            nucObj = self.getNucleus(nucleusName)
            if nucObj is None:
                print "!!! WARNING: Nucleus object not found: %s !!!" % nucleusName
                nucObjList = []
            else:
                nucObjList = [nucObj]
        else:
            nucObjList = self._nucleus
        #-- Parse Nucleus List --#
        nodes = []
        for nucleus in nucObjList:
            nodes.extend(nucleus.getNode(nodeName, nodeType=nodeType))
        return nodes

    def addNucleus(self, nodeName, nodeType):
        """
        Add root object to RiggDescriptor

        :param nodeName: New node name
        :type nodeName: str
        :param nodeType: New node type ('nucleus')
        :type nodeType: str
        :return: New root object
        :rtype Nucleus
        """
        nucleusObject = Nucleus(nodeName, nodeType, parent=self)
        self._nucleus.append(nucleusObject)
        return nucleusObject

    def buildFromScene(self, buildPresets=False, buildVtxMaps=False):
        """
        Build roots from current scene

        :param buildPresets: Enable default attributes parsing
        :type buildPresets: bool
        :param buildVtxMaps: Enable vtxMaps parsing
        :type buildVtxMaps bool
        """
        print "\n#========== Decompose Rigg ==========#"
        self._nucleus = []
        for nucleus in self.allNucleus:
            newNucleus = self.addNucleus(str(nucleus), 'nucleus')
            newNucleus.buildFromScene(buildPresets=buildPresets, buildVtxMaps=buildVtxMaps)

    def riggApply(self):
        print "\n#========== Rigg Apply ==========#"
        for nucleus in self._nucleus:
            nucleus.riggApply()
