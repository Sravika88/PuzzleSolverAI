# PuzzleBoard.py
# Handles the 8-puzzle board setup and utility functions.

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
