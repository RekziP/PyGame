import pygame
pygame.init()

# Capture settings
FPS = 60
W = 1000
H = 800
caption_name = 'Asteroids'
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
font = pygame.font.SysFont('arialunicode', 30)
score_position = (20, 10)
lives_position = (W - 120, 10)
font_game_over = pygame.font.SysFont('applesdgothicneo', 100, bold=True)
game_over_position = (W//2-220, H//2-40)
background = 'images/background2.jpg'

# Ship settings:
ship = 'images/ship.png'
ship_start_pos = (10, H // 2)
ship_speed = 10
ship_size = (90, 45)
ship_start_degree = 0
ship_rotate = 5
ship_lives = 3

# Rocket settings:
rocket = 'images/rocket.png'
rocket_size = (45, 20)
rocket_speed = 10
rocket_live_time = H / (rocket_speed * 100)

# Asteroid settings:
asteroid = 'images/asteroid.png'
asteroid_op = 'images/asteroid_op.png'
asteroid_min_size = (90, 90)
asteroid_max_size = (180, 180)
asteroid_min_speed = 1
asteroid_max_speed = 5
asteroid_min_x = 4*W/5
asteroid_time_interval = 1 * 1000
