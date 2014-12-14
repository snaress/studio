import sys
from PyQt4 import QtGui
from lib.qt import scriptEditor


app = QtGui.QApplication(sys.argv)
window = scriptEditor.ScriptEditor()
window.show()
sys.exit(app.exec_())
