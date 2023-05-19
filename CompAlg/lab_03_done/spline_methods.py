def spline(table, value, start_x_derivative, end_x_derivative):
    x_value_list = [point.x for point in table]
    y_value_list = [point.y for point in table]

    index = find_index(x_value_list, value)
    coefs = calculate_coefficients(x_value_list, y_value_list, start_x_derivative, end_x_derivative)

    result = count_polynom(x_value_list, coefs, index, value)

    return result, coefs, index

def print_spline_polynom(x, y, x_i, index, coefs):
    print(f'x = {x:.6g}')
    print(f'Ф(х) = {coefs[0][index]:.6g}', end = ' ')

    for i in range(1, len(coefs)):
        print(f'+ {coefs[i][index]:.6g} * (x - {x_i:.6g})^{i}', end=' ')

    print(f'= {y:6g}', end='\n\n')

def count_polynom(x_value_list, coefs, index, value):
    result = 0
    h = value - x_value_list[index]
    for i in range(4):
        result += coefs[i][index] * (h ** i)

    return result

def find_index(x_value_list, value):
    index = 1
    size = len(x_value_list)

    while index < size and x_value_list[index] < value:
        index += 1

    return index - 1

def calculate_coefficients(x_value_list, y_value_list, start_x_derivative, end_x_derivative):
    a_coef = get_A_coefficients(y_value_list)
    c_coef = get_C_coefficients(x_value_list, y_value_list, start_x_derivative, end_x_derivative)
    b_coef = get_B_coefficients(x_value_list, y_value_list, c_coef)
    d_coef = get_D_coefficients(x_value_list, c_coef)

    return a_coef, b_coef, c_coef, d_coef

def get_A_coefficients(y_value_list):
    a_list = list()

    for i in range(len(y_value_list)):
        a_list.append(y_value_list[i])

    return a_list

def get_B_coefficients(x_value_list, y_value_list, c_value_list):
    b_value_list = list()

    for i in range(1, len(x_value_list) - 1):
        h = x_value_list[i] - x_value_list[i - 1]

        b_value_list.append(get_B(y_value_list[i - 1], y_value_list[i], c_value_list[i - 1], c_value_list[i], h))

    h = x_value_list[-1] - x_value_list[-2]
    b_value_list.append(get_B(y_value_list[-2], y_value_list[-1], 0, c_value_list[-1], h))

    return b_value_list

def get_B(y1, y2, c1, c2, h):
    return (y2 - y1) / h - h * (c2 + 2 * c1) / 3

def get_D_coefficients(x_value_list, c_value_list):
    d_value_list = list()

    for i in range(1, len(x_value_list) - 1):
        h = x_value_list[i] - x_value_list[i - 1]
        d_value_list.append(get_D(c_value_list[i - 1], c_value_list[i], h))

    h = x_value_list[-1] - x_value_list[-2]
    d_value_list.append(get_D(c_value_list[-1], 0, h))

    return d_value_list

def get_D(c1, c2, h):
    return (c2 - c1) / (3 * h)

def get_H_coefficients(x_value_list):
    h_value_list = list()

    for i in range(1, len(x_value_list)):
        h_value_list.append(x_value_list[i] - x_value_list[i - 1])

    return h_value_list

def get_C_coefficients(x_value_list, y_value_list, start_x_derivative, end_x_derivative):
    c_value_list = [0] * (len(x_value_list) - 1)
    c_value_list[0] = start_x_derivative
    c_value_list[1] = end_x_derivative

    if start_x_derivative == 0 and end_x_derivative == 0:
        ksi_value_list = [0, 0]
        theta_value_list = [0, 0]
    elif start_x_derivative == 0:
        ksi_value_list = [0, end_x_derivative / 2]
        theta_value_list = [0, end_x_derivative / 2]
    else:
        ksi_value_list = [start_x_derivative / 2, end_x_derivative / 2]
        theta_value_list = [start_x_derivative / 2, end_x_derivative / 2]

    for i in range(2, len(x_value_list)):
        h1 = x_value_list[i - 1] - x_value_list[i - 2]
        h2 = x_value_list[i] - x_value_list[i - 1]

        ksi_cur = get_ksi(ksi_value_list[-1], h1, h2)
        fi_cur = get_Fi(y_value_list[i - 2], y_value_list[i - 1], y_value_list[i], h1, h2)
        theta_cur = get_theta(theta_value_list[-1], fi_cur, h1, h2, ksi_value_list[-1])

        ksi_value_list.append(ksi_cur)
        theta_value_list.append(theta_cur)

    c_value_list[-1] = theta_value_list[-1]

    for i in range(len(x_value_list) - 2, 0, -1):
        c_value_list[i - 1] = get_C(c_value_list[i], ksi_value_list[i], theta_value_list[i])

    return c_value_list


def get_Fi(y1, y2, y3, h1, h2):
    return 3 * ((y3 - y2) / h2 - (y2 - y1) / h1)

def get_theta(old_theta, f_i, h1, h2, ksi):
    return (f_i - h1 * old_theta) / ((ksi * h1) + 2 * (h1 + h2))

def get_ksi(old_ksi, h1, h2):
    return -1 * h2 / (h1 * old_ksi + 2 * (h1 + h2))

def get_C(next_c, ksi, theta):
    return ksi * next_c + theta
