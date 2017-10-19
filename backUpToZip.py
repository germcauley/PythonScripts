# !python3

# Project Backup to Zip
# Copies a folder recursively into a zip file and names it incrementally.
# Zip is created in local directory(Where script is located)

import os
import zipfile


def backupToZip(folder):
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    #Create the zipfile
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in ' + foldername + '...')
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('Done')


backupToZip('/Users/gmcauley/Desktop/Phone')#Add path to folder you wish to backup here

'''Things to do:
-Modify script to only zip files with the .txt extension'''