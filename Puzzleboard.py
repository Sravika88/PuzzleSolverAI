class PuzzleBoard:
    def __init__(self, initial_state):
        """
        Initialize the puzzle board with the given state.
        :param initial_state: List of lists representing the 8-puzzle board.
        """
        self.state = initial_state
        self.empty_tile = self.find_empty_tile()

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
        :return: List of PuzzleBoard objects with new states.
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
                # Create a new state by swapping the empty tile
                new_state = [row[:] for row in self.state]
                new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                moves.append(PuzzleBoard(new_state))

        return moves

    def format_state(self):
        """
        Format the board state into a unique string representation.
        This helps in identifying visited states.
        :return: A string representation of the board state.
        """
        return ''.join(str(tile) for row in self.state for tile in row)

    def __str__(self):
        """
        Format the board for printing.
        :return: A string representation of the board.
        """
        return '\n'.join(' '.join(map(str, row)) for row in self.state)


if __name__ == "__main__":
    # Test the PuzzleBoard class
    board = PuzzleBoard([[1, 2, 3], [4, 5, 0], [6, 7, 8]])
    print("Initial Board:")
    print(board)
    print("\nPossible Moves:")
    for move in board.generate_moves():
        print(move)
        print("---")
    print("Formatted State:", board.format_state())
