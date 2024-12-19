import random
import math

class TicTacToePlayer:
    def __init__(self, letter: str):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanTicTacToePlayer(TicTacToePlayer):
    def __init__(self, letter: str):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again. Enter a number between 0-8 and select an empty square.")
        return val


class RandomTicTacToeComputerPlayer(TicTacToePlayer):
    def __init__(self, letter: str):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class MinimaxTicTacToeComputerPlayer(TicTacToePlayer):
    def __init__(self, letter: str):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player: str):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # Base case: check if the opponent has won
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # Simulate the game after the move

            # Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # Save the position of the best move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
