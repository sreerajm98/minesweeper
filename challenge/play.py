from board import Board
import argparse


def game(n, num_mines):

    game_board = Board(n, num_mines)
    game_board.print_user_board()

    print("Enter your next move as shown below:")
    print("row col")

    move = input().split()

    while (not move[0].isdigit() or not move[1].isdigit() or
           int(move[0]) < 0 or int(move[0]) > n - 1 or int(move[1]) < 0 or int(move[1]) > n - 1):
        print ("Invalid move, please enter row and col values between 0 and " + str(n - 1))
        move = input().split()

    move_row = int(move[0])
    move_col = int(move[1])

    game_board.set_board((move_row, move_col))

    is_playing = game_board.play(move_row, move_col)

    while is_playing:

        game_board.print_user_board()

        if game_board.win_condition():
            return True

        print("Enter your next move as shown below:")
        print("row col")
        move = input().split()
        move_row = int(move[0])
        move_col = int(move[1])
        is_playing = game_board.play(move_row, move_col)

    game_board.print_user_board()
    return False


def main(n, num_mines):
    print("Welcome to MineSweeper!" + "\n")

    if game(int(n), int(num_mines)):
        print("Congrats! You have won the game!")
    else:
        print("Game Over! Better Luck Next Time!")


# DO NOT EDIT--------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', nargs='?', type=int, default=10)
    parser.add_argument('num_mines', nargs='?', type=int, default=10)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args.n, args.num_mines)

# DO NOT EDIT--------------------------------------------
