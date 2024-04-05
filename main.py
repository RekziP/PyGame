import pygame
import random
pygame.init()
screen=pygame.display.set_mode ((800, 600), pygame. RESIZABLE)
screen.fil1([255,255,255]) #белый фон. Аналог записи screen. fill ('white')
pygame.display.set_caption ( 'Первая программа в руате')
#создание кругов с разными способами задания цвета pygame.draw.circle (screen, 'red', [200,1001,30,width=0) #30-радиус в пикселях,width-ширина контура
pygame.draw.circle(screen, [255,154, 13], [100,400], 50,width=15) pygame.draw.circle (screen, '#FFEE54', [400,3001,100, width=5)
# создать прямоугольник
pygame.draw.rect (screen, 'yellow', [400,20,300,2001, 0) # [400,20,300, 200] - x, Y, ширина, высота
#создать пять рандомных по размеру и положению прямоугольников
for i in range (5):
top=random. randint (50,700)
left=random. randint (50, 500)
W=random. randint (10,200)
h=random. randint (10,100)
color=[random. randint (0,255), random.randint (0,255) , random.randint (0,255)] pygame.draw.rect (screen, color, [top, left,w,h], 4)
#создать произвольную фигуру из линий
dots=[[221,4321,[225,3311, [133,3421, [141,3101,
[51,2301,174,2171, 158,1531,1114,1641,
[123, 1351, [176,1901, 1159,771, 1193,931,
(230,281,1267,931,1301,771,1284,1901,
[327,1351, (336,1641, (402,1531, [386,217],
[409,2301, [319,3101,1327,3421,1233,3311,
[237,432]]
pygame.draw.lines (screen, 'green', True, dots, 2) #closed=True первая и последняя точка соединены
#яблоко на экране
apple=pygame.image.load ('apple.png')
screen.blit (apple, [400,450]) #копирование пикселей с растрового изображения (блиттинг) pygame.display. flip () #обновляет монитор
#передвинуть изображение в новые координаты
pygame.time.delay (2000) # 2000мс=2 сек
Pygame.draw.rect (screen, 'white', (400, 450, 100, 1001,0) #стираем старое яблоко screen. blit (apple, [600,450]) #копирование пикселей с растрового изображения (блиттинг)
pygame.display.flip() #обновляет монитор
running=True while running:
for event in pygame.event.get () :
if event.type==pygame.QUIT: #пришло ли событие нажатия на крестик
running=False
pygame. quit () #закрыть окно крестиком