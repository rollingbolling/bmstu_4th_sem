from Point import *

from tkinter import Tk, Canvas, Label, Entry, Button, messagebox, Listbox, LAST

window = Tk()
WINDOW_W = window.winfo_screenwidth()
WINDOW_H = window.winfo_screenheight() - 70
AXIS_SPACE = 10

CANVAS_X = WINDOW_W
CANVAS_Y = WINDOW_H - 120

numb_points = 0
point_list = []

def task():
    messagebox.showinfo("Условие задачи", 
                        "На плоскости дано множество точек.\n"
                        "Определить радиусы и центры двух окружностей, проходящих,\n"
                        "по крайней мере , через четыре различные точки заданного множества,\n"
                        "\n")

def transform_origin_x(x):
    return x * (x_max - x_min) / CANVAS_X - x_min

def tranform_origin_y(y):
    return -(y * (y_max - y_min) / CANVAS_Y - y_max)

def draw_axis():
    for i in range(0, CANVAS_Y, 50):
        canvas.create_line(7, CANVAS_Y - i - AXIS_SPACE, 13, CANVAS_Y - i - AXIS_SPACE, width=2)
        if i != 0:
            canvas.create_text(25, CANVAS_Y - i - AXIS_SPACE, text=str(round(tranform_origin_y(CANVAS_Y - i - AXIS_SPACE), 2)))

    for i in range(0, CANVAS_X, 50):
        canvas.create_line(i + AXIS_SPACE, CANVAS_Y - 13, i + AXIS_SPACE, CANVAS_Y - 7, width=2)
        if i != 0:
            canvas.create_text(i + AXIS_SPACE, CANVAS_Y - AXIS_SPACE - 10, text=str(round(transform_origin_x(i + AXIS_SPACE), 2)))

    canvas.create_line(0, CANVAS_Y - AXIS_SPACE, CANVAS_X, CANVAS_Y - AXIS_SPACE, width=2, arrow=LAST)
    canvas.create_line(AXIS_SPACE, CANVAS_Y, AXIS_SPACE, 0, width=2, arrow=LAST)
    
    
def clear_canvas_field():
    global numb_points
    # global flag_find_circle

    # canvas.delete()


if __name__ == "__main__":
    CORRECT = 1
    MISTAKE = 0
    color_points = "purple"
    kx_space = 1.01
    ky_space = 1.02

    x_min = 0
    x_max = 20
    y_min = 0
    y_max = 10

    x_c = (x_min + x_max) / 2
    x_min = x_c - (x_c - x_min) * kx_space
    x_max = x_c + (x_max - x_c) * kx_space

    y_c = (y_min + y_max) / 2
    y_min = y_c - (y_c - y_min) * ky_space
    y_max = y_c + (y_max - y_c) * ky_space

    flag_found_circle = False
    
    window.title("Lab №1")
    window.geometry("%dx%d" % (WINDOW_W, WINDOW_H))
    window.resizable(True, True)

    canvas = Canvas(window, width=CANVAS_X, height=CANVAS_Y, bg="lightblue")
    canvas.place(x=0, y=120)

    draw_axis()

    Label(window, text="X: ", font=("Times New Roman", 18)).place(width=60, height=40, x=10, y=15)
    x_point_txt = Entry(window, font=("Times New Roman", 13))
    x_point_txt.place(width=50, height=40, x=50, y=15)

    Label(window, text="Y: ", font=("Times New Roman", 18)).place(width=60, height=40, x=10, y=70)
    y_point_txt = Entry(window, font=("Times New Roman", 13))
    y_point_txt.place(width=50, height=40, x=50, y=70)

    window.mainloop()
