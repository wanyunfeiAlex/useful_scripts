import numpy as np
from scipy.spatial.transform import Rotation as R

input_file_path = "/home/wan/work/MARS/dataset/HK_island/HKisland/pose/nerf.txt"
output_file_path = "/home/wan/work/MARS/dataset/HK_island/HKisland/pose/nerf_w2c.txt"


# mat_test = np.array([[1, 2, 3], [4, 6, 8]])
# print(f"mat_test : (1, 2) {mat_test[1][2]} \n")
# exit()



def quaternion2rot(quaternion):
    r = R.from_quat(quaternion, scalar_first=True)
    rot = r.as_matrix()
    return rot

poses = []
# qw qx qy qz x y z
rotations = []
img_names = []
with open(input_file_path, "r") as f:
    lines = f.readlines()

    for line in lines:
        if (len(line)) < 10:
            continue

        if (len(line.split()) != 8):
            continue

        if (line[0] == "#"):
            continue
    
        poses.append(line.split()[5:])
        rotations.append(quaternion2rot(line.split()[1:5]))
        img_names.append(line.split()[0])
    # print(data[0].split()[-1])
# print(quat[-1])

# print(rotations[0])


w2c_pos = []
for rot, pos in zip(rotations, poses):
    se3 = np.eye(4)
    se3[:3, 3] = pos
    se3[:3, :3] = rot
    se3 = np.linalg.inv(se3)
    # xyz = se3[:3, 3]
    w2c_pos.append([se3[0][0], se3[0][1], se3[0][2], se3[0][3],\
                    se3[1][0], se3[1][1], se3[1][2], se3[1][3],\
                    se3[2][0], se3[2][1], se3[2][2], se3[2][3],\
                    se3[3][0], se3[3][1], se3[3][2], se3[3][3],])


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

with open(output_file_path, "w") as f:
    for i in range(len(w2c_pos)):
        # f.write(f"{p[0]} {p[1]} {p[2]}\n")
        f.write(f"{img_names[i]} {w2c_pos[i][0]} {w2c_pos[i][1]} {w2c_pos[i][2]} {w2c_pos[i][3]} {w2c_pos[i][4]} {w2c_pos[i][5]} {w2c_pos[i][6]} {w2c_pos[i][7]} {w2c_pos[i][8]} {w2c_pos[i][9]} {w2c_pos[i][10]} {w2c_pos[i][11]} {w2c_pos[i][12]} {w2c_pos[i][13]} {w2c_pos[i][14]} {w2c_pos[i][15]}\n")
        # exit()




# print((quaternion2rot(quat[0])))

