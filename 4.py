import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Clock & snake setup
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font = pygame.font.SysFont("bahnschrift", 25)

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False

    x1, y1 = width / 2, height / 2
    x1_change, y1_change = 0, 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change, y1_change = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    x1_change, y1_change = snake_block, 0
                elif event.key == pygame.K_UP:
                    x1_change, y1_change = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change, y1_change = 0, snake_block

        # Update snake position
        x1 += x1_change
        y1 += y1_change

        # Check boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True

        screen.fill(black)

        # Draw food
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        # Snake body
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check collision with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True

        draw_snake(snake_list)
        pygame.display.update()

        # Check food collision
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    # End message
    screen.fill(black)
    message("Game Over! Press Q to Quit", red)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()

gameLoop()
