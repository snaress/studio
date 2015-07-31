#-- Global Proc --#
from lib.qt import procQt as pQt
reload(pQt)


#-- Maya Proc --#
from tools.maya.cmds import pScene, pCloth
reload(pScene)
reload(pCloth)


#-- clothEditor Tool --#
from tools.maya.cloth import dynEval
reload(dynEval)
from tools.maya.cloth.dynEval.ui import wgSceneNodesUI, wgSceneNodeUI, wgCacheEvalUI, wgCacheListUI, wgCacheInfoUI
reload(wgSceneNodesUI)
reload(wgSceneNodeUI)
reload(wgCacheEvalUI)
reload(wgCacheListUI)
reload(wgCacheInfoUI)
from tools.maya.cloth.dynEval.ui import dynEvalUI
reload(dynEvalUI)
from tools.maya.cloth.dynEval import dynEvalCmds, dynEvalWgts, dynEvalUi
reload(dynEvalCmds)
reload(dynEvalWgts)
reload(dynEvalUi)


#-- Launch Ui --#
dynEvalUi.launch()