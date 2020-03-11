from board import Board
import random

# This solver is based on two simple principles to predict each cell
#
# for each number squares:
#
#     if count of unopened around == square number: all of them are mines
#     if square number - count of flagged around == 0: all of the unopened are not mines
#
# Source: https://stackoverflow.com/questions/1738128/minesweeper-solving-algorithm


class Solver:
    def __init__(self):
        self.solver_board = Board(10, 10)
        self.solver_board.set_board((0, 0))

    def find_mines(self):
        for r in range(self.solver_board.n):
            for c in range(self.solver_board.n):
                if str(self.solver_board.user_board[r][c]).isdigit():
                    unopened_and_mines = self.solver_board.neighbor_finder(r, c, ['X', 'M'],
                                                                           self.solver_board.user_board)
                    if len(unopened_and_mines) == self.solver_board.user_board[r][c]:
                        for (r_unopened, c_unopened) in unopened_and_mines:
                            self.solver_board.user_board[r_unopened][c_unopened] = 'M'

    def find_clear_cells(self):
        played = False
        for r in range(self.solver_board.n):
            for c in range(self.solver_board.n):
                if str(self.solver_board.user_board[r][c]).isdigit():
                    neighbor_mines = self.solver_board.neighbor_finder(r, c, ['M'], self.solver_board.user_board)
                    if len(neighbor_mines) == self.solver_board.user_board[r][c]:
                        unopened = self.solver_board.neighbor_finder(r, c, ['X'], self.solver_board.user_board)

                        for (r_unopened, c_unopened) in unopened:
                            self.solver_board.play(r_unopened, c_unopened)
                            played = True
        return played

    def guess(self):
        available_moves = []
        for r in range(self.solver_board.n):
            for c in range(self.solver_board.n):
                if self.solver_board.user_board[r][c] == 'X':
                    available_moves.append((r, c))

        next_move = random.choice(available_moves)

        return self.solver_board.play(next_move[0], next_move[1])

    def play_game(self):
        self.find_mines()
        changed = self.find_clear_cells()
        if not changed:
            return self.guess()
        return True

    def solve(self):
        is_playing = self.solver_board.play(0, 0)

        while is_playing:
            if self.solver_board.win_condition():
                return True
            is_playing = self.play_game()
        return False
