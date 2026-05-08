# Building-and-Running-mazes

## Description

This project is a visual maze generator and solver built using Python and Pygame. It generates a perfect maze using a stack-based Depth-First Search (DFS) algorithm and then solves it using a similar backtracking approach.

The maze generation behaves like a “mouse in a maze” — it randomly explores paths, removes walls between cells, and backtracks whenever it reaches a dead end until the entire maze is completed.

---

## How it Works

### Maze Generation

* Uses a randomized DFS algorithm with backtracking
* Starts from a random cell
* Moves to unvisited neighboring cells
* Removes walls between connected cells
* Backtracks when no valid moves are available
* Creates a perfect maze with only one valid path between cells

### Maze Solving

* Starts from the top-left corner
* Searches for the exit at the bottom-right corner
* Uses DFS and backtracking to explore paths
* Avoids revisiting explored cells
* Marks dead ends and highlights the correct solution path

---

## Visualization

* 🔴 Red → Current position / active path
* 🔵 Blue → Dead ends
* Black lines → Maze walls
* White gaps → Maze entrances and exits

---

## Tech Used

* Python
* Pygame

---

## Idea Behind It

Both the maze generation and solving processes are based on stack-driven DFS traversal. The project demonstrates how recursive backtracking and graph traversal algorithms can be used to generate and solve complex maze structures visually in real time.
