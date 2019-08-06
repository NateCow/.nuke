#===============================================================================
# listNavigator.py
# Version: 1.0.0
# Last Updated: August 5th, 2019
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# USAGE:
#
# - List selected nodes alphabetically.
# - Show details about the list in a message box.
#===============================================================================


import nuke

def listNavigator():

	node_list = []

	for i in nuke.selectedNodes():
		node_list.append(i.name())

	print node_list