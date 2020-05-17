#===============================================================================
# moblur_controller.py
# Version: 1.0.0
# Last Updated: May 16, 2020
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# USAGE:
#
# Creates a NoOp node which allows the user to control
# motionblur on all nodes globally.
#
# Need to make a manual link button. Not liking the auto-linking of
# all transform nodes and the like.
#===============================================================================

import nuke

def moblur_controller():

    # Check if the Nuke script already has a GLOBAL_MOTIONBLUR_CONTROLLER NoOp node.
    for x in nuke.allNodes('NoOp'):
        if x.name() == "GLOBAL_MOTIONBLUR_CONTROLLER":
            nuke.message("You already have one of those in your script!")
            return

    node_list = []

    # Loop through all nodes, and the ones that have a motionblur or samples knob, add them to node_list.
    for n in nuke.allNodes():
        if n.knob('motionblur') or n.knob('samples'):
            node_list.append(n)
    
    # Create a NoOp node and make it pretty
    NoOp = nuke.createNode('NoOp')
    NoOp['name'].setValue("GLOBAL_MOTIONBLUR_CONTROLLER")
    NoOp['tile_color'].setValue(255)
    NoOp['note_font'].setValue("Bold")

    # Behold! The Knobs!
    NoOp.addKnob(nuke.Int_Knob('global_motionblur', "motionblur"))
    NoOp.addKnob(nuke.Double_Knob('global_shutter', "shutter"))
    NoOp.addKnob(nuke.Boolean_Knob('global_disable_moblur', "disable motionblur"))

    # Default values
    NoOp['global_motionblur'].setValue(1)
    NoOp['global_shutter'].setValue(0.5)

    NoOp['global_disable_moblur'].setFlag(nuke.STARTLINE)


    # Loop through all the nodes in node_list
    for node in node_list:

        if node.knob('motionblur'):
            node['motionblur'].setExpression('GLOBAL_MOTIONBLUR_CONTROLLER.global_disable_moblur == 0 ? GLOBAL_MOTIONBLUR_CONTROLLER.global_motionblur : 0')
            node['shutter'].setExpression('GLOBAL_MOTIONBLUR_CONTROLLER.global_shutter')

        elif node.knob('samples'):
            node['samples'].setExpression('GLOBAL_MOTIONBLUR_CONTROLLER.global_disable_moblur == 0 ? GLOBAL_MOTIONBLUR_CONTROLLER.global_motionblur : 1')
            node['shutter'].setExpression('GLOBAL_MOTIONBLUR_CONTROLLER.global_shutter')

    def addExpr():
        tn = nuke.thisNode()

        if tn.knob('motionblur'):
            tn['motionblur'].setExpression('GLOBAL_MOTIONBLUR_CONTROLLER.global_disable_moblur == 0 ? GLOBAL_MOTIONBLUR_CONTROLLER.global_motionblur : 0')
            tn['shutter'].setExpression('GLOBAL_MOTIONBLUR_CONTROLLER.global_shutter')
        elif tn.knob('samples'):
            tn['samples'].setExpression('GLOBAL_MOTIONBLUR_CONTROLLER.global_disable_moblur == 0 ? GLOBAL_MOTIONBLUR_CONTROLLER.global_motionblur : 1')
            tn['shutter'].setExpression('GLOBAL_MOTIONBLUR_CONTROLLER.global_shutter')

    nuke.addOnCreate(addExpr)


    def deleteExpressions():
        
        for node in nuke.allNodes():
            if node.knob('motionblur'):
                node['motionblur'].clearAnimated()
                node['motionblur'].setValue(0)
                node['shutter'].clearAnimated()
                node['shutter'].setValue(0.5)

            elif node.knob('samples'):
                node['samples'].clearAnimated()
                node['samples'].setValue(1)
                node['shutter'].clearAnimated()
                node['shutter'].setValue(0.5)

    nuke.addOnDestroy(deleteExpressions, nodeClass='NoOp') # This will affect Cow Blur Controller. Figure out a way to do without class.

nuke.menu('Nuke').addCommand('Utilities/Global Motionblur Controller', 'moblur_controller.moblur_controller()')