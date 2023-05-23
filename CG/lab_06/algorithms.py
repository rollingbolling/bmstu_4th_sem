from config import *

EPS = 1e-6

class Point:
    def __int__(self):
        self.x = 0
        self.y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equal_points(self, x, y):
        if (abs(x - self.x) < EPS and abs(y - self.y) < EPS):
            return True
        return False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y

def draw_pixel(img, x, y, colour):
    img.put(colour, (x, y))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def rgb(colour):
    return (int(colour[1:3], 16), int(colour[3:5], 16), int(colour[5:7], 16))

def fill_with_seed(canvas, img, border_colour, fill_colour, seed_point, delay=False):
    fill_colour_rgb = rgb(fill_colour)
    border_colour_rgb = rgb(border_colour)

    stack = [seed_point]
    while stack:
        seed_pixel = stack.pop()
        x = seed_pixel.x
        y = seed_pixel.y

        draw_pixel(img, x, y, fill_colour)
        tx = x
        ty = y

        
        #right
        x += 1
        while img.get(x, y) != fill_colour_rgb and \
              img.get(x, y) != border_colour_rgb and x < CANVAS_W:
            draw_pixel(img, x, y, fill_colour)
            x += 1

        xr = x - 1
        #left
        x = tx - 1
        while img.get(x, y) != fill_colour_rgb and \
              img.get(x, y) != border_colour_rgb and x > 0:
            draw_pixel(img, x, y, fill_colour)
            x -= 1

        xl = x + 1
        #up
        x = xl
        if ty < CANVAS_H:
            y = ty + 1

            while x <= xr:
                flag = False

                while img.get(x, y) != fill_colour_rgb and \
                      img.get(x, y) != border_colour_rgb and x <= xr:
                    flag = True
                    x += 1

                # Помещаем в стек крайний справа пиксель

                if flag:
                    if x == xr and img.get(x, y) != fill_colour_rgb and \
                                   img.get(x, y) != border_colour_rgb:
                        if y < CANVAS_H:
                            stack.append(Point(x, y))
                    else:
                        if y < CANVAS_H:
                            stack.append(Point(x - 1, y))

                    flag = False

                # Продолжаем проверку, если интервал был прерван

                x_in = x
                while (img.get(x, y) == fill_colour_rgb or
                       img.get(x, y) == border_colour_rgb) and x < xr:
                    x = x + 1

                if x == x_in:
                    x += 1
        #down
        x = xl
        y = ty - 1

        while x <= xr:
            flag = False

            while img.get(x, y) != fill_colour_rgb and \
                  img.get(x, y) != border_colour_rgb and x <= xr:
                flag = True
                x += 1

            # Помещаем в стек крайний справа пиксель

            if flag:

                if x == xr and img.get(x, y) != fill_colour_rgb and \
                        img.get(x, y) != border_colour_rgb:
                    if y > 0:
                        stack.append(Point(x, y))
                else:
                    if y > 0:
                        stack.append(Point(x - 1, y))

                flag = False

            # Продолжаем проверку, если интервал был прерван

            x_in = x
            while (img.get(x, y) == fill_colour_rgb or
                   img.get(x, y) == border_colour_rgb) and x < xr:
                x = x + 1

            if x == x_in:
                x += 1

        if delay:
            canvas.update()

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def bresenhem_int(beg_point, end_point):
    dx = end_point.x - beg_point.x
    dy = end_point.y - beg_point.y

    if dx == 0 and dy == 0:
        return [Point(beg_point.x, beg_point.y)]

    x_sign = sign(dx)
    y_sign = sign(dy)

    dx = abs(dx)
    dy = abs(dy)

    if dy > dx:
        dx, dy = dy, dx
        exchange = 1
    else:
        exchange = 0

    two_dy = 2 * dy
    two_dx = 2 * dx

    e = two_dy - dx

    x = beg_point.x
    y = beg_point.y
    points = []

    i = 0
    while i <= dx:
        points.append(Point(x, y))

        if e >= 0:
            if exchange == 1:
                x += x_sign
            else:
                y += y_sign

            e -= two_dx

        if exchange == 1:
            y += y_sign
        else:
            x += x_sign

        e += two_dy
        i += 1

    return points
