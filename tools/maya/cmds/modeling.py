try:
    import maya.cmds as mc
except:
    pass


def getBboxInfoFromMesh(mesh):
    """ Get boundingBox info from given mesh
        :param mesh: Mesh name
        :type mesh: str
        :return: Bbox info {'bbox', 'pMin', 'pMax', 'x', 'y', 'z', 'surfaceArea'}
        :rtype: dict """
    bbox = mc.exactWorldBoundingBox(mesh)
    return getInfoFromBbox(bbox)

def getInfoFromBbox(bbox):
    """ Get boundingBox info from bbox values
        :param bbox: BoundingBox values (Xmin, Ymin, Zmin, Xmax, Ymax, Zmax)
        :type bbox: list
        :return: Bbox info {'bbox', 'pMin', 'pMax', 'x', 'y', 'z', 'surfaceArea'}
        :rtype: dict """
    pMin = (bbox[0], bbox[1], bbox[2])
    pMax = (bbox[3], bbox[4], bbox[5])
    x = (bbox[3] - bbox[0])
    y = (bbox[4] - bbox[1])
    z = (bbox[5] - bbox[2])
    bboxSurfaceArea = (2 * ((x * y) + (x * z) + (y * z)))
    return {'bbox': bbox, 'pMin': pMin, 'pMax': pMax, 'x': x, 'y': y, 'z': z, 'surfaceArea': bboxSurfaceArea}
