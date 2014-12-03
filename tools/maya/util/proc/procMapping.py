try:
    import maya.cmds as mc
except:
    pass


def getShadingEngine(model):
    """ Get shading engine from given mesh
        :param model: (str) : Transform name or mesh name
        :return: (str) : Shading engine """
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
