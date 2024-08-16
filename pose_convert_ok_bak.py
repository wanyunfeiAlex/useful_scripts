import numpy as np
from scipy.spatial.transform import Rotation as R

input_file_path = "/Users/moyunfei/Downloads/work/LIVO2_pose/nerf.txt"
output_file_path = "/Users/moyunfei/Downloads/work/LIVO2_pose/w2c_pose.txt"


def quaternion2rot(quaternion):
    r = R.from_quat(quaternion, scalar_first=True)
    rot = r.as_matrix()
    return rot

poses = []
# qw qx qy qz
quat = []
rotations = []
with open(input_file_path, "r") as f:
    lines = f.readlines()
    
    for line in lines:
        poses.append(line.split()[-3:])
        rotations.append(quaternion2rot(line.split()[1:5]))
    # print(data[0].split()[-1])
# print(quat[-1])

# print(rotations[0])


w2c_pos = []
for rot, pos in zip(rotations, poses):
    se3 = np.eye(4)
    se3[:3, 3] = pos
    se3[:3, :3] = rot
    se3 = np.linalg.inv(se3)
    xyz = se3[:3, 3]
    w2c_pos.append(xyz)
    # np_pos_vec = np.transpose(np.array([float(pos[0]), float(pos[1]), float(pos[2])]))
    # np_rot_mat = np.array(rot)
    
    # np.linalg.inv

    # w2c_pos.append(np.matmul((np_rot_mat), np_pos_vec))

    # print((np_rot_mat))
    # print((np_pos_vec))
    
    # print(np.matmul(np.linalg.inv(np_rot_mat), np_pos_vec))
    # exit()
    # rotations.
print(len(w2c_pos))

with open("/Users/moyunfei/Downloads/work/LIVO2_pose/w2c_pose_lyf_scaler.txt", "w") as f:
    for p in w2c_pos:
        f.write(f"{p[0]} {p[1]} {p[2]}\n")




# print((quaternion2rot(quat[0])))

