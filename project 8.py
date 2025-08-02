alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode ():
    cipher_text = " "
    for letter in list(message):
        if letter not in alphabets:
            cipher_text += letter
        else:
            shifted_index = alphabets.index(letter) + shift
            shifted_index %= len(alphabets)
            cipher_text += alphabets[shifted_index]
        
    print(f"The encoded message is {cipher_text}")

def decode ():
    cipher_text = " "
    for letter in list(message):
         if letter not in alphabets:
            cipher_text += letter
         else:
            shifted_index = alphabets.index(letter) - shift
            shifted_index %= len(alphabets)
            cipher_text += alphabets[shifted_index]
    print(f"The decoded message is {cipher_text}")

def ceaser():
    if direction == "encode":
        encode()
    elif direction == "decode":
        decode()
    else:
        print("Error !")  


should_continue = True
while should_continue == True:
    direction = input("Do you want to 'encode' or 'decode' the message ?\n").lower()
    message = input("Type your message !\n").lower()
    shift = int(input("Type your shift no !\n"))
    ceaser()
    restart = input("To restart type Yes or to exit type no ! \n").lower()
    if restart == "no":
        should_continue = False
        print("goodbye!")
    elif restart == "yes":
        should_continue = True
    else:
        print("error !")





