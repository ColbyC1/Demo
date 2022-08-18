from random import randint

def Coin_Flips():
    
    coin = ['Heads','Tails']

    count = 0
    h_count = 0
    t_count = 0
    flip_list = []
    
    flips = int(input('How many times should i flip this coin (Must be int)? '))
    print('\n')
    
    while count < flips:
        flip = coin[randint(0,1)]
        
        if flip == 'Heads':
            h_count+=1
            count+=1
            flip_list.append(flip)
        
        elif flip == 'Tails':
            t_count+=1
            count+=1
            flip_list.append(flip)
    
    print(f'Out of {flips} flips you get: \n\nHeads: {h_count} Tails: {t_count} \nListing: {flip_list}')
    
# Coin_Flips()    
