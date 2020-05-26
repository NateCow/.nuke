for i in nuke.selectedNodes():

    if i.name() in node_list:
        print i.name()+" is already in the list."

    else:
        node_list.append(i.name())

print node_list



# Turn the list into a single string, and add
# a line break, a bullet point, and a space in between each item.
node_list_cleaned = '\n• '.join(node_list)

# Set the value of the text knob.
nuke.thisNode()['txtknob_node_list'].setValue("• "+node_list_cleaned)


def disableNodesInList():

    for i in node_list:

        if nuke.toNode(i).knob('disable'):

            nuke.toNode(i).knob('disable').setValue(nuke.thisNode().knob('disable').value())

        else:
            print " - "+i+" does not have a 'disable' knob. Ignoring..."



nuke.toNode('COW_NODE_DISABLER').knob('knobChanged').setValue('disableNodesInList()')