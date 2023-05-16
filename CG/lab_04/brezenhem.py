from draw import *

def brezenhem_circle(canvas, xc, yc, r, colour, draw):
    x = 0
    y = r
    if draw:
        draw_pixels(canvas, [x + xc, y + yc, colour], xc, yc, circle=True)

    delta = 2 * (1 - r)

    while y >= 0:
        if delta < 0:
            d1 = 2 * delta + 2 * y - 1
            if d1 <= 0:
                x += 1
                delta += 2 * x + 1
            elif d1 > 0:
                x += 1
                y -= 1
                delta += 2 * (x - y + 1)
        elif delta > 0:
            d2 = 2 * delta + 2 * x - 1
            if d2 <= 0:
                x += 1
                y -= 1
                delta += 2 * (x - y + 1)
            elif d2 > 0:
                y -= 1
                delta -= 2 * y + 1
        else:
            x += 1
            y -= 1
            delta += 2 * (x - y + 1)

        if draw:
            draw_pixels(canvas, [x + xc, y + yc, colour], xc, yc, circle=True)