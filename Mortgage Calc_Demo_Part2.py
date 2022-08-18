import pandas as pd
import numpy_financial as npf
import numpy as np
from datetime import date

def Mortgage_Sheet():
    
    mortgage = int(input('How much is your mortgage loan? '))
    interest = int(input('How high/low was the interest (Do not include "." or "%")? '))*.01
    years = int(input('How many years do you have to pay it off? '))
    payments_per_year = int(input('How many payments per year? '))
    start_date = input('When did you begin payments (YYYY-MM-DD)? ')

    rng = pd.date_range(start_date, periods=years*payments_per_year, freq='MS')
    rng.name = 'Payment Date'
    
    df = pd.DataFrame(index=rng, columns=['Beginning Balance', 'Payment', 'Principal Paid', 'Interest Paid', 'Ending Balance', 'Cumulative Interest'], dtype='float')
    
    df.reset_index(inplace=True)
    df.index+=1
    df.index.name = 'Period'
    
    df['Payment'] = -1*npf.pmt(interest/12, years*12,mortgage)
    df['Principal Paid'] = -1*npf.ppmt(interest/12,df.index,years*12,mortgage)
    df['Interest Paid'] = -1*npf.ipmt(interest/12,df.index,years*12,mortgage)

    df.loc[1,'Beginning Balance'] = mortgage
    df.loc[1, 'Ending Balance'] = mortgage-(df.loc[1, 'Principal Paid'])
    df.loc[1, 'Cumulative Interest'] = df.loc[1, 'Interest Paid']

    df = df.round(2)
    
    for period in range(2, len(df)+1):
        
        prev_balance = df.loc[period-1, 'Ending Balance']
        cur_principal = df.loc[period, 'Principal Paid']
    
        df.loc[period, 'Ending Balance'] = prev_balance-cur_principal
    
        df.loc[period, 'Beginning Balance'] = df.loc[period-1, 'Ending Balance']
    
        if df.loc[period, 'Ending Balance'] == 0:
            break
            
        prev_cuml = df.loc[period-1, 'Cumulative Interest']
        cur_int_paid = df.loc[period,'Interest Paid']
    
        df.loc[period,'Cumulative Interest'] = prev_cuml+cur_int_paid
    
    return df

# Mortgage_Sheet()
