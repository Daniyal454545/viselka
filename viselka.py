import random
def viselka():
    print('привет ты готов сыграть в игру?')
    words = ['apple', 'thunder', 'women', 'flash', 'superman', 'batman', 'spiderman', 'ironman']
    secret = random.choice(words)
    glass = 'aoyuei'
    turns = 5
    while turns > 0:
        missed = 0
        for i in secret:
            if i in glass:
                print(i, end=' ')
            else:
                print('_', end='')
                missed += 1
        if missed == 0:
            print('\n you win')
            break
        gues = input('\n назови букву')
        glass += gues
        if gues not in secret:
            turns -= 1
            print('не угадал!', turns)
            if turns < 5: print('\n |' )
            if turns < 4: print(  'O' )
            if turns < 3: print(' /|\ ' )
            if turns < 2: print(  '|' )
            if turns < 1: print(  '/\ ' )
            if turns == 0: print( f'\n это слово {secret} ' )
end = 'yes'
while end == 'yes':
        viselka()
        print('do you want continue?')
        end = input()