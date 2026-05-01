import pygame
import sys

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    pygame.display.update()
    clock.tick(60)
