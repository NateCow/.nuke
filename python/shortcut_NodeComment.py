#===============================================================================
# shortcut_NodeComment.py
# Version: 1.0.0
# Last Updated: May 16, 2020
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# USAGE:
#
# Adds meta+c shorcut to create a node's label, so you don't
# waste valuable clicks opening a node and switching to the Node label.
# i.e: for lazy people.
#===============================================================================

import nuke

def shortcut_NodeComment():

	selectedNode = nuke.selectedNode()
	oldComment = selectedNode['label'].value()

	inputBox = nuke.getInput("Please enter a node label", oldComment)

	# Determin if Cancel button was pressed
	if inputBox == None:
		# Remain as Galadriel
		selectedNode['label'].setValue(oldComment)
		# Otherwise update node label
	else:
		selectedNode['label'].setValue(inputBox)


# Add menu items
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Add Comment to Node', 'shortcut_NodeComment.shortcut_NodeComment()', 'ctrl+alt+c')