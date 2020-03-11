import unittest
from solver import Solver


class TestSolver(unittest.TestCase):

    def test_find_mines(self):
        test_board = [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 2],
            ['X', 'X', 1, 1]
        ]

        result_board = [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'M', 2],
            ['X', 'X', 1, 1]
        ]

        test_solver = Solver()
        test_solver.solver_board.user_board = test_board
        test_solver.solver_board.n = 4
        test_solver.find_mines()
        self.assertEqual(test_solver.solver_board.user_board, result_board)

    def test_find_empty_cells(self):

        test_board = [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'M', 'X'],
            ['X', 'X', 'M', 2],
            ['X', 'X', 1, 1]
        ]

        real_board = [
            [1, 1, 1, 1],
            ['M', 3, 'M', 2],
            [1, 3, 'M', 2],
            ['.', 1, 1, 1]
        ]

        result_board = [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'M', 2],
            ['X', 3, 'M', 2],
            ['X', 1, 1, 1]
        ]

        test_solver = Solver()
        test_solver.solver_board.user_board = test_board
        test_solver.solver_board.real_board = real_board
        test_solver.solver_board.n = 4
        self.assertEqual(test_solver.find_clear_cells(), True)
        self.assertEqual(test_solver.solver_board.user_board, result_board)

    def test_win_condition(self):
        test_board = [
            [1, 1, 1, 1],
            ['M', 3, 'X', 2],
            [1, 3, 'M', 2],
            ['.', 1, 1, 1]
        ]

        real_board = [
            [1, 1, 1, 1],
            ['M', 3, 'M', 2],
            [1, 3, 'M', 2],
            ['.', 1, 1, 1]
        ]

        test_solver = Solver()
        test_solver.solver_board.user_board = test_board
        test_solver.solver_board.real_board = real_board
        test_solver.solver_board.n = 4
        test_solver.solver_board.num_mines = 3

        self.assertEqual(test_solver.solver_board.win_condition(), True)

    def test_solve(self):
        test_solver = Solver()
        result = test_solver.solve()

        if result:
            self.assertEqual(test_solver.solver_board.win_condition(), True)
        else:
            self.assertEqual(test_solver.solver_board.win_condition(), False)


if __name__ == "__main__":
    unittest.main()
