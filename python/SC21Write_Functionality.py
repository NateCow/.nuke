shotNames = {
    'V1-0001-scp-vfx' : 'V1-0001_scp_vfx',
    'V1-0002-scp-vfx' : 'V1-0002_scp_vfx',
    'V1-0003-scp-vfx' : 'V1-0003_scp_vfx',
    'V1-0004-scp-vfx' : 'V1-0004_scp_vfx',
    'V1-0005-scp-vfx' : 'V1-0005_scp_vfx',
    'V1-0006-scp-vfx' : 'V1-0006_scp_vfx',
    'V1-0007-scp-vfx' : 'V1-0007_scp_vfx',
    'V1-0008-scp-vfx' : 'V1-0008_scp_vfx',
    'V1-0009-scp-vfx' : 'V1-0009_scp_vfx',
    'V1-0010-scp-vfx' : 'V1-0010_scp_vfx',
    'V1-0011-scp-vfx' : 'V1-0011_scp_vfx',
    'V1-0012-scp-vfx' : 'V1-0012_scp_vfx',
    'V1-0013-scp-vfx' : 'V1-0013_scp_vfx',
    'V1-0014-scp-vfx' : 'V1-0014_scp_vfx',
    'V1-0015-scp-vfx' : 'V1-0015_scp_vfx',
    'V1-0016-scp-vfx' : 'V1-0016_scp_vfx',
    'V1-0017-scp-vfx' : 'V1-0017_scp_vfx',
    'V1-0018-scp-vfx' : 'V1-0018_scp_vfx',
    'V1-0019-scp-vfx' : 'V1-0019_scp_vfx',
    'V1-0020-scp-vfx' : 'V1-0020_scp_vfx',
    'V1-0021-scp-vfx' : 'V1-0021_scp_vfx',
    'V1-0022-scp-vfx' : 'V1-0022_scp_vfx',
    'V1-0023-scp-vfx' : 'V1-0023_scp_vfx',
    'V1-0024-scp-vfx' : 'V1-0024_scp_vfx',
    'V1-0025-scp-vfx' : 'V1-0025_scp_vfx',
    'V1-0026-scp-vfx' : 'V1-0026_scp_vfx',
    'V1-0027-scp-vfx' : 'V1-0027_scp_vfx',
    'V1-0028-scp-vfx' : 'V1-0028_scp_vfx',
    'V1-0029-scp-vfx' : 'V1-0029_scp_vfx',
    'V1-0030-scp-vfx' : 'V1-0030_scp_vfx',
    'V1-0031-scp-vfx' : 'V1-0031_scp_vfx',
    'V1-0032-scp-vfx' : 'V1-0032_scp_vfx',
    'V1-0033-scp-vfx' : 'V1-0033_scp_vfx',
    'V1-0034-scp-vfx' : 'V1-0034_scp_vfx',
    'V1-0035-scp-vfx' : 'V1-0035_scp_vfx',
    'V1-0036-scp-vfx' : 'V1-0036_scp_vfx',
    'V1-0037-scp-vfx' : 'V1-0037_scp_vfx',
    'V1-0038-scp-vfx' : 'V1-0038_scp_vfx',
    'V1-0039-scp-vfx' : 'V1-0039_scp_vfx',
    'V1-0040-scp-vfx' : 'V1-0040_scp_vfx',
    'V1-0041-scp-vfx' : 'V1-0041_scp_vfx',
}

deliveryFolder = 'S:/Projects/SC21/vfx/_Delivery/'


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