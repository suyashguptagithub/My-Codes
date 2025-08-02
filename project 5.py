import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = [ ]
no_of_char = int(input("How many letters do you want in your password !\n"))
no_of_num = int(input("How many numbers do you want your password !\n"))
no_of_symbl = int(input("How many symbol do you want in your password !\n"))

for char in range(0 , no_of_char):
    password += random.choice(letters)

for num in range(0, no_of_num):
    password += random.choice(numbers)

for sym in range(0, no_of_symbl):
    password += random.choice(symbols)

random.shuffle(password)
print(password)
final_pass = " "
for char in password:
    final_pass += char

print(f"here is ur password {final_pass}")