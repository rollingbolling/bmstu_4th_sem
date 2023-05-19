from polynomial_methods import Newton_polynomial
from spline_methods import spline
from point import Point
from read_data import xIndex, yIndex, zIndex, matrixIndex

NEWTON = 1
SPLINE = 2

def multi_interpolation(data, nx=0, ny=0, nz=0, x_search=0, y_search=0, z_search=0, x_direction=NEWTON, y_direction=NEWTON, z_direction=NEWTON):
    x_array = data[xIndex]
    y_array = data[yIndex]
    z_array = data[zIndex]
    matrix = data[matrixIndex]

    xy_from_u = []

    for i in range(len(x_array)):
        xy_from_u.append([])
        for j in range(len(y_array)):
            z_from_u_matrix = []
            for z in range(len(z_array)):
                z_from_u_matrix.append(Point(z_array[z], matrix[z][j][i], 0))

            u = 0
            if z_direction == NEWTON:
                u = Newton_polynomial(z_from_u_matrix, nz, z_search)[0]
            elif z_direction == SPLINE:
                u = spline(z_from_u_matrix, z_search, 0, 0)[0]

            xy_from_u[i].append(Point(y_array[j], u, 0))

    x_from_u_array = []
    for i in range(len(x_array)):
        u = 0

        if y_direction == NEWTON:
            u = Newton_polynomial(xy_from_u[i], ny, y_search)[0]
        elif y_direction == SPLINE:
            u = spline(xy_from_u[i], y_search, 0, 0)[0]

        x_from_u_array.append(Point(x_array[i], u, 0))

    result = 0
    

    if x_direction == NEWTON:
        result = Newton_polynomial(x_from_u_array, nx, x_search)[0]
    elif x_direction == SPLINE:
        result = spline(x_from_u_array, x_search, 0, 0)[0]

    return result