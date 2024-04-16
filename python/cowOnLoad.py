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

    currentNukePath = nuke.root().name()

    # Example Nuke filepath for script (root.name within Nuke):
    # K:/Freelance/Bug/5-SHOTS/001/bug_001_013/Comp/Nuke/bug_001_013_cmp_main_v001.nk
    # Following variables extract either from user text fields or slicing up the root.name

    splitPathList = currentNukePath.split('/')
    # ['K:', 'Freelance', 'Bug', '5-SHOTS', '001', 'bug_001_013', 'Comp', 'Nuke', 'bug_001_013_cmp_main_v001.nk']

    currentScriptFilename = splitPathList[-1]                               # bug_001_013_cmp_main_v001.nk
    currentScriptFileNoExt = splitPathList[-1].split('.')[0]                # bug_001_013_cmp_main_v001
    splitSceneNameList = currentScriptFileNoExt.split('_')
    # ['bug', '001', '013', 'cmp', 'main', 'v001']

    currentProjectCode = splitSceneNameList[0]                              # bug
    currentSequence = splitSceneNameList[1]                                 # 001
    currentShot = splitSceneNameList[2]                                     # 013
    currentPipeCode = splitSceneNameList[3]                                 # cmp
    currentDescriptor = splitSceneNameList[4]                               # main
    currentVersionStr = splitSceneNameList[-1][1:]                          # 001
    currentVersionInt = int(currentVersion)                                 # 1 (as integer)

    currentSceneNameShort = '_'.join(splitSceneNameList[1:3])               # 001_013
    currentSceneNameFull = splitPathList[-4]                                # bug_001_013
    currentPipeStep = splitPathList[-3]                                     # Comp
    currentPipeDir = '/'.join(splitPathList[:-2])                           # K:/Freelance/Bug/5-SHOTS/001/Bug_001_013/Comp
    currentSceneDir = '/'.join(splitPathList[:-3])                          # K:/Freelance/Bug/5-SHOTS/001/Bug_001_013