from tools.maya.cmds import pRigg
try:
    import maya.cmds as mc
except:
    pass


def newNCacheNode(cachePath, fileName, clothNode, cacheModeIndex):
    """
    Create new cache node and connect it
    :param cachePath: NCloth cache path
    :type cachePath: str
    :param fileName: NCloth cache file name
    :type fileName: str
    :param clothNode: NCloth shape node name
    :type clothNode: str
    :return:New cacheFile node
    :rtype: str
    """
    #-- Create Cache Node --#
    if cacheModeIndex == 0:
        inAttr = '%s.positions' % clothNode
    elif cacheModeIndex == 1:
        inAttr = ['%s.positions' % clothNode, '%s.velocities' % clothNode]
    elif cacheModeIndex == 2:
        inAttr = ['%s.positions' % clothNode, '%s.velocities' % clothNode, '%s.internalState' % clothNode]
    else:
        inAttr = '%s.positions' % clothNode
    cacheNode = mc.cacheFile(dir=cachePath, f=fileName, ccn=True, ia=inAttr)
    #-- Connect Cache Node --#
    print "\t Connect cache node ..."
    mc.connectAttr('%s.inRange' % cacheNode, '%s.playFromCache' % clothNode)
    return cacheNode

def delCacheNode(node):
    """
    Delected all cacheFile node connected to given node
    :param node: Maya node
    :type node: str
    """
    cacheNodes = pRigg.findTypeInHistory(node, 'cacheFile', past=True, future=True) or []
    for cacheNode in cacheNodes:
        if mc.objectType(node) in ['nCloth', 'nRigid']:
            print "Deleting cacheNode: %s ..." % cacheNode
            mc.setAttr('%s.enable', False)
            mc.delete(cacheNode)

def newNCacheFile(cachePath, fileName, clothNode, start, stop, rfDisplay, cacheModeIndex, newCacheNode=False):
    """
    Create new cache files, attach to new cacheNode, connect new cacheNode
    :param cachePath: NCloth cache path
    :type cachePath: str
    :param fileName: NCloth cache file name
    :type fileName: str
    :param clothNode: NCloth shape node name
    :type clothNode: str
    :param start: NCloth cache start frame
    :type start: int
    :param stop: NCloth cache end frame
    :type stop: int
    :param rfDisplay: Refresh maya display state
    :type rfDisplay: bool
    :param cacheModeIndex: NCloth node cacheable attributes index.
                           (0=positions, 1=velocities, 2=internalState)
    :type cacheModeIndex: int
    :param newCacheNode: Create new cache node
    :type newCacheNode: bool
    :return: New cacheFile node
    :rtype: str
    """
    #-- Print Cache Info --#
    infos = ["#-- Cache Infos --#",
             "Cache Path = %s" % cachePath,
             "File Name = %s" % fileName,
             "Cloth Node = %s" % clothNode,
             "Start Frame = %s" % start,
             "End Frame = %s" % stop,
             "Refresh Maya Display = %s" % rfDisplay,
             "Cache Mode Index = %s | (0=positions, 1=velocities, 2=internalState)" % cacheModeIndex]
    print '\n'.join(infos)
    #-- Init Cache Mode --#
    print "\t Init cache mode ..."
    mc.setAttr('%s.cacheableAttributes' % clothNode, cacheModeIndex)
    #-- Create Cache File --#
    print "\t Create cache files ..."
    mc.cacheFile(dir=cachePath, f=fileName, cnd=clothNode, st=start, et=stop, fm='OneFile', r=rfDisplay,
                 ci="getNClothDescriptionInfo %s" % clothNode)
    #-- Create Cache Node --#
    if newCacheNode:
        print "\t Create cache node ..."
        cacheNode = newNCacheNode(cachePath, fileName, clothNode, cacheModeIndex)
    else:
        cacheNode = None
    return cacheNode
