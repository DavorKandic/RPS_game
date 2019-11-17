import sys
from random import choice as rch

def ending(num):
    global opponent
    if num == 1:
        print('        Player One Wins!        ')
    elif num == 2:
        if opponent == '1':
            print('        Player Two Wins!        ')
        else:
            print('         Computer Wins!         ')
    elif num == 0:
        print('        It\'s a Tie! !          ')


def compy():
    return rch(valid_moves[:3])


def close():
    print()
    print('Bye-bye!')
    print()
    sys.exit()


def wrong():
    print('    -----#######################-----     ')
    print('  -----######__Wrong input!__#####------  ')
    print('    -----#######################-----     ')


def cheat_block():
    print('****** NO CHEATING!!! ******\n\n' * 20)
        

print('...rock...')
print('...paper...')
print('...scissors...')
print()
while True:
    valid_moves = ['rock', 'paper', 'scissors', 'r', 'p', 's']
    valid_dict = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    while True:
        print('Enter 1 if you want to play against human, or 2 to play vs computer:')
        print('If you want to quit just enter "q"...')
        opponent = input()
        if opponent == '1' or opponent == '2' or opponent == 'q':
            break
        else:
            wrong()
    if opponent == 'q':
        close()
    print('You can enter: "rock" or "r",\n"paper" or "p",\n"scissors" or "s"...')
    print('If you want to quit just enter "q"...')
    choice_1 = None
    while choice_1 not in valid_moves:
        choice_1 = input('Player One, enter your choice: ').lower()
        if choice_1 == 'q':
            close()
        if choice_1 not in valid_moves:
            wrong()
    if choice_1 in valid_dict.keys():
        choice_1 = valid_dict[choice_1]  
    cheat_block()
    choice_2 = None
    if opponent == '2':
        choice_2 = compy()
    else:
        while choice_2 not in valid_moves:
            choice_2 = input('Player Two, enter your choice: ').lower()
            if choice_2 == 'q':
                close()
            if choice_2 not in valid_moves:
                wrong()
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

    
