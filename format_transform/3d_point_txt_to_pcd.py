import collections
import os
import struct

import numpy as np

def write_pcd(points, output_file):
    with open(output_file, 'w') as f:
        f.write("# .PCD v0.7 - Point Cloud Data file format\n")
        f.write("VERSION 0.7\n")
        f.write("FIELDS x y z\n")
        f.write("SIZE 4 4 4\n")
        f.write("TYPE F F F\n")
        f.write("COUNT 1 1 1\n")
        f.write("WIDTH {}\n".format(len(points)))
        f.write("HEIGHT 1\n")
        f.write("VIEWPOINT 0 0 0 1 0 0 0\n")
        f.write("POINTS {}\n".format(len(points)))
        f.write("DATA ascii\n")

        for point in points:
            # r, g, b = point['rgb']
            # rgb_value = (r << 16) | (g << 8) | b  # 转换为 RGB 整数
            f.write(f"{point[0]} {point[1]} {point[2]}\n")

def read_3d_pts_txt(file_path):
    xyz_all = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if (line[0] == '/'):
                continue

            if (len(line.split()) != 6):
                continue
    
            xyz = line.split()
            xyz_all.append([xyz[0], xyz[1], xyz[2]])

    return xyz_all
        


if __name__=='__main__':
    bin_path = "/home/wan/work/MARS/dataset/LIVO2_SZB/point_cloud/points3D_manual_clean.txt"
    out_pcd_path = "/home/wan/work/MARS/dataset/LIVO2_SZB/point_cloud/points3D_manual_clean.pcd"
    points3D = read_3d_pts_txt(bin_path)

    print(f"points3D len : {len(points3D)}")

    write_pcd(points3D, out_pcd_path)
