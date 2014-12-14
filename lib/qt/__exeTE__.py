import sys
from PyQt4 import QtGui
from lib.qt import textEditor


app = QtGui.QApplication(sys.argv)
window = textEditor.TextEditor()
window.show()
sys.exit(app.exec_())
