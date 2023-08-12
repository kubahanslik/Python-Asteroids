import math
import random
import Settings


class Asteroid:
    def __init__(self, image, window) -> None:
        self.window = window

        self.image = image
        self.rect = image.get_rect()

        self.velocity_x = 0
        self.velocity_y = 0



    def update(self):
        self.rect.centerx += self.velocity_x
        self.rect.centery -= self.velocity_y



    def draw(self):
        self.window.blit(self.image, self.rect)


    
    def isOut(self):
        return self.rect.right < -10 or self.rect.left > self.window.get_width() + 10 or self.rect.bottom < -10 or self.rect.top > self.window.get_height() + 10



class BigAsteroid(Asteroid):
    def __init__(self, image, window) -> None:
        super().__init__(image, window)

        spawn_side_chance = random.random()

        if spawn_side_chance < 0.25:
            self.rect.right = 0
            self.rect.centery = random.random() * self.window.get_height()

        elif spawn_side_chance < 0.5:
            self.rect.centerx = random.random() * self.window.get_width()
            self.rect.top = self.window.get_height()

        elif spawn_side_chance < 0.75:
            self.rect.left = self.window.get_width()
            self.rect.centery = random.random() * self.window.get_height()

        elif spawn_side_chance < 1:
            self.rect.centerx = random.random() * self.window.get_width()
            self.rect.bottom = 0

        c = math.sqrt((self.window.get_width()/2 - self.rect.centerx)**2 + (self.rect.centery - self.window.get_height()/2)**2)

        self.velocity_x = ((self.window.get_width()/2 - self.rect.centerx)/c) * Settings.ASTEROID_SPEED * (random.randrange(3, 11)/10)
        self.velocity_y = ((self.rect.centery - self.window.get_height()/2)/c) * Settings.ASTEROID_SPEED * (random.randrange(3, 11)/10)



class MidAsteroid(Asteroid):
    def __init__(self, position, image, window) -> None:
        super().__init__(image, window)

        self.rect.centerx = position[0]
        self.rect.centery = position[1]

        if random.random() < 0.5:
            self.velocity_x = -Settings.ASTEROID_SPEED * (random.randrange(3, 11)/10)
        else:
            self.velocity_x = Settings.ASTEROID_SPEED * (random.randrange(3, 11)/10)

        if random.random() < 0.5:
            self.velocity_y = -Settings.ASTEROID_SPEED * (random.randrange(3, 11)/10)
        else:
            self.velocity_y = Settings.ASTEROID_SPEED * (random.randrange(3, 11)/10)

class SmallAsteroid(MidAsteroid):
    def __init__(self, position, image, window) -> None:
        super().__init__(position, image, window)
