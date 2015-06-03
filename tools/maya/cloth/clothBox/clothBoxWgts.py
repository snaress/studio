import os
from PyQt4 import QtGui
from functools import partial
from tools.maya.cloth.clothBox import clothBoxCmds as cbCmds
from tools.maya.cloth.clothBox.ui import wgModeBoxUI, wgRiggBoxUI


class ModeBoxUi(QtGui.QWidget, wgModeBoxUI.Ui_wgModeBox):
    """ Widget ModeBox, child of mainUi
        :param mainUi: ClothBox mainUi
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        print "\t ---> ModeBoxUi"
        self.mainUi = mainUi
        self.duplicateSelectedIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'duplicateSelected.png'))
        self.createOutMeshIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'outMeshCreate.png'))
        self.connectOutMeshIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'outMeshConnect.png'))
        self.updateOutMeshIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'outMeshUpdate.png'))
        super(ModeBoxUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        self.pbDuplicateSelected.setIcon(self.duplicateSelectedIcon)
        self.pbDuplicateSelected.clicked.connect(self.on_duplicateSelected)
        self.pbCreateOutMesh.setIcon(self.createOutMeshIcon)
        self.pbCreateOutMesh.clicked.connect(self.on_createOutMesh)
        self.pbConnectOutMesh.setIcon(self.connectOutMeshIcon)
        self.pbConnectOutMesh.clicked.connect(self.on_connectOutMesh)
        self.pbUpdateOutMesh.setIcon(self.updateOutMeshIcon)
        self.pbUpdateOutMesh.clicked.connect(self.on_updateOutMesh)

    @staticmethod
    def on_duplicateSelected():
        """ Command launched when 'Duplicate Selected' QPushButton is clicked """
        cbCmds.duplicateSelected()

    @staticmethod
    def on_createOutMesh():
        """ Command launched when 'Create OutMesh' QPushButton is clicked """
        cbCmds.createOutMesh()

    @staticmethod
    def on_connectOutMesh():
        """ Command launched when 'Connect OutMesh' QPushButton is clicked """
        cbCmds.connectOutMesh()

    @staticmethod
    def on_updateOutMesh():
        """ Command launched when 'Update OutMesh' QPushButton is clicked """
        cbCmds.updateOutMesh()


class RiggBoxUi(QtGui.QWidget, wgRiggBoxUI.Ui_wgRiggBox):
    """ Widget RiggBox, child of mainUi
        :param mainUi: ClothBox mainUi
        :type mainUi: QtGui.QMainWindow """

    def __init__(self, mainUi):
        print "\t ---> RiggBoxUi"
        self.mainUi = mainUi
        self.nClothIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'nCloth.png'))
        self.nRigidIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'nRigid.png'))
        self.nContraintIcon = QtGui.QIcon(os.path.join(self.mainUi.iconPath, 'nConstraint.png'))
        super(RiggBoxUi, self).__init__()
        self._setupUi()

    # noinspection PyUnresolvedReferences
    def _setupUi(self):
        """ Setup widget ui """
        self.setupUi(self)
        #-- nCloth --#
        self.pbPickClothDriver.clicked.connect(partial(self.on_pick, self.leClothDriver, "mesh"))
        self.leClothMesh.wgResult = self.leClothResult
        self.pbPickClothMesh.clicked.connect(partial(self.on_pick, self.leClothMesh, "mesh"))
        self.pbClothSolverRf.clicked.connect(partial(self.rf_clothSolver, self.cbClothSolver))
        self.pbCreateCloth.setIcon(self.nClothIcon)
        self.pbCreateCloth.clicked.connect(self.on_createCloth)
        #-- nRigid --#
        self.pbPickRigidDriver.clicked.connect(partial(self.on_pick, self.leRigidDriver, "pass"))
        self.leRigidMesh.wgResult = self.leRigidResult
        self.pbPickRigidMesh.clicked.connect(partial(self.on_pick, self.leRigidMesh, "pass"))
        self.pbRigidSolverRf.clicked.connect(partial(self.rf_clothSolver, self.cbRigidSolver))
        self.pbCreateRigid.setIcon(self.nRigidIcon)
        self.pbCreateRigid.clicked.connect(self.on_createRigid)
        #-- nConstraint --#
        self.leConstraint.wgResult = self.leConstResult
        self.pbPickConstraint.clicked.connect(partial(self.on_pick, self.leConstraint, "const"))
        self.pbStoreConst.setIcon(self.nContraintIcon)
        self.pbStoreConst.clicked.connect(self.on_storeConstraint)

    @property
    def clothSolver(self):
        """ Get current cloth solver
            :return: Cloth solver
            :rtype: str """
        return str(self.cbClothSolver.currentText())

    @property
    def rigidSolver(self):
        """ Get current rigid solver
            :return: Rigid solver
            :rtype: str """
        return str(self.cbRigidSolver.currentText())

    @property
    def passiveMode(self):
        """ Get current passive mode
            :return: Passive mode ('collide', 'pushOut', 'passive')
            :rtype: str """
        if self.rbCollide.isChecked():
            return "collide"
        elif self.rbPushOut.isChecked():
            return "pushOut"
        elif self.rbPassive.isChecked():
            return "passive"

    @staticmethod
    def rf_clothSolver(QComboBox):
        """ Refresh Cloth and passive solver list """
        QComboBox.clear()
        nucleusList = cbCmds.getAllNucleus()
        nucleusList.insert(0, "New Nucleus")
        QComboBox.addItems(nucleusList)

    def on_pick(self, QLineEdit, suffixe):
        """ Command launched when 'Pick' QPushButton is clicked
            :param QLineEdit: LineEdit to fill
            :type QLineEdit: QtGui.QLineEdit
            :param suffixe: Node suffixe ('mesh', 'pass', 'const'
            :type suffixe: str """
        sceneSel = cbCmds.getSceneSelection()
        if sceneSel:
            QLineEdit.setText(sceneSel[0])
            if hasattr(QLineEdit, 'wgResult'):
                if suffixe == 'pass':
                    if self.rigidSolver == "New Nucleus":
                        result = "%s_%s" % (sceneSel[0], suffixe)
                    else:
                        clothGrp = cbCmds.getParentTransform(self.rigidSolver)[0]
                        prefixe = clothGrp.replace('GRP_', '')
                        if sceneSel[0].startswith(prefixe.split('_')[0]):
                            name = '_'.join(sceneSel[0].split('_')[1:])
                        else:
                            name = sceneSel[0]
                        result = "%s_%s_%s" % (prefixe, name, suffixe)
                elif suffixe == 'const':
                    clothNode = cbCmds.findtype(sceneSel[0], ['nCloth'])[0]
                    dynName = '_'.join(clothNode.split('_')[:-1])
                    result = "%s_%s_%s" % (sceneSel[0], dynName, suffixe)
                else:
                    result = "%s_%s" % (sceneSel[0], suffixe)
                QLineEdit.wgResult.setText(result)

    def on_createCloth(self):
        """ Command launched when 'Create Cloth' QPushButton is clicked """
        driver = str(self.leClothDriver.text())
        mesh = str(self.leClothMesh.text())
        result = str(self.leClothResult.text())
        if driver in ["", " "] or mesh in ["", " "] or result in ["", " "]:
            raise ValueError, "!!! ClothDriver, ClothMesh or ClothResult can not be empty !!!"
        cbCmds.createCloth(driver, mesh, result, self.clothSolver)

    def on_createRigid(self):
        """ Command launched when 'Create Rigid' QPushButton is clicked """
        driver = str(self.leRigidDriver.text())
        mesh = str(self.leRigidMesh.text())
        result = str(self.leRigidResult.text())
        if driver in ["", " "] or mesh in ["", " "] or result in ["", " "]:
            raise ValueError, "!!! RigidDriver, RigidMesh or RigidResult can not be empty !!!"
        cbCmds.createRigid(driver, mesh, result, self.passiveMode, self.rigidSolver)

    def on_storeConstraint(self):
        """ Command launched when 'Store Constraint' QPushButton is clicked """
        dynConst = str(self.leConstraint.text())
        result = str(self.leConstResult.text())
        if dynConst in ["", " "] or result in ["", " "]:
            raise ValueError, "!!! DynConstraint, DynResult can not be empty !!!"
        cbCmds.storeConstraint(dynConst, result)