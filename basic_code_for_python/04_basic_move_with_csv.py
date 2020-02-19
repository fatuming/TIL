import os
import shutil
import csv


#csv path
csv_path = os.path.join('./', '.csv')

root_path = ''

save_path = '/'
os.makedirs(save_path)

df = open(csv_path, 'r')

read = csv.reader(df, delimiter=',')

for i, row in enumerate(read):
    barcode = row[0]
    dst = os.path.join(save_path, barcode)
    if not os.path.exists(dst):
        os.makedirs(dst)
    shutil.copy(os.path.join(root_path, row[1]), dst)
    
    
    
