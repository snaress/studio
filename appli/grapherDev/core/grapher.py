import os
from lib.system import procFile as pFile


def createProjectFolder(projectsRootPath, prodsRootPath, projectAlias, projectName):
    """
    Create project folder
    :param projectsRootPath: Grapher projects root path
    :type projectsRootPath: str
    :param prodsRootPath: Prods root path
    :type prodsRootPath: str
    :param projectAlias: Project alias
    :type projectAlias: str
    :param projectName: Project Name
    :type projectName: str
    """
    projectFolder = "%s--%s" % (projectAlias, projectName)
    graphProjectPath = os.path.join(projectsRootPath, projectFolder)
    prodProjectPath = os.path.join(prodsRootPath, projectFolder)
    if os.path.exists(graphProjectPath) or os.path.exists(prodProjectPath):
        raise IOError, "!!! Project folder '%s' already exists !!!" % projectFolder
    try:
        os.mkdir(graphProjectPath)
        os.mkdir(os.path.join(graphProjectPath, 'bank'))
        os.mkdir(os.path.join(graphProjectPath, 'graph'))
        os.mkdir(os.path.join(graphProjectPath, 'graph', 'assets'))
        os.mkdir(os.path.join(graphProjectPath, 'graph', 'shots'))
        os.mkdir(os.path.join(graphProjectPath, 'template'))
        os.mkdir(os.path.join(graphProjectPath, 'template', 'assets'))
        os.mkdir(os.path.join(graphProjectPath, 'template', 'shots'))
    except:
        raise IOError, "!!! Can not create project folder '%s' in '/grapher' !!!" % projectFolder
    try:
        os.mkdir(prodProjectPath)
        os.mkdir(os.path.join(prodProjectPath, 'assets'))
        os.mkdir(os.path.join(prodProjectPath, 'shots'))
    except:
        raise IOError, "!!! Can not create project folder '%s' in '/prods' !!!" % projectFolder

def getGrapherProjects(graphRootPath):
    """
    Get grapher projects
    :param graphRootPath: Grapher projects root path
    :type graphRootPath: str
    :return: Grapher projects list (list of dict)
    :rtype: list
    """
    pList = []
    for project in os.listdir(graphRootPath):
        if os.path.isdir(os.path.join(graphRootPath, project)) and '--' in project:
            pList.append({'alias': project.split('--')[0], 'name': project.split('--')[1]})
    return pList

def createGrapherFolder(folderPath, category):
    """
    Create grapher folder
    :param folderPath: New folder path
    :type folderPath: str
    :param category: Category name
    :type category: str
    """
    if os.path.exists(folderPath):
        raise IOError, "!!! Grapher '%s' folder '%s' already exists !!! " % (category, folderPath)
    try:
        os.mkdir(folderPath)
    except:
        raise IOError, "!!! Can not create grapher '%s' folder '%s' !!!" % (category, folderPath)

def createGrapherAsset(assetPath, assetData):
    """
    Create grapher asset
    :param assetPath: New asset path
    :type assetPath: str
    :param assetData: New asset data
    :type assetData: dict
    """
    createGrapherFolder(assetPath, 'New Asset')
    #-- Create asset casting file --#
    cstFile = "%s.cst.py" % assetData['assetName']
    cstFilePath = os.path.join(assetPath, cstFile)
    datas = []
    for k, v in assetData.iteritems():
        if isinstance(v, str):
            datas.append("%s = %r" % (k, v))
        else:
            datas.append("%s = %s" % (k, v))
    try:
        pFile.writeFile(cstFilePath, '\n'.join(datas))
    except:
        raise IOError, "!!! Can not write asset casting file '%s' !!!" % cstFile

def getProjectStructure(projectRootPath):
    """
    Get grapher project structure
    :param projectRootPath: Graph project root path
    :type projectRootPath: str
    :return: Project structure
    :rtype: list
    """
    treeDicts = []
    for tree in os.listdir(projectRootPath):
        treeDicts.append(pFile.pathToDict(os.path.join(projectRootPath, tree)))
    structure = []
    for tree in treeDicts:
        for path in tree['_order']:
            structure.append(pFile.conformPath(path.replace('%s%s' % (projectRootPath, os.sep), '')))
    return structure

def getProjectTree(projectRootPath):
    """
    Get grapher project tree contents
    :param projectRootPath: Graph project root path
    :type projectRootPath: str
    :return: Project tree
    :rtype: dict
    """
    return pFile.pathToDict(projectRootPath)

def createUser(usersRootPath, userName):
    """
    Create new user folders in Grapher data base
    :param usersRootPath: Users root path
    :type usersRootPath: str
    :param userName: New user name
    :type userName: str
    """
    if not os.path.exists(usersRootPath):
        raise IOError, "!!! Users RootPath doesn't exists: %s !!!" % usersRootPath
    userPath = os.path.join(usersRootPath, userName)
    if os.path.exists(userPath):
        raise IOError, "!!! User already exists: %s !!!" % userName
    try:
        os.mkdir(userPath)
        os.mkdir(os.path.join(userPath, 'scripts'))
        os.mkdir(os.path.join(userPath, 'tmp'))
        os.mkdir(os.path.join(userPath, 'tmp', 'externData'))
    except:
        raise IOError, "!!! Can not create user folders !!!"

def getAllUsers(usersRootPath):
    """
    Get all users in Grapher data base
    :param usersRootPath: Users root path
    :type usersRootPath: str
    :return: User list
    :rtype: list
    """
    if not os.path.exists(usersRootPath):
        raise IOError, "!!! Users RootPath doesn't exists: %s !!!" % usersRootPath
    users = []
    for fld in os.listdir(usersRootPath):
        userPath = os.path.join(usersRootPath, fld)
        if os.path.isdir(userPath) and not fld.startswith('_'):
            users.append(fld)
    return users

def createExternPath(externRootPath, projectFullName):
    """
    Create extern tmp path for externalized data
    :param externRootPath: Extern tmp root path
    :type externRootPath: str
    :param projectFullName: Current project full name
    :type projectFullName: str
    :return: Extern path
    :rtype: str
    """
    if not os.path.exists(externRootPath):
        raise IOError, "!!! Extern root path doesn't exists: %s !!!" % externRootPath
    externPath = os.path.join(externRootPath, projectFullName)
    if not os.path.exists(externPath):
        try:
            os.mkdir(externPath)
        except:
            raise IOError, "!!! Can not create extern path !!!"
    return externPath
