import sys

def ending(num):
    if num == 1:
        print('        Player One Wins!        ')
    elif num == 2:
        print('        Player Two Wins!        ')
    elif num == 0:
        print('        It\'s a Tie! !        ')
        

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
    print('****** NO CHEATING!!! ******\n\n' * 20)
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
    if choice_1 == choice_2:
        ending(0)
    elif choice_1 == 'rock':
        if choice_2 == 'scissors':
            ending(1)
        elif choice_2 == 'paper':
            ending(2)    
    elif choice_1 == 'scissors':
        if choice_2 == 'rock':
            ending(2)
        elif choice_2 == 'paper':
            ending(1)
    elif choice_1 == 'paper':
        if choice_2 == 'scissors':
            ending(2)
        elif choice_2 == 'rock':
            ending(1)
    elif choice_1 == choice_2:
        ending(0)

    
