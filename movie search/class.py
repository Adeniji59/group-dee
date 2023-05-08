import pygame
import random

# initialize Pygame
pygame.init()

# set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# set the font
font = pygame.font.SysFont('Arial', 30)

# load the images
player_img = pygame.image.load('player.png').convert_alpha()
obstacle_img = pygame.image.load('obstacle.png').convert_alpha()

# set the game variables
player_x = 50
player_y = screen_height - player_img.get_height() - 50
player_speed = 5
obstacle_x = screen_width
obstacle_y = screen_height - obstacle_img.get_height() - 50
obstacle_speed = 5
score = 0

# define functions
def move_player(keys_pressed):
    global player_x
    if keys_pressed[pygame.K_LEFT]:
        player_x -= player_speed
    elif keys_pressed[pygame.K_RIGHT]:
        player_x += player_speed

def move_obstacle():
    global obstacle_x, obstacle_speed, score
    obstacle_x -= obstacle_speed
    if obstacle_x < -obstacle_img.get_width():
        obstacle_x = screen_width
        score += 1

def draw_screen():
    screen.fill((255, 255, 255))
    screen.blit(player_img, (player_x, player_y))
    screen.blit(obstacle_img, (obstacle_x, obstacle_y))
    score_text = font.render('Score: ' + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.update()

# game loop
clock = pygame.time.Clock()
game_over = False
while not game_over:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    keys_pressed = pygame.key.get_pressed()
    move_player(keys_pressed)
    move_obstacle()
    draw_screen()
    clock.tick(60)

# quit Pygame
pygame.quit()











































