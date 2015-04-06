#-- Global Proc --#
from lib.qt import procQt as pQt
reload(pQt)


#-- Maya Proc --#
from tools.maya.cmds import pScene, pRigg
reload(pScene)
reload(pRigg)


#-- clothEditor Tool --#
from tools.maya.cloth import clothEditor
reload(clothEditor)
from tools.maya.cloth.clothEditor.ui import wgSceneNodesUI, wgAttrUI, wgAttrNodeUI, wgVtxMapUI, wgVtxMapNodeUI
reload(wgSceneNodesUI)
reload(wgAttrUI)
reload(wgAttrNodeUI)
reload(wgVtxMapUI)
reload(wgVtxMapNodeUI)
from tools.maya.cloth.clothEditor.ui import clothEditorUI
reload(clothEditorUI)
from tools.maya.cloth.clothEditor import clothEditorUi, clothEditorWgts, clothEditorCmds
reload(clothEditorUi)
reload(clothEditorWgts)
reload(clothEditorCmds)


#-- Launch Ui --#
clothEditorUi.launch()
