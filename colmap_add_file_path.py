import os

path_prefix = "/home/wan/work/MARS/dataset/LIVO2_SZB/undistorted/"
out_path = "/home/wan/work/MARS/dataset/scripts/out/test.txt"

with open("/home/wan/work/MARS/dataset/LIVO2_SZB/my_colmap_out_txt/images.txt", "r") as f:
    lines = f.readlines()

    new_lines = []

    for line in lines:
        if (line[0] == "#"):
            new_lines.append(line)
            continue

        if (line.split()[-1].split('.')[-1] != "png"):
            new_lines.append(line)
            continue

        file_name = line.split()[-1]

        # line = file_name

        full_path = " " + path_prefix + file_name + "\n"

        new_lines.append(line.rsplit(" ", 1)[0] + full_path)        

    with open(out_path, 'w') as out:
        for l in new_lines:
            out.write(l)





