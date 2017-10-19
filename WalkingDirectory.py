#Script that searches a given directory and lists all the subfolders and files within
import os

for folderName, subfolders, filenames in os.walk('/Users/gmcauley/Desktop/Code/'):#Add your directory path here
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')