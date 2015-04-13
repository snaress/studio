import maya.cmds as mc


def buttonConstrain():
    """ Create button constrain
        :return: ButtonConstrain class dict,
                 ('parent', 'master', 'masterVtx', 'slaveRef',
                  'slaveRefVtx', 'slave', 'slaveVtx', 'const', 'bs')
        :rtype: dict """
    bc = ButtonConstrain()
    bc._exec(createCtrn=True, keepOrient=True, createBS=True)
    return bc.__dict__

class ButtonConstrain(object):

    def __init__(self):
        print "\n########## Button Constrain ##########"
        self.parent = None
        self.master = None
        self.masterVtx = None
        self.slaveRef = None
        self.slaveRefVtx = None
        self.slave = None
        self.slaveVtx = None
        self.const = None
        self.bs = None
        self.checkSelection()

    def _exec(self, createCtrn=False, keepOrient=False, createBS=False):
        """ Create constrain
            :param keepOrient: Trye to keep original orient
            :type keepOrient: bool """
        if createCtrn:
            self.createSlave()
            self.centerPivot()
            self.createConstrain()
        if keepOrient:
            self.keepOrient()
        if createBS:
            self.blendSlave()

    def checkSelection(self):
        """ Check if selection is valide
            :return: True if success
            :rtype: bool """
        print "#-- Check Selection --#"
        sel = mc.ls(sl=True)
        #-- Check Selection Size --#
        if not len(sel) == 2:
            raise IOError, "!!! Select master, then slave !!!"
        #-- Check Selection Contents --#
        if not '.vtx' in sel[0] or not '.vtx' in sel[1]:
            raise IOError, "!!! Select master vtx, then slave vtx !!!"
        #-- Parse Selection --#
        self.masterVtx = sel[0]
        self.slaveRefVtx = sel[1]
        self.master = mc.listRelatives(mc.listRelatives(self.masterVtx, p=True, pa=True)[0], p=True, pa=True)[0]
        self.slaveRef = mc.listRelatives(mc.listRelatives(self.slaveRefVtx, p=True, pa=True)[0], p=True, pa=True)[0]
        #-- Check Master And Slave --#
        if self.master == self.slaveRef:
            raise IOError, "!!! Error: First selection should be master, second and third should be slave !!!"
        #-- Result --#
        print "---> Done !"
        return True

    def createSlave(self):
        """ Create Slave model """
        print "#-- Create Slave --#"
        #-- Duplicate Ref Model --#
        self.slave = mc.duplicate(self.slaveRef, n="%s_cp#" % self.slaveRef)[0]
        mc.delete(self.slave, ch=True)
        self.slaveVtx = "%s.%s" % (self.slave, self.slaveRefVtx.split('.')[-1])
        slavePos = mc.xform(self.slaveVtx, q=True, t=True, ws=True)
        print "Duplicate riginal slave --> OK"
        #-- Create Locator --#
        loc = mc.createNode('locator')
        self.parent = mc.rename(mc.listRelatives(loc, p=True, pa=True)[0], "N_%s" % self.slave)
        mc.setAttr('%s.translate' % self.parent, slavePos[0], slavePos[1], slavePos[2])
        print "Create slave locator --> OK"
        #-- Parent Slave --#
        mc.parent(self.slave, self.parent)
        print "Parent slave to locator --> OK"
        print "---> Done !"

    def centerPivot(self):
        """ Snap slave pivot on slaveVtx1 """
        print "#-- Edit Pivot --#"
        curPos = mc.xform(self.slaveVtx, q=True, t=True, ws=True)
        mc.xform(self.slave, piv=(curPos[0], curPos[1], curPos[2]), ws=True)
        print "---> Done !"

    def createConstrain(self):
        """ Constrain slave to masterVtx """
        print "#-- Constrain Button --#"
        #-- Create Constrain --#
        self.const = mc.pointOnPolyConstraint(self.masterVtx, self.parent)[0]
        print "Create constrain ---> OK:", self.const
        #-- Edit Constrain --#
        uvMap = mc.polyListComponentConversion(self.masterVtx, fvf=True, tuv=True)[0]
        uvVal = mc.polyEditUV(uvMap, q=True, u=True, v=True)
        mc.setAttr("%s.%sU0" % (self.const, self.master), uvVal[0])
        mc.setAttr("%s.%sV0" % (self.const, self.master), uvVal[1])
        print "Edit constrain ---> OK: U=%s  V=%s" % (uvVal[0], uvVal[1])
        print "---> Done !"

    def keepOrient(self):
        """ Try to keep original orient """
        print "#-- Keep Orient --#"
        newOrient = mc.getAttr("%s.rotate" % self.parent)[0]
        mc.setAttr("%s.rotate" % self.slave, (newOrient[0] * -1), (newOrient[1] * -1), (newOrient[2] * -1))
        print "---> Done !"

    def blendSlave(self):
        """ BlendShape between slave and original model """
        print "#-- Blend Slave --#"
        #-- Create BlendShape --#
        self.bs = mc.blendShape(self.slave, self.slaveRef, n="BS_%s" % self.slave, bf=True, o='world')[0]
        print "Create BlendShape ---> OK:", self.bs
        #-- Select Continuous Vertex --#
        mc.select(self.slaveRefVtx, r=True)
        vtxSel = mc.polyEvaluate(self.slaveRef, vc=True)
        self.polySelectTraverse()
        while not mc.polyEvaluate(self.slaveRef, vc=True) == vtxSel:
            vtxSel = mc.polyEvaluate(self.slaveRef, vc=True)
            self.polySelectTraverse()
        sel = mc.ls(sl=True, fl=True)
        print "Select continous vertex ---> OK"
        #-- Edit BS Weights PerVertex --#
        for n in range(mc.polyEvaluate(self.slaveRef, v=True)):
            vtx = "%s.vtx[%s]" % (self.slaveRef, n)
            if vtx in sel:
                mc.setAttr("%s.inputTarget[0].baseWeights[%s]" % (self.bs, n), 1)
            else:
                mc.setAttr("%s.inputTarget[0].baseWeights[%s]" % (self.bs, n), 0)
        mc.blendShape(self.bs, e=True, w=(0, 1))
        print "Edit blendShape weights perVertex ---> OK"
        print "---> Done !"

    @staticmethod
    def polySelectTraverse(traversal=1):
        """ Grow polyComponent selection
            :param traversal: 0 = Off.
                              1 = More : will add current selection border to current selection.
                              2 = Less : will remove current selection border from current selection.
                              3 = Border : will keep only current selection border.
                              4 = Contiguous Edges : Add edges aligned with the current edges selected
            :type traversal: int """
        #-- Vertex --#
        result = mc.polyListComponentConversion(fv=True, tv=True)
        if result:
            mc.polySelectConstraint(pp=traversal, t=0x0001)
        else:
            #-- Edge --#
            result = mc.polyListComponentConversion(fe=True, te=True)
            if result:
                mc.polySelectConstraint(pp=traversal, t=0x8000)
            else:
                #-- Face --#
                result = mc.polyListComponentConversion(ff=True, tf=True)
                if result:
                    mc.polySelectConstraint(pp=traversal, t=0x0008)
                else:
                    #-- Uv --#
                    result = mc.polyListComponentConversion(fuv=True, tuv=True)
                    if result:
                        mc.polySelectConstraint(pp=traversal, t=0x0010)
