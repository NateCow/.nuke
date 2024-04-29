import nuke
import cowOnLoad

pipeCodeUserSelect = int(nuke.thisNode().knob('pipeSelect').getValue())
renderFormatUserSelect = int(nuke.thisNode().knob('renderFormat').getValue())

pipeCodeSelect = {
    0: "cmp",
    1: "prc",
    2: "plt_DN",
    3: "roto",
    4: "pnt",
    5: "test",
    6: "plt"
}

pipeCodeFolder = {
    "cmp": "Comp/_Renders",
    "prc": "Precomps/_Renders",
    "plt_DN": "_Plates/Denoised",
    "roto": "Roto/_Renders",
    "pnt": "Paint/_Renders",
    "test": "Precomps/_Renders",
    "plt": "_Plates"
}

renderTypeStr = pipeCodeSelect.get(pipeCodeUserSelect)
pipeFolder = pipeCodeFolder[renderTypeStr]

renderFormatSelect = {
    0: "dpx",
    1: "exr",
    2: "jpg",
    3: "mov"
}

renderFormatExt = renderFormatSelect.get(renderFormatUserSelect)

#===============================================================================
# Remapping variables from cowOnLoad.roundUpVariables()
#===============================================================================

currentDescriptor = cowOnLoad.currentDescriptor
currentSceneDir = cowOnLoad.currentSceneDir
currentPipeStep = cowOnLoad.currentPipeStep
currentVersionStr = cowOnLoad.currentVersionStr
currentSceneNameFull = cowOnLoad.currentSceneNameFull


#===============================================================================
# Example Nuke filepath for script (root.name within Nuke):
# K:/Freelance/Bug/5-SHOTS/001/bug_001_013/Comp/Nuke/bug_001_013_cmp_main_v001.nk
# Following variables extract either from user text fields or slicing up the root.name
#===============================================================================
customLabelStr = str(nuke.thisNode().knob('customLabel').getValue())        # User field: Bug_001_013_cmp_[customLabelStr]_v001 (uses 'main' by default (see below))
versionUserDefined = str(nuke.thisNode().knob('vers').getValue())           # User field: Bug_001_013_cmp_main_v[versionUserDefined]

if pipeCodeUserSelect == 2:
    if len(customLabelStr) > 0:
        renderLabel = "plt_DN" + str(nuke.thisNode().knob('customLabel').getValue())       # If custom label is filled in on Denoise Plate selection, label is "DN[customLabel]"
    else:
        renderLabel = "plt_DN"
elif len(customLabelStr) > 0: # Any text detected in custom label field gets assigned here.
    renderLabel = customLabelStr
else: # Otherwise assume "main". Hard-coding the underscore is stupid.
    renderLabel = currentDescriptor

if len(versionUserDefined) > 0:
    versionForOutput = versionUserDefined
else:
    versionForOutput = currentVersionStr



renderDir = currentSceneDir + '/' + pipeFolder
if pipeCodeUserSelect == 2:
    renderFilenameList = [currentSceneNameFull, renderLabel, "v" + versionForOutput]
    renderFileName = "_".join(renderFilenameList)
else:
    renderFilenameList = [currentSceneNameFull, renderTypeStr, renderLabel, "v" + versionForOutput]
    renderFileName = "_".join(renderFilenameList)
#renderFileName = currentSceneNameFull + "_" + renderTypeStr + renderLabel + "_v" + versionUserDefined   # Name for render without frame padding or file exension - Bug_001_013_cmp_main_v001.
                                                                                # Note in the case of Bug, this doesn't get used for cmp_main renders. I write out to the client name below.

pipeFolder = pipeCodeFolder[renderTypeStr]
#renderDir = (shotRoot + "/" + pipeFolder)
#fileOutputListQT = [renderDir, renderFileName, renderFormatExt]
#fileOutputListImageSeq =  [renderDir, renderFileName,]

    
if nuke.thisNode().knob('renderFormat').getValue() == 3: # QT movie
    nuke.thisNode().knob('file_type').setValue(renderFormatExt)
    nuke.thisNode().knob('file').setValue(renderDir + "/" + renderFileName + "." + renderFormatExt)
else:
    nuke.thisNode().knob('file_type').setValue(renderFormatExt) # Image Sequences
    nuke.thisNode().knob('file').setValue(renderDir + "/" + renderFileName + "/" + renderFormatExt + "/" + renderFileName + ".%0" + "4d." + renderFormatExt)

if nuke.thisNode().knob('renderFormat').getValue() == 2: # Knobs specific to jpegs that need set, thus why this is a seperate conditional.
    nuke.thisNode().knob('file_type').setValue('jpeg')
    nuke.thisNode().knob('_jpeg_quality').setValue('1')

outputDir = nuke.thisNode().knob('file').getValue()
outputMessage = "File out directory set to: " + outputDir
#print("test")
#print("llamas")
print(outputMessage)

# Llamas. That is all.