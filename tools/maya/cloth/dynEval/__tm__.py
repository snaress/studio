#-- Global Proc --#
from lib.qt import procQt as pQt
reload(pQt)
from lib.system import procFile as pFile
reload(pFile)


#-- Maya Proc --#
from tools.maya.cmds import pScene, pMode, pRigg, pCloth, pCache
reload(pScene)
reload(pMode)
reload(pRigg)
reload(pCloth)
reload(pCache)


#-- clothEditor Tool --#
from tools.maya.cloth import dynEval
reload(dynEval)
from tools.maya.cloth.dynEval.ui import wgSceneNodesUI, wgSceneNodeUI, wgDynEvalUI, wgCacheListUI,\
                                        wgCacheNodeUI, wgCacheInfoUI, wgInfoNodeUI
reload(wgSceneNodesUI)
reload(wgSceneNodeUI)
reload(wgDynEvalUI)
reload(wgCacheListUI)
reload(wgCacheNodeUI)
reload(wgCacheInfoUI)
reload(wgInfoNodeUI)
from tools.maya.cloth.dynEval.ui import dynEvalUI
reload(dynEvalUI)
from tools.maya.cloth.dynEval import dynEvalCmds, dynEvalWgts, dynEvalUi
reload(dynEvalCmds)
reload(dynEvalWgts)
reload(dynEvalUi)


#-- Launch Ui --#
_dynEvalUi = dynEvalUi.launch()