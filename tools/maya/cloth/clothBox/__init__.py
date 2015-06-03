import os
from lib.qt import procQt as pQt


#-- Packager Var --#
toolPath = os.path.normpath(os.path.dirname(__file__))
toolName = toolPath.split(os.sep)[-1]
toolPack = __package__
iconPath = os.path.join(toolPath, 'icon')

pQt.CompileUi2(uiDir=toolPath)