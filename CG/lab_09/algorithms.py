from config import *

def scalar_mul(a_vector, b_vector):
    return a_vector[0] * b_vector[0] + a_vector[1] * b_vector[1]

def get_vect(point_b, point_e):
    return [point_e[0] - point_b[0], point_e[1] - point_b[1]]

def get_vect_mul(a_vector, b_vector):
    return a_vector[0] * b_vector[1] - a_vector[1] * b_vector[0]

def check_convexity(clipper):
    if len(clipper) < 3:
        return False
    
    vect1 = get_vect(clipper[0], clipper[1])
    vect2 = get_vect(clipper[1], clipper[2])

    sign = None
    if get_vect_mul(vect1, vect2) > 0:
        sign = 1
    else:
        sign = -1

    for i in range(len(clipper)):
        vecti = get_vect(clipper[i-2], clipper[i-1])
        vectj = get_vect(clipper[i-1], clipper[i])
        if sign * get_vect_mul(vecti, vectj) < 0:
            return False
    
    if sign < 0:
        clipper.reverse()

    return True

def cyrus_beck_alg(canvas, clipper_figure, line, colour):
    pass
