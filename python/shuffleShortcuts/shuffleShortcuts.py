#===============================================================================
# shuffleShortcuts.py
# Version: 0.2.1
# Last Updated: August 4th, 2019
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

import nuke

def createCustomShuffle(in_channel, out_channel, set_channel, rColor, gColor, bColor):

    # Create a new shuffle node, and assign it to a variable so we can change some things...
    myShuffle = nuke.createNode('Shuffle')

    # Change the input & output channels to what is defined in the in_channel and out_channel arguments.
    myShuffle['in'].setValue(in_channel)
    myShuffle['out'].setValue(out_channel)

    # Change the relevant knobs to shuffle the RGBA channels to the green channel.
    myShuffle['red'].setValue(set_channel)
    myShuffle['green'].setValue(set_channel)
    myShuffle['blue'].setValue(set_channel)
    myShuffle['alpha'].setValue(set_channel)
    
    # Change the node color to green (converting Nuke's hex color values to RGB to be a bit more human-readable)
    myShuffle['tile_color'].setValue(int('%02x%02x%02x%02x' % (rColor*255,gColor*255,bColor*255,1), 16))
    
    # Add a node label
    myShuffle['label'].setValue("[value red] > [value out]")



def shuffleRGBchannels():

    selectedNode = nuke.selectedNode()
    selectedNode_xPos = selectedNode['xpos'].value()
    selectedNode_yPos = selectedNode['ypos'].value()

    createCustomShuffle('rgba', 'rgba', 'red', 1, 0, 0)
    redShuffle = nuke.selectedNode()
    createCustomShuffle('rgba', 'rgba', 'green', 0, 1, 0)
    greenShuffle = nuke.selectedNode()
    createCustomShuffle('rgba', 'rgba', 'blue', 0, 0, 1)
    blueShuffle = nuke.selectedNode()

    redShuffle.setInput(0, selectedNode)
    redShuffle['xpos'].setValue(selectedNode_xPos-150)
    redShuffle['ypos'].setValue(selectedNode_yPos+150)

    greenShuffle.setInput(0, selectedNode)
    greenShuffle['xpos'].setValue(selectedNode_xPos)
    greenShuffle['ypos'].setValue(selectedNode_yPos+150)

    blueShuffle.setInput(0, selectedNode)
    blueShuffle['xpos'].setValue(selectedNode_xPos+150)
    blueShuffle['ypos'].setValue(selectedNode_yPos+150)


# Add menu
nuke.menu('Nodes').addCommand("Channel/Shuffle (Red to All)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'red', 1, 0, 0)", "ctrl+shift+r", icon="redShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Green to All)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'green', 0, 1, 0)", "ctrl+shift+g", icon="greenShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Blue to All)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'blue', 0, 0, 1)", "ctrl+shift+b", icon="blueShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to All)", "shuffleShortcuts.createCustomShuffle('alpha', 'rgba', 'alpha', 1, 1, 1)", "ctrl+shift+a", icon="alphaToAll.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to 0)", "shuffleShortcuts.createCustomShuffle('alpha', 'alpha', 'black', 0, 0, 0)", "ctrl+shift+`", icon="alpha0Shuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to 1)", "shuffleShortcuts.createCustomShuffle('alpha', 'alpha', 'white', 1, 1, 1)", "ctrl+shift+1", icon="alpha1Shuffle.png", shortcutContext=2)

nuke.menu('Nodes').addCommand("Channel/Shuffle (Split RGB channels)", "shuffleShortcuts.shuffleRGBchannels()", "ctrl+shift+s", icon="ShuffleSplitRGB.png", shortcutContext=2)