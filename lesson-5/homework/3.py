def factor(num):
    for i in range (1, num + 1):
        if num % i == 0:
            print(f'{i} is a factor of {num}')

num = int(input('number: '))

factor(num)