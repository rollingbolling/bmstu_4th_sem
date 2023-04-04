import tkinter as tk
import tkinter.messagebox as mb
import config as cfg

root = tk.Tk()
root.title("Лабораторная радота №2")
root["bg"] = cfg.MAIN_COLOR
root.geometry(str(cfg.WINDOW_W) + "x" + str(cfg.WINDOW_H))
root.resizable(height=False, width=False)

dataFrame = tk.Frame(root)
dataFrame["bg"] = cfg.MAIN_FRAME_COLOR
dataFrame.place(x=int(cfg.BORDERS_SPACE), y=int(cfg.BORDERS_SPACE), width=cfg.DATA_W, height=cfg.DATA_H)

field = tk.Canvas(root, bg="lightblue")
field.place(x=cfg.WINDOW_W * cfg.BORDERS_MAIN_MAKE + 2 * cfg.BORDERS_SPACE, y=cfg.BORDERS_SPACE,\
            width=cfg.FIELD_W, height=cfg.FIELD_H)



root.mainloop()
