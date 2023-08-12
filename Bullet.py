import pygame as pg
import math
import Settings


class Bullet:
    def __init__(self, position, angle, window) -> None:
        self.rect = pg.Rect(position[0], position[1], 1, 1)

        self.window = window

        self.velocity_x = math.cos(math.radians(angle)) * Settings.BULLET_SPEED
        self.velocity_y = math.sin(math.radians(angle)) * Settings.BULLET_SPEED



    def isOut(self):
        return self.rect.centerx < 0 or self.rect.centerx > self.window.get_width() or self.rect.centery < 0 or self.rect.centery > self.window.get_height()



    def update(self):
        self.rect.centerx += self.velocity_x
        self.rect.centery -= self.velocity_y

    

    def draw(self):
        pg.draw.rect(self.window, 'white', self.rect)