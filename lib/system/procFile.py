import os, math, time, subprocess, pprint
from lib.env import studio


def conformPath(path):
    """
    Comform path separator with '/'

    :param path: Path to conform
    :type path: str
    :return: Conformed path
    :rtype: str
    """
    return path.replace('\\', '/')

def pathToDict(path, conformed=False):
    """
    Translate directory contents to dict

    :param path: Absolut path
    :type path: str
    :param conformed: Conform path before storing
    :type conformed: bool
    :return: Path contents
    :rtype: dict
    """
    if not os.path.exists(path):
        raise IOError, "!!! ERROR: Path not found!!!\n%s" % path
    pathDict = {'_order': []}
    for root, flds, files in os.walk(path):
        if conformed:
            rootPath = conformPath(root)
        else:
            rootPath = root
        pathDict['_order'].append(rootPath)
        pathDict[rootPath] = {'folders': flds, 'files': files}
    return pathDict

def makeDir(directory, verbose=False):
    """
    Create given directory

    :param directory: Full directory path
    :type directory: str
    :param verbose: Enable verbose
    :type verbose: bool
    """
    path = os.path.normpath(directory)
    if not os.path.exists(path):
        try:
            os.mkdir(path)
            if verbose:
                print "\t Create folder '%s' in '%s'" % (path.split(os.sep)[-1],
                                                         conformPath(os.sep.join(path.split(os.sep)[:-1])))
        except(IOError, os.error) as log:
            raise IOError, log
    else:
        if verbose:
            print "\t Skip folder creation, directory already exists: %s !!!" % path

def mkPathFolders(rootPath, absPath, sep=None):
    """
    Create absPath folders not in rootPath

    :param rootPath: Root path
    :type rootPath: str
    :param absPath: Absolut Path
    :type absPath: str
    :param sep: Os separator
    :type sep: str
    """
    if not os.path.exists(rootPath):
        raise IOError, "!!! ERROR: rootPath not found !!!"
    if sep is None:
        sep = os.sep
    relPath = absPath.replace('%s%s' % (rootPath, sep), '')
    checkPath = rootPath
    for fld in relPath.split(sep):
        checkPath = "%s%s%s" % (checkPath, sep, fld)
        if not os.path.exists(checkPath):
            print "[sysInfo] : Create folder %s in %s" % (fld, sep.join(checkPath.split(sep)[:-1]))
            try:
                os.mkdir(checkPath)
            except(IOError, os.error) as log:
                raise IOError, log

def readFile(filePath):
    """
    Get text from file

    :param filePath: File absolut path
    :type filePath: str
    :return: Text line by line
    :rtype: list
    """
    if not os.path.exists(filePath):
        raise IOError, "!!! Error: Can't read, file doesn't exists !!!"
    fileId = open(filePath, 'r')
    getText = fileId.readlines()
    fileId.close()
    return getText

def readDictFile(filePath):
    return eval(''.join(readFile(filePath)))

def readPyFile(filePath, keepBuiltin=False):
    """
    Get text from pyFile

    :param filePath: Python file absolut path
    :type filePath: str
    :param keepBuiltin: Keep builtins key
    :type keepBuiltin: bool
    :return: File dict
    :rtype: dict
    """
    if not os.path.exists(filePath):
        raise IOError, "!!! Error: Can't read, file doesn't exists !!!"
    params = {}
    execfile(filePath, params)
    if keepBuiltin:
        return params
    else:
        if '__builtins__' in params.keys():
            params.pop('__builtins__')
            return params

def writeDictFile(filePath, dictToPrint):
    """
    Create readable text file from given dict

    :param filePath: File absolut path
    :type filePath: str
    :param dictToPrint: Dict to translate and print
    :type dictToPrint: dict
    """
    fileId = open(filePath, 'w')
    fileId.write(pprint.pformat(dictToPrint))
    fileId.close()

def writeFile(filePath, textToWrite, add=False):
    """
    Create and edit text file. If file already exists, it is overwritten

    :param filePath: File absolut path
    :type filePath: str
    :param textToWrite: Text to edit in file
    :type textToWrite: str | list
    :param add: Add text to existing one in file
    :type add: bool
    """
    oldTxt = ""
    if add:
        oldTxt = ''.join(readFile(filePath))
        if not oldTxt.endswith('\n'):
            oldTxt = "%s\n" % oldTxt
    fileId = open(filePath, 'w')
    if add:
        fileId.write(oldTxt)
    if isinstance(textToWrite, str):
        fileId.write(textToWrite)
    elif isinstance(textToWrite, (list, tuple)):
        fileId.writelines(textToWrite)
    fileId.close()

def fileSizeFormat(_bytes, precision=2):
    """
    Returns a humanized string for a given amount of bytes

    :param _bytes: File size in bytes
    :type _bytes: int
    :param precision: Precision after coma
    :type precision: int
    :return: Humanized string
    :rtype: str
    """
    _bytes = int(_bytes)
    if _bytes is 0:
        return '0 b'
    log = math.floor(math.log(bytes, 1024))
    return "%.*f %s" % (precision, bytes / math.pow(1024, log),
                       ['b', 'kb', 'mb', 'gb', 'tb','pb', 'eb', 'zb', 'yb'][int(log)])

def secondsToStr(seconds):
    """
    Convert number of seconds into humanized string

    :param seconds: Number of seconds
    :type seconds: int
    :return: Humanized string
    :rtype: str
    """
    S = int(seconds)
    hours = S / 3600
    S -= hours * 3600
    minutes = S / 60
    seconds = S - (minutes * 60)
    return "%s:%s:%s" % (hours, minutes, seconds)

def getDate():
    """
    Get current date

    :return: yyyy_mm_dd
    :rtype: str
    """
    return time.strftime("%Y_%m_%d")

def getTime():
    """
    Get current time

    :return: hh_mm_ss
    :rtype: str
    """
    return time.strftime("%H_%M_%S")


class Logger(object):
    """
    Print given message using log levels

    :param title: Log title
    :type title: str
    :param level: Log level ('critical', 'error', 'warning', 'info', 'debug', 'detail')
    :type level: str
    """

    def __init__(self, title='LOG', level='info'):
        self.levels = ['critical', 'error', 'warning', 'info', 'debug', 'detail']
        self.title = title
        self.level = level

    @property
    def lvlIndex(self):
        """
        Get current level index

        :return: Current level index
        :rtype: int
        """
        return self.levels.index(self.level)

    def critical(self, message, newLinesBefor=0, newLinesAfter=0):
        """
        Print given message with critical level

        :param message: Message to print
        :type message: str
        :param newLinesBefor: New lines to insert befor message
        :type newLinesBefor: int
        :param newLinesAfter: New lines to insert after message
        :type newLinesAfter: int
        """
        if self.lvlIndex >= 0:
            self._addNewLines(newLinesBefor)
            print "| %s | Critical | %s | %s" % (self.title, self.currentTime, message)
            self._addNewLines(newLinesAfter)

    def error(self, message, newLinesBefor=0, newLinesAfter=0):
        """
        Print given message with error level

        :param message: Message to print
        :type message: str
        :param newLinesBefor: New lines to insert befor message
        :type newLinesBefor: int
        :param newLinesAfter: New lines to insert after message
        :type newLinesAfter: int
        """
        if self.lvlIndex >= 1:
            self._addNewLines(newLinesBefor)
            print "| %s | Error | %s | %s" % (self.title, self.currentTime, message)
            self._addNewLines(newLinesAfter)

    def warning(self, message, newLinesBefor=0, newLinesAfter=0):
        """
        Print given message with warning level

        :param message: Message to print
        :type message: str
        :param newLinesBefor: New lines to insert befor message
        :type newLinesBefor: int
        :param newLinesAfter: New lines to insert after message
        :type newLinesAfter: int
        """
        if self.lvlIndex >= 2:
            self._addNewLines(newLinesBefor)
            print "| %s | Warning | %s | %s" % (self.title, self.currentTime, message)
            self._addNewLines(newLinesAfter)

    def info(self, message, newLinesBefor=0, newLinesAfter=0):
        """
        Print given message with info level

        :param message: Message to print
        :type message: str
        :param newLinesBefor: New lines to insert befor message
        :type newLinesBefor: int
        :param newLinesAfter: New lines to insert after message
        :type newLinesAfter: int
        """
        if self.lvlIndex >= 3:
            self._addNewLines(newLinesBefor)
            print "| %s | Info | %s | %s" % (self.title, self.currentTime, message)
            self._addNewLines(newLinesAfter)

    def debug(self, message, newLinesBefor=0, newLinesAfter=0):
        """
        Print given message with debug level

        :param message: Message to print
        :type message: str
        :param newLinesBefor: New lines to insert befor message
        :type newLinesBefor: int
        :param newLinesAfter: New lines to insert after message
        :type newLinesAfter: int
        """
        if self.lvlIndex >= 4:
            self._addNewLines(newLinesBefor)
            print "| %s | Debug | %s | %s" % (self.title, self.currentTime, message)
            self._addNewLines(newLinesAfter)

    def detail(self, message, newLinesBefor=0, newLinesAfter=0):
        """
        Print given message with detail level

        :param message: Message to print
        :type message: str
        :param newLinesBefor: New lines to insert befor message
        :type newLinesBefor: int
        :param newLinesAfter: New lines to insert after message
        :type newLinesAfter: int
        """
        if self.lvlIndex >= 5:
            self._addNewLines(newLinesBefor)
            print "| %s | Detail | %s | %s" % (self.title, self.currentTime, message)
            self._addNewLines(newLinesAfter)

    @property
    def currentTime(self):
        """
        Get current time

        :return: Current time
        :rtype: str
        """
        return getTime().replace('_', ':')

    @staticmethod
    def _addNewLines(newLines):
        """
        Print new empty lines

        :param newLines: Number of new lines to print
        :type newLines: int
        """
        if newLines > 0:
            if newLines == 1:
                print ""
            else:
                print '\n' * (newLines - 1)


class Image(object):
    """
    Class to manipulate image or get info from file

    Usage: ima = Image()
           r = ima.getInfo(filePath, options=['-fp'], returnAs='dict')
           r.resizeIma(fileIn, fileOut, resize=(200, 200), ratio=True, force=True, printCmd=True, extern=True)
    """

    ffmpeg = studio.ffmpeg
    djvInfo = studio.djvInfo
    nConvert = studio.nConvert
    djvConvert = studio.djvConvert

    def __init__(self):
        pass

    def getInfo(self, path, options=None, returnAs='dict'):
        """ get image file info
            @param path: (str) : Directory or image file absolute path
            @param options: (list) : Options from djv_info.exe
            @param returnAs: (str) : 'dict' or 'str'
            @return: (dict or str) : Image file info """
        proc = self._getInfoProc(path, options)
        result = proc.communicate()[0]
        if not "ERROR" in result:
            if returnAs == 'str':
                return result
            elif returnAs == 'dict':
                return self._getInfoDict(result)
        else:
            print result

    def resizeIma(self, imaIn, imaOut, resize=(None, None), ratio=False, force=False, printCmd=False, extern=False):
        """ Convert given image with given resize options via nConvert
            :param imaIn: (str) : Image file in absolute path
            :param imaOut: (str) : Image file out absolute path
            :param resize: (tuple) : Width(int), Height(int)
            :param ratio: (bool) : Keep aspect ratio
            :param force: (bool) : Overwrite destination
            :param printCmd: (bool) : Print resize command
            :param extern: (bool) : Launch resize in new xtem """
        cmd = [self.nConvert, '-out', self._getExtKey(imaOut), '-o', os.path.normpath(imaOut), os.path.normpath(imaIn)]
        if resize[0] is not None and resize[1] is not None:
            if not ratio:
                cmd.insert(3, "-resize %s %s" % (resize[0], resize[1]))
            else:
                cmd.insert(3, "-resize %s %s -ratio" % (resize[0], resize[1]))
        if force:
            cmd.insert(-3, '-overwrite')
        if printCmd:
            print "#-- Resize Command --#\n", ' '.join(cmd)
        if not extern:
            os.system(' '.join(cmd))
        else:
            os.system('start %s' % ' '.join(cmd))

    def resizeIma2(self, imaIn, imaOut, resize=(None, None), ratio=False, printCmd=False, extern=False):
        """ Convert given image with given resize options via djvConvert
            :param imaIn: (str) : Image file in absolute path
            :param imaOut: (str) : Image file out absolute path
            :param resize: (tuple) : Width(int), Height(int)
            :param ratio: (bool) : Keep aspect ratio
            :param printCmd: (bool) : Print resize command
            :param extern: (bool) : Launch resize in new xtem """
        cmd = [self.djvConvert, os.path.normpath(imaIn), os.path.normpath(imaOut)]
        if resize[0] is not None and resize[1] is not None:
            if not ratio:
                cmd.append("-resize %s %s" % (resize[0], resize[1]))
            else:
                newSize = self._getNewSize(imaIn, resize)
                cmd.append("-resize %s %s" % (newSize[0], newSize[1]))
        if printCmd:
            print "#-- Resize Command --#\n", ' '.join(cmd)
        if not extern:
            os.system(' '.join(cmd))
        else:
            os.system('start %s' % ' '.join(cmd))

    def createMovie(self, fileIn, fileOut, resize=(None, None), ratio=False, speed='24',
                    force=False, printCmd=False, extern=False):
        """ Convert given file to movie via ffmpeg
            :param fileIn: (str) : Image file in absolute path (name.%0Xd.ext)
            :param fileOut: (str) : Movie file out absolute path
            :param resize: (tuple) : Width(int), Height(int)
            :param ratio: (bool) : Keep aspect ratio (fileIn must be name.start-end.ext)
            :param speed: (str) : Frame rate, default = 24
            :param force: (bool) : Overwrite destination
            :param printCmd: (bool) : Print resize command
            :param extern: (bool) : Launch resize in new xtem """
        cmd = [self.ffmpeg, '-v', 'error', '-stats', '-r', speed, '-f', 'image2']
        if resize[0] is not None and resize[1] is not None:
            if not ratio:
                cmd.append("-i %s -s %sx%s" % (fileIn, resize[0], resize[1]))
            else:
                if not len(os.path.basename(fileIn).split('.')) == 3:
                    raise AttributeError, "fileIn must be name.start-end.ext !!!"
                if not '-' in os.path.basename(fileIn).split('.')[1]:
                    raise AttributeError, "fileIn must be name.start-end.ext !!!"
                imaSeq, width, height = self._getMovieParams(fileIn, resize)
                cmd.append("-i %s -s %sx%s" % (imaSeq, width, height))
        else:
            cmd.append("-i %s" % fileIn)
        if force:
            cmd.append("-y")
        cmd.append(os.path.normpath(fileOut))
        if printCmd:
            print "#-- Movie Command --#\n", ' '.join(cmd)
        if not extern:
            os.system(' '.join(cmd))
        else:
            os.system('start %s' % ' '.join(cmd))

    def _getInfoProc(self, path, options):
        """ Get info subprocess cmdArgs
            @param path: (str) : Directory or image file absolute path
            @param options: (list) : Options from djv_info.exe
            @return: (object) : Subprocess """
        cmd = [self.djvInfo, '-v', os.path.normpath(path)]
        if options is not None:
            for opt in options:
                cmd.append(opt)
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        return proc

    def _getInfoDict(self, result):
        """ Translate info subprocess result to dict
            @param result: Subprocess result
            @return: (dict) : Info dict """
        info = {}
        blocks = self._getBlocks(result)
        for block in blocks:
            label = None
            for n, line in enumerate(block):
                if n == 0:
                    name = conformPath(line.strip())
                    label = os.path.basename(name).replace('.', '|')
                    info[label] = {'Name': name}
                else:
                    k = line.split('=')[0].strip().replace(' ', '')
                    v = line.split('=')[-1].strip()
                    info[label][k] = v
        return info

    @staticmethod
    def _getBlocks(result):
        """ Convert result in blocks
            :param result: (str) : Image info
            :return: (list) : Info blocks """
        block = []
        blocks = []
        lines = result.split('\n')
        for n, line in enumerate(lines):
            if line == '\r' or n == (len(lines) - 1):
                blocks.append(block)
                block = []
            else:
                block.append(line)
        return blocks

    @staticmethod
    def _getExtKey(imaOut):
        """ Get output extention argument
            :param imaOut: (str) : Image file out absolute path
            :return: (str) : Output extention argument """
        if os.path.splitext(imaOut)[-1] == '.jpg':
            return 'jpeg'
        else:
            return os.path.splitext(imaOut)[-1].replace('.', '')

    def _getNewSize(self, imaFile, resize):
        """ Get new size with aspect ratio constrain
            :param imaFile: Image file in absolute path
            :param resize: (tuple) : Width(int), Height(int)
            :return: (tuple) : New size Width(int), Height(int) """
        datas = self.getInfo(imaFile)
        imaDict = datas[datas.keys()[0]]
        # noinspection PyTypeChecker
        ratio = float(imaDict['Aspect'])
        if ratio < 1:
            newSize = (int(resize[1] * ratio), int(resize[1]))
        else:
            newSize = (int(resize[0]), int(resize[0] / ratio))
        return newSize

    def _getMovieParams(self, fileIn, resize):
        """ Get movie params for resize with aspect constrain
            :param fileIn: Image file in absolute path
            :param resize: (tuple) : Width(int), Height(int)
            :return: (str, int, int) : Sequence absolute path, Width, Height """
        imaPath = os.path.normpath(os.path.dirname(fileIn))
        imaName = os.path.basename(fileIn).split('.')[0]
        imaFrame = os.path.basename(fileIn).split('.')[1].split('-')[0]
        iFrame = ("%0" + str(len(imaFrame)) + "d")
        imaExt = os.path.basename(fileIn).split('.')[2]
        imaFile = os.path.join(imaPath, "%s.%s.%s" % (imaName, imaFrame, imaExt))
        imaSeq = os.path.join(imaPath, "%s.%s.%s" % (imaName, iFrame, imaExt))
        newSize = self._getNewSize(imaFile, resize)
        if str(newSize[0])[-1] in ['1', '3', '5', '7', '9']:
            newSize = (newSize[0] + 1, newSize[1])
        if str(newSize[1])[-1] in ['1', '3', '5', '7', '9']:
            newSize = (newSize[0], newSize[1] + 1)
        return imaSeq, newSize[0], newSize[1]


if __name__ == '__main__':
    ima = Image()
    fileIn = "D:/factory/stockShot/fire/embers/seq/embers_001/embers_001.0001-0070.jpg"
    # fileIn = "D:/factory/stockShot/fire/embers/seq/embers_001/embers_001.%04d.jpg"
    fileOut = "D:/factory/stockShot/fire/embers/seq/embers_001/toto2.mov"
    ima.createMovie(fileIn, fileOut, resize=(200, 200), ratio=True, force=True, printCmd=True)
