# BFS.py
# Implements the Breadth-First Search algorithm for solving the 8-puzzle problem.

from collections import deque

def bfs(initial_state, goal_state):
    """
    Perform Breadth-First Search to find the solution to the 8-puzzle problem.
    
    :param initial_state: List of lists representing the initial puzzle state.
    :param goal_state: List of lists representing the goal puzzle state.
    :return: Solution path as a list of states, or None if no solution is found.
    """
    visited = set()  # To keep track of visited states
    queue = deque([(initial_state, [])])  # Queue stores (current_state, path_to_state)
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path + [current_state]
        
        # Skip already visited states
        state_tuple = tuple(map(tuple, current_state))
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        
        # Generate moves and add them to the queue
        board = PuzzleBoard(current_state)
        for move in board.generate_moves():
            new_state = board.apply_move(move)  # Apply the move to generate a new state
            queue.append((new_state, path + [current_state]))
    
    return None  # Return None if no solution is found

if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    solution = bfs(initial_state, goal_state)
    if solution:
        print("Solution found!")
        for step in solution:
            for row in step:
                print(row)
            print()
    else:
        print("No solution exists.")

