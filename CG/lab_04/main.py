from ui import *


# BUTTON_FUNCS
def draw_axes():
    colour = "gray"
    canvasField.create_line(0, 3, CANVAS_W, 3, width=1, fill='gray', arrow=tk.LAST)
    canvasField.create_line(3, 0, 3, CANVAS_H, width=1, fill='gray', arrow=tk.LAST)
    for i in range(50, int(CANVAS_W), 50):
        canvasField.create_text(i, 15, text=str(abs(i)), fill=colour)
        canvasField.create_line(i, 0, i, 5, fill=colour)
    for i in range(50, int(CANVAS_H), 50):
        canvasField.create_text(15, i, text=str(abs(i)), fill=colour)
        canvasField.create_line(0, i, 5, i, fill=colour)


def clear_screen():
    canvasField.delete("all")
    draw_axes()


# LAB WINDOW CREATION + SIZE CONFIGURATION
root = tk.Tk()
root.title("Lab №3")
root.geometry(str(WINDOW_W) + "x" + str(WINDOW_H))
root["bg"] = MAIN_COLOUR
root.resizable(True, True)

# UI
if __name__ == "__main__":
    # FRAME CREATION
    dataFrame = tk.Frame(root)
    dataFrame["bg"] = FRAME_COLOUR
    dataFrame.place(x=BORDERS_SPACE, y=BORDERS_SPACE, width=FRAME_W, height=FRAME_H)

    # CANVAS CREATION
    canvasField = tk.Canvas(root, bg=CANVAS_COLOUR)
    canvasField.place(x=WINDOW_W * FRAME_SITUATION + BORDERS_SPACE, y=BORDERS_SPACE, width=CANVAS_W, height=CANVAS_H)
    draw_axes()

    # ВЫБОР АЛГОРИТМА
    place_algo_choose(dataFrame, 0)

    # ВЫБОР ЦВЕТА
    place_colour_choose_block(dataFrame, canvasField, 7)

    # DRAW FIGURE
    place_draw_figure_block(dataFrame, clear_screen(), clear_screen(), 14)

    # DRAW SPECTOR
    place_draw_spectre_block(dataFrame, clear_screen(), clear_screen(), 22)

    # INFO & STATS
    place_analys_block(dataFrame, clear_screen(), clear_screen(), 29)
    place_clear_info_block(dataFrame, clear_screen(), 32)

root.mainloop()
