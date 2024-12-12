# Puzzle Solver AI

## Project Overview
This project implements search algorithms (BFS, DFS, and A*) to solve the 8-puzzle problem. It also provides a comparison of algorithm performance.

## Objectives
- Solve the 8-puzzle problem using:
  - **Breadth-First Search (BFS)**
  - **Depth-First Search (DFS)**
  - **A* Search with a custom heuristic**
- Compare the performance of these algorithms based on:
  - Execution Time
  - Nodes Expanded
  - Solution Path Optimality
## Project Presentation
The presentation file for this project is available [here](ppt1.pptx).

## How to Run
1. Clone the repository:
    ```bash
    git clone https://github.com/Sravika88/PuzzleSolverAI.git
    ```
2. Navigate to the project directory:
    ```bash
    cd PuzzleSolverAI
    ```
3. Run any of the scripts:
    - BFS: 
        ```bash
        python BFS.py
        ```
    - DFS:
        ```bash
        python DFS.py
        ```
    - A*:
        ```bash
        python AStar.py
        ```
    - Compare Algorithms:
        ```bash
        python compare_algorithms.py
        ```

## Compare Algorithms Script

The `compare_algorithms.py` script is designed to compare the performance of BFS and A* search algorithms for solving the 8-puzzle problem.

### Features
- Measures execution time for BFS and A* algorithms.
- Counts the total number of nodes explored by each algorithm.
- Displays a bar chart comparing their performance.

### Usage
Run the script as follows:
```bash
python compare_algorithms.py
