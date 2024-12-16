my_set = set(map(int, input().split()))

odd_numbers = {x for x in my_set if x % 2 != 0}

print(odd_numbers)