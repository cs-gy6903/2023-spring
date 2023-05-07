# -*- coding: utf-8 -*-
"""
For this assignment we will be using EC curve: y**2 = x**3 + ax + b (mod p)

https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication
"""


def multiplicative_inverse(i: int, p: int) -> int:
    """
    Compute multiplicative inverse of i for modulus p

    It needs to be smallest positive integer modular multiplicative inverse

    More on wikipedia:
    https://en.wikipedia.org/wiki/Modular_multiplicative_inverse

    Hint you can use pow() built-in function

    >>> multiplicative_inverse(10, 17)
    12
    >>> multiplicative_inverse(5, 17)
    7
    """
    return 0  # TODO: this is a placeholder, add your solution here


def point_negate(a: int, b: int, p: int, x: int, y: int) -> tuple:
    """
    Negate a point (x, y) on curve (a, b, p)

    https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Point_negation

    Remember all we are trying to do is to flip point around x-axis
    (flipping y coordinate) so we can sipmly use the formula:

    (x, -y) == -(x, y)

    >>> point_negate(a=2, b=3, p=17, x=5, y=11)
    (5, 6)
    """
    return 0, 0  # TODO: this is a placeholder, add your solution here


def point_add(a: int, b: int, p: int, x1: int, y1: int, x2: int, y2: int) -> tuple:
    """
    Add point (x1, y1) to point (x2, y2) on curve (a, b, p)

    https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Point_addition

    You will need to compute the lambda (slope) which is:

    slope = y2 - y1
            -------
            x2 - x1

    Remember that instead of division we are multiplying by mod inverse.

    Then you can use slope to get the new point which is the result of the point
    addition:

    x = slope ** 2 - x1 - x2
    y = slope(x1 - x) - y1

    >>> point_add(a=2, b=3, p=17, x1=15, y1=5, x2=5, y2=11)
    (13, 4)
    >>> point_add(a=2, b=3, p=17, x2=15, y2=5, x1=5, y1=11)
    (13, 4)
    """
    return 0, 0  # TODO: this is a placeholder, add your solution here


def point_double(a: int, b: int, p: int, x: int, y: int) -> tuple:
    """
    Double (add to itself) a point (x, y) on curve (a, b, p)

    https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Point_doubling

    Doubling is similar to addtion except computing slope is different:

    slope = 3 * x1**2 + a
            -------------
            2 * y1

    >>> point_double(a=2, b=3, p=17, x=5, y=11)
    (15, 5)
    """
    return 0, 0  # TODO: this is a placeholder, add your solution here


def point_multiply(a: int, b: int, p: int, x: int, y: int, n: int) -> tuple:
    """
    Multiply point (x, y) by n on curve (a, b, p)

    https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Double-and-add

    Now that we can:

    * negate points
    * double them
    * add 2 points

    we can implement point multiplication where multiplying by:

    * 1 == point itself
    * 2 == point double
    * x == point added x times. double and add method make this easy
    * -1 == point negation
    * -x == x * -1 (negate point and then multiply by positive multiplier)

    Instead of adding same point many-many times, double and add method should be used
    to make that operation much simpler. For example:
    p * 3 == p + p + p         == (p * 2) + p
    p * 5 == p + p + p + p + p == (p * 2) + (p * 2) + p == (p * 2) * 2 + p

    >>> point_multiply(a=2, b=3, p=17, x=5, y=11, n=-1)
    (5, 6)
    >>> point_multiply(a=2, b=3, p=17, x=5, y=11, n=1)
    (5, 11)
    >>> point_multiply(a=2, b=3, p=17, x=5, y=11, n=2)
    (15, 5)
    >>> point_multiply(a=2, b=3, p=17, x=5, y=11, n=3)
    (13, 4)
    >>> point_multiply(a=2, b=3, p=17, x=5, y=11, n=4)
    (8, 15)
    >>> point_multiply(a=2, b=3, p=17, x=5, y=11, n=5)
    (2, 10)
    >>> point_multiply(a=106, b=18, p=107, x=52, y=61, n=-37)
    (82, 19)
    """
    return 0, 0  # TODO: this is a placeholder, add your solution here


def ecdh_agreement(
    a: int,
    b: int,
    p: int,
    x_A: int,
    y_A: int,
    d_A: int,
    x_B: int,
    y_B: int,
    d_B: int,
) -> int:
    """
    Given:
        1. curve (a, b, p)
        2. Alice's public key A as point (x_A, y_A)
        3. Alice's private key as scalar d_A
        4. Bob's public key B as point (x_B, y_B)
        5. Bob's private key as scalar d_B

    Compute and return the shared secret.

    The steps to do this are roughly as follows (including optional steps for
    validating your solution with asserts):

        1. Compute point k_A = B * d_A
        2. Compute point k_B = A * d_B (optional)
        3. Assert that k_A == k_B (optional)
        4. Return the x coordinate of k_A as the shared secret

    Reference:

    https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman#Key_establishment_protocol

    >>> ecdh_agreement(a=31, b=49, p=107, x_A=49, y_A=74, d_A=53, x_B=42, y_B=2, d_B=40)
    12
    >>> ecdh_agreement(a=17, b=4, p=107, x_A=104, y_A=56, d_A=70, x_B=37, y_B=51, d_B=55)
    53
    >>> ecdh_agreement(a=163, b=141, p=179, x_A=103, y_A=6, d_A=76, x_B=90, y_B=148, d_B=42)
    33
    >>> ecdh_agreement(a=70, b=4, p=179, x_A=150, y_A=16, d_A=65, x_B=138, y_B=23, d_B=140)
    138
    """
    return 0  # TODO: this is a placeholder, add your solution here
