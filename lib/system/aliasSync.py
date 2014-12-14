import os, shutil
toolPath = os.path.normpath(os.path.dirname(__file__))


def syncAlias():
    """ Copy alias file from bank to user path """
    aliasFile = os.path.normpath(os.path.join(toolPath, 'alias.txt'))
    user = os.environ.get('username')
    userFile = os.path.join('C:', os.sep, 'Users', user, 'alias.txt')
    if not os.path.exists(os.path.dirname(userFile)):
        raise IOError, "!!! User path not found !!!"
    else:
        print "\n#-- Alias Synch --#"
        print "Copy %s to %s" % (aliasFile, userFile)
        try:
            shutil.copy(aliasFile, userFile)
        except:
            raise IOError, "!!! Can not copy %s !!!" % aliasFile


if __name__ == '__main__':
    syncAlias()