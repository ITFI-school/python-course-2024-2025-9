''' A unit with geometry functions for triangles
'''

import math


def area(base, height):
    '''(number, number) -> number

    Return the area of a triangle with given base and height
    Precondition: base and height must be positive, otherwise -> 0

    >>> area(10, 40)
    200.0
    >>> area(3.4, 7.5)
    12.75
    >>> area(-1, 2)
    0
    '''
    if base<0 or height<0:
        return 0

    return base * height / 2


def perimeter(side1, side2, side3):
    '''(number, number, number) -> number

    Return the perimeter of a triangle with given side sizes
    Precondition: sides must be positive, otherwise -> 0

    >>> perimeter(3, 4, 5)
    12.0
    >>> perimeter(10.5, 6, 9.3)
    25.8
    >>> perimeter(-1,2,3)
    0
    '''
    if side1<0 or side2<0 or side3<0:
        return 0

    return side1 + side2 + side3


def semiperimeter(side1, side2, side3):
    '''(number, number, number) -> float

    Return the semiperimeter of a triangle with sides of length side1, side2 and side3
    Precondition: sides must be positive, otherwise -> 0

    >>> semiperimeter(3, 4, 5)
    6.0
    >>> semiperimeter(10.5, 6, 9.3)
    12.9
    >>> semiperimeter(-1,2,3)
    0
    '''
    return perimeter(side1, side2, side3) / 2


def area_heron(side1, side2, side3):
    '''(number, number, number) -> float

    Return the area of a triangle by Heron formula, calculated with sides of length side1, side2 and side3
    Precondition: sides must be positive, otherwise -> 0

    >>> area_heron(3, 4, 5)
    6.0
    >>> area_heron(10.5, 6, 9.3)
    27.73168584850189
    >>> area_heron(-1,2,3)
    0
    '''
    semi = semiperimeter(side1, side2, side3)
    area = math.sqrt(semi * (semi - side1) * (semi - side2) * (semi - side3))
    return area
