import optparse


#-- Options --#
usage = "fondation -p [Project] -v [Verbose]"
parser = optparse.OptionParser(usage=usage)
parser.add_option('-p', '--project', type='string', help="[str] Load given project.")
parser.add_option('-v', '--verbose', type='choice', default='info',
                  choices=['critical', 'error', 'warning', 'info', 'debug', 'detail'],
                  help=''.join(["[choice=('critical', 'error', 'warning', 'info', 'debug', 'detail')]",
                                "Log level (default: 'info')"]))


if __name__ == '__main__':
    options, args = parser.parse_args()
    options = eval(str(options))

    from appli.grapher import grapherUi
    grapherUi.launch(logLvl=options['verbose'])
