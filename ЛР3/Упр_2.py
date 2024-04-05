import pygame as pg
import sys


class Player(pg.sprite.Sprite):
    def __init__(self, filename, hero_x=400, hero_y=300, x_speed=0, y_speed=0):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename)
        self.rect = self.image.get_rect()
        self.hero_x = hero_x
        self.hero_y = hero_y
        self.rect.x = hero_x
        self.rect.y = hero_y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.x += self.x_speed

        # проверка, чтобы персонаж не выходил за границы экрана по X
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > window_width:
            self.rect.right = window_width

        self.rect.y += self.y_speed

        # проверка, чтобы персонаж не выходил за границы экрана по Y
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > window_height:
            self.rect.bottom = window_height

pg.init()

window_width = 800
window_height = 600
background_path = 'images/I.jpeg'
heroes_path = 'images/Dungeon_master.png'
background_speed = 1

window = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Соколанов Алексей")
master = Player(heroes_path)

img = pg.image.load(background_path)
background = pg.transform.scale(img, (window_width, window_height))

background_x = 0
background_speed = 0
hero_speed = 1  

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                master.y_speed = -hero_speed
            elif event.key == pg.K_DOWN:
                master.y_speed = hero_speed
            elif event.key == pg.K_LEFT:
                master.x_speed = -hero_speed
                background_speed = master.x_speed * 0.5
            elif event.key == pg.K_RIGHT:
                master.x_speed = hero_speed
                background_speed = master.x_speed * 0.5
        elif event.type == pg.KEYUP:
            if event.key in (pg.K_LEFT, pg.K_RIGHT):
                master.x_speed = 0
                background_speed = 0
            elif event.key in (pg.K_UP, pg.K_DOWN):
                master.y_speed = 0

    master.update()

    if (master.rect.left <= 0) or (master.rect.right >= window_width):
        try:
            background_x -= background_speed * master.x_speed / abs(master.x_speed)
        except:
            pass
        if background_x >= window_width:
            background_x -= window_width
        elif background_x <= -window_width:
            background_x += window_width

    # отрисовка фона
    window.blit(background, (background_x, 0))
    if background_x > 0:
        window.blit(background, (background_x - window_width, 0))
    else:
        window.blit(background, (background_x + window_width, 0))

    # отрисовка героя
    window.blit(master.image, master.rect)

    pg.display.flip()

pg.quit()
sys.exit()