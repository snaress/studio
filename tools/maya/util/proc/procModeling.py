from lib.system import procMath as pMath
try:
    import maya.cmds as mc
except:
    pass


def creeBox(name=None):
    """ Create bbox from selection
        :param name: (str) : Bbox name
        :return: (str) : Bbox name """
    #-- Recup Info --#
    modelList = mc.ls(sl=True, type="transform") or []
    if len(modelList) == 0:
        mc.warning("Selectionne au moins un model !!!")
    else:
        #-- Recup Bbox--#
        minX = 100000
        maxX = -100000
        minY = 100000
        maxY = -100000
        minZ = 100000
        maxZ = -100000
        for model in modelList:
            modelMin = [mc.getAttr("%s.boundingBoxMinX" % model),
                        mc.getAttr("%s.boundingBoxMinY" % model),
                        mc.getAttr("%s.boundingBoxMinZ" % model)]
            modelMax = [mc.getAttr("%s.boundingBoxMaxX" % model),
                        mc.getAttr("%s.boundingBoxMaxY" % model),
                        mc.getAttr("%s.boundingBoxMaxZ" % model)]
            if modelMin[0] < minX:
                minX = modelMin[0]
            if modelMax[0] > maxX:
                maxX = modelMax[0]
            if modelMin[1] < minY:
                minY = modelMin[1]
            if modelMax[1] > maxY:
                maxY = modelMax[1]
            if modelMin[2] < minZ:
                minZ = modelMin[2]
            if modelMax[2] > maxZ:
                maxZ = modelMax[2]
        Vmin = [minX, minY, minZ]
        Vmax = [maxX, maxY, maxZ]
        #-- Recup Bbox Size --#
        p1 = list([Vmin[0], Vmax[1], Vmin[2]])
        p2 = list([Vmin[0], Vmin[1], Vmin[2]])
        p3 = list([Vmax[0], Vmin[1], Vmin[2]])
        p4 = list([Vmin[0], Vmin[1], Vmax[2]])
        W = pMath.getDistance(p2, p3)
        H = pMath.getDistance(p1, p2)
        D = pMath.getDistance(p2, p4)
        P = pMath.coordOp(Vmin, Vmax, "average")
        #-- Genere Bbox --#
        if name is None:
            boxName = mc.polyCube(n="newBox1", w=W, h=H, d=D)
        else:
            boxName = mc.polyCube(n=name, w=W, h=H, d=D)
        mc.xform(t=(P[0], P[1], P[2]))
        return boxName
