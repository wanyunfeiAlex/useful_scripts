import cv2 as cv
import numpy as np
import os
from tqdm import tqdm, trange

input_img_dir = "/home/wan/work/MARS/dataset/HK_island/HKisland/undistort/"
out_img_dir = "/home/wan/work/MARS/dataset/HK_island/HKisland/undist_downsample/"

# https://zhuanlan.zhihu.com/p/87185139

# cx' = s * cx - 0.5 * s + 0.5 : 313.456795 - 0.5 * 0.5 + 0.5 = 313.706795 
# cy' = s * cy - 0.5 * s + 0.5 : 261.399612 - 0.5 * 0.5 + 0.5 = 261.649612

all_imgs = os.listdir(input_img_dir)

print(len(all_imgs))

for img in tqdm(all_imgs):
    loaded_img = cv.imread(os.path.abspath(input_img_dir + img))
    down_img = cv.pyrDown(loaded_img)
    cv.imwrite(os.path.abspath(out_img_dir + img), down_img)
# undist_img = undist_img[y:y+h, x:x+w]


# newcameramtx LIVO2 retail
# [[640.661     0.      313.9261 ]
#  [  0.      640.8937  261.36517]
#  [  0.        0.        1.     ]]

# newcameramtx HK_island
# [[1.6103733e+03 0.0000000e+00 1.2071509e+03]
#  [0.0000000e+00 1.6127657e+03 1.0317281e+03]
#  [0.0000000e+00 0.0000000e+00 1.0000000e+00]]

