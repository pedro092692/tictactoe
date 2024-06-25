from game import Game
import os
from art import logo


def play_game():
    game = Game()
    print(logo)
    single_player = False
    single = input('Do you want to play against cpu? Y/N ').lower()
    if single == 'y':
        single_player = True

    while True:
        try:
            position = int(input(f'Select your play ({game.player}) '))
            # os.system('cls')
            if game.check_play(play=position):
                game.play_game(position=position)
                if single_player:
                    game.cpu_play()
                if game.check_winner():
                    print('Finish game')
                    new_game = input('Do you want to play a new game? Y/N ').lower()
                    if new_game == 'y':
                        play_game()
                    return
        except ValueError:
            print('Invalid input Please Select 1-9 ')


play_game()

