import os, shutil
from appli import factory
from lib.system import procFile as pFile


class Factory(object):
    """ Factory main class
        :param logLvl: (str) : Log level ('critical', 'error', 'warning', 'info', 'debug') """

    def __init__(self, logLvl='info'):
        self.log = pFile.Logger(title="Factory", level=logLvl)
        self.log.info("#-- Init Factory --#")
        self.path = factory.factoryPath
        self.libPath = factory.libPath
        self.rndBinPath = factory.rndBinPath
        self.texture = Tree('texture', parent=self)
        self.shader = Tree('shader', parent=self)
        self.stockShot = Tree('stockShot', parent=self)

    def parseTree(self, tree):
        """ Parse given tree
            :param tree: (object) : Tree object """
        self.log.debug("Parsing %s ..." % tree.treeName)
        tree.tree = []
        #-- Parse Category --#
        cats = os.listdir(tree.path) or []
        for cat in cats:
            catPath = pFile.conformPath(os.path.join(tree.path, cat))
            if not cat.startswith('_') and not cat.startswith('.') and os.path.isdir(catPath):
                newCat = TreeNode('category', cat, catPath, tree=tree)
                tree.tree.append(newCat)
                #-- Parse Sub Category --#
                subCats = os.listdir(catPath) or []
                for subCat in subCats:
                    subCatPath = pFile.conformPath(os.path.join(catPath, subCat))
                    if (not subCat.startswith('_') and not subCat.startswith('.')
                        and os.path.isdir(subCatPath)):
                        newSubCat = TreeNode('subCategory', subCat, subCatPath, tree=tree, parent=newCat)
                        newCat._children.append(newSubCat)
                        #-- Parse Files --#
                        files = os.listdir(subCatPath) or []
                        for f in files:
                            filePath = pFile.conformPath(os.path.join(subCatPath, f))
                            if (not f.startswith('_') and not f.startswith('.')
                                and os.path.isfile(filePath)):
                                newFile = TreeNode('file', f.split('.')[0], filePath, tree=tree, parent=newSubCat)
                                newSubCat._children.append(newFile)
        self.log.debug("\t Parsing done.")

    def transfertTexture(self, src, dst):
        """ Transfert texture
            :param src: (str) : Source file
            :param dst: (str) : Destination path """
        try:
            shutil.copy(src, dst)
            self.log.info("Copy texture %s in %s" % (src, dst))
        except:
            self.log.error("Can not copy file: %s" %src)

    def transfertStockShot(self, src, dst):
        """ Transfert stockShot
            :param src: (str) : Source file
            :param dst: (str) : Destination path """
        srcPath = os.path.dirname(src)
        srcFile = os.path.basename(src)
        fldName = os.path.splitext(srcFile)[0]
        stockPath = os.path.join(srcPath, 'seq', fldName)
        for file in os.listdir(stockPath):
            if not file.startswith('_') and not file.startswith('.'):
                srcAbsPath = os.path.join(stockPath, file)
                dstPath = os.path.join(dst, fldName)
                if not os.path.exists(dstPath):
                    try:
                        os.mkdir(dstPath)
                        self.log.info("Create Tmp folder %s" % fldName)
                    except:
                        raise IOError, "Can not create stockShot folder: %s" % fldName
                try:
                    shutil.copy(srcAbsPath, dstPath)
                    self.log.info("Copy stockShot %s in %s" % (srcAbsPath, dstPath))
                except:
                    self.log.error("Can not copy file: %s" %srcAbsPath)

    def ud_thumbnailImages(self, imaFile, imaType):
        """ Create or update thumbnail or preview image
            :param imaFile: (str) : Original image absolute path
            :param imaType: (str) : 'icon' or 'preview' """
        self.log.info("Create %s file ..." % imaType)
        srcFile = os.path.normpath(imaFile)
        thumbPath = pFile.conformPath(os.path.join(os.path.dirname(imaFile), '_%s' % imaType))
        if not os.path.exists(thumbPath):
            os.mkdir(thumbPath)
            self.log.info("Create path %s" % thumbPath)
        thumbFile = os.path.splitext(os.path.basename(imaFile))[0]
        thumbAbsPath = os.path.normpath(os.path.join(thumbPath, '%s.png' % thumbFile))
        if imaType == 'icon':
            iconSize = 100
        elif imaType == 'preview':
            iconSize = 250
        else:
            iconSize = 80
        ima = pFile.Image()
        if os.path.splitext(srcFile)[1] in ['.bmp', '.hdr']:
            ima.resizeIma(srcFile, thumbAbsPath, resize=(iconSize, iconSize), ratio=True, force=True)
        else:
            ima.resizeIma2(srcFile, thumbAbsPath, resize=(iconSize, iconSize), ratio=True)

    def ud_thumbnailDatas(self, imaFile, treeName):
        """ Create or update thumbnail data
            :param imaFile: (str) : Original image absolute path
            :param treeName: (str) : Tree object name """
        self.log.info("Create data file ...")
        node = self.getNode(treeName, imaFile)
        dataPath = pFile.conformPath(os.path.dirname(node.dataFile))
        if not os.path.exists(dataPath):
            os.mkdir(dataPath)
            self.log.info("Create path %s" % dataPath)
        tmpDict = node.getFileInfo()
        if tmpDict is not None:
            dataDict = tmpDict[tmpDict.keys()[0]]
            if dataDict is not None:
                dataTxt = ['Path = %r' % pFile.conformPath(os.path.dirname(imaFile))]
                for k, v in dataDict.iteritems():
                    if isinstance(v, str):
                        dataTxt.append("%s = %r" % (k, v))
                    else:
                        dataTxt.append("%s = %s" % (k, v))
                try:
                    pFile.writeFile(node.dataFile, '\n'.join(dataTxt))
                    self.log.info("Create thumbnail datas successfully: %s" % node.nodeName)
                except:
                    self.log.error("Can not create thumbnail datas for %s" % node.nodeName)
            else:
                self.log.warning("Can not access fileData, skip %s" % node.nodeName)
        else:
            self.log.warning("Can not access fileData, skip %s" % node.nodeName)

    def ud_movie(self, fileIn, fileOut):
        """ Create or update movie
            :param fileIn: (str) : Original movie absolute path
            :param fileOut: (str) : Destination movie absolute path """
        self.log.info("Create movie file ...")
        movPath = os.path.dirname(fileOut)
        if not os.path.exists(movPath):
            os.mkdir(movPath)
            self.log.info("Create path %s" % movPath)
        ima = pFile.Image()
        ima.createMovie(fileIn, fileOut, force=True, printCmd=True)

    def getNode(self, treeName, nodePath):
        """ Get node from given treeName and nodePath
            :param treeName: (str) : Tree object name
            :param nodePath: (str) : Node path
            :return: (object) : Node object """
        tree = getattr(self, treeName)
        node = tree.getNode(nodePath=nodePath)
        return node


class Tree(object):
    """ Factory tree object
        :param treeName : (str) : Tree name
        :param parent : (object) : Parent class """

    def __init__(self, treeName, parent=None):
        self._parent = parent
        self.treeName = treeName
        self._parent.log.info("#-- %s Tree --#" % self.treeName)
        self.path = os.path.join(self._parent.path, self.treeName)
        self.tree = []
        self._parent.parseTree(self)

    def getAllNodes(self):
        """ Get all treeNodes
            :return: (list) : Tree nodes list """
        allNodes = []
        for node in self.tree:
            allNodes.extend(self.getAllChildren(node))
        return allNodes

    @staticmethod
    def getAllChildren(node, depth=-1):
        """ get all children from given node
            :param node: (object) : Tree node
            :param depth: (int) : recursion depth
            :return: (list) : Tree nodes list """
        nodes = []
        def recurse(currentNode, depth):
            nodes.append(currentNode)
            if depth != 0:
                for n in range(len(currentNode._children)):
                    recurse(currentNode._children[n], depth-1)
        recurse(node, depth)
        return nodes

    def getNode(self, nodePath=None):
        """ Get node from given nodePath
            :param nodePath: (str) : Node path
            :return: (object) : Node object """
        if nodePath is not None:
            for node in self.getAllNodes():
                if node.nodePath == nodePath:
                    return node


class TreeNode(object):
    """ Factory tree node
        :param nodeType : (str) : 'category', 'subCategory' or 'file'
        :param nodeName : (str) : Node name
        :param nodePath : (str) : Node path
        :param tree : (object) : Parent tree object
        :param parent : (object) : Parent treeNode object """

    def __init__(self, nodeType, nodeName, nodePath, tree=None, parent=None):
        self._tree = tree
        self._parent = parent
        self._children = []
        self.nodeType = nodeType
        self.nodeName = nodeName
        self.nodePath = nodePath

    @property
    def sequencePath(self):
        """ Get sequence path
            :return: (str) : Sequence absolute path """
        path = os.path.join(os.path.dirname(self.nodePath), 'seq', self.nodeName)
        return pFile.conformPath(path)

    @property
    def movieFile(self):
        """ Get movie file
            :return: (str) : Movie file absolute path """
        path = os.path.join(os.path.dirname(self.nodePath), 'mov')
        return pFile.conformPath(os.path.join(path, "%s.mov" % self.nodeName))

    @property
    def dataFile(self):
        """ get data file
            :return: (str) : Data file absolute path """
        path = os.path.join(os.path.dirname(self.nodePath), '_data')
        return pFile.conformPath(os.path.join(path, "%s.py" % self.nodeName))

    @property
    def datas(self):
        """ Get datas
            :return: (dict) : File datas """
        if os.path.exists(self.dataFile):
            return pFile.readPyFile(self.dataFile)

    @property
    def datasString(self):
        """ Convert datas dict into readable string
            :return: (str) : Datas string """
        txt = []
        if self._tree.treeName is not 'shader':
            infoOrder = ['Path', 'Name', 'Width', 'Height', 'Aspect', 'Layer', 'Pixel', 'Duration', 'Speed']
            if self.datas is not None:
                txt.append("#-- %s --#" % self.datas['Name'])
                for info in infoOrder:
                    if info in self.datas.keys():
                        if isinstance(self.datas[info], str):
                            txt.append("%s = %r" % (info, self.datas[info]))
                        else:
                            txt.append("%s = %s" % (info, self.datas[info]))
                txt.append("\n#----------------------------------------#\n")
                for dataKey in self.datas.keys():
                    if not dataKey in infoOrder:
                        if isinstance(self.datas[dataKey], str):
                            txt.append("%s = %r" % (dataKey, self.datas[dataKey]))
                        else:
                            txt.append("%s = %s" % (dataKey, self.datas[dataKey]))
            return '\n'.join(txt)
        else:
            infoOrder = ['SurfaceShader', 'DisplaceShader', 'VolumeShader', 'mapFiles']
            if self.datas is not None:
                txt.append("#-- %s --#" % self.datas['Name'])
                for info in infoOrder:
                    if info in self.datas.keys():
                        if info == 'mapFiles':
                            txt.append("\n#--------------- Textures ---------------#\n")
                            for mapFile in self.datas[info]:
                                txt.append(mapFile)
                        else:
                            if isinstance(self.datas[info], str):
                                txt.append("%s = %r" % (info, self.datas[info]))
                            else:
                                txt.append("%s = %s" % (info, self.datas[info]))
            return '\n'.join(txt)

    def hasSequence(self):
        """ Check if node has sequence folder
            :return: (bool) : True if exists """
        if os.path.exists(self.sequencePath):
            return True
        else:
            return False

    def hasMovie(self):
        """ Check if node has movie file
            :return: (bool) : True if exists """
        if os.path.exists(self.movieFile):
            return True
        else:
            return False

    def getFileInfo(self):
        """ Get file info
            :return: (str) : File info """
        if self.hasSequence():
            path = self.sequencePath
        else:
            path = self.nodePath
        try:
            info = pFile.Image().getInfo(path)
            return info
        except:
            return None


if __name__ == '__main__':
    f = Factory(logLvl='debug')
    nodes = f.texture.getAllNodes()
    for node in nodes:
        print node.nodeName
