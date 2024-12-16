nums = list(map(int, input().split()))
element = int(input())

indices = []

for i in range(len(nums)):
    if nums[i] == element:
        indices.append(i)

print(indices)