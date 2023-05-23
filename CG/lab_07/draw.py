def draw_lines(canvas, lines):
    for line in lines:
        if len(line) == 3:
            canvas.create_line(line[0], line[1], fill=line[2])

def set_pixel(canvas, x, y, colour):
    canvas.create_line(x, y, x+1, y, fill=colour)

def add_line(canvas, lines, xb, yb, xe, ye, linecolour):
    canvas.create_line(xb, yb, xe, ye, fill=linecolour)

    lines.append([])
    lines[-1].append([xb, yb])
    lines[-1].append([xe, ye])
    lines[-1].append(linecolour)

def draw_rect(canvas, rect, lines, clip_colour):
    canvas.delete("all")
    draw_lines(canvas, lines)
    canvas.create_rectangle(rect[0], rect[1], rect[2], rect[3], outline=clip_colour)

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

def draw_rect_by_button(event, rect, lines, canvas, clipcolour, flag):
    if flag == False:
        rect[0] = event.x
        rect[1] = event.y
        flag = True
    else:
        x = event.x
        y = event.y

        canvas.delete("all")
        draw_lines(canvas, lines)
        canvas.create_rectangle(rect[0], rect[1], x, y, outline=clipcolour)

        rect[2] = x
        rect[3] = y
    return flag
