tuple_nums = tuple(map(int, input().split()))

if list(tuple_nums) == sorted(list(tuple_nums)):
    print(True)
else:
    print(False)