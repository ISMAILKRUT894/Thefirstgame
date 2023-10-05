import pygame

# инициализация Pygame
pygame.init()
WHITE = (225, 225, 225)
# задаем размер окна
screen_width = 1280
screen_height = 720

# создаем окно
screen = pygame.display.set_mode((screen_width, screen_height))

# загружаем изображения девушки и платья
silhouette_shoes = pygame.image.load('Туфли .jpg')
sells = pygame.image.load('Sells.png')
pygame.mixer.music.load("Back_music.mp3")
girl_image = pygame.image.load('girl.png')
dress_image = pygame.image.load('Body.png')
hair_image = pygame.image.load('Hair.png')
shoes_image = pygame.image.load('Legs.png')
rdress_image = pygame.image.load('Raiden_dress.png')
rhair_image = pygame.image.load('Raiden_hair.png')
background = pygame.image.load('Background (2).png')
pygame.mixer.music.play(-1)
# Отрисовка девушки по сериде экрана
girl_width, girl_height = girl_image.get_size()
x = (screen_width - girl_width) // 2
y = (screen_height - girl_height) // 2

# задаем начальные координаты платья
dress_x = 300
dress_y = 200
hair_x = 300
hair_y = 50
shoes_x = 33
shoes_y = 30
rdress_x = 500
rdress_y = 150
rhair_x = 500
rhair_y = 50

silhouette_shoes_x = 1010
silhouette_shoes_y = 30

# Фон приложения
screen.blit(background, (0, 0))

# флаг, указывающий на то, что платье на девушке
dress_on_girl = False
hair_on_girl = False
shoes_on_girl = False
rdress_on_girl = False
rhair_on_girl = False
image_clrked = True





screen.blit(sells, (0, 0))
# основной цикл игры
running = True
while running:
    # обрабатываем события Pygame
    for event in pygame.event.get():
        # если пользователь закрыл окно, завершаем цикл
        if event.type == pygame.QUIT:
            running = False
        # если пользователь нажал кнопку мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # получаем координаты клика
            click_x, click_y = event.pos
            if silhouette_shoes_x <= click_x <= silhouette_shoes_x + silhouette_shoes.get_width() and \
                    silhouette_shoes_y <= click_y <= silhouette_shoes_y + silhouette_shoes.get_height():
                pygame.time.wait(10000)












                # проверяем, что клик был в пределах платья
                if dress_x <= click_x <= dress_x + dress_image.get_width() and \
                    dress_y <= click_y <= dress_y + dress_image.get_height():
                # перемещаем платье на девушку, если оно было на ней, иначе перемещаем его на девушку
                    if dress_on_girl:
                        dress_on_girl = False
                        dress_x = 300
                        dress_y = 200
                    else:
                        dress_on_girl = True
                        dress_x = 130
                        dress_y = 180
                screen.blit(dress_image, (dress_x, dress_y))

                # перемещаем платье на девушку, если оно было на ней, иначе перемещаем его на девушку


            elif hair_x <= click_x <= hair_x + hair_image.get_width() and \
                    hair_y <= click_y <= hair_y + hair_image.get_height():
                # перемещаем платье на девушку, если оно было на ней, иначе перемещаем его на девушку
                if hair_on_girl:
                    hair_on_girl = False
                    hair_x = 300
                    hair_y = 50
                else:
                    hair_on_girl = True
                    hair_x = 145
                    hair_y = 80

            elif rhair_x <= click_x <= rhair_x + rhair_image.get_width() and \
                    rhair_y <= click_y <= rhair_y + rhair_image.get_height():
                # перемещаем платье на девушку, если оно было на ней, иначе перемещаем его на девушку
                if rhair_on_girl:
                    rhair_on_girl = False
                    rhair_x = 500
                    rhair_y = 50
                else:
                    rhair_on_girl = True
                    rhair_x = 100
                    rhair_y = 90

            elif rdress_x <= click_x <= rdress_x + rdress_image.get_width() and \
                    rdress_y <= click_y <= rdress_y + rdress_image.get_height():
                # перемещаем платье на девушку, если оно было на ней, иначе перемещаем его на девушку
                if rdress_on_girl:
                    rdress_on_girl = False
                    rdress_x = 500
                    rdress_y = 150
                else:
                    rdress_on_girl = True
                    rdress_x = 100
                    rdress_y = 170



    # отрисовываем девушку и платье
    screen.blit(girl_image, (x, y))


    screen.blit(silhouette_shoes, (1010, 30))



    # обновляем экран
    pygame.display.update()

# завершаем работу Pygame
pygame.quit()