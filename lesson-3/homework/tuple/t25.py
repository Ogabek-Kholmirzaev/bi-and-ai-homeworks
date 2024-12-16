tuple_nums = tuple(map(int, input().split()))

unique_tuple = tuple(dict.fromkeys(tuple_nums))

print(unique_tuple)
