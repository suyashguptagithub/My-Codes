
def blackJack():
    import random

    cards = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    start_game = str(input("Do you want to start the game, y/n: ")).lower()

    if start_game == "y":
        user_cards = [ ]
        computer_cards = [ ]
        def ran_card():
            return random.choice(cards)
        
        # repeat = [ 1 , 2]
        # for each_num in repeat:
        for _ in range(2):
            user_cards.append(int(ran_card()))
            computer_cards.append(int(ran_card()))
            # random_card = True
            # while random_card == True:
                
                # random_card = False

        

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
                if user_score >= 21:
                    print(f"""
You went over. You lose 😭
Your final hand: {user_cards}, final score: {user_score}
Computer's final hand: {computer_cards}, final score: {comp_score} """)
                    restart()
                
                elif comp_score >= 21: 
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