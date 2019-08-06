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

	node_list.sort()

	# Print all nodes in list
	print "NODES IN LIST:\n"

	for i in node_list:
		print "- "+i

	nuke.message("There are "+str(len(node_list))+" nodes in the list.")