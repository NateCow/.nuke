#===============================================================================
# hangWrite_Functionality.py
# Version: 1.0.0
# Last Updated: July 21, 2023
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# USAGE:
#
# - Execute write node parameters, updated for freelance work on Hangman.
#   More robust tooling to follow.
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


customLabelStr = str(nuke.thisNode().knob('customLabel').getValue())
versionStr = str(nuke.thisNode().knob('vers').getValue())
dirRoot = str(nuke.thisNode().knob('proj_root').getValue())
projName = dirRoot.split('/')[2]
scriptStep = str(nuke.thisNode().knob('step').getValue())
dirSeq = str(nuke.thisNode().knob('seq').getValue())
dirShot = str(nuke.thisNode().knob('shot').getValue())
dirScript = str(nuke.thisNode().knob('script').getValue())

if renderTypeSelection == 2:
    dirLabel = ""
elif len(nuke.thisNode().knob('customLabel').getValue()) > 0: #no custom label
    dirLabel = "_" + str(nuke.thisNode().knob('customLabel').getValue())
else:
    dirLabel = "_main"

shotBaseDir = str(dirRoot+"/"+dirShot+"/") #do we need this?
renderFileName = dirShot + "_" + renderTypeStr + dirLabel + "_v" + versionStr

if renderTypeSelection == 0:
    subFolder = "Comp/_Renders/"
elif renderTypeSelection == 2:
    subFolder = "_Plates/Denoised/"
elif renderTypeSelection == 3:
    subFolder = "Roto/_Renders/"
elif renderTypeSelection == 4:
    subFolder = "Paint/_Renders"
else:
    subFolder = "Precomps/_Renders/"

tempDir = ("J:/Nuke_Renders/hang/" + dirSeq + "/" + dirShot + "/" + subFolder)
    
if nuke.thisNode().knob('renderFormat').getValue() == 3: #QT movie
    nuke.thisNode().knob('file_type').setValue(renderFormatExt)
    nuke.thisNode().knob('file').setValue(tempDir + renderFileName + "/" + renderFormatExt + "/" + renderFileName + "." + renderFormatExt)
else:
    nuke.thisNode().knob('file_type').setValue(renderFormatExt)
    nuke.thisNode().knob('file').setValue(tempDir + renderFileName + "/" + renderFormatExt + "/" + renderFileName + ".%0" + "4d." + renderFormatExt)

if nuke.thisNode().knob('renderFormat').getValue() == 2: #jpeg sequence
    nuke.thisNode().knob('file_type').setValue('jpeg')
    nuke.thisNode().knob('_jpeg_quality').setValue('1')

# Llamas. That is all.