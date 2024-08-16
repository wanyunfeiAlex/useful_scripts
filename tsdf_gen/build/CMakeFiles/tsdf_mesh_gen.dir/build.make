# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.26

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/wan/anaconda3/envs/py3_10/bin/cmake

# The command to remove a file.
RM = /home/wan/anaconda3/envs/py3_10/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/wan/work/MARS/dataset/LIVO2_SZB/scripts/tsdf_gen

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/wan/work/MARS/dataset/LIVO2_SZB/scripts/tsdf_gen/build

# Include any dependencies generated for this target.
include CMakeFiles/tsdf_mesh_gen.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/tsdf_mesh_gen.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/tsdf_mesh_gen.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/tsdf_mesh_gen.dir/flags.make

CMakeFiles/tsdf_mesh_gen.dir/main.cpp.o: CMakeFiles/tsdf_mesh_gen.dir/flags.make
CMakeFiles/tsdf_mesh_gen.dir/main.cpp.o: /home/wan/work/MARS/dataset/LIVO2_SZB/scripts/tsdf_gen/main.cpp
CMakeFiles/tsdf_mesh_gen.dir/main.cpp.o: CMakeFiles/tsdf_mesh_gen.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wan/work/MARS/dataset/LIVO2_SZB/scripts/tsdf_gen/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/tsdf_mesh_gen.dir/main.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/tsdf_mesh_gen.dir/main.cpp.o -MF CMakeFiles/tsdf_mesh_gen.dir/main.cpp.o.d -o CMakeFiles/tsdf_mesh_gen.dir/main.cpp.o -c /home/wan/work/MARS/dataset/LIVO2_SZB/scripts/tsdf_gen/main.cpp

CMakeFiles/tsdf_mesh_gen.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/tsdf_mesh_gen.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/wan/work/MARS/dataset/LIVO2_SZB/scripts/tsdf_gen/main.cpp > CMakeFiles/tsdf_mesh_gen.dir/main.cpp.i

CMakeFiles/tsdf_mesh_gen.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/tsdf_mesh_gen.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/wan/work/MARS/dataset/LIVO2_SZB/scripts/tsdf_gen/main.cpp -o CMakeFiles/tsdf_mesh_gen.dir/main.cpp.s

# Object files for target tsdf_mesh_gen
tsdf_mesh_gen_OBJECTS = \
"CMakeFiles/tsdf_mesh_gen.dir/main.cpp.o"

# External object files for target tsdf_mesh_gen
tsdf_mesh_gen_EXTERNAL_OBJECTS =

tsdf_mesh_gen: CMakeFiles/tsdf_mesh_gen.dir/main.cpp.o
tsdf_mesh_gen: CMakeFiles/tsdf_mesh_gen.dir/build.make
tsdf_mesh_gen: /usr/local/lib/libvdbfusion.a
tsdf_mesh_gen: /home/wan/work/MARS/third_party/open3d/install/lib/libOpen3D.so
tsdf_mesh_gen: /usr/local/lib/libopenvdb.so
tsdf_mesh_gen: /usr/lib/x86_64-linux-gnu/libboost_iostreams.so.1.74.0
tsdf_mesh_gen: /usr/lib/x86_64-linux-gnu/libtbb.so
tsdf_mesh_gen: CMakeFiles/tsdf_mesh_gen.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/wan/work/MARS/dataset/LIVO2_SZB/scripts/tsdf_gen/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable tsdf_mesh_gen"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/tsdf_mesh_gen.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/tsdf_mesh_gen.dir/build: tsdf_mesh_gen
.PHONY : CMakeFiles/tsdf_mesh_gen.dir/build

CMakeFiles/tsdf_mesh_gen.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/tsdf_mesh_gen.dir/cmake_clean.cmake
.PHONY : CMakeFiles/tsdf_mesh_gen.dir/clean

CMakeFiles/tsdf_mesh_gen.dir/depend:
	cd /home/wan/work/MARS/dataset/LIVO2_SZB/scripts/tsdf_gen/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wan/work/MARS/dataset/LIVO2_SZB/scripts/tsdf_gen /home/wan/work/MARS/dataset/LIVO2_SZB/scripts/tsdf_gen /home/wan/work/MARS/dataset/LIVO2_SZB/scripts/tsdf_gen/build /home/wan/work/MARS/dataset/LIVO2_SZB/scripts/tsdf_gen/build /home/wan/work/MARS/dataset/LIVO2_SZB/scripts/tsdf_gen/build/CMakeFiles/tsdf_mesh_gen.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/tsdf_mesh_gen.dir/depend

