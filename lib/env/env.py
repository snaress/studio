import os, sys


#-- Package Var --#
toolPath = os.path.normpath(os.path.dirname(__file__))
toolName = toolPath.split(os.sep)[-1]
toolPack = __package__


#-- Studio Var --#
wsPath = os.sep.join(toolPath.split(os.sep)[:-2])
if not wsPath in sys.path:
    print "[sys] | Info | Add %s to sysPath" % wsPath
    sys.path.insert(0, wsPath)
