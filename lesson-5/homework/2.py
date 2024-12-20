def invest(amount, rate, years):
    for i in range(years):
        amount += amount * rate
    
    return amount

amount = float(input('amount: '))
rate = float(input('rate: '))
years = int(input('years: '))

print(f'overall: {invest(amount, rate / 100, years)}')