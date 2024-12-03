class PuzzleBoard:
    def __init__(self, initial_state):
        """
        Initialize the puzzle board with the given state.
        :param initial_state: List of lists representing the 8-puzzle board.
        """
        self.state = initial_state
        self.empty_tile = self.find_empty_tile()
        self.parent = None  # To keep track of the parent state for solution path

    def find_empty_tile(self):
        """
        Find the position of the empty tile (represented as 0).
        :return: Tuple of (row, col) for the empty tile.
        """
        for row in range(len(self.state)):
            for col in range(len(self.state[row])):
                if self.state[row][col] == 0:
                    return (row, col)
        return None

    def is_goal_state(self, goal_state):
        """
        Check if the current state matches the goal state.
        :param goal_state: List of lists representing the goal state.
        :return: True if current state is the goal state, else False.
        """
        return self.state == goal_state

    def generate_moves(self):
        """
        Generate all possible moves for the empty tile.
        :return: List of new PuzzleBoard instances representing valid moves.
        """
        row, col = self.empty_tile
        moves = []

        # Define potential moves: up, down, left, right
        potential_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in potential_moves:
            new_row = row + move[0]
            new_col = col + move[1]

            # Check if the move is within bounds
            if 0 <= new_row < len(self.state) and 0 <= new_col < len(self.state[0]):
                new_state = [row[:] for row in self.state]  # Copy the current state
                # Swap the empty tile with the new position
                new_state[row][col], new_state[new_row][new_col] = (
                    new_state[new_row][new_col],
                    new_state[row][col],
                )
                new_board = PuzzleBoard(new_state)
                new_board.parent = self  # Set parent for backtracking
                moves.append(new_board)

        return moves

    def format_state(self):
        """
        Create a unique string representation of the state.
        Useful for tracking visited states.
        :return: String representing the puzzle state.
        """
        return ''.join(str(num) for row in self.state for num in row)

    def get_solution_path(self):
        """
        Backtrack from the current state to the initial state to find the solution path.
        :return: List of PuzzleBoard states representing the solution path.
        """
        path = []
        current = self
        while current:
            path.append(current)
            current = current.parent
        return path[::-1]  # Reverse the path to start from the initial state

    def __str__(self):
        """
        String representation of the puzzle board for printing.
        :return: String showing the current state of the board.
        """
        return '\n'.join(' '.join(map(str, row)) for row in self.state)


if __name__ == "__main__":
    # Example usage
    initial = [[1, 2, 3], [4, 5, 0], [6, 7, 8]]
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    board = PuzzleBoard(initial)

    print("Initial State:")
    print(board)
    print("\nPossible Moves:")
    for move in board.generate_moves():
        print(move)
        print("-" * 10)
