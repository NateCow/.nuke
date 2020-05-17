#===============================================================================
# shortcut_NodeCustomizer.py
# Version: 1.0.1
# Last Updated: May 16, 2020
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# USAGE:
#
# Adds a shortcut to change the node label,
# easily add the value of a knob to the label,
# and the color of the node.
#===============================================================================

import nuke

def shortcut_NodeCustomizer():

    # Set variables & list to hold information we'll need...
    selectedNode = nuke.selectedNode()
    oldComment = selectedNode['label'].value()
    knobList = []

    # Get a list of all the knobs in the selected Node
    for i in selectedNode.knobs():
        knobList.append(i)

    knobList.sort()
    knobList.insert(0, 'None')

    knobList_string = " ".join(knobList)

    # Create a panel
    panel = nuke.Panel("Node Customizer")

    # Add knobs
    panel.addSingleLineInput("Comment", oldComment)
    panel.addEnumerationPulldown("Knob", knobList_string)
    panel.addBooleanCheckBox("Change Node Color?", False)


    # If the cancel button is pressed, do nothing.
    if not panel.show():
        return

    # Assign the value of all our panel's knobs to variables to use later...
    comment_input = panel.value("Comment")
    knob_choice = panel.value("Knob")
    node_label = comment_input + "\n" + knob_choice+": [value "+knob_choice+"]"

    # Change values on our selected node from user choice

    # If the user doesn't enter any data or change anything, pop open a message and exit the window.
    if comment_input == "" and panel.value("Knob") == "None":
        if panel.value("Change Node Colour?") == False:
            nuke.message("Please enter a node label")

    # If a label is typed but no knob value selected, set the selected node's label to the comment_input.
    elif knob_choice == "None":
        selectedNode['label'].setValue(comment_input)

    # If If no label is typed but a knob value is selected, set the selected node's label to display the knob's value
    elif comment_input == "":
        selectedNode['label'].setValue(knob_choice+": [value "+knob_choice+"]")

    # Otherwise if none of these conditions are met, set the selected node's label to
    # display both the comment_input and knob_choice (this is our node_label variable)
    else:
        selectedNode['label'].setValue(node_label)

    # Check if the checkbox to change the color is checked. If yes, pop open a color picker window.
    if panel.value("Change Node Color?") == True:
        selectedNode['tile_color'].setValue(nuke.getColor())
    else:
        return

nuke.menu('Nuke').addCommand('Utilities/Node Customizer', 'shortcut_NodeCustomizer.shortcut_NodeCustomizer()', 'ctrl+alt+c')