from ui import *
from config import *
from algorithms import *
from draw import *

def place_section_colour_choice(frame, size_colour, start_column):
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
    cur_colour_line = tk.Label(frame, bg=LINE_COLOUR)
    cur_colour_text_label.place(x=BORDERS_SPACE, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 1.5,
                                height=FRAME_H // COLUMNS)
    cur_colour_line.place(x=FRAME_W // 3 - BORDERS_SPACE + FRAME_W // 2, y=(start_column + 2) * FRAME_H // COLUMNS, width=size_colour,
                            height=FRAME_H // COLUMNS)
    colour_line = tk.Label(frame, bg=FRAME_COLOUR, text="ЦВЕТ Отрезка:", font=("Consoles", FONT_LABEL),
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

def place_cliper_colour_choise(frame, size_colour, start_column):
    def get_colour_line():
        colour = colorchooser.askcolor(title="Choose colour")
        set_line_colour(colour[-1])

    def set_line_colour(colour):
        global CLIP_COLOUR
        CLIP_COLOUR = colour
        cur_colour_line.configure(bg=CLIP_COLOUR)

    cur_colour_text_label = tk.Label(frame, bg=FRAME_COLOUR, text="Текущий цвет:",
                                     font=("Consoles", FONT_LABEL),
                                     fg=MAIN_COLOUR_LABEL_TEXT)
    cur_colour_line = tk.Label(frame, bg=CLIP_COLOUR)
    cur_colour_text_label.place(x=BORDERS_SPACE, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 1.5,
                                height=FRAME_H // COLUMNS)
    cur_colour_line.place(x=FRAME_W // 3 - BORDERS_SPACE + FRAME_W // 2, y=(start_column + 2) * FRAME_H // COLUMNS, width=size_colour,
                            height=FRAME_H // COLUMNS)
    colour_line = tk.Label(frame, bg=FRAME_COLOUR, text="ЦВЕТ Отсекателя:", font=("Consoles", FONT_LABEL),
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

def place_res_colour_choise(frame, size_colour, start_column):
    def get_colour_line():
        colour = colorchooser.askcolor(title="Choose colour")
        set_line_colour(colour[-1])

    def set_line_colour(colour):
        global RES_COLOUR
        RES_COLOUR = colour
        cur_colour_line.configure(bg=RES_COLOUR)

    cur_colour_text_label = tk.Label(frame, bg=FRAME_COLOUR, text="Текущий цвет:",
                                     font=("Consoles", FONT_LABEL),
                                     fg=MAIN_COLOUR_LABEL_TEXT)
    cur_colour_line = tk.Label(frame, bg=RES_COLOUR)
    cur_colour_text_label.place(x=BORDERS_SPACE, y=(start_column + 2) * FRAME_H // COLUMNS, width=FRAME_W // 1.5,
                                height=FRAME_H // COLUMNS)
    cur_colour_line.place(x=FRAME_W // 3 - BORDERS_SPACE + FRAME_W // 2, y=(start_column + 2) * FRAME_H // COLUMNS, width=size_colour,
                            height=FRAME_H // COLUMNS)
    colour_line = tk.Label(frame, bg=FRAME_COLOUR, text="ЦВЕТ Результата:", font=("Consoles", FONT_LABEL),
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

    place_section_colour_choice(frame, size_colour, start_column + 1)
    place_cliper_colour_choise(frame, size_colour, start_column + 4.5)
    place_res_colour_choise(frame, size_colour, start_column + 8)


def clear_screen():
    global is_set_rectangle
    canvasField.delete("all")
    lines.clear()
    is_set_rectangle = False
    clipper_figure.clear()

def click_left(event):
    global is_set_rectangle
    if is_set_rectangle:
        clipper_figure.clear()
        canvasField.delete("all")
        for line in lines:
            if len(line) > 1:
                canvasField.create_line(line[0], line[1], fill=LINE_COLOUR)
        is_set_rectangle = False

    add_clipper(canvasField, clipper_figure, [event.x, event.y], CLIP_COLOUR)

def click_right(event, lines, canvas, linecolour):
    x = event.x
    y = event.y

    if len(lines) == 0 or len(lines[-1]) > 2:
        lines.append([])

    set_pixel(canvas, x, y, linecolour)

    lines[-1].append([x, y])

    if len(lines[-1]) == 2:
        canvas.create_line(lines[-1][0], lines[-1][1], fill=linecolour)

        lines[-1].append(linecolour)

def click_mid(event=None):
    global is_set_rectangle
    if len(clipper_figure) < 3:
        messagebox.showwarning("ERROR",
                               "Отсекатель должен иметь не меньше 3 вершин")
        return

    is_set_rectangle = True
    close_clipper(canvasField, clipper_figure, CLIP_COLOUR)

def cut_off_command():
    if not clipper_figure:
        messagebox.showwarning("ERROR", "Не был введен отсекатель")
        return
    if not check_convexity(clipper_figure):
        messagebox.showinfo("ERROR", "Отсекатель не является выпуклым")
        return

    canvasField.create_polygon(clipper_figure, outline=CLIP_COLOUR, fill=CANVAS_COLOUR)

    for line in lines:
        if len(line) > 1:
            cyrus_beck_alg(canvasField, clipper_figure, line, RES_COLOUR)


def draw_line():
    xstart = xsEntry.get()
    ystart = ysEntry.get()
    xend = xsEntry.get()
    yend = yeEntry.get()

    if not xstart or not ystart:
        messagebox.showwarning("ERROR", "Не введены координаты начала отрезка")
    elif not xend or not yend:
        messagebox.showwarning("ERROR", "Не введены координаты конца отрезка")
    else:
        try:
            xstart, ystart = int(xstart), int(ystart)
            xend, yend = int(xend), int(yend)
        except ValueError:
            messagebox.showwarning("ERROR", "Координаты заданы неверно")
        add_line(canvasField, lines, xstart, ystart, xend, yend, LINE_COLOUR)

def add_hor_vert_lines():
    if not clipper_figure:
        messagebox.showwarning("ERROR", "Нет отсекателя")
        return
    
    for i in range(len(clipper_figure) - 1):
        x1 = clipper_figure[i][0]
        y1 = clipper_figure[i][1]
        x2 = clipper_figure[i + 1][0]
        y2 = clipper_figure[i + 1][1]

        dx = x2 - x1
        dy = y2 - y1
        k = (y2 - y1) / (x2 - x1)
        def find_paral(k, x1, y1, x2):
            return y1 + k * (x2-x1)
        if dx > dy:
            lines.append([[x1, y1 + 0.5 * dy], [x2, find_paral(k, x1, y1 + 0.5 * dy, x2)], LINE_COLOUR])
            lines.append([[x1, y1 - 0.5 * dy], [x2, find_paral(k, x1, y1 - 0.5 * dy, x2)], LINE_COLOUR])
            canvasField.create_line(x1, y1 + 0.5 * dy, x2, find_paral(k, x1, y1 + 0.5 * dy, x2), fill=LINE_COLOUR)
            canvasField.create_line(x1, y1 - 0.5 * dy, x2, find_paral(k, x1, y1 - 0.5 * dy, x2), fill=LINE_COLOUR)
    
def draw_clip():
    global is_set_rectangle
    xcl = xclEntry.get()
    ycl = yclEntry.get()
    if not xcl or not ycl:
        messagebox.showwarning("ERROR", "Не заданы вершина отсекателя")
        return
    try:
        xcl = int(xcl)
        ycl = int(ycl)
    except ValueError:
        messagebox.showwarning("ERROR", "Неверно заданы координаты вершины отсекателя")
        return
    if is_set_rectangle:
        clipper_figure.clear()
        canvasField.delete("all")
        for line in lines:
            if len(line) > 1:
                canvasField.create_line(line[0], line[1], fill=LINE_COLOUR)
            is_set_rectangle = False

    add_clipper(canvasField, clipper_figure, [xcl, ycl], CLIP_COLOUR)

# LAB WINDOW CREATION + SIZE CONFIGURATION
root = tk.Tk()
root.title("Lab №8")
root.geometry(str(WINDOW_W) + "x" + str(WINDOW_H))
root["bg"] = MAIN_COLOUR
root.resizable(True, True)

clipper_figure = []
lines = []
is_set_rectangle = False

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
    
    canvasField.bind("<Button-1>", lambda event: click_left(event))
    canvasField.bind("<Button-2>", lambda event: click_mid(event))
    canvasField.bind("<Button-3>", lambda event: click_right(event, lines, canvasField, LINE_COLOUR))
    
    
    place_colour_choose_block(frame, 0)

    xsEntry = tk.Entry(frame, bg="white", font=("Consolas", FONT_ENTRY), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    ysEntry = tk.Entry(frame, bg="white", font=("Consolas", FONT_ENTRY), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    xeEntry = tk.Entry(frame, bg="white", font=("Consolas", FONT_ENTRY), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    yeEntry = tk.Entry(frame, bg="white", font=("Consolas", FONT_ENTRY), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    
    place_draw_section(frame, xsEntry, ysEntry, xeEntry, yeEntry, draw_line, 12)

    xclEntry = tk.Entry(frame, bg="white", font=("Consolas", FONT_ENTRY), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    yclEntry = tk.Entry(frame, bg="white", font=("Consolas", FONT_ENTRY), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
    
    place_draw_cliper(frame, xclEntry, yclEntry, draw_clip, click_mid, 17)

    place_mouse_mode(frame, lambda: add_hor_vert_lines(), cut_off_command, 22)
    
    place_clear_info_block(frame, clear_screen, COLUMNS - 3)

xsEntry.insert(0, 100)
ysEntry.insert(0, 200)
xeEntry.insert(0, 800)
yeEntry.insert(0, 500)

xclEntry.insert(0, 100)
yclEntry.insert(0, 200)

root.mainloop()