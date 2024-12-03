class PuzzleBoard:
    def __init__(self, initial_state):
        self.state = initial_state
        self.empty_tile = self.find_empty_tile()

    def find_empty_tile(self):
        for row in range(len(self.state)):
            for col in range(len(self.state[row])):
                if self.state[row][col] == 0:
                    return row, col
        return None

    def generate_moves(self):
        row, col = self.empty_tile
        moves = []
        potential_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in potential_moves:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < len(self.state) and 0 <= new_col < len(self.state[0]):
                new_state = [list(r) for r in self.state]
                new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                moves.append(PuzzleBoard(new_state))
        return moves

    def format_state(self):
        return ''.join(str(tile) for row in self.state for tile in row)

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.state)
