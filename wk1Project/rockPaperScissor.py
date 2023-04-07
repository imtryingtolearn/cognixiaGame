
from datetime import datetime
from pathlib import Path
import random
from time import strftime




def gameOfRPS():
    """setting global variables for all the possible game options, 
    as well as setting the scores of any player involved in the game to 0
    """
    validchoice= ("R","P","S")
    player1 = 0
    player2 = 0
    CPU = 0
    games = 0
    loses = ("\U0001F612","\U0001F605","\U0001F910")
    wins = ("\U0001F601","\U0001F923","\U0001F602")
    playersSelect= (1,2)

    
    
    # setting up the game by asking how many players are playing
    # how many games to determine best of however many games.
    
    players = int(input("\nHow many players are playing, Enter 1 or 2: "))
    amtGame = int(input("\nBest of how many games would you like to play odd numbers only: "))
    
    # getting the breaking point of the game, the target score
    targetScore = int(amtGame /2 + 1)
    
    """determining if its a multiplier game setup or a single vs cpu game."""
    while (players in playersSelect):
        while amtGame % 3 == 0:
            if players == 2:
                
                # while runGame:
                """checking to make sure no one has reached the target score, and while  thats true
                    running through the game by asking the players what they choose of teh options
                    depending on the out if player 1 wins the score increments, if player 2 wins
                    player2 score is incremented otherwise it is a draw and no one gets credited points"""
                while (player1 < targetScore) and (player2 < targetScore):
                    p1 = input("\nplayer1 Enter r: Rock, p: Paper, s: Scissor: ").capitalize()
                    p2 = input("\nplayer2 Enter r: Rock, p: Paper, s: Scissor:  ").capitalize()
                    #checks to make sure the input by player1 and player 2
                    while (p1 in validchoice) and (p2 in validchoice):
                        if p1 == "R" and p2 == "S" or p1 == "P" and p2 == "R" or p1 == "S" and p2 == "P":
                            ranW= random.choice(wins)
                            ranL= random.choice(loses)
                            print(f"\nplayer 1 wins with {toSpell(p1)} {ranW}!\n")
                            print(f"\nplayer 2 loses {ranL}\n")
                            player1 += 1
                            
                        elif p2 == "R" and p1 == "S" or p2 == "P" and p1 == "R" or p2 == "S" and p1 == "P":
                            ranW= random.choice(wins)
                            ranL= random.choice(loses)
                            print(f"\nplayer 2 wins with {toSpell(p2)} {ranW}!\n")
                            print(f"\nplayer 1 loses {ranL}\n")
                            player2 += 1
                            
                        else: print("\nIt's a draw\n") 
                        break
                    else:print("\nTry again!\n")
                    print(f"\nCurrent Score Player1:\t{player1}\t\t Player2:\t{player2}\t\tYour Target Score:\t{targetScore}")
                    games += 1
                try:
                    new_file= Path("wk1Project/logFile.txt")
                    if new_file.is_file():
                        with open("wk1Project/logFile.txt","a") as new_file:
                            dt = datetime.now()
                            timeS = dt.strftime("%c")
                            new_file.write(f"\n\n--------------\nFinal Scores\n-------\nYou played {games} rounds\nPlayer 1:\t{player1}\nPlayer 2:\t{player2}\n{timeS}\n")
                    else: 
                        new_file=open("wk1Project/logFile.txt", "x")
                        dt = datetime.now()
                        timeS = dt.strftime("%c")
                        new_file.write(f"\n--------------\nFinal Scores\n-------\nYou played {games} rounds\nPlayer 1:\t{player1}\nPlayer 2:\t{player2}\n{timeS}\n")
                        new_file.close()
                except FileNotFoundError:
                    print(f"This file {new_file} is not found")
                    new_file.close()
                print (f"\nFinal from your game\nPlayer1 Score: {player1}  \nPlayer2 Score: {player2}\n")
            else:  
                
                print(f"\nThe first player to {targetScore} wins!\n")
                while (player1 < targetScore) and (CPU < targetScore):
                    p1 = input("\nplayer1 Enter r: Rock, p: Paper, s: Scissor: ").capitalize()
                    cpu = random.choice(validchoice).capitalize()
                    print(f"\nCPU selected: {toSpell(cpu)}")
                    while p1 in validchoice:
                        if p1 == "R" and cpu == "S" or p1 == "P" and cpu == "R" or p1 == "S" and cpu == "P":
                            ranW= random.choice(wins)
                            ranL= random.choice(loses)
                            print(f"\nplayer 1 wins with {toSpell(p1)} {ranW}!")
                            print(f"\nCPU loses {ranL}")
                            player1 += 1
                        elif cpu == "R" and p1 == "S" or cpu == "P" and p1 == "R" or cpu == "S" and p1 == "P":
                            ranW= random.choice(wins)
                            ranL= random.choice(loses)
                            print(f"\nCPU wins with {toSpell(cpu)} {ranW}!")
                            print(f"\nplayer 1 loses {ranL}")
                            CPU += 1
                        else: print("\nIt's a draw\n") 
                        break
                    else:print("\nTry again!\n")
                    print(f"\nCurrent Score Player1:\t{player1}\t\t CPU:\t{CPU}\t\tYour Target Score:\t{targetScore}")
                    games += 1
                try:
                    new_file= Path("wk1Project/logFile.txt")
                    if new_file.is_file():
                        with open("wk1Project/logFile.txt","a") as new_file:
                            dt = datetime.now()
                            timeS = dt.strftime("%c")
                            new_file.write(f"\n\n--------------\nFinal Scores\n-------\nYou Played {games} rounds\nPlayer 1:\t{player1}\nCPU:\t\t{CPU}\n {timeS}")
                    else: 
                        new_file=open("wk1Project/logFile.txt", "x")
                        dt = datetime.now()
                        timeS = dt.strftime("%c")
                        new_file.write(f"\n--------------\nFinal Scores\n-------\nYou played {games} rounds\nPlayer 1:\t{player1}\nCPU:\t\t{CPU}\n{timeS}")
                        new_file.close()
                except FileNotFoundError:
                    print(f"This file {new_file} is not found")
                    new_file.close()
                print (f"\nFinal from your game\nPlayer1 Score: {player1}  \nCPU Score: {CPU}")
            break   
        else:
            print(f"\nTry again, {amtGame} is not an acceptable entry!\n")     
        break
    restartGame()
def restartGame():
    start = input("Would you like to play again (Y/N):").capitalize()
    if start == "Y":
        gameOfRPS()
    else: return 0

def toSpell(x):
    if x == "S":
        return "Scissors"
    elif x == "R":
        return "Rock"
    else: return "paper"