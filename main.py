import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Super Engg Girlies')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/font.otf', 50)

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #  if player_rect.bottom == 450:
                    player_gravity = -20  # Remove for mario game
    # draw stuff :p
    screen.blit(background, (0, 0))
    screen.blit(ground, (0, 450))
    screen.blit(text, (250, 75))
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
        pygame.quit()
        exit()

    # if player_rect.colliderect(homework_rect):
    pygame.display.update()
    clock.tick(60)
