from config import CANVAS_COLOUR
from methodfuncs import get_sign, get_rgb_intens

def BrezenhemFloat(x1, y1, x2, y2, colour="black", stepmode=False):
    point_list = []
    if x1==x2 and y1==y2:
        point_list.append([x1, y1, colour])
    else:
        dx = x2 - x1
        dy = y2 - y1

        sx = get_sign(dx)
        sy = get_sign(dy)

        dx = abs(dx)
        dy = abs(dy)

        if dy > dx:
            dx, dy = dy, dx
            exchange = 1
        else:
            exchange = 0

        tg = dy / dx
        e = tg - 0.5
        x, xb = x1, x1
        y, yb = y1, y1
        steps = 0

        while x != x2 or y != y2:
            if not stepmode:
                point_list.append([x, y, colour])

            if e >= 0:
                if exchange == 1:
                    x += sx
                else:
                    y += sy
                e -= 1

            if e <= 0:
                if exchange == 0:
                    x += sx
                else:
                    y += sy
                e += tg

            if stepmode:
                if xb != x and yb != y:
                    steps += 1
                xb = x
                yb = y

        if stepmode:
            return steps
    return point_list

def BrezenhemInt(x1, y1, x2, y2, colour="black", stepmode=False):
    point_list = []
    if x1==x2 and y1==y2:
        point_list.append([x1, y1, colour])
    else:
        dx = x2 - x1
        dy = y2 - y1

        sx = get_sign(dx)
        sy = get_sign(dy)

        dx = abs(dx)
        dy = abs(dy)

        if dy > dx:
            dx, dy = dy, dx
            exchange = 1
        else:
            exchange = 0

        e = 2 * dy - dx
        x = x1
        y = y1

        xb = x
        yb = y
        steps = 0

        while x != x2 or y != y2:
            if stepmode == False:
                point_list.append([x, y, colour])
            if e >= 0:
                if exchange == 1:
                    x += sx
                else:
                    y += sy
                e -= 2 * dx
            if e <= 0:
                if exchange == 0:
                    x += sx
                else:
                    y += sy
                e += 2 * dy

            if stepmode:
                if xb != x and yb != y:
                    steps += 1
                xb = x
                yb = y

        if stepmode:
            return steps
    return point_list

def BrezenhemSmooth(canvas, x1, y1, x2, y2, fill="black", stepmode=False):
    point_list = []
    I = 100
    fill = get_rgb_intens(canvas, fill, CANVAS_COLOUR, I)
    dx = x2 - x1
    dy = y2 - y1
    sx = get_sign(dx)
    sy = get_sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    if dy >= dx:
        dx, dy = dy, dx
        steep = 1
    else:
        steep = 0
    tg = dy / dx * I 
    e = I / 2
    w = I - tg
    x = x1
    y = y1

    xb = x
    yb = y
    steps = 0

    while x != x2 or y != y2:
        if not stepmode:
            point_list.append([x, y, fill[round(e) - 1]])

        if e < w:
            if steep == 0:
                x += sx
            else:
                y += sy
            e += tg
        elif e >= w:
            x += sx
            y += sy 
            e -= w

        if stepmode:
            if xb != x and yb != y:
                steps += 1
            xb = x
            yb = y

    if stepmode:
        return steps
    return point_list
