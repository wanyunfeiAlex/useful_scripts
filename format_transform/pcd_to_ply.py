# import pcl.pcl_visualization
# # import pcl

# pc = pcl.load("/home/wan/work/MARS/dataset/LIVO2_SZB/point_cloud/Scan_all.pcd")

# points = pc.to_array()

# cloud = pcl.PointCloud()
# cloud.from_array(points)

# cloud.to_file(b"/home/wan/work/MARS/dataset/LIVO2_SZB/point_cloud/Scan_all.ply")

# # pcl.io.savePLYFile("/home/wan/work/MARS/dataset/LIVO2_SZB/point_cloud/Scan_all.ply", cloud)

# print(len(points))

import open3d as o3d
print("Testing IO for point cloud ...")
pcd = o3d.io.read_point_cloud("/home/wan/work/MARS/dataset/LIVO2_SZB/point_cloud/Scan_all.pcd")
# print(pcd)
o3d.io.write_point_cloud("/home/wan/work/MARS/dataset/LIVO2_SZB/point_cloud/Scan_all.ply", pcd)
