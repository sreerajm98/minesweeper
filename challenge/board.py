import random


class Board:

    def __init__(self, n, num_mines):
        self.n = n
        self.num_mines = num_mines
        self.user_board = [['X' for x in range(n)] for y in range(n)]
        self.real_board = [['X' for x in range(n)] for y in range(n)]
        # "neighbors" are the cells adjacent above, below, left, right, and all 4 diagonals
        self.neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # neighbor_finder allows us to find neighbors of a specific kind(s) mentioned in the to_find array
    def neighbor_finder(self, r, c, to_find, board):
        result = []
        for (delta_row, delta_col) in self.neighbors:
            if 0 <= r + delta_row < self.n:
                if 0 <= c + delta_col < self.n:
                    if board[r + delta_row][c + delta_col] in to_find:
                        result.append((r + delta_row, c + delta_col))
        return result

    # set_board sets up the data structures for the game.
    # This involves randomly placing mines on the board while
    # making sure that the first move doesn't result in a detonation.
    # The real_board which will be our reference board for the game is
    # also set up using this function
    def set_board(self, first_move):
        if self.n < 2 or self.num_mines >= pow(self.n, 2):
            print("This is an invalid input for the board")
            print("1. Please make sure that the number of mines don't equal or exceed the size of the board")
            print("2. Please set the size of the board to at least be 2")
            return False

        # This set contains the locations where mines are present.
        mine_set = set()

        while len(mine_set) < self.num_mines:
            mine_row, mine_col = random.randint(0, self.n - 1), random.randint(0, self.n - 1)
            while (mine_row, mine_col) in mine_set or (mine_row, mine_col) == first_move:
                mine_row, mine_col = random.randint(0, self.n - 1), random.randint(0, self.n - 1)

            mine_set.add((mine_row, mine_col))

        self.real_board = [['X' for i in range(self.n)] for j in range(self.n)]

        for mine in mine_set:
            self.real_board[mine[0]][mine[1]] = 'M'

        for row in range(self.n):
            for col in range(self.n):
                if self.real_board[row][col] == 'X':
                    total_adjacent_mines = len(self.neighbor_finder(row, col, ['M'], self.real_board))

                    if total_adjacent_mines == 0:
                        self.real_board[row][col] = '.'
                    else:
                        self.real_board[row][col] = total_adjacent_mines
        return True

    # This is a DFS function that recursively cleared all connected empty
    # cells to cell that was just opened.
    def connected_empty_clearer(self, r, c, visited):
        if visited[r][c]:
            return
        if str(self.real_board[r][c]).isdigit():
            self.user_board[r][c] = self.real_board[r][c]
            return
        if self.real_board[r][c] == 'M':
            return
        else:
            visited[r][c] = True
            neighbors = self.neighbor_finder(r, c, ['.', 1, 2, 3, 4, 5, 6, 7, 8], self.real_board)

            for (n_row, n_col) in neighbors:
                if self.real_board[r][c] == '.' and not visited[n_row][n_col]:
                    self.user_board[n_row][n_col] = self.real_board[n_row][n_col]
                    self.connected_empty_clearer(n_row, n_col, visited)
                elif str(self.real_board[r][c]).isdigit() and not visited[n_row][n_col]:
                    self.user_board[n_row][n_col] = self.real_board[n_row][n_col]

    # This function is used to make a move i.e. open a cell. Depending on
    # what is inside the cell, the player could either win or proceed to
    # making the next move.
    def play(self, r, c):
        if r < 0 or r > self.n - 1 or c < 0 or c > self.n - 1:
            print("Please make sure that the row and column you want to open is within the board")
            return True

        if self.user_board[r][c] == 'X':
            self.user_board[r][c] = self.real_board[r][c]
            # Opens a bomb
            if self.real_board[r][c] == 'M':
                return False
            # Open a square with 0 neighboring bombs
            elif self.real_board[r][c] == '.':
                visited = [[False for i in range(self.n)] for j in range(self.n)]
                self.connected_empty_clearer(r, c, visited)

        return True

    # win_condition states if the player has won the game or not.
    # This can be done by checking if the number of unopened cells and
    # marked cells is equal to the total number of mines.
    def win_condition(self):
        total_x = sum([i.count('X') for i in self.user_board])
        total_m = sum([i.count('M') for i in self.user_board])
        if total_x + total_m == self.num_mines:
            return True
        else:
            return False

    # print_user_board prints the board which the user plays with.
    def print_user_board(self):
        to_print = ""
        for r in range(self.n):
            for c in range(self.n):
                to_print += str(self.user_board[r][c]) + "   "
                if c == self.n - 1:
                    to_print += "\n"
        print(to_print + "\n")
