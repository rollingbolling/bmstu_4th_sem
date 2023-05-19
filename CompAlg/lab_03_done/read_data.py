xIndex = 0
yIndex = 1
zIndex = 2
matrixIndex = 3

def read_table(filename):
    data_table = [[], [], [], []]
    new_z = 1
    z_cur_index = 0
    y_cur_index = 0
    flag_x = False
    flag_y = False
    with open(filename) as file:
        for line in file.readlines():
            row = line.split('\n')[0].split('\t')

            if 'z=' in row[0]:
                new_z = 1
                data_table[matrixIndex].append([])
                z_number = row[0].split('z=')[1]
                data_table[zIndex].append(float(z_number))
            elif "y\\x" in row[0]:
                if not flag_x:
                    for i in range(1, len(row)):
                        data_table[xIndex].append(float(row[i]))
                    flag_x = True
            else:
                if row[0] == '':
                    z_cur_index += 1
                    y_cur_index = 0
                    flag_y = True
                    continue

                if not flag_y:
                    data_table[yIndex].append(float(row[0]))


                data_table[matrixIndex][z_cur_index].append([])

                for i in range(1, len(row)):
                    data_table[matrixIndex][z_cur_index][y_cur_index].append(float(row[i]))

                y_cur_index += 1

    return data_table