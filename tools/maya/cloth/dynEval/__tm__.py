#-- Global Proc --#
from lib.qt import procQt as pQt
reload(pQt)


#-- Maya Proc --#
from tools.maya.cmds import pScene, pRigg, pCloth, pCache
reload(pScene)
reload(pRigg)
reload(pCloth)
reload(pCache)


#-- clothEditor Tool --#
from tools.maya.cloth import dynEval
reload(dynEval)
from tools.maya.cloth.dynEval.ui import wgSceneNodesUI, wgSceneNodeUI, wgDynEvalUI, wgCacheListUI,\
                                        wgCacheNodeUI, wgCacheInfoUI
reload(wgSceneNodesUI)
reload(wgSceneNodeUI)
reload(wgDynEvalUI)
reload(wgCacheListUI)
reload(wgCacheNodeUI)
reload(wgCacheInfoUI)
from tools.maya.cloth.dynEval.ui import dynEvalUI
reload(dynEvalUI)
from tools.maya.cloth.dynEval import dynEvalCmds, dynEvalWgts, dynEvalUi
reload(dynEvalCmds)
reload(dynEvalWgts)
reload(dynEvalUi)


#-- Launch Ui --#
dynEvalUi.launch()