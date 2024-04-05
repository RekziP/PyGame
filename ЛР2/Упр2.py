import pygame
import random

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# инициализация pygame
pygame.init()

# параметры окна
width = 800
height = 600

# создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Соколанов Алексей")

# цвета
black = (0, 0, 0)
white = (255, 255, 255)

# параметры фигур
square_size = 50
rectangle_width = 70
rectangle_height = 40
circle_radius = 25
triangle_height = 50

# начальные координаты и скорости движения фигур
square_x, square_y = 50, 50
square_speed = 5
square_direction = 1

rectangle_x, rectangle_y = 50, 150
rectangle_speed = 3
rectangle_direction = 1

circle_x, circle_y = 50, 250
circle_speed = 4
circle_direction = 1

triangle_x, triangle_y = 50, 350
triangle_speed = 10
triangle_direction = 1

# цвета фигур
square_color = (255, 0, 0)
rectangle_color = (0, 255, 0)
circle_color = (0, 0, 255)
triangle_color = (255, 255, 0)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (square_x - square_size <= event.pos[0] <= square_x + square_size 
                        and square_y - square_size <= event.pos[1] <= square_y + square_size):
                    square_color = random_color()
                    
                if (rectangle_x - rectangle_width <= event.pos[0] <= rectangle_x + rectangle_width
                        and rectangle_y - rectangle_height <= event.pos[1] <= rectangle_y + rectangle_height):
                    rectangle_color = random_color()
                    
                if (triangle_x - triangle_height <= event.pos[0] <= triangle_x + triangle_height
                        and triangle_y - triangle_height <= event.pos[1] <= triangle_y + triangle_height):
                    triangle_color = random_color()
                    
                if (circle_x - circle_radius <= event.pos[0] <= circle_y + circle_radius
                        and circle_y - circle_radius <= event.pos[1] <= circle_y + circle_radius):
                    circle_color = random_color()

    # движение фигур
    square_x += square_speed * square_direction
    if square_x + square_size > width or square_x < 0:
        square_direction *= -1
        square_color = random_color()

    rectangle_x += rectangle_speed * rectangle_direction
    if rectangle_x + rectangle_width > width or rectangle_x < 0:
        rectangle_direction *= -1
        rectangle_color = random_color()

    circle_x += circle_speed * circle_direction
    if circle_x + circle_radius > width or circle_x - circle_radius < 0:
        circle_direction *= -1
        circle_color = random_color()

    triangle_x += triangle_speed * triangle_direction
    if triangle_x + triangle_height > width or triangle_x < 0:
        triangle_direction *= -1
        triangle_color = random_color()

    # отрисовка фигур
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))
    pygame.draw.rect(screen, rectangle_color, (rectangle_x, rectangle_y, rectangle_width, rectangle_height))
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)
    pygame.draw.polygon(screen, triangle_color, [(triangle_x, triangle_y), (triangle_x + triangle_height, triangle_y), (triangle_x + triangle_height / 2, triangle_y - 1.73 * triangle_height / 2)])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()