shotNames = {
    'ltm_pnt_010': 'Lie_To_Me_VFX_Clip_01',
    'ltm_hr_010': 'Lie_To_Me_VFX_Clip_02',
    'ltm_pnt_020': 'Lie_To_Me_VFX_Clip_03',
    'ltm_hr_020': 'Lie_To_Me_VFX_Clip_04',
    'ltm_hr_030': 'Lie_To_Me_VFX_Clip_05',
    'ltm_pnt_060': 'Lie_To_Me_VFX_Clip_06',
    'ltm_hr_040': 'Lie_To_Me_VFX_Clip_07',
    'ltm_pnt_030': 'Lie_To_Me_VFX_Clip_17',
    'ltm_hr_050': 'Lie_To_Me_VFX_Clip_18',
    'ltm_pnt_040': 'Lie_To_Me_VFX_Clip_19',
    'ltm_pnt_050': 'Lie_To_Me_VFX_Clip_20'
}


versionStr = str(nuke.thisNode().knob('vers').getValue())
dirRoot = str(nuke.thisNode().knob('proj_root').getValue())
dirSeq = str(nuke.thisNode().knob('seq').getValue())
dirShot = str(nuke.thisNode().knob('shot').getValue())
dirScript = str(nuke.thisNode().knob('script').getValue())


nuke.thisNode().knob('file').setValue(dirRoot+'/'+dirSeq+'/'+dirShot+'/COMPS/'+ shotNames[('_').join(dirScript.split('_')[0:3])] + '_comp_' + versionStr + '.mov')
nuke.thisNode().knob('file_type').setValue('mov')
nuke.thisNode().knob('raw').setValue(1)
nuke.thisNode().knob('meta_codec').setValue(6)


# Llamas. That is all.