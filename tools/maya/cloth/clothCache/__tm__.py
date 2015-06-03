#-- Global Proc --#
from lib.qt import procQt as pQt
reload(pQt)


#-- Maya Proc --#
from tools.maya.cmds import pScene
reload(pScene)


#-- clothEditor Tool --#
from tools.maya.cloth import clothCache
reload(clothCache)
from tools.maya.cloth.clothCache.ui import wgSceneNodesUI, wgSceneNodeUI, wgCacheEvalUI, wgCacheListUI, wgCacheInfoUI
reload(wgSceneNodesUI)
reload(wgSceneNodeUI)
reload(wgCacheEvalUI)
reload(wgCacheListUI)
reload(wgCacheInfoUI)
from tools.maya.cloth.clothCache.ui import clothCacheUI
reload(clothCacheUI)
from tools.maya.cloth.clothCache import clothCacheCmds, clothCacheWgts, clothCacheUi
reload(clothCacheCmds)
reload(clothCacheWgts)
reload(clothCacheUi)


#-- Launch Ui --#
clothCacheUi.launch()