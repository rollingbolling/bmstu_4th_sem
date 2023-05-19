from scipy.misc import derivative

def Newton_polynomial(table, n_degree, search_value, axis = 'x'):
    start_index, end_index = get_points_range_indexes(table, n_degree, search_value, axis=axis)
    newton_table = table[start_index:end_index + 1:1]

    differences_list = list()

    for index in range(len(newton_table)):
        if axis == 'x':
            differences_list.append(newton_divided_difference(newton_table, index))
        else:
            differences_list.append(newton_divided_difference(newton_table, index, axis='y'))

    polynomial = differences_list[0]

    for index in range(1, n_degree + 1):
        multiplication = 1
        for j_index in range(index):
            if axis == 'x':
                multiplication *= (search_value - newton_table[j_index].x)
            else:
                multiplication *= (search_value - newton_table[j_index].y)

        polynomial += multiplication * differences_list[index]

    return polynomial, differences_list, newton_table


def get_points_range_indexes(table, n_degree, search_value, axis = 'x'):
    end_index = -1

    for index in range(len(table)):
        if (axis == 'x' and table[index].x >= search_value) or (axis == 'y' and table[index].y >= search_value):
            end_index = index
            break

    if end_index == 0:
        end_index = 1
    elif end_index == -1:
        end_index == len(table) - 1

    start_index = end_index - 1

    if n_degree == 0:
        if axis == 'x':
            if abs(table[end_index].x - search_value) >= abs(table[start_index].x - search_value):
                end_index = start_index
            else:
                start_index = end_index
        else:
            if abs(table[end_index].y - search_value) >= abs(table[start_index].y - search_value):
                end_index = start_index
            else:
                start_index = end_index
    else:
        count_points = 0
        while (count_points != n_degree - 1):
            if (start_index - 1 >= 0):
                count_points += 1
                start_index -= 1
            if (count_points != n_degree - 1 and end_index + 1 < len(table)):
                count_points += 1
                end_index += 1

    return start_index, end_index

def newton_divided_difference(table, end_index, axis='x'):
    difference = 0

    for i in range(end_index + 1):
        multiplication = 1
        for j in range(end_index + 1):
            if i != j:
                if axis == 'x':
                    multiplication *= table[i].x - table[j].x
                else:
                    multiplication *= table[i].y - table[j].y

        if axis == 'x':
            difference += table[i].y / multiplication
        else:
            difference += table[i].x / multiplication

    return difference

def find_newton_polynom_derivative(table, n_degree, x_value):
    polynom, differences, newton_table = Newton_polynomial(table, n_degree, x_value)

    def aprox_func(x):
        result = 0
        x_res = 1
        for i in range(len(differences)):
            result += differences[i] * x_res
            x_res *= (x - newton_table[i].x)

        return result

    derivative_degree_2 = derivative(aprox_func, x_value, n=2, dx=1e-6)

    return derivative_degree_2


