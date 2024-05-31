import os
import shutil
from tqdm import tqdm

Raw_DIR = r"dataset"

for dirpath, dirname, filenames in os.walk(Raw_DIR):
    for i in tqdm([f for f in filenames if f.endswith('.png')]):
        if i.split('_')[4] == '0':
            shutil.copy(src=os.path.join(dirpath, i), dst=r"dataset/train/Closed")
        elif i.split('_')[4] == '1':
            shutil.copy(src=os.path.join(dirpath, i), dst="dataset/train/Open")
