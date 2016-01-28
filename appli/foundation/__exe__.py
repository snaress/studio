import optparse


usage = "foundation -p [Project] -v [LogLevel]"
parser = optparse.OptionParser(usage=usage)
parser.add_option('-p', '--project', type='string', help="Load given project (projectName--projectCode)")
parser.add_option('-v', '--logLvl', type='choice', default='info',
                  choices=['critical', 'error', 'warning', 'info', 'debug', 'detail'],
                  help=' '.join(["['critical','error','warning','info','debug','detail']",
                                 "Log level (default: 'info')"]))


if __name__ == '__main__':
    options, args = parser.parse_args()
    options = eval(str(options))

    from appli.foundation.gui.foundation import foundationUi
    foundationUi.launch(**options)
