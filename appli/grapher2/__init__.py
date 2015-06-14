import os
from lib.qt import procQt as pQt


#-- Packager Var --#
toolPath = os.path.normpath(os.path.dirname(__file__))
toolName = toolPath.split(os.sep)[-1]
toolPack = __package__


#-- Global Var --#
user = os.environ.get('username')
station = os.environ.get('computername')
iconPath = os.path.join(toolPath, 'icon')


#-- Show Info --#
print '########## %s ##########' % toolName.upper()
print 'Tool Path : ', toolPath
print 'Tool Package : ', toolPack
print 'Icon Path : ', iconPath
print '#%s#' % ('-'*(22+len(toolName)))
print 'User : ', user
print 'Station : ', station
pQt.CompileUi2(uiDir=toolPath)
print '%s\n' % ('#'*(22+len(toolName)))
