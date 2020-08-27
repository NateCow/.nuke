#===============================================================================
# batchCommand.py
# Version: 1.0.0
# Last Updated: August 3, 2020
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
    frameFirst = str(int(nuke.root()['first_frame'].value()))
    frameLast = str(int(nuke.root()['last_frame'].value()))
    selectedWrite = nuke.selectedNode().name()

    batchCommand = 'start Nuke10.0.exe -i -X '+selectedWrite+' -F '+frameFirst+'-'+frameLast+' \"'+scriptPath+'\"'

    pyperclip.copy(batchCommand)

nuke.menu('Nuke').addCommand('Render/Copy Batch Command', 'batchCommand.getBatchCommand()', 'F9', shortcutContext=2)