import pygame

pygame.init

dis = pygame.display.set_mode((1000, 700))
sells = pygame.image.load('Sells.png').convert_alpha()
legs = pygame.image.load('Legs.png').convert_alpha()
hair = pygame.image.load('Hair.png').convert_alpha()
dress = pygame.image.load('Body.png').convert_alpha()
girl = pygame.image.load('girl.png').convert_alpha()
BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
BLUE = (0, 0, 225)
GREEN = (0, 225, 0)
MAGENTA = (225, 0, 225)
YELLOW = (225, 225, 0)
pygame.display.set_caption('Lohushka')
dis.fill(WHITE)


# Создание платья №1
body_width = 114
body_height = 196
body_x = 350
body_y = 10
dis.blit(dress, (body_x, body_y))
dress_x = 0
dress_y = 0
dress_on_girl = False
pygame.display.update()

# Создание волос №2
hair_width = 90
hair_height = 134

hair_x = girl.get_height() // 2 - hair.get_width() // 2
hair_y = girl.get_height() - dress.get_height() - hair.get_height() + 10
hair_on_girl = False
pygame.display.update()



# Создание ног №3
legs_width = 84
legs_height = 59
legs_x = 350
legs_y = 400
dis.blit(legs, (legs_x, legs_y))
dis.blit(girl, (100, 50))
pygame.display.update()

# ОСновная логика игры(Выборка)
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


        elif event.type == pygame.MOUSEBUTTONDOWN:

            click_x, click_y = event.pos
            for i in range(3):

                if dress_x <= click_x <= dress_x + dress.get_width() and \
                    dress_y <= click_y <= dress_y + dress.get_height():
                    if dress_on_girl:
                        dress_on_girl = False
                        dress_x = 0
                        dress_y = 0
                        hair_x = 0
                        hair_y = -10
                    else:
                        dress_on_girl = True
                        dress_x = 150
                        dress_y = 150
                        hair_x = girl.get_width() // 2 - dress.get_width() // 2
                        hair_y = girl.get_height() - dress.get_height() - hair.get_height() +10
                elif hair_x <= click_x <= hair_x + hair.get_width() and \
                    hair_y <= click_y <= hair_y + hair.get_height():
                    if hair_on_girl:
                        dress_on_girl = False
                        dress_x = 0
                        dress_y = 0
                        hair_x = 0                            
                        hair_y = -10

                    else:
                        dress_on_girl = True
                        dress_x = 100
                        dress_y = 100
                        hair_x = girl.get_width() // 2 - hair.get_width() // 2
                        hair_y = girl.get_height() - dress.get_height() - hair.get_height()


                #elif legs_x <= click_x <= legs_x + legs_width and legs_y <= click_y <= legs_y + legs_height:
                    #dis.blit(legs, (143, 425))
                    #pygame.display.update()
    dis.fill((WHITE))
    if dress_on_girl:
        dis.blit(girl, (100, 100))
        dis.blit(dress, (dress_x, dress_y))
        dis.blit(hair, (hair_x, hair_y))
    else:
        dis.blit(dress, (0, 0))
        dis.blit(girl, (0, 0))
        dis.blit(hair, (hair_x, hair_y))


    pygame.display.update()

pygame.quit()
quit()