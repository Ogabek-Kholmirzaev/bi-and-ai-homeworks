tuple_nums = tuple(map(int, input().split()))
element = int(input())

temp_list = list(tuple_nums)
temp_list.remove(element)
new_tuple = tuple(temp_list)

print(new_tuple)