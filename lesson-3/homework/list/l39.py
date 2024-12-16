nums = list(map(int, input().split()))
sublist_size = int(input())

nested_nums = []

for i in range(0, len(nums), sublist_size):
    nested_nums.append(nested_nums[i:i + sublist_size])

print(nested_nums)
