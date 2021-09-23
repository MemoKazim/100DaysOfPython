user_input = int(input("Type number which you want to check prime\n:"))
check = True

if user_input == 1:
    print(f"{user_input} is not prime number!")
else:
    for i in range(2 , user_input):
        if user_input % i == 0:
            check = False
    if check == True:
        print(f"{user_input} is prime number!")
    else:
        print(f"{user_input} is not prime number!")
