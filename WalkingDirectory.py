#Automate the boring stuff with Python Chapter 9
#Script that searches a given directory and lists all the subfolders and files within
import os

for folderName, subfolders, filenames in os.walk('/Users/JoeBloggs/Desktop/FolderXYZ/'):#Add directory here
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
