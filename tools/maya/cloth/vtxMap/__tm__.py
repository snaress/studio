#-- Global Proc --#
from lib.qt import procQt as pQt
reload(pQt)

#-- Maya Proc --#
from tools.maya.cmds import procUi
reload(procUi)
from tools.maya.cmds import procScene
reload(procScene)
from tools.maya.cmds import modeling
reload(modeling)
from tools.maya.cmds import procModeling
reload(procModeling)
from tools.maya.cmds import rigg
reload(rigg)
from tools.maya.cmds import cloth
reload(cloth)
from tools.maya.cmds import procCloth
reload(procCloth)
from tools.maya.cmds import procRender
reload(procRender)
import tools.maya.cmds as smc
reload(smc)

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