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

#-- Factory Tool --#
from tools.maya.util import factory as initMayaFactory
reload(initMayaFactory)
from tools.maya.util.factory.ui import dialShaderUI
reload(dialShaderUI)
from tools.maya.util.factory import factoryUi as mayaFactoryUi
reload(mayaFactoryUi)
from tools.maya.util.factory import factoryCmds as fCmds
reload(fCmds)


mayaFactoryUi.launch()
