try:
    import maya.cmds as mc
except:
    pass


def getShadingEngine(model):
    """ Get shading engine from given mesh
        :param model: (str) : Transform name or mesh name
        :return: (str) : Shading engine """
    if mc.objectType(model, isType='transform'):
        shapes = mc.listRelatives(model, s=True, ni=True)
    elif mc.objectType(model, isType='mesh'):
        shapes = [model]
    else:
        shapes = []
    if not shapes:
        print "Error: Shape not found."
    else:
        shapeName = shapes[0]
        connections = mc.listConnections(shapeName, s=True, d=True, c=True)
        for n, connect in enumerate(connections):
            if connect == "%s.instObjGroups" % shapeName:
                sg = connections[n+1]
                if mc.objectType(sg, isType='shadingEngine'):
                    return sg

def getMatFromSg(sg):
    """ Get material from given shading engine
        :param sg: (str) : Shading engine
        :return: (dict) : Connected materials """
    matDict = {'ss': None, 'ds': None, 'vs': None}
    #-- Surface shader --#
    connections = mc.listConnections('%s.surfaceShader' % sg, s=True)
    if connections:
        matDict['ss'] = connections[0]
    #-- Displace shader --#
    connections = mc.listConnections('%s.displacementShader' % sg, s=True)
    if connections:
        matDict['ds'] = connections[0]
    #-- Volume Shader --#
    connections = mc.listConnections('%s.volumeShader' % sg, s=True)
    if connections:
        matDict['vs'] = connections[0]
    return matDict
