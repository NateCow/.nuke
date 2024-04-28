#===============================================================================
# menu.py
# Version: 1.1.8
# Last Updated: July 19, 2020
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

import nuke
import platform
import errorReport
import nukescripts

Win_Dir = 'C:\Users\NateCow\.nuke'
MacOSX_Dir = ''
Linux_Dir = '/home/natecow/.nuke'

# Set global directory
if platform.system() == "Windows":
    dir = Win_Dir
elif platform.system() == "Darwin":
    dir = MacOSX_Dir
elif platform.system() == "Linux":
    dir = Linux_Dir
else:
    dir = None

#===============================================================================
# Knob Defaults
#===============================================================================

# -- Motion blur shutter. Perfectly balanced, as all things should be. ---------
nuke.knobDefault('shutteroffset', "centered")

# -- FRAMEHOLD DEFAULT - Sets frameHold nodes to whatever frame you're on. -----
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')



#===============================================================================
# Custom Menus
#===============================================================================

cowMenu = nuke.menu('Nuke').addMenu('Cow')
utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')

utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')

cowMenu.addCommand("Read This", lambda: readFromWrite(), 'alt+r', shortcutContext=2)
cowMenu.addCommand("Start Frame 1001", lambda: setStartFrame())
cowMenu.addCommand("Set sRGB", lambda: setsRGB())
cowMenu.addCommand("Set Project Settings", lambda: setProject())


myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon=dir+"myGizmoes_icon.png")

myGizmosMenu.addCommand('Autocrop', 'nukescripts.autocrop()')
myGizmosMenu.addCommand('bm_GrainTransfer', 'nuke.createNode("bm_GrainTransfer")', icon="Grain.png")
myGizmosMenu.addCommand('AdvancedGrain', 'nuke.createNode("AdvancedGrain")', icon="Grain.png")
myGizmosMenu.addCommand('EdgeExtend', 'nuke.createNode("EdgeExtend2")')

m = nuke.menu('Nodes')
m.addCommand( '*HM* toolbox/Draw/GrainMaster' , "nuke.nodes.GrainMaster()" , 'shift+g' )
m.addCommand( '*HM* toolbox/3D/Parent Constraint' , "nuke.nodes.ParentConstraint()")




#===============================================================================
# Cow Functions
#===============================================================================

# -- Sets read node to start at 1001. ------------------------------------------

def setStartFrame():

    nodes = nuke.selectedNodes()
    for n in nodes:
        n.knob('frame_mode').setValue("start at")
        n.knob('frame').setValue('1001')



# -- Sets colorspace of read node. Currently it just sets it to sRGB. Need to update.

def setsRGB():

    nodes = nuke.selectedNodes()
    for n in nodes:
        n.knob('colorspace').setValue("sRGB") #For now, you could change "sRGB" to whatever you need it to be.



# -- Sets the frame range based on the currently selected read node.
# -- This assumes a 1001-based timeline.

def setProject():

    node = nuke.selectedNode()
    frameStart = int(node.knob('first').getValue())
    frameEnd = int(node.knob('last').getValue())
    nodeFormat = node.format()

    nuke.root()['first_frame'].setValue(1001)
    nuke.root()['last_frame'].setValue(frameEnd - frameStart + 1001)
    nuke.root()['format'].setValue(nodeFormat.name())



# -- After feable attempts, readFromWrite found here:
# -- http://nullege.com/codes/show/src@v@f@vfxpipe-HEAD@nuke@fxpipenukescripts@readFromWrite.py/19/nuke.nodes.Read

def readFromWrite():
  
    nodes = nuke.selectedNodes()
    if len(nodes) < 1:
        print('No nodes selected')
    else :
        foundWrites = False
        writeNodes = []
        for node in nodes:
            if node.Class() == 'Write':
                writeNodes.append(node)
                foundWrites = True
  
        if foundWrites == True:  # we found some writes
  
            for node in writeNodes:
                nodeRead = nuke.nodes.Read() # create a read node
                nodeRead['file'].setValue(nuke.filename(node)) #set the filename
                if node['use_limit'].getValue() == 1: #check to see if there is a range and set the values in the read node
                    nodeRead['first'].setValue(int(node['first'].getValue()))
                    nodeRead['last'].setValue(int(node['last'].getValue()))
                else: # no range on the write?  take a stab at using the range from the script value
                    nodeRead['first'].setValue(int(nuke.root()['first_frame'].getValue()))
                    nodeRead['last'].setValue(int(nuke.root()['last_frame'].getValue()))       
                nodeRead.setXpos(node.xpos()) #let's set the position 
                nodeRead.setYpos(node.ypos()+50)
                nodeRead['premultiplied'].setValue(node['premultiplied'].getValue()) # use premult if checked
                nodeRead['raw'].setValue(node['raw'].getValue()) # use raw if checked
        else:
  
            print('No Writes Found in Node Selection')




#===============================================================================
# Keyboard Shortcuts
#===============================================================================

nuke.menu('Nodes').addCommand("Channel/Shuffle", "nuke.createNode('Shuffle')", "v", icon="Shuffle.png", shortcutContext=2)


# -------- Merge Node Shortcuts-------------------------------------------------
mergeMenu = nuke.menu('Nodes').findItem("Merge/Merges")

mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B")', "alt+o", icon="MergeOut.png", shortcutContext=2)
mergeMenu.addCommand('Mask', 'nuke.createNode("Merge2", "operation mask bbox A")', "alt+i", icon="MergeIn.png", shortcutContext=2)
mergeMenu.addCommand('Plus', 'nuke.createNode("Merge2", "operation plus")', "alt+]", icon="MergePlus.png", shortcutContext=2)
mergeMenu.addCommand('From', 'nuke.createNode("Merge2", "operation from")', "alt+[", icon="MergeDifference.png", shortcutContext=2)


# --------------------------------------------------------------
#  PYTHON SCRIPTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------


import shuffleShortcuts
import listNavigator
import filepathLister
import paste_selected
# import shortcut_NodeComment
import shortcut_NodeCustomizer
import shortcut_operationSwitcher
import moblur_controller
import mixPercent
import batchCommand
import cowOnLoad



#===============================================================================
# Error Report Tool, for finding bad frames and such.
#===============================================================================

nuke.menu("Nuke").addCommand('Scripts/errorReport', 'errorReport.runErrorReport()', 'alt+d')


#===============================================================================
# Optical Flares
#===============================================================================

toolbar = nuke.toolbar("Nodes")
toolbar.addMenu("VideoCopilot", icon="VideoCopilot.png")
toolbar.addCommand( "VideoCopilot/OpticalFlares", "nuke.createNode('OpticalFlares')", icon="OpticalFlares.png")


#===============================================================================
# BVFX ToolBar Menu definitions
#===============================================================================

toolbar = nuke.menu("Nodes")
bvfxt = toolbar.addMenu("BoundaryVFX Tools", "BoundaryVFX.png")
bvfxt.addCommand('Rotopaint to SplineWarp Nukev7', 'Roto_to_WarpSpline_v2()', icon='bvfx_SplineW.png')

toolbar = nuke.menu("Nodes")
bvfxt = toolbar.addMenu("BoundaryVFX Tools", "BoundaryVFX.png")
bvfxt.addCommand('FreezeWarp for Nukev7', 'freezeWarp_v2()','shift+F8', icon='bvfx_SplineF.png')



#===============================================================================
# Other Stuffs
#===============================================================================

import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte_ui()
#>>>PrismStart
'''
import nuke
if not nuke.env["studio"]:
	import sys, os

	Dir = os.path.join("C:/Prism", "Scripts")
	if Dir not in sys.path:
		sys.path.append(Dir)

	import PrismCore
	pcore = PrismCore.PrismCore(app="Nuke")
'''



