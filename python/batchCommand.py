#===============================================================================
# batchCommand.py
# Version: 1.1.1
# Last Updated: June 23, 2024
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# USAGE:
#
# - Copy the necessary command to paste into a batch file for command line rendering.
#===============================================================================

import nuke
import pyperclip

def getBatchCommand():

    scriptPath = nuke.root().name()

    renderPath = nuke.selectedNode()['file'].value()
    renderTitle = renderPath.split('/')[-1].split('.')[0] # Grabs last piece of filepath which is the filename [-1], then lops off the frame padding and file extention, leaving just the render name [0]

    if nuke.selectedNode()['use_limit'].value() == 1:
        frameFirst = str(int(nuke.selectedNode()['first'].value()))
        frameLast = str(int(nuke.selectedNode()['last'].value()))
    else:
        frameFirst = str(int(nuke.root()['first_frame'].value()))
        frameLast = str(int(nuke.root()['last_frame'].value()))


    selectedWrite = nuke.selectedNode().name()

    batchCommand = 'start "' + renderTitle + '" Nuke10.0.exe -i -X '+selectedWrite+' -F '+frameFirst+'-'+frameLast+' \"'+scriptPath+'\"'

    pyperclip.copy(batchCommand)

nuke.menu('Nuke').addCommand('Render/Copy Batch Command', 'batchCommand.getBatchCommand()', 'F9', shortcutContext=2)