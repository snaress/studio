import sys


wsPath = "F:/rnd/workspace/studio"
qtPath = "C:/Python27/Lib/site-packages"
for path in [wsPath, qtPath]:
    if not path in sys.path:
        print "[sys] | Info | Add %s to sysPath" % path
        sys.path.insert(0, path)
