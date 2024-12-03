from PuzzleBoard import PuzzleBoard
from heapq import heappop, heappush

def heuristic(state, goal_state):
    """
    Calculate the Manhattan distance heuristic.
    :param state: Current board state.
    :param goal_state: Goal board state.
    :return: Heuristic value.
    """
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            value = state[i][j]
            if value != 0:  # Ignore the empty tile
                goal_row, goal_col = divmod(goal_state.index(value), len(state))
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

def a_star_search(initial_state, goal_state):
    """
    Perform the A* search algorithm.
    :param initial_state: PuzzleBoard object for the initial state.
    :param goal_state: List of lists representing the goal state.
    :return: Path to the solution.
    """
    frontier = []
    heappush(frontier, (0, initial_state))
    visited = set()
    came_from = {initial_state.format_state(): None}
    cost_so_far = {initial_state.format_state(): 0}

    while frontier:
        _, current_board = heappop(frontier)

        if current_board.is_goal_state(goal_state):
            print("Solution found!")
            path = []
            while current_board:
                path.append(current_board)
                current_board = came_from[current_board.format_state()]
            path.reverse()
            return path

        visited.add(current_board.format_state())

        for neighbor in current_board.generate_moves():
            new_cost = cost_so_far[current_board.format_state()] + 1
            if neighbor.format_state() not in cost_so_far or new_cost < cost_so_far[neighbor.format_state()]:
                cost_so_far[neighbor.format_state()] = new_cost
                priority = new_cost + heuristic(neighbor.state, goal_state)
                heappush(frontier, (priority, neighbor))
                came_from[neighbor.format_state()] = current_board

    print("No solution found.")
    return None

if __name__ == "__main__":
    # Define the initial and goal states
    initial_state = PuzzleBoard([[1, 2, 3], [4, 5, 0], [6, 7, 8]])
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # Run the A* search algorithm
    solution_path = a_star_search(initial_state, goal_state)

    # Print the solution steps if found
    if solution_path:
        print("\nSolution path:")
        for step in solution_path:
            print(step)
            print("---")
    else:
        print("No solution could be found.")
