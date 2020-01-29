import os

filePath = "/home/seobuntu/Desktop/Python/003_Hanhwa/xmls"
Files = os.listdir(filePath)




def checkFileSize():

    #change your target size (bytes)
    targetSize = 350

    for x in Files:
        finalPath = filePath + "/" + str(x)
        a = os.path.getsize(finalPath)
            if a < targetSize :
                print("please check:"+finalPath+ "\t"+ "size:" + str(a))
