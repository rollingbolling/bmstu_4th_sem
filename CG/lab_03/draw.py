import time
from math import radians
from methodfuncs import turn_point

def draw_line_stand_algo(canvas, x1, y1, x2, y2, colour):
    canvas.create_line(x1, y1, x2, y2, fill = colour)

def draw_line_by_algo(canvas, point_list):
    for point in point_list:
        canvas.create_line(point[0], point[1], point[0] + 1, point[1], fill=point[2])

def draw_specter_by_algo(canvas, method, x1, y1, x2, y2, angle, colour, draw = True, intesive = False):
    total = 0
    steps = int(360//angle)
    for i in range(steps):
        if intesive:
            cur1 = time.time()
            point_list = method(canvas, x1, y1, x2, y2, colour)
            cur2 = time.time()
        else:
            cur1 = time.time()
            point_list = method(x1, y1, x2, y2, colour)
            cur2 = time.time()
        if draw:
            draw_line_by_algo(canvas, point_list)
        
        x2, y2 = turn_point(radians(angle), x2, y2, x1, y1)
        total += cur2 - cur1
        
    return total / (steps - 2)

def draw_specter_stand_algo(canvas, x1, y1, x2, y2, angle, colour):
    steps = int(360 // angle)
    for i in range(steps):
        draw_line_stand_algo(canvas, x1, y1, x2, y2, colour)
        x2, y2 = turn_point(radians(angle), x2, y2, x1, y1)
