nums = list(map(int, input().split()))
nums_sublist = list(map(int, input().split()))

found = False

for i in range(len(nums) - len(nums_sublist) + 1):
    if nums[i:i+len(nums_sublist)] == nums_sublist:
        found = True
        break

print(found)