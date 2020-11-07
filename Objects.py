from vec_math import Vec3, Mat3
from Matrix import rotate_x, rotate_y, rotate_z


class Voxel:
    def __init__(self, pos: Vec3, color: tuple):
        self.pos, self.color = pos, color
        self.rot = Vec3(0, 0, 0)

        #self.pos += Vec3(1, 1, 1)

    def rotate_x(self, a: float):
        self.rot.x += a

    def rotate_y(self, a: float):
        self.rot.y += a

    def rotate_z(self, a: float):
        self.rot.z += a

    def is_intersect(self, p: Vec3) -> bool:
        b = self.pos

        p *= rotate_x(self.rot.x)
        p *= rotate_y(self.rot.y)
        p *= rotate_z(self.rot.z)
        
        return b.x - 0.5 <= p.x <= b.x + 0.5 and b.y - 0.5 <= p.y <= b.y + 0.5 and b.z - 0.5 <= p.z <= b.z + 0.5
