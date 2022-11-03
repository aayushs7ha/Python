# Initialize the directory
from genericpath import isfile
import os
dir_path = r'C:\\Users\\sinha.ttl\\Downloads\\Tata Service Stations'
# Initialize counter variable
count = 0 
# Iterate over files in the directory
for path in os.listdir(dir_path):
    #check if the files are in the assigned path / directory
    if os.path.isfile(os.path.join(dir_path,path)):
        count += 1
print('File Count :', count)
    