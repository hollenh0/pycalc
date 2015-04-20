import math
import random


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def exponenets(a, b):
    return a ** b


def logarithm(a, b):
    return math.log(a, b)


def absolute_value(a):
    return math.fabs(a)


def square_root(a):
    return math.sqrt(a)


def sine(a):
    return math.sin(a)


def cosine(a):
    return math.cos(a)


def tangent(a):
    return math.tan(a)


def cosecant(a):
    sine = math.sin(a)
    return 1 / sine


def secant(a):
    cosine = math.cos(a)
    return 1 / cosine


def cotangent(a):
    tangent = math.tan(a)
    return 1 / tangent


def degrees_to_radians(a):
    return math.radians(a)


def radians_to_degrees(a):
    return math.degrees(a)


def quadratic_formula(a, b, c):
    part_aa = b * -1
    part_ab = a * 2
    part_a = part_aa / part_ab
    part_ba = b ** 2
    part_bb = -4 * a
    part_bc = part_bb * c
    part_bd = part_ba + part_bc
    if part_bd < 0:
        return 'undefined'
    else:
        part_be = math.sqrt(part_bd)
        part_b = part_be / part_ab
        first_x = part_a + part_b
        second_x = part_a - part_b
        return first_x, second_x


def rand_number(a, b):
    return random.randint(a, b)


def pythagorean_theorem_a(b, c):
    part_b = b ** 2
    part_c = c ** 2
    part_a_squared = part_c - part_b
    part_a = math.sqrt(part_a_squared)
    return part_a


def pythagorean_theorem_b(a, c):
    part_a = a ** 2
    part_c = c ** 2
    part_b_squared = part_c - part_a
    part_b = math.sqrt(part_b_squared)
    return part_b


def pythagorean_theorem_c(a, b):
    part_a = a ** 2
    part_b = b ** 2
    part_c_squared = part_a + part_b
    part_c = math.sqrt(part_c_squared)
    return part_c


def rectangle_perimeter(a, b):
    first_sides = a * 2
    second_sides = b * 2
    perimeter = second_sides + first_sides
    return perimeter


def rectangle_area(a, b):
    return a * b


def rectangle_diagonals(a, b):
    a_squared = a ** 2
    b_squared = b ** 2
    diagonal_squared = a_squared + b_squared
    diagonal = math.sqrt(diagonal_squared)
    return diagonal


def triangle_area(a, b):
    double_area = a * b
    area = double_area / 2
    return area


def triangle_perimeter(a, b, c):
    return a + b + c


def circle_area(a):
    squared_radius = a ** 2
    area = squared_radius * math.pi
    return area


def circle_circumference(a):
    double_radius = a * 2
    circumference = double_radius * math.pi
    return circumference


def sphere_volume(a):
    radius_cubed = a ** 3
    four_thirds = 4 / 3
    volume = radius_cubed * four_thirds * math.pi
    return volume


def sphere_surface_area(a):
    radius_squared = a ** 2
    surface_area = 4 * math.pi * radius_squared
    return surface_area


def cone_volume(a, b):
    new_height = b / 3
    radius_squared = a ** 2
    volume = new_height * radius_squared * math.pi
    return volume


def cone_surface_area(a, b):
    height_squared = b ** 2
    radius_squared = a ** 2
    part_e = height_squared + radius_squared
    part_ee = math.sqrt(part_e)
    part_ef = part_ee + a
    surface_area = math.pi * part_ef * a
    return surface_area


def prism_volume(a, b, c):
    volume = a * b * c
    return volume


def prism_surface_area(a, b, c):
    wl = a * b
    wh = b * c
    hl = a * c
    combined = wl + wh + hl
    surface_area = combined * 2
    return surface_area


def prism_diagonal(a, b, c):
    length_squared = a ** 2
    width_squared = b ** 2
    height_squared = c ** 2
    combined = length_squared + width_squared + height_squared
    diagonal = math.sqrt(combined)
    return diagonal


def cylinder_volume(a, b):
    radius_squared = a ** 2
    volume = math.pi * radius_squared * b
    return volume


def cylinder_surface_area(a, b):
    radius_squared = a ** 2
    part_b = 2 * math.pi * radius_squared
    part_a = 2 * math.pi * a * b
    surface_area = part_b + part_a
    return surface_area


def simple_interest(a, b, c):
    second_interest = b / 100
    third_interest = second_interest + 1
    final_amount = a * third_interest * c
    return final_amount


# d = how many times interest is compounded in a year
def compounded_interest(a, b, c, d):
    second_interest = b / 100
    part_aa = second_interest / d
    part_ab = 1 + part_aa
    part_b = c * d
    part_c = part_ab ** part_b
    final_amount = a * part_c
    return final_amount
