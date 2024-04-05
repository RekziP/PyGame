import pygame as pg
import time

pg.init()

# Глобальные переменные (настройки)
window_width = 800
window_height = 600
background_path = 'images/I.jpeg'

# Параметры окна:
window = pg.display.set_mode([window_width, window_height])
pg.display.set_caption('Соколанов Алексей')

# Параметры фона
speed = 0
background_shift = 0

# Загрузка фона
img = pg.image.load(background_path)
background = pg.transform.scale(img, (window_width, window_height))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                speed = 5
            elif event.key == pg.K_RIGHT:
                speed = -5
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                speed = 0

    background_shift = (background_shift + speed) % window_width
    window.blit(background, (background_shift, 0))
    # Продолжение фона:
    if background_shift != 0:
        window.blit(background, (background_shift - window_width, 0))

    pg.display.update()

pg.quit()