import pygame
import sys
import random

# Grid settings
rows = 15
cols = 20
cell_size = 30
width = cols * cell_size
height = rows * cell_size

# Initalize pygame window
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Generator and Solver")
clock = pygame.time.Clock()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
BLUE = (0, 80, 255)
GREEN = (0, 180, 0)

# Maze structure data
top_wall = [[1 for _ in range(cols)] for _ in range(rows)]
right_wall = [[1 for _ in range(cols)] for _ in range(rows)]
seen = [[False for _ in range(cols)] for _ in range(rows)]

# Draw maze on screen


def draw_maze(path=None, dead=None, cur=None):
    screen.fill(WHITE)

    # Draw solution path
    if path:
        for r, c in path:
            pygame.draw.circle(
                screen, RED,
                (c * cell_size + cell_size // 2, r * cell_size + cell_size // 2),
                5
            )

    # Draw dead ends
    if dead:
        for r, c in dead:
            pygame.draw.circle(
                screen, BLUE,
                (c * cell_size + cell_size // 2, r * cell_size + cell_size // 2),
                5
            )

    # Draw current positon
    if cur:
        r, c = cur
        pygame.draw.circle(
            screen, RED,
            (c * cell_size + cell_size // 2, r * cell_size + cell_size // 2),
            7
        )

    # Draw maze walls
    for r in range(rows):
        for c in range(cols):
            x = c * cell_size
            y = r * cell_size

            if top_wall[r][c]:
                pygame.draw.line(screen, BLACK, (x, y), (x + cell_size, y), 2)

            if right_wall[r][c]:
                pygame.draw.line(screen, BLACK, (x + cell_size, y),
                                 (x + cell_size, y + cell_size), 2)

            if c == 0:
                pygame.draw.line(screen, BLACK, (x, y), (x, y + cell_size), 2)

            if r == rows - 1:
                pygame.draw.line(screen, BLACK, (x, y + cell_size),
                                 (x + cell_size, y + cell_size), 2)

    # Maze entrance and exit
    pygame.draw.line(screen, WHITE, (0, cell_size // 2), (0, cell_size - 3), 4)
    pygame.draw.line(
        screen, WHITE,
        (width, (rows - 1) * cell_size + cell_size // 2),
        (width, rows * cell_size - 3),
        4
    )

    pygame.display.update()

# Get valid neighbors


def get_neighbors(r, c):
    neighbors = []

    if r > 0 and not seen[r - 1][c]:
        neighbors.append((r - 1, c, "up"))

    if r < rows - 1 and not seen[r + 1][c]:
        neighbors.append((r + 1, c, "down"))

    if c > 0 and not seen[r][c - 1]:
        neighbors.append((r, c - 1, "left"))

    if c < cols - 1 and not seen[r][c + 1]:
        neighbors.append((r, c + 1, "right"))

    return neighbors

# Remove wall between cells


def remove_wall(r, c, nr, nc, direction):
    if direction == "up":
        top_wall[r][c] = 0
    elif direction == "down":
        top_wall[nr][nc] = 0
    elif direction == "left":
        right_wall[r][nc] = 0
    elif direction == "right":
        right_wall[r][c] = 0

# Maze generation using DFS backtracking


def generate_maze():
    path = []

    r = random.randint(0, rows - 1)
    c = random.randint(0, cols - 1)
    seen[r][c] = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_maze(cur=(r, c))
        clock.tick(20)

        neighbors = get_neighbors(r, c)

        if neighbors:
            nr, nc, direction = random.choice(neighbors)
            path.append((r, c))

            remove_wall(r, c, nr, nc, direction)

            r, c = nr, nc
            seen[r][c] = True

        elif path:
            r, c = path.pop()
        else:
            break

# Check movement validity


def can_move(r, c, nr, nc):
    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
        return False

    if nr == r - 1 and nc == c:
        return top_wall[r][c] == 0

    if nr == r + 1 and nc == c:
        return top_wall[nr][nc] == 0

    if nr == r and nc == c - 1:
        return right_wall[r][nc] == 0

    if nr == r and nc == c + 1:
        return right_wall[r][c] == 0

    return False

# Maze solving using DFS backtracking


def solve_maze():
    start = (0, 0)
    end = (rows - 1, cols - 1)

    path = [start]
    seen_path = set()
    dead = set()

    while path:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        cur = path[-1]
        r, c = cur
        seen_path.add(cur)

        draw_maze(path=path, dead=dead, cur=cur)
        clock.tick(5)

        if cur == end:
            return path

        moves = [
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1)
        ]

        random.shuffle(moves)
        moved = False

        for nr, nc in moves:
            if (nr, nc) not in seen_path and can_move(r, c, nr, nc):
                path.append((nr, nc))
                moved = True
                break

        if not moved:
            dead.add(path.pop())

    return None


# Run maze generator
generate_maze()
solution = solve_maze()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_maze(path=solution)
