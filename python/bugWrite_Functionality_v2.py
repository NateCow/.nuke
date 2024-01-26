#===============================================================================
# butWrite_Functionality_v2.py
# Version: 2.0.0
# Last Updated: January 24, 2024
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
# [project]_[sequence]_[shot number]_[pipeline step]_[descriptor]_[version].[frame].[extension]
# Bug_001_013_cmp_main_v001.1001.exr
# Example Nuke filepath for script (root.name within Nuke):
# K:/Freelance/Bug/5-SHOTS/001/Bug_001_013/Comp/Nuke/bug_001_013_cmp_main_v001.nk
#===============================================================================


#===============================================================================
#  Drop-down menus; returns index of selection
#  and then matches that to dictionary keys in renderTypeDict and renderFormatDict
#  Probably a way to pull the actual string value,
#  but I probably had trouble getting that to work
#  I need a better way to name the dictionaries; I don't like 'dict' :P 
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

#===============================================================================
# Several of these knobs are filters within the read node that breakdown the directory path and return sections of it.
# Example Nuke filepath for script (root.name within Nuke):
# K:/Freelance/Bug/5-SHOTS/001/Bug_001_013/Comp/Nuke/bug_001_013_cmp_main_v001.nk
# Following variables extract either from user text fields or slicing up the root.name
#===============================================================================
customLabelStr = str(nuke.thisNode().knob('customLabel').getValue()) # User field: Bug_001_013_cmp_[customLabelStr]_v001 (uses 'main' by default (line 87))
versionStr = str(nuke.thisNode().knob('vers').getValue())            # User field: Bug_001_013_cmp_main_v[versionStr]
dirRoot = str(nuke.thisNode().knob('proj_root').getValue())          # From root: 'K:/Freelance/Bug/5-SHOTS/001/Bug_001_013/Comp/Nuke'
shotRoot = str(nuke.thisNode().knob('shot_root').getValue())         # From root: 'K:/Freelance/Bug/5-SHOTS/001/Bug_001_013'
projName = dirRoot.split('/')[2]                                     # From root: 'Bug'
scriptStep = str(nuke.thisNode().knob('step').getValue())            # From root: 'Comp'
dirShot = str(nuke.thisNode().knob('shot').getValue())               # From root: 'Bug_001_013'
dirScript = str(nuke.thisNode().knob('script').getValue())           # From root: 'Bug_001_013_cmp_main_v001'

if renderTypeSelection == 2: # Line 37
    dirLabel = ""            # Ensures "plt_DN" in the case of "Denoise Plate" selection.
                             # Custom label needs to be blank as renderTypeStr on line 55 will assign "plt_DN" as both the render type (plate) AND custom label (denoise (DN))
elif len(nuke.thisNode().knob('customLabel').getValue()) > 0: # Any text detected in custom label field gets assigned here.
    dirLabel = "_" + str(nuke.thisNode().knob('customLabel').getValue())
else: # Otherwise assume "main". Hard-coding the underscore is stupid.
    dirLabel = "_main"

#===============================================================================
# I know a .join('_') would go a long way for putting some elements together.
# I just have to make sure everything is clean and doesn't already have an understore in it. (See comment on line 86)
#===============================================================================

shotBaseDir = str(dirRoot+"/"+ dirShot +"/")    # This might have been an older variable. We have shotRoot on line 75 that producees the same thing except without the trailing "/"
renderFileName = dirShot + "_" + renderTypeStr + dirLabel + "_v" + versionStr   # Name for render without frame padding or file exension - Bug_001_013_cmp_main_v001.
                                                                                # Note in the case of Bug, this doesn't get used for cmp_main renders. I write out to the client name below.

#===============================================================================
# Tracking my internal name as the key and client name as value.
#===============================================================================
clientNameDict = {
    "Bug_001_001": "A001C007_231213_R51W",
    "Bug_001_002": "A001C007_231213_R51W",
    "Bug_001_003": "A001C012_231213_R51W",
    "Bug_001_004": "A001C023_231213_R51W",
    "Bug_001_005": "A001C025_231213_R51W",
    "Bug_001_006": "A001C030_231213_R51W",
    "Bug_001_007": "A003C017_231214_R51W",
    "Bug_001_008": "A003C014_231213_R51W",
    "Bug_001_009": "A005C024_231214_R51W",
    "Bug_001_010": "A005C021_231214_R51W",
    "Bug_001_011": "A002C016_231213_R51W",
    "Bug_001_012": "A004C027_231214_R51W",
    "Bug_001_013": "A007C012_231214_R51W",
    "Bug_002_001": "A005C006_231214_R51W", # TV Shot
    "Bug_002_002": "A005C005_231214_R51W", # TV Shot
    "Bug_002_003": "A005C006_231214_R51W"  # TV Shot
}

if renderTypeSelection == 0: # dpx
    shotNumber = dirShot.split('_')[2]          # '013' - dirShot returns 'Bug_001_013' so splits into list and grabs the last index item ([-1] would probably be better and allow for situations where I don't have sequence numbers)
    subFolder = "Comp/_Renders/Event_Version 1_0001_0" + shotNumber + "_comp_v" + versionStr    # 'Comp/_Renders/Event_Version 1_0001_0013_comp_v001'
    clientName = clientNameDict[dirShot]   # 'A007C012_231214_R51W'
    # The above only happens on the DPX selection because this project delivers DPX files as the original client name.
    # All other renders that I do internally to EXR, I leave with my internal naming.
elif renderTypeSelection == 2:
    subFolder = "_Plates/Denoised/"
elif renderTypeSelection == 3:
    subFolder = "Roto/_Renders/"
elif renderTypeSelection == 4:
    subFolder = "Paint/_Renders"
else:
    subFolder = "Precomps/_Renders/"

renderDir = (shotRoot + "/" + subFolder)
    
if nuke.thisNode().knob('renderFormat').getValue() == 3: # QT movie
    nuke.thisNode().knob('file_type').setValue(renderFormatExt)
    nuke.thisNode().knob('file').setValue(renderDir + renderFileName + "/" + renderFormatExt + "/" + renderFileName + "." + renderFormatExt)
elif nuke.thisNode().knob('renderFormat').getValue() == 0: # DPX for Bug only, needs a 7-digit frame padding instead of my usual 4.
    nuke.thisNode().knob('file_type').setValue(renderFormatExt)
    nuke.thisNode().knob('file').setValue(renderDir + "/" + clientName + "_comp_v" + versionStr + ".%0" + "7d." + renderFormatExt) # 'K:/Freelance/Bug/5-SHOTS/001/Bug_001_013/Comp/_Renders/Event_Version 1_0001_0013_comp_v001/A007C012_231214_R51W_comp_v001.%07d.dpx'
else:
    nuke.thisNode().knob('file_type').setValue(renderFormatExt) # Only other options are EXR & JPG, in which case they both get the same naming here.
    nuke.thisNode().knob('file').setValue(renderDir + renderFileName + "/" + renderFormatExt + "/" + renderFileName + ".%0" + "4d." + renderFormatExt)

if nuke.thisNode().knob('renderFormat').getValue() == 2: # Knobs specific to jpegs that need set, thus why this is a seperate conditional.
    nuke.thisNode().knob('file_type').setValue('jpeg')
    nuke.thisNode().knob('_jpeg_quality').setValue('1')







# Llamas. That is all.