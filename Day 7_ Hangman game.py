import random as r

words = ['africa' , 'america' , 'bookshelf' , 'waitress' , 'animals']
rand = round(r.randint(0,4))
current_word = words[rand]
current_word = list(current_word)
display = ''
for _ in range (len(current_word)):
    display += '_ '

print(display , '\n')

count = 0
while True:
    user_input_char = input('Guess letter: ').lower()

    p=False
    for i in current_word:
        if user_input_char == i:
            p=True
    if p == False:
        count+=1
        if count == 1:
            print(r"""
+-------+
|          |
|          0
|
|
|
=========
""")
            print(display)
        elif count == 2:
            print(r"""
+-------+
|          |
|          0
|          |
|
|
=========
""")
            print(display)
        elif count == 3:
            print(r"""
+-------+
|          |
|          0
|        /|
|
|
=========
""")
            print(display)
        elif count == 4:
            print(r"""
+-------+
|          |
|          0
|        /|\
|
|
=========
""")
            print(display)
        elif count == 5:
            print(r"""
+-------+
|          |
|          0
|        /|\
|         /
|
=========
""")
            print(display)
        elif count == 6:
            print(r"""
+-------+
|          |
|          0
|        /|\
|         /\
|
=========
""" , '\n\nGAME OVER. YOU LOST GAME')
            print(display)
            break
    else:
        for i in range (len(current_word)):
            letter = current_word[i]
            if letter == user_input_char:
                current_word[i] = '-'
                display = list(display)
                i*=2
                display[i] = user_input_char
                display = ''.join(map(str, display))
        print(display)
        game_over = True
        for i in display:
            if i == '_':
                game_over=False

        if game_over == True:
            print('CONGRATULATIONS!\nYOU WON GAME!')
            break
            
