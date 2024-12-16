tuple_nums = tuple(map(int, input().split()))
subtuple_size = int(input())

nested_tuple = tuple(tuple_nums[i:i + subtuple_size] for i in range(0, len(tuple_nums), subtuple_size))

print("Nested Tuple:", nested_tuple)