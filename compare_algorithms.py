from collections import deque
from PuzzleBoard import PuzzleBoard
import time
import matplotlib.pyplot as plt


def manhattan_distance(state, goal):
    """Calculate the Manhattan Distance heuristic."""
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0:
                goal_pos = [(r, c) for r, row in enumerate(goal) for c, val in enumerate(row) if val == state[i][j]][0]
                distance += abs(goal_pos[0] - i) + abs(goal_pos[1] - j)
    return distance


def bfs(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])
    nodes_explored = 0

    while queue:
        current_board, path = queue.popleft()
        nodes_explored += 1

        if current_board.is_goal_state(goal_state):
            return path, nodes_explored

        visited.add(current_board.format_state())

        for move in current_board.generate_moves():
            next_board = current_board.apply_move(move)
            if next_board.format_state() not in visited:
                queue.append((next_board, path + [next_board]))

    return None, nodes_explored


def a_star(initial_state, goal_state):
    from heapq import heappush, heappop

    visited = set()
    priority_queue = []
    heappush(priority_queue, (0, initial_state, []))
    nodes_explored = 0

    while priority_queue:
        _, current_board, path = heappop(priority_queue)
        nodes_explored += 1

        if current_board.is_goal_state(goal_state):
            return path, nodes_explored

        visited.add(current_board.format_state())

        for move in current_board.generate_moves():
            next_board = current_board.apply_move(move)
            if next_board.format_state() not in visited:
                heuristic = manhattan_distance(next_board.state, goal_state)
                heappush(priority_queue, (len(path) + heuristic, next_board, path + [next_board]))

    return None, nodes_explored


def compare_algorithms(initial_state, goal_state):
    results = {}

    print("Running BFS...")
    start_time = time.time()
    bfs_path, bfs_nodes = bfs(PuzzleBoard(initial_state), goal_state)
    results["BFS"] = (time.time() - start_time, bfs_nodes)

    print("Running A*...")
    start_time = time.time()
    a_star_path, a_star_nodes = a_star(PuzzleBoard(initial_state), goal_state)
    results["A*"] = (time.time() - start_time, a_star_nodes)

    # Plot results
    plt.bar(results.keys(), [v[0] for v in results.values()], color="blue")
    plt.xlabel("Algorithm")
    plt.ylabel("Time (s)")
    plt.title("Performance Comparison")
    plt.show()

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
