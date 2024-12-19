import math
import time

class TicTacToe:
    def __init__(self):
        self.board = self.create_board()
        self.current_winner = None

    @staticmethod
    def create_board() -> list:
        """Initialize the board with empty spaces."""
        return [' ' for _ in range(9)]


    def print_board(self):
        """Print the current state of the board with horizontal and vertical lines."""
        for row_num in range(3):
            print(f'| {self.board[row_num * 3]} | {self.board[row_num * 3 + 1]} | {self.board[row_num * 3 + 2]} |')
            
            if row_num < 2:
                print('-------------')

    @staticmethod
    def print_board_nums():
        """Print numbers corresponding to the board positions."""
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row_num, row in enumerate(number_board):
            print('| ' + ' | '.join(row) + ' |')
            if row_num < 2:
                print('-------------')
        print()


    def make_move(self, square: int, letter: str) -> bool:
        """Place a letter in the square if it's empty, and check for a winner."""
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square: int, letter: str) -> bool:
        """Check if a player has won."""

        def check_line(indices: list) -> bool:
            """Checks if all squares in the line are the same letter."""
            return all([self.board[i] == letter for i in indices])

        # Check row and column
        row_ind = square // 3
        col_ind = square % 3

        if check_line([row_ind * 3 + i for i in range(3)]):
            return True
        if check_line([col_ind + i * 3 for i in range(3)]):
            return True

        # Check diagonals
        if square % 2 == 0:
            if check_line([0, 4, 8]):  
                return True
            if check_line([2, 4, 6]): 
                return True

        return False

    def empty_squares(self) -> bool:
        """Return True if there are any empty squares left on the board."""
        return ' ' in self.board

    def num_empty_squares(self) -> int:
        """Return the number of empty squares."""
        return self.board.count(' ')

    def available_moves(self) -> list:
        """Return a list of indices of empty squares."""
        return [i for i, x in enumerate(self.board) if x == " "]
