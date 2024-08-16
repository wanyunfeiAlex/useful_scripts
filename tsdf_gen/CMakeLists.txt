# MIT License
#
# # Copyright (c) 2022 Ignacio Vizzo, Cyrill Stachniss, University of Bonn
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

cmake_minimum_required(VERSION 3.10)
project(VDBFusion_Examples)

find_package(VDBFusion REQUIRED)

set(Open3D_DIR /home/wan/work/MARS/third_party/open3d/install/lib/cmake/Open3D/)
find_package(Open3D REQUIRED)
list(APPEND Open3D_LIBRARIES dl)
if (Open3D_FOUND)
    message(STATUS "Found Open3D ${Open3D_VERSION}")
    link_directories(${Open3D_LIBRARY_DIRS})
endif()


set(CMAKE_BUILD_TYPE Release)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Pull dependencies used only for the C++ examples
# include(3rdparty/find_dependencies.cmake)
# add_subdirectory(datasets)

add_executable(tsdf_mesh_gen main.cpp)
target_compile_features(tsdf_mesh_gen PUBLIC cxx_std_11)
target_link_libraries(tsdf_mesh_gen PRIVATE VDBFusion::vdbfusion ${Open3D_LIBRARIES})
# set_target_properties(tsdf_mesh_gen PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
