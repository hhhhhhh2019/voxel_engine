import pygame as pg
from vec_math import Vec3#, Mat3
from Objects import Voxel
from Camera import Camera
from Settings import *
from math import radians


screen = pg.display.set_mode(RES)
clock = pg.time.Clock()

scene = [
    Voxel(Vec3(0, 0, 0), (0, 0, 0))
]

light = Vec3(0, -1, -1)

cam = Camera(Vec3(0, 0, -2), Vec3(0, 0, 0), CAM_RES)


while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()

        if e.type == pg.KEYDOWN:
            if e.key == pg.K_ESCAPE:
                exit()

    #cam.rotate_y(radians(3))

    scene[0].rotate_y(radians(10))

    cam.render(screen, scene, light)

    pg.display.flip()

    pg.display.set_caption(str(clock.get_fps()))

    clock.tick(60)
