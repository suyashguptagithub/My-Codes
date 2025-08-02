
import random
words = ["engine"]

chosen_word = random.choice(words)
print("Chosen word has", len(chosen_word), "letters.")

display = "_" * len(chosen_word)

while display != chosen_word:
    print("Current word:", display)
    user_input = input("Guess a letter: ").lower()
    user_life = 6
    new_display = ""
    if user_life > 0:
        for index in range(len(chosen_word)):
            if chosen_word[index] == user_input:
                new_display += user_input
            else:
                new_display += display[index]
                user_life -= 1 
        display = new_display
    else:
        print("You lose ! :(")
    

print("Congratulations! You guessed the word:", chosen_word)


