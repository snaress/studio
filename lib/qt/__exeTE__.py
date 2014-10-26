import os, sys


#-- Package Var --#
toolPath = os.path.normpath(os.path.dirname(__file__))
toolName = toolPath.split(os.sep)[-1]
toolPack = __package__


#-- SysPath --#
wsPath = os.sep.join(toolPath.split(os.sep)[:-2])
if not wsPath in sys.path:
    print "[sys] | Info | Add %s to sysPath" % wsPath
    sys.path.insert(0, wsPath)


#-- Launch --#
from PyQt4 import QtGui
from lib.qt import textEditor
app = QtGui.QApplication(sys.argv)
window = textEditor.TextEditor()
window.show()
sys.exit(app.exec_())
