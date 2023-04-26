import pygame
import random

# Global variables
BLOCK_SIZE = 20
SPEED = 10
snake = [(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)]
direction = "RIGHT"

# Pygame setup
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Functions
def move_snake(direction):
    global snake
    head = snake[0]
    if direction == "UP":
        new_head = (head[0], head[1] - BLOCK_SIZE)
    elif direction == "DOWN":
        new_head = (head[0], head[1] + BLOCK_SIZE)
    elif direction == "LEFT":
        new_head = (head[0] - BLOCK_SIZE, head[1])
    elif direction == "RIGHT":
        new_head = (head[0] + BLOCK_SIZE, head[1])
    snake.insert(0, new_head)
    snake.pop()

# Game loop
def main():
    global direction
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # Move snake
        move_snake(direction)

        # Draw screen
        screen.fill((0, 0, 0))
        for block in snake:
            pygame.draw.rect(screen, (255, 255, 255), (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.update()

        # Update clock
        clock.tick(SPEED)

if __name__ == "__main__":
    main()
