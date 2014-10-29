import os, sys, optparse


#-- Options --#
usage = "userManager -v [Verbose Index]"
parser = optparse.OptionParser(usage=usage)
parser.add_option('-v', '--verbose', type='choice', default='info',
                  choices=['critical', 'error', 'warning', 'info', 'debug'],
                  help=''.join(["[choice=('critical', 'error', 'warning', 'info', 'debug')] ",
                                "Log level (default='info')"]))


if __name__ == '__main__':
    #-- Package Var --#
    toolPath = os.path.normpath(os.path.dirname(__file__))
    toolName = toolPath.split(os.sep)[-1]
    toolPack = __package__

    #-- SysPath --#
    wsPath = os.sep.join(toolPath.split(os.sep)[:-2])
    if not wsPath in sys.path:
        print "[sys] | Info | Add %s to sysPath" % wsPath
        sys.path.insert(0, wsPath)

    options, args = parser.parse_args()
    options = eval(str(options))

    from appli.userManager import userManagerUi
    userManagerUi.launch(logLvl=options['verbose'])