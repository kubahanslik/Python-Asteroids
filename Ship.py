import pygame as pg
import math
import Settings


class Ship:
    def __init__(self, window) -> None:
        self.window = window

        self.score = 0
        self.score_font = pg.font.SysFont(Settings.SCORE_FONT, Settings.SCORE_FONT_SIZE)
        self.score_surface = self.score_font.render(str(self.score), True, 'white', 'black')

        self.center_x = window.get_width()//2
        self.center_y = window.get_height()//2
        self.angle = 90
        self.positions = self.pos1, self.pos2, self.pos3 = [(self.center_x + math.cos(math.radians(self.angle)) * Settings.SHIP_HALF_HEIGHT, self.center_y - math.sin(math.radians(self.angle)) * Settings.SHIP_HALF_HEIGHT), 
                                                            (self.center_x + math.cos(math.radians(self.angle + Settings.SHIP_ALFA)) * Settings.SHIP_C, self.center_y - math.sin(math.radians(self.angle + Settings.SHIP_ALFA)) * Settings.SHIP_C), 
                                                            (self.center_x + math.cos(math.radians(self.angle - Settings.SHIP_ALFA)) * Settings.SHIP_C, self.center_y - math.sin(math.radians(self.angle - Settings.SHIP_ALFA)) * Settings.SHIP_C)]
        self.velocity_x = 0
        self.velocity_y = 0



    def bullet_hit(self):
        self.score += Settings.SCORE_GAIN
        self.score_font = pg.font.SysFont(Settings.SCORE_FONT, Settings.SCORE_FONT_SIZE)
        self.score_surface = self.score_font.render(str(self.score), True, 'white', 'black')
                                


    def rotate(self, direction):
        if direction == "left":
            self.angle += Settings.SHIP_ROTATE_SPEED
        elif direction == "right":
            self.angle -= Settings.SHIP_ROTATE_SPEED
        


    def move(self):
        if math.sqrt(self.velocity_x**2 + self.velocity_y**2) < Settings.SHIP_MAX_SPEED:
            self.velocity_x += math.cos(math.radians(self.angle)) * Settings.SHIP_ACCELERATION
            self.velocity_y += math.sin(math.radians(self.angle)) * Settings.SHIP_ACCELERATION



    def update(self):
        self.center_x += self.velocity_x
        self.center_y -= self.velocity_y

        if self.center_x < 0:
            self.center_x = self.window.get_width()
        elif self.center_x > self.window.get_width():
            self.center_x = 0
        if self.center_y < 0:
            self.center_y = self.window.get_height()
        elif self.center_y > self.window.get_height():
            self.center_y = 0

        speed = math.sqrt(self.velocity_x**2 + self.velocity_y**2)

        if self.velocity_x > 0:
            self.velocity_x -= Settings.SHIP_DEACCELERATION * (abs(self.velocity_x)/speed)
        elif self.velocity_x < 0:
            self.velocity_x += Settings.SHIP_DEACCELERATION * (abs(self.velocity_x)/speed)
        if self.velocity_y > 0:
            self.velocity_y -= Settings.SHIP_DEACCELERATION * (abs(self.velocity_y)/speed)
        elif self.velocity_y < 0:
            self.velocity_y += Settings.SHIP_DEACCELERATION * (abs(self.velocity_y)/speed)

        if  -Settings.SHIP_DEACCELERATION < self.velocity_x < Settings.SHIP_DEACCELERATION:
            self.velocity_x = 0
        if  -Settings.SHIP_DEACCELERATION < self.velocity_y < Settings.SHIP_DEACCELERATION:
            self.velocity_y = 0

        self.positions = self.pos1, self.pos2, self.pos3 = [(self.center_x + math.cos(math.radians(self.angle)) * Settings.SHIP_HALF_HEIGHT, self.center_y - math.sin(math.radians(self.angle)) * Settings.SHIP_HALF_HEIGHT),
                                                            (self.center_x + math.cos(math.radians(self.angle + Settings.SHIP_ALFA)) * Settings.SHIP_C, self.center_y - math.sin(math.radians(self.angle + Settings.SHIP_ALFA)) * Settings.SHIP_C), 
                                                            (self.center_x + math.cos(math.radians(self.angle - Settings.SHIP_ALFA)) * Settings.SHIP_C, self.center_y - math.sin(math.radians(self.angle - Settings.SHIP_ALFA)) * Settings.SHIP_C)]



    def draw(self):
        pg.draw.polygon(self.window, 'white', self.positions)
        self.window.blit(self.score_surface, (Settings.SCORE_TOP, Settings.SCORE_LEFT))
