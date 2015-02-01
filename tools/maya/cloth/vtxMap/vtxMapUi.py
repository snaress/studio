from PyQt4 import QtGui
from functools import partial
from tools.maya.util.proc import procUi as pUi
from tools.maya.cloth.vtxMap.ui import vtxMapUI
from tools.maya.cloth.vtxMap import vtxMapWgts as vmWgts
from tools.maya.cloth.vtxMap import vtxMapCmds as vmCmds
try:
    import maya.cmds as mc
except:
    pass


class VtxMapUi(QtGui.QMainWindow, vtxMapUI.Ui_mwVtxMap):

    def __init__(self, parent=None):
        super(VtxMapUi, self).__init__(parent)
        self._setupUi()
        self._initUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup main ui """
        self.setupUi(self)
        self._initWidgets()
        self.pbInit.clicked.connect(partial(self.on_init, shapeName=None))
        self.pbSelect.clicked.connect(self.on_select)
        self.cbSceneNodes.clicked.connect(self.rf_sceneNodesVisibility)

    def _initWidgets(self):
        """ Import main ui widgets """
        self.wgSceneNodes = vmWgts.SceneNodeUi(self)
        self.vlSceneNodes.insertWidget(0, self.wgSceneNodes)
        self.wgVtxType = vmWgts.VtxMapUi(self)
        self.vlMapType.insertWidget(0, self.wgVtxType)
        self.wgVtxEdit = vmWgts.VtxEditUi(self)
        self.vlVtxEdition.insertWidget(0, self.wgVtxEdit)
        self.wgVtxInfo = vmWgts.VtxInfoUi(self)
        self.vlVtxValues.insertWidget(0, self.wgVtxInfo)

    def _initUi(self):
        """ Initialized main ui """
        self.wgSceneNodes.rf_sceneNodes()

    @property
    def clothNode(self):
        """ Get cloth node name from ui
            :return: Initialized cloth node name
            :rtype: str """
        clothNode = str(self.leInit.text())
        if clothNode in ['', ' ', '  ']:
            return None
        return clothNode

    def rf_sceneNodesVisibility(self):
        """ Refresh scene nodes widget visibility """
        if self.cbSceneNodes.isChecked():
            self.vfSceneNodes.setVisible(True)
            self.wgSceneNodes.rf_sceneNodes()
        else:
            self.vfSceneNodes.setVisible(False)
            self.wgSceneNodes.twSceneNodes.clear()

    def on_init(self, shapeName=None):
        """ Command launched when QPushButton 'Init' is clicked,
            Update mainUi with selected cloth node
            :param shapeName: Force update with given node
            :type shapeName: str """
        self.leInit.clear()
        if shapeName is not None:
            self.leInit.setText(shapeName)
        else:
            clothNodes = vmCmds.getClothNodesFromSel()
            if clothNodes:
                self.leInit.setText(clothNodes[0])
        self.wgVtxType.rf_mapType()

    def on_select(self):
        """ Command launched when QPushButton 'Select' is clicked,
            Update scene selection with initialized cloth node """
        if self.clothNode is not None:
            vmCmds.selectClothNode(self.clothNode)

    @staticmethod
    def cleanVtxIndexList(selected=None, indexOnly=False):
        """ Get a clean index list from selected
            :param selected: Force using given selection list, if None, parse scene
            :type selected: list
            :param indexOnly: If True, return index only, else fullName
            :type indexOnly: bool
            :return: Clean index list
            :rtype: list """
        if selected is None:
            selected = mc.ls(sl=True)
        selVtx = []
        for node in selected:
            if node.endswith(']'):
                selName = node.split('.')[0]
                ind = node.split('.')[-1].replace('vtx[', '').replace(']','')
                if not ':' in ind:
                    if indexOnly:
                        selVtx.append(int(ind))
                    else:
                        selVtx.append("%s.vtx[%s]" % (selName, ind))
                else:
                    deb = int(ind.split(':')[0])
                    fin = int(ind.split(':')[1])
                    for n in range(deb, (fin + 1), 1):
                        if indexOnly:
                            selVtx.append(n)
                        else:
                            selVtx.append("%s.vtx[%s]" % (selName, n))
        return selVtx


def launch():
    """ Launch VtxMap
        :return: Launched window
        :rtype: object """
    toolName = 'mwVtxMap'
    if mc.window(toolName, q=True, ex=True):
        mc.deleteUI(toolName, wnd=True)
    global window
    window = VtxMapUi(parent=pUi.getMayaMainWindow())
    window.show()
    return window
