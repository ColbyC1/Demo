from random import randint

def RPS():
    
    print('Welcome to RPS')
    print('\n')
    
    ops = ['Rock', 'Paper', 'Scissors']
    computer_choice = ops[randint(0,2)]
    game_on = True
    
    while game_on:
        
        player_choice = input('Choose Rock, Paper, or Scissors: ')
        
        if player_choice not in ops or player_choice.isdigit():
            print(f'{player_choice} is not an option')
            print('\n')
            
        else:
            print(f'Player choice: {player_choice}')
            print(f'Computer choice: {computer_choice}')
            print('\n')
        
        if player_choice == 'Rock':
            if computer_choice == 'Scissors':
                print('Player Wins, Rock > Scissors')
                game_on = False
                
            if computer_choice == 'Paper':
                print('Computer Wins, Paper > Rock')
                game_on = False
                
            elif computer_choice == player_choice:
                print('Draw, Rock = Rock')
                game_on = True
                
        if player_choice == 'Paper':
            if computer_choice == 'Scissors':
                print('Computer Wins, Paper < Scissors')
                game_on = False
                
            if computer_choice == 'Rock':
                print('Player Wins, Paper > Rock')
                game_on = False
            
            elif computer_choice == player_choice:
                print('Draw, Paper = Paper')
                game_on = True
                
        if player_choice == 'Scissors':
            if computer_choice == 'Rock':
                print('Computer Wins, Rock > Scissors')
                game_on = False
                
            if computer_choice == 'Paper':
                print('Player Wins, Scissors > Paper')
                game_on = False
            
            elif computer_choice == player_choice:
                print('Draw, Scissors = Scissors')
                game_on = True
        

    while game_on == False:
        keep_playing = input('Would you like to play again (Yes/No)? ')
        
        if keep_playing != 'Yes' and keep_playing != 'No':
            print(f'{keep_playing} is not an option')
            
        if keep_playing == 'Yes':
            game_on = True
            RPS()
                
        if keep_playing == 'No':
            return('Thanks for playing!')
            game_on = False

# RPS()
