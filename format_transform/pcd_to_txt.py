import pcl.pcl_visualization

pc = pcl.load("/home/wan/work/MARS/dataset/LIVO2_SZB/my_colmap_dense_out/0/points3D.pcd")

points = pc.to_array()

print(len(points))

with open("/home/wan/work/MARS/dataset/LIVO2_SZB/my_colmap_dense_out/0/points3D.txt", "w") as f:
    for pt in points:
        f.write(f"{pt[0]} {pt[1]} {pt[2]}\n")
