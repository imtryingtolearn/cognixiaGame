''' This is the main file. Run this file to select and play a particular
    game.'''

from rockPaperScissor import gameOfRPS
# from c4 import *

game_lib = {
    1: "Rock,Paper,Scissor",
    2: "Tic-Tac-Toe(Currently Unavailable)"
  
}
while True:
    print(f"-----------------------------\nYour game library:\n1:{game_lib[1]}\n2:{game_lib[2]}")
    game_choice = input("\nWhat game would you like to play? Input the game ID, or type 'exit' to exit:\t")

    if game_choice == '1':
        gameOfRPS()
        game_choice = None

    # elif game_choice == '2':
    #     play_c4()
    #     game_choice = None

    # elif game_choice == '3':
    #     play_checkers()

    elif game_choice == 'exit':
        break