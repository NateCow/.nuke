#===============================================================================
# mixPercent.py
# Version: 1.0.0
# Last Updated: June 29, 2020
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# USAGE:
#
# Checks if the node has a mix value and
# sets the label to display it as a percentage.
#
#===============================================================================

import nuke

def mixPercent():

    newNode = nuke.thisNode()

    if newNode.knob('mix'):
    
        newNode.knob('label').setValue("[ expr { [value mix] * 100 } ]%")


nuke.addOnCreate(mixPercent)