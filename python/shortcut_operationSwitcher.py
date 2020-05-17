#===============================================================================
# shortcut_operationSwitcher.py
# Version: 1.0.0
# Last Updated: May 16, 2020
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# USAGE:
#
# Ctrl+Shift+S toggles between over/under, mask/stencil, plus/from, etc.
#===============================================================================

import nuke

def shortcut_operationSwitcher():
    
    try:
        node = nuke.selectedNode()
    except:
        nuke.createNode('Invert')
        return

    merge_ops = {'over':'under', 'mask':'stencil', 'plus':'from', 'multiply':'divide', 'max':'min', 'conjoint-over':'disjoint-over', 'log2lin':'lin2log'}


    if node.Class() == "Merge2" or node.Class() == "Log2Lin":

        current_op = node['operation'].value()

        if current_op in merge_ops.keys():

            node['operation'].setValue(merge_ops[node['operation'].value()]) 

        elif current_op in merge_ops.values():

            node['operation'].setValue(merge_ops.keys()[merge_ops.values().index(current_op)])



nuke.menu('Nuke').addCommand('Edit/Shortcuts/Swap Operation', 'shortcut_operationSwitcher.shortcut_operationSwitcher()', 'ctrl+shift+s')    