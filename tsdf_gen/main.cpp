#include <openvdb/openvdb.h>
#include <vdbfusion/VDBVolume.h>
#include <filesystem>
#include <fstream>
#include <string>

#include <Eigen/Dense>
#include <iostream>
#include <memory>


#include "open3d/Open3D.h"

namespace fs = std::filesystem;
using namespace open3d;


void PrintPointCloud(const open3d::geometry::PointCloud &pointcloud) {
    using namespace open3d;

    bool pointcloud_has_normal = pointcloud.HasNormals();
    utility::LogInfo("Pointcloud has %d points.",
                     (int)pointcloud.points_.size());

    Eigen::Vector3d min_bound = pointcloud.GetMinBound();
    Eigen::Vector3d max_bound = pointcloud.GetMaxBound();
    utility::LogInfo(
            "Bounding box is: ({:.4f}, {:.4f}, {:.4f}) - ({:.4f}, {:.4f}, "
            "{:.4f})",
            min_bound(0), min_bound(1), min_bound(2), max_bound(0),
            max_bound(1), max_bound(2));

    for (size_t i = 0; i < pointcloud.points_.size(); i++) {
        if (pointcloud_has_normal) {
            const Eigen::Vector3d &point = pointcloud.points_[i];
            const Eigen::Vector3d &normal = pointcloud.normals_[i];
            utility::LogInfo("{:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f}",
                             point(0), point(1), point(2), normal(0), normal(1),
                             normal(2));
        } else {
            const Eigen::Vector3d &point = pointcloud.points_[i];
            utility::LogInfo("{:.6f} {:.6f} {:.6f}", point(0), point(1),
                             point(2));
        }
    }
    utility::LogInfo("End of the list.");
}

void PrintHelp() {
    using namespace open3d;

    PrintOpen3DVersion();
    // clang-format off
    utility::LogInfo("Usage:");
    utility::LogInfo("    > PointCloud [pointcloud_filename]");
    // clang-format on
    utility::LogInfo("");
}

// int main(int argc, char *argv[]) {
//     using namespace open3d;

//     utility::SetVerbosityLevel(utility::VerbosityLevel::Debug);

//     if (argc != 2 ||
//         utility::ProgramOptionExistsAny(argc, argv, {"-h", "--help"})) {
//         PrintHelp();
//         return 1;
//     }

//     auto pcd = io::CreatePointCloudFromFile(argv[1]);
    

//     {
//         utility::ScopeTimer timer("Normal estimation with KNN20");
//         for (int i = 0; i < 20; i++) {
//             pcd->EstimateNormals(open3d::geometry::KDTreeSearchParamKNN(20));
//         }
//     }
//     std::cout << pcd->normals_[0] << std::endl;
//     std::cout << pcd->normals_[10] << std::endl;

//     {
//         utility::ScopeTimer timer("Normal estimation with Radius 0.01666");
//         for (int i = 0; i < 20; i++) {
//             pcd->EstimateNormals(
//                     open3d::geometry::KDTreeSearchParamRadius(0.01666));
//         }
//     }
//     std::cout << pcd->normals_[0] << std::endl;
//     std::cout << pcd->normals_[10] << std::endl;

//     {
//         utility::ScopeTimer timer("Normal estimation with Hybrid 0.01666, 60");
//         for (int i = 0; i < 20; i++) {
//             pcd->EstimateNormals(
//                     open3d::geometry::KDTreeSearchParamHybrid(0.01666, 60));
//         }
//     }
//     {
//         utility::ScopeTimer timer("FPFH estimation with Radius 0.25");
//         // for (int i = 0; i < 20; i++) {
//         pipelines::registration::ComputeFPFHFeature(
//                 *pcd, open3d::geometry::KDTreeSearchParamRadius(0.25));
//         //}
//     }
//     std::cout << pcd->normals_[0] << std::endl;
//     std::cout << pcd->normals_[10] << std::endl;

//     auto downpcd = pcd->VoxelDownSample(0.05);

//     // 1. test basic pointcloud functions.

    // geometry::PointCloud pointcloud;
//     PrintPointCloud(pointcloud);

//     pointcloud.points_.push_back(Eigen::Vector3d(0.0, 0.0, 0.0));
//     pointcloud.points_.push_back(Eigen::Vector3d(1.0, 0.0, 0.0));
//     pointcloud.points_.push_back(Eigen::Vector3d(0.0, 1.0, 0.0));
//     pointcloud.points_.push_back(Eigen::Vector3d(0.0, 0.0, 1.0));
//     PrintPointCloud(pointcloud);

//     // 2. test pointcloud IO.

//     const std::string filename_xyz("test.xyz");
//     const std::string filename_ply("test.ply");

//     if (io::ReadPointCloud(argv[1], pointcloud)) {
//         utility::LogInfo("Successfully read {}", argv[1]);

//         /*
//         geometry::PointCloud pointcloud_copy;
//         pointcloud_copy.CloneFrom(pointcloud);

//         if (io::WritePointCloud(filename_xyz, pointcloud)) {
//             utility::LogInfo("Successfully wrote {}",
//         filename_xyz.c_str()); } else { utility::LogError("Failed to write
//         {}", filename_xyz);
//         }

//         if (io::WritePointCloud(filename_ply, pointcloud_copy)) {
//             utility::LogInfo("Successfully wrote {}",
//         filename_ply); } else { utility::LogError("Failed to write
//         {}", filename_ply);
//         }
//          */
//     } else {
//         utility::LogWarning("Failed to read {}", argv[1]);
//     }

//     // 3. test pointcloud visualization

//     visualization::Visualizer visualizer;
//     std::shared_ptr<geometry::PointCloud> pointcloud_ptr(
//             new geometry::PointCloud);
//     *pointcloud_ptr = pointcloud;
//     pointcloud_ptr->NormalizeNormals();
//     auto bounding_box = pointcloud_ptr->GetAxisAlignedBoundingBox();

//     std::shared_ptr<geometry::PointCloud> pointcloud_transformed_ptr(
//             new geometry::PointCloud);
//     *pointcloud_transformed_ptr = *pointcloud_ptr;
//     Eigen::Matrix4d trans_to_origin = Eigen::Matrix4d::Identity();
//     trans_to_origin.block<3, 1>(0, 3) = bounding_box.GetCenter() * -1.0;
//     Eigen::Matrix4d transformation = Eigen::Matrix4d::Identity();
//     transformation.block<3, 3>(0, 0) = static_cast<Eigen::Matrix3d>(
//             Eigen::AngleAxisd(M_PI / 4.0, Eigen::Vector3d::UnitX()));
//     pointcloud_transformed_ptr->Transform(trans_to_origin.inverse() *
//                                           transformation * trans_to_origin);

//     visualizer.CreateVisualizerWindow("Open3D", 1600, 900);
//     visualizer.AddGeometry(pointcloud_ptr);
//     visualizer.AddGeometry(pointcloud_transformed_ptr);
//     visualizer.Run();
//     visualizer.DestroyVisualizerWindow();

//     // 4. test operations
//     *pointcloud_transformed_ptr += *pointcloud_ptr;
//     visualization::DrawGeometries({pointcloud_transformed_ptr},
//                                   "Combined Pointcloud");

//     // 5. test downsample
//     auto downsampled = pointcloud_ptr->VoxelDownSample(0.05);
//     visualization::DrawGeometries({downsampled}, "Down Sampled Pointcloud");

//     // 6. test normal estimation
//     visualization::DrawGeometriesWithKeyCallbacks(
//             {pointcloud_ptr},
//             {{GLFW_KEY_SPACE,
//               [&](visualization::Visualizer *vis) {
//                   // EstimateNormals(*pointcloud_ptr,
//                   //        open3d::KDTreeSearchParamKNN(20));
//                   pointcloud_ptr->EstimateNormals(
//                           open3d::geometry::KDTreeSearchParamRadius(0.05));
//                   utility::LogInfo("Done.");
//                   return true;
//               }}},
//             "Press Space to Estimate Normal", 1600, 900);

//     // n. test end

//     utility::LogInfo("End of the test.");
//     return 0;
// }

int main(int argc, char* argv[])
{
    openvdb::initialize();

    float voxelSize = 0.05;
    float sdfTrunc = 0.3;
    bool spaceCarving = true;

    // fmt::print("Integrating {} scans\n", dataset.size());
    vdbfusion::VDBVolume tsdf_volume(voxelSize, sdfTrunc, spaceCarving);

    geometry::PointCloud pointcloud;
    if (io::ReadPointCloud(argv[1], pointcloud)) {
        utility::LogInfo("Successfully read {}", argv[1]);
        utility::LogInfo("read points num :{}", pointcloud.points_.size());
    } else {
        utility::LogWarning("Failed to read {}", argv[1]);
    }

    std::random_device rd;  // 获取随机数种子
    std::mt19937 gen(rd()); // Mersenne Twister 生成器
    std::uniform_real_distribution<double> dis(0.0, 1.0); // 均匀分布 (0, 1)

    Eigen::Vector3d origin;
    for (int i = 0; i < 3; ++i) {
        origin[i] = dis(gen); // 每个元素随机采样
    }

    utility::LogInfo("start to call tsdf_volume.Integrate\n");
    tsdf_volume.Integrate(pointcloud.points_, origin, [](float /*unused*/) { return 1.0; });

    utility::LogInfo("start to call ExtractTriangleMesh\n");
    auto [vertices, triangles] = tsdf_volume.ExtractTriangleMesh(true, -20.0);

    utility::LogInfo("start to call ComputeVertexNormals\n");
    auto mesh = open3d::geometry::TriangleMesh(vertices, triangles);
    mesh.ComputeVertexNormals();

    utility::LogInfo("start to call DrawGeometries\n");

    // std::shared_ptr<geometry::TriangleMesh> mesh_ptr(new geometry::TriangleMesh);
    // *mesh_ptr = mesh;

    // std::vector<std::shared_ptr<const geometry::Geometry>> input;
    // input.push_back(mesh_ptr);
    // open3d::visualization::DrawGeometries(input);

    utility::LogInfo("start to save mesh\n");

    open3d::io::WriteTriangleMeshToPLY(argv[2], mesh, false, false, false, false, false, true);


    return 0;
}