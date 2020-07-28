renderTypeSelection = int(nuke.thisNode().knob('renderType').getValue())
renderFormatSelection = int(nuke.thisNode().knob('renderFormat').getValue())
framePaddingSelection = int(nuke.thisNode().knob('framePadding').getValue())

renderTypeDict = {
	0: "comp_main",
	1: "prc",
	2: "plt_DN",
	3: "test",
	4: "slap",
	5: "matte",
}

renderTypeStr = renderTypeDict.get(renderTypeSelection)

renderFormatDict = {
	0: "dpx",
	1: "exr",
	2: "jpg",
	3: "mov"
}

renderFormatExt = renderFormatDict.get(renderFormatSelection)

framePaddingDict = {
	0: "2",
	1: "4",
	2: "5",
	3: "6"
}

framePaddingStr = framePaddingDict.get(framePaddingSelection)

customLabelStr = str(nuke.thisNode().knob('customLabel').getValue())
versionStr = str(nuke.thisNode().knob('vers').getValue())
dirRoot = str(nuke.thisNode().knob('proj_root').getValue())
dirSeq = str(nuke.thisNode().knob('seq').getValue())
dirShot = str(nuke.thisNode().knob('shot').getValue())
dirScript = str(nuke.thisNode().knob('script').getValue())
dirLabel = "_" + str(nuke.thisNode().knob('customLabel').getValue())

shotBaseDir = str(dirRoot+"/"+dirSeq+"/"+dirShot+"/")

if renderTypeSelection == 0:
	subFolder = "comp/"
elif renderTypeSelection == 2:
	subFolder = "live_action/"
elif renderTypeSelection == 5:
	subFolder = "mattes/"
else:
	subFolder = "precomps/"

if len(nuke.thisNode().knob('customLabel').getValue()) > 0: #no custom label
	if nuke.thisNode().knob('renderFormat').getValue() == 3: #QT movie
		nuke.thisNode().knob('file_type').setValue(renderFormatExt)
		nuke.thisNode().knob('file').setValue(shotBaseDir + subFolder + dirShot + "_" + renderTypeStr + dirLabel + "_v" + versionStr + "." + renderFormatExt)
	else:
		nuke.thisNode().knob('file_type').setValue(renderFormatExt)
		nuke.thisNode().knob('file').setValue(shotBaseDir + subFolder + dirShot + "_" + renderTypeStr + dirLabel + "_v" + versionStr + "/" + renderFormatExt + "/" + dirShot + "_" + renderTypeStr + dirLabel + "_v" + versionStr + ".%0" + framePaddingStr + "d." + renderFormatExt)
else:
	if nuke.thisNode().knob('renderFormat').getValue() == 3: #QT movie
		nuke.thisNode().knob('file_type').setValue(renderFormatExt)
		nuke.thisNode().knob('file').setValue(shotBaseDir + subFolder + dirShot + "_" + renderTypeStr + "_v" + versionStr + "." + renderFormatExt)
	else:
		nuke.thisNode().knob('file_type').setValue(renderFormatExt)
		nuke.thisNode().knob('file').setValue(shotBaseDir + subFolder + dirShot + "_" + renderTypeStr + "_v" + versionStr + "/" + renderFormatExt + "/" + dirShot + "_" + renderTypeStr + "_v" + versionStr + ".%0" + framePaddingStr + "d." + renderFormatExt)

if nuke.thisNode().knob('renderFormat').getValue() == 2: #jpeg sequence
	nuke.thisNode().knob('file_type').setValue('jpeg')
	nuke.thisNode().knob('_jpeg_quality').setValue('1')

# Llamas. That is all.