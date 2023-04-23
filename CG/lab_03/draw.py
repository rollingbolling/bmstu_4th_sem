import time
from math import radians
# from method

def draw_line(canvas, x1, y1, x2, y2, colour):
    canvas.create_line(x1, y1, x2, y2, fill = colour)

def draw_specter(canvas, point_list):
    for point in point_list:
        canvas.create_line(point[0], point[1], point[0] + 1, fill = point[2])

def draw_specter_by_method(canvas, method, x1, y1, x2, y2, angle, colour, draw = True, intesive = False):
    total = 0
    steps = int(360//angle)
    for i in range(steps):
        if intesive:
            cur1 = time.time()
            point_list = method(canvas, x1, y1, x2, y2, colour)
            cur2 = time.time()
