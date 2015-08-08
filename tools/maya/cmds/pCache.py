import os
from tools.maya.cmds import pRigg
from lib.system import procFile as pFile
try:
    import maya.cmds as mc
    import maya.mel as ml
except:
    pass


def newGeoCacheNode(cachePath, fileName, mesh):
    """
    Assign given cache file to given mesh
    :param cachePath: NCloth cache path
    :type cachePath: str
    :param fileName: NCloth cache file name
    :type fileName: str
    :param mesh: mesh shape node name
    :type mesh: str
    :return: New cacheFile node
    :rtype: str
    """
    hSwitch = ml.eval('createHistorySwitch("%s", false)' % mesh)
    cacheNode = mc.cacheFile(dir=cachePath, f=fileName, cnm=mesh, af=True, ia="%s.inp[0]" % hSwitch)
    mc.setAttr("%s.playFromCache" % hSwitch, 1)
    return cacheNode

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
    #-- Get inAttr --#
    if cacheModeIndex == 0:
        inAttr = '%s.positions' % clothNode
    elif cacheModeIndex == 1:
        inAttr = ['%s.positions' % clothNode, '%s.velocities' % clothNode]
    elif cacheModeIndex == 2:
        inAttr = ['%s.positions' % clothNode, '%s.velocities' % clothNode, '%s.internalState' % clothNode]
    else:
        inAttr = '%s.positions' % clothNode
    #-- Create Cache Node --#
    cacheNode = mc.cacheFile(dir=cachePath, f=fileName, ccn=True, ia=inAttr)
    mc.connectAttr('%s.inRange' % cacheNode, '%s.playFromCache' % clothNode)
    return cacheNode

def getCacheNodes(node):
    """
    Get cacheFile nodes connected to given node name
    :param node: Maya node
    :type node: str
    :return: CacheFile nodes
    :rtype: list
    """
    return pRigg.findTypeInHistory(node, 'cacheFile', past=True, future=True) or []

def delCacheNode(node):
    """
    Delected all cacheFile node connected to given node
    :param node: Maya node
    :type node: str
    """
    cacheNodes = getCacheNodes(node)
    for cacheNode in cacheNodes:
        print "Deleting cacheNode: %s ..." % cacheNode
        mc.setAttr('%s.enable' % cacheNode, False)
        mc.delete(cacheNode)

def geoCacheFile(cachePath, fileName, shapeName, startFrame, stopFrame, rfDisplay, newCacheNode):
    """
    Create new cache files, attach to new cacheNode, connect new cacheNode
    :param cachePath: NCloth cache path
    :type cachePath: str
    :param fileName: NCloth cache file name
    :type fileName: str
    :param shapeName: Shape name
    :type shapeName: str
    :param startFrame: NCloth cache start frame
    :type startFrame: int
    :param stopFrame: NCloth cache end frame
    :type stopFrame: int
    :param rfDisplay: Refresh maya display state
    :type rfDisplay: bool
    :param newCacheNode: Create new cache node
    :type newCacheNode: bool
    :return: New cacheFile node
    :rtype: str
    """
    #-- Print Cache Info --#
    infos = ["#" * 60, "#-- Cache Infos --#",
             "Cache Path = %s" % cachePath,
             "File Name = %s" % fileName,
             "Shape Node = %s" % shapeName,
             "Start Frame = %s" % startFrame,
             "End Frame = %s" % stopFrame,
             "Refresh Maya Display = %s" % rfDisplay,
             "New Cache Node = %s" % str(newCacheNode), "#" * 60]
    print '\n'.join(infos)
    #-- Launch Cache Creation --#
    print "\t Create cache files ..."
    mc.playbackOptions(ps=0)
    mc.cacheFile(dir=cachePath, f=fileName, pts=shapeName, st=startFrame, et=stopFrame, fm='OneFile',
                 r=rfDisplay,  ws=True)
    #-- Create Cache Node --#
    if newCacheNode:
        print "\t Create cache node ..."
        cacheNode = newGeoCacheNode(cachePath, fileName, shapeName)
    else:
        cacheNode = None
    return cacheNode

def nCacheFile(cachePath, fileName, clothNode, startFrame, stopFrame, rfDisplay, cacheModeIndex,
               newCacheNode=False, modeAppend=False, noBackup=False):
    """
    Create new cache files, attach to new cacheNode, connect new cacheNode
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
    :param newCacheNode: Create new cache node
    :type newCacheNode: bool
    :param noBackup: Specifies that backup files should not be created
                     for any files that may be over-written during append
    :type noBackup: bool
    :return: New cacheFile node
    :rtype: str
    """
    #-- Print Cache Info --#
    infos = ["#" * 60, "#-- Cache Infos --#",
             "Cache Path = %s" % cachePath,
             "File Name = %s" % fileName,
             "Cloth Node = %s" % clothNode,
             "Start Frame = %s" % startFrame,
             "End Frame = %s" % stopFrame,
             "Refresh Maya Display = %s" % rfDisplay,
             "Cache Mode Index = %s" % cacheModeIndex,
             "New Cache Node = %s" % str(newCacheNode), "#" * 60]
    print '\n'.join(infos)
    #-- Init Cache Mode --#
    print "\t Init cache mode ..."
    mc.setAttr('%s.cacheableAttributes' % clothNode, cacheModeIndex)
    mc.playbackOptions(ps=0)
    #-- Launch Simulation --#
    if not modeAppend:
        print "\t Create cache files ..."
        mc.cacheFile(dir=cachePath, f=fileName, cnd=clothNode, st=startFrame, et=stopFrame, fm='OneFile', r=rfDisplay,
                     ci="getNClothDescriptionInfo %s" % clothNode)
    else:
        print "\t Append to cache files ..."
        mc.cacheFile(dir=cachePath, f=fileName, cnd=clothNode, apf=True, st=startFrame, et=stopFrame, fm='OneFile',
                     r=rfDisplay, ci="getNClothDescriptionInfo %s" % clothNode, nb=noBackup)
    #-- Create Cache Node --#
    if not modeAppend:
        if newCacheNode:
            print "\t Create cache node ..."
            cacheNode = newNCacheNode(cachePath, fileName, clothNode, cacheModeIndex)
        else:
            cacheNode = None
        return cacheNode


class CacheFileParser(object):

    __extraLineIn = '  <extra>'
    __extraLineOut = '</extra>'
    __channelsStart = '  <Channels>'
    __channelsEnd = '  </Channels>'
    __channelLineIn = '    <channel'
    __channelLineOut = '/>'
    __nClothAttrKey = 'NCloth Info for'

    def __init__(self, cacheFile=None):
        #-- Init Parser --#
        self._cacheFile = None
        self._cacheLines = None
        self._headers = {}
        self._extraLines = {}
        self._channels = {}
        self._signaturs = {}
        #-- Load Given CacheFile --#
        if cacheFile is not None:
            self._cacheFile = cacheFile
            self.loadFile()

    @property
    def cacheFile(self):
        """
        Get cacheFile value
        :return: CacheFile full path
        :rtype: str
        """
        return self._cacheFile

    @cacheFile.setter
    def cacheFile(self, value):
        """
        Set cacheFile Value
        :param value: CacheFile full path
        :type value: str
        """
        if value is None:
            self._cacheFile = None
        else:
            if os.path.exists(os.path.normpath(value)):
                self._cacheFile = pFile.conformPath(value)
            else:
                print "!!! WARNING: Given cacheFile path not found: %s !!!" % pFile.conformPath(value)

    def loadFile(self):
        """
        Parse cache file
        """
        if self.cacheFile is not None:
            self._cacheLines = pFile.readFile(self.cacheFile)
            #-- Store Extra Lines and Channels --#
            for n, line in enumerate(self._cacheLines):
                line = line.strip('\n')
                #-- Store Extra Lines --#
                if line.startswith(self.__extraLineIn):
                    self._extraLines[n+1] = str(line.split('>')[1].split('<')[0])
                #-- Store Channels --#
                if line.startswith(self.__channelLineIn):
                    channelLine = line.split('<')[1].split('/')[0]
                    chanParams = channelLine.split(' ')
                    self._channels[n+1] = {}
                    self._channels[n+1][chanParams[0]] = {}
                    #-- Store Channels Params --#
                    for i, p in enumerate(chanParams):
                        if i:
                            k = p.split('=')[0]
                            v = p.split('=')[1]
                            self._channels[n+1][chanParams[0]][k] = v
            #-- Store Headers --#
            firstExtraLine = self._extraLines.keys()[0]
            headers = self._cacheLines[:firstExtraLine-1]
            for n, header in enumerate(headers):
                self._headers[n+1] = header.strip('\n')
            #-- Store Signaturs --#
            lastChannelLine = self._channels.keys()[-1]
            signaturs = self._cacheLines[lastChannelLine+1:]
            for n, signatur in enumerate(signaturs):
                nLine = (self._channels.keys()[-1] + 1) + (n + 1)
                self._signaturs[nLine] = signatur.strip('\n')

    def hasNClothParams(self):
        """
        Check if cache file has nCloth params
        :return: Has nCloth params
        :rtype: bool
        """
        if self._extraLines is not None:
            for k, v in sorted(self._extraLines.iteritems()):
                if self.__nClothAttrKey in v:
                    return True

    def extractNClothParams(self):
        """
        Translate extraLines to nCloth params if any exists
        :return: nCloth params
        :rtype: dict
        """
        if self.hasNClothParams():
            clothDict = {'connected': {}, 'attributes': {}}
            for k, v in sorted(self._extraLines.iteritems()):
                #-- Get Connected Nodes --#
                if ':  ' in v:
                    key = v.split(':  ')[0]
                    val = v.split(':  ')[1]
                    if not key in clothDict['connected'].keys():
                        clothDict['connected'][key] = []
                    clothDict['connected'][key].append(val)
                #-- Get Nodes Params --#
                elif '.' in v and '=' in v:
                    obj = v.split('.')[0]
                    attr = v.split('.')[1].split('=')[0]
                    val = v.split('=')[-1]
                    if not obj in clothDict['attributes'].keys():
                        clothDict['attributes'][obj] = {}
                    clothDict['attributes'][obj][attr] = val
            #-- Result --#
            return clothDict
