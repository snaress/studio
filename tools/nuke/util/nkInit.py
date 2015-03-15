import os, sys
from lib.system import procFile as pFile

modPath = os.path.normpath(os.path.dirname(__file__))
nodePath = os.path.join(os.sep.join(modPath.split(os.sep)[:-1]), 'gizmo')
iconPath = os.path.join(nodePath, '_lib', 'icons')

print "########## INIT NUKE STUDIO ##########"
print "rnd node path: ", pFile.conformPath(nodePath)
print 'rnd icon path: ', pFile.conformPath(iconPath)


print "\n#-- INIT STUDIO ENV --#"
import nuke

#-- Plugin Path --#
print "Adding Nuke Plugin Path ..."
for cat in os.listdir(nodePath):
    catPath = pFile.conformPath(os.path.join(nodePath, cat))
    if os.path.isdir(catPath) and not cat.startswith('_') and not cat.startswith('.'):
        print "\t --> Add %s" %catPath
        nuke.pluginAddPath(catPath)

#-- Icon Path --#
print "Adding Nuke Icon Path ..."
print "\t --> Add %s" % pFile.conformPath(iconPath)
nuke.pluginAddPath(pFile.conformPath(iconPath))


print "\n#-- INIT STUDIO MENU --#"
menubar = nuke.menu("Nuke")
m = menubar.addMenu("Studio")


print "\n#-- INIT STUDIO TOOLBAR --#"
myToolbar = nuke.toolbar('Nodes')

#-- Add Menu --#
menuName = 'StudioTools'
print "Adding %r Menu ..." % menuName
myToolbar.addMenu(menuName, icon=os.path.join(iconPath, '%s.png' % menuName))

#-- Add Category --#
for cat in os.listdir(nodePath):
    catPath = pFile.conformPath(os.path.join(nodePath, cat))
    if os.path.isdir(catPath) and not cat.startswith('_') and not cat.startswith('.'):
        label = "%s%s" % (cat[0].upper(), cat[1:])
        print "\t Adding %r Category ..." % label
        catName = "%s/%s" % (menuName, label)
        myToolbar.addMenu(catName, icon='%s.png' % label)
        #-- Add Nodes --#
        for gizmo in os.listdir(catPath):
            gizmoFile = pFile.conformPath(os.path.join(catPath, gizmo))
            if gizmo.endswith('.gizmo') and not gizmo.startswith('_') and not gizmo.startswith('.'):
                gName = os.path.splitext(gizmo)[0]
                label = "%s%s" % (gName[0].upper(), gName[1:])
                print "\t\t --> %s" % label
                gizmoName = "%s/%s" % (catName, label)
                ima = os.path.join(iconPath, '%s.png' % gName)
                if not os.path.exists(ima):
                    myToolbar.addCommand(gizmoName, "nuke.createNode(%r)" % gName)
                else:
                    myToolbar.addCommand(gizmoName, "nuke.createNode(%r)" % gName, icon='%s.png' % gName)


print "\n########## !!! INIT NUKE STUDIO COMPLETE !!! ##########"