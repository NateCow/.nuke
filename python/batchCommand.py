#===============================================================================
# batchCommand.py
# Version: 1.1.0
# Last Updated: February 24, 2021
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

    if nuke.selectedNode()['use_limit'].value() == 1:
        frameFirst = str(int(nuke.selectedNode()['first'].value()))
        frameLast = str(int(nuke.selectedNode()['last'].value()))
    else:
        frameFirst = str(int(nuke.root()['first_frame'].value()))
        frameLast = str(int(nuke.root()['last_frame'].value()))


    selectedWrite = nuke.selectedNode().name()

    batchCommand = 'start Nuke10.0.exe -i -X '+selectedWrite+' -F '+frameFirst+'-'+frameLast+' \"'+scriptPath+'\"'

    pyperclip.copy(batchCommand)

nuke.menu('Nuke').addCommand('Render/Copy Batch Command', 'batchCommand.getBatchCommand()', 'F9', shortcutContext=2)