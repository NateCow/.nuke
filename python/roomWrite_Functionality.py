shotNames = {
    'bell_001_001': 'MOLTO_BELLA_REEL_001_shot_1',
    'bell_001_020': 'VFX_Reel_1_phone',
    'bell_003_020': 'VFX_Reel_3_phone',
    'bell_005_020': 'VFX_Reel_5_Bathroom',
    'bell_005_000': 'VFX_Reel_5_BG_Plate',
    'bell_005_001': 'VFX_Reel_5_sunrise_1',
    'bell_005_010': 'VFX_Reel_5_sunrise_10',
    'bell_005_011': 'VFX_Reel_5_sunrise_11',
    'bell_005_012': 'VFX_Reel_5_sunrise_12',
    'bell_005_013': 'VFX_Reel_5_sunrise_13',
    'bell_005_002': 'VFX_Reel_5_sunrise_2',
    'bell_005_003': 'VFX_Reel_5_sunrise_3',
    'bell_005_004': 'VFX_Reel_5_sunrise_4',
    'bell_005_005': 'VFX_Reel_5_sunrise_5',
    'bell_005_006': 'VFX_Reel_5_sunrise_6',
    'bell_005_007': 'VFX_Reel_5_sunrise_7',
    'bell_005_008': 'VFX_Reel_5_sunrise_8',
    'bell_005_009': 'VFX_Reel_5_sunrise_9'
}

deliveryFolder = 'S:/Projects/room/vfx/_Delivery/'


versionStr = str(nuke.thisNode().knob('vers').getValue())
dirRoot = str(nuke.thisNode().knob('proj_root').getValue())
dirSeq = str(nuke.thisNode().knob('seq').getValue())
dirShot = str(nuke.thisNode().knob('shot').getValue())
dirScript = str(nuke.thisNode().knob('script').getValue())


nuke.thisNode().knob('file').setValue(deliveryFolder + shotNames[dirShot] + '_comp_v' + versionStr + '.mov')
nuke.thisNode().knob('file_type').setValue('mov')
nuke.thisNode().knob('colorspace').setValue('AlexaV3LogC')
nuke.thisNode().knob('meta_codec').setValue(6)


# Llamas. That is all.