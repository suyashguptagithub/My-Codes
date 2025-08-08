# #Fair ticket 
# age = input("wht is ur age ?\n ")

# if int(age) < 8:
#     print("You are not allowded")
# elif int(age) < 12:
#     height = input("what is ur height ?\n")
#     if int(height) < 30:
#          print("You are not allowded")
#     else:
#         print("You r good to go and ur fair ticket is 5rs")
# elif int(age) < 18:
#     height = input("what is ur height ?\n")
#     if int(height) < 30:
#          print("You are not allowded")
#     else:
#         print("You r good to go and ur fair ticket is 10rs")
# else:
#     height = input("what is ur height ?\n")
#     if int(height) < 30:
#          print("You are not allowded")
#     else:
#         print("You r good to go and ur fair ticket is 15rs")
# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# if bmi <= 18.5: 
#     print("underweight")
# elif bmi <= 25:
#     print("normal")
# else:
#     print("overweight")





# bill = 10
# height = int(input("what is the height of person ? \n"))

# if height >= 140:
#     age = int(input("what is the age of the person ? \n"))

#     if age >= 10:
#         bill = bill + 3
#         print(f"You are a teen so ur ticket is {bill}")
#         photo = str(input("Do u want to take picture ? Yes/ No \n"))
#         if photo == "yes":
#              bill = bill + 5
#              print(f"your ticket price with photograph is {bill}")
#         elif photo == "no":
#             bill = bill
#             print(f"your ticket price without photograph is {bill}")

#     elif age >= 18:
#         bill = bill + 5
#         print(f"You are an adult so ur ticket is {bill}")
#         photo = str(input("Do u want to take picture ? Yes/ No \n"))
#         if photo == "yes":
#              bill = bill + 5
#              print(f"your ticket price with photograph is {bill}")
#         elif photo == "no":
#             bill = bill
#             print(f"your ticket price without photograph is {bill}")

#     else:
#         print("you are not allowded to roller coster !!")
        
# else:
#  print("you are not allowded to roller coster !!")


# # pizza project 

# small_size = 300
# medium_size = 500
# large_size = 800
# bill = 0
# pizza = str(input("What size of pizza u want ? s for small(300), m for medium(500rs) and l for large (800rs) !\n"))

# if pizza == "s":
#     bill += small_size
#     toppings = str(input("what topings u want? olives (+20)/ tamato(+30)/ peporeni(+50).\n"))
#     if toppings == "olives":
#         bill += 20
#     elif toppings == "tamato":
#         bill += 30
#     elif toppings == "peporeni":
#         bill += 50
#     else:
#         bill == bill
#     cheese = str(input("Do u want extra cheese(+40)? Yes - y , No - n. \n"))
#     if cheese == "y":
#         bill += 40
#         print(f"Yor bill for your pizza would be {bill} rs !")
#     else:
#         bill == bill
#         print(f"Yor bill for your pizza would be {bill} rs !")

# elif pizza == "m": 
#     bill += medium_size
#     toppings = str(input("what topings u want? olives (+20)/ tamato(+30)/ peporeni(+50).\n"))
#     if toppings == "olives":
#         bill += 20
#     elif toppings == "tamato":
#         bill += 30
#     elif toppings == "peporeni":
#         bill += 50
#     else:
#         bill == bill
#     cheese = str(input("Do u want extra cheese(+40)? Yes - y , No - n. \n"))
#     if cheese == "y":
#         bill += 40
#         print(f"Yor bill for your pizza would be {bill} rs !")
#     else:
#         bill == bill
#         print(f"Yor bill for your pizza would be {bill} rs !")

# elif pizza == "l":
#     bill += large_size
#     toppings = str(input("what topings u want? olives (+20)/ tamato(+30)/ peporeni(+50).\n"))
#     if toppings == "olives":
#         bill += 20
#     elif toppings == "tamato":
#         bill += 30
#     elif toppings == "peporeni":
#         bill += 50
#     else:
#         bill == bill
#     cheese = str(input("Do u want extra cheese(+40)? Yes - y , No - n. \n"))
#     if cheese == "y":
#         bill += 40
#         print(f"Yor bill for your pizza would be {bill} rs !")
#     else:
#         bill == bill
#         print(f"Yor bill for your pizza would be {bill} rs !")
# else: 
#     print("we can process this request!!")


# import random

# random_int = random.randint(2, 90)

# print(random_int)

# random_no = random.randint(0,1)
# if random_no == 1:
#     print("heads")
# else:
#     print("tails")

# sates_of_india = ["madhya pradesh", "tamilnadu", "westbengal", "maharastra", "hariyana"]


# sates_of_india.append = "Delhi"
# print(sates_of_india)

# sates_of_india.extend(["assam", "nagaland"])
# print(sates_of_india)

# import random
# friends =["anhul",'aman',"vickey", "aditya", "pratik", "suyash"]
# # random_name = random.choice(friends)
# # print(random_name)

# random_name = random.randint(0, 5)
# print(friends[random_name])

#russian rollute 

# import random
# friends =["anhul",'aman',"vickey", "aditya", "pratik", "suyash"]
# count = len(friends)

# all_ready = str(input(f"do all {count} people ready ?\n")).lower()

# if all_ready == "yes":
#     bill_payer = random.choice(friends)

#     print(f"{bill_payer} is going to pay the bill of {count} of us!")
# elif all_ready == "no":
#     ask_why = str(input("Why all not ready ? add new member or remove a member?\n")).lower()
#     if ask_why == "add new member":
        
#         ask_new_name = str(input("who wants to add ? name pls !\n"))
#         friends.append(ask_new_name)
#         print(f"{ask_new_name} is added to list !")
#         count = len(friends)
#         ask = str(input("should we continue ? Only yes and no !\n")).lower()
#         if ask == "yes":
#             bill_payer = random.choice(friends)
#             print(f"{bill_payer} is going to pay the bill of {count} of us!")
#         else:
#              print("error!!")

#     elif ask_why == "add new members":

#         ask_new_names = str(input("who wants to add ? names pls in list format !\n"))
#         new_members = eval(ask_new_names)
#         friends.extend([new_members])
#         print(f"{new_members} is added to list !")
#         count = len(friends)
#         ask = str(input("should we continue ? Only yes and no !\n")).lower()

#         if ask == "yes":
#             bill_payer = random.choice(friends)
#             print(f"{bill_payer} is going to pay the bill of {count} of us!")
#         else:
#              print("error!!")

#     else:
#         print("error!!")
# else:
#         print("Only yes and no is allowded!!")

# friends =["anhul",'aman',"vickey", "aditya", "pratik", "suyash"]

# # quantity = len(friends)
# # print(friends[quantity -1  ])

# friends.anshul()

# home_friends =["anhul",'aman',"vickey", "aditya", "pratik", "suyash"]
# school_friends = ["himanshu", "prakhyat", "kartik", "rounak"]

# all_Friends = [home_friends, school_friends]
# # print(all_Friends[1][2])
 
# for friends in home_friends:
#     print(friends)

# students_score = [ 223, 300, 129, 349, 453]
# max_score = 0 
# for score in students_score:
#     if score > max_score:
#        max_score = score
# print(max_score)
# print(students_score)
 
# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# password = [ ]
# no_of_char = int(input("How many letters do you want in your password !\n"))
# no_of_num = int(input("How many numbers do you want your password !\n"))
# no_of_symbl = int(input("How many symbol do you want in your password !\n"))

# for char in range(0 , no_of_char):
#     password += random.choice(letters)

# for num in range(0, no_of_num):
#     password += random.choice(numbers)

# for sym in range(0, no_of_symbl):
#     password += random.choice(symbols)

# random.shuffle(password)
# print(password)
# final_pass = " "
# for char in password:
#     final_pass += char

# print(f"here is ur password {final_pass}")

# def numbers():
#     print(123)
# for num in range(6):
# 	numbers()
      


# def greet_with_name(NAME, LOCATION):
#     print(f"hello {NAME}")
#     print('Good Morning !')
#     print(f"Today weather is nice in {LOCATION}")


# # greet_with_name(NAME="SUYASH", LOCATION= "INDORE")
# Word1 = ["T", "R", "U", "E"]
# Word2 = ["L", "O", "V", "E"]

# def calculate_love_score():
#     name1 = "Suyash"
#     name2 = "Robots"

#     names = (name1 + name2).lower()
#     new_word1 = [letter.lower() for letter in Word1]
#     new_word2 = [letter.lower() for letter in Word2]
# unt1) + str(count2))}")

# calculate_love_score()


#     count1 = sum(names.count(letter) for letter in new_word1)
#     count2 = sum(names.count(letter) for letter in new_word2)

#     print(f"Total in TRUE: {count1}")
#     print(f"Total in LOVE: {count2}")
#     print(f"Final LOVE score: {int(str(count) 


# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number: \n"))
# if direction == "encode":
#     def encrypt():
#         listed_name = list(text)
#         a = len(text)
#         while a != 0:
#             full_letter = [ ]
#             for each_alpha in alphabets:
#                 if each_alpha == listed_name:
#                     a -= 1
#                     index = alphabets.index(each_alpha)
#                     new_index = index + shift 
#                     shifted_letter = alphabets[new_index]
#                     full_letter.append(shifted_letter)
#         print(full_letter)


# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def greet(name, age):
#     print(f"Good morning {name} !\n")
#     print(f"Your age is {age} \n")

# greet(age=18, name="Suyash")


# def calculate_love_score():
#     name1 = input("what is the name of person 1\n").lower()
#     name2 = input("what is the name of person 2\n").lower()
    
#     combined_name = name1 + name2
    
#     word1 = "TRUE"
#     word2 = "LOVE"
    
#     True_total = 0 
#     for each_letter in word1:
#         x = combined_name.count(each_letter.lower())
#         print(f"{each_letter} occurs {x} times.\n")
#         True_total += x
#     print(f"Total = {True_total}\n")       
    
#     love_total = 0 
#     for each_letter in word2:
#         y = combined_name.count(each_letter.lower())
#         print(f"{each_letter} occurs {x} times.\n") 
#         love_total += y
#     print(f"Total = {love_total}\n")

#     love_score = int(str(True_total) + str(love_total))
#     print(f"Love Score = {love_score}")
    
# calculate_love_score()




# def calculate_love_score():
#     name1 = input("What is the name of person 1?\n").lower()
#     name2 = input("What is the name of person 2?\n").lower()
    
#     combined_name = name1 + name2  # combine as string

#     word1 = "TRUE"
#     word2 = "LOVE"

#     # Count total occurrences of letters from "TRUE"
#     true_total = 0
#     for letter in word1:
#         count = combined_name.count(letter.lower())
#         print(f"{letter} occurs {count} times.")
#         true_total += count
#     print(f"Total TRUE score = {true_total}\n")

#     # Count total occurrences of letters from "LOVE"
#     love_total = 0
#     for letter in word2:
#         count = combined_name.count(letter.lower())
#         print(f"{letter} occurs {count} times.")
#         love_total += count
#     print(f"Total LOVE score = {love_total}\n")

#     # Calculate love score
#     love_score = int(str(true_total) + str(love_total))
#     print(f"Love Score = {love_score}")

# calculate_love_score()


# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Do you want to 'encode' or 'decode' the message ?\n").lower()
# message = input("Type your message !\n").lower()
# shift = int(input("Type your shift no !\n"))


# def encode ():
#     cipher_text = " "
#     for letter in list(message):
#         shifted_index = alphabets.index(letter) + shift
#         shifted_index %= len(alphabets)
#         cipher_text += alphabets[shifted_index]
#     print(f"The encoded message is {cipher_text}")

# def decode ():
#     cipher_text = " "
#     for letter in list(message):
#         shifted_index = alphabets.index(letter) - shift
#         shifted_index %= len(alphabets)
#         cipher_text += alphabets[shifted_index]
#     print(f"The decoded message is {cipher_text}")   

# if direction == "encode":
#     encode()
# elif direction == "decode":
#     decode()
# else:
#     print("Error !")  


# student = {
#     "name": "Suyash",
#     "age": 18,
#     "subjects": ["Maths", "CS"],
#     "is_enrolled": True
# }

# student["rollno"] = "Student roll no is 123"

# print(student)

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
# student_grades = { }

# for student in student_scores:
#     score = student_scores[student]
#     if score >= 91:
#         student_grades[student] = "Outstanding" 
#     elif 81 <= score <= 90:
#         student_grades[student] = "Exceeds Expectations"
#     elif 71 <= score <= 80:
#         student_grades[student] = "Acceptable"  
#     else:
#         student_grades[student] = "Fail" 
        
# print(student_grades)


# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

# print(travel_log["germany"]["cities_visited"][2] )

# data_of_bidders = {}
# bidders_more = True

# while bidders_more:
#     name = input("What is the name of the person?\n")
#     bid_amt = int(input("What is the BID amount?\n"))  # Convert to int for comparison
#     data_of_bidders[name] = bid_amt

#     more_bidders = input("Are more people willing to bid? Yes/No\n").lower()

#     if more_bidders == "no":
#         bidders_more = False

#         # Find highest bidder
#         highest_bidder = max(data_of_bidders, key=data_of_bidders.get)
#         amt = data_of_bidders[highest_bidder]
#         print(f"\n💰 {highest_bidder} has the highest bid of ₹{amt}.")
#     else:
#         print("\n" * 100)  # Clears the screen (basic effect)

# def name_title(f_name, l_name):
#     f_name = f_name.title()
#     l_name = l_name.title()
#     return f_name, l_name

# first, last = name_title("SuYaSh", "GuPtA")
# print(first, last)
# def calculator():
        
#     cal_value = " "
#     first_num  = float(input("Pick a number: "))
#     print("""
#     +
#     -
#     *
#     /     
#     """)
#     oper_pick = str(input("Pick a operation: "))
#     sec_num = float(input("what is the next number: "))

#     def calculation():

#         if oper_pick == "+":
#             cal_value = first_num  + sec_num
#         elif oper_pick == "-":
#             cal_value = first_num - sec_num
#         elif oper_pick == "/":
#             cal_value = first_num / sec_num
#         elif oper_pick == "*":
#             cal_value == first_num * sec_num
#         return cal_value

#     value = calculation()
#     print(value)

#     user_ask = str(input("Type 'y' to continue, or type n for new calculation: ")).lower()
#     if user_ask == "n":
#         calculation()

#     elif user_ask == "y":
#         first_num = cal_value
#         calculation()


# make a calculator- 

# def Calculation():
#     def add(n1, n2):
#         return n1 + n2
#     def subtract(n1, n2):
#         return n1 - n2
#     def divide(n1, n2):
#         return n1 / n2
#     def multiply(n1, n2):
#         return n1 * n2
    
#     old_calc = True

#     op = {
#             "+":add,
#             "-":subtract,
#             "*":multiply,
#             "/":divide
#     }
#     first = float(input("Type your number: "))
#     while old_calc:
#         for sign in op:
#             print(sign)
#         operation = str(input("Type your operation: "))
#         second = float(input(f"To which num you want to {first} {operation}: "))


#         answer = op[operation](first, second)
#         print(f"{first} {operation} {second} = {answer}")

#         choice = str(input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation. ")).lower()

#         if choice == "y":
#             first = answer
            
#         else:
#             old_calc = False
#             print("\n" * 100)
#             Calculation()  

# Calculation()

def blackJack():
    import random

    cards = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    start_game = str(input("Do you want to start the game, y/n: ")).lower()

    if start_game == "y":
        user_cards = [ ]
        computer_cards = [ ]
        def ran_card():
            return random.choice(cards)
        
        repeat = [ 1 , 2]
        for each_num in repeat:
            random_card = True
            while random_card == True:
                
                user_cards.append(int(ran_card()))
                random_card = False

        
        computer_cards.append(int(ran_card()))

        user_score = sum(user_cards)
        comp_score = sum(computer_cards)

        print(f"Your cards: {user_cards}, current score:{user_score}")
        print(f"Computer's first card: {computer_cards[-1]}")

        def restart():
                ask_user = str(input("Do u want to play again blackJack ?, y/n : ")).lower()
                if ask_user == "y":
                    print("\n" *100 )
                    blackJack()
                else:
                    return None

        def condition():
                if user_score > 21:
                    print(f"""
You went over. You lose 😭
Your final hand: {user_cards}, final score: {user_score}
Computer's final hand: {computer_cards}, final score: {comp_score} """)
                    restart()
                
                elif comp_score > 21: 
                    print(f"""
You Win 👑
Your final hand: {user_cards}, final score: {user_score}
Computer's final hand: {computer_cards}, final score: {comp_score} """)
                    restart()
                    
                
        while user_score and comp_score < 21:
            ask_for_choice = str(input("To withdraw another card, entre 'y' or if you want to pass entre 'n':")).lower()
            if ask_for_choice == "y":
                user_cards.append(ran_card())
                user_score += user_cards[-1]
                print(f"Your cards: {user_cards}, current score:{user_score}")
                print(f"Computer's first card: {computer_cards}")
                condition()

                while comp_score < 17:
                 computer_cards.append(ran_card())
                 comp_score = sum(computer_cards)


            elif ask_for_choice == "n":
                computer_cards.append(ran_card())
                comp_score += computer_cards[-1]
                print(f"Your cards: {user_cards}, current score:{user_score}")
                print(f"Computer's first card: {computer_cards[0]}")
                condition()
            

    else:
        print("Press run to restart.")

blackJack()