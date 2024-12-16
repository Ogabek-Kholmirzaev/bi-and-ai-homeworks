tuple_nums = tuple(map(int, input().split()))
element = int(input())

indices = []

for i in range(len(tuple_nums)):
    if tuple_nums[i] == element:
        indices.append(i)

print(indices)