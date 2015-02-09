#-- Global Proc --#
from lib.qt import procQt
reload(procQt)
from lib.system import procFile as pFile
reload(pFile)
from lib.system import procMath as pMath
reload(pMath)

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

#-- CamPrez Tool --#
from tools.maya.camera.camPrez.ui import camPrezUI
reload(camPrezUI)
from tools.maya.camera import camPrez
reload(camPrez)
from tools.maya.camera.camPrez import camPrezUi
reload(camPrezUi)
from tools.maya.camera.camPrez import camPrezCmds
reload(camPrezCmds)


camPrezUi.launch()
