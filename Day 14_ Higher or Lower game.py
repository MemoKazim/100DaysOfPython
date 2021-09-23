import random

logo = r"""

  _    _ _       _               
 | |  | (_)     | |              
 | |__| |_  __ _| |__   ___ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__|
 | |  | | | (_| | | | |  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|   
 | |        __/ |                
 | |     __|___/    _____ _ __   
 | |    / _ \ \ /\ / / _ \ '__|  
 | |___| (_) \ V  V /  __/ |     
 |______\___/ \_/\_/ \___|_|     
                                 
                                 


***RULES***
1. You should guess that next number will be higher or lower
2. Number scale is 1 - 10000
3. Good luck :)
"""



play_game = input("Do you want to play 'Higher or Lower' game? (type 'y' for yes , 'n' for no) : ")
player_score = 0
showen_number = random.randint(1,10000)
if play_game == 'y':
    print(logo)
while play_game == 'y':
    player_choice = input(f"Current number is {showen_number}.\nNext number will be ('h' for higher , 'l' for lower) : ")
    chosen_number_2 = random.randint(1,10000)
    if player_choice == 'h':
        if showen_number <= chosen_number_2:
            player_score+=1
            print(f'You found. Your score is {player_score}.')
        else:
            print(f'You lost. Last score is {player_score}')
            play_game = input("Do you want to try again? 'y' or 'n' : ")
            if play_game == 'n':
                break
            elif play_game == 'y':
                print(logo)
    elif player_choice == 'l':
        if showen_number >= chosen_number_2:
            player_score+=1
            print(f'You found. Your score is {player_score}.')
        else:
            print(f'You lost. Last score is {player_score}')
            play_game = input("Do you want to try again? 'y' or 'n' : ")
            if play_game == 'n':
                break
            elif play_game == 'y':
                replit.clear()
                print(logo)
    else:
        replit.clear()
        print(f'Invalid input: {player_choice}')
        play_game = input("Do you want to try again? 'y' or 'n' : ")
        if play_game == 'n':
            break
        elif play_game == 'y':
            print(logo)
    
    showen_number = chosen_number_2
