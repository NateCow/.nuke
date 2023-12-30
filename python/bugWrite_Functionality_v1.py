#===============================================================================
# butWrite_Functionality_v1.py
# Version: 1.0.0
# Last Updated: December 29, 2023
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# USAGE:
#
# - Execute write node parameters, updated for freelance work on "Bug",
#   in late December 2023 / Early January 2024
# - No longer writing to J drive, just right where the files belong on SSD.
# - Utilizing custom delivery names for DPX Comp renders only.
#===============================================================================

#===============================================================================
# Example strings:
# [project]_[sequence]_[shot number]_[pipeline step]_[descriptor]_[version].[frame].[extention]
# bug_001_001_cmp_main_v001.1001.exr
# Nuke filepath for script:
# K
#===============================================================================


#===============================================================================
#  Drop-down menus; merely getting index of selection.
#  Probably a way to pull the actual string value,
#  but I probably had trouble getting that to work
#===============================================================================
renderTypeSelection = int(nuke.thisNode().knob('renderType').getValue())
renderFormatSelection = int(nuke.thisNode().knob('renderFormat').getValue())

renderTypeDict = {
    0: "cmp",
    1: "prc",
    2: "plt_DN",
    3: "rto",
    4: "pnt",
    5: "test",
}

pipelineStepDict = {
    "cmp": "Comp",
    "prc": "Precomps",
    "plt_DN": "_Plates",
    "rto": "Roto",
    "pnt": "Paint",
    "test": "Precomps"
}

renderTypeStr = renderTypeDict.get(renderTypeSelection)

renderFormatDict = {
    0: "dpx",
    1: "exr",
    2: "jpg",
    3: "mov"
}

renderFormatExt = renderFormatDict.get(renderFormatSelection)

# Several of these knobs are filters within the read node that breakdown the directory path and return sections of it.
# 
customLabelStr = str(nuke.thisNode().knob('customLabel').getValue()) # A text field for user to add custom labeling - bug_001_001_cmp_[customLabelStr]_v001
versionStr = str(nuke.thisNode().knob('vers').getValue())
dirRoot = str(nuke.thisNode().knob('proj_root').getValue())
shotRoot = str(nuke.thisNode().knob('shot_root').getValue())
projName = dirRoot.split('/')[2]
scriptStep = str(nuke.thisNode().knob('step').getValue())
dirShot = str(nuke.thisNode().knob('shot').getValue())
dirScript = str(nuke.thisNode().knob('script').getValue())

if renderTypeSelection == 2:
    dirLabel = ""
elif len(nuke.thisNode().knob('customLabel').getValue()) > 0: #no custom label
    dirLabel = "_" + str(nuke.thisNode().knob('customLabel').getValue())
else:
    dirLabel = "_main"

#===============================================================================
# I know a .join('_') would go a long way for putting some elements together.
# I just have to make sure everything is clean and doesn't already have an understore in it.
#===============================================================================

shotBaseDir = str(dirRoot+"/"+ dirShot +"/")    #do we need this?
renderFileName = dirShot + "_" + renderTypeStr + dirLabel + "_v" + versionStr

if renderTypeSelection == 0: #dpx
    shotNumber = dirShot.split('_')[2]          #dirShot returns bug_001_001 so splits into list and grabs the last 3 digits
    subFolder = "Comp/_Renders/Event_Version 1_0001_0" + shotNumber + "_comp_v" + versionStr
    clientName = "A001C007_231213_R51W"
elif renderTypeSelection == 2:
    subFolder = "_Plates/Denoised/"
elif renderTypeSelection == 3:
    subFolder = "Roto/_Renders/"
elif renderTypeSelection == 4:
    subFolder = "Paint/_Renders"
else:
    subFolder = "Precomps/_Renders/"

renderDir = (shotRoot + "/" + subFolder)
    
if nuke.thisNode().knob('renderFormat').getValue() == 3: #QT movie
    nuke.thisNode().knob('file_type').setValue(renderFormatExt)
    nuke.thisNode().knob('file').setValue(renderDir + renderFileName + "/" + renderFormatExt + "/" + renderFileName + "." + renderFormatExt)
elif nuke.thisNode().knob('renderFormat').getValue() == 0: #DPX for Bug only
    nuke.thisNode().knob('file_type').setValue(renderFormatExt)
    nuke.thisNode().knob('file').setValue(renderDir + "/" + clientName + "_comp_v" + versionStr + ".%0" + "7d." + renderFormatExt)
else:
    nuke.thisNode().knob('file_type').setValue(renderFormatExt)
    nuke.thisNode().knob('file').setValue(renderDir + renderFileName + "/" + renderFormatExt + "/" + renderFileName + ".%0" + "4d." + renderFormatExt)

if nuke.thisNode().knob('renderFormat').getValue() == 2: #jpeg sequence
    nuke.thisNode().knob('file_type').setValue('jpeg')
    nuke.thisNode().knob('_jpeg_quality').setValue('1')


# Llamas. That is all.