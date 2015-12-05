import os
from lib.qt import procQt as pQt


#-- Packager Var --#
toolPath = os.path.normpath(os.path.dirname(__file__))
toolName = toolPath.split(os.sep)[-1]
toolPack = __package__


#-- Compile Ui --#
print '%s %s %s' % ('#'*30, toolName.capitalize() ,'#'*30)
print 'Tool Path : ', toolPath
print 'Tool Package : ', toolPack
print '#%s#' % ('-'*(60+len(toolName)))
pQt.CompileUi2(uiDir=os.path.join(toolPath, 'src'),
               uiDest=os.path.join(toolPath, 'ui'))
print '%s\n' % ('#'*(62+len(toolName)))
