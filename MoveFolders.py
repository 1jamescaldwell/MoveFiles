#Move Folders, Created by James Caldwell, 9/1/23

#Moves all the files within a subfolder containing "HSV" in the folder name to a new location

    # "MoveFolder" has subfolders for each test, and each test has subfolders DAS, HSV, DSD, and VICON
    # This script collects all files in the HSV subfolder for each test and moves them all into the same folder, target_folder

import os
import shutil

source_folder = r'C:\Users\james.caldwell\OneDrive - University of Virginia\Documents\2Python\MoveFolder' + '\\'
target_folder = r'C:\Users\james.caldwell\OneDrive - University of Virginia\Documents\2Python\MoveFolderGoal' + '\\'

move_or_copy = 'copy' #type 'move' or 'copy' here for move/copy of files

for path,dir,files in os.walk(source_folder):
    # print(path)
    if 'HSV' in path: #HSV - High Speed Video
        for file in files:
            #Naming format should be RunName_LFT.mcf
                #Sometimes, run name is missing

            if move_or_copy == 'move':
                os.rename(path + '\\' + file, target_folder + file)
            if move_or_copy == 'copy':
                shutil.copyfile(path + '\\' + file, target_folder + file)
            print(file + ' complete')

    # print(files)
    # if files:
    #     for file in files:
            