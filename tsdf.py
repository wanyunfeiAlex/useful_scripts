import numpy as np
import open3d as o3d
import vdbfusion

class Dataset:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.n_scans = len(file_paths)

    def __len__(self) -> int:
        return self.n_scans

    def __getitem__(self, idx: int):
        # 从文件加载点云数据
        pcd = o3d.io.read_point_cloud(self.file_paths[idx])
        points = np.asarray(pcd.points)
        print(f"points dim : {points.shape} \n")
        origin = np.random.rand(3)  # 随机生成原点位置
        return points, origin

# 初始化参数
voxel_size = 0.05  # 体素大小
sdf_trunc = 0.03  # 符号距离场截断
space_carving = True  # 是否进行空间雕刻

# 创建 VDBVolume 实例
vdb_volume = vdbfusion.VDBVolume(voxel_size, sdf_trunc, space_carving)

# 创建 Dataset 实例，包括您提供的PCD文件路径
dataset = Dataset([
    "/home/wan/work/MARS/dataset/LIVO2_SZB/point_cloud/Scan_all.pcd"
])

# 遍历数据集，集成每个扫描
for scan, origin in dataset:
    # print(f"Processing scan {scan}")
    vdb_volume.integrate(scan, origin)

print("start to extract mesh11\n")
# 从 VDBVolume 提取三角网格
vert, tri = vdb_volume.extract_triangle_mesh()

print("start to create mesh\n")
# 使用 open3d 创建和可视化三角网格
mesh = o3d.geometry.TriangleMesh(
    o3d.utility.Vector3dVector(vert),
    o3d.utility.Vector3iVector(tri)
)

print("start to compute normals\n")
mesh.compute_vertex_normals()  # 计算顶点法线以改善渲染效果

print("start to save\n")
o3d.io.write_triangle_mesh("/home/wan/work/MARS/dataset/LIVO2_SZB/mesh/Scan_all_test_tsdf.ply", mesh)
# # o3d.visualization.draw_geometries([mesh])  # 可视化网格

