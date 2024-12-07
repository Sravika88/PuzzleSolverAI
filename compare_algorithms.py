import time
from BFS import bfs
from DFS import dfs
from AStar import a_star
from PuzzleSolverAI.Puzzleboard import PuzzleBoard

def compare_algorithms(initial_state, goal_state):
    results = {}

    print("Running BFS...")
    start_time = time.time()
    bfs_solution = bfs(initial_state, goal_state)
    results["BFS"] = time.time() - start_time

    print("Running DFS...")
    start_time = time.time()
    dfs_solution = dfs(initial_state, goal_state)
    results["DFS"] = time.time() - start_time

    print("Running A*...")
    start_time = time.time()
    a_star_solution = a_star(initial_state, goal_state)
    results["A*"] = time.time() - start_time


    print(f"Results: {results}")

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8],
    ]
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0],
    ]

    compare_algorithms(initial_state, goal_state)
