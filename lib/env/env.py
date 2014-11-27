import os, sys


#-- Package Var --#
toolPath = os.path.normpath(os.path.dirname(__file__))
toolName = toolPath.split(os.sep)[-1]
toolPack = __package__


#-- Studio Var --#
wsPath = os.sep.join(toolPath.split(os.sep)[:-2])
qtPath = "C:/Python27/Lib/site-packages"
for path in [wsPath, qtPath]:
    if not path in sys.path:
        print "[sys] | Info | Add %s to sysPath" % path
        sys.path.insert(0, path)
