#===============================================================================
# Copy and paste this stuff into your menu.py file in your .nuke directory.
#===============================================================================

# -- This is probably already in your menu.py
import nuke


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

cowMenu.addCommand("Read This", lambda: readFromWrite(), 'alt+r', shortcutContext=2)
cowMenu.addCommand("Start Frame 1001", lambda: setStartFrame())
cowMenu.addCommand("Set sRGB", lambda: setsRGB())
cowMenu.addCommand("Set Project Settings", lambda: setProject())




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
# -- This assumes a 1001-based timeline. Could easily change the 1001 values below to however you want.

def setProject():

    node = nuke.selectedNode()
    frameStart = int(node.knob('first').getValue())
    frameEnd = int(node.knob('last').getValue())
    nodeFormat = node.format()

    nuke.root()['first_frame'].setValue(1001)
    nuke.root()['last_frame'].setValue(frameEnd - frameStart + 1001)
    nuke.root()['format'].setValue(nodeFormat.name())



# -- After feable attempts, readFromWrite found here: http://nullege.com/codes/show/src@v@f@vfxpipe-HEAD@nuke@fxpipenukescripts@readFromWrite.py/19/nuke.nodes.Read
# -- This allows you to select a write node and hit Alt + R to read it back in.

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

# -- V key creates a Shuffle node, something I've grown used to at Zoic and DD.
nuke.menu('Nodes').addCommand("Channel/Shuffle", "nuke.createNode('Shuffle')", "v", icon="Shuffle.png", shortcutContext=2)




