import os
from lib.env import studio
from lib.qt import procQt as pQt


#-- Packager Var --#
toolPath = os.path.normpath(os.path.dirname(__file__))
toolName = toolPath.split(os.sep)[-1]
toolPack = __package__


#-- Global Var --#
user = os.environ.get('username')
libPath = os.path.join(toolPath, '_lib')
rndBinPath = os.path.join(studio.rndBinPath, toolName)
factoryPath = os.path.normpath("D:/factory")


#-- Show Info --#
print '########## %s ##########' % toolName.upper()
print 'Tool Path : ', toolPath
print 'Tool Package : ', toolPack
print '#%s#' % ('-'*(22+len(toolName)))
print 'User : ', user
print 'Lib Path : ', libPath
print 'Factory : ', factoryPath
print 'rndBinPath: ', rndBinPath
pQt.CompileUi(uiDir=os.path.join(toolPath, 'ui'))
print '%s\n' % ('#'*(22+len(toolName)))