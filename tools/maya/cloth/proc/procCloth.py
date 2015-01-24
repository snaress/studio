try:
    import maya.cmds as mc
except:
    pass


def getClothNodeFromSel(raiseError=False):
    """ Try to find cloth node connected to selected object.
        Only one object must be selected
        :param raiseError: (bool) : Raise error enable
        :return: (str) : Cloth node name, or None if cloth node not found """
    selection = mc.ls(sl=True)
    #-- Check Selection --#
    if not len(selection) == 1:
        log = "!!! WARNING: Select only one object !!!"
        if raiseError:
            raise ValueError, log
        print log
        return None
    #-- Search Cloth Node --#
    return getClothNode(selection[0], raiseError=raiseError)

def getClothNode(objectName, debug=False, raiseError=False):
    """ Try to find cloth node connected to given object
        :param objectName: (str) : Transform or Mesh node name
        :param debug: (bool) : Enable debug lines
        :param raiseError: (bool) : Raise error enable
        :return: (str) : Cloth node name, or None if cloth node not found """
    #-- Check Object Type --#
    selObj = objectName
    if mc.nodeType(selObj) == "transform":
        if debug:
            print "SelType detected: transform"
        shapes = mc.listRelatives(selObj, s=True, ni=True)
        #-- Check Connected Shape --#
        if shapes is None:
            log = "!!! WARNING: Shape not found !!!"
            if raiseError:
                raise ValueError, log
            print log
            return None
        #-- Check No-Intermediate Shape --#
        if not len(shapes) == 1:
            log = "!!! WARNING: Selection should have only one non-intermediate shape !!!"
            if raiseError:
                raise ValueError, log
            print log
            return None
        selShape = shapes[0]
    elif mc.nodeType(selObj) == "mesh":
        if debug:
            print "SelType detected: mesh"
        selShape = selObj
    else:
        log = "!!! WARNING: SelType should be 'transform' or 'mesh', get %s" % mc.nodeType(selObj)
        if raiseError:
            raise ValueError, log
        print log
        return None
    #-- Search Cloth Node --#
    connections = mc.listConnections(selShape, s=True, d=True, p=True)
    for c in connections:
        cName = c.split('.')[0]
        if mc.nodeType(cName) == "nCloth":
            print "Cloth node found: ", cName
            return cName
    print "---> getClothNode result: No cloth node found"
    return None
