import pygame as pg
import random
from Ship import Ship
import Bullet
import Settings
import Asteroid


class Game:
    def __init__(self) -> None:
        pg.init()
        
        self.clock = pg.time.Clock()

        self.window = pg.display.set_mode(Settings.WINDOW_SIZE)
        pg.display.set_caption("Asteroids")

        self.ship = Ship(self.window)
        self.bullets = []
        self.asteroids = []


    

    def collisions(self):
        for bullet in self.bullets:
            if bullet.isOut():
                self.bullets.remove(bullet)
        for asteroid in self.asteroids:
            if asteroid.isOut():
                self.asteroids.remove(asteroid)
            if any([pg.Rect.collidepoint(asteroid.rect, pos[0], pos[1]) for pos in self.ship.positions]):
                exit()
            for bullet in self.bullets:
                if pg.Rect.colliderect(asteroid.rect, bullet.rect):
                    self.ship.bullet_hit()
                    if type(asteroid) == Asteroid.BigAsteroid:
                        [self.asteroids.append(Asteroid.MidAsteroid(asteroid.rect.center, pg.image.load("resources/medium_asteroid.png"), self.window)) for x in range(2)]
                    elif type(asteroid) == Asteroid.MidAsteroid:
                        [self.asteroids.append(Asteroid.SmallAsteroid(asteroid.rect.center, pg.image.load("resources/small_asteroid.png"), self.window)) for x in range(2)]
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)

    

    def update(self):
        self.ship.update()
        for bullet in self.bullets:
            bullet.update()
        for asteroid in self.asteroids:
            asteroid.update()



    def draw(self):
        self.window.fill('black')

        for bullet in self.bullets:
            bullet.draw()
        for asteroid in self.asteroids:
            asteroid.draw()
        self.ship.draw()

        pg.display.update()



    def main(self):
        while True:
            pg.display.set_caption(str(1000/self.clock.tick(Settings.FPS)))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.bullets.append(Bullet.Bullet(self.ship.pos1, self.ship.angle, self.window))
            
            keys = pg.key.get_pressed()
            if keys[pg.K_a]:
                self.ship.rotate("left")
            if keys[pg.K_d]:
                self.ship.rotate("right")
            if keys[pg.K_w]:
                self.ship.move()

            if random.random() < Settings.SPAWN_CHANCE:
                self.asteroids.append(Asteroid.BigAsteroid(pg.image.load("resources/big_asteroid.png"), self.window))

            self.update()
            self.collisions()
            self.draw()
        
        pg.quit()



if __name__ == '__main__':
    Game().main()