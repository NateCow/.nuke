
shotNames = {
    'adi_000_001' : 'addie_vfx_shot001',
    'adi_000_004' : 'addie_vfx_shot004',
    'adi_000_007' : 'addie_vfx_shot007',
    'adi_000_008' : 'addie_vfx_shot008',
    'adi_000_009' : 'addie_vfx_shot009'
}

deliveryFolder = 'S:/Projects/adi/vfx/_Delivery/'


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