from vec_math import Vec3, norm#, dot, distance
import pygame as pg
from Settings import *
from Matrix import rotate_x, rotate_y, rotate_z
from threading import Thread
from numba import jit


#def light(p: Vec3, ld: Vec3) -> float:
#    return 1#max(min(dot(p, ld) * 0.5 + 0.5 , 1), 0)


class Camera:
    def __init__(self, pos: Vec3, rot: Vec3, res: tuple):
        self.pos, self.rot, self.res = pos, rot, res

    def rotate_x(self, a: float):
        self.rot.x += a

    def rotate_y(self, a: float):
        self.rot.y += a

    def rotate_z(self, a: float):
        self.rot.z += a

    @staticmethod
    def trayce(o, d, v, ld):
        p = o

        while (o - p).size < 5:
            if v.is_intersect(p):
                l = 1#light(p - v.pos, ld)
                return int(255 * l), int(255 * l), int(255 * l)

            p += d * 0.5

        return 0, 0, 0

    def row(self, scene, screen, y, w, h, ld):
        for x in range(self.res[0]):
            d = norm(Vec3(x/self.res[0]*2-1, y/self.res[1]*2-1, 1))

            d *= rotate_x(self.rot.x)
            d *= rotate_y(self.rot.y)
            d *= rotate_z(self.rot.z)

            c = (0, 0, 0)

            for o in scene:
                c = self.trayce(self.pos, d, o, ld)

            pg.draw.rect(screen, c, pg.Rect(x * w, y * h, w, h))
        
    @jit(forceobj = True)
    def render(self, screen: pg.Surface, scene: list, ld: Vec3):
        w, h = WIDTH / self.res[0], HEIGHT / self.res[1]

        self.thread_count = self.res[1]

        for y in range(self.res[1]):
            #thr = Thread(target = self.row, args = (scene, screen, y, w, h, ld))

            #thr.start()
            #self.row(scene, screen, y, w, h, ld)

            for x in range(self.res[0]):
                d = norm(Vec3(x/self.res[0]*2-1, y/self.res[1]*2-1, 1))

                d *= rotate_x(self.rot.x)
                d *= rotate_y(self.rot.y)
                d *= rotate_z(self.rot.z)

                c = (0, 0, 0)

                for o in scene:
                    c = self.trayce(self.pos, d, o, ld)

                pg.draw.rect(screen, c, pg.Rect(x * w, y * h, w, h))





















