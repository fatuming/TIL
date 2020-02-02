import os
import glob

'''
rename file// first, choice folder structure and change file name(#change) what u want
'''


'''
#structure

###folder###
#---list---#

folderPath = './valid_images'
file_name_array= sorted(os.listdir(folderPath))


def rename():
    for f in file_name_array:
        #change name
        new_name = f.replace('.jpg','_.jpg') #change
        original_filePath = os.path.join(folderPath, f)
        new_filePath = os.path.join(folderPath, new_name)
        os.rename(original_filePath,new_filePath)

rename()
'''




#structure

##folder#folder##
###list###list###




def rename():
    folderPath = './data'
    folder_array = sorted(os.listdir(folderPath))
    for folder in folder_array:
        subfolderPath = os.path.join(folderPath, folder)
        file_array = sorted(os.listdir(subfolderPath))
        for f in file_array:
            original_filePath = os.path.join(subfolderPath, f)
            new_name = f.replace('.jpg','_.jpg') #change
            new_filePath = os.path.join(subfolderPath, new_name)
            os.rename(original_filePath,new_filePath)
rename()    
