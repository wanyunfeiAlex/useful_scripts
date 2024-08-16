import cv2 as cv
import numpy as np
import os
from tqdm import tqdm, trange

input_img_dir = "/home/wan/work/MARS/dataset/HK_island/HKisland/images/"
out_img_dir = "/home/wan/work/MARS/dataset/HK_island/HKisland/undistort/"

imgW = 2448
imgH = 2048

# cam_width: 1280
# cam_height: 1024
# cam_fx: 1293.56944
# cam_fy: 1293.3155
# cam_cx: 626.91359
# cam_cy: 522.799224
# cam_d0: -0.076160
# cam_d1: 0.123001
# cam_d2: -0.00113
# cam_d3: 0.000251

# https://zhuanlan.zhihu.com/p/87185139

# cx' = s * cx - 0.5 * s + 0.5 : 313.456795 - 0.5 * 0.5 + 0.5 = 313.706795 
# cy' = s * cy - 0.5 * s + 0.5 : 261.399612 - 0.5 * 0.5 + 0.5 = 261.649612


intrinsic_mat = np.array([[1628.36, 0, 1203.43],
                 [0, 1627.74, 1031.77],
                 [0, 0, 1]], dtype=np.float32)
dist_coeff = np.array([-0.121, 0.1113, 0.0002, 0.00059], dtype=np.float32)
newcameramtx, roi = cv.getOptimalNewCameraMatrix(intrinsic_mat, dist_coeff, np.array([imgW, imgH]), 0)

all_imgs = os.listdir(input_img_dir)

print(len(all_imgs))

for img in tqdm(all_imgs):
    loaded_img = cv.imread(os.path.abspath(input_img_dir + img))
    undist_img = cv.undistort(loaded_img, intrinsic_mat, dist_coeff, None, newcameramtx)
    cv.imwrite(os.path.abspath(out_img_dir + img), undist_img)
x, y, w, h = roi
# undist_img = undist_img[y:y+h, x:x+w]


print(newcameramtx)
print(roi)

# newcameramtx LIVO2 retail
# [[640.661     0.      313.9261 ]
#  [  0.      640.8937  261.36517]
#  [  0.        0.        1.     ]]

# newcameramtx HK_island
# [[1.6103733e+03 0.0000000e+00 1.2071509e+03]
#  [0.0000000e+00 1.6127657e+03 1.0317281e+03]
#  [0.0000000e+00 0.0000000e+00 1.0000000e+00]]

