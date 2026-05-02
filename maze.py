import pygame
import sys
import random

rows = 15
cols = 20
cell_size = 30
width = cols * cell_size
height = rows * cell_size

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Generator and Solver")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
BLUE = (0, 80, 255)
GREEN = (0, 180, 0)

top_wall = [[1 for _ in range(cols)] for _ in range(rows)]
right_wall = [[1 for _ in range(cols)] for _ in range(rows)]
seen = [[False for _ in range(cols)] for _ in range(rows)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    pygame.display.update()
    clock.tick(60)
