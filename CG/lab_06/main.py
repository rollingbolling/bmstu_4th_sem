from ui import *
from config import *
from classPoint import Point

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

    white_line = tk.Button(frame, bg="white", activebackground="white",
                             command=lambda: set_line_colour("white"))
    yellow_line = tk.Button(frame, bg="yellow", activebackground="yellow",
                              command=lambda: set_line_colour("yellow"))
    orange_line = tk.Button(frame, bg="orange", activebackground="orange",
                              command=lambda: set_line_colour("orange"))
    red_line = tk.Button(frame, bg="red", activebackground="red", command=lambda: set_line_colour("red"))
    purple_line = tk.Button(frame, bg="purple", activebackground="purple",
                              command=lambda: set_line_colour("purple"))
    light_green_line = tk.Button(frame, bg="light green", activebackground="light green",
                                   command=lambda: set_line_colour("light green"))
    green_line = tk.Button(frame, bg="green", activebackground="green",
                             command=lambda: set_line_colour("green"))
    light_blue_line = tk.Button(frame, bg="light blue", activebackground="light blue",
                                  command=lambda: set_line_colour("light blue"))

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
    
def findIndexForListPointScroll(all_figures, cur_figure):
    index = 0

    for point_figure in all_figures:
        index += len(point_figure) + 1

    index += len(cur_figure)
    return index

def add_point(x, y):
    if Point(x, y) not in cur_figure:
        if cur_figure:
             canvasField.create_line(cur_figure[-1].x, cur_figure[-1].y, x, y)

        index = findIndexForListPointScroll(all_figures, cur_figure)
        listPoint_scroll.insert(index,  "{:3d}) X = {:4d}; Y = {:4d}".format(index + 1, x, y))
        cur_figure.append(Point(x, y))
    else:
        messagebox.showwarning("Предупреждение!", "Точка с такими координатами фигуры уже введена!")

def add_point_figure_onClick(event):
    x, y = event.x, event.y
    add_point(x, y)

def add_seed(x, y):
    

def close_figure():
    global cur_figure
    if len(cur_figure) > 2:
        canvasField.create_line(cur_figure[-1].x, cur_figure[-1].y, cur_figure[0].x, cur_figure[0].y)

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
        delay = False
        if methodDraw.get() == 0:
            delay = True
        time_start = time.time()
        CAP_algorithm_with_ordered_list_of_edges(canvasField, all_figures, colour=LINE_COLOUR, delay=delay)
        time_end = time.time() - time_start
        if round(time_end * 1000, 2) < 1000:
            timeLabel["text"] = "Время закраски: " + str(round(time_end * 1000, 2)) + " mc."
        else:
            timeLabel["text"] = "Время закраски: " + str(round(time_end, 2)) + " c."

# LAB WINDOW CREATION + SIZE CONFIGURATION
root = tk.Tk()
root.title("Lab №5")
root.geometry(str(WINDOW_W) + "x" + str(WINDOW_H))
root["bg"] = MAIN_COLOUR
root.resizable(True, True)

cur_figure = []
all_figures = []

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
    
    canvasField.bind("<Button-1>", add_point_figure_onClick)
    canvasField.bind("<Button-3>", lambda event: close_figure())
    
    
    place_colour_choose_block(frame, 0)

    methodDraw = tk.IntVar()
    place_draw_method(frame, methodDraw, 5)

    xEntry = tk.Entry(frame, bg="white", font=("Consolas", FONT_ENTRY), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    yEntry = tk.Entry(frame, bg="white", font=("Consolas", FONT_ENTRY), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    listPoint_scroll = tk.Listbox(font=("Consolas", FONT_ENTRY))
    place_draw_point(frame, xEntry, yEntry, listPoint_scroll, get_point, close_figure, 8)

    timeLabel = tk.Label(root, bg="gray", text="Время закраски: ",
                             font=("Consolas", 16),
                             fg=MAIN_COLOUR_LABEL_TEXT)
    fillingBtn = tk.Button(frame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Закрасить фигуры", font=("Consolas", 14), command=fill_all_figures)
    place_mouse_mode(frame, fillingBtn, timeLabel, 20)
    
    place_clear_info_block(frame, clear_screen, COLUMNS - 4)

root.mainloop()