#-- Global Proc --#
from lib.qt import procQt as pQt
reload(pQt)


#-- Maya Proc --#
from tools.maya.cmds import pScene, pCloth
reload(pScene)
reload(pCloth)


#-- VtxMap Tool --#
from tools.maya.cloth import vtxMap
reload(vtxMap)
from tools.maya.cloth.vtxMap.ui import wgSceneNodesUI, wgVtxEditUI, wgVtxInfoUI
reload(wgSceneNodesUI)
reload(wgVtxEditUI)
reload(wgVtxInfoUI)
from tools.maya.cloth.vtxMap.ui import wgVtxMapUI, wgVtxTypeUI, vtxMapUI, wgVtxFileUI
reload(wgVtxMapUI)
reload(wgVtxTypeUI)
reload(vtxMapUI)
reload(wgVtxFileUI)
from tools.maya.cloth.vtxMap import vtxMapUi, vtxMapWgts, vtxMapCmds
reload(vtxMapUi)
reload(vtxMapWgts)
reload(vtxMapCmds)


#-- Launch Ui --#
vtxMapUi.launch()