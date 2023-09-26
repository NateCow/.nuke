#===============================================================================
# shiftWrite_Functionality_v2.py
# Version: 2.0.0
# Last Updated: July 17, 2023
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# USAGE:
#
# - Execute write node parameters, updated for freelance work on TheShift and
#   Hangman. More robust tooling to follow.
#===============================================================================


def Order66():
    
    import nuke

    renderTypeSelection = int(nuke.thisNode().knob('renderType').getValue())
    renderFormatSelection = int(nuke.thisNode().knob('renderFormat').getValue())

    renderTypeDict = {
        0: "cmp",
        1: "prc",
        2: "plt_DN",
        3: "test",
        4: "slp",
        5: "rot",
    }

    renderTypeStr = renderTypeDict.get(renderTypeSelection)

    renderFormatDict = {
        0: "dpx",
        1: "exr",
        2: "jpg",
        3: "mov"
    }

    renderFormatExt = renderFormatDict.get(renderFormatSelection)


    customLabelStr = str(nuke.thisNode().knob('customLabel').getValue())
    versionStr = str(nuke.thisNode().knob('vers').getValue())
    dirRoot = str(nuke.thisNode().knob('proj_root').getValue())
    projName = dirRoot.split('/')[2]
    scriptStep = str(nuke.thisNode().knob('step').getValue())
    dirShot = str(nuke.thisNode().knob('shot').getValue())
    dirScript = str(nuke.thisNode().knob('script').getValue())
    if len(nuke.thisNode().knob('customLabel').getValue()) > 0: #no custom label
        dirLabel = "_" + str(nuke.thisNode().knob('customLabel').getValue())
    else:
        dirLabel = "_main"

    shotBaseDir = str(dirRoot+"/"+dirShot+"/") #do we need this?

    if renderTypeSelection == 0:
        cmpTemp = ("J:/Nuke_Renders/" + projName + "/" + dirShot + "/" + dirShot + "_cmp_main_v" + versionStr + "/" + renderFormatExt)
    elif renderTypeSelection == 2:
        subFolder = "_Plates/Denoised/"
    elif renderTypeSelection == 5:
        subFolder = "Roto/_Renders/"
    else:
        subFolder = "Precomps/_Renders/"

        
    if nuke.thisNode().knob('renderFormat').getValue() == 3: #QT movie
        nuke.thisNode().knob('file_type').setValue(renderFormatExt)
        nuke.thisNode().knob('file').setValue(shotBaseDir + subFolder + dirShot + "_" + renderTypeStr + dirLabel + "_v" + versionStr + "." + renderFormatExt)
    else:
        nuke.thisNode().knob('file_type').setValue(renderFormatExt)
        nuke.thisNode().knob('file').setValue(shotBaseDir + subFolder + dirShot + "_" + renderTypeStr + dirLabel + "_v" + versionStr + "/" + renderFormatExt + "/" + dirShot + "_" + renderTypeStr + dirLabel + "_v" + versionStr + ".%0" + "4d." + renderFormatExt)

    if nuke.thisNode().knob('renderFormat').getValue() == 2: #jpeg sequence
        nuke.thisNode().knob('file_type').setValue('jpeg')
        nuke.thisNode().knob('_jpeg_quality').setValue('1')

# Llamas. That is all.