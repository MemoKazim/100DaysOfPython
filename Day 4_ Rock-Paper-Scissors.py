import random as r

play_game = input("Do you want to play rock-paper-scissors game? ('y' or 'n') : ")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock , paper , scissors]
while play_game == 'y':
    user_choice = int(input('Type 0 for rock , 1 for paper , 2 for scissors\n:'))
    computer_choice = r.randint(0,2)

    if user_choice >= 3 or user_choice < 0:
        print("You typed invalid number. You lose!")
        play_game = input("Do you want to play again? ('y' or 'n') : ")
        if play_game == 'n':
            break
    else:
        print(f"Your choise:\t\t {user_choice}\n" + game_images[user_choice] + '\n')
        print(f"Computer choise:\t {computer_choice}\n" + game_images[computer_choice] + '\n')

        if user_choice == 0 and computer_choice == 2:
            print("You win!")
            play_game = input("Do you want to play again? ('y' or 'n') : ")
            if play_game == 'n':
                break
        elif user_choice == 2 and computer_choice == 0:
            print("You lose!")
            play_game = input("Do you want to play again? ('y' or 'n') : ")
            if play_game == 'n':
                break
        elif computer_choice > user_choice:
            print("You lose!")
            play_game = input("Do you want to play again? ('y' or 'n') : ")
            if play_game == 'n':
                break
        elif user_choice > computer_choice:
            print("You win!")
            play_game = input("Do you want to play again? ('y' or 'n') : ")
            if play_game == 'n':
                break
        else:
            print("It is draw!")
            play_game = input("Do you want to play again? ('y' or 'n') : ")
            if play_game == 'n':
                break
