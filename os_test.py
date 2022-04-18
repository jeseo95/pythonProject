import os
import glob

# print(os.getcwd())
# print(glob.glob('./*.py'))
for root, dirs, files in os.walk('C:\SEP'):
    print(dirs)
    # print(f'{dirs} : {files}')
