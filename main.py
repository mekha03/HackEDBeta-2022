import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Super Engg Girlies')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/font.otf', 50)
game_active = True

background = pygame.image.load('graphics/16431.jpg').convert()
ground = pygame.Surface((800, 50))
ground.fill('snow')

text = test_font.render('Super Engg Girlies', True, 'Black')
text_rect = text.get_rect(center = (400,100))

homework = pygame.image.load('graphics/homework-.png').convert_alpha()
homework_rect = homework.get_rect(bottomleft=(800, 500))

player = pygame.image.load('graphics/Character_right.png').convert_alpha()
player_rect = player.get_rect(bottomleft=(200, 450))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #  if player_rect.bottom == 450:
                        player_gravity = -20  # Remove for mario game
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                homework_rect.left = 800
                text = test_font.render('Super Engg Girlies', True, 'Black')
                text_rect = text.get_rect(center=(400, 100))

    # draw stuff :p
    if game_active:
        screen.blit(background, (0, 0))
        screen.blit(ground, (0, 450))
        screen.blit(text, text_rect)
        if homework_rect.left < -100:
            homework_rect.left = 800
        else:
            homework_rect.left -= 4
        screen.blit(homework, homework_rect)

        player_gravity +=1
        player_rect.bottom += player_gravity
        if player_rect.bottom >=450:
            player_rect.bottom = 450
        screen.blit(player, player_rect)

        if homework_rect.colliderect(player_rect):
            game_active = False
            if game_active == False:
                screen.fill('grey1')
                text_font = pygame.font.Font(None, 50)
                text = text_font.render('Game Over', True, 'White')
                text2 = text_font.render('Press Space-bar to', True, 'White')
                text3 = text_font.render('RESTART', True, 'White')
                text_rect = text.get_rect(center=(400, 200))
                text2_rect = text.get_rect(center=(325, 275))
                text3_rect = text.get_rect(center=(400, 350))
                screen.blit(text, text_rect)
                screen.blit(text2, text2_rect)
                screen.blit(text3, text3_rect)
    # if player_rect.colliderect(homework_rect):
    pygame.display.update()
    clock.tick(60)
