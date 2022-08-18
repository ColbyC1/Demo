def mort_calc():
    
    mortgage = int(input('How much was your mortgage loan? '))
    years = int(input('How many years do you have to pay it off? '))
    interest = int(input('How high/low was the interest? '))*.01
    
    mo_int = interest/12
    total_mo = years*12
    
    top = mo_int*((1+mo_int)**total_mo)
    bottom = ((1+mo_int)**total_mo)-1
    form = top/bottom
    
    mo_payments = float(round(mortgage*form))
    
    return(f'Monthly Payments: ${mo_payments}')
