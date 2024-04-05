import pygame
import sys
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Соколанов Алексей")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BROWN = (165, 42, 42)


# Draw house
def draw_house():
    screen.fill(WHITE)

    # Крыша
    pygame.draw.polygon(screen, RED, [(400, 100), (200, 300), (600, 300)])

    # Коробка
    pygame.draw.rect(screen, BROWN, (250, 300, 300, 300))

    pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_house()
