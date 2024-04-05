import pygame

# Инициализация pygame и создание экрана
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Цвет домика
color = (255, 255, 255)

# Создание линий для домика
lines = [[400, 100], [400, 200], [400, 300], [400, 400], [400, 500], [400, 600]]
pygame.draw.lines(screen, color, False, lines, 2)

# Создание линий для крыши
roof_lines = [[300, 200], [500, 200], [400, 300], [400, 400]]
pygame.draw.lines(screen, color, False, roof_lines, 2)

# Создание линий для окна
window_lines = [[300, 300], [500, 300], [400, 400], [400, 500]]
pygame.draw.lines(screen, color, False, window_lines, 2)

# Создание линий для двери
door_lines = [[350, 150], [450, 150], [400, 200], [400, 250]]
pygame.draw.lines(screen, color, False, door_lines, 2)

# Обновление экрана
pygame.display.flip()

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Завершение программы
pygame.quit()

