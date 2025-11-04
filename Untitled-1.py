import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 950))
pygame.display.set_caption("Okamurka")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Project folder/Pixeltype.ttf", 50)


sky_surface = pygame.image.load("Project folder/okamura2.jpg")
ground_surface = pygame.image.load("Project folder/ground.png").convert()
text_surface = test_font.render("tomijo  okamurka", False, "Blue")
score_surface = test_font.render("score", False, "Black")

snail_surface = pygame.image.load("Project folder/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (500,850))

player_surface = pygame.image.load("Project folder/sprite_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (150, 850))
player_gravity = 0

score_rect = score_surface.get_rect(topleft = (300, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print("collision")
        if event.type == pygame.MOUSEBUTTONDOWN:
             if player_rect.collidepoint(event.pos):
                 player_gravity = -15


    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 850))
    screen.blit(text_surface, (300, 500))
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player_gravity = -15
   

    player_gravity += 1
    player_rect.y += player_gravity


    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)
    pygame.draw.rect(screen, "Pink", score_rect)
    pygame.draw.rect(screen, "Pink", score_rect, 10)
    pygame.draw.ellipse(screen, "Black", pygame.Rect(780, 790, 40, 60))
    screen.blit(score_surface, score_rect)

    #if player_rect.colliderect(snail_rect):
       # print("collision")

   # mouse_pos = pygame.mouse.get_pos()
   # if player_rect.collidepoint(mouse_pos):
       # print(pygame.mouse.get_pressed())
     
    pygame.display.update()
    clock.tick(60)
