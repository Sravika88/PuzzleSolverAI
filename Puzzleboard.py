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

    def format_state(self):
        """
        Generate a unique string representation of the current state.
        :return: String representation of the state.
        """
        return ''.join(str(num) for row in self.state for num in row)

    def is_goal_sta
