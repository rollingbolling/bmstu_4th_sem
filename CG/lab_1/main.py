from Point import *
from circle_funcs import *
from tkinter import Tk, Canvas, Label, Entry, Button, messagebox, Listbox, LAST

window = Tk()
WINDOW_W = window.winfo_screenwidth() 
WINDOW_H = window.winfo_screenheight() - 70
AXIS_SPACE = 10

CANVAS_X = WINDOW_W
CANVAS_Y = WINDOW_H - 120

numb_points = 0
point_list = []

def translate_to_can_sys(x, y):
    return transform_x(x), transform_y(y)

def point_not_enter():
    messagebox.showwarning("Warning!", "Координаты точки не введены!")

def number_not_enter():
    messagebox.showwarning("Warning!", "Точка для удаления не введена!")

def point_not_exist():
    messagebox.showwarning("Warning!", "Введенная точка не существует!")

def point_is_exist():
    messagebox.showwarning("Warning!", "Введенная точка уже существует!")

def task():
    messagebox.showinfo("Условие задачи", "На плоскости дано множество точек. Определить радиусы и центры двух окружностей, \n"
                        "проходящих, по крайней мере , через четыре различные точки заданного множества, которые содержат\n" 
                        "внутри наибольшее кол-во точек этого множества, притом площадь их пересечения максимальна.")

def translate_from_can_sys(x, y):
    return transform_origin_x(x), transform_origin_y(y)

def transform_origin_x(x):
    return x * (x_max - x_min) / CANVAS_X - x_min

def transform_origin_y(y):
    return -(y * (y_max - y_min) / CANVAS_Y - y_max)

def transform_x(x):
    return (x - x_min) / (x_max - x_min) * CANVAS_X

def transform_y(y):
    return (y_max - y) / (y_max - y_min) * CANVAS_Y

def draw_axis():
    for i in range(0, CANVAS_Y, 50):
        canvas.create_line(7, CANVAS_Y - i - AXIS_SPACE, 13, CANVAS_Y - i - AXIS_SPACE, width=2)
        if i != 0:
            canvas.create_text(25, CANVAS_Y - i - AXIS_SPACE, text=str(round(transform_origin_y(CANVAS_Y - i - AXIS_SPACE), 2)))

    for i in range(0, CANVAS_X, 50):
        canvas.create_line(i + AXIS_SPACE, CANVAS_Y - 13, i + AXIS_SPACE, CANVAS_Y - 7, width=2)
        if i != 0:
            canvas.create_text(i + AXIS_SPACE, CANVAS_Y - AXIS_SPACE - 10, text=str(round(transform_origin_x(i + AXIS_SPACE), 2)))

    canvas.create_line(0, CANVAS_Y - AXIS_SPACE, CANVAS_X, CANVAS_Y - AXIS_SPACE, width=2, arrow=LAST)
    canvas.create_line(AXIS_SPACE, CANVAS_Y, AXIS_SPACE, 0, width=2, arrow=LAST)

def draw_point(x, y, name, color):
    xp, yp = transform_x(x), transform_y(y)
    coor = str(name) + ".(" + str(round(x, 2)) + ";" + str(round(y, 2)) + ")"
    canvas.create_oval(xp - 2, yp - 2, xp + 2, yp + 2, fill=color, outline=color, width=2)
    canvas.create_text(xp + 5, yp - 10, text=coor, fill=color, font=("Times New Roman", 10))

def clear_fields(field):
    string = field.get()
    len_str = len(string)
    while len_str >= 1:
        field.delete(len_str - 1)
        len_str -= 1

def add_point():
    global numb_points, flag_found_circles, area_inter, amount_points

    x_text = x_point_txt.get()
    y_text = y_point_txt.get()

    if x_text == "" or y_text == "":
        point_not_enter()
    else:
        try:
            x, y = float(x_text), float(y_text)
            flag = False
            for p in point_list:
                flag = p.equal_points(x, y)
                if flag:
                    break
            if point_list == [] or (not flag):
                if flag_found_circles == True:
                    canvas.delete("all")
                    draw_axis()
                    flag_found_circles = False
                    area_inter = -1
                    amount_points = -1
                    for i in range(0, len(point_list)):
                        draw_point(point_list[i].x, point_list[i].y, i + 1, color_points_add)
                point_list.append(Point(x, y))
                scroll_menu.insert(numb_points, str(numb_points + 1) + ".(" + str(round(x, 2)) + ";" + str(round(y, 2)) + ")")
                numb_points += 1
                draw_point(x, y, numb_points, color_points_add)
                clear_fields(del_point_txt)
                del_point_txt.insert(0, numb_points)
            else:
                point_is_exist()
        except:
            messagebox.showwarning("Warning!", "Введены недопустимые символы")
        clear_fields(x_point_txt)
        clear_fields(y_point_txt)

def del_point():
    global numb_points, flag_found_circles, area_inter, amount_points

    del_text = del_point_txt.get()
    if del_text == "":
        number_not_enter()
    else:
        try:
            index_del = int(del_text) - 1
            if index_del >= len(point_list) or index_del < 0:
                point_not_exist()
                
            elif numb_points != 0:
                canvas.delete("all")
                draw_axis()
                point_list.pop(index_del)

                for i in range(0, len(point_list)):
                    draw_point(point_list[i].x, point_list[i].y, i + 1, color_points_add)
                
                scroll_menu.delete(index_del)
                clear_fields(del_point_txt)
                numb_points -= 1
                if numb_points != 0:
                    del_point_txt.insert(0, numb_points)

                if index_del == numb_points:
                    scroll_menu.delete(index_del)
                else:
                    scroll_menu.delete(index_del, scroll_menu.size() - 1)
                    for i in range(index_del, len(point_list)):
                        x, y = point_list[i].x, point_list[i].y
                        scroll_menu.insert(i, str(i + 1) + ".(" + str(round(x, 2)) + ";" + str(round(y, 2)) + ")")
        
                flag_found_circles = False
                area_inter = -1
                amount_points = -1
        except:
            number_not_enter()
    
def draw_circle(center, rad):
    x1, y1 = center.x, center.y
    x1, x2, y1, y2 = x1-rad, x1+rad, (y1+rad), (y1-rad)
    
    x1, y1 = translate_to_can_sys(x1, y1)
    x2, y2 = translate_to_can_sys(x2, y2)
    canvas.create_oval(x1, y1, x2, y2, outline="green", width=2)

def all_points_on_one_line():
    amount = len(point_list)
    for i in range(amount - 2):
        for j in range(i + 1, amount - 1):
            for k in range(j + 1, amount):
                if points_on_one_line(point_list[i], point_list[j], point_list[k]) == CORRECT:
                    return CORRECT
    return MISTAKE

def find_circle():
    global numb_points, amount_points, area_inter, flag_found_circles
    global circle_1, circle_2, radius_1, radius_2
    amount = len(point_list)
    circles_list = []
    if not point_list or numb_points < 4:
        messagebox.showwarning("Error", "Введено недостаточно точек\nВведите четыре точки")
        return
    if all_points_on_one_line() == MISTAKE:
        messagebox.showwarning("Error", "Невозможно построить окружность на заданных точках\nВведите четыре точки")
        return
    if flag_found_circles:
        canvas.delete("all")
        draw_axis()
        if point_list:
            for i in range(0, amount):
                draw_point(point_list[i].x, point_list[i].y, i + 1, color_points_add)
        flag_found_circles = False
    for i in range(amount - 2):
        for j in range(i + 1, amount - 1):
            for k in range(j + 1, amount):
                pa = point_list[i]
                pb = point_list[j]
                pc = point_list[k]
                tmp_center = get_center(pa, pb, pc)
                if tmp_center != MISTAKE:
                    tmp_rad = get_radius(tmp_center, pa)
                    tmp_circle_data = [tmp_center, tmp_rad]
                    circles_list.append(tmp_circle_data)

    circles_amount = len(circles_list)
    for i in range(circles_amount - 1):
        for j in range(i + 1, circles_amount):
            tmp_amount_points = get_amount_points_in_area(circles_list[i], circles_list[j], point_list)
            tmp_area = get_area_inters(circles_list[i], circles_list[j])
            if (tmp_amount_points > amount_points or (tmp_amount_points == amount_points and tmp_area > area_inter)):
                flag_found_circles = True
                amount_points = tmp_amount_points
                area_inter = tmp_area
                circle_1 = circles_list[i][0]
                radius_1 = circles_list[i][1]
                circle_2 = circles_list[j][0]
                radius_2 = circles_list[j][1]
    
    if flag_found_circles == True:
        draw_circle(circle_1, radius_1)
        draw_circle(circle_2, radius_2)

def print_result():
    global circle_1, circle_2, radius_1, radius_2
    if flag_found_circles == False:
        messagebox.showwarning("Error", "Окружности не были найдены\nПопробуйте посторить окружности")
        return
    messagebox.showinfo("Result", "Центр первой окружности: X:{}\tY:{}\nРадиус первой окружности: {}\n\n"
                                  "Центр второй окружности: X:{}\tY:{}\nРадиус второй окружности: {}".format(circle_1.x, circle_1.y, radius_1,\
                                                                                                  circle_2.x, circle_2.y, radius_2))

def clear_canvas_field():
    global numb_points
    global flag_found_circles

    canvas.delete("all")
    clear_fields(del_point_txt)
    clear_fields(x_point_txt)
    clear_fields(y_point_txt)
    draw_axis()
    point_list.clear()
    numb_points = 0
    scroll_menu.delete(0, scroll_menu.size() - 1)
    flag_found_circles = False

if __name__ == "__main__":
    CORRECT = 1
    MISTAKE = 0
    color_points_add = "purple"
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

    flag_found_circles = False
    amount_points = -1
    area_inter = -1
    circle_1 = Point(0, 0)
    radius_1 = 0
    circle_2 = Point(0, 0)
    radius_2 = 0
    
    window.title("Lab №1")
    window.geometry("%dx%d" % (WINDOW_W, WINDOW_H))
    window.resizable(False, False)

    canvas = Canvas(window, width=CANVAS_X, height=CANVAS_Y, bg="lightblue")
    canvas.place(x=0, y=120)

    draw_axis()

    Label(window, text="X: ", font=("Times New Roman", 18)).place(width=60, height=40, x=10, y=15)
    x_point_txt = Entry(window, font=("Times New Roman", 13))
    x_point_txt.place(width=50, height=40, x=50, y=15)

    Label(window, text="Y: ", font=("Times New Roman", 18)).place(width=60, height=40, x=100, y=15)
    y_point_txt = Entry(window, font=("Times New Roman", 13))
    y_point_txt.place(width=50, height=40, x=140, y=15)

    Button(text="Добавить точку", font=("Times New Roman", 15), command=add_point).place(width=180, height=40, x=10, y=60)

    Label(window, text="Список точек:", font=("Times New Roman", 15)).place(width=180, height=40, x=830, y=15)
    scroll_menu = Listbox()
    scroll_menu.place(width=180, height=100, x=1000, y=15)
    
    
    Label(window, text="№: ", font=("Times New Roman", 18)).place(width=60, height=40, x=200, y=15)
    del_point_txt = Entry(window, font=("Times New Roman", 13))
    del_point_txt.place(width=130, height=40, x=250, y=15)
    Button(text="Удалить точку", font=("Times New Roman", 15), command=del_point).place(width=180, height=40, x=200, y=60)
    Button(text="Удалить все точки", font=("Times New Roman", 15), command=clear_canvas_field).place(width=180, height=40, x=600, y=15)

    Button(text="Построить окруж.", font=("Times New Roman", 15), command=find_circle).place(width=180, height=40, x=400, y=60)
    Button(text="Вывести результат", font=("Times New Roman", 15), command=print_result).place(width=180, height=40, x=600, y=60)
    
    Button(text="Условие задачи", font=("Times New Roman", 15), command=task).place(width=180, height=40, x=400, y=15)
    
    
    window.mainloop()
