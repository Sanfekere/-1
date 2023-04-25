# Snake spēle

import pygame
import random

# definējam krāsas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# definējam izmēru
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# definējam bloka izmēru un daudzumu
BLOCK_SIZE = 20
BLOCK_COUNT = (WINDOW_WIDTH // BLOCK_SIZE, WINDOW_HEIGHT // BLOCK_SIZE)

# inicializējam pygame
pygame.init()

# izveidojam logu
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

# izveidojam laika skaitītāju
clock = pygame.time.Clock()

# izveidojam funkciju, kas zīmē bloku
def draw_block(color, row, col):
    pygame.draw.rect(window, color, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# izveidojam Snake klasi
class Snake:
    def __init__(self):
        self.body = [(4, 4), (4, 5), (4, 6)]
        self.direction = "right"

    def move(self):
        head = self.body[0]
        if self.direction == "up":
            new_head = (head[0] - 1, head[1])
        elif self.direction == "down":
            new_head = (head[0] + 1, head[1])
        elif self.direction == "left":
            new_head = (head[0], head[1] - 1)
        elif self.direction == "right":
            new_head = (head[0], head[1] + 1)

        self.body.insert(0, new_head)
        self.body.pop()

    def draw(self):
        for block in self.body:
            draw_block(GREEN, block[0], block[1])

    def change_direction(self, direction):
        if direction == "up" and self.direction != "down":
            self.direction = "up"
        elif direction == "down" and self.direction != "up":
            self.direction = "down"
        elif direction == "left" and self.direction != "right":
            self.direction = "left"
        elif direction == "right" and self.direction != "left":
            self.direction = "right"

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)


# izveidojam Food klasi
class Food:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.spawn()

    def spawn(self):
        self.row = random.randint(0, BLOCK_COUNT[0] - 1)
        self.col = random.randint(0, BLOCK_COUNT[1] - 1)

    def draw(self):
        draw_block(RED, self.row, self.col)

# izveidojam Snake un Food objektus
snake = Snake()
food = Food()

# galvenais cikls
while True:
    # ...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'
            elif event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
    # ...
    # Move the snake
    move_snake(direction)

    # Check if snake hits the wall or itself
    if check_collision(snake[0], SCREEN_WIDTH, SCREEN_HEIGHT):
        pygame.quit()
        sys.exit()

    # Check if snake eats the food
    if snake[0]['x'] == food['x'] and snake[0]['y'] == food['y']:
        food = generate_food()
        snake.append({'x': snake[-1]['x'], 'y': snake[-1]['y']})

    # Draw everything
    draw_screen()
    draw_snake(snake)
    draw_rect(food['x'], food['y'], BLOCK_SIZE, BLOCK_SIZE, GREEN)

    # Update the screen
    pygame.display.update()

    # Set the speed of the game
    clock.tick(FPS)
