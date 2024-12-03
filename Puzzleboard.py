class PuzzleBoard:
    def __init__(self, initial_state):
        self.state = initial_state
        self.empty_tile = self.find_empty_tile()

    def find_empty_tile(self):
        for row in range(len(self.state)):
            for col in range(len(self.state[row])):
                if self.state[row][col] == 0:
                    return (row, col)
        return None

    def format_state(self):
        return tuple(tuple(row) for row in self.state)

    def is_goal_state(self, goal_state):
        return self.state == goal_state

    def generate_moves(self):
        row, col = self.empty_tile
        moves = []
        potential_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for move in potential_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < len(self.state) and 0 <= new_col < len(self.state[0]):
                new_state = [row[:] for row in self.state]
                new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                moves.append(PuzzleBoard(new_state))
        return moves

if __name__ == "__main__":
    board = PuzzleBoard([[1, 2, 3], [4, 5, 0], [6, 7, 8]])
    print("Initial State:")
    print(board.state)
    print("Possible Moves:")
    print([move.state for move in board.generate_moves()])
