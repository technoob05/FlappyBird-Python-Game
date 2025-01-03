import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 432, 768
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 120
GRAVITY = 0.2
PIPE_SPAWN_EVENT = pygame.USEREVENT
PIPE_SPAWN_TIME = 1200
PIPE_HEIGHTS = [300, 400, 500]

# Load assets
BACKGROUND = pygame.transform.scale2x(pygame.image.load('background-night.png').convert())
FLOOR = pygame.transform.scale2x(pygame.image.load('assets/floor.png').convert())

PIPE = pygame.transform.scale2x(pygame.image.load('assets/pipe-green.png').convert())
#Bird 
bird_down = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-downflap.png').convert_alpha())
bird_mid = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-midflap.png').convert_alpha())
bird_up = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-upflap.png').convert_alpha())
bird_list = [bird_down,bird_mid,bird_up]
bird_index = 0 
BIRD = bird_list[bird_index]
#Timer for bird 
birdflap = pygame.USEREVENT +1
pygame.time.set_timer(birdflap,200)
# Variables
bird_rect = BIRD.get_rect(center=(100, HEIGHT / 2))
bird_movement = 0
pipe_list = []
score = 0
font = pygame.font.Font(None, 36)
game_active = False  # Thêm định nghĩa của game_active

# Functions
def draw_floor():
    SCREEN.blit(FLOOR, (floor_x_pos, 600))
    SCREEN.blit(FLOOR, (floor_x_pos + 432, 600))

def create_pipe():
    random_pipe_pos = random.choice(PIPE_HEIGHTS)
    bottom_pipe = PIPE.get_rect(midtop=(500, random_pipe_pos))
    top_pipe = PIPE.get_rect(midbottom=(500, random_pipe_pos - 300))
    return bottom_pipe, top_pipe

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            SCREEN.blit(PIPE, pipe)
        else:
            flip_pipe = pygame.transform.flip(PIPE, False, True)
            SCREEN.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return True
    if bird_rect.top <= -75 or bird_rect.bottom >= 650:
        return True
    return False

def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1, bird_movement * -3, 1)
    return new_bird

def display_score():
    score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(WIDTH // 2, 100))
    SCREEN.blit(score_surface, score_rect)
def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100,bird_rect.centery))
    return new_bird,new_bird_rect
# Game loop
floor_x_pos = 0
pygame.time.set_timer(PIPE_SPAWN_EVENT, PIPE_SPAWN_TIME)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and bird_rect.centery > 0:
                bird_movement = 0
                bird_movement -= 8
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, HEIGHT / 2)
                bird_movement = 0
                score = 0
        if event.type == PIPE_SPAWN_EVENT:
            pipe_list.extend(create_pipe())
        if event.type == birdflap:
            if bird_index < 2 :
                bird_index +=1 
            else :
                bird_index = 0
            bird,bird_rect = bird_animation()

    SCREEN.blit(BACKGROUND, (0, 0))

    if game_active:
        # Bird
        bird_movement += GRAVITY
        rotated_bird = rotate_bird(BIRD)
        bird_rect.centery += bird_movement
        SCREEN.blit(rotated_bird, bird_rect)

        # Pipes
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)

        # Score
        for pipe in pipe_list:
            if pipe.centerx == 100:
                score += 1

        # Collision
        if check_collision(pipe_list):
            game_active = False

    # Floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0

    display_score()
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

pygame.quit()
sys.exit()
