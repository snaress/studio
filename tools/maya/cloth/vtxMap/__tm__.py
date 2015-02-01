#-- Global Proc --#
from lib.qt import procQt as pQt
reload(pQt)

#-- Maya Proc --#
from tools.maya.util.proc import procCloth as pCloth
reload(pCloth)
from tools.maya.util.proc import procRigg as pRigg
reload(pRigg)

#-- VtxMap Tool --#
from tools.maya.cloth import vtxMap
reload(vtxMap)
from tools.maya.cloth.vtxMap.ui import wgSceneNodesUI
reload(wgSceneNodesUI)
from tools.maya.cloth.vtxMap.ui import wgVtxEditUI
reload(wgVtxEditUI)
from tools.maya.cloth.vtxMap.ui import wgVtxInfoUI
reload(wgVtxInfoUI)
from tools.maya.cloth.vtxMap.ui import wgVtxMapUI
reload(wgVtxMapUI)
from tools.maya.cloth.vtxMap.ui import wgVtxTypeUI
reload(wgVtxTypeUI)
from tools.maya.cloth.vtxMap.ui import vtxMapUI
reload(vtxMapUI)
from tools.maya.cloth.vtxMap import vtxMapUi
reload(vtxMapUi)
from tools.maya.cloth.vtxMap import vtxMapWgts
reload(vtxMapWgts)
from tools.maya.cloth.vtxMap import vtxMapCmds
reload(vtxMapCmds)

#-- Launch Ui --#
vtxMapUi.launch()