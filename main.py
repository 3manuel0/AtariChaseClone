import pygame
from sys import exit
import random 
pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Atari Chase')
clock = pygame.time.Clock()
vel = 10
my_font = pygame.font.SysFont('Comic Sans MS', 30)
# players 
player_one_x_pos = 100
player_one_y_pos = 50
player_two_x_pos = 300
player_two_y_pos = 50
player_one_score = 0
player_one_surf = pygame.Surface((40, 40))
player_one_rect = player_one_surf.get_rect(center = (player_one_x_pos, player_one_y_pos))
player_two_surf = pygame.Surface((40, 40))
player_two_rect = player_two_surf.get_rect(center = (player_two_x_pos, player_two_y_pos))
player_two_score = 0
# Food 
food_x_pos = random.randint(20 , 880)
food_y_pos = random.randint(20 , 440)
food_surf = pygame.Surface((40, 40))
food_rect = food_surf.get_rect(center = (food_x_pos, food_y_pos))

# surfeses 
surface = pygame.Surface((900, 500))
score_surf = pygame.Surface((900, 100))
surface.fill('white')
player_one_surf.fill('red')
player_two_surf.fill('blue')
food_surf.fill('purple')
score_surf.fill('white')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    # player one movements 
    if player_one_x_pos > 20:
         player_one_x_pos -= keys[pygame.K_LEFT] * vel
    if player_one_x_pos < 880:
         player_one_x_pos+= keys[pygame.K_RIGHT] * vel
    if player_one_y_pos > 20:     
         player_one_y_pos -= keys[pygame.K_UP] * vel
    if player_one_y_pos < 480:
         player_one_y_pos += keys[pygame.K_DOWN] * vel 

    # player two movement
    if player_two_x_pos > 20:
         player_two_x_pos -= keys[pygame.K_a] * vel
    if player_two_x_pos < 880:
         player_two_x_pos+= keys[pygame.K_d] * vel
    if player_two_y_pos > 20:     
         player_two_y_pos -= keys[pygame.K_w] * vel
    if player_two_y_pos < 480:
         player_two_y_pos += keys[pygame.K_s] * vel     
    player_two_rect.center = (player_two_x_pos, player_two_y_pos)
    player_one_rect.center = (player_one_x_pos, player_one_y_pos)
    if  player_one_rect.colliderect(food_rect):
         food_rect.center = (random.randint(20 , 880), random.randint(20 , 440))
         player_one_score += 1
    if player_two_rect.colliderect(food_rect):
         food_rect.center = (random.randint(20 , 880), random.randint(20 , 440))
         player_two_score += 1       
    screen.blit(surface, (0, 0))   
    screen.blit(score_surf, (0, 520))
    screen.blit(food_surf, food_rect)
    screen.blit(player_one_surf, player_one_rect)
    screen.blit(player_two_surf, player_two_rect)
    screen.blit(my_font.render(f'{player_one_score}', True, (255, 0, 0)), (500, 530)) 
    screen.blit(my_font.render(f'{player_two_score}', True, (0, 0, 255)), (400, 530)) 
    pygame.display.update()
    clock.tick(60)