from ui import *
from config import *
from algorithms import *
import time as time

def place_line_colour_choice(frame, size_colour, start_column):
    def get_colour_line():
        colour = colorchooser.askcolor(title="Choose colour")
        set_line_colour(colour[-1])

    def set_line_colour(colour):
        global LINE_COLOUR
        LINE_COLOUR = colour
        cur_colour_line.configure(bg=LINE_COLOUR)

    cur_colour_text_label = tk.Label(frame, bg=FRAME_COLOUR, text="Текущий цвет:",
                                     font=("Consoles", FONT_LABEL),
                                     fg=MAIN_COLOUR_LABEL_TEXT)
    cur_colour_line = tk.Label(frame, bg="black")
    cur_colour_text_label.place(x=BORDERS_SPACE, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 1.5,
                                height=FRAME_H // COLUMNS)
    cur_colour_line.place(x=FRAME_W // 3 - BORDERS_SPACE + FRAME_W // 2, y=(start_column + 2) * FRAME_H // COLUMNS, width=size_colour,
                            height=FRAME_H // COLUMNS)
    colour_line = tk.Label(frame, bg=FRAME_COLOUR, text="ЦВЕТ:", font=("Consoles", FONT_LABEL),
                             fg=MAIN_COLOUR_LABEL_TEXT)
    colour_line.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W // 3, height=FRAME_H // COLUMNS)

    white_line = tk.Button(frame, bg="#fcfcee", activebackground="#fcfcee",
                             command=lambda: set_line_colour("#fcfcee"))
    yellow_line = tk.Button(frame, bg="#f39f18", activebackground="#f39f18",
                              command=lambda: set_line_colour("#f39f18"))
    orange_line = tk.Button(frame, bg="#ff6800", activebackground="#ff6800",
                              command=lambda: set_line_colour("#ff6800"))
    red_line = tk.Button(frame, bg="#ff2400", activebackground="#ff2400", 
                              command=lambda: set_line_colour("#ff2400"))
    purple_line = tk.Button(frame, bg="#8b00ff", activebackground="#8b00ff",
                              command=lambda: set_line_colour("#8b00ff"))
    light_green_line = tk.Button(frame, bg="#90EE90", activebackground="#90EE90",
                                   command=lambda: set_line_colour("#90EE90"))
    green_line = tk.Button(frame, bg="#00FF00", activebackground="#00FF00",
                             command=lambda: set_line_colour("#00FF00"))
    light_blue_line = tk.Button(frame, bg="#ADD8E6", activebackground="#ADD8E6",
                                  command=lambda: set_line_colour("#ADD8E6"))

    white_line.place(x=FRAME_W // 3 - BORDERS_SPACE, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                       height=FRAME_H // COLUMNS)
    yellow_line.place(x=FRAME_W // 3 - BORDERS_SPACE + size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                        height=FRAME_H // COLUMNS)
    orange_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 2 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                        height=FRAME_H // COLUMNS)
    red_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 3 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                     height=FRAME_H // COLUMNS)
    purple_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 4 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                        height=FRAME_H // COLUMNS)
    light_green_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 5 * size_colour, y=start_column * FRAME_H // COLUMNS,
                             width=size_colour, height=FRAME_H // COLUMNS)
    green_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 6 * size_colour, y=start_column * FRAME_H // COLUMNS, width=size_colour,
                       height=FRAME_H // COLUMNS)
    light_blue_line.place(x=FRAME_W // 3 - BORDERS_SPACE + 7 * size_colour, y=start_column * FRAME_H // COLUMNS,
                            width=size_colour, height=FRAME_H // COLUMNS)

    line_colour_change = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Поменять цвет",
                                     font=("Consoles", 11), command=get_colour_line)
    line_colour_change.place(x=FRAME_W // 3 - BORDERS_SPACE, y=(start_column + 1) * FRAME_H // COLUMNS, width=FRAME_W // 1.5,
                               height=FRAME_H // COLUMNS)


def place_colour_choose_block(frame, start_column):
    size_colour = (FRAME_W // 1.5) // 8

    colour_choice_label = tk.Label(frame, bg=MAIN_COLOUR_LABEL_BG, text="ВЫБОР ЦВЕТА", font=("Consoles", FONT_HEAD),
                                   fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

    colour_choice_label.place(x=0, y=start_column * FRAME_H // COLUMNS, width=FRAME_W, height=FRAME_H // COLUMNS)

    place_line_colour_choice(frame, size_colour, start_column + 1)


def clear_screen():
    all_figures.clear()
    cur_figure.clear()
    listPoint_scroll.delete(0, tk.END)
    canvasField.delete("all")
    canvasImg.put(CANVAS_COLOUR, to=(0, 0, int(CANVAS_W), int(CANVAS_H)))
    canvasField.create_image(CANVAS_W // 2, CANVAS_H // 2, image=canvasImg, state="normal")

def get_point():
    x = xEntry.get()
    y = yEntry.get()
    if not x or not y:
        messagebox.showinfo("Предупреждение!", "Координаты точек не введены!")
    else:
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            messagebox.showinfo("Предупреждение!", "Координаты точек должны быть только целые!")
            return
        add_point(x, y)
    
def get_seed():
    x = xEntry.get()
    y = yEntry.get()
    if not x or not y:
        messagebox.showinfo("Предупреждение!", "Координаты точек не введены!")
    else:
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            messagebox.showinfo("Предупреждение!", "Координаты точек должны быть только целые!")
            return
        add_seed(x, y)

def findIndexForListPointScroll(all_figures, cur_figure):
    index = 0

    for point_figure in all_figures:
        index += len(point_figure) + 1

    index += len(cur_figure)
    return index

def add_point(x, y, colour="#000000"):
    if Point(x, y) not in cur_figure:
        if cur_figure:
            draw_line_on_img(canvasImg, cur_figure[-1], Point(x, y), colour)

        index = findIndexForListPointScroll(all_figures, cur_figure)
        listPoint_scroll.insert(index,  "{:3d}) X = {:4d}; Y = {:4d}".format(index + 1, x, y))
        cur_figure.append(Point(x, y))
    else:
        messagebox.showwarning("Предупреждение!", "Точка с такими координатами фигуры уже введена!")

def draw_line_on_img(img, ps, pe, colour="#000000"):
    points = bresenhem_int(ps, pe)
    for p in points:
        draw_pixel(img, p.x, p.y, colour)

def add_point_figure_onClick(event):
    x, y = event.x, event.y
    add_point(x, y, BORDER_COLOUR)

def add_seed(x, y):
    draw_pixel(canvasImg, x+1, y+1, colour="orange")
    draw_pixel(canvasImg, x+1, y  , colour="orange")
    draw_pixel(canvasImg, x+1, y-1, colour="orange")
    draw_pixel(canvasImg, x  , y+1, colour="orange")
    draw_pixel(canvasImg, x  , y  , colour="orange")
    draw_pixel(canvasImg, x  , y-1, colour="orange")
    draw_pixel(canvasImg, x-1, y+1, colour="orange")
    draw_pixel(canvasImg, x-1, y  , colour="orange")
    draw_pixel(canvasImg, x-1, y-1, colour="orange")

    listPoint_scroll.insert(tk.END, "SEED PIXEL: ({:4d}, {:4d})".format(x, y))

    seed_points.append(Point(x, y))

def close_figure():
    global cur_figure
    if len(cur_figure) > 2:
        #canvasField.create_line(cur_figure[-1].x, cur_figure[-1].y, cur_figure[0].x, cur_figure[0].y)
        draw_line_on_img(canvasImg, cur_figure[-1], cur_figure[0], BORDER_COLOUR)
        index = findIndexForListPointScroll(all_figures, cur_figure)
        listPoint_scroll.insert(index, "------------Closed------------")

        all_figures.append(cur_figure)
        cur_figure = []
    elif len(cur_figure) == 0:
        messagebox.showwarning("Предупреждение!", "Точки фигуры не введены!")
    else:
        messagebox.showwarning("Предупреждение!", "Такую фигуру нельзя замкнуть!\nНеобходимо как минимум, чтобы у фигуры было 3 точки!")

def fill_all_figures():
    global LINE_COLOUR
    if not all_figures and not cur_figure:
        messagebox.showwarning("Предупреждение!", "Фигура не введена для закраски!")
    elif not all_figures and  cur_figure:
        messagebox.showwarning("Предупреждение!", "Фигура не замкнута для закраски!")
    else:
        if not seed_points:
            messagebox.showwarning("Предупреждение!", "Затравочный пиксел не установлен!")
            return
        if LINE_COLOUR == BORDER_COLOUR:
            messagebox.showwarning("Предупреждение!", "Цвет границы и цвет закраски не должны совпадать!")
            return
        if LINE_COLOUR == CANVAS_COLOUR:
            messagebox.showwarning("Предупреждение!", "Цвет границы и цвет фона не должны совпадать!")
            return
        
        delay = False
        if methodDraw.get() == 0:
            delay = True
        print(seed_points)
        time_start = time.time()
        fill_with_seed(canvasField, canvasImg, BORDER_COLOUR, LINE_COLOUR, seed_points[-1], delay=delay)
        time_end = time.time() - time_start
        if round(time_end * 1000, 2) < 1000:
            timeLabel["text"] = "Время закраски: " + str(round(time_end * 1000, 2)) + " mc."
        else:
            timeLabel["text"] = "Время закраски: " + str(round(time_end, 2)) + " c."

# LAB WINDOW CREATION + SIZE CONFIGURATION
root = tk.Tk()
root.title("Lab №6")
root.geometry(str(WINDOW_W) + "x" + str(WINDOW_H))
root["bg"] = MAIN_COLOUR
root.resizable(True, True)

cur_figure = []
all_figures = []
seed_points = []

if __name__ == "__main__":
    frame = tk.Frame(root)
    frame["bg"] = FRAME_COLOUR
    frame.place(x=BORDERS_SPACE,
                    y=BORDERS_SPACE,
                    width=FRAME_W,
                    height=FRAME_H)
    
    canvasField = tk.Canvas(root, bg=CANVAS_COLOUR)
    canvasField.place(x=WINDOW_W*FRAME_SITUATION + BORDERS_SPACE,
                      y=BORDERS_SPACE,
                      width=CANVAS_W,
                      height=CANVAS_H)
    
    canvasImg = tk.PhotoImage(width=int(CANVAS_W+1), height=int(CANVAS_H+1))
    canvasField.create_image(CANVAS_W // 2, CANVAS_H // 2, image=canvasImg, state='normal')
    canvasImg.put(CANVAS_COLOUR, to=(0, 0, int(CANVAS_W), int(CANVAS_H)))
    
    canvasField.bind("<Button-1>", add_point_figure_onClick)
    canvasField.bind("<Button-2>", lambda event: add_seed(event.x, event.y))
    canvasField.bind("<Button-3>", lambda event: close_figure())
    canvasField.bind("<B1-Motion>", add_point_figure_onClick)
    
    
    place_colour_choose_block(frame, 0)

    methodDraw = tk.IntVar()
    place_draw_method(frame, methodDraw, 5)

    xEntry = tk.Entry(frame, bg="white", font=("Consolas", FONT_ENTRY), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    yEntry = tk.Entry(frame, bg="white", font=("Consolas", FONT_ENTRY), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    listPoint_scroll = tk.Listbox(font=("Consolas", FONT_ENTRY))
    place_draw_point(frame, xEntry, yEntry, listPoint_scroll, get_point, close_figure, get_seed, 8)

    timeLabel = tk.Label(root, bg="gray", text="Время закраски: ",
                             font=("Consolas", 16),
                             fg=MAIN_COLOUR_LABEL_TEXT)
    fillingBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Закрасить фигуры", font=("Consolas", 14), command=fill_all_figures)
    place_mouse_mode(frame, fillingBtn, timeLabel, 20)
    
    place_clear_info_block(frame, clear_screen, COLUMNS - 4)

root.mainloop()