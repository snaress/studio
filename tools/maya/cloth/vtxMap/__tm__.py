#-- Global Proc --#
from lib.qt import procQt as pQt
reload(pQt)

#-- Maya Proc --#
from tools.maya.util.proc import procCloth as pCloth
reload(pCloth)

#-- VtxMap Tool --#
from tools.maya.cloth.vtxMap.ui import vtxMapUI as vmUi
reload(vmUi)
from tools.maya.cloth.vtxMap.ui import wgVtxMapUI
reload(wgVtxMapUI)
from tools.maya.cloth import vtxMap
reload(vtxMap)
from tools.maya.cloth.vtxMap import vtxMapUi
reload(vtxMapUi)
from tools.maya.cloth.vtxMap import vtxMapCmds as vmCmds
reload(vmCmds)

vtxMapUi.launch()