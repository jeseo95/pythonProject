import os
import pandas as pd
import glob

# print(os.getcwd())
# print(glob.glob('./*.py'))

# -------------------------------------------------------------
# os.walk
# root: 탐색 중인 상위 폴더의 경로
# dirs: 탐색 중인 경로의 폴더 이름들
# files: 탐색 중인 경로의 파일 이름들
# -------------------------------------------------------------
import pandas as pd

for root, dirs, files in os.walk('C:\SEP'):
    for file in files:
        file_path = os.path.join(root, file)
        # print(file_path)
    # print(f'{dirs} : {files}')


# -------------------------------------------------------------
# dir_file
# input path : 탐색할 경로
# outpu df: 탐색 경로의 하위 폴더, 파일명 데이터 프레임
# -------------------------------------------------------------


def dir_file(path):

    df = pd.DataFrame(columns=['file_dir', 'file_nm'])
    for root, dirs, files in os.walk(path):
        for file in files:
            df = df.append({'file_dir': root, 'file_nm': file}, ignore_index=True)
    return df


df_test = dir_file('C:\SEP')
print(df_test.head())
print("-"*50)
print(df_test.tail())
