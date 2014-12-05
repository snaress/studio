#-- Factory Appli --#
from appli import factory as initFactory
reload(initFactory)
from appli.factory import factory
reload(factory)
from appli.factory import factoryUi as factoryUi
reload(factoryUi)
from appli.factory.ui import factoryUI, wgtThumbnailUI, dialTransfertUI
reload(factoryUI)
reload(wgtThumbnailUI)
reload(dialTransfertUI)

#-- Global Proc --#
from lib.system import procFile as pFile
reload(pFile)

#-- Maya Proc --#
from tools.maya.util.proc import procScene as pScene
reload(pScene)
from tools.maya.util.proc import procMapping as pMap
reload(pMap)
from tools.maya.util.proc import procRender as pRender
reload(pRender)

#-- Factory Tool --#
from tools.maya.util import factory as initMayaFactory
reload(initMayaFactory)
from tools.maya.util.factory import factoryUi as mayaFactoryUi
reload(mayaFactoryUi)
from tools.maya.util.factory import factoryCmds as fCmds
reload(fCmds)
from tools.maya.util.factory.ui import dialShaderUI
reload(dialShaderUI)


mayaFactoryUi.launch()
