#===============================================================================
# cowPostRenderMove.py
# Version: 1.0.0
# Last Updated: July 17, 2023
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# Looks at the files that were just rendered onto J: drive and copies them back
# to where they belong in the project working directory on K: and  T: drives.
# 
# This is currently only going to work for TheShift, as its project naming scheme
# doesn't use sequence numbers and is a little screwy.
#
# 2. Plate names lead with the same string as the individual shot directories
#================================================================================

import os, shutil, glob, time, re
from pathlib import Path

print("NateCow's Nuke Render Mover 9000\n\n")

# Get the Incoming and VFX directories from user
#sourcePath = input('Paste Input directory (source): ')
sourcePath = "J:/Nuke_Renders"
#TODO: Input validation to make sure a valid directory has been provided.
#vfxDir = input('\nPaste VFX Shots directory (destination): ')
vfxDirSSD = "K:/Freelance/TheShift/5-SHOTS"
vfxDirServer = "T:/Freelance/TheShift/5-SHOTS"
shotList = os.listdir(sourcePath)

os.chdir(sourcePath)
time.sleep(1)

print('\nHold onto your butts...\n')

# Test directories
# S:\Development\Automation\Transcoded_Brothers_Quarrel_Full_v05
# S:\Development\Automation\bro_vfx


for shot in shotList:
    
    newDir1 = f'{vfxDirSSD}/{shot}'
    newDir2 = f'{vfxDirServer}/{shot}'
    dest1 = Path(newDir1)
    dest2 = Path(newDir2)
    
    print(f'Copying  {shot}  to  {dest1}')

    shutil.copy(shot, dest1)

    print(f'Copying  {shot}  to  {dest2}')

    shutil.copy(shot, dest2)
    

message = "Job's done!"
print("-"*len(message) + "\n" + message + "\n")
input('Press Enter to exit')