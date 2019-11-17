import sys

print('...rock...')
print('...paper...')
print('...scissors...')
print()
while True:
    valid_moves = ['rock', 'paper', 'scissors', 'r', 'p', 's']
    valid_dict = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    print('You can enter: "rock" or "r",\n"paper" or "p",\n"scissors" or "s"...')
    print('If you want to quit just enter "q"...')
    choice_1 = None
    while choice_1 not in valid_moves:
        choice_1 = input('Player One, enter your choice: ')
        if choice_1 == 'q':
            print()
            print('Bye-bye!')
            print()
            sys.exit()
        if choice_1 not in valid_moves:
            print('  -----######__Wrong input!__#####------  ')
    if choice_1 in valid_dict.keys():
        choice_1 = valid_dict[choice_1]
        
    for i in range(10):
        print('****** NO CHEATING!!! ******')
        print()
        print('****** NO CHEATING!!! ******')
        print()
    choice_2 = None
    while choice_2 not in valid_moves:
        choice_2 = input('Player Two, enter your choice: ')
        if choice_2 == 'q':
            print()
            print('Bye-bye!')
            print()
            sys.exit()
        if choice_2 not in valid_moves:
            print('  -----######__Wrong input!__#####------  ')
    if choice_2 in valid_dict.keys():
        choice_2 = valid_dict[choice_2]
    print('          SHOOT!          ')
    if choice_1 == 'rock' and choice_2 == 'scissors':
        print('        Player One Wins!        ')
    elif choice_1 == 'scissors' and choice_2 == 'rock':
        print('        Player Two Wins!        ')
    elif choice_1 == 'paper' and choice_2 == 'scissors':
        print('        Player Two Wins!        ')
    elif choice_1 == 'scissors' and choice_2 == 'paper':
        print('        Player One Wins!        ')
    elif choice_1 == 'paper' and choice_2 == 'rock':
        print('        Player One Wins!        ')
    elif choice_1 == 'rock' and choice_2 == 'paper':
        print('        Player Two Wins!        ')
    elif choice_1 == choice_2:
        print('        It\'s a DRAW! !        ')

    
