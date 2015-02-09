import os


class SeqLs(object):
    """ List given directory with a sequence compact view
        ex: ima_1.[001:005:1].txt ([start:stop:step])
        :param dir: Directory to list
        :type dir: str """

    def __init__(self, dir):
        if not os.path.exists(dir):
            raise IOError, "!!! ERROR: Directory not found: %s !!!" % dir
        self.dir = dir
        self.seqList = []
        self.seqDict = {}
        self.dirList = os.listdir(self.dir)
        self._exec()

    def _exec(self):
        """ Launch listing commands """
        self.parseDir()
        self.printResult()

    def parseDir(self):
        """ Parse given directory """
        for item in self.dirList:
            #-- Item is folder --#
            if os.path.isdir(item):
                self.seqList.append(item.upper())
            #-- Item is file --#
            elif os.path.isfile(item):
                #-- Seq type : name.index.ext --#
                if len(item.split('.')) == 3 and item.split('.')[1].isdigit():
                    name = item.split('.')[0]
                    index = item.split('.')[1]
                    ext = item.split('.')[2]
                    label = '%s/%s' % (name, ext)
                    if not label in self.seqDict.keys():
                        self.seqDict[label] = [index]
                    else:
                        self.seqDict[label].append(index)
                #-- Seq type : other --#
                else:
                    self.seqList.append(item)

    def printResult(self):
        """ Print sequence listing """
        lines = []
        for k in sorted(self.seqDict.keys()):
            first = self.seqDict[k][0]
            last = self.seqDict[k][-1]
            if len(self.seqDict[k]) == ((int(last) - int(first)) + 1):
                step = 1
            else:
                sec = self.seqDict[k][1]
                step = (int(sec) - int(first))
                for n, ind in enumerate(self.seqDict[k]):
                    if n > 0:
                        prevInd = self.seqDict[k][n-1]
                        if not (int(ind) - int(prevInd)) == step:
                            step = None
                            break
            if step is None:
                lines.append('%s.[%s...%s].%s' % (k.split('/')[0], self.seqDict[k][0],
                                                  self.seqDict[k][-1], k.split('/')[-1]))
            else:
                lines.append('%s.[%s:%s:%s].%s' % (k.split('/')[0], self.seqDict[k][0], self.seqDict[k][-1],
                                                   step, k.split('/')[-1]))
        self.seqList.extend(lines)
        for l in sorted(lines):
            print l


if __name__ == '__main__':
    currentDir = os.getcwd()
    sls = SeqLs(currentDir)
