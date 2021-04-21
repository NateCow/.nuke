shotNames = {
    'room_002_001': 'SCENE 02_NECK SLICE_SHOT 1',
    'room_002_002': 'SCENE 02_NECK SLICE_SHOT 2',
    'room_002_003': 'SCENE 02_NECK SLICE_SHOT 3',
    'room_002_004': 'SCENE 02_NECK SLICE_SHOT 4',
    'room_002_005': 'SCENE 02_NECK SLICE_SHOT 5',
    'room_002_006': 'SCENE 02_NECK SLICE_SHOT 6',
    'room_002_007': 'SCENE 02_NECK SLICE_SHOT 7',
    'room_047_001': 'SCENE 47_IZZY EYE CHANGE 0',
    'room_048_001': 'SCENE 48_ELEVATOR DIAL',
    'room_058_001': 'SCENE 58_IZZY EYE CHANGE 1',
    'room_059_001': 'SCENE 59_CROW ON BED_SHOT 1',
    'room_059_002': 'SCENE 59_CROW ON BED_SHOT 2',
    'room_059_003': 'SCENE 59_CROW ON BED_SHOT 3',
    'room_059_004': 'SCENE 59_CROW ON BED_SHOT 4',
    'room_059_005': 'SCENE 59_CROW ON BED_SHOT 5',
    'room_059_006': 'SCENE 59_CROW ON BED_SHOT 6',
    'room_076_001': 'SCENE 76_IZZY EYE CHANGE 2',
    'room_077_001': 'SCENE 77_RONAN EYE STAB_SHOT 1',
    'room_077_002': 'SCENE 77_RONAN EYE STAB_SHOT 2',
    'room_085_001': 'SCENE 85_RONAN SUICIDE_SHOT 1',
    'room_085_002': 'SCENE 85_RONAN SUICIDE_SHOT 2',
    'room_085_003': 'SCENE 85_RONAN SUICIDE_SHOT 3',
    'room_085_004': 'SCENE 85_RONAN SUICIDE_SHOT 4',
    'room_085_005': 'SCENE 85_RONAN SUICIDE_SHOT 5',
    'room_088_001': 'SCENE 88_CROWS SMACK WINDOW_SHOT 1',
    'room_088_002': 'SCENE 88_CROWS SMACK WINDOW_SHOT 2',
    'room_088_003': 'SCENE 88_CROWS SMACK WINDOW_SHOT 3',
    'room_088_004': 'SCENE 88_CROWS SMACK WINDOW_SHOT 4',
    'room_088_005': 'SCENE 88_CROWS SMACK WINDOW_SHOT 5',
    'room_088_006': 'SCENE 88_CROWS SMACK WINDOW_SHOT 6',
    'room_088_007': 'SCENE 88_CROWS SMACK WINDOW_SHOT 7',
    'room_088_008': 'SCENE 88_CROWS SMACK WINDOW_SHOT 8',
    'room_088_009': 'SCENE 88_CROWS SMACK WINDOW_SHOT 9',
    'room_088_010': 'SCENE 88_CROWS SMACK WINDOW_SHOT 10',
    'room_088_011': 'SCENE 88_CROWS SMACK WINDOW_SHOT 11',
    'room_088_012': 'SCENE 88_CROWS SMACK WINDOW_SHOT 12',
    'room_088_013': 'SCENE 88_CROWS SMACK WINDOW_SHOT 13',
    'room_088_014': 'SCENE 88_CROWS SMACK WINDOW_SHOT 14',
    'room_088_015': 'SCENE 88_CROWS SMACK WINDOW_SHOT 15',
    'room_088_016': 'SCENE 88_CROWS SMACK WINDOW_SHOT 16',
    'room_088_017': 'SCENE 88_CROWS SMACK WINDOW_SHOT 17',
    'room_088_018': 'SCENE 88_CROWS SMACK WINDOW_SHOT 18',
    'room_090_001': 'SCENE 90_FINAL SHOT_STITCH'
}

deliveryFolder = 'S:/Projects/room/vfx/_Delivery/'


versionStr = str(nuke.thisNode().knob('vers').getValue())
dirRoot = str(nuke.thisNode().knob('proj_root').getValue())
dirSeq = str(nuke.thisNode().knob('seq').getValue())
dirShot = str(nuke.thisNode().knob('shot').getValue())
dirScript = str(nuke.thisNode().knob('script').getValue())


nuke.thisNode().knob('message').setValue(str(shotNames[dirShot] + '_comp_v' + versionStr))


# Llamas. That is all.