import os, time, shutil
from lib.system import procFile as pFile
from tools.maya.cmds import pScene, pMode, pCloth, pCache
try:
    import maya.cmds as mc
    import maya.mel as ml
except:
    pass


def mayaWarning(message):
    """
    Display maya warning
    :param message: Warning to print
    :type message: str
    """
    pScene.mayaWarning(message)

def mayaError(message):
    """
    Display maya error
    :param message: Error to print
    :type message: str
    """
    pScene.mayaError(message)

def getAttr(nodeName, nodeAttr):
    """
    Get given nodeAttr value
    :param nodeName: Node full name
    :type nodeName: str
    :param nodeAttr: Node attribute
    :type nodeAttr: str
    :return: Node attribute value
    :rtype: float | list
    """
    if mc.objExists("%s.%s" % (nodeName, nodeAttr)):
        return mc.getAttr("%s.%s" % (nodeName, nodeAttr))

def setAttr(nodeName, nodeAttr, value):
    """
    set given nodeAttr value
    :param nodeName: Node full name
    :type nodeName: str
    :param nodeAttr: Node attribute
    :type nodeAttr: str
    :param value: Node attriute value
    :type value: int | float | list | tuple
    """
    node = "%s.%s" % (nodeName, nodeAttr)
    if mc.objExists(node):
        if mc.getAttr(node, type=True) == 'float3':
            mc.setAttr("%s.%s" % (nodeName, nodeAttr), value[0], value[1], value[2])
        else:
            mc.setAttr("%s.%s" % (nodeName, nodeAttr), value)

def getNamespace(nodeName, returnList=False):
    """
    Get given node namespace
    :param nodeName: Node full name
    :type nodeName: str
    :param returnList: Return result as list instead of str
    :return: Node namespace, Node name
    :rtype: (str | list, str)
    """
    ns, name = pScene.getNamespace(nodeName, returnList=returnList)
    return ns, name

def getAllNucleus():
    """
    Get all nucleus in scene
    :return: Nucleus nodes
    :rtype: list
    """
    return mc.ls(type='nucleus')

def getNodeParent(nodeName):
    """
    Get given node parent (transform)
    :param nodeName: Node name
    :type nodeName: str
    :return: Node parent name (transform)
    :rtype: str
    """
    if mc.objExists(nodeName):
        parent = mc.listRelatives(nodeName, p=True)
        if parent:
            return parent[0]
        print "!!! WARNING: Parent not found for %s" % nodeName
    else:
        print "!!! WARNING: ClothNode not found for %s" % nodeName

def getSelectedNodes():
    """
    Get maya selected nodes
    :return: Maya selection
    :rtype: list
    """
    return mc.ls(sl=True, l=True)

def getNodeShape(nodeName):
    """
    Get given node shape (mesh)
    :param nodeName: Node name
    :type nodeName: str
    :return: Node parent name (transform)
    :rtype: str
    """
    if mc.objExists(nodeName):
        shape = mc.listRelatives(nodeName, s=True, ni=True)
        if shape:
            return shape[0]
        print "!!! WARNING: Shape not found for %s" % nodeName
    else:
        print "!!! WARNING: Node not found for %s" % nodeName

def getClothType(clothNode):
    """
    Get clothNode type
    :param clothNode: Cloth node name
    :type clothNode: str
    :return: Cloth node type ['nCloth', 'nRigid']
    :rtype: str
    """
    clothType = mc.nodeType(clothNode)
    if clothType in ['nucleus', 'nCloth', 'nRigid']:
        return clothType

def getModelFromClothNode(clothNode):
    """
    Get model from given clothNode
    :param clothNode: Cloth node name
    :type clothNode: str
    :return: Connected model
    :rtype: str
    """
    return pCloth.getModelFromClothNode(clothNode)

def selectModel(clothNode):
    """
    Select model from given clothNode
    :param clothNode: Cloth node name
    :type clothNode: str
    """
    if mc.nodeType(clothNode) == 'nucleus':
        model = clothNode
    else:
        model = getModelFromClothNode(clothNode)
    if mc.objExists(model):
        mc.select(model, r=True)

def getCurrentFrame():
    """
    Get current frame
    :return: Current frame
    :rtype: int
    """
    return int(mc.currentTime(q=True))

def getTimeRange():
    """
    Get scene time range
    :return: time range info
    :rtype: dict
    """
    return pScene.getTimeRange()

def getLastVersion(path):
    """
    Get last cache version
    :param path: Cache path
    :type path: str
    :return: Last version
    :rtype: str
    """
    #-- Check Path --#
    if not os.path.exists(path):
        return None
    #-- Get Versions --#
    folders = []
    for fld in os.listdir(path):
        vPath = os.path.join(path, fld)
        if os.path.isdir(vPath) and fld.startswith('v') and len(fld) == 4:
            folders.append(fld)
    if not folders:
        return None
    return max(folders)

def getNextVersion(path):
    """
    Get next available cache version
    :param path: Cache path
    :type path: str
    :return: Next version
    :rtype: str
    """
    #-- Check Path --#
    if not os.path.exists(path):
        return 'v001'
    #-- Result --#
    last = getLastVersion(path)
    if last is None:
        return 'v001'
    return 'v%s' % str(int(last[1:]) + 1).zfill(3)

def getCacheNodes(node):
    """
    Get cacheFile nodes connected to given node name
    :param node: Maya node
    :type node: str
    :return: CacheFile nodes
    :rtype: list
    """
    return pCache.getCacheNodes(node)

def deleteCacheNode(node):
    """
    Delected all cacheFile node connected to given node
    :param node: Maya node
    :type node: str
    """
    pCache.delCacheNode(node)

def writeInfoFile(cachePath, fileName, cacheType, nodeName, startFrame, stopFrame, cacheModeIndex, debTime, endTime):
    """
    Write cache info file
    :param cachePath: Geo cache path
    :type cachePath: str
    :param fileName: Geo cache file name
    :type fileName: str
    :param cacheType: Cache file type ('nCloth' or 'geo')
    :type cacheType: str
    :param nodeName: node shape name
    :type nodeName: str
    :param startFrame: NCloth cache start frame
    :type startFrame: int
    :param stopFrame: NCloth cache end frame
    :type stopFrame: int
    :param cacheModeIndex: NCloth node cacheable attributes index.
                           (0=positions, 1=velocities, 2=internalState)
    :type cacheModeIndex: int
    :param debTime: Cache file process start time
    :type debTime: int
    :param endTime: Cache file process end time
    :type endTime: int
    """
    print "Creating cache file info ..."
    info =  ['sceneName = "%s"' % mc.file(q=True, sn=True),
            'UserName = "%s"' % os.environ.get('username'),
            'DateTime = "%s -- %s"' % (pFile.getDate().replace('_', '/'),
                                       pFile.getTime().replace('_', ':')),
            'cacheType = "%s"' % cacheType,
            'nodeName = "%s"' % nodeName,
            'originalStartFrame = %s' % startFrame,
            'originalStopFrame = %s' % stopFrame,
            'cacheModeIndex = %s' % cacheModeIndex,
            'simulation = "%s"' % pFile.secondsToStr(endTime - debTime),
            'note = "No Comment !"']
    fileInfo = os.path.normpath(os.path.join(cachePath, '%s.py' % fileName))
    pFile.writeFile(fileInfo, str('\n'.join(info)))

def newNCacheFile(cachePath, fileName, clothNode, startFrame, stopFrame, rfDisplay, cacheModeIndex):
    """
    Create new cache files, attach new cacheNode, connect new cacheNode
    :param cachePath: NCloth cache path
    :type cachePath: str
    :param fileName: NCloth cache file name
    :type fileName: str
    :param clothNode: NCloth shape node name
    :type clothNode: str
    :param startFrame: NCloth cache start frame
    :type startFrame: int
    :param stopFrame: NCloth cache end frame
    :type stopFrame: int
    :param rfDisplay: Refresh maya display state
    :type rfDisplay: bool
    :param cacheModeIndex: NCloth node cacheable attributes index.
                           (0=positions, 1=velocities, 2=internalState)
    :type cacheModeIndex: int
    :return: New cacheFile node
    :rtype: str
    """
    debTime = time.time()
    cacheNode = pCache.nCacheFile(cachePath, fileName, clothNode, startFrame, stopFrame, rfDisplay,
                                  cacheModeIndex, newCacheNode=True)
    endTime = time.time()
    print "Simulation Duration: %s" % pFile.secondsToStr(endTime - debTime)
    writeInfoFile(cachePath, fileName, 'nCloth', clothNode, startFrame, stopFrame, cacheModeIndex, debTime, endTime)
    if cacheNode is not None:
        cacheNode = mc.rename(cacheNode, 'dynEval_%s' % fileName.replace('-', '_'))
    return cacheNode

def newGeoCacheFile(cachePath, fileName, shapeName, startFrame, stopFrame, rfDisplay):
    """
    Create new cache files, attach new cacheNode, connect new cacheNode
    :param cachePath: Geo cache path
    :type cachePath: str
    :param fileName: Geo cache file name
    :type fileName: str
    :param shapeName: Selected shape name
    :type shapeName: str
    :param startFrame: Geo cache start frame
    :type startFrame: int
    :param stopFrame: Geo cache end frame
    :type stopFrame: int
    :param rfDisplay: Refresh maya display state
    :type rfDisplay: bool
    :return: New cacheFile node
    :rtype: str
    """
    debTime = time.time()
    cacheNode = pCache.geoCacheFile(cachePath, fileName, shapeName, startFrame, stopFrame, rfDisplay,
                                    newCacheNode=True)
    endTime = time.time()
    print "Caching Duration: %s" % pFile.secondsToStr(endTime - debTime)
    writeInfoFile(cachePath, fileName, 'geo', shapeName, startFrame, stopFrame, 0, debTime, endTime)
    if cacheNode is not None:
        cacheNode = mc.rename(cacheNode, 'geoCache_%s' % fileName.replace('-', '_'))
    return cacheNode

def appendToNCacheFile(cachePath, fileName, clothNode, startFrame, stopFrame, rfDisplay, cacheModeIndex, backup=False):
    """
    Append to cache files
    :param cachePath: NCloth cache path
    :type cachePath: str
    :param fileName: NCloth cache file name
    :type fileName: str
    :param clothNode: NCloth shape node name
    :type clothNode: str
    :param startFrame: NCloth cache start frame
    :type startFrame: int
    :param stopFrame: NCloth cache end frame
    :type stopFrame: int
    :param rfDisplay: Refresh maya display state
    :type rfDisplay: bool
    :param cacheModeIndex: NCloth node cacheable attributes index.
                           (0=positions, 1=velocities, 2=internalState)
    :type cacheModeIndex: int
    :param backup: Enable cache file backup
    :type backup: bool
    """
    debTime = time.time()
    pCache.nCacheFile(cachePath, fileName, clothNode, startFrame, stopFrame, rfDisplay, cacheModeIndex,
                      modeAppend=True, noBackup=not backup)
    endTime = time.time()
    print "Simulation Duration: %s" % pFile.secondsToStr(endTime - debTime)

def assignNCacheFile(cachePath, fileName, clothNode, cacheModeIndex):
    """
    Assign given cache file to given nCloth node
    :param cachePath: NCloth cache path
    :type cachePath: str
    :param fileName: NCloth cache file name
    :type fileName: str
    :param clothNode: NCloth shape node name
    :type clothNode: str
    :param cacheModeIndex: NCloth node cacheable attributes index.
                           (0=positions, 1=velocities, 2=internalState)
    :type cacheModeIndex: int
    :return: New cacheFile node
    :rtype: str
    """
    deleteCacheNode(clothNode)
    cacheNode = pCache.newNCacheNode(cachePath, fileName, clothNode, cacheModeIndex)
    if cacheNode is not None:
        cacheNode = mc.rename(cacheNode, 'dynEval_%s' % fileName.replace('-', '_'))
    return cacheNode

def assignGeoCacheFile(cachePath, fileName, mesh):
    """
    Assign given cache file to given mesh node
    :param cachePath: NCloth cache path
    :type cachePath: str
    :param fileName: NCloth cache file name
    :type fileName: str
    :param mesh: mesh shape node name
    :type mesh: str
    :return: New cacheFile node
    :rtype: str
    """
    deleteCacheNode(mesh)
    cacheNode = pCache.newGeoCacheNode(cachePath, fileName, mesh)
    if cacheNode is not None:
        cacheNode = mc.rename(cacheNode, 'geoCache_%s' % fileName.replace('-', '_'))
    return cacheNode

def materializeCacheVersion(cachePath, fileName, mesh):
    """
    Materialize given cache version
    :param cachePath: NCloth cache path
    :type cachePath: str
    :param fileName: NCloth cache file name
    :type fileName: str
    :param mesh: mesh shape node name
    :type mesh: str
    :return: New cache file node
    :rtype: str
    """
    #-- Get Info --#
    cacheVersion = cachePath.split('/')[-1]
    print "Cache Path:", cachePath
    print "Cache Version:", cacheVersion
    print "Cache File:", fileName
    print "Mesh Name:", mesh
    if not mc.objExists(mesh):
        raise IOError, "!!! Mesh not found: %s !!!" % mesh
    #-- Materialize Cache Version --#
    newMesh = pMode.duplicateSelected(selObjects=str(mesh), name='%s_%s_##' % (mesh, cacheVersion))
    shapes = mc.listRelatives(newMesh[0], s=True, ni=True, f=True)
    newShape = mc.rename(shapes[0], '%s_OutShape'  % newMesh[0])
    cacheNode = assignGeoCacheFile(cachePath, fileName, newShape)
    #-- Result --#
    return cacheNode

def duplicateCacheVersion(cachePath, cacheVersion):
    """
    Duplicate given cache file version to next avalaible version
    :param cachePath: Cache file path (without version)
    :type cachePath: str
    :param cacheVersion: Cache version to duplicate
    :type cacheVersion: str
    :return: New cache version
    :rtype: str
    """
    #-- Get Info --#
    newVersion = getNextVersion(os.path.normpath(cachePath))
    print "Cache Path:", cachePath
    print "Cache Version:", cacheVersion
    print "Next Version:", newVersion
    #-- Create Version Folder --#
    dst = os.path.normpath(os.path.join(cachePath, newVersion))
    if os.path.exists(dst):
        raise IOError, "!!! New cache path already exists: %s !!!" % dst
    try:
        print "Creating new version folder: %s ..." % newVersion
        os.mkdir(dst)
    except:
        raise IOError, "!!! Can not make directory: %s !!!" % dst
    #-- Copy Cache Files --#
    src = os.path.normpath(os.path.join(cachePath, cacheVersion))
    cacheFiles = os.listdir(os.path.normpath(os.path.join(cachePath, cacheVersion)))
    for cacheFile in cacheFiles:
        if '-%s.' % cacheVersion in cacheFile:
            newCacheFile = cacheFile.replace(cacheVersion, newVersion)
            print "Copying %s ---> %s" % (cacheFile, newCacheFile)
            srcFile = os.path.join(src, cacheFile)
            dstFile = os.path.join(dst, newCacheFile)
            shutil.copy(srcFile, dstFile)
    #-- Result --#
    return newVersion

def assignCacheFileToSel(cachePath, fileName):
    """
    Assign given cache verion to selected mesh
    :param cachePath: NCloth cache path
    :type cachePath: str
    :param fileName: NCloth cache file name
    :type fileName: str
    :return: New cache file node
    :rtype: str
    """
    #-- Get Info --#
    print "Cache Path:", cachePath
    print "Cache File:", fileName
    sel = mc.ls(sl=True)
    if not len(sel) == 1:
        raise ValueError, "!!! Select only one node !!!"
    #-- Assign Cache Version --#
    shapes = mc.listRelatives(sel[0], s=True, ni=True, f=True)
    deleteCacheNode(shapes[0])
    cacheNode = assignGeoCacheFile(cachePath, fileName, shapes[0])
    #-- Result --#
    return  cacheNode

def deleteCacheVersion(cachePath):
    """
    Delete cache files
    :param cachePath: NCloth cache path
    :type cachePath: str
    """
    #-- Get Info --#
    rootPath = '/'.join(cachePath.split('/')[:-1])
    cacheVersion = cachePath.split('/')[-1]
    print "Cache Path:", cachePath
    print "Cache Root Path:", rootPath
    print "Cache Version:", cacheVersion
    if not os.path.exists(cachePath):
        raise IOError, "!!! Cache path not found: %s !!!" % cachePath
    #-- Delete Cache Node --#
    cacheNodes = mc.ls(type='cacheFile') or []
    for cNode in cacheNodes:
        if mc.getAttr('%s.cachePath' % cNode) == cachePath:
            deleteCacheNode(cNode)
    #-- Get Cache Files To Delete --#
    cacheFiles = os.listdir(cachePath) or []
    delList = []
    for cFile in cacheFiles:
        cFilePath = os.path.normpath(os.path.join(cachePath, cFile))
        if os.path.isfile(cFilePath):
            delList.append(cFilePath)
        elif os.path.isdir(cFilePath):
            raise IOError, "!!! Folder found in varsion path, can not clean!!!"
    #-- Delete Cache Files --#
    for delFile in delList:
        try:
            print "Deleting file %s ..." % delFile
            os.remove(delFile)
        except:
            raise IOError, "!!! Can not delete file: %s !!!" % delFile
    #-- Delete Cache Folder --#
    try:
        print "Deleting folder %s ..." % cacheVersion
        os.removedirs(cachePath)
    except:
        raise IOError, "!!! Can not delete folder: %s !!!" % cacheVersion
