from vec_math import Mat3, Vec3
from math import sin, cos


def rotate_x(a: float) -> Mat3:
    return Mat3(
        Vec3(1, 0, 0),
        Vec3(0, cos(a), -sin(a)),
        Vec3(0, sin(a), cos(a))
    )

def rotate_y(a: float) -> Mat3:
    return Mat3(
        Vec3(cos(a), 0, sin(a)),
        Vec3(0, 1, 0),
        Vec3(-sin(a), 0, cos(a))
    )

def rotate_z(a: float) -> Mat3:
    return Mat3(
        Vec3(cos(a), -sin(a), 0),
        Vec3(sin(a), cos(a), 0),
        Vec3(0, 0, 1)
    )
