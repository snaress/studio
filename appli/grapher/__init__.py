import os
from lib.qt import procQt as pQt


#-- Packager Var --#
toolPath = os.path.normpath(os.path.dirname(__file__))
toolName = toolPath.split(os.sep)[-1]
toolPack = __package__
os.chdir(toolPath)


#-- Global Var --#
user = os.environ.get('username')
station = os.environ.get('computername')
grapherRootPath = os.path.join('E:', os.sep, 'grapher')
prodsRootPath =  os.path.join('E:', os.sep, 'prods')


#-- Show Info --#
print '########## %s ##########' % toolName.upper()
print 'Tool Path : ', toolPath
print 'Tool Package : ', toolPack
print '#%s#' % ('-'*(22+len(toolName)))
print 'User : ', user
print 'Station : ', station
print 'Grapher Root Path : ', grapherRootPath
print 'Prods Root Path : ', prodsRootPath
pQt.CompileUi2(uiDir=os.path.join(toolPath, 'gui', 'src'),
               uiDest=os.path.join(toolPath, 'gui', 'ui'))
print '%s\n' % ('#'*(22+len(toolName)))
