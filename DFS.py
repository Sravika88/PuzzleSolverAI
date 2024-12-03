from PuzzleBoard import PuzzleBoard

def dfs(initial_state, goal_state):
    print("Debug: Starting DFS execution.")
    stack = [initial_state]  # Use a stack for DFS
    visited = set()  # To track visited states

    while stack:
        current_board = stack.pop()  # Get the last added state
        print(f"Exploring state:\n{current_board.state}")
        visited.add(current_board.format_state())  # Mark as visited

        # Check if the current state is the goal
        if current_board.is_goal_state(goal_state):
            print("Solution found!")
            return current_board.state

        # Generate possible moves and add to the stack if not visited
        for move in current_board.generate_moves():
            if move.format_state() not in visited:
                stack.append(move)

    print("No solution found!")
    return None


if __name__ == "__main__":
    # Define the initial and goal states
    initial_state = PuzzleBoard([[1, 2, 3], [4, 5, 0], [6, 7, 8]])
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # Run the DFS algorithm
    solution = dfs(initial_state, goal_state)

    # Print the solution steps if found
    if solution:
        print("Solution path:")
        print(solution)
    else:
        print("No solution path could be found.")
