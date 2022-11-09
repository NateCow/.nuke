
shotNames = {
    'erz_071_001' : 'ERZULIE_VFX 7-1_SCENE 57_SHOT 1',
    'erz_065_001' : 'ERZULIE_VFX 8-1_SCENE 65_SHOT 1',
    'erz_065_002' : 'ERZULIE_VFX 8-2_SCENE 65_SHOT 2'
}

deliveryFolder = 'S:/Projects/ERZ/vfx/_Delivery/'


versionStr = str(nuke.thisNode().knob('vers').getValue())
dirRoot = str(nuke.thisNode().knob('proj_root').getValue())
dirSeq = str(nuke.thisNode().knob('seq').getValue())
dirShot = str(nuke.thisNode().knob('shot').getValue())
dirScript = str(nuke.thisNode().knob('script').getValue())


nuke.thisNode().knob('file').setValue(deliveryFolder + shotNames[dirShot] + '_comp_v' + versionStr + '.mov')
nuke.thisNode().knob('file_type').setValue('mov')
nuke.thisNode().knob('raw').setValue(1)
nuke.thisNode().knob('meta_codec').setValue(6)


# Llamas. That is all.