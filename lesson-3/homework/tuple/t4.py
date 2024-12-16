tuple_nums = tuple(map(int, input().split()))
element = int(input())

found = False

for num in tuple_nums:
    if num == element:
        found = True
        break

print(found)