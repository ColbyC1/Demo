from random import randint

def Guess():
    
    print(f'Welcome to GUESS \n')
    
    name = input('Im Bot, Whats your name? ')
    print('\n')
    print(f'Okay {name}! I am thinking of a number between 1-10 and you have 5 tries to guess it.\n')
    
    game_on = True
    computer_num = randint(0,10)
    tries = 0
    
    while game_on:
        guess = int(input('Guess: '))
        
        if guess > computer_num:
            tries+=1
            print(f'Attempt:{tries} \n\nGuess to high. Try again')
        
        if guess < computer_num:
            tries+=1
            print(f'Attempt:{tries} \n\nGuess to low. Try again')
        
        if guess == computer_num:
            tries+=1
            game_on = False
            return (f'Correct! It was {computer_num}')
        
        elif tries >= 5:
            game_on = False
            return (f'Sorry, it took you too many tries. My number was {computer_num}')
            
            
# Guess()
