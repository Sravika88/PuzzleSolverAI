from Puzzleboard import PuzzleBoard

def dfs(initial_state, goal_state):
    """
    Perform Depth-First Search to find the solution to the 8-puzzle problem.
    :param initial_state: List of lists representing the initial puzzle state.
    :param goal_state: List of lists representing the goal puzzle state.
    :return: Solution path as a list of states, or None if no solution is found.
    """
    stack = [(PuzzleBoard(initial_state), [])]
    visited = set()

    while stack:
        current_board, path = stack.pop()

        if current_board.is_goal_state(goal_state):
            return path + [current_board.state]

        if current_board.format_state() in visited:
            continue

        visited.add(current_board.format_state())

        for move in current_board.generate_moves():
            stack.append((move, path + [current_board.state]))

    return None  # Return None if no solution is found

if _name_ == "_main_":
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

    solution = dfs(initial_state, goal_state)
    if solution:
        print("Solution found!")
        for step in solution:
            for row in step:
                print(row)
            print()
    else:
        print("No solution exists.")
