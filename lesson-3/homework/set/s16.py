my_set = set(map(int, input().split()))

even_numbers = {x for x in my_set if x % 2 == 0}

print(even_numbers)