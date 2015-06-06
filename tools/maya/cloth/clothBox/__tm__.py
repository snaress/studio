#-- Global Proc --#
from lib.qt import procQt as pQt
reload(pQt)


#-- Maya Proc --#
from tools.maya.cmds import pScene, pMode, pRigg, pCloth
reload(pScene)
reload(pMode)
reload(pRigg)
reload(pCloth)


#-- clothBox Tool --#
from tools.maya.cloth import clothBox
reload(clothBox)
from tools.maya.cloth.clothBox.ui import wgModeBoxUI, wgRiggBoxUI, wgSimuBoxUI, clothBoxUI
reload(wgModeBoxUI)
reload(wgRiggBoxUI)
reload(wgSimuBoxUI)
reload(clothBoxUI)
from tools.maya.cloth.clothBox import clothBoxCmds, clothBoxWgts, clothBoxUi
reload(clothBoxCmds)
reload(clothBoxWgts)
reload(clothBoxUi)


#-- Launch Ui --#
clothBoxUi.launch()