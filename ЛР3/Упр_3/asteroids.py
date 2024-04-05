import pygame
import config as conf
import random


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, height, width, speed, image):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed


def create_asteroid(image):
    x = random.randint(conf.asteroid_min_x, conf.W)
    y = random.randint(0, conf.H)
    speed = random.randint(conf.asteroid_min_speed, conf.asteroid_max_speed)
    width = random.randint(conf.asteroid_min_size[0], conf.asteroid_max_size[0])
    height = width
    return Asteroid(x, y, height, width, speed, image)


def collide_asteroid(ship, rockets, asteroids, game_score, lives):
    for asteroid in asteroids:
        if asteroid.rect.collidepoint(ship.head):
            lives -= 1
            ship.rect.center = conf.ship_start_pos
            break
        for rocket in rockets:
            if asteroid.rect.collidepoint(rocket.rect.center):
                game_score += 1
                asteroid.kill()
                rocket.kill()
                break
    return game_score, lives
