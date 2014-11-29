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
from tools.maya.util import factory as initMayaFactory
reload(initMayaFactory)
from tools.maya.util.factory import factoryUi as mayaFactoryUi
reload(mayaFactoryUi)
from tools.maya.util.factory.ui import dialShaderUI
reload(dialShaderUI)

mayaFactoryUi.launch()
