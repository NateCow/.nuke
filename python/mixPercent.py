#===============================================================================
# mixPercent.py
# Version: 1.0.1
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
# 1.0.1 Limits this functionality to Grades, ColorCorrects, and Merges.
#
#===============================================================================

import nuke

def mixPercent():

    newNode = nuke.thisNode()

    if newNode.Class() == "Merge2" or newNode.Class() == "Grade" or newNode.Class() == "ColorCorrect":
    
        newNode.knob('label').setValue("[ expr { [value mix] * 100 } ]%")


nuke.addOnCreate(mixPercent)