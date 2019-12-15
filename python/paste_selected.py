#===============================================================================
# paste_selected.py
# Version: 1.0.0
# Last Updated: August 6th, 2019
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# USAGE:
#
# - Pastes previous-copied node to all the selected nodes.
#===============================================================================

import nuke

def paste_selected():

	for i in nuke.selectedNodes():
		i.setSelected(True)
		nuke.nodePaste("%clipboard%")


editMenu = nuke.menu('Nuke').findItem("Edit")
editMenu.addCommand('Pasted Selected', 'paste_selected.paste_selected()', "ctrl+shift+v", shortcutContext=2)