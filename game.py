import os
import random


class Game:
    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        self.board_plays = [0, 0, 0,
                            0, 0, 0,
                            0, 0, 0]

        self.winning_plays = [[0, 1, 2], [3, 4, 5],
                              [6, 7, 8], [0, 3, 6],
                              [1, 4, 7], [2, 5, 8],
                              [0, 4, 8], [2, 4, 6],
                              [1, 4, 7]]

        self.player = 'X'

        self.turn = 1

        self.cpu_moves = []

    def play_game(self, position):
        self.print_board(position=position)

    def check_play(self, play):

        if play < 1 or play > 9:
            print('Position Our Of Range Please Select 1-9 ')
            return False
        if self.board_plays[play-1] != 0:
            print('This Position Is Already Taken ')
            return False

        return play

    def select_turn(self):
        if self.turn % 2 != 0:
            self.player = 'X'
        else:
            self.player = '0'

    def print_board(self, position):
        self.board[position - 1] = self.player
        self.board_plays[position - 1] = self.player

        self.single_player()
        board = f' {self.board[0]} | {self.board[1]} | {self.board[2]} \n' \
                f'___|___|___ \n' \
                f' {self.board[3]} | {self.board[4]} | {self.board[5]} \n' \
                f'___|___|___ \n' \
                f' {self.board[6]} | {self.board[7]} | {self.board[8]} \n' \
                f'   |   |   '
        self.turn += 1
        self.select_turn()
        print(board)

    def check_winner(self):
        if 0 not in self.board_plays:
            print('Tie')
            return True

        for winner_play in self.winning_plays:
            if self.board_plays[winner_play[0]] == self.board_plays[winner_play[1]] == self.board_plays[winner_play[2]] != 0:
                if self.board_plays[winner_play[0]] == 'X':
                    print('Player X Wins')
                elif self.board_plays[winner_play[0] == '0']:
                    print('Player 0 Wins')

                return True

    def single_player(self, free=None):

        free_position = [position for position in range(len(self.board_plays)) if self.board_plays[position] != 'X']
        if free:
            return free_position
        else:
            return self.calculate_move(free_position=free_position)

    def calculate_move(self, free_position):
        next_moves = []
        for positions in self.winning_plays:
            if positions[0] in free_position and positions[1] in free_position and positions[2] in free_position:
                next_moves.append(positions)

        return next_moves

    def cpu_play(self):
        if not self.check_winner():
            try:
                moves = self.single_player()[-1]
                for move in moves:
                    if move not in self.cpu_moves:
                        next_move = move
                        self.cpu_moves.append(move)
                        break
            except IndexError:
                free_position = [position for position in range(len(self.board_plays))
                                                 if self.board_plays[position] == 0]
                next_move = random.choice(free_position)

            self.play_game(position=next_move + 1)

