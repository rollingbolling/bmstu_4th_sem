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

def brezenhem_ellipse(canvas, xc, yc ,ra, rb, colour, draw):
    x = 0
    y = rb

    if draw:
        draw_pixels(canvas, [x + xc, y + yc, colour], xc, yc, circle=True)

    sqr_ra = ra ** 2
    sqr_rb = rb ** 2
    delta =  sqr_rb - sqr_ra * (2 * rb + 1)

    while y >= 0:
        if delta < 0:
            d1 = 2 * delta + sqr_ra * (2 * y + 2)

            x += 1
            if d1 < 0:
                delta += sqr_rb * (2 * x + 1)
            else:
                y -= 1
                delta += sqr_rb * (2 * x + 1) + sqr_ra * (1 - 2 * y)
        elif delta > 0:
            d2 = 2 * delta + sqr_rb * (2 - 2 * x)

            y -= 1
            if d2 > 0:
                delta += sqr_ra * (1 - 2 * y)
            else:
                x += 1
                delta += sqr_rb * (2 * x + 1) + sqr_ra * (1 - 2 * y)
        else:
            y -= 1
            x += 1
            delta += sqr_rb * (2 * x + 1) + sqr_ra * (1 - 2 * y)

        if draw:
            draw_pixels(canvas, [x + xc, y + yc, colour], xc, yc, circle=False)
