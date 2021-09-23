MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print("""
WELCOME TO COFFEE MACHINE!!!

                            ██    ██    ██                                    
                        ██      ██  ██                                      
                        ██    ██    ██                                      
                            ██  ██      ██                                    
                            ██    ██    ██                                    
                                                                            
                        ████████████████████                                  
                        ██                ██████                              
                        ██                ██  ██                              
                        ██                ██  ██                              
                        ██                ██████                              
                        ██            ██                                    
                    ████████████████████████                                
                    ██                    ██                                
                        ████████████████████      


""")

while True:
    user_input = input('What would you like to drink? (espresso / latte / cappuccino) : ')
    if user_input == 'report':
        print(f'Water: {resources["water"]} ml\nMilk: {resources["milk"]} ml\nCoffee: {resources["coffee"]} gr')

    elif user_input == 'espresso':
        if resources['water'] < MENU['espresso']['ingredients']['water'] or resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
            print('There is not enought resources for this sorry...')
        else:
            print('Input money...')
            penny_coin = int(input('number of penny coin (0.01$) : '))
            nickel_coin = int(input('number of nickel coin (0.05$) : '))
            dime_coin = int(input('number of dime coin (0.10$) : '))
            quarter_coin = int(input('number of quarter coin (0.25$) : '))
            user_total_coin = round(0.01 * penny_coin + 0.05 * nickel_coin + 0.10 * dime_coin + 0.25 * quarter_coin , 3)
            print(f'Total inserted money is {user_total_coin}')
            if user_total_coin < MENU["espresso"]["cost"]:
                print('There is no enought money, payment refused and refund.')
            elif user_total_coin == MENU["espresso"]["cost"]:
                print('Here is your coffee...')
                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
            else:
                print(f'Here is your coffee...\nCharge of bill: {user_total_coin - MENU["espresso"]["cost"]} take it.')
                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']

    elif user_input == 'latte':
        if resources['water'] < MENU['latte']['ingredients']['water'] or resources['coffee'] < MENU['latte']['ingredients']['coffee'] or resources['milk'] < MENU['latte']['ingredients']['milk']:
            print('There is not enought resources for this sorry...')
        else:
            print('Input money...')
            penny_coin = int(input('number of penny coin (0.01$) : '))
            nickel_coin = int(input('number of nickel coin (0.05$) : '))
            dime_coin = int(input('number of dime coin (0.10$) : '))
            quarter_coin = int(input('number of quarter coin (0.25$) : '))
            user_total_coin = round(0.01 * penny_coin + 0.05 * nickel_coin + 0.10 * dime_coin + 0.25 * quarter_coin , 3)
            print(f'Total inserted money is {user_total_coin}')
            if user_total_coin < MENU["latte"]["cost"]:
                print('There is no enought money, payment refused and refund.')
            elif user_total_coin == MENU["latte"]["cost"]:
                print('Here is your coffee...')
                resources['water'] -= MENU['latte']['ingredients']['water']
                resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                resources['milk'] -= MENU['latte']['ingredients']['milk']
            else:
                print(f'Here is your coffee...\nCharge of bill: {user_total_coin - MENU["latte"]["cost"]} take it.')
                resources['water'] -= MENU['latte']['ingredients']['water']
                resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                resources['milk'] -= MENU['latte']['ingredients']['milk']

    elif user_input == 'cappuccino':
        if resources['water'] < MENU['cappuccino']['ingredients']['water'] or resources['coffee'] < MENU['cappuccino']['ingredients']['coffee'] or resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
            print('There is not enought resources for this sorry...')
        else:
            print('Input money...')
            penny_coin = int(input('number of penny coin (0.01$) : '))
            nickel_coin = int(input('number of nickel coin (0.05$) : '))
            dime_coin = int(input('number of dime coin (0.10$) : '))
            quarter_coin = int(input('number of quarter coin (0.25$) : '))
            user_total_coin = round(0.01 * penny_coin + 0.05 * nickel_coin + 0.10 * dime_coin + 0.25 * quarter_coin , 3)
            print(f'Total inserted money is {user_total_coin}')
            if user_total_coin < MENU["cappuccino"]["cost"]:
                print('There is no enought money, payment refused and refund.')
            elif user_total_coin == MENU["cappuccino"]["cost"]:
                print('Here is your coffee...')
                resources['water'] -= MENU['cappuccino']['ingredients']['water']
                resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
            else:
                print(f'Here is your coffee...\nCharge of bill: {user_total_coin - MENU["cappuccino"]["cost"]} take it.')
                resources['water'] -= MENU['cappuccino']['ingredients']['water']
                resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                resources['milk'] -= MENU['cappuccino']['ingredients']['milk']

    else:
        print(f"invalid input '{user_input}'")
        break