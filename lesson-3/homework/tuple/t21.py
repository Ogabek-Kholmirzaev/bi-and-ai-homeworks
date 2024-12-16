tuple_nums = tuple(map(int, input().split()))
repeat_times = int(input())

new_tuple = tuple([element for element in tuple_nums for _ in range(repeat_times)])

print(new_tuple)