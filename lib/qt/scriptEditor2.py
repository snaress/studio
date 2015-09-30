from PyQt4 import QtGui
from PyQt4.Qsci import QsciScintilla, QsciLexerPython


class ScriptEditor(QsciScintilla):

    def __init__(self, parent=None):
        super(ScriptEditor, self).__init__(parent)
        self.markerNum = 8
        self._setupWidget()

    # noinspection PyUnresolvedReferences
    def _setupWidget(self):
        #-- Font --#
        font = QtGui.QFont('Courier', 10, QtGui.QFont.Normal)
        font.setStyleHint(QtGui.QFont.Monospace)
        fm = QtGui.QFontMetrics(font)
        #-- Line Numbers --#
        self.setMarginWidth(0, fm.width("000"))
        self.setMarginLineNumbers(0, True)
        self.setAutoIndent(True)
        #-- Edge --#
        self.setEdgeMode(QsciScintilla.EdgeLine)
        self.setEdgeColumn(80)
        self.setEdgeColor(QtGui.QColor(255, 0, 0))
        #-- Folding --#
        self.setFolding(QsciScintilla.BoxedTreeFoldStyle)
        #-- Markers --#
        self.setMarginSensitivity(1, True)
        self.marginClicked.connect(self.on_marginClicked)
        self.markerDefine(QsciScintilla.RightArrow, self.markerNum)
        self.setMarkerBackgroundColor(QtGui.QColor(255, 0, 0), self.markerNum)
        #-- Tab --#
        self.setIndentationsUseTabs(True)
        self.setIndentationGuides(True)
        self.setTabWidth(4)
        self.setTabIndents(True)
        #-- White Space --#
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setWhitespaceVisibility(QsciScintilla.SC_PRINT_BLACKONWHITE)
        self.setWhitespaceSize(2)
        #-- Lexer --#
        lexer = QsciLexerPython()
        lexer.setDefaultFont(font)
        lexer.setFont(font)
        self.setLexer(lexer)
        self.recolor()
        #-- Completion --#
        self.setAutoCompletionThreshold(2)
        self.setAutoCompletionSource(QsciScintilla.AcsDocument)
        self.setAutoCompletionCaseSensitivity(True)
        self.setAutoCompletionReplaceWord(True)
        self.setAutoCompletionFillupsEnabled(True)

    def on_marginClicked(self, nmargin, nline, modifiers):
        if not self.markersAtLine(nline) == 0:
            self.markerDelete(nline, self.markerNum)
        else:
            self.markerAdd(nline, self.markerNum)
        print self.text()

    def getCode(self):
        return self.text()

    def setCode(self, text):
        self.setText(text)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = ScriptEditor()
    window.resize(640, 512)
    window.show()
    sys.exit(app.exec_())
