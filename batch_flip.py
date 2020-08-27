import os
import re
from glob import glob
from pprint import pprint

import imageio
import numpy

#import the filename list

src_dir = "Z:/CTsao/4F_4legs_dual_LSM/kidney/20200813_kidney_ExM_7d_old_k15_NKCC2_568_same0812_CamA_bin4-4-1_bin2-2-1_bin2-2-1"

files = glob(os.path.join(src_dir, "*.tif"))

pprint(files)

#define create_folder and create new folder

def create_folder(directory):
    try:
        os.makedirs(directory)
    except FileExistsError:
        pass

dst_dir = f"{src_dir}_x_flip"
create_folder(dst_dir)

#flip and save images
data = []
for single_file in files:
    #read image using the filename list
    image = imageio.volread(single_file)
    
    #flipped image in x-direction
    image_flip = image[...,::-1]
    
    #flipped image name
    filename_split = single_file.split("\\")
    path = os.path.join(dst_dir, f"{filename_split[-1]}.tif")
    
    #save flipped image 
    future = imageio.volwrite(path, image_flip)
    data.append(future)

    print()