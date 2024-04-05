import pygame
import config as conf
from ship import Ship
from asteroids import create_asteroid, collide_asteroid

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, conf.asteroid_time_interval)

sc = pygame.display.set_mode((conf.W, conf.H))
pygame.display.set_caption(conf.caption_name)
clock = pygame.time.Clock()
background = pygame.image.load(conf.background).convert()
background = pygame.transform.scale(background, (conf.W, conf.H))

ship = Ship()
rockets = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
game_score = 0
lives = conf.ship_lives
is_started = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN and is_started:
            if event.key == pygame.K_SPACE:
                rockets.add(ship.shot())

        if event.type == pygame.USEREVENT:
            image = conf.asteroid if is_started else conf.asteroid_op
            asteroids.add(create_asteroid(image))

        if event.type == pygame.MOUSEBUTTONDOWN and not is_started:
            asteroids = pygame.sprite.Group()
            is_started = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and is_started:
        ship.rotate(left=True)

    if keys[pygame.K_RIGHT] and is_started:
        ship.rotate(left=False)

    if keys[pygame.K_UP] and is_started:
        ship.move()

    # Фиксирование столкновений
    if is_started:
        old_lives = lives
        game_score, lives = collide_asteroid(ship, rockets, asteroids, game_score, lives)
        if lives < old_lives:
            asteroids = pygame.sprite.Group()

    # Отрисовка поля и очков
    sc.blit(background, (0, 0))
    sc_score = conf.font.render(f'Score: {game_score}', 1, conf.GREEN, conf.WHITE)
    sc.blit(sc_score, conf.score_position)
    sc_lives = conf.font.render(f'Lives: {lives}', 1, conf.RED, conf.WHITE)
    sc.blit(sc_lives, conf.lives_position)

    # Остановка игры при 0 жизней
    if lives <= 0:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                ship = Ship()
                rockets = pygame.sprite.Group()
                asteroids = pygame.sprite.Group()
                game_score = 0
                lives = conf.ship_lives
                break

            sc_game_over = conf.font_game_over.render(f'Game Over', 1, conf.RED)
            sc.blit(sc_game_over, conf.game_over_position)

            pygame.display.update()
            clock.tick(conf.FPS)
        continue

    # Отрисовка корабля
    if is_started:
        sc.blit(ship.ship_image, ship.rect)

    # Отрисовка ракет
    rockets.draw(sc)
    rockets.update()

    # Отрисовка астероидов
    asteroids.draw(sc)
    asteroids.update()

    # Начальный экран:
    if not is_started:
        sc_get_started = conf.font_game_over.render(f'Get started', 1, conf.GREEN)
        sc.blit(sc_get_started, conf.game_over_position)

    # Обновление дисплея
    pygame.display.update()

    clock.tick(conf.FPS)

