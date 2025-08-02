import random
player_name = "Suyash"
print(f" Welcome to the Stone paper sissor game {player_name}")


player_permission = str(input("Should we begin ? Yes/No\n")).lower()


if player_permission == "yes":
    player = int(input("what do u choose ? 1 for rock, 2 for paper and 3 for scissors! \n"))
    computer = random.randint(1,3)
    #1st Condition
    if  player == 1 and computer == 2:
        print('''  
        ,--.--._
    ------" _, \___)
            / _/____)
            \//(____)
    ------\     (__)
        `-----"
    ''')
        print(f"{player_name} have choosen rock !")
        print('''            ___..__
    __..--""" ._ __.'
                "-..__
                '"--..__";
    ___        '--...__"";
        `-..__ '"---..._;"
            """"----'     ''')
        print("computer have choosen paper !")
        print("Paper covers stone, Computer Wins !")
    #2nd Condition
    elif player == 2 and computer == 3:
        print('''            ___..__
    __..--""" ._ __.'
                "-..__
                '"--..__";
    ___        '--...__"";
        `-..__ '"---..._;"
            """"----'     ''')
        print(f"{player_name} have choosen paper !")
        print(''' .-.  _
        | | / )
        | |/ /
     _|__ /_
     / __)-' )
     \  `(.-')
     > ._>-'
     / \/

    ''' )
        print("computer have choosen scissors !")
        print("Scissors Cut paper, Computer Wins !")

    #3rd Condition
    elif  player == 3 and computer == 2:
        print(''' .-.  _
        | | / )
        | |/ /
    _|__ /_
    / __)-' )
    \  `(.-')
    > ._>-'
    / \/

    ''' )
        print(f"{player_name} have choosen scissors !")
        print('''            ___..__
    __..--""" ._ __.'
                "-..__
                '"--..__";
    ___        '--...__"";
        `-..__ '"---..._;"
            """"----'     ''')
        print("computer have choosen paper !")
        print("Scissors Cut paper, Player Wins !")

    #4th Condition
    elif player == 2 and computer == 1:
        print('''            ___..__
    __..--""" ._ __.'
                "-..__
                '"--..__";
    ___        '--...__"";
        `-..__ '"---..._;"
            """"----'     ''')
        print(f"{player_name} have choosen paper !")
        print('''  
        ,--.--._
    ------" _, \___)
            / _/____)
            \//(____)
    ------\     (__)
        `-----"
    ''')
        print("Computer have choosen rock !")
        print("Paper covers stone, Player Wins !")

    #5th Condition
    elif player == 1 and computer == 3:
        print('''  
        ,--.--._
    ------" _, \___)
            / _/____)
            \//(____)
    ------\     (__)
        `-----"
    ''')
        print(f"{player_name} have choosen rock !")
        print(''' .-.  _
        | | / )
        | |/ /
    _|__ /_
    / __)-' )
    \  `(.-')
    > ._>-'
    / \/

    ''' )
        print("Computer have choosen scissors !")
        print("Rock smashes scissors ! Player Wins ")

    #6th Condition
    elif player == 3 and computer == 1:
        print(''' .-.  _
        | | / )
        | |/ /
    _|__ /_
    / __)-' )
    \  `(.-')
    > ._>-'
    / \/

    ''' )
        print(f"{player_name} have choosen scissors !")
        print('''  
        ,--.--._
    ------" _, \___)
            / _/____)
            \//(____)
    ------\     (__)
        `-----"
    ''')
        print("Computer have choosen rock !")
        print("Rock smashes scissors ! Computer Wins ")
    elif player == computer:
        print(f"{player_name} and computer have same choice, its a tie !")
elif player_permission == "no":
    print("Refresh to play !")
else:
    print("Retry !")



        

