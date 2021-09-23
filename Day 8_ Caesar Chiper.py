def encrypt(text , shift):
    encrypted_text=''
    while shift >= 26:
        shift = shift % 26
    for i in text:
        if 65 <= ord(i) <= 90:
            if 65 <= ord(i) + shift <= 90:
                encrypted_text += chr(ord(i) + shift)
            else:
                encrypted_text += chr((ord(i)+shift)%90+64)
            
            

        elif 97 <= ord(i) <= 122:
            if 97 <= ord(i) + shift <= 122:
                encrypted_text += chr(ord(i) + shift)
            else:
                encrypted_text += chr((ord(i)+shift)%122+96)
            
            
        else:
            encrypted_text += i
             
    print(f"The encoded text is {encrypted_text}")

def decrypt(text , shift):
    decrypted_text=''
    while shift >= 26:
        shift = shift % 26
    for i in text:
        if 65 <= ord(i) <= 90:
            if 65 <= ord(i) - shift <= 90:
                decrypted_text += chr(ord(i) - shift)
            else:
                decrypted_text += chr((ord(i) - shift) % 90 + 64)
            
            

        elif 97 <= ord(i) <= 122:
            if 97 <= ord(i) - shift <= 122:
                decrypted_text += chr(ord(i) - shift)
            else:
                decrypted_text += chr((ord(i) - shift) % 122 + 96)
            
            
        else:
            decrypted_text += i
             
    print(f"The decoded text is {decrypted_text}")



print("""

   _____                              _____ _       _                
  / ____|                            / ____(_)     | |               
 | |     __ _  ___  ___  __ _ _ __  | |     _ _ __ | |__   ___ _ __  
 | |    / _` |/ _ \/ __|/ _` | '__| | |    | | '_ \| '_ \ / _ \ '__| 
 | |___| (_| |  __/\__ \ (_| | |    | |____| | |_) | | | |  __/ |    
  \_____\__,_|\___||___/\__,_|_|     \_____|_| .__/|_| |_|\___|_|    
                                             | |                     
                                             |_| 

""")

repeat = 'yes'
while repeat == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != 'encode' and direction != 'decode':
        print('You entered invalid option.')
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))


        if direction == 'encode':
            encrypt(text , shift)
        elif direction == 'decode':
            decrypt(text , shift)


    repeat = input("Do you want to repeat? (type 'yes' for use again, 'no' for break)\n:").lower()
