import tkinter as tk
import tkinter.messagebox as mb
import config as cfg
import math as m

INFORMATION = "Функциональность программы"

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_x(self, x):
        self.x += (cfg.CONST_FIELD_W * x)
        return self.x

    def move_y(self, y):
        self.y += (cfg.CONST_FIELD_H * y)
        return self.y

def read_figure(name):
    figure_steps = [[], [], [], []]
    file = open(name)
    i = 0
    for line in file.readlines():
        if line == '\n':
            i += 1
        else:
            row = list(map(int, line.split(" ")))
            figure_steps[i].append(Point(row[0], row[1]))
    file.close()
    return figure_steps

def translate_to_field_coord(point):
    point.x += (cfg.WINDOW_W * cfg.BORDERS_MAIN_MAKE + 2 * cfg.BORDERS_SPACE)
    point.y += (-cfg.BORDERS_SPACE + cfg.FIELD_H)
    return point

def create_point(x, y):
    point = Point(x, y)
    return point

def get_figure():
    figure = [[], [], [], []]
    figure_steps = read_figure(cfg.FIGURE_FILE)
    point = Point()
    translate_to_field_coord(point)
    for i in range(len(figure_steps)):
        for step in range(len(figure_steps[i])):
            point.x = point.move_x(figure_steps[i][step].x)
            point.y = point.move_y(figure_steps[i][step].y)
            figure[i].append(create_point(point.x, point.y))
    return figure

figure_points = get_figure()

def draw_figure(field):
    global figure_points
    for i in range(len(figure_points)):
        for step in range(len(figure_points[i])):
            if step != 0:
                field.create_line(figure_points[i][step - 1].x, figure_points[i][step - 1].y, figure_points[i][step].x, figure_points[i][step].y)

def showInfoParams():
    mb.showinfo("Info", INFORMATION)

def add_point(point, center):
    point.x += center.x
    point.y += center.y

def sub_point(point, center):
    point.x -= center.x
    point.y -= center.y

def move_list(move_cof):
    global figure_points
    for part in figure_points:
        for point in part:
            point.x += move_cof[0]
            point.y += move_cof[1]
            
def scale_list(scale_cof, scale_center):
    global figure_points
    center = Point(scale_center[0], scale_center[1])
    translate_to_field_coord(center)
    for part in figure_points:
        for point in part:
            sub_point(point, center)
            point.x *= scale_cof[0]
            point.y *= scale_cof[1]
            add_point(point, center)

def rotate_list(rot_center, rot_angle):
    global figure_points
    center = Point(rot_center[0], rot_center[1])
    translate_to_field_coord(center)
    for part in figure_points:
        for point in part:
            sub_point(point, center)
            r_cos = m.cos(rot_angle * (m.pi / 180))
            r_sin = m.sin(rot_angle * (m.pi / 180))
            x = point.x
            y = point.y
            point.x = x * r_cos - y * r_sin
            point.y = x * r_sin + y * r_cos
            add_point(point, center)
