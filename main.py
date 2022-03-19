import pygame
from pygame.locals import *
from random import randint
HEIGHT, WIDTH = 800, 800  # Strictly accepts numbers divisable by 10

window = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Snake Game')

x, y = 100, 100
VELOCITY = 10  # Speed of the snake, do not change
FPS = 10 # Frames per second
snake_width, snake_height = 10, 10  # Snake dimentions
run = True
# X,Y velocity, determines which way the snake should be moved
velocity_x, velocity_y = 1, 0
# Positions of the snakes body (index 0 is current position & index -1 is end of snakes body)
last_positions = [(0, 0, 0, 0)]


# Food and generation
food = []  # Positions of food
length = 3  # Length of snake on intial run, min: 1
eaten = 10  # Amount of food the snake has eaten

generation = 10  # Quantity of food randomly generated per erase

clock = pygame.time.Clock()

while run:
    clock.tick(FPS)
    # Basic Input control
    if velocity_x != 0:
        if velocity_x > 0:
            x += VELOCITY
        elif velocity_x < 0:
            x -= VELOCITY
    else:
        if velocity_y > 0:
            y -= VELOCITY
        elif velocity_y < 0:
            y += VELOCITY

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        velocity_x = 0
        velocity_y = 1
    if keys[pygame.K_DOWN]:
        velocity_x = 0
        velocity_y = -1
    if keys[pygame.K_LEFT]:
        velocity_y = 0
        velocity_x = -1
    if keys[pygame.K_RIGHT]:
        velocity_y = 0
        velocity_x = 1

    # Food generation & Food collision check
    if eaten == generation:
        eaten = 0
        for i in range(generation):
            values = (randint(1, WIDTH/10-2)*10, randint(1, HEIGHT/10-2)*10,
                      snake_width, snake_height)  # Randomly generated position for the food
            food.append(values)
            pygame.draw.rect(window, (randint(0, 255), randint(
                0, 225), randint(0, 255)), values)

    current_pos = (x, y, snake_height, snake_width)
    if current_pos in food:  # Checks if the snakes head has touched the food, if so, add a length of 1
        print('Scored a point!')
        eaten += 1
        length += 1
    # Body collision check & Snake misc
    if last_positions[0] != current_pos:
        if current_pos in last_positions:  # Checks if the snakes head has touched its body, if so, game over
            print('You have died, game over')
            run = False
        else:
            pygame.draw.rect(window, (0, 225, 0), current_pos)  # Main player
            last_positions.insert(0, current_pos)
    if len(last_positions) > length:
        last = last_positions.pop()
        pygame.draw.rect(window, (0, 0, 0), last)

    pygame.display.update()

pygame.quit()
