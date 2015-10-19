import os
from lib.system import procFile as pFile


def makeCheckFile(tmpCheckFile, loopNodeName, iterator, iter):
    """
    Create loop check file

    :param tmpCheckFile: Loop check file relative path
    :type tmpCheckFile: str
    :param loopNodeName: Loop node name
    :type loopNodeName: str
    :param iterator: Loop iterator
    :type iterator: str
    :param iter: Current loop iter
    :type iter: str | int
    :return: 'exists' if checkFile already exists, else 'create'
    :rtype: str
    """
    print "#--- Check TmpFile ---#"
    print "Tmp File:", tmpCheckFile
    #-- Check If File Exists --#
    if os.path.exists(tmpCheckFile):
        print "---> tmpFile found, skipp iter !"
        return 'exists'
    #-- Get CheckFile Text --#
    txt = ["Date = %r" % pFile.getDate(), "Time = %r" % pFile.getTime(),
           "Station = %r" % os.environ['COMPUTERNAME'], "User = %r" % os.environ['USERNAME'],
           "LoopNode = %r" % loopNodeName, "Iterator = %r" % iterator]
    if isinstance(iter, str):
        txt.append("Iter = %r" % iter)
        txt.append("%s = %r" % (iterator, iter))
    else:
        txt.append("Iter = %s" % iter)
        txt.append("%s = %s" % (iterator, iter))
    #-- Write CheckFile Text --#
    try:
        pFile.writeFile(tmpCheckFile, '\n'.join(txt))
        print "Check file written:", tmpCheckFile
        return 'create'
    except:
        raise IOError("!!! Can Not write check file: %s !!!" % tmpCheckFile)

def makeLauncher(launchFile, scriptFile, loopChecks=None):
    """
    Create node launcher file

    :param launchFile: Launcher script file name
    :type launchFile: str
    :param scriptFile: Node script file name
    :type scriptFile: str
    :param loopChecks: Loop check files
    :type loopChecks: list
    """
    txt = []
    #-- Python Launcher --#
    if launchFile.endswith('.py'):
        if loopChecks is not None:
            for loopFile in loopChecks:
                txt.append('execfile(%r)' % pFile.conformPath(loopFile))
        txt.append('execfile(%r)' % pFile.conformPath(scriptFile))
    #-- Mel Launcher --#
    elif launchFile.endswith('.mel'):
        if loopChecks is not None:
            for loopFile in loopChecks:
                txt.append('python("execfile(%r)");' % pFile.conformPath(loopFile))
        txt.append('python("execfile(%r)");' % pFile.conformPath(scriptFile))
    #-- Write Launcher --#
    try:
        pFile.writeFile(pFile.conformPath(os.path.realpath(launchFile)), '\n'.join(txt))
        print "Launcher file written:", pFile.conformPath(launchFile)
    except:
        raise IOError("!!! Can Not write launcher file: %s !!!" % pFile.conformPath(launchFile))
