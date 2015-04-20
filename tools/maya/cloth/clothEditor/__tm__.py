#-- Global Proc --#
from lib.qt import procQt as pQt
reload(pQt)


#-- Maya Proc --#
from tools.maya.cmds import pScene, pMode, pRigg, pCloth
reload(pScene)
reload(pMode)
reload(pRigg)
reload(pCloth)


#-- clothEditor Tool --#
from tools.maya.cloth import clothEditor
reload(clothEditor)
from tools.maya.cloth.clothEditor.ui import wgSceneNodesUI, wgSceneNodeUI, wgAttrUI, wgAttrNodeUI
reload(wgSceneNodesUI)
reload(wgSceneNodeUI)
reload(wgAttrUI)
reload(wgAttrNodeUI)
from tools.maya.cloth.clothEditor.ui import wgVtxMapUI, wgVtxMapNodeUI, wgFilesUI
reload(wgVtxMapUI)
reload(wgVtxMapNodeUI)
reload(wgFilesUI)
from tools.maya.cloth.clothEditor.ui import clothEditorUI
reload(clothEditorUI)
from tools.maya.cloth.clothEditor import clothEditorUi, clothEditorWgts, clothEditorCmds
reload(clothEditorUi)
reload(clothEditorWgts)
reload(clothEditorCmds)


#-- Launch Ui --#
clothEditorUi.launch()
