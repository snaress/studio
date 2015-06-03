from tools.maya.cmds import pRigg, pCloth
try:
    import maya.cmds as mc
except:
    pass


def getSceneSelection():
    """ Get scene selection
        :return: Scene selection list
        :rtype: list """
    return mc.ls(sl=True)

def getParentTransform(mesh):
    """ get transform from given mesh
        :param mesh: Mesh node name
        :type mesh: str
        :return: Transform node
        :rtype: list """
    return pRigg.listTransforms(mesh)

def findtype(nodeName, typeList):
    """ Get connected nodes with matching type
        :param nodeName: Dynamic constraint name
        :type nodeName: str
        :param typeList:
        :return: Matching type nodes
        :rtype: list """
    return pRigg.findTypeInHistory(nodeName, typeList, future=True, past=True)

def duplicateSelected(selObjects=None, name=None, worldParent=True):
    """ Duplicate and parent to world selected objects
        :param selObjects: Objects to duplicate.
                           If None, duplicate selected scene nodes.
        :type selObjects: str | list
        :param name: New object name
        :type name: str
        :param worldParent: Parent new object to world
        :type worldParent: bool
        :return: Duplicate objects
        :rtype: list """
    #-- Check Object List --#
    if selObjects is None:
        objectList = mc.ls(sl=True)
    else:
        if isinstance(selObjects, str):
            objectList = [selObjects]
        else:
            objectList = selObjects
    #-- Duplicate Objects --#
    cpList = []
    for obj in objectList:
        if name is None:
            cpName = "%s__cp#" % obj.split(':')[-1].split('__')[0]
        else:
            cpName = name
        cpObject = mc.duplicate(obj, n=cpName)
        newName = cpObject[0]
        #-- Parent To World --#
        if worldParent:
            if mc.listRelatives(cpObject[0], p=True) is not None:
                newName = mc.parent(cpObject[0], w=True)
        cpList.append(newName)
    return cpList

def connectOutMesh(srcMesh=None, outMesh=None, force=True):
    """ Connect srcMesh.outMesh to outMesh.inMesh
        :param srcMesh: Source mesh
        :type srcMesh: str
        :param outMesh: Out mesh
        :type outMesh: str
        :param force: Force connection
        :type force: True """
    #-- Check Object List --#
    if srcMesh is None and outMesh is None:
        selObjects = mc.ls(sl=True)
        if not selObjects:
            print "!!! Error: Select srcMesh, then outMesh !!!"
        else:
            srcMesh = selObjects[0]
            outMesh = selObjects[1]
    #-- Connect Attr --#
    ind = pRigg.getNextFreeMultiIndex("%s.worldMesh" % srcMesh)
    mc.connectAttr("%s.worldMesh[%s]" % (srcMesh, ind), "%s.inMesh" % outMesh, f=force)
    print "// Connect %s.worldMesh ---> %s.inMesh" % (srcMesh, outMesh)

def updateOutMesh(srcMesh=None, outMesh=None, force=True):
    """ Update given outMesh, then remove connection
        :param srcMesh: Source mesh
        :type srcMesh: str
        :param outMesh: Out mesh
        :type outMesh: str
        :param force: Force connection
        :type force: True """
    #-- Check Object List --#
    if srcMesh is None and outMesh is None:
        selObjects = mc.ls(sl=True)
        print selObjects
        if not selObjects:
            print "!!! Error: Select srcMesh, then outMesh !!!"
        else:
            srcMesh = selObjects[0]
            outMesh = selObjects[1]
    #-- Update Mesh --#
    connectOutMesh(srcMesh, outMesh, force=force)
    mc.refresh()
    mc.disconnectAttr("%s.outMesh" % srcMesh, "%s.inMesh" % outMesh)
    print "// Update %s.outMesh ---> %s.inMesh" % (srcMesh, outMesh)

def createOutMesh(selObjects=None, name=None, worldParent=True):
    """ Create outMesh from selected objects
        :param selObjects: Objects to duplicate and connect.
                           If None, duplicate selected scene nodes.
        :type selObjects: str | list
        :param name: New object name
        :type name: str
        :param worldParent: Parent new object to world
        :type worldParent: bool
        :return: OutMesh objects
        :rtype: list """
    #-- Check Object List --#
    if selObjects is None:
        selObjects = mc.ls(sl=True)
    else:
        if isinstance(selObjects, str):
            selObjects = [selObjects]
    #-- Create OutMesh --#
    outList = []
    for obj in selObjects:
        if name is None:
            outName = "%s__out#" % obj.split(':')[-1].split('__')[0]
        else:
            outName = name
        outMesh = duplicateSelected(selObjects=str(obj), name=str(outName), worldParent=worldParent)[0]
        if isinstance(outMesh, list):
            connectOutMesh(srcMesh=str(obj), outMesh=str(outMesh[0]))
            outList.append(outMesh[0])
        else:
            connectOutMesh(srcMesh=str(obj), outMesh=str(outMesh))
            outList.append(outMesh)
    return outList

def getAllNucleus():
    """ Get all nucleus in scene
        :return: Nucleus nodes
        :rtype: list """
    return mc.ls(type='nucleus')

def createSimuGroups():
    """ Create Simulation groups """
    grpList = ["|ALL|SIMU",
               "|ALL|SIMU|CLOTH",
               "|ALL|SIMU|CLOTH|RIGG_CLOTH",
               "|ALL|SIMU|CLOTH|RIGG_CLOTH|initMesh",
               "|ALL|SIMU|CLOTH|RIGG_CLOTH|inputMesh",
               "|ALL|SIMU|CLOTH|RIGG_CLOTH|wrapBase",
               "|ALL|SIMU|CLOTH|EXPORT_CLOTH",
               "|ALL|SIMU|CLOTH|EXPORT_CLOTH|loToHi",
               "|ALL|SIMU|CLOTH|EXPORT_CLOTH|hiMesh",
               "|ALL|SIMU|HAIR"]
    for grp in grpList:
        if not mc.objExists(grp):
            print "\t ---> Create group %r" % grp
            mc.group(n=grp.split('|')[-1], p='|'.join(grp.split('|')[:-1]), em=True)

def createClothGroups(grpName):
    """ Create nClothGroup
        :param grpName: Cloth group name
        :type grpName: str
        :return: ClothGroup full name
        :rtype: str """
    clothGrp = "|ALL|SIMU|CLOTH|%s" % grpName
    if not mc.objExists(clothGrp):
        print "\t ---> Create group %s" % clothGrp
        clothGrp = mc.group(n=grpName, p="|ALL|SIMU|CLOTH", em=True)
        mc.reorder(clothGrp, r=-2)
    return clothGrp

def createRigidGroups(clothGrp, grpName):
    """ Create nRigidGroup
        :param clothGrp: Cloth group name
        :type clothGrp: str
        :param grpName: Rigid group name
        :type grpName: str
        :return: RigidGroup full name
        :rtype: str """
    rigidGrp = "%s|%s" % (clothGrp, grpName)
    if not mc.objExists(rigidGrp):
        print "\t ---> Create group %s" % rigidGrp
        rigidGrp = mc.group(n=grpName, p=clothGrp, em=True)
    return rigidGrp

def createClothInitMesh(mesh):
    """ Create cloth initMesh
        :param mesh: ClothMesh name
        :type mesh: str
        :return: InitMesh name
        :rtype: str """
    initMesh = duplicateSelected(selObjects=mesh, name="%s_initMsh" % mesh)[0]
    mc.parent(initMesh, "|ALL|SIMU|CLOTH|RIGG_CLOTH|initMesh")
    return initMesh

def createClothInputMesh(driver, mesh):
    """ Create cloth inputMesh
        :param driver: Cloth driver mesh name
        :type driver: str
        :param mesh: ClothMesh name
        :type mesh: str
        :return: InputMesh name
        :rtype: str """
    if mc.polyEvaluate(driver, v=True) == mc.polyEvaluate(mesh, v=True):
        print "\t ---> Use outMesh driver"
        inputMesh = driver
    else:
        print "\t ---> Use wrap driver"
        inputMesh = duplicateSelected(selObjects=mesh, name="%s_inputMsh" % mesh)[0]
        mc.parent(inputMesh, "|ALL|SIMU|CLOTH|RIGG_CLOTH|inputMesh")
        baseName, wrapNode = pRigg.createWrap(driver, inputMesh)
        mc.parent(baseName, "|ALL|SIMU|CLOTH|RIGG_CLOTH|wrapBase")
    return inputMesh

def _checkClothArgs(driver, mesh, result, solver):
    """ Check cloth args
        :param driver: Cloth driver mesh name
        :type driver: str
        :param mesh: ClothMesh name
        :type mesh: str
        :param result: Cloth mesh name
        :type result: str
        :param solver: Nucleus name, or 'New Nucleus' to create a new one"""
    if not mc.objExists(driver):
        raise ValueError, "!!! Cloth driver not found: %s !!!" % driver
    if not mc.objExists(mesh):
        raise ValueError, "!!! Cloth mesh not found: %s !!!" % mesh
    if mc.objExists(result):
        raise ValueError, "!!! Cloth mesh already exists: %s !!!" % result
    if not solver == "New Nucleus":
        if not mc.objExists(solver):
            raise ValueError, "!!! Cloth solver not found: %s !!!" % solver

def createCloth(driver, mesh, clothMesh, solver):
    """ Create cloth system
        :param driver: Cloth driver mesh name
        :type driver: str
        :param mesh: Cloth slave mesh name
        :type mesh: str
        :param clothMesh: Cloth mesh name
        :type clothMesh: str
        :param solver: Nucleus name, or 'New Nucleus' to create a new one
        :type solver: str """
    print "\n########## CREATE CLOTH ##########"
    #-- Verif Args --#
    print "Checking Values ..."
    _checkClothArgs(driver, mesh, clothMesh, solver)
    #-- Create Simu Groups --#
    print "Checking Simu Groups ..."
    createSimuGroups()
    #-- Create Cloth --#
    print "Creating Cloth Mesh ..."
    duplicateSelected(selObjects=mesh, name=clothMesh)
    defaultName = clothMesh.replace('_mesh', '')
    if solver == "New Nucleus":
        #-- Create Cloth Group --#
        print "Checking Cloth Groups ..."
        clothGrp = createClothGroups("GRP_%s" % defaultName)
        #-- Create ClothNodes --#
        print "\t ---> New Nucleus"
        mc.select(clothMesh, r=True)
        clothNodes = pCloth.createNCloth(createNew=True, outMeshName="%s_outputCloth" % mesh)
        nucleus = pRigg.findTypeInHistory(clothNodes[0], ['nucleus'], future=True, past=True)
        nucleus = mc.rename(nucleus, "%s_nucleus" % defaultName)
        mc.parent(nucleus, clothGrp)
    else:
        #-- Create ClothNodes --#
        print "\t ---> Use Nucleus: %s" % solver
        mc.select(clothMesh, r=True)
        clothNodes = pCloth.createNCloth(useNucleus=solver, outMeshName="%s_outputCloth" % mesh)
        nucleus = pRigg.findTypeInHistory(clothNodes[0], ['nucleus'], future=True, past=True)[0]
        clothGrp = pRigg.listTransforms(nucleus)
    clothNode = pRigg.listTransforms(clothNodes[0])
    clothNode = mc.rename(clothNode, "%s_nCloth" % defaultName)
    mc.parent(clothMesh, clothGrp)
    mc.parent(clothNode, clothGrp)
    print "\t ---> Nucleus: %s" % nucleus
    print "\t ---> ClothNode: %s" % clothNode
    print "\t ---> ClothMesh: %s" % clothMesh
    #-- Create InitMesh --#
    print "Creating Init Mesh ..."
    clothNodeShape = pCloth.getClothNode(clothNode)[0]
    initMesh = createClothInitMesh(mesh)
    mc.connectAttr("%s.worldMesh[0]" % initMesh, "%s.restShapeMesh" % clothNodeShape, f=True)
    print "\t ---> %s" % initMesh
    #-- Create InputMesh --#
    print "Creating Input Mesh ..."
    inputMesh = createClothInputMesh(driver, mesh)
    meshShape = mc.listRelatives(clothMesh, s=True, ni=False)[0]
    connectOutMesh(srcMesh=inputMesh, outMesh=meshShape)
    print "\t ---> %s" % inputMesh

def paramRigidMode(rigidNode, rigidMode):
    """ Param rigidNode mode
        :param rigidNode: RigidNode name
        :type rigidNode: str
        :param rigidMode: Rigid mode ('collide', 'pushOut', 'passive')
        :type rigidMode: str """
    rigidNodeShape = pCloth.getClothNode(rigidNode)[0]
    mc.setAttr("%s.pushOut" % rigidNodeShape, 0.08)
    mc.setAttr("%s.pushOutRadius" % rigidNodeShape, 0.2)
    if rigidMode == 'collide':
        mc.setAttr("%s.collide" % rigidNodeShape, True)
        mc.setAttr("%s.trappedCheck" % rigidNodeShape, True)
    elif rigidMode == 'pushOut':
        mc.setAttr("%s.collide" % rigidNodeShape, False)
        mc.setAttr("%s.trappedCheck" % rigidNodeShape, True)
    elif rigidMode == 'passive':
        mc.setAttr("%s.collide" % rigidNodeShape, False)
        mc.setAttr("%s.trappedCheck" % rigidNodeShape, False)
        mc.setAttr("%s.pushOut" % rigidNodeShape, 0.0)
        mc.setAttr("%s.pushOutRadius" % rigidNodeShape, 0.0)

def createRigid(driver, mesh, rigidMesh, rigidMode, solver):
    """ Create rigid system
        :param driver: Passive driver mesh name
        :type driver: str
        :param mesh: Passive slave mesh name
        :type mesh: str
        :param rigidMesh: Passive mesh name
        :type rigidMesh: str
        :param rigidMode: Rigid mode ('collide', 'pushOut', 'passive')
        :type rigidMode: str
        :param solver: Nucleus name, or 'New Nucleus' to create a new one
        :type solver: str """
    print "\n########## CREATE RIGID ##########"
    #-- Verif Args --#
    print "Checking Values ..."
    _checkClothArgs(driver, mesh, rigidMesh, solver)
    #-- Create Rigid --#
    duplicateSelected(selObjects=mesh, name=rigidMesh)
    defaultName = rigidMesh.replace('_pass', '')
    if solver == "New Nucleus":
        #-- Create Cloth Group --#
        print "Checking Cloth Groups ..."
        clothGrp = createClothGroups("GRP_%s" % defaultName)
        #-- Create RigidNodes --#
        print "\t ---> New Nucleus"
        mc.select(rigidMesh, r=True)
        rigidNodes = pCloth.createNRigid(createNew=True)
        nucleus = pRigg.findTypeInHistory(rigidNodes[0], ['nucleus'], future=True, past=True)
        nucleus = mc.rename(nucleus, "%s_nucleus" % defaultName)
        mc.parent(nucleus, clothGrp)
        #-- Create Passive Group --#
        print "Checking Rigid Group ..."
        rigidGrp = createRigidGroups(clothGrp, "%s_passive" % clothGrp)
    else:
        #-- Create RigidNodes --#
        print "\t ---> Use Nucleus: %s" % solver
        mc.select(rigidMesh, r=True)
        rigidNodes = pCloth.createNRigid(useNucleus=solver)
        nucleus = pRigg.findTypeInHistory(rigidNodes[0], ['nucleus'], future=True, past=True)[0]
        clothGrp = pRigg.listTransforms(nucleus)[0]
        #-- Create Passive Group --#
        print "Checking Rigid Group ..."
        rigidGrp = createRigidGroups(clothGrp, "%s_passive" % clothGrp)
        createRigidGroups(clothGrp, "%s_component" % clothGrp)
    rigidNode = pRigg.listTransforms(rigidNodes[0])
    rigidNode = mc.rename(rigidNode, "%s_nRigid" % defaultName)
    mc.parent(rigidMesh, rigidGrp)
    mc.parent(rigidNode, rigidGrp)
    print "\t ---> Nucleus: %s" % nucleus
    print "\t ---> RigidNode: %s" % rigidNode
    print "\t ---> RigidMesh: %s" % rigidMesh
    #-- Connect Driver --#
    print "Connecting driver ..."
    connectOutMesh(srcMesh=driver, outMesh=rigidMesh)
    print "\t %s ---> %s" % (driver, rigidMesh)
    #-- Edit Mode --#
    print "Editing Rigid Node ..."
    paramRigidMode(rigidNode, rigidMode)
    print "\t ---> %s" % rigidMode

def _checkConstArgs(dynConst, constName):
    """ Check cloth args
        :param dynConst: Dynamic constraint name
        :type dynConst: str
        :param constName: Dynamic constraint result name
        :type constName: str """
    if not mc.objExists(dynConst):
        raise ValueError, "!!! Dynamic constraint not found: %s !!!" % dynConst
    if mc.objExists(constName):
        raise ValueError, "!!! Dynamic constraint already exists: %s !!!" % constName

def storeConstraint(dynConst, constName):
    print "\n########## STORE CONSTRAINT ##########"
    #-- Verif Args --#
    print "Checking Values ..."
    _checkConstArgs(dynConst, constName)
    #-- Create Component Group --#
    nucleus = findtype(dynConst, ['nucleus'])[0]
    clothGrp = getParentTransform(nucleus)[0]
    constGrp = createRigidGroups(clothGrp, "%s_component" % clothGrp.replace('GRP_', ''))
    const = mc.rename(dynConst, constName)
    mc.parent(const, constGrp)