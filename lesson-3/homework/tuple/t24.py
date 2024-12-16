tuple_nums = tuple(map(int, input().split()))

if tuple_nums == tuple_nums[::-1]:
    print(True)
else:
    print(False)