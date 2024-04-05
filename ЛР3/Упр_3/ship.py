import pygame
import config as conf
import math
import time

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ship_image = pygame.image.load(conf.ship).convert_alpha()
        self.ship_image = pygame.transform.scale(self.ship_image, conf.ship_size)
        self.original_ship_image = self.ship_image
        self.rect = self.ship_image.get_rect(center=conf.ship_start_pos)
        self.speed = conf.ship_speed
        self.angle = conf.ship_start_degree
        # Координаты носа корабля:
        self.head = [self.rect.right, (self.rect.topright[1] - self.rect.bottomright[1]) / 2 + self.rect.bottomright[1]]
        self.radius = abs(self.rect.center[0] - self.rect.right)


    def move(self):
        x1, y1 = self.rect.center
        x2, y2 = self.head[0], self.head[1]

        if round(x2 - x1, 5) != 0:
            tangens = (y2 - y1)/(x2 - x1)
            cosinus = math.sqrt(1/(1+tangens**2))
            x = self.speed * cosinus * (-1 if self.head[0] < x1 else 1) + x1
            y = ((x - x1)/(x2-x1))*(y2-y1) + y1
        else:
            x, y = x1, y1 + self.speed * (-1 if y2 < y1 else 1)

        if not 0 <= x < conf.W:
            if isinstance(self, Rocket):
                self.kill()
            x = abs(conf.W - abs(x))

        if not 0 <= y < conf.H:
            if isinstance(self, Rocket):
                self.kill()
            y = abs(conf.H - abs(y))

        self.rect.center = (x, y)
        self.head = [(self.radius * math.cos(math.radians(-self.angle)) + self.rect.center[0]),
                     (self.radius * math.sin(math.radians(-self.angle)) + self.rect.center[1])]


    def rotate(self, left=True):
        position = self.rect.center
        self.angle += conf.ship_rotate * (1 if left else -1)
        self.ship_image = pygame.transform.rotate(self.original_ship_image, self.angle)
        self.rect = self.ship_image.get_rect(center=position)
        self.head = [(self.radius * math.cos(math.radians(-self.angle)) + self.rect.center[0]),
                    (self.radius * math.sin(math.radians(-self.angle)) + self.rect.center[1])]

    def shot(self):
        return Rocket(self)

    def angle_of_rotate(self):
        """
        Функция нужна для расчета угла, на который нам нужно будет повернуть ракету
        """
        x1, y1 = self.rect.center
        x2, y2 = self.head[0], self.head[1]
        if round((x2 - x1), 5) != 0:
            tangens = (y2 - y1) / (x2 - x1)
            angle = math.degrees(math.atan(-tangens)) + (180 if x2 < x1 else 0)
        else:
            angle = 90 + (180 if y2 > y1 else 0)
        return angle


class Rocket(Ship):
    def __init__(self, ship):
        super().__init__()
        self.ship = ship
        self.image = pygame.image.load(conf.rocket).convert_alpha()
        self.image = pygame.transform.scale(self.image, conf.rocket_size)
        self.original_image = self.image
        self.rect = self.image.get_rect(center=ship.head)
        self.speed = conf.rocket_speed
        self.head = [self.rect.right, (self.rect.topright[1] - self.rect.bottomright[1]) / 2 + self.rect.bottomright[1]]
        self.radius = abs(self.rect.center[0] - self.rect.right)
        self.angle = ship.angle_of_rotate()
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.born_time = time.time()

    def update(self):
        super().move()
        if time.time() - self.born_time >= conf.rocket_live_time:
            self.kill()


