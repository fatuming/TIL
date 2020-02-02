import os
import glob
import shutil

'''
copy file// choice folder structure
'''

#structure

###folder###
#---list---#

'''  
def copyFile():
    folderPath = './valid_images'
    file_name_array= sorted(os.listdir(folderPath))
    for f in file_name_array:
        original_filePath = os.path.join(folderPath, f)
        copyFolder = './data'
        if not os.path.exists(copyFolder):
            try:
                os.makedirs(copyFolder)
                #print 'create' + copyFolder
            except OSError as e:
                if e.errno != e.errno.EEXIST:
                    raise
        copy_filePath = os.path.join(copyFolder, f)
        shutil.copy(original_filePath, copy_filePath)         

copyFile()

'''




#structure

##folder#folder##
###list###list###

def copyFile():
    folderPath = './data'
    folder_array= sorted(os.listdir(folderPath))
    copyFolder = './test_data'
    if not os.path.exists(copyFolder):
        try:
            os.makedirs(copyFolder)
            #print 'create' + copyFolder
        except OSError as e:
            if e.errno != e.errno.EEXIST:
                raise
    
    for folder in folder_array:
        subfolderPath = os.path.join(folderPath, folder)
        file_array = sorted(os.listdir(subfolderPath))
        subcopyPath = os.path.join(copyFolder, folder)
        if not os.path.exists(subcopyPath):
            try:
                os.makedirs(subcopyPath)
                #print 'create' + copyFolder
            except OSError as e:
                if e.errno != e.errno.EEXIST:
                    raise

        for f in file_array:
            original_filePath = os.path.join(subfolderPath, f)
            copy_filePath = os.path.join(subcopyPath, f)
            shutil.copy(original_filePath, copy_filePath)         

copyFile()
