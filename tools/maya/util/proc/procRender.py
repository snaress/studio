try:
    import maya.cmds as mc
except:
    pass


def initMrDefaultNodes():
    """ Create mentalRay default nodes """
    print "Init Mentalray default nodes ..."
    mrNodes = {'mentalrayGlobals': 'mentalrayGlobals', 'mentalrayItemsList': 'mentalrayItemsList',
               'mentalrayOptions': 'miDefaultOptions', 'mentalrayFramebuffer': 'miDefaultFramebuffer'}
    #-- Create mrNodes --#
    create = False
    for mrNode in mrNodes.keys():
        if not mc.objExists(mrNode):
            print "\tCreate mrNode %s named %s" % (mrNode, mrNodes[mrNode])
            mc.createNode(mrNode, n=mrNodes[mrNode])
            create = True
    #-- Link mrNodes --#
    if create:
        conns = {'mentalrayGlobals.options': 'miDefaultOptions.message',
                 'mentalrayItemsList.options[0]': 'miDefaultOptions.message',
                 'mentalrayGlobals.framebuffer': 'miDefaultFramebuffer.message',
                 'mentalrayItemsList.framebuffers[0]': 'miDefaultFramebuffer.message',
                 'mentalrayItemsList.globals': 'mentalrayGlobals.message'}
        for dst, src in conns.iteritems():
            try:
                mc.connectAttr(src, dst)
                print "\tConnect %s to %s" % (src, dst)
            except:
                print "\tSkip connection %s to %s" % (src, dst)
