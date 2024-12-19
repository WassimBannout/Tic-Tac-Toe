import random
import time
from runner import TicTacToe
from players import HumanTicTacToePlayer, RandomTicTacToeComputerPlayer, MinimaxTicTacToeComputerPlayer


def play(game: TicTacToe, x_player, o_player, print_game=True, delay=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'X':
            square = x_player.get_move(game)
            player = 'X'
        else:
            square = o_player.get_move(game)
            player = 'O'

        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')
                return letter  # Game over

            letter = 'O' if letter == 'X' else 'X'

        if delay:
            time.sleep(1)

    if print_game:
        print("It's a tie!")

if __name__ == '__main__':
    print("Welcome to Tic-Tac-Toe!")
    opponent_choice = input("Choose opponent (0 for random, 1 for minimax): ")
    bot = ''
    human_marker = ''

    if random.choice([True, False]):
        print("Human is X, Bot is O")
        human_marker = 'X'
        bot = 'O'
    else:
        print("Human is O, Bot is X")
        human_marker = 'O'
        bot = 'X'

    if opponent_choice == '0':
        if bot == 'X':
            x_player = RandomTicTacToeComputerPlayer(bot)
            o_player = HumanTicTacToePlayer(human_marker)
        else:
            o_player = RandomTicTacToeComputerPlayer(bot)
            x_player = HumanTicTacToePlayer(human_marker)
    elif opponent_choice == '1':
        if bot == 'X':
            x_player = MinimaxTicTacToeComputerPlayer(bot)
            o_player = HumanTicTacToePlayer(human_marker)
        else:
            o_player = MinimaxTicTacToeComputerPlayer(bot)
            x_player = HumanTicTacToePlayer(human_marker)

    else:
        print("Invalid choice! Defaulting to Minimax AI.")
        if bot == 'X':
            x_player = MinimaxTicTacToeComputerPlayer(bot)
            o_player = HumanTicTacToePlayer(human_marker)
        else:
            o_player = MinimaxTicTacToeComputerPlayer(bot)
            x_player = HumanTicTacToePlayer(human_marker)
        

    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
