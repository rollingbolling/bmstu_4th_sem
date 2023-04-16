from math import sqrt, acos, sin, pi
from Point import *

def points_on_one_line(a, b, c):
    if abs((c.x - a.x) * (b.y - b.y) - (b.x - a.x) * (c.y - a.y)) > EPS: 
        return 1
    return 0

def get_radius(center, a):
    dx = center.x - a.x
    dy = center.y - a.y
    return round(sqrt(dx * dx + dy * dy), 3)

def get_center(a, b, c):
    d1 = {"x" : (b.y - a.y),
          "y" : (a.x - b.x)}
    d2 = {"x" : (c.y - a.y), 
          "y" : (a.x - c.x)}
    k = d2["x"] * d1["y"] - d2["y"] * d1["x"]
    if abs(k) <= EPS:
        return 0
    s1 = {"x" : (a.x + b.x) / 2, 
          "y" : (a.y + b.y) / 2}
    s2 = {"x" : (a.x + c.x) / 2, 
          "y" : (a.y + c.y) / 2}
    l = d1["x"] * (s2["y"] - s1["y"]) - d1["y"] * (s2["x"] - s1["x"])
    m = l / k
    center = Point(round(s2["x"] + m * d2["x"], 3),
                   round(s2["y"] + m * d2["y"], 3))
    return center

def get_area_inters(circle_1, circle_2):
    d = get_radius(circle_1[0], circle_2[0])
    r = circle_1[1]
    R = circle_2[1]
    if d >= (r + R):
        return 0
    if r > R:
        r = circle_2[1]
        R = circle_1[1]
    if d <= abs(r - R) and (r >= R or r < R):
        return -2
    
    angle1 = (r**2 + d ** 2 - R**2) / (2 * r * d)
    angle2 = (R**2 + d ** 2 - r**2) / (2 * R * d)

    # check if the circles are overlapping
    if (-1 <= angle1 < 1) or (-1 <= angle2 < 1):
        theta1 = acos(angle1) * 2
        theta2 = acos(angle2) * 2

        area1 = (0.5 * theta2 * R**2) - (0.5 * R**2 * sin(theta2))
        area2 = (0.5 * theta1 * r**2) - (0.5 * r**2 * sin(theta1))

        return area1 + area2
    elif angle1 < -1 or angle2 < -1:
        # Smaller circle is completely inside the largest circle.
        # Intersection area will be area of smaller circle
        # return area(c1_r), area(c2_r)
        return pi * min(r, R) ** 2
    return 0

def get_amount_points_in_area(circle_1, circle_2, point_list):
    amount = 0
    for point in point_list:
        if (get_radius(circle_1[0], point) < circle_1[1] or get_radius(circle_2[0], point) < circle_2[1]):
            amount += 1

    return amount
