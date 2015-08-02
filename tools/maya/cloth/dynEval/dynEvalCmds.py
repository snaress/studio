import os, time
from lib.system import procFile as pFile
from tools.maya.cmds import pScene, pCloth, pCache
try:
    import maya.cmds as mc
except:
    pass


def mayaWarning(message):
    """
    Display maya warning
    :param message: Warning to print
    :type message: str
    """
    pScene.mayaWarning(message)

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

def getInfoText(nodeName, startFrame, stopFrame, cacheModeIndex, debTime, endTime):
    """
    Get info text
    :param nodeName: node shape name
    :type nodeName: str
    :param startFrame: NCloth cache start frame
    :type startFrame: int
    :param stopFrame: NCloth cache end frame
    :type stopFrame: int
    :param cacheModeIndex: NCloth node cacheable attributes index.
                           (-1=None, 0=positions, 1=velocities, 2=internalState)
    :type cacheModeIndex: int
    :param debTime: Cache file process start time
    :type debTime: int
    :param endTime: Cache file process end time
    :type endTime: int
    :return: Cache info text
    :rtype: list
    """
    return ['sceneName = "%s"' % mc.file(q=True, sn=True),
            'UserName = "%s"' % os.environ.get('username'),
            'DateTime = "%s -- %s"' % (pFile.getDate().replace('_', '/'),
                                       pFile.getTime().replace('_', ':')),
            'cacheType = "nCloth"',
            'nodeName = "%s"' % nodeName,
            'originalStartFrame = %s' % startFrame,
            'originalStopFrame = %s' % stopFrame,
            'cacheModeIndex = %s' % cacheModeIndex,
            'simulation = "%s"' % pFile.secondsToStr(endTime - debTime),
            'note = "No Comment !"']

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
                           (-1=None, 0=positions, 1=velocities, 2=internalState)
    :type cacheModeIndex: int
    :return: New cacheFile node
    :rtype: str
    """
    debTime = time.time()
    cacheNode = pCache.newNCacheFile(cachePath, fileName, clothNode, startFrame, stopFrame, rfDisplay,
                                     cacheModeIndex, newCacheNode=True)
    endTime = time.time()
    print "Creating cache file info ..."
    fileInfo = os.path.normpath(os.path.join(cachePath, '%s.py' % fileName))
    info = getInfoText(clothNode, startFrame, stopFrame, cacheModeIndex, debTime, endTime)
    pFile.writeFile(fileInfo, str('\n'.join(info)))
    if cacheNode is not None:
        cacheNode = mc.rename(cacheNode, 'dynEval_%s' % fileName.replace('-', '_'))
    return cacheNode

def delCacheNode(node):
    """
    Delected all cacheFile node connected to given node
    :param node: Maya node
    :type node: str
    """
    pCache.delCacheNode(node)
