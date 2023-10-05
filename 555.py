import pygame
import sys

pygame.init()

# Установка размеров экрана
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Перемещение картинок")

# Загрузка картинок
image1 = pygame.image.load("Body.png")
image2 = pygame.image.load("Hair.png")

# Начальные координаты картинок
x1, y1 = 100, 100
x2, y2 = 300, 100

clock = pygame.time.Clock()

show_image2 = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Если нажали на картинку1, показываем картинку2
            if image1.get_rect().collidepoint(event.pos):
                show_image2 = True

    # Обработка перемещения картинки2 по щелчку мыши
    if show_image2 and pygame.mouse.get_pressed()[0]:
        x2 += 100

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Отрисовка картинок на соответствующих координатах
    screen.blit(image1, (x1, y1))
    if show_image2:
        screen.blit(image2, (x2, y2))

    # Обновление экрана
    pygame.display.flip()

    clock.tick(60)