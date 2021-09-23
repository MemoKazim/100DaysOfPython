logo = r"""

  _______ _            _   _                 _                           
 |__   __| |          | \ | |               | |                          
    | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __             
    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|            
    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |               
    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|               
   _____                     _                _____                      
  / ____|                   (_)              / ____|                     
 | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \
 | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
  \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                      __/ |                              
                                     |___/                               

"""

import random as r

print(logo)
print("Welcome to number guessing game.")
print("""
***RULES***
1. You have to guess number between 1 and 100.
2. You should find number as soon as possible
3. Easy mode: you will have 10 attempt to find number
4. Hard mode: you will have 5 attempt to find number
5. Good Luck :)
""")
retry = input("Do you want to play the number guessing game? 'y' or 'n' : ")


while retry == 'y':
    chosen_number = r.randint(1,100)
    difficulty_choice = input("Choose difficulty. Type 'easy' or 'hard' : ")
    if difficulty_choice == 'easy':
        remaining_guess = 10
        while remaining_guess > 0:
            user_input = int(input('Guess number : '))
            if chosen_number > user_input:
                print('Too low')
                remaining_guess -=1
                print(f'You have {remaining_guess} attempt remaining')
            
            elif chosen_number < user_input:
                print('Too high')
                remaining_guess -=1
                print(f'You have {remaining_guess} attempt remaining')

            else:
                print('You found number!\nYou win!!!')
                retry = input("Do you want to play again? 'y' or 'n' : ")
                break


    elif difficulty_choice == 'hard':
        remaining_guess = 5
        while remaining_guess > 0:
            user_input = int(input('Guess number : '))
            if chosen_number > user_input:
                print('Too low')
                remaining_guess -=1
                print(f'You have {remaining_guess} attempt remaining')
            
            elif chosen_number < user_input:
                print('Too high')
                remaining_guess -=1
                print(f'You have {remaining_guess} attempt remaining')

            else:
                print('You found number!\nYou win!!!')
                retry = input("Do you want to play again? 'y' or 'n' : ")
                break

    else:
        print("invalid input.")
        retry = input("Do you want to play again? 'y' or 'n' : ")
