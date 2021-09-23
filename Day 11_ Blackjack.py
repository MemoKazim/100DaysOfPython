import random as r

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           

"""
play_game = input("Do you want to play Blackjack game? ('y' or 'n') : ")
while play_game == 'y':
    print(logo)
    computer_cards = []
    computer_cards.append(r.choice(cards))
    computer_cards.append(r.choice(cards))

    dealer_cards = []
    dealer_cards.append(r.choice(cards))
    dealer_cards.append(r.choice(cards))
    print(f"computer cards:\t{computer_cards} = {sum(computer_cards)}\nyour cards:\t{dealer_cards} = {sum(dealer_cards)}")

    if sum(dealer_cards) == 21:
        print("You win!")
        play_game = input("Do you want play again? ('y' or 'n') : ")
        break
    elif sum(computer_cards) == 21:
        print("You lose!")
        play_game = input("Do you want play again? ('y' or 'n') : ")
        break
    else:
        while sum(dealer_cards) < 21 and sum(computer_cards) < 21:
            choice = input("Do you want to draw a card? 'y' or 'n': ")
            while choice == 'y':
                dealer_cards.append(r.choice(cards))
                print(f"computer cards:\t{computer_cards} = {sum(computer_cards)}\nyour cards:\t{dealer_cards} = {sum(dealer_cards)}")
                if sum(dealer_cards) > 21:
                    print("You lose!")
                    play_game = input("Do you want play again? ('y' or 'n') : ")
                    break
                choice = input("Do you want to draw a card? 'y' or 'n': ")
                        
            if choice == 'n':
                while sum(computer_cards) < 17:
                    computer_cards.append(r.choice(cards))
                print(f"computer cards:\t{computer_cards} = {sum(computer_cards)}\nyour cards:\t{dealer_cards} = {sum(dealer_cards)}")
                if sum(dealer_cards) == 21 or sum(computer_cards) > 21 or dealer_cards > computer_cards:
                    print("You win!")
                    play_game = input("Do you want play again? ('y' or 'n') : ")
                    break
                elif sum(computer_cards) == 21 or sum(dealer_cards) > 21 or dealer_cards < computer_cards:
                    print("You lose!")
                    play_game = input("Do you want play again? ('y' or 'n') : ")
                    break
                elif dealer_cards == computer_cards:
                    print("Draw!")
                    play_game = input("Do you want play again? ('y' or 'n') : ")
                    break
                play_game = input("Do you want play again? ('y' or 'n') : ")
                break
