try:
    import maya.cmds as mc
except:
    pass


def getShadingEngine(model):
    """ Get shading engine from given mesh
        :param model: Transform name or mesh name
        :type model: str
        :return: Shading engine
        :rtype: str """
    if mc.objectType(model, isType='transform'):
        sets = mc.listSets(type=1, o=model, ets=True)
    elif mc.objectType(model, isType='mesh'):
        sets = mc.listSets(type=1, o=model, ets=False)
    else:
        sets = []
    if not sets:
        print "!!! Error: Shading engine not found."
    else:
        return sets

def getMatFromSg(sg):
    """ Get material from given shading engine
        :param sg: Shading engine
        :type sg: str
        :return: Connected materials
        :rtype: dict """
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
    #-- Mental Ray Shader --#
    connections = mc.listConnections(sg, s=True, d=True, c=True, p=True)
    for n in range(0, len(connections), 2):
        if connections[n].split('.')[-1].startswith('mi'):
            matDict[connections[n].split('.')[-1]] = connections[n+1].split('.')[0]
    return matDict

