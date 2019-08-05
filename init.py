#===============================================================================
# init.py
# Version: 1.0.3
# Last Updated: August 4th, 2019
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

# ----- DEFINE CUSTOM FOLDER STRUCTURE -----------------------------------------

nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./python')
nuke.pluginAddPath('./icons')



# Project Settings > Default format: TWWS
nuke.knobDefault("Root.format", "GSP")
nuke.knobDefault("fps", "24")

nuke.addFormat("4096 1728 1 Memoir_4k")
nuke.addFormat("2048 864 1 Memoir_2k")
nuke.addFormat("1920 810 1 Memoir_1080p")
nuke.addFormat("2048 1714 2 Native 2k Anamorphic")
nuke.addFormat("2048 1706 2 TC 2k Anamorphic")
nuke.addFormat("2944 2160 2 VW Anamorphic")
nuke.addFormat("2880 2160 2 HS 2 Anamorphic")
nuke.addFormat("4096 1743 1 Aria")
nuke.addFormat("4096 1707 1 Candyland")
nuke.addFormat("1920 800 1 Candyland 1080")
nuke.addFormat("2880 1620 1 TCW")
nuke.addFormat("1920 960 1 HOHH 2k")
nuke.addFormat("4096 1716 1 GSP")
nuke.addFormat("3200 1800 1 Yosemite Full")
nuke.addFormat("1600 900 1 Yosemite Half")
nuke.addFormat("3841 1600 1 SC19 4k Wide")
nuke.addFormat("1920 1607 2 Minecraft Anamorphic")

nuke.pluginAddPath('f:/nuke_plugins')
nuke.pluginAddPath('f:/nuke_plugins/errorReport')

#custom input/output LUTs
nuke.root().knob('luts').addCurve("AlexaV3LogC", "{ t > 0.1496582 ? (pow(10.0, (t - 0.385537) / 0.2471896) - 0.052272) / 5.555556 : (t - 0.092809) / 5.367655 }")
# ViewerProcess LUTs
nuke.ViewerProcess.register("AlexaV3Rec709", nuke.createNode,
("Vectorfield", "vfield_file F:/nuke_plugins/luts/AlexaV3_K1S1_LogC2Video_Rec709_EE_nuke3d.cube colorspaceIn AlexaV3LogC"))


import cryptomatte_utilities
cryptomatte_utilities.setup_cryptomatte()
