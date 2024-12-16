nums = list(map(int, input().split()))

nums.sort()

if len(nums) > 1:
    print(nums[1])