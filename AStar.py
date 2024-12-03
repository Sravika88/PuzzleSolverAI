from PuzzleBoard import PuzzleBoard

def a_star(initial_state, goal_state):
    from heapq import heappush, heappop
    open_list = []
    heappush(open_list, (0, initial_state))
    visited = set()
    nodes_explored = 0

    while open_list:
        _, current_board = heappop(open_list)
        nodes_explored += 1
        visited.add(current_board.format_state())

        if current_board.state == goal_state:
            print("Solution found!")
            return current_board.state, nodes_explored

        for move in current_board.generate_moves():
            if move.format_state() not in visited:
                g_cost = 0  # Replace with actual cost logic
                h_cost = 0  # Replace with heuristic calculation
                f_cost = g_cost + h_cost
                heappush(open_list, (f_cost, move))

    print("No solution found!")
    return None, nodes_explored

if __name__ == "__main__":
    initial_state = PuzzleBoard([[1, 2, 3], [4, 5, 0], [6, 7, 8]])
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    solution, nodes = a_star(initial_state, goal_state)

    if solution:
        print("Solution path:")
        for step in solution:
            print(step)
        print(f"Nodes explored: {nodes}")
    else:
        print("No solution path found.")
