from lib.system import procFile as pFile


class MaFile(object):

    def __init__(self, scene=None):
        self._sceneFile = scene
        self._sceneLines = []
        self._sceneDict = {}
        if self.sceneFile is not None:
            self.sceneLines = pFile.readFile(self.sceneFile)
            self.parse()

    @property
    def sceneFile(self):
        return self._sceneFile

    @sceneFile.setter
    def sceneFile(self, value):
        self._sceneFile = value

    @property
    def sceneLines(self):
        return self._sceneLines

    @sceneLines.setter
    def sceneLines(self, value):
        self._sceneLines = value

    @property
    def sceneDict(self):
        return self._sceneDict

    @sceneDict.setter
    def sceneDict(self, value):
        self._sceneDict = value

    def parse(self):
        if self.sceneFile is not None:
            maDict = {}
            #-- Store Nodes --#
            for n, line in enumerate(self.sceneLines):
                cleanLine = line.strip('\n')
                if cleanLine.startswith("createNode "):
                    nodeName = cleanLine.split(' ')[-1][1:-2]
                    nodeType = cleanLine.split(' ')[1]
                    maDict[nodeName] = {'type': nodeType, 'attrList': {}}
                    ind = 1
                    while self.sceneLines[n+ind].startswith('\tsetAttr'):
                        attrLine = self.sceneLines[n+ind].strip()
                        attr = attrLine.split(' ')[1][1:-1]
                        if not attrLine.split(' ')[2] == '-type':
                            attrType = 'num'
                            tmpVal = attrLine.split(' ')[2][:-1]
                            if tmpVal in ['yes', 'Yes', 'YES', 'True', 'true', 'no', 'No', 'NO', 'False', 'false']:
                                if tmpVal in ['yes', 'Yes', 'YES', 'True', 'true']:
                                    value = 1
                                else:
                                    value = 0
                            else:
                                if '.' in tmpVal:
                                    value = float(tmpVal)
                                else:
                                    value = int(tmpVal)
                        else:
                            attrType = attrLine.split(' ')[3][1:-1]
                            if attrType == 'string':
                                value = attrLine.split(' ')[4][1:-2]
                            else:
                                value = attrLine.split(' ')[4][1:-1]
                        maDict[nodeName]['attrList'][attr] = {'type': attrType, 'value': value}
                        ind += 1
            self.sceneDict = maDict

    def write(self, outFile=None):
        if outFile is None:
            outFile = self.sceneFile
        try:
            pFile.writeFile(outFile, self.sceneLines)
            print "Scene saved as %s" % outFile
        except:
            print "ERROR: Can not save scene %s" % outFile

    def getNodes(self):
        return self.sceneDict.keys()

    def getNodesByType(self, nodeType):
        nodes = self.getNodes()
        result = []
        for node in nodes:
            if self.sceneDict[node]['type'] == nodeType:
                result.append(node)
        return result

    def getAttrList(self, nodeName):
        if nodeName in self.sceneDict.keys():
            return self.sceneDict[nodeName]['attrList'].keys()

    def getAttrValue(self, nodeName, attr):
        if nodeName in self.sceneDict.keys():
            if attr in self.sceneDict[nodeName]['attrList'].keys():
                return self.sceneDict[nodeName]['attrList'][attr]['value']

    def getAttrType(self, nodeName, attr):
        if nodeName in self.sceneDict.keys():
            if attr in self.sceneDict[nodeName]['attrList'].keys():
                return self.sceneDict[nodeName]['attrList'][attr]['type']

    def setAttr(self, nodeName, attr, value):
        #-- Check Args --#
        if not nodeName in self.sceneDict.keys():
            raise KeyError, "Node %s not found" % nodeName
        if not attr in self.sceneDict[nodeName]['attrList'].keys():
            raise KeyError, "Attribute %s not found" % attr
        #-- Set Attribute --#
        newLines = []
        step = 0
        for n in range(len(self.sceneLines)):
            n = (n + step)
            if n < len(self.sceneLines):
                nodeType = self.sceneDict[nodeName]['type']
                if self.sceneLines[n].startswith('createNode %s -n "%s"' % (nodeType, nodeName)):
                    newLines.append(self.sceneLines[n])
                    ind = 1
                    while self.sceneLines[n+ind].startswith('\tsetAttr'):
                        if attr in self.sceneLines[n+ind]:
                            currentVal = self.getAttrValue(nodeName, attr)
                            newLine = self.sceneLines[n+ind].replace(currentVal, value)
                            newLines.append(newLine)
                        else:
                            newLines.append(self.sceneLines[n+ind])
                        ind += 1
                    step = ind-1
                else:
                    newLines.append(self.sceneLines[n])
        self.sceneLines = newLines
        self.parse()


if __name__ == '__main__':
    sf = "D:/factory/shader/concrete/pattern/shader/brickWall_001.ma"
    ma = MaFile(scene=sf)
    print ma.getNodes()
    print ma.getAttrList('map_C_brickWall_001')
    print ma.getAttrValue('map_C_brickWall_001', '.ftn')
    # nodes = ma.getNodesByType('file')
    # for node in nodes:
    #     if '.ftn' in ma.getAttrList(node):
    #         print 'result: ', node
    # print ma.getAttrType('map_C_brickWall_001', '.ftn')
    ma.setAttr('map_C_brickWall_001', '.ftn', 'D:/toto/test.jpg')
    print ma.getAttrValue('map_C_brickWall_001', '.ftn')
    # ma.write(outFile="D:/prods/test/out.ma")