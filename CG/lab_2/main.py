import tkinter as tk
import tkinter.messagebox as mb
import config as cfg
import buttonFunc as bf

def draw_figure_on_can():
    field.delete("all")
    bf.get_figure()
    bf.draw_figure(field)

def move_figure():
    try:
        x = float(dxEntry.get())
        y = -float(dyEntry.get())
    except ValueError:
        mb.showerror("Неверный ввод",
                    "Введите действительные числа в поля ввода")

    else:
        move_coefs = [x, y]
        bf.move_list(move_coefs)
    
    field.delete("all")
    bf.draw_figure(field)

def scale_figure():
    try:
        x = float(scxEntry.get())
        y = float(scyEntry.get())
        cx_scale = float(sxEntry.get())
        cy_scale = float(syEntry.get())
    except ValueError:
        mb.showerror("Неверный ввод",
                    "Введите действительные числа в поля ввода")
    else:
        scale_coefs = [x, y]
        scale_center = [cx_scale, cy_scale]
        bf.scale_list(scale_coefs, scale_center)
    field.delete("all")
    bf.draw_figure(field)

def rotate_figure():
    try:
        x = float(rxEntry.get())
        y = float(ryEntry.get())
        angle = float(angleEntry.get())
    except ValueError:
        mb.showerror("Неверный ввод",
                    "Введите действительные числа в поля ввода")
    else:
        rot_center = [x, y]
        bf.rotate_list(rot_center, angle)
    field.delete("all")
    bf.draw_figure(field)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Лабораторная радота №2")
    root["bg"] = cfg.MAIN_COLOUR
    root.geometry(str(cfg.WINDOW_W) + "x" + str(cfg.WINDOW_H))
    root.resizable(height=False, width=False)

    dataFrame = tk.Frame(root)
    dataFrame["bg"] = cfg.MAIN_FRAME_COLOUR
    dataFrame.place(x=int(cfg.BORDERS_SPACE), y=int(cfg.BORDERS_SPACE), width=cfg.DATA_W, height=cfg.DATA_H)

    field = tk.Canvas(root, bg="lightblue")
    field.place(x=cfg.WINDOW_W * cfg.BORDERS_MAIN_MAKE + 2 * cfg.BORDERS_SPACE, y=cfg.BORDERS_SPACE,\
                width=cfg.FIELD_W, height=cfg.FIELD_H)


    #Move---------------------------------------------------------------------------------------------------------------------------------------------
    moveInfButton = tk.Button(dataFrame, text="i", font=("Consolas", 20), bg=cfg.ADD_COLOUR, fg=cfg.TEXT_ENTRY_COLOUR,
                            activebackground=cfg.ADD_COLOUR, 
                            activeforeground=cfg.MAIN_COLOUR)

    moveLabel = tk.Label(dataFrame, bg=cfg.ADD_COLOUR, text="ПЕРЕМЕЩЕНИЕ",
                        font=("Consolas", 16),
                        fg=cfg.TEXT_ENTRY_COLOUR, relief=tk.GROOVE)

    dxEntry = tk.Entry(dataFrame, bg=cfg.TEXT_ENTRY_COLOUR, font=("Consolas", 14),
                    fg=cfg.MAIN_FRAME_COLOUR, justify="center")
    dyEntry = tk.Entry(dataFrame, bg=cfg.TEXT_ENTRY_COLOUR, font=("Consolas", 15),
                    fg=cfg.MAIN_FRAME_COLOUR, justify="center")
    moveBtn = tk.Button(dataFrame, text="Переместить", font=("Consolas", 14),
                        bg=cfg.MAIN_FRAME_COLOUR, fg=cfg.TEXT_ENTRY_COLOUR, command=move_figure,
                        activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_FRAME_COLOUR)

    moveLabel.place(x=0, y=0, width=cfg.DATA_W * cfg.DATA_K_LABEL, height=cfg.DATA_H // cfg.COLUMNS)
    moveInfButton.place(x=cfg.DATA_W * cfg.DATA_K_LABEL, y=0, width=cfg.DATA_W * (1 - cfg.DATA_K_LABEL), height=cfg.DATA_H // cfg.COLUMNS)

    tk.Label(dataFrame, bg=cfg.ADD_COLOUR, text="dx         dy",
                        font=("Consolas", 18),
                        fg=cfg.TEXT_ENTRY_COLOUR).\
                        place(x=0, y=cfg.DATA_H // cfg.COLUMNS, width=cfg.DATA_W, height=cfg.DATA_H // cfg.COLUMNS)

    dxEntry.place(x=0, y=2 * cfg.DATA_H // cfg.COLUMNS, width=cfg.DATA_W // 2,
                height=cfg.DATA_H // cfg.COLUMNS)
    dyEntry.place(x=cfg.DATA_W // 2, y=2 * cfg.DATA_H // cfg.COLUMNS,
                width=cfg.DATA_W // 2, height=cfg.DATA_H // cfg.COLUMNS)
    moveBtn.place(x=0, y=3 * cfg.DATA_H // cfg.COLUMNS, width=cfg.DATA_W,
                height=cfg.DATA_H // cfg.COLUMNS)
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    #Scale--------------------------------------------------------------------------------------------------------------------------------------------
    scaleInfButton = tk.Button(dataFrame, text="i", font=("Consolas", 20),
                            bg=cfg.ADD_COLOUR, fg=cfg.TEXT_ENTRY_COLOUR,# command=bf.showInfoScale,
                            activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_COLOUR)

    scaleLabel = tk.Label(dataFrame, bg=cfg.ADD_COLOUR, text="МАСШТАБИРОВАНИЕ",
                        font=("Consolas", 16),
                        fg=cfg.TEXT_ENTRY_COLOUR, relief=tk.GROOVE)

    sxEntry = tk.Entry(dataFrame, bg=cfg.TEXT_ENTRY_COLOUR, font=("Consolas", 13),
                    fg=cfg.MAIN_FRAME_COLOUR, justify="center")
    syEntry = tk.Entry(dataFrame, bg=cfg.TEXT_ENTRY_COLOUR, font=("Consolas", 13),
                    fg=cfg.MAIN_FRAME_COLOUR, justify="center")
    scxEntry = tk.Entry(dataFrame, bg=cfg.TEXT_ENTRY_COLOUR, font=("Consolas", 13),
                        fg=cfg.MAIN_FRAME_COLOUR, justify="center")
    scyEntry = tk.Entry(dataFrame, bg=cfg.TEXT_ENTRY_COLOUR, font=("Consolas", 13),
                        fg=cfg.MAIN_FRAME_COLOUR, justify="center")

    scaleBtn = tk.Button(dataFrame, text="Масштабировать", font=("Consolas", 14),
                        bg=cfg.MAIN_FRAME_COLOUR, fg=cfg.TEXT_ENTRY_COLOUR, command=scale_figure,
                        activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_FRAME_COLOUR)

    scaleLabel.place(x=0, y=cfg.DATA_H * 2 * cfg.COLUMNS_DATA_BORDERS_H + 20, width=cfg.DATA_W * cfg.DATA_K_LABEL, height=cfg.DATA_H // cfg.COLUMNS)
    scaleInfButton.place(x=cfg.DATA_W * cfg.DATA_K_LABEL, y=cfg.DATA_H * 2 * cfg.COLUMNS_DATA_BORDERS_H + 20, width=cfg.DATA_W * (1 - cfg.DATA_K_LABEL), height=cfg.DATA_H // cfg.COLUMNS)

    tk.Label(dataFrame, bg=cfg.ADD_COLOUR, text="kx    ky    cx    cy",
                        font=("Consolas", 18),
                        fg=cfg.TEXT_ENTRY_COLOUR).\
                        place(x=0, y=cfg.DATA_H * 2 * cfg.COLUMNS_DATA_BORDERS_H + cfg.DATA_H // cfg.COLUMNS + 20, width=cfg.DATA_W, height=cfg.DATA_H // cfg.COLUMNS)

    sxEntry.place(x=0, y=cfg.DATA_H * 2 * cfg.COLUMNS_DATA_BORDERS_H + 2 * cfg.DATA_H // cfg.COLUMNS + 20, width=cfg.DATA_W // 3,
                height=cfg.DATA_H // cfg.COLUMNS)

    syEntry.place(x=cfg.DATA_W // 4, y=cfg.DATA_H * 2 * cfg.COLUMNS_DATA_BORDERS_H + 2 * cfg.DATA_H // cfg.COLUMNS + 20,
                width=cfg.DATA_W // 4, height=cfg.DATA_H // cfg.COLUMNS)

    scxEntry.place(x=2 * cfg.DATA_W // 4, y=cfg.DATA_H * 2 * cfg.COLUMNS_DATA_BORDERS_H + 2 * cfg.DATA_H // cfg.COLUMNS + 20,
                width=cfg.DATA_W // 4, height=cfg.DATA_H // cfg.COLUMNS)

    scyEntry.place(x=3 * cfg.DATA_W // 4, y=cfg.DATA_H * 2 * cfg.COLUMNS_DATA_BORDERS_H + 2 * cfg.DATA_H // cfg.COLUMNS + 20,
                width=cfg.DATA_W // 4, height=cfg.DATA_H // cfg.COLUMNS)

    scaleBtn.place(x=0, y=cfg.DATA_H * 2 * cfg.COLUMNS_DATA_BORDERS_H + 3 * cfg.DATA_H // cfg.COLUMNS + 20, width=cfg.DATA_W,
                height=cfg.DATA_H // cfg.COLUMNS)
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    #Rotate-------------------------------------------------------------------------------------------------------------------------------------------
    rotateInfButton = tk.Button(dataFrame, text="i", font=("Consolas", 20),
                            bg=cfg.ADD_COLOUR, fg=cfg.TEXT_ENTRY_COLOUR,# command=bf.showInfoRotate,
                            activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_COLOUR)

    rotateLabel = tk.Label(dataFrame, bg=cfg.ADD_COLOUR, text="ПОВЕРНУТЬ",
                        font=("Consolas", 16),
                        fg=cfg.TEXT_ENTRY_COLOUR, relief=tk.GROOVE)

    rxEntry = tk.Entry(dataFrame, bg=cfg.TEXT_ENTRY_COLOUR, font=("Consolas", 13),
                    fg=cfg.MAIN_FRAME_COLOUR, justify="center")
    ryEntry = tk.Entry(dataFrame, bg=cfg.TEXT_ENTRY_COLOUR, font=("Consolas", 13),
                    fg=cfg.MAIN_FRAME_COLOUR, justify="center")
    angleEntry = tk.Entry(dataFrame, bg=cfg.TEXT_ENTRY_COLOUR, font=("Consolas", 13),
                        fg=cfg.MAIN_FRAME_COLOUR, justify="center")

    rotateBtn = tk.Button(dataFrame, text="Повернуть", font=("Consolas", 14),
                        bg=cfg.MAIN_FRAME_COLOUR, fg=cfg.TEXT_ENTRY_COLOUR, command=rotate_figure,
                        activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_FRAME_COLOUR)

    rotateLabel.place(x=0, y=cfg.DATA_H * cfg.COLUMNS_DATA_BORDERS_H + 10, width=cfg.DATA_W * cfg.DATA_K_LABEL, height=cfg.DATA_H // cfg.COLUMNS)
    rotateInfButton.place(x=cfg.DATA_W * cfg.DATA_K_LABEL, y=cfg.DATA_H * cfg.COLUMNS_DATA_BORDERS_H + 10, width=cfg.DATA_W * (1 - cfg.DATA_K_LABEL), height=cfg.DATA_H // cfg.COLUMNS)

    tk.Label(dataFrame, bg=cfg.ADD_COLOUR, text="rx      ry    angle",
                        font=("Consolas", 18),
                        fg=cfg.TEXT_ENTRY_COLOUR).\
                        place(x=0, y=cfg.DATA_H * cfg.COLUMNS_DATA_BORDERS_H + cfg.DATA_H // cfg.COLUMNS + 10, width=cfg.DATA_W, height=cfg.DATA_H // cfg.COLUMNS)

    rxEntry.place(x=0, y=cfg.DATA_H * cfg.COLUMNS_DATA_BORDERS_H + 2 * cfg.DATA_H // cfg.COLUMNS + 10, width=cfg.DATA_W // 3,
                height=cfg.DATA_H // cfg.COLUMNS)

    ryEntry.place(x=cfg.DATA_W // 3, y=cfg.DATA_H * cfg.COLUMNS_DATA_BORDERS_H + 2 * cfg.DATA_H // cfg.COLUMNS + 10,
                width=cfg.DATA_W // 3, height=cfg.DATA_H // cfg.COLUMNS)

    angleEntry.place(x=2 * cfg.DATA_W // 3, y=cfg.DATA_H * cfg.COLUMNS_DATA_BORDERS_H + 2 * cfg.DATA_H // cfg.COLUMNS + 10,
                width=cfg.DATA_W // 3, height=cfg.DATA_H // cfg.COLUMNS)

    rotateBtn.place(x=0, y=cfg.DATA_H * cfg.COLUMNS_DATA_BORDERS_H + 3 * cfg.DATA_H // cfg.COLUMNS + 10, width=cfg.DATA_W,
                height=cfg.DATA_H // cfg.COLUMNS)
    #-------------------------------------------------------------------------------------------------------------------------------------------------
    #Draw---------------------------------------------------------------------------------------------------------------------------------------------
    constBtn = tk.Button(dataFrame, text="Построить", font=("Consolas", 14),
                        bg=cfg.MAIN_FRAME_COLOUR, fg=cfg.TEXT_ENTRY_COLOUR, command=draw_figure_on_can,
                        activebackground=cfg.ADD_COLOUR, activeforeground=cfg.MAIN_FRAME_COLOUR)

    constBtn.place(x=0, y=cfg.DATA_H * 3 * cfg.COLUMNS_DATA_BORDERS_H + 3 * cfg.DATA_H // cfg.COLUMNS + 30, width=cfg.DATA_W,
                height=cfg.DATA_H // cfg.COLUMNS)
    #-------------------------------------------------------------------------------------------------------------------------------------------------




    root.mainloop()
