#===============================================================================
# cowOnLoad.py
# Version: 1.0.0
# Last Updated: April 16, 2024
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# USAGE:
#
# - To be executed on project load, storing variables for custom write node tool.
# - May initially set this as a menu command to run, in case project opening doesn't follow pattern.
# - Should do a check initially to make sure file hierarchy and filename match pipeline.
#===============================================================================

import nuke

def roundUpVariables():


    global currentNukePath
    currentNukePath = nuke.root().name()

    # Example Nuke filepath for script (root.name within Nuke):
    # K:/Freelance/Bug/5-SHOTS/001/bug_001_013/Comp/Nuke/bug_001_013_cmp_main_v001.nk
    # Following variables extract either from user text fields or slicing up the root.name

    splitPathList = currentNukePath.split('/')
    # ['K:', 'Freelance', 'Bug', '5-SHOTS', '001', 'bug_001_013', 'Comp', 'Nuke', 'bug_001_013_cmp_main_v001.nk']

    global currentScriptFilename
    currentScriptFilename = splitPathList[-1]                               # bug_001_013_cmp_main_v001.nk
    global currentScriptFileNoExt
    currentScriptFileNoExt = splitPathList[-1].split('.')[0]                # bug_001_013_cmp_main_v001

    splitSceneNameList = currentScriptFileNoExt.split('_')
    # ['bug', '001', '013', 'cmp', 'main', 'v001']

    global currentProjectCode
    currentProjectCode = splitSceneNameList[0]                              # bug
    global currentSequence
    currentSequence = splitSceneNameList[1]                                 # 001
    global currentShot
    currentShot = splitSceneNameList[2]                                     # 013
    global currentPipeCode
    currentPipeCode = splitSceneNameList[3]                                 # cmp
    global currentDescriptor
    currentDescriptor = splitSceneNameList[4]                               # main
    global currentVersionStr
    currentVersionStr = splitSceneNameList[-1][1:]                          # 001
    global currentVersionInt
    currentVersionInt = int(currentVersionStr)                              # 1 (as integer)

    global currentSceneNameShort
    currentSceneNameShort = '_'.join(splitSceneNameList[1:3])               # 001_013
    global currentSceneNameFull
    currentSceneNameFull = splitPathList[-4]                                # bug_001_013
    global currentPipeStep
    currentPipeStep = splitPathList[-3]                                     # Comp
    global currentPipeDir
    currentPipeDir = '/'.join(splitPathList[:-2])                           # K:/Freelance/Bug/5-SHOTS/001/Bug_001_013/Comp
    global currentSceneDir
    currentSceneDir = '/'.join(splitPathList[:-3])                          # K:/Freelance/Bug/5-SHOTS/001/Bug_001_013


nuke.menu('Nuke').addCommand('Cow/Round Up Variables', 'cowOnLoad.roundUpVariables()', 'F8', shortcutContext=2)